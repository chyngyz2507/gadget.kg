# from celery import shared_task
# from django.core.mail import send_mail
#
# @shared_task
# def send_activation_email_task(subject, message, recipient):
#     send_mail(subject, message, "admin@gadget.kg", [recipient])

from celery import shared_task

from utils import send_message


@shared_task
def send_message_register(email, id):
    send_message(email, id)
