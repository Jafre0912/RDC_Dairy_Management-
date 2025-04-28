from django.utils.deprecation import MiddlewareMixin
import html

class SanitizeInputMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method in ['POST', 'PUT', 'PATCH']:
            for key, value in request.POST.items():
                if isinstance(value, str):
                    request.POST[key] = html.escape(value)