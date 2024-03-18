from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Permission to check if the user is a moderator.
    """

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
