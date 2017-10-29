import json
from pprint import pprint

from django.core.management.base import BaseCommand

from eddb.models import System


def filter_dict(dict_in, keys):
    return {key: value for (key, value) in dict_in.items() if key in keys}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', required=True, help='The EDDB file systens_populated.json')

    def handle(self, *args, **options):
        filename = options['file']
        print "importing from file", filename
        with open(filename, 'rb') as f:
            data = json.load(f)
        system_keys = [
            u'allegiance',
            u'allegiance_id',
            u'controlling_minor_faction',
            u'controlling_minor_faction_id',
            u'edsm_id',
            u'government',
            u'government_id',
            u'id',
            u'name',
            u'needs_permit',
            u'population',
            u'power',
            u'power_state',
            u'power_state_id',
            u'primary_economy',
            u'primary_economy_id',
            u'security',
            u'security_id',
            u'state',
            u'state_id',
            u'x',
            u'y',
            u'z',
            ]

        for system_data in data:
            pprint(system_data)
            pprint(system_data.keys())
            system, is_new_system = System.objects.get_or_create(
                    system_id=system_data['id'],
                    defaults=filter_dict(system_data, keys=system_keys))
            if not is_new_system:
                system.__dict__.update(system_data)
                system.save()
