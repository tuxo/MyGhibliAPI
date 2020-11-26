from django.db import models

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Species"

class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    eye_color = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    direction = models.CharField(max_length=255)
    release_year = models.IntegerField() 
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title

