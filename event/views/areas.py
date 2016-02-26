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


@permission_required('event.change_area', login_url='/homepage/index/')
@view_function
def process_request(request):
    '''Lists the Areas in a table on the screen'''
    areas = emod.Area.objects.all().order_by('name')
    template_vars = {
    'areas': areas,
    }
    return dmp_render_to_response(request, 'areas.html', template_vars)


# Add a area
@permission_required('event.add_area', login_url='/homepage/index/')
@view_function
def create(request):
    '''Create a Area'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            area = emod.Area()
            area.name = form.cleaned_data.get('name')
            area.description = form.cleaned_data.get('description')
            area.place_number = form.cleaned_data.get('place_number')
            area.event = form.cleaned_data.get('event')
            area.save()
            return HttpResponseRedirect('/event/areas')
    print(form.errors)
    template_vars = {
    'form': form,
    }
    return dmp_render_to_response(request, 'areas.create.html', template_vars)

class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Address', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_number = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    event = forms.ModelChoiceField(label='Creator', required=False, queryset=emod.Event.objects.order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))


@permission_required('event.change_area', login_url='/homepage/index/')
@view_function
def edit(request):
    '''Edits a area'''
    try:
        area = emod.Area.objects.get(id=request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect('/event/areas/')
    # process the form
    id=request.urlparams[1]
    form = EditForm(initial=model_to_dict(area))
    if request.method == 'POST':  # just submitted the form
        form = EditForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                # save data and redirect, create a area object, and set equal to session area variable
                # THIS IS DIFFERENT THAN CREATE
                area = emod.Area()
                area.name = form.cleaned_data.get('name')
                area.description = form.cleaned_data.get('description')
                area.place_number = form.cleaned_data.get('place_number')
                event = emod.Event.objects.get(id=request.urlparams[1])
                area.event = event
                area.save()
                return HttpResponseRedirect('/event/events.edit/'+id)
    areas = emod.Area.objects.all().order_by('name').filter(id=area.id)
    # show the edit form html
    template_vars = {
        'form': form,
        'areas': areas,
        'id': id,
    }
    return dmp_render_to_response(request, 'areas.edit.html', template_vars)


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Address', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_number = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    event = forms.ModelChoiceField(label='Creator', required=False, queryset=emod.Event.objects.order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))


@permission_required('event.delete_area', login_url='/homepage/index/')
@view_function
def delete(request):
    '''Deletes a area'''
    try:
        area = emod.Area.objects.get(id=request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect('/event/areas/')
    # delete the area
    area.delete()
    return HttpResponseRedirect('/event/areas/')


@permission_required('catalog.add_product', login_url='/homepage/index/')
@view_function
def add(request):
    '''Add an Area'''
    # process the form
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            area = emod.Area()
            area.name = form.cleaned_data.get('name')
            area.description = form.cleaned_data.get('description')
            area.place_number = form.cleaned_data.get('place_number')
            area.event = emod.Event.objects.get(id=request.urlparams[0])
            area.save()
            return HttpResponseRedirect('/event/events.edit/'+request.urlparams[0])
        print(form.errors)
    template_vars = {
    'form': form,
    }
    return dmp_render_to_response(request, 'areas.add.html', template_vars)

class AddForm(forms.Form):
    name = forms.CharField(label='Name', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Address', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_number = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # event = forms.ModelChoiceField(label='Creator', required=False, queryset=emod.Event.objects.order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))  # This is passed in through the urlparams
