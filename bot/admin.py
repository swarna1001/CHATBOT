from django.contrib import admin
from .models import Degree, Preference, Interest, Experience, UserInteraction

# Register your models here.
admin.site.register(Degree)
admin.site.register(Preference)
admin.site.register(Interest)
admin.site.register(Experience)
admin.site.register(UserInteraction)
