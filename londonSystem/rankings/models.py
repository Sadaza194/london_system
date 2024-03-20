from django.db import models

# Create your models here.

class Player(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    # rank = models.PositiveIntegerField()
    rank = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # age = models.PositiveIntegerField()
    age = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    classic_rank = models.CharField(max_length=100)
    rapid_rank = models.CharField(max_length=100)
    blitz_rank = models.CharField(max_length=100)

    def __str__(self):
        return str(self.lname + ", " + self.fname)



class Tournament(models.Model):

    w_player = models.CharField(max_length=100)
    w_player_rank = models.CharField(max_length=100)
    b_player = models.CharField(max_length=100)
    b_player_rank = models.CharField(max_length=100)
    game_result = models.CharField(max_length=100)
    number_of_moves = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)