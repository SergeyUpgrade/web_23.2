# Generated by Django 5.1.1 on 2024-10-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров'),
        ),
    ]