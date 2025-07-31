from django.db import models

# Create your models here.


from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    batting_style = models.CharField(max_length=50)
    bowling_style = models.CharField(max_length=50)
    age = models.IntegerField()
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()

    