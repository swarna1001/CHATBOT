from datetime import date
from django.db import models

# Create your models here.
DEGREE_TYPES = (
    ("btech", "B Tech"),
    ("bca", "BCA"),
    ("mca", "MCA"),
    ("mba", "MBA"),
)


class Degree(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=16, unique=True, null=True, blank=True)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=16, unique=True, null=True, blank=True)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class Preference(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=16, unique=True, null=True, blank=True)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=16, unique=True, null=True, blank=True)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class UserInteraction(models.Model):
    message = models.CharField(max_length=256, null=True, blank=True)
    reply = models.CharField(max_length=1024, null=True, blank=True)
    associated_choice_field = models.IntegerField(null=True, blank=True)
    created_at = models.IntegerField(null=True, blank=True)
    user_choice = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.message
