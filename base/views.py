from django.shortcuts import render
from .models import Clergy, Event,TodaysDate, Gallery
from .events import events

# Create your views here.
def index(request):
  context = events()  
  return render(request, 'index.html', context)


def sotik(request):
  name = 'SOTIK'
  todaysdate = TodaysDate.objects.get(id = 1)
  context = {'name': name, 'todaysdate': todaysdate}
  return render(request, 'Sotikarchdeaconary.html',context)

def kericho(request):
  name = 'KERICHO'
  todaysdate = TodaysDate.objects.get(id = 1)
  context = {'name': name, 'todaysdate': todaysdate}
  return render(request, 'kerichoarchdeaconary.html',context)

def narok(request):
  name = 'NAROK'
  todaysdate = TodaysDate.objects.get(id = 1)
  context = {'name': name, 'todaysdate': todaysdate}
  return render(request, 'Narok.html',context)

def transmara(request):
  name = 'TRANSMARA'
  todaysdate = TodaysDate.objects.get(id = 1)
  context = {'name': name, 'todaysdate': todaysdate}
  return render(request, 'kilgoris.html',context)

def cathedral(request):
  context = events()
  return render(request, 'cathedral.html', context)

def clergy(request):
  clergy = Clergy.objects.all()
  context = { 'clergy': clergy}
  return render(request, 'clergy.html' , context)

def Events(request):
  events  = Event.objects.all()
  todaysdate = TodaysDate.objects.get(id = 1)
  todaysdate.name = 'today'
  todaysdate.save()
  context = {'events': events,'today': todaysdate}
  return render(request, 'events.html', context)

def kama(request):
  return render(request, 'kama.html')

def mu(request):
  return render(request, 'MU.html')

def kayo(request):
  return render(request, 'kayo.html')

def sschool(request):
  return render(request, 'sschool.html')

def school(request):
  return render(request, 'schools.html')

def gallery(request):
  images = Gallery.objects.all()
  context = { 'images': images}
  return render(request , 'gallery.html', context)