from django.shortcuts import render
from Areatest.models import AreaInfo
from django.http import JsonResponse
# Create your views here.


def area(request):
    return render(request,"area.html")


def prov(request):
    area_prov=AreaInfo.objects.filter(aParent__isnull=True)
    print (area_prov)
    provlist=[]
    for area in area_prov:
        provlist.append((area.id,area.atitle))

    return JsonResponse({"data":provlist})



def city(request,pid):
    area_city=AreaInfo.objects.filter(aParent__id=pid)
    citylist = []
    for area in area_city:
        citylist.append((area.id, area.atitle))

    return JsonResponse({"data": citylist})


