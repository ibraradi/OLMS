from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='accounts/profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.full_name if self.full_name else self.username