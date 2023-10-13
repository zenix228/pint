from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категорию'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            args=[self.slug]
        )

class Product(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField('Слаг', max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title'])
        ]

    def get_absolute_url(self):
        return reverse(
            args=[self.id, self.slug]
        )