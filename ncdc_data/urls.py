from django.urls import path
from .views import SamplesTested

urlpatterns = [
    path('samples_tested/', SamplesTested.as_view()),
]