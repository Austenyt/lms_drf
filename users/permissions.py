from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательский класс прав доступа, позволяющий только владельцу объекта редактировать его.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS запросы всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить редактирование объекта только владельцу
        return obj.owner == request.user
