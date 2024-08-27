from .models import Event,TodaysDate

def events():
  events = Event.objects.all()
  todaysdate = TodaysDate.objects.get(id = 1)
  todaysdate.name = 'today'
  todaysdate.save()
  for event in events:   
    if event.Date >= todaysdate.date:
      upcoming = event
      for event in events:
        if upcoming.Date <= event.Date and event != upcoming:
          next = event 
          context = {'upcoming': upcoming , 'next': next ,"todaysdate": todaysdate}
          return context
