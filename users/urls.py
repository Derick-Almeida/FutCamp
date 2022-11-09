from rest_framework.urls import path

from . import views
from .utils.user_extra_views import (
    UserFavoriteTeamView,
    UserFavoritePlayerView,
    UserFavoriteChampionshipView,
    UserFavoriteDetailView,
)

urlpatterns = [
    path("login/", views.loginView.as_view()),
    path("register/", views.UserCreateView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
    path("users/<str:user_id>/enable_disable/", views.EnableDisableUserView.as_view()),
    path("users/<str:user_id>/favorites/teams/", UserFavoriteTeamView.as_view()),
    path("users/<str:user_id>/favorites/players/", UserFavoritePlayerView.as_view()),
    path(
        "users/<str:user_id>/favorites/championships/",
        UserFavoriteChampionshipView.as_view(),
    ),
    path(
        "users/<str:user_id>/favorites/add_team/",
        UserFavoriteDetailView.as_view(),
    ),
    path(
        "users/<str:user_id>/favorites/add_player/",
        UserFavoriteDetailView.as_view(),
    ),
    path(
        "users/<str:user_id>/favorites/add_championship/",
        UserFavoriteDetailView.as_view(),
    ),
]
