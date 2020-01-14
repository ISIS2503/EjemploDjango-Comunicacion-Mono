from django.shortcuts import render
from .models import Room

# Create your views here.


def get_room_by_code(request, p_code):
    room = Room.objects.get(code=p_code)
    return render(request, 'room_template.html', {'room': room})
