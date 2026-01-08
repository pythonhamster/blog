from django.db import models

class Devloper(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_photo = models.ImageField(upload_to="developer/")

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github = models.URLField()
    gist = models.URLField()
    photo = models.ImageField(upload_to="projects/")
    developers = models.ManyToManyField(to=Devloper)
