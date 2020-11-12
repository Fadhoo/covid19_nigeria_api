from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
import json
from ncdc_data.models import CovidData
from ncdc_data.serializers import CovidDataSerializer

# Create your views here.

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):

        import datetime
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        
        json_obj = requests.get('https://covid19-nigeria-api-test.herokuapp.com/ncdc_data/')
        json_data = json_obj.json()
        data = json_data[0]['today']
        samples_tested = data['samples_tested']
        active = data['active_cases']
        confirmed = data['confirmed_cases']
        deaths = data['deaths']
        discharged_cases = data['discharged_cases']

        last_month = json_data[1]['last_month']
        last_samples_tested = last_month['samples_tested']
        last_active = last_month['active_cases']
        last_confirmed = last_month['confirmed_cases']
        last_deaths = last_month['deaths']
        last_discharged_cases = last_month['discharged_cases']


        context = {
            'samples_tested': samples_tested,
            'active': active,
            'confirmed': confirmed,
            'deaths': deaths,
            'discharged': discharged_cases,
            'last_samples_tested': last_samples_tested,
            'last_active': last_active,
            'last_confirmed': last_confirmed,
            'last_deaths': last_deaths,
            'last_discharged': last_discharged_cases,
            'date':today,
            'lst_month':lastMonth,
        }

        return Response(template_name='index.html', data=context)

# class NcdcData(APIView):
#     serializer_class = CovidDataSerializer

#     def get(self, request):
#         covid_data = CovidData.objects.filter().order_by('date')[0]
#         serializer = CovidDataSerializer(covid_data)
#         return Response(serializer.data)
