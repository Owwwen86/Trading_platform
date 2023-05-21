from rest_framework.permissions import IsAuthenticated


class UserLinkPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_active:
            return True
        return False
