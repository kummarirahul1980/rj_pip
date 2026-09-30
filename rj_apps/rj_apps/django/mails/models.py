from django.db import models
from rj_mails.mails import APP_EMAIL as sender_email, MailTypeChoices
# Create your models here.
 

class MailType(models.TextChoices):
    TEXT = MailTypeChoices.TEXT
    HTML = MailTypeChoices.HTML
    OTHER = MailTypeChoices.OTHER

class EmailLogger(models.Model):


    sent_at = models.DateTimeField(auto_now_add=True)
    html = models.TextField(null=True)
    subject  = models.CharField(null=True, max_length=1000)
    text_message = models.TextField(null=False)
    sender_email = models.EmailField(default=sender_email)
    receiver_email = models.EmailField(null=False)
    sent_as_html = models.BooleanField(default=False)
    mail_type = models.CharField(default=MailType.TEXT, choices=MailType)

    @staticmethod
    def write_log(sender_email, reciever_email, text_message, subject="",mail_type = MailTypeChoices.TEXT,html_message=None   ):
        if mail_type == MailTypeChoices.HTML and   html_message:
            raise TypeError("'html_message' argument is missing or none. It should not be none.")
        obj = EmailLogger.objects.create(html = html_message, 
                                         subject = subject,
                                         text_message=text_message,
                                         html  = html_message,
                                         sender_email = sender_email, 
                                         reciever_email = reciever_email, 
                                         sent_as_html  = bool(mail_type == MailTypeChoices.HTML),
                                         mail_type = mail_type)
        
        return obj

        