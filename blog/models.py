from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )

    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите текст", **NULLABLE
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name

# Create your models here.
