import json

from django.core.management.base import BaseCommand

from eddb.models import Station, System


def filter_dict(dict_in, keys):
    return {key: value for (key, value) in dict_in.items() if key in keys}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', required=True, help='The EDDB file stations.json')

    def handle(self, *args, **options):
        filename = options['file']
        print "importing from file", filename
        with open(filename, 'rb') as f:
            data = json.load(f)
        station_keys = [
            'system',
            'station_id',
            'distance_to_star',
            'name',
            'max_landing_pad_size',
            'allegiance',
            'allegiance_id',
            'controlling_minor_faction_id',
            'government',
            'government_id',
            'has_blackmarket',
            'has_commodities',
            'has_docking',
            'has_market',
            'has_outfitting',
            'has_rearm',
            'has_refuel',
            'has_repair',
            'has_shipyard',
            'is_planetary',
            'state',
            'state_id',
            'type',
            'type_id',
        ]

        for station_data in data:
            try:
                system = System.objects.get(system_id=station_data['system_id'])
            except System.DoesNotExist:
                print "!!!", station_data.get('name')
                continue
            print system.name, '->', station_data.get('name')
            station_id = station_data['id']
            station_data = filter_dict(station_data, keys=station_keys)
            station, is_new_station = Station.objects.get_or_create(
                    station_id=station_id,
                    system=system,
                    defaults=station_data)
            if not is_new_station:
                station.__dict__.update(station_data)
                station.save()
