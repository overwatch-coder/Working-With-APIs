from django.shortcuts import render
from rest_framework import generics
from .serializers import LinkSerializer
from .models import Link

# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer



