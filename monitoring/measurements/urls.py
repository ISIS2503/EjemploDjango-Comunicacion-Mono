from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .services.services_measurements import post_measurement, get_sensor_measurements
from .services.services_variable import post_variable


urlpatterns = [
    path('newMeasurement/', csrf_exempt(post_measurement)),
    path('newVariable/', csrf_exempt(post_variable)),
    path('sensor/<slug:sensor_code>/measurements', get_sensor_measurements),
]
