from django.db import models


# must may want

# Create your models here.
class Must(models.Model):
    title = models.CharField(max_length=150, verbose_name='Запись')
    # content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    edited = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Надо'
        verbose_name = 'Надо'
        ordering = ['-published']

    def __str__(self):
        return self.title


class May(models.Model):
    title = models.CharField(max_length=150, verbose_name='Запись')
    # content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Могу'
        verbose_name = 'Могу'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Want(models.Model):
    title = models.CharField(max_length=150, verbose_name='Запись')
    # content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Хочу'
        verbose_name = 'Хочу'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
