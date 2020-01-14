from ..models import Building


def add_building(diccionario):
    building = Building()
    building.name = diccionario['name']
    building.save()
