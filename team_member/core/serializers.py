from team_member.core.models import TeamMember
from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        # to allow numeric input
        if data in self._choices:
            return data

        # to allow case insensitive text input
        elif type(data) == str:
            for key, val in self._choices.items():
                if val.lower() == data.lower():
                    return key
        self.fail('invalid_choice', input=data)


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

    role = ChoiceField(choices=TeamMember.ROLE_CHOICES)

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'phone_number',
            'email',
            'role',
            'created',
            'last_modified'
        ]