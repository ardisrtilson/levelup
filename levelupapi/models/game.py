from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("gameType", on_delete=models.CASCADE)
    number_of_players = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)

                "title": "Settlers of Catan",
            "maker": "Klaus Teuber",
            "gamer": 1,
            "gametype": 1,
            "number_of_players": 4,
            "skill_level": 4