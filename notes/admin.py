from django.contrib import admin
from .models import Note
from .models import TimeTracker

# Register your models here.
admin.site.register(Note)
admin.site.register(TimeTracker)