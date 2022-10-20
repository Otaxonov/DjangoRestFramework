from django.urls import path
from .views import (
    PostsListView,
    PostDetailView,
    UserPostsView,
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    path('post/list/', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('user/<str:username>/posts/', UserPostsView.as_view(), name='user_posts'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
]