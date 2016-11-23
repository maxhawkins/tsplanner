import unittest

import routing

class StubEvaluator(object):
    def __init__(self, service, travel):
      self._service_time = service
      self._travel_time = travel
    def __call__(self, nodes):
      return self
    def service_time(self, idx):
      return self._service_time
    def travel_time(self, origin_idx, dest_idx):
      return self._travel_time

class RoutingTests(unittest.TestCase):

  def test_routing_skip_middle(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 1, 'end': 2},
      {'lat': 0, 'lng': 0, 'start': 2, 'end': 3},
      {'lat': 0, 'lng': 0, 'start': 3, 'end': 4},
    ]
    window = routing.TimeRange(1, 5)
    evaluator = StubEvaluator(service=1, travel=1)

    got = routing.solve(nodes, window, evaluator)
    want = [
      {'start': 1, 'end': 2, 'node_idx': 0},
      {'start': 3, 'end': 4, 'node_idx': 2},
      {'start': 5, 'end': 5, 'node_idx': 0},
    ]

    self.assertEquals(got, want)

  def test_event_starts_after_window_end(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 1, 'end': 2},
      {'lat': 0, 'lng': 0, 'start': 12, 'end': 13},
    ]
    window = routing.TimeRange(1, 11)
    
    got = routing.solve(nodes, window, StubEvaluator(1, 1))
    want = [
      {'start': 1, 'end': 2, 'node_idx': 0},
    ]

    self.assertEquals(got, want)

  def test_event_starts_before_window_start(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 1, 'end': 2},
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 0},
    ]
    window = routing.TimeRange(1, 3)
    
    got = routing.solve(nodes, window, StubEvaluator(1, 1))
    want = [
      {'start': 1, 'end': 2, 'node_idx': 0},
    ]

    self.assertEquals(got, want)

  def test_large_depot_time_range(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': -1e9, 'end': 1e9},
      {'lat': 0, 'lng': 0, 'start': 10, 'end': 10},
    ]
    window = routing.TimeRange(1, 10)
    
    got = routing.solve(nodes, window, StubEvaluator(1, 1))
    want = [
      {'start': 1, 'end': 2, 'node_idx': 0},
    ]

    self.assertEquals(got, want)

  def test_depot_end_before_window_start_raises(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': -500, 'end': -500},
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 0},
    ]
    window = routing.TimeRange(0, 1)
    
    with self.assertRaises(ValueError):
      routing.solve(nodes, window, StubEvaluator(1, 1))

  def test_depot_after_window_start_raises(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 500, 'end': 1000},
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 0},
    ]
    window = routing.TimeRange(0, 1)

    with self.assertRaises(ValueError):
      routing.solve(nodes, window, StubEvaluator(1, 1))

  def test_bad_time_range_raises(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 1},
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 1},
    ]
    window = routing.TimeRange(1, 0)
    
    with self.assertRaises(ValueError):
      routing.solve(nodes, window, StubEvaluator(1, 1))

  def test_int64_range_for_time_vars(self):
    nodes = [
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 0},
      {'lat': 0, 'lng': 0, 'start': 0, 'end': 1e99},
    ]
    window = routing.TimeRange(0, 1)

    with self.assertRaises(ValueError):
      routing.solve(nodes, window, StubEvaluator(1, 1))

if __name__ == '__main__':
    unittest.main()