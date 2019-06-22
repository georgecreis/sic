from django.db import models

class Event(models.Model):
    name      = models.CharField(max_length=200)
    uid       = models.CharField(max_length=20)
    latitude  = models.FloatField(default=0)
    longitude = models.FloatField()
    time      = models.DateTimeField(auto_now=True)    
 
    def __str__(self):
        return self.name +' '+ self.uid +' ['+str(self.latitude)+','+str(self.longitude)+']\r\n'
