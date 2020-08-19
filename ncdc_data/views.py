from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CovidData
from .serializers import CovidDataSerializer
from rest_framework import filters


class SamplesTested(APIView):
    serializer_class = CovidDataSerializer

    def get(self, request):
        covid_data = CovidData.objects.filter().order_by('date')[0]
        serializer = CovidDataSerializer(covid_data)
        return Response(serializer.data)