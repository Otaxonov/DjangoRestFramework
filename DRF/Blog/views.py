from rest_framework import generics, permissions
from .serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer, RegisterSerializer
from django.shortcuts import get_object_or_404
from .models import User, Post

# Create your views here.

class PostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.all().filter(author=user)
    
class PostCreateView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer