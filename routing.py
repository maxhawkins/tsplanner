from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

TIME_KEY = "Time"

INT64_MAX = 1 << 63

class TimeRange(object):
    '''
    The ORTools code has problems when the values for
    the time dimension get too large. To prevent this,
    each node's start and end time is calculated as an
    offset from the solver's time window. This class puts
    all of those time calculations in one place.
    '''
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def duration(self):
        return int(self.end - self.start)
    def to_relative(self, t):
        return int(t - self.start)
    def to_absolute(self, t):
        return int(t + self.start)

def solve(nodes, time_range, evaluator_factory):
    '''
    Run a vehicle routing problem with time windows optimization on the
    provided nodes.

    Parameters
    ----------
    nodes : array of nodes
        points to route between
    time_range : TimeRange
        the time range within which the solution can lie
    evaluator_factory: Evaluator
        the evaluator class used to calculate the distance between
        points in the input

    Returns
    -------
    results - array of routing results
        An index, start time, and end time for each node in the solution
    '''
    if len(nodes) < 2:
        raise ValueError("must have at least two nodes")

    depot = nodes[0]
    if time_range.to_relative(depot['end']) < 0 or time_range.to_relative(depot['start']) > 0:
        raise ValueError('depot (first node) must be available at the start of the given time interval')

    for node in nodes:
        if node['start'] > INT64_MAX:
            raise ValueError('node start must fit in a 64bit int')
        if node['end'] > INT64_MAX:
            raise ValueError('node end must fit in a 64bit int')

    if time_range.duration() < 0:
        raise ValueError('invalid time range: start must be before end')

    routing = pywrapcp.RoutingModel(len(nodes), 1, 0)

    parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    parameters.time_limit_ms = 20000

    evaluator = evaluator_factory(nodes)

    cost_func = evaluator.travel_time
    routing.SetArcCostEvaluatorOfAllVehicles(cost_func)

    def travel_plus_service_time(origin_idx, dest_idx):
        travel = evaluator.travel_time(origin_idx, dest_idx)
        service = evaluator.service_time(origin_idx)
        return travel + service
    time_func = travel_plus_service_time
    routing.AddDimension(time_func,
        time_range.duration(), time_range.duration(),
        True, TIME_KEY)

    time_dim = routing.GetDimensionOrDie(TIME_KEY)
    time_dim.CumulVar(0).SetRange(0, time_range.duration())

    for i, node in enumerate(nodes):
        start = time_range.to_relative(node['start'])
        end = time_range.to_relative(node['end'])

        if start > time_range.duration():
            # TODO(maxhawkins): if the event happens after
            # our time window we want to remove it from
            # consideration. Does doing this remove it or is
            # it possible to match if t == time_range.end?
            time_dim.CumulVar(i).SetRange(
                time_range.duration(), time_range.duration())
        elif end < 0:
            time_dim.CumulVar(i).SetRange(
                0, 0)
        else:
            time_dim.CumulVar(i).SetRange(start, end)

        routing.AddDisjunction([i], 100000)

    assignment = routing.SolveWithParameters(parameters)

    if not assignment:
        return []

    route_number = 0
    node_id = routing.Start(route_number)
    results = []
    while not routing.IsEnd(node_id):
        arrival = time_dim.CumulVar(node_id)
        start = time_range.to_absolute(assignment.Min(arrival))

        service_time = evaluator.service_time(
            routing.IndexToNode(node_id))
        end = start + service_time

        node = nodes[node_id]
        result = {
            'node_idx': node_id,
            'start': start,
            'end': end,
        }
        results.append(result)

        node_id = assignment.Value(routing.NextVar(node_id))

    if len(results) < 2:
        return results

    last_end = results[-1]['end']
    time_to_depot = evaluator.travel_time(
        routing.IndexToNode(node_id), 0)
    finish_time = last_end + time_to_depot
    results.append({
        'node_idx': 0,
        'start': finish_time,
        'end': finish_time,
    })

    return results
