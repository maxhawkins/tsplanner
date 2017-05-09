import os
import random
import time
import tornado.ioloop
import tornado.web
import json

import evaluator
import routing

class RouteHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()

    def post(self):
        req = json.loads(self.request.body)
        nodes = req['nodes']
        if len(nodes) < 2:
            self.clear()
            self.set_status(400)
            self.finish('must have at least two nodes')
            return

        win_start = req['startTime']
        win_end = req['endTime']
        window = routing.TimeRange(win_start, win_end)

        start = req['start']
        if not ('lat' in start and 'lng' in start):
            self.clear()
            self.set_status(400)
            self.finish('start must have lat and lng')
            return
        nodes = [start] + nodes

        # HACK(maxhawkins): ORTools requires the depot to
        # be open at the start and end of our journey. Just
        # set its open/close time toa  really huge range for now.
        nodes[0]['start'] = -1e10
        nodes[0]['end'] = 1e10

        for node in nodes:
            if 'lat' not in node or 'lng' not in node:
                self.clear()
                self.set_status(400)
                self.finish('each node must have lat and lng')
                return

            # HACK(maxhawkins): eventually we should support nodes
            # that don't have open/close times using single-sided
            # inequalities in the optimization code. For now, just
            # give these nodes a really huge time window.
            if 'start' not in node or node['start'] is None:
                node['start'] = -1e10
            if 'end' not in node or node['end'] is None:
                node['end'] = node['start'] + 60 * 60

        route = routing.solve(nodes, window, evaluator.Haversine)
        for step in route:
            step['node'] = nodes[step['node_idx']]

        result = {'results': route}
        js = json.dumps(result, indent=2)

        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Content-Type', 'application/json')
        self.write(js)

def make_app():
    settings = {
        'debug': True,
        'static_path': os.path.join(os.path.dirname(__file__), 'static')
    }
    handlers = [
        (r"/routes", RouteHandler),
        (
            r"/(.*)",
            tornado.web.StaticFileHandler,
            {
                'path': settings['static_path'],
                'default_filename': 'index.html',
            },
        ),
    ]
    return tornado.web.Application(handlers, **settings)

def main():
    app = make_app()
    port = 8000
    print 'listening at :%d' % (port)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
