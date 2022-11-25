from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts.choices import UserTypeChoices


class IsCEO(BasePermission):
    """ Allow only Administrator to create users """

    def has_permission(self, request, view):
        if not request.user:  return False
        
        return request.user.user_type == UserTypeChoices.CEO 


class IsClientAdmin(BasePermission):
    """ Allow only Administrator to create users """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated: return False

        return request.user.user_type == UserTypeChoices.CLIENT_ADMIN or request.user.is_superuser

class IsHeadOfDepartment(BasePermission):
    """ Allow only Administrator to create users """

    def has_permission(self, request, view):
        if not request.user: return False

        return request.user.user_type == UserTypeChoices.HoD


class IsSubDepartment(BasePermission):
    """ Allow only Administrator to create users """
    """ Allow only Administrator to create users """

    def has_permission(self, request, view):
        if not request.user: return False

        return request.user.user_type == UserTypeChoices.SUB
