from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>/', views.MyUser.as_view()),
]