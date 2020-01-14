from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from ..logic.logic_room import add_room, find_room_by_code, find_frequent_sensors


def post_room(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The room was added correctly'
    try:
        add_room(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)


def get_room_by_code(request, p_code):
    response = 'room not found'
    try:
        room = find_room_by_code(p_code)
        response = serializers.serialize('json', [room])
    except Exception as e:
        response = e
    return HttpResponse(response)


def get_frequent_sensors(request, room_code):
    response = ''
    try:
        room = find_room_by_code(room_code)
        if room is None:
            response = 'room not found'
        else:
            sensors = find_frequent_sensors(room)
            response = serializers.serialize('json', sensors)
    except Exception as e:
        response = e
    return HttpResponse(response)
