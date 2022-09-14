from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog_item,
        'nama': 'Naila Azizah',
        'studentid': '2106705814'

    }
    return render(request, "katalog.html", context)

