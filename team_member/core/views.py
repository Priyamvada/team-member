from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from team_member.core import models, serializers


class TeamMemberModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows team members to be viewed, added, edited or deleted.
    """
    queryset = models.TeamMember.objects.all().order_by('-last_modified')
    serializer_class = serializers.TeamMemberSerializer
    permission_classes = [permissions.AllowAny]

    def destroy(self, request, *args, **kwargs):
        # had to override this because expectation was empty object rather than empty response
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={},status=status.HTTP_204_NO_CONTENT)
