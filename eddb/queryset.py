from django.db.models import QuerySet, F


class SystemQueryset(QuerySet):
    def get_by_name(self, name):
        systems = sorted(
            self.filter(name__icontains=name),
            key=lambda system: len(system.name))
        if not systems:
            raise ValueError("System '{}' not found".format(name))
        return systems[0]

    def neighbours_of(self, system, range=15):
        return self.annotate(distance=(
            (F('x') - system.x) ** 2 +
            (F('y') - system.y) ** 2 +
            (F('z') - system.z) ** 2
            ) ** (0.5)).filter(distance__lte=range)
