
from rest_framework.permissions import IsAuthenticated


class AutenticacionSoloPost(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(AutenticacionSoloPost, self).has_permission(request, view)

class AutenticacionSoloGet(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(AutenticacionSoloGet, self).has_permission(request, view)