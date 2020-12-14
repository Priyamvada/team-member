from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Base model for audit logging purpose
    """
    created = models.DateTimeField(
        "Created Date",
        auto_now=False,
        auto_now_add=True
    )

    last_modified = models.DateTimeField(
        "Last Modified Date",
        auto_now=True,
        auto_now_add=False
    )

    class Meta:
        abstract = True


class TeamMember(TimeStampedModel):
    class Role(models.TextChoices):
        ADMIN = 'ADM', _('Admin')
        REGULAR = 'REG', _('Regular')

    first_name = models.CharField(
        "First Name",
        max_length=30
    )
    last_name = models.CharField(
        "Last Name",
        max_length=30,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        "Phone Number",
        max_length=14
    )
    email = models.EmailField(
        "Email ID",
        max_length=100,
        unique=True
    )
    role = models.CharField(
        max_length=3,
        choices=Role.choices,
        default=Role.REGULAR,
    )

    '''
    Returns the person's full name
    '''
    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name or '')

    class Meta:
        db_table = 'team_member'
        ordering = ['first_name', 'last_name']
