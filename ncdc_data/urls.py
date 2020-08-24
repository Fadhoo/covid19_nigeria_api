from django.urls import path
from .views import NcdcData

urlpatterns = [
    path('ncdc_data/', NcdcData.as_view()),
]