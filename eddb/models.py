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


