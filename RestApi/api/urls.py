from api.views import BetViewSet, UserViewSet, api_root, EventViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from django.conf.urls import url, include

bet_list = BetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
bet_detail = BetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
bet_highlight = BetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list',
    'post' : 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
event_list = EventViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})
event_detail = BetViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})
urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^bets/$', bet_list, name='bet-list'),
    url(r'^bets/(?P<pk>[0-9]+)/$', bet_detail, name='bet-detail'),
    url(r'^bets/(?P<pk>[0-9]+)/highlight/$', bet_highlight, name='bet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^events/$', event_list, name='event-list'),
    url(r'^events/(?P<pk>[0-9]+)/$', event_detail, name='event-detail'),
])