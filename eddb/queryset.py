from django.db.models import QuerySet, F


class SystemQueryset(QuerySet):
    def get_by_name(self, name):
        systems = sorted(
            self.filter(name__icontains=name),
            key=lambda system: len(system.name))
        if not systems:
            raise self.model.DoesNotExist
        return systems[0]

    def neighbours_of(self, system, range=15):
        range = float(range)
        return self.annotate(distance_squared=(
            (F('x') - system.x) ** 2 +
            (F('y') - system.y) ** 2 +
            (F('z') - system.z) ** 2
            )).filter(distance_squared__lte=range**2)

    @property
    def control_systems(self):
        return self.filter(power_state='Control')

    def exploiting(self, system):
        return self.control_systems.neighbours_of(system, range=15)
