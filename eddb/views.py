# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse

from eddb.models import System


POWERS = [
        u'Felicia Winters',
        u'Pranav Antal',
        u'Edmund Mahon',
        u'Archon Delaine',
        u'LiYong-Rui',
        u'Zachary Hudson',
        u'Denton Patreus',
        u'Arissa Lavigny-Duval',
        u'Yuri Grom',
        u'Zemina Torval',
        u'Aisling Duval',
        ]


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_system(request, system_id):
    return json_response(system_dict(System.objects.get(system_id=system_id), deep=True))


def search(request):
    name = request.GET['name']
    return json_response([system_dict(System.objects.get_by_name(name), deep=True)])


def bubble(request):
    id = request.GET['id']
    radius = request.GET.get('radius', 15)
    system = System.objects.get(system_id=id)
    data = [system_dict(s) for s in System.objects.neighbours_of(system, radius)]
    return json_response(data)


def control_systems_search(request):
    ids = filter(bool, request.GET.getlist('ids', []))
    ids += filter(bool, request.GET.getlist('ids[]', []))
    data = [
        system_dict(s)
        for s in System.objects.all().control_systems.filter(id__in=ids)]
    return json_response(data)


def powers(request):
    data = [{"name": name} for name in POWERS]
    return json_response(data)


def system_dict(system, deep=False):
    """
    # expected output



    {
      "id": 1,
      "eddb_id": 1,
      "name": "1 G. Caeli",
      "position": {
        "x": 80.90625,
        "y": -83.53125,
        "z": -30.8125
      },
      "population": 6544826,
      "allegiance": "Empire",
      "security": "Medium",
      "needs_permit": false,
      "stations": [
        {
          "id": 941,
          "eddb_id": 5611,
          "name": "Smoot Gateway",
          "is_planetary": false,
          "pad_size": "L",
          "distance": 4713
        },
        {
          "id": 6803,
          "eddb_id": 45547,
          "name": "Giacobini Base",
          "is_planetary": true,
          "pad_size": "L",
          "distance": 3491
        },
        {
          "id": 7419,
          "eddb_id": 49182,
          "name": "Kandel Arsenal",
          "is_planetary": true,
          "pad_size": "L",
          "distance": 3493
        },
        {
          "id": 9628,
          "eddb_id": 63794,
          "name": "Sabine Survey",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 3493
        },
        {
          "id": 9629,
          "eddb_id": 63795,
          "name": "Laird Landing",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 3491
        },
        {
          "id": 9630,
          "eddb_id": 63796,
          "name": "Yize Camp",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 3490
        },
        {
          "id": 9631,
          "eddb_id": 63797,
          "name": "Difate Beacon",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 3507
        },
        {
          "id": 9632,
          "eddb_id": 63798,
          "name": "Auld Depot",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 4712
        },
        {
          "id": 9633,
          "eddb_id": 63799,
          "name": "Gurevich Arena",
          "is_planetary": true,
          "pad_size": "None",
          "distance": 4712
        }
      ],
      "cc_value": 8,
      "contested": false,
      "exploitations": [
        56
      ]
    }
    """
    d = system.__dict__.copy()
    d['cc_value'] = system.cc
    del d['_state']
    d['eddb_id'] = system.system_id
    # .. TODO: Add exploiting control systems
    d.setdefault(
        'exploitations',
        list(System.objects.exploiting(system).values_list('system_id', flat=True)))
    # .. TODO: Add stations
    d.setdefault('stations', [])
    if system.power:
        d['power_id'] = POWERS.index(system.power) + 1
    d['position'] = {
        "x": d["x"],
        "y": d["y"],
        "z": d["z"],
        }
    return d
