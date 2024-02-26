from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', null=True)
    product_price = models.IntegerField(verbose_name='цена за штуку')
    product_date = models.DateTimeField(verbose_name='дата создания')
    product_last_modified = models.DateTimeField(verbose_name='дата последнего изменения')

    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')
    # created_at = models.DateTimeField(verbose_name='дата создания', null=True)


    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='url для пользователя')
    description = models.TextField(max_length=500, verbose_name='содержимое')
    blog_image = models.ImageField(upload_to='photo_blog/', verbose_name='изображение', **NULLABLE)
    product_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    blog_is_published = models.BooleanField(default=True, verbose_name='опубликован')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.blog_title}'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
        ordering = ('blog_title',)