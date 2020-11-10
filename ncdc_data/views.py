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
        # year = date.today().year
        # month = date.today().month
        # day = date.today().day
        # lastest_data = CovidData.objects.filter().order_by('date')

        # if  lastest_data['date'].date() != date.today():
        #     get_ncdc_data()  
        
        import datetime
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        lst_mnth = lastMonth.strftime("%Y" + "-" + "%m" + "-" + "%d")
        tday = today.strftime("%Y" + "-" + "%m" + "-" + "%d")

        covid_data = CovidData.objects.filter(date=tday)[0]
        last_month = CovidData.objects.filter(date=lst_mnth)[0]
        serializer = CovidDataSerializer(covid_data)
        serializerL = CovidDataSerializer(last_month)
        return Response([serializer.data, serializerL.data])



class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response(template_name='index.html')
        