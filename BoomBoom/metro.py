import copy

from .models import Congestion
from .stations import get_stations


class Metro:
    routing = {}
    stations = {}

    def __init__(self, stations: get_stations(), timestamp) -> None:
        super().__init__()
        self.stations = stations
        self.timestamp = timestamp

    def find_path(self, _from, _to):
        self.routing = {}
        for station in self.stations.keys():
            self.routing[station] = {'shortestDist': 0, 'route': [], 'visited': 0}
        self.visit_place(_from)
        while 1:
            min_dist = max(self.routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
            to_visit = ''
            for name, search in self.routing.items():
                if 0 < search['shortestDist'] <= min_dist and not search['visited']:
                    min_dist = search['shortestDist']
                    to_visit = name
            if to_visit == '':
                break
            self.visit_place(to_visit)
        return self.routing[_to]['route']

    def visit_place(self, visit):
        self.routing[visit]['visited'] = 1
        for to_go, betweenDist in self.stations[visit]["links"].items():
            try:
                cong = Congestion.objects.get(
                    _from=visit,
                    _to=to_go,
                    timestamp=self.timestamp,
                ).cong
            except:
                cong = 0
            self.stations[visit]["links"][to_go] = cong
            to_dist = self.routing[visit]['shortestDist'] + cong
            if (self.routing[to_go]['shortestDist'] >= to_dist) or not self.routing[to_go]['route']:
                self.routing[to_go]['shortestDist'] = to_dist
                self.routing[to_go]['route'] = copy.deepcopy(self.routing[visit]['route'])
                self.routing[to_go]['route'].append(visit)
