from django.db import models
from category.models import Category

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    completed = models.BooleanField()
    category = models.ManyToManyField(Category)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
