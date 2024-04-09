import datetime

from django.db import models
import uuid


class UserRegistrationModel(models.Model):
    full_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False, primary_key=True)
    password = models.CharField(max_length=256, blank=False)
    points = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=20, blank=True, null=True)
    unique_id = models.CharField(max_length=10, default=uuid.uuid4, unique=True)
    registered_on = models.DateTimeField(default=datetime.datetime.now())

