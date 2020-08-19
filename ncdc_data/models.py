from django.db import models


class CovidData(models.Model):
    date = models.DateField()
    samples_tested = models.CharField(max_length=10)
    confirmed_cases = models.CharField(max_length=10)
    active_cases = models.CharField(max_length=10)
    discharged_cases = models.CharField(max_length=10)
    deaths = models.CharField(max_length=10)

