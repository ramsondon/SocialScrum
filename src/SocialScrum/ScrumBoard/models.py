from django.db import models
import datetime

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
    


class Task(models.Model):
    story = models.ForeignKey(Story)
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
    
    def in_progress(self):
        today = datetime.datetime.today()
        return  (today >= self.start and today <= self.end) 
    in_progress.short_description = 'In Progress?'
