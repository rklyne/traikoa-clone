import itertools

from .models import System

counter = itertools.count(100)


def create_system(**kwargs):
    defaults = {
        "system_id": next(counter),
        "edsm_id": next(counter),
        "x": next(counter),
        "y": next(counter),
        "z": next(counter),
        "name": "blank name",
        "needs_permit": False,
        "population": 0,
        }
    defaults.update(kwargs)
    return System.objects.create(**defaults)
