from django.shortcuts import render
from rest_framework.views import APIView
from ncdc import total_samples_tested


class SamplesTested(APIView):
    total_sample_tested = total_samples_tested()

# Create your views here.
