from django.db import models

class Tuba(models.Model):

    toa_number = models.IntegerField(default=1)
    kylalise_nimi = models.CharField(max_length=200)
    valjumise_kuupaev = models.DateTimeField(blank=True,null=True)