import functools
from django.http import HttpResponse

from .models import AuthClient


def _get_client_ip(request):
    x_forwarded_for = request.headers.get('HTTP_X_FORWARDED_FOR')
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
                print("no auth header provided")
                return HttpResponse(status=401)
            try:
                method, auth_token = auth_token.split()
            except ValueError:
                # malformed auth request
                print("malformed auth request")
                return HttpResponse(status=401)

            # TODO: a different status code might be right
            if method.lower() != "koop":
                print("Wring method...")
                return HttpResponse(status=401)

            remote_ip = _get_client_ip(request)
            try:
                _client = AuthClient.objects.filter(
                    enabled=True,
                    service__name__iexact=service_name,
                    ip_address__iexact=remote_ip
                ).get(id=auth_token)
            except AuthClient.DoesNotExist:
                print("client entry not found")
                return HttpResponse(status=401)

            return view_func(request,*args, **kwargs)
        return wrapper
    return auth_decorator