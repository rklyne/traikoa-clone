import math

from django.core.management.base import BaseCommand

from eddb.models import System


def filter_dict(dict_in, keys):
    return {key: value for (key, value) in dict_in.items() if key in keys}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('system_names', nargs='+')

    def handle(self, *args, **options):
        print args, options
        args = options['system_names']
        system0 = System.objects.get_by_name(args[0])
        systems = map(System.objects.get_by_name, args[1:])
        print system0, "->"
        for system in systems:
            dist = math.sqrt(
                (system.x - system0.x)**2 +
                (system.y - system0.y)**2 +
                (system.z - system0.z)**2
                )
            print "  ", system, ": ", dist
