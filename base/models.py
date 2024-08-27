from django.db import models

# Create your models here.
class Event(models.Model):
  Date = models.DateField()
  EventName = models.CharField( max_length= 200)
  OrganisingDept = models.CharField( max_length= 200)
  venue = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    return self.EventName

class Clergy(models.Model):
  Name = models.CharField(max_length= 200)
  Tittle = models.CharField(max_length= 200)
  Post = models.CharField(max_length= 200 , null=True)
  Image  = models.ImageField(null=True,default='profile.jpg')
  url = models.CharField(max_length=200, null=True)  
  
  def __str__(self):
    return self.Name

class TodaysDate(models.Model):
  name = models.CharField(max_length=200, null= True)
  id = models.CharField(max_length=200,primary_key=True)
  date = models.DateField(auto_now= True)
  
class Gallery(models.Model):
  description = models.CharField(max_length=255, null= True)
  Image = models.ImageField(default='kericho.png')
  
  def __str__(self):
    return self.description
  
# class Verse(models.Model):
#   Verse = models.CharField(max_length=200,null=False)
#   cont = models.CharField(max_length=200, null=False)
  
#   def __str__(self):
#     return self.Verse