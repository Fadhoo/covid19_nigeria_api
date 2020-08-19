from rest_framework import serializers
from .models import CovidData


class CovidDataSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        return {
            'samples_tested': obj.samples_tested,
            'confirmed_cases': obj.confirmed_cases,
            'active_cases': obj.active_cases,
            'discharged_cases': obj.discharged_cases,
            'deaths': obj.deaths,
        }

    class Meta:
        model = CovidData
        fields = '__all__'
