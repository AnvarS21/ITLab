import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    PROJECT_MANAGER = 'project_manager'
    UI_UX_DESIGNER = 'ui_ui_designer'
    TESTER = 'tester'

    POSITION_CHOICES = [
        (BACKEND, 'Backend'),
        (FRONTEND, 'Frontend'),
        (PROJECT_MANAGER, 'Project Manager'),
        (UI_UX_DESIGNER, 'UI UX Designer'),
        (TESTER, 'Tester')
    ]

    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=128, verbose_name="ФИО",  blank=True, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name="Должность")
    image = models.ImageField(upload_to='avatars/', verbose_name="Аватар", blank=True, null=True, default='avatars/default_avatar.jpg')
    about_me = models.TextField(blank=True, null=True, verbose_name="О себе")
    activation_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Активационный код")
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def create_activation_code(self):
        code = str(uuid.uuid4())
        return code

    def save(self, *args, **kwargs):
        self.activation_code = self.create_activation_code()
        if self.is_superuser:
            self.is_active = True
        super().save(*args, **kwargs)




    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class SocialLinks(models.Model):
    user = models.OneToOneField(CustomUser, related_name='social', on_delete=models.CASCADE)
    telegram = models.URLField(max_length=512, verbose_name="Телеграм", blank=True, null=True)
    facebook = models.URLField(max_length=512, verbose_name="Фейсбук", blank=True, null=True)
    instagram = models.URLField(max_length=512, verbose_name="Инстаграмм", blank=True, null=True)
    linkedin = models.URLField(max_length=512, verbose_name="Линкдин", blank=True, null=True)
    github = models.URLField(max_length=512, verbose_name="ГитХаб", blank=True, null=True)
    site_cv = models.URLField(max_length=512, verbose_name="Персональный сайт", blank=True, null=True)
    vk = models.URLField(max_length=512, verbose_name="ВКонтакте", blank=True, null=True)

    def __str__(self):
        return f"Сoц сети {self.user}"

    class Meta:
        verbose_name = "Ссылка на соц. сеть"
        verbose_name_plural = "Ссылки на соц. сети"
