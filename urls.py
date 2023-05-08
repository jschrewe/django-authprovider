from django.urls import path

from .views import authenticate_view, get_user_view, multiplikatoren_api

app_name='authprovider'

urlpatterns = [
    path("authenticate/", authenticate_view, name="authenticate"),
    path("getuser/<int:user_id>/", get_user_view, name="get_user"),
    path("getmultis/<int:user_id>/", multiplikatoren_api, name=multiplikatoren_api),
]