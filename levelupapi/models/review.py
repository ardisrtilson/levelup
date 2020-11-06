from django.db import models

class Review(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    submitter = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    review = models.CharField(max_length=50)