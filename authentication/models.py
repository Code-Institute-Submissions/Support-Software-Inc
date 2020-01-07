import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Organisation(models.Model):
    '''
    Organisation Table

    id - Organisations ID
    name - Organisations Name (Max length of 255 characters)
    '''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    name = models.TextField(
        max_length=255,
        name="Organisation Name"
        )