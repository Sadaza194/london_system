from django.db import models

# Create your models here.

class Player(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    rank = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=200)
    classic_rank = models.PositiveIntegerField()
    rapid_rank = models.PositiveIntegerField()
    blitz_rank = models.PositiveIntegerField()

    def __str__(self):
        return str(self.lname + ", " + self.fname)

    