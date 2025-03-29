from rest_framework import permissions

class IsModer(permissions.BasePermission):
    message = 'Вы не имеете прав модератора'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модератор').exists()


class IsOwner(permissions.BasePermission):
    message = 'Вы не имеете прав владельца'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False