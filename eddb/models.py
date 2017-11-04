# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math

from django.db import models
from .queryset import SystemQueryset


class System(models.Model):
    system_id = models.IntegerField(db_index=True)
    x = models.FloatField(db_index=True)
    y = models.FloatField(db_index=True)
    z = models.FloatField(db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    allegiance = models.CharField(max_length=50, null=True, blank=True)
    allegiance_id = models.IntegerField(null=True, blank=True)
    edsm_id = models.IntegerField(db_index=True, null=True, blank=True)
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
        return self.name


class Station(models.Model):
    system = models.ForeignKey(System)
    station_id = models.IntegerField(db_index=True)
    distance_to_star = models.FloatField(db_index=True, null=True, blank=True)
    name = models.CharField(max_length=255, db_index=True)
    max_landing_pad_size = models.CharField(max_length=8, blank=True, null=True)
    allegiance = models.CharField(max_length=50, null=True, blank=True)
    allegiance_id = models.IntegerField(null=True, blank=True)
    controlling_minor_faction_id = models.IntegerField(null=True, blank=True)
    government = models.CharField(max_length=50, null=True, blank=True)
    government_id = models.IntegerField(null=True, blank=True)
    has_blackmarket = models.BooleanField()
    has_commodities = models.BooleanField()
    has_docking = models.BooleanField()
    has_market = models.BooleanField()
    has_outfitting = models.BooleanField()
    has_rearm = models.BooleanField()
    has_refuel = models.BooleanField()
    has_repair = models.BooleanField()
    has_shipyard = models.BooleanField()
    is_planetary = models.BooleanField()
    state = models.CharField(max_length=50, null=True, blank=True)
    state_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name
