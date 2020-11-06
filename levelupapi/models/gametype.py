from django.db import models

class gameType(models.Model):

    label = models.CharField(max_length=50)