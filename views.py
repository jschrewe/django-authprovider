import json

from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt

from app_user.views.shared_logic.user_passes import is_admin, is_multiplicator, is_participant

from .decorators import authenticate_client


def _make_user_dict(user):
     return {
        "email": user.email,
        "id": user.id,
        "admin": is_admin(user),
        "multiplicator": is_multiplicator(user),
        "participant": is_participant(user),
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
    

@csrf_exempt
@authenticate_client(service_name="multiplikatoren_api")
def multiplikatoren_api(request, id):
    try:
        User = get_user_model()
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    #
    # Logik um die dem Benutzer zugehörigen Multiplikatoren zu finden...
    # Benötigte Felder: Vorname, Nachname, E-Mail Adresse
    #
    # Etwa: qs = Multi.objects.get(...)
    data = list(qs.values("vorname", "nachname", "email"))
    
    return JsonResponse({'multis': data})