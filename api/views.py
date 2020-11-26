from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import *
from .models import *


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name')
    serializer_class = CharacterSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all().order_by('name')
    serializer_class = SpeciesSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by('title')
    serializer_class = FilmSerializer