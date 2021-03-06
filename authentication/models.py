'''
Models.py file for authentication model

Tables

MyUser - extends django default user model
with extra fields
'''

from django.contrib.auth.models import User
from django.db import models

from organisations.models import Organisation as Org


class MyUser(models.Model):
    '''
    User Table - Extends the base User model via Abstract User
    profile_picture - Image Field that holds the user's profile image
    organisation - One to Many relationship - Organisation table id
    '''
    ROLE_CHOICES = [
        ('AGN', 'Agent'),
        ('USR', 'End User')
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default="USR",
    )
    profile_picture = models.ImageField(
        name="Profile Picture",
        upload_to='',
        null=True,
        blank=True,
    )

    is_organisation_admin = models.BooleanField(
        name="Organisation Admin",
        default=False,
    )

    organisation = models.ForeignKey(
        Org,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username

    def get_email(self):
        '''
        Returns the user's email
        '''
        return self.user.email

    def get_username_and_email(self):
        '''
        Returns the user's username and email
        '''
        return self.user.username + ' (' + self.user.email + ')'
