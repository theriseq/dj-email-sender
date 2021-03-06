from django.contrib import admin
from .models import Recipient

models = [Recipient]

admin.site.register(models)
