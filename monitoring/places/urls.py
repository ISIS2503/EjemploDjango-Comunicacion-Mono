from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .services.services_room import post_room, get_frequent_sensors
from .services.services_building import post_building
from .services.services_sensor import post_sensor
from .views import get_room_by_code

urlpatterns = [
    path('newBuilding/', csrf_exempt(post_building)),
    path('newRoom/', csrf_exempt(post_room)),
    path('newSensor/', csrf_exempt(post_sensor)),
    path('rooms/<slug:p_code>/', get_room_by_code),
    path('rooms/<slug:room_code>/sensors/frequent', get_frequent_sensors)
]
