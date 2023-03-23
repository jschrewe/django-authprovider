import json

from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt

from .decorators import authenticate_client


def _make_user_dict(user):
     return {
        "email": user.email,
        "id": user.id,
        "permissions": list(user.get_user_permissions()),
    }


@csrf_exempt
@authenticate_client(service_name="userauth")
def authenticate_view(request):
    """
    request json looks like: {
        "email": email,
        "password": password
    }
    """
    if request.method != "POST":
        return HttpResponse(status=405)
    try:
        auth_req = json.loads(request.body)
    except:
        return HttpResponse(status=400)

    try:
        email = auth_req['email']
        password = auth_req['password']
    except KeyError:
        return HttpResponse(status=400)
    
    # TODO: This needs more checks
    user = authenticate(request, username=email, password=password)
    if user is not None:
        return JsonResponse(_make_user_dict(user))
    else:
        return HttpResponse(status=401)


@csrf_exempt
@authenticate_client(service_name="userauth")
def get_user_view(request, user_id):
    try:
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        return JsonResponse(_make_user_dict(user))
    except User.DoesNotExist:
        return HttpResponse(status=404)