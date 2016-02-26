from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel

# If you drop/create your database, you need to delete all 'migrations' folders in your project

class Product(PolymorphicModel):
    '''The superclass of all products in our database'''
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateTimeField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Product (abstract): %s (%s)' % (self.name, self.add_date)

admin.site.register(Product)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired', 'No Longer Rentable'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

class RentalProduct(Product):
    '''A Product that is rentable'''
    status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)
    # rental = models.ForeignKey('Rental', null=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Rental Product: %s (%s): ' % (self.name, self.status)

admin.site.register(RentalProduct)

class IndividualProduct(Product):
    '''A product that we track individually'''
    creator = models.ForeignKey('account.User')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Individual Product: %s (%s): ' % (self.name, self.creator.get_full_name())#The end of this line was cutoff in the video

admin.site.register(IndividualProduct)

class BulkProduct(Product):
    '''A product that we track by quantity'''
    quantity = models.IntegerField(default=0)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Bulk Product: %s (%s): ' % (self.name, self.quantity)

admin.site.register(BulkProduct)
