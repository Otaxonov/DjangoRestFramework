from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='blog_posts'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post_detail'),
    path('user/<str:username>/posts/', views.UserPostsView.as_view(), name='user_posts'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]