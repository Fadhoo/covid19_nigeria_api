from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CovidData
from .serializers import CovidDataSerializer
from rest_framework import filters
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import timezone, date
import datetime
from ncdc import get_ncdc_data

class NcdcData(APIView):
    serializer_class = CovidDataSerializer

    def get(self, request):
        year = date.today().year
        month = date.today().month
        day = date.today().day
        # lastest_data = CovidData.objects.filter().order_by('date')

        # if  lastest_data['date'].date() != date.today():
        #     get_ncdc_data()  
        
        covid_data = CovidData.objects.filter().order_by('date')[0]
        last_month = CovidData.objects.filter(date='2020-10-31')
        serializer = CovidDataSerializer(covid_data)
        serializerL = CovidDataSerializer(last_month)
        return Response([serializer.data, serializerL.data])



class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response(template_name='index.html')