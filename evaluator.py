from math import radians, cos, sin, asin, sqrt

# Source:
# http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine_m(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371000 # Radius of earth in meters. Use 3956 for miles
    return c * r

class Haversine(object):
    '''Evaluator that computes weights using the
    haversine distance between each of the points
    in the route.'''
    def __init__(self, nodes):
        self.nodes = nodes
    def dist(self, origin_idx, dest_idx):
        origin = self.nodes[origin_idx]
        dest = self.nodes[dest_idx]
        dist_m = haversine_m(
            origin['lng'], origin['lat'],
            dest['lng'], dest['lat'],
        )
        return dist_m
    def service_time(self, node_idx):
        return 60 * 30
    def travel_time(self, origin_idx, dest_idx):
        dist_m = self.dist(origin_idx, dest_idx)
        rate = 2 # m/s
        duration = dist_m / rate
        return duration
