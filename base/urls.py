from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
  path('',  views.index, name= 'home'),
  path('SotikArchdeaconary/',views.sotik, name= 'sotik'),
  path('KerichoArchdeaconary/',views.kericho, name= 'kericho'),
  path('NarokArchdeaconary/',views.narok, name= 'narok'),
  path('TransmaraArchdeaconary/',views.transmara, name= 'transmara'),
  path('cathedral/', views.cathedral, name= 'cathedral'),
  path('clergy/',views.clergy, name='clergy'),  
  path('events/',views.Events, name='events'),  
  path('kama/',views.kama, name='kama'),
  path('mu/',views.mu, name='mu'),
  path('kayo/',views.kayo, name='kayo'),
  path('sundayschool/',views.sschool, name='sschool'),
  path('ackkcodiocschools/',views.school, name='schools'),
  path('gallery/',views.gallery, name='gallery'),
]
