import functools
from django.http import HttpResponse

from .models import AuthClient


def _get_client_ip(request):
    x_forwarded_for = request.headers.get('X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def authenticate_client(service_name):
    def auth_decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                auth_token = request.headers['Authorization']
            except KeyError:
                # no auth header provided
                return HttpResponse(content="no auth header provided", status=401)
            try:
                method, auth_token = auth_token.split()
            except ValueError:
                # malformed auth request
                return HttpResponse(content="malformed auth request", status=401)

            # TODO: a different status code might be right
            if method.lower() != "koop":
                return HttpResponse(status=401)

            remote_ip = _get_client_ip(request)
            try:
                _client = AuthClient.objects.filter(
                    enabled=True,
                    service__name__iexact=service_name,
                    ip_address__iexact=remote_ip
                ).get(id=auth_token)
            except AuthClient.DoesNotExist:
                return HttpResponse(content="client entry not found", status=401)

            return view_func(request,*args, **kwargs)
        return wrapper
    return auth_decorator