from django.contrib.auth import get_user_model

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего обновления записи")

    def __str__(self):
        return f"Отзыв от {self.user.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['created_at']


class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта")
    phone_number = PhoneNumberField('Номер телефона', help_text='Пример: +996700777777')
    description = models.TextField(verbose_name="Информация о студенте")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Client(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта")
    phone_number = PhoneNumberField('Номер телефона', help_text='Пример: +996700777777')
    company = models.CharField(max_length=255, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

