from django.test import TestCase

from eddb.models import System

from .mocks import create_system


class TestNeighbours(TestCase):
    def setUp(self):
        self.origin = create_system(
                x=0, y=0, z=0, name='Origin')
        self.s1 = create_system(
                x=1, y=0, z=0, name='1ly')
        self.s2 = create_system(
                x=3, y=4, z=0, name='5ly')
        self.s3 = create_system(
                x=3, y=4, z=5, name='5ly')

    def test_search_includes_origin(self):
        self.assertEqual(1, System.objects.neighbours_of(self.origin, range=0).count())

    def test_short_range_search_covers_nearby_systems(self):
        self.assertEqual(2, System.objects.neighbours_of(self.origin, range=1).count())

    def test_medium_range_search_covers_nearby_systems(self):
        self.assertEqual(4, System.objects.neighbours_of(self.origin, range=8).count())
