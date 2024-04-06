from django.core.mail import send_mail
from decouple import config as de_config
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

HOST = de_config('HOST')


def send_confirmation_email(user, code):
    link = f'http://{HOST}/account/activate/{code}'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка работает один раз!',
        de_config('EMAIL_USER'),
        [user],
        fail_silently=False,
    )


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f"Привет,\n\nЧтобы сбросить пароль, перейдите по этой ссылке:\n\nhttp://{HOST}/api/password_reset/confirm/\n\n\tИ введите вот этот токен\t{reset_password_token.key}"

    send_mail(
        "Сброс пароля",
        email_plaintext_message,
        de_config('EMAIL_USER'),
        [reset_password_token.user.email],
)