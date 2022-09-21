from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'movie_list': data_mywatchlist,
        'nama': 'Naila Azizah',
        'npm': '2106705814'
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
