from ..models import Variable
from django.apps import apps
from django.db import models


def add_variable(diccionario):
    variable = Variable()
    variable.name = diccionario['name']
    variable.save()
    return True
