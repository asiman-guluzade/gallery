from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=False, blank=False)

    def __str__(self) -> str:
        return self.description
# Create your models here.
