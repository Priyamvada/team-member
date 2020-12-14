from team_member.core.models import TeamMember
from rest_framework import serializers


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    created = serializers.DateTimeField(
        read_only=True,
        required=False,
        allow_null=True,
        format='%Y-%m-%d %H:%M:%S %z',
        input_formats=['%Y-%m-%d %H:%M'],
    )

    last_modified = serializers.DateTimeField(
        read_only=True,
        required=False,
        allow_null=True,
        format='%Y-%m-%d %H:%M:%S %z',
        input_formats=['%Y-%m-%d %H:%M'],
    )

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'role',
            'patient_name',
            'created',
            'last_modified'
        ]