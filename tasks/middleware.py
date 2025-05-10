from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url, '/admin/login/', '/static/']

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            if not any(url in path for url in self.open_urls):
                return redirect(f"{self.login_url}?next={path}")
        
        response = self.get_response(request)
        return response