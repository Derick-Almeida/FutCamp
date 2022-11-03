from rest_framework.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("login/", obtain_auth_token),
    path("users/", views.UserCreateView.as_view()),
    path("users/<str:user_id>/", views.UserCreateView.as_view())
]