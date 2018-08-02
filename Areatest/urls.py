
from django.conf.urls import include, url
from django.contrib import admin
from Areatest import views



urlpatterns = [
    url(r'^area$',views.area),
    url(r'^prov$',views.prov),
    url(r'^city(\d+)$',views.city),
    url(r'^dis(\d+)$',views.city),
]
