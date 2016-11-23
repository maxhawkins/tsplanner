tsplanner
=========

A web service for solving time-window vehicle routing problems.

Give it a list of where and when events are happening near you.
It returns a schedule that you can follow that minimizes wasted
travel time between event locations while ensuring you see as
many events as possible.

There's a web ui where you can preview the results on a map, but
it's really meant to be used as the backend to a larger web application.

This is a thin web service wrapper on the Google ORTools
library's vehicle routing problem code.
