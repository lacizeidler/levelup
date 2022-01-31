from tkinter import CASCADE
from django.db import models 

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    description = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=CASCADE)