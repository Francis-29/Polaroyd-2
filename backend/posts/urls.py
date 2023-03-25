from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.Posts.as_view()),
    # path('users/', views.Users.as_view()),
    path('post/<int:pk>/', views.Post.as_view()),
    path('like/', views.LikePost.as_view()),
    path('like-delete/<int:pk>/', views.LikePostDelete.as_view()),
]