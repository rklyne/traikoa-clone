# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math

from django.db import models
from .queryset import SystemQueryset


class System(models.Model):
    system_id = models.IntegerField(db_index=True)
    x = models.IntegerField(db_index=True)
    y = models.IntegerField(db_index=True)
    z = models.IntegerField(db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    allegiance = models.CharField(max_length=50, null=True, blank=True)
    allegiance_id = models.IntegerField(null=True, blank=True)
    edsm_id = models.IntegerField(db_index=True)
    controlling_minor_faction = models.CharField(max_length=50, null=True, blank=True)
    controlling_minor_faction_id = models.IntegerField(null=True, blank=True)
    government = models.CharField(max_length=50, null=True, blank=True)
    government_id = models.IntegerField(null=True, blank=True)
    power = models.CharField(max_length=50, null=True, blank=True)
    power_state = models.CharField(max_length=50, null=True, blank=True)
    power_state_id = models.IntegerField(null=True, blank=True)
    primary_economy = models.CharField(max_length=50, null=True, blank=True)
    primary_economy_id = models.IntegerField(null=True, blank=True)
    security = models.CharField(max_length=50, null=True, blank=True)
    security_id = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    state_id = models.IntegerField(null=True, blank=True)
    needs_permit = models.BooleanField(db_index=True)
    population = models.IntegerField()

    objects = SystemQueryset.as_manager()

    @property
    def cc(self):
        if not self.population:
            return 0
        return round(math.log10(self.population * 10))

    def __unicode__(self):
        return '<System {}>'.format(self.name)


expected_output = """
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

