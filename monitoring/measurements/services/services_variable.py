from django.http import HttpResponse
import json
from ..logic.logic_variable import add_variable


def post_variable(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The variable was added correctly'
    try:
        add_variable(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)
