from rest_framework.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("login/", views.loginView.as_view()),
    path("register/", views.UserCreateView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
    path("users/<str:user_id>/enable_disable/", views.EnableDisableUserView.as_view()),
]
