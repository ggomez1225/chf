from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account import models as amod
from catalog import models as cmod
from event import models as emod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group


@permission_required('event.change_venue', login_url='/homepage/index/')
@view_function
def process_request(request):
    '''Lists the Venues in a table on the screen'''
    venues = emod.Venue.objects.all().order_by('name')
    template_vars = {
    'venues': venues,
    }
    return dmp_render_to_response(request, 'venues.html', template_vars)


# Create a venue
@permission_required('event.add_venue', login_url='/homepage/index/')
@view_function
def create(request):
    '''Create a Venue'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            venue = emod.Venue()
            venue.name = form.cleaned_data.get('name')
            venue.address = form.cleaned_data.get('address')
            venue.city = form.cleaned_data.get('city')
            venue.state = form.cleaned_data.get('state')
            venue.postal = form.cleaned_data.get('postal')
            venue.save()
            return HttpResponseRedirect('/event/venues')
        print(form.errors)
    template_vars = {
    'form': form,
    }
    return dmp_render_to_response(request, 'venues.create.html', template_vars)


class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal = forms.CharField(label='Zip Code', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


@permission_required('event.change_venue', login_url='/homepage/index/')
@view_function
def edit(request):
    '''Edits a venue'''
    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/event/venues/')
    # process the form
    form = EditForm(initial=model_to_dict(venue))
    if request.method == 'POST':  # just submitted the form
        form = EditForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                # save data and redirect, create a venue object, and set equal to session venue variable
                # THIS IS DIFFERENT THAN CREATE
                venue = emod.Venue(id=request.urlparams[0])
                venue.name = form.cleaned_data.get('name')
                venue.address = form.cleaned_data.get('address')
                venue.city = form.cleaned_data.get('city')
                venue.state = form.cleaned_data.get('state')
                venue.postal = form.cleaned_data.get('postal')
                venue.save()
                return HttpResponseRedirect('/event/venues')
    areas = emod.Area.objects.all().order_by('name').filter(event_id=venue.id)
    # show the edit form html
    template_vars = {
        'form': form,
        'areas': areas,
    }
    return dmp_render_to_response(request, 'venues.edit.html', template_vars)


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal = forms.CharField(label='Zip Code', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


@permission_required('event.delete_venue', login_url='/homepage/index/')
@view_function
def delete(request):
    '''Deletes a venue'''
    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/event/venues/')
    # delete the venue
    venue.delete()
    return HttpResponseRedirect('/event/venues/')
