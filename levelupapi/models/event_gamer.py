from tkinter import CASCADE
from django.db import models

class EventGamer(models.Model): 
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE)
    event = models.ForeignKey("Event", on_delete=CASCADE)