from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from .models import CustomUser
# from .tasks import send_activation_email_task


# @receiver(post_save, sender=CustomUser)
# def send_activation_email(sender, instance, created, **kwargs):
#     if created and not instance.is_active:
#         uid = urlsafe_base64_encode(force_bytes(instance.pk))
#         token = default_token_generator.make_token(instance)
#
#         activation_link = f"http://localhost:8000/api/user/activate/{uid}/{token}/"
#         subject = "Активация аккаунта"
#         message = f"Здравствуйте, {instance.email}!\n\nПожалуйста, активируйте свой аккаунт по ссылке:\n{activation_link}\n\nСпасибо!"
#
#         send_activation_email_task.delay(subject, message, instance.email)
