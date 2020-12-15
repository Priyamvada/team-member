from django.db import models


class TeamMemberQuerySet(models.QuerySet):
    pass


class TeamMemberManager(models.Manager):
    def get_queryset(self):
        queryset = TeamMemberQuerySet(self.model, using=self._db)
        return queryset
