from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware que requiere login para todas las páginas excepto las especificadas
    en LOGIN_EXEMPT_URLS en settings.py.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs que no requieren autenticación - intentar obtener de settings
        from django.conf import settings
        self.exempt_urls = getattr(settings, 'LOGIN_EXEMPT_URLS', [
            '/login/',
            '/signup/',
            '/admin/',
            '/admin/login/',
        ])
        
    def __call__(self, request):
        # Si el usuario no está autenticado y la URL no está exenta
        if not request.user.is_authenticated:
            # Comprobar si la URL actual está exenta
            path = request.path_info
            if not any(path.startswith(url) for url in self.exempt_urls):
                # Redireccionar al login
                return redirect(settings.LOGIN_URL)
        
        response = self.get_response(request)
        return response