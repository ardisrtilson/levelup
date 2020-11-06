from django.db import models

class Image(models.Model):

    name = models.CharField(max_length=50)
    imgURL = models.CharField(max_length=50)
    sumbitter = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)