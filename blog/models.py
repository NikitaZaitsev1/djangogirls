from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    full_name = models.CharField(max_length=256, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронный адрес')
    phone = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    active = models.BooleanField(default=True, verbose_name='В работе')

    class Meta:
        db_table = "feedback"
        unique_together = ("full_name", "email", "active")
        verbose_name = "Обращение гражданина"
        verbose_name_plural = "Обращения граждан"
