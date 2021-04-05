from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from BoomBoom.metro import Metro
from BoomBoom.models import Congestion
from BoomBoom.stations import get_stations

# Create your views here.


class SearchUncrowdedRouteView(APIView):

    def get(self, request, *args, **kwargs):
        querystring = request.GET
        stations = get_stations()
        if querystring.get("departureTime") == "":
            timestamp = timezone.localtime().strftime("%Y-%m-%d %H:00:00+0900")
        else:
            timestamp = f"{timezone.localtime().strftime('%Y-%m-%d')} {querystring.get('departureTime')}"

        _from = int(querystring.get("from"))
        _to = int(querystring.get("to"))
        metro = Metro(stations, timestamp)
        routes = metro.find_path(_from, _to)
        routes.append(_to)
        context = {
            "routes": routes,
            "congestions": [stations[routes[i]]["links"][routes[i + 1]] for i in range(len(routes) - 1)],
        }
        return Response(context, status=status.HTTP_200_OK)
