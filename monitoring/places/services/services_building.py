from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from ..logic.logic_building import add_building


def post_building(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The building was added correctly'
    try:
        add_building(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)
