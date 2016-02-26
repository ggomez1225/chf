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


@permission_required('event.add_area', login_url='/homepage/index/')
@view_function
def process_request(request):
    '''Lists the Events in a table on the screen'''
    events = emod.Event.objects.all().order_by('name')
    venues = emod.Venue.objects.all().order_by('name')
    areas = emod.Area.objects.all().order_by('name')
    template_vars = {
    'events': events,
    'venues': venues,
    'areas': areas,
    }
    return dmp_render_to_response(request, 'events.html', template_vars)


# Create a event
@permission_required('event.add_area', login_url='/homepage/index/')
@view_function
def create(request):
    '''Create a Event'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            event = emod.Event()
            event.name = form.cleaned_data.get('name')
            event.start_date = form.cleaned_data.get('start_date')
            event.end_date = form.cleaned_data.get('end_date')
            event.venue = form.cleaned_data.get('venue')
            event.save()
            return HttpResponseRedirect('/event/events')
        print(form.errors)
    template_vars = {
    'form': form,
    }
    return dmp_render_to_response(request, 'events.create.html', template_vars)


class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(label='Start Date', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control datepicker datetimepicker', 'data-date-format': 'yyyy-mm-dd'}))
    end_date = forms.DateField(label='End Date', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control datepicker datetimepicker', 'data-date-format': 'yyyy-mm-dd'}))
    venue = forms.ModelChoiceField(label='venue', required=False, queryset=emod.Venue.objects.order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))


@permission_required('event.change_event', login_url='/homepage/index/')
@view_function
def edit(request):
    '''Edits a event'''
    try:
        event = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/event/events/')
    # process the form
    form = EditForm(initial=model_to_dict(event))
    areas = emod.Area.objects.order_by('name').filter(event_id=event.id)
    if request.method == 'POST':  # just submitted the form
        form = EditForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                # save data and redirect, create a event object, and set equal to session event variable
                # THIS IS DIFFERENT THAN CREATE
                event = emod.Event(id=request.urlparams[0])
                event.name = form.cleaned_data.get('name')
                event.start_date = form.cleaned_data.get('start_date')
                event.end_date = form.cleaned_data.get('end_date')
                event.venue = form.cleaned_data.get('venue')
                event.save()
                return HttpResponseRedirect('/event/events')
    # show the edit form html
    template_vars = {
        'form': form,
        'areas': areas,
        'event': event,
    }
    return dmp_render_to_response(request, 'events.edit.html', template_vars)


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(label='Start Date', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}))
    end_date = forms.DateField(label='End Date', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}))
    venue = forms.ModelChoiceField(label='venue', required=False, queryset=emod.Venue.objects.order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))


@permission_required('event.delete_event', login_url='/homepage/index/')
@view_function
def delete(request):
    '''Deletes a event'''
    try:
        event = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/event/events/')
    # delete the event
    event.delete()
    return HttpResponseRedirect('/event/events/')
