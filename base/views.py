from django.shortcuts import render
from .models import Clergy, Event,TodaysDate, Gallery

# Create your views here.
def index(request):
  events = Event.objects.all()
  todaysdate = TodaysDate.objects.get(id = 1)
  todaysdate.name = 'today'
  todaysdate.save()
  for event in events:    
    if event.Date.month  == todaysdate.date.month:
     i = -1
     if event.Date.day >= todaysdate.date.day:
       upcoming = event
       context = {'upcoming': upcoming, 'today': todaysdate}
       return render(request, 'index.html',context)          
  return render(request, 'index.html')


def sotik(request):
  name = 'SOTIK'
  context = {'name': name}
  return render(request, 'Sotikarchdeaconary.html',context)

def kericho(request):
  name = 'KERICHO'
  context = {'name': name}
  return render(request, 'kerichoarchdeaconary.html',context)

def narok(request):
  name = 'NAROK'
  context = {'name': name}
  return render(request, 'Narok.html',context)

def transmara(request):
  name = 'TRANSMARA'
  context = {'name': name}
  return render(request, 'kilgoris.html',context)

def cathedral(request):
  events = Event.objects.all()
  todaysdate = TodaysDate.objects.get(id = 1)
  todaysdate.name = 'today'
  todaysdate.save()
  for event in events:    
    if event.Date.month  == todaysdate.date.month:
     i = -1
     if event.Date.day >= todaysdate.date.day:
       upcoming = event
       for event in events:
         if upcoming.Date < event.Date:
          next = event           
          context = {'upcoming': upcoming , 'next': next}
          return render(request, 'cathedral.html',context)
  return render(request, 'cathedral.html')

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