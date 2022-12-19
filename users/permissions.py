from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.views import Request


class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request: Request, view):
        return request.method == "POST" or request.user.is_staff
