from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    # No need for is_student field as all users are students by default

    def __str__(self):
        return self.full_name if self.full_name else self.username