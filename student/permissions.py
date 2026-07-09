from rest_framework import permissions

class IsFaculty(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Faculty").exists()
        )
    

class IsOwnerOrFaculty(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_faculty = request.user.groups.filter(name="Faculty").exists()

        if request.method in permissions.SAFE_METHODS:
            is_own = (
                obj.user is not None
                and obj.user == request.user
            )

            return is_faculty or is_own
        return is_faculty