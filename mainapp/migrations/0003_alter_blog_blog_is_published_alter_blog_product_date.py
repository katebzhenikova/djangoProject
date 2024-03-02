# Generated by Django 5.0.1 on 2024-02-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_is_published',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='опубликован'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='product_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата создания'),
        ),
    ]