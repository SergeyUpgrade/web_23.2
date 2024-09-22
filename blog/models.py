from django.db import models

class Blog(models.Model):

    name = models.CharField(max_length=100,verbose_name="Заголовок",)

    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    content = models.TextField(verbose_name="Содержание")

    image = models.ImageField(upload_to="catalog/image",verbose_name="Изображение",help_text="Загрузите изображение")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(default=True)

    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
# Create your models here.
