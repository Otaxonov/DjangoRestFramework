from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, PostCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions


User = get_user_model()
# Create your views here.

class PostsListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserPostsView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.all().filter(author=user)

class PostCreateView(CreateAPIView):
    queryset = Post
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
