from django.db import models
from django.utils.timezone import now

class FailedLoginAttempt(models.Model):
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Failed login attempt by {self.username or 'Unknown'} from {self.ip_address} at {self.timestamp}"