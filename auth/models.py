from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from datetime import timedelta
from django.utils.timezone import now

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('user', 'User'),
            ('admin', 'Admin'),
            ('farmer', 'Farmer'),
            ('distributor', 'Distributor'),
            ('retailer', 'Retailer'),
        ],
        default='user',
    )
    token_version = models.IntegerField(default=0)
    login_attempts = models.IntegerField(default=0)
    lock_until = models.DateTimeField(null=True, blank=True)
    password_reset_token = models.CharField(max_length=64, null=True, blank=True)
    password_reset_expires = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def create_password_reset_token(self):
        import hashlib
        import os
        reset_token = os.urandom(32).hex()
        self.password_reset_token = hashlib.sha256(reset_token.encode()).hexdigest()
        self.password_reset_expires = now() + timedelta(minutes=10)
        self.save()
        return reset_token