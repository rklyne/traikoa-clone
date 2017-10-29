from django.db.models import QuerySet, F


class SystemQueryset(QuerySet):
    def neighbours_of(self, system, range=15):
        return self.annotate(distance=(
            (F('x') - system.x) ** 2 +
            (F('y') - system.y) ** 2 +
            (F('z') - system.z) ** 2
            ) ** (0.5)).filter(distance__lte=range)
