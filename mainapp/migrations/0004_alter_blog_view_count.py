# Generated by Django 5.0.1 on 2024-02-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_blog_blog_is_published_alter_blog_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='количество просмотров'),
        ),
    ]
