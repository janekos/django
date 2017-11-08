from django.db import models

class Tuba(models.Model):

    toa_number = models.IntegerField(default=1)
    kylalise_nimi = models.CharField(max_length=200)
    valjumise_kuupaev = models.DateTimeField(blank=True,null=True)

class Calories(models.Model):
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    
class raamatud(models.Model):
    raamatu_nr = models.IntegerField(default=0, primary_key=True)
    raamatu_nimi = models.CharField(max_length=255)
    raamatu_lehti = models.IntegerField(default=0)
    omanikud = models.ManyToManyField("omanikud")
    
class omanikud(models.Model):
    id = models.IntegerField(primary_key=True)
    omaniku_nr = models.IntegerField(default=0)
    omanik_nimi = models.CharField(max_length=255)
    omatud_raamatu_nr = models.IntegerField(default=0)
    