from django.urls import path
from mywatchlist.views import mywatchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', mywatchlist, name='mywatchlist'),
    path('html/', mywatchlist, name='mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]