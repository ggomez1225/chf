from django.db import models
from django.contrib import admin


class Venue(models.Model):
    """The Venue for an event"""
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    postal = models.TextField(null=True, blank=True)


    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Venue: %s (%s)' % (self.name, self.state)

admin.site.register(Venue)


class Event(models.Model):
    """The Event"""
    name = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    venue = models.ForeignKey('Venue')


    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Event: %s (%s)' % (self.name, self.venue)

admin.site.register(Event)


class Area(models.Model):
    '''The Area at an event'''
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    place_number = models.TextField(null=True, blank=True)
    event = models.ForeignKey('Event')


    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Area: %s (%s)' % (self.name, self.place_number)

admin.site.register(Area)
