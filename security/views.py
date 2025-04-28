from django.http import JsonResponse
from .models import FailedLoginAttempt
from .rate_limit import RateLimiter
from django.utils.timezone import now
from datetime import timedelta

def failed_login_view(request):
    ip_address = get_client_ip(request)
    username = request.POST.get('username', None)

    # Log the failed login attempt
    FailedLoginAttempt.objects.create(ip_address=ip_address, username=username)

    return JsonResponse({"message": "Failed login attempt logged"}, status=403)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def rate_limited_view(request):
    limiter = RateLimiter(key=f"rate_limit:{get_client_ip(request)}", limit=5, duration=timedelta(minutes=1))
    if not limiter.is_allowed():
        return JsonResponse({"message": "Too many requests. Please try again later."}, status=429)

    return JsonResponse({"message": "Request allowed"}, status=200)