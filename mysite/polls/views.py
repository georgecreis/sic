from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
import datetime
import folium

coord = [-13.0052932,-38.5326853]

def index(request):
    my_map = folium.Map(location=coord,tiles='Stamen Terrain',zoom_start=12) 
    for evt in Event.objects.all():
        folium.Marker(
          location=[evt.longitude, evt.latitude],
          popup="%s\r\n%s/%s/%s - %02d:%02d" % (evt.name,evt.time.day,evt.time.month,evt.time.year,evt.time.hour,evt.time.minute),
          icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(my_map)
    return HttpResponse(my_map._repr_html_())

def api(request):
    name      = request.GET['name']
    uid       = request.GET['uid']
    latitude  = request.GET['lat']
    longitude = request.GET['long']

    new_entry = Event(name=name, uid=uid, latitude=latitude,longitude=longitude)
    new_entry.save()    

 
    return HttpResponse("add OK")

def getDB(request):
   query_results = Event.objects.all()
   return HttpResponse(query_results)
