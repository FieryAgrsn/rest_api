from api.models import Bet, Event, User
from api.serializers import BetSerializer, EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import UserSerializer
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.auth import Authentication



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BetHighlight(generics.GenericAPIView):
    queryset = Bet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        bet = self.get_object()
        return Response(bet.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bets': reverse('bet-list', request=request, format=format)
    })

class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer



class BetViewSet(viewsets.ModelViewSet):

    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        bet = self.get_object()
        return Response(bet.highlighted)


    def perform_create(self, serializer):
        bet_event = Event.objects.get(text=self.request.data.get('code'))
        if(self.request.data.get('selected_team') == bet_event.Team_1):
            bet_size = float(self.request.data.get('size_of_bet'))
            author = self.request.user
            t1 = bet_event.Team_1_bets
            bet_size += t1
            Event.objects.filter(text = self.request.data.get('code')).update(Team_1_bets = bet_size)
            tmp_user = User.objects.get(username=author)
            usr_money = tmp_user.money - t1
            User.objects.filter(username=self.request.user.username).update(money=usr_money)
        serializer.save(owner=self.request.user, event=bet_event)




