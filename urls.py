from django.urls import path

from .views import authenticate_view, get_user_view

app_name='authprovider'

urlpatterns = [
    path("authenticate/", authenticate_view, name="authenticate"),
    path("getuser/<int:user_id>/", get_user_view, name="get_user"),
]