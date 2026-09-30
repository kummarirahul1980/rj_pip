from django.contrib import admin

# Register your models here.
from rj_apps.django.mails.models import *

admin.site.register(EmailLogger)