from django.urls import path
from . import views

urlpatterns = [
    path('coach/',views.CreateListCoachView.as_view()),
    path('coach/<pk>/',views.GetUpdateDeleteCoachView.as_view())
]