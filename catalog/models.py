from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
