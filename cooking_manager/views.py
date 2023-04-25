from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrReadOnly
from .serializers import RecipeSerializer

from .models import Recipe, Day_of_week


class RecipeAPIList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeAPIUpdate(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated)


class RecipeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAdminOrReadOnly,)






