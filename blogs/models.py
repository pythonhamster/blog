from django.db import models, transaction, IntegrityError
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        


class Blog(models.Model):
    choices = [("unpublished", "unpublished"), ("published", "published")]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog/")
    published = models.CharField(choices=choices, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, editable=False)
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True, blank=True)

    