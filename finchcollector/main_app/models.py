from django.db import models
from django.urls import reverse

class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/finches/' + str(self.id)

class Habitat(models.Model):
    location = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return self.location

