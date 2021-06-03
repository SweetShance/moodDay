from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TimeClass)
admin.site.register(MoodLabel)
admin.site.register(MoodData)
admin.site.register(MoodValue)