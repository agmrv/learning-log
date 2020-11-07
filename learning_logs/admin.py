from django.contrib import admin

from learning_logs.models import Topic, Entry  # from .models

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
