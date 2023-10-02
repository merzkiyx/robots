from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Robot

@receiver(post_save, sender=Robot)
def notify_clients(sender, instance, **kwargs):
    if instance.in_stock:

        subject = 'Робот в наличии'
        message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
        from_email = 'robotsshop@gmail.com'  # Наш адрес электронной почты
        recipient_list = [instance.obi_wan_kenobi_mail]  # Адрес клиента
        send_mail(subject, message, from_email, recipient_list)
