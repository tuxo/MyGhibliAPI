from rest_framework import serializers

from .models import *

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'gender', 'age', 'eye_color', 'hair_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('name', 'classification')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','title', 'description', 'direction', 'release_year', 'characters')