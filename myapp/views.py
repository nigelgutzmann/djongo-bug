from django.http import HttpResponse
import json

from myapp.models import Planet, SolarSystem, Universe


def create(request):
    planet = request.GET.get('planet')
    if planet:
        (universe, _) = Universe.objects.get_or_create(
            name='Laniakea'
        )
        (solar_system, _) = SolarSystem.objects.get_or_create(
            name='milky way',
            universe=universe,
        )
        (planet, _) = Planet.objects.get_or_create(
            name=planet,
            solar_system=solar_system,
        )
    return HttpResponse('ok')


def data(request):
    planets = Planet.objects.all()
    universes = list(set([planet.solar_system.universe.name for planet in planets]))
    return HttpResponse(json.dumps({
        'planets': [planet.name for planet in planets],
        'solar_systems': [SolarSystem.objects.get(planet=planet).name for planet in planets],
        'universes': universes,
    }))
