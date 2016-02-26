from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin


class User(AbstractUser):
    """In class example"""
    address1 = models.TextField(null=True, blank=True)  # labeled as address
    address2 = models.TextField(null=True, blank=True)  # not included
    state = models.TextField(null=True, blank=True)  # not included, but city is
    postal = models.TextField(null=True, blank=True)  # not included
    birth = models.DateField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)


    def __str__(self):
        '''Prints for debugging purposes'''
        return 'User: %s (%s)' % (self.get_full_name(), self.username)

admin.site.register(User)
