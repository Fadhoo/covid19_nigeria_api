from django.db import models


class CovidData(models.Model):
    date = models.DateField()
    samples_tested = models.IntegerField()
    confirmed_cases = models.IntegerField()
    active_cases = models.IntegerField()
    discharged_cases = models.IntegerField()
    deaths = models.IntegerField()

