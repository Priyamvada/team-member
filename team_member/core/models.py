from django.db import models
from django.utils.translation import gettext_lazy as _
from team_member.core import managers


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

    ROLE_CHOICES = (
        (0, _('Admin')),
        (1, _('Regular'))
    )

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
        max_length=14,
        null=True,
        blank=True
    )
    email = models.EmailField(
        "Email ID",
        max_length=100,
        unique=True
    )
    role = models.IntegerField(
        choices=ROLE_CHOICES,
        default=1,
    )

    objects = managers.TeamMemberManager()

    '''
    Returns the person's full name
    '''
    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name or '')

    def save(self, **kwargs):
        self.email = self.email.lower()
        super(TeamMember, self).save(**kwargs)

    class Meta:
        db_table = 'team_member'
        ordering = ['first_name', 'last_name']
