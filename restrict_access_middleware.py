# restrict_access_middleware.py
from django.http import HttpResponseForbidden
from django.urls import resolve

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        if path != '/accounts/login/' and not path.startswith('/static/'):
            return HttpResponseForbidden("Access Denied")

        response = self.get_response(request)
        return response
