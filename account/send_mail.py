from django.core.mail import send_mail
from decouple import config as de_config


def send_confirmation_email(user, code):
    link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка работает один раз!',
        de_config('EMAIL_USER'),
        [user],
        fail_silently=False,
    )