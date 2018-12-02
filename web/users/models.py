from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Warehouse Manager'),
        (2, 'Supplier'),
        (3, 'Warehouse Employee'),
    )
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
