from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account import models as amod
from catalog import models as cmod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group


@permission_required('account.add_user', login_url='/homepage/index/')
@view_function
def process_request(request):
    '''Lists the users in a table on the screen'''
    users = amod.User.objects.all().order_by('first_name', 'last_name')

    template_vars = {
        'users': users,
    }
    return dmp_render_to_response(request, 'users.html', template_vars)


# Create a user
@permission_required('account.add_user', login_url='/homepage/index/')
@view_function
def create(request):
    '''Creates a user'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':  # Just submitted the form
        form = CreateForm(request.POST)
        if form.is_valid():
            # create a user object
            u = amod.User()
            # fill the user object with the data from the form
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.email = form.cleaned_data.get('email')
            u.set_password(form.cleaned_data.get('password'))
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.save()  # required to save twice
            for group in form.cleaned_data['groups']:
                u.groups.add(group)
            for permission in form.cleaned_data['user_permissions']:
                u.user_permissions.add(permission)
            u.save()
            return HttpResponseRedirect('/manager/users/')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.create.html', template_vars)


class CreateForm(forms.Form):
    # fields
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', required=True, max_length=100, widget=forms.PasswordInput())
    address1 = forms.CharField(label='Address 1', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth = forms.DateField(label='Birthday', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'id': 'datetimepicker', 'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}))
    phone_number = forms.CharField(label='Phone Number', required=False, widget=forms.TextInput(attrs={'type': 'tel'}))
    groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    user_permissions = forms.ModelMultipleChoiceField(label='Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    def clean_username(self):
        # Is the username already taken
        username = self.cleaned_data.get('username')
        if amod.User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('This username is already taken. Please choose a new username.')
        return username

    def clean(self):  # Deals with two or more fields, must be the final method
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match. Please try again.')
        return self.cleaned_data


@permission_required('account.change_user', login_url='/homepage/index/')
@view_function
def edit(request):
    '''Edits a user'''
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')
    # process the form
    form = EditForm(initial=model_to_dict(user))
    u = amod.User.objects.get(id=request.urlparams[0])
    if request.method == 'POST':  # just submitted the form
        form = EditForm(request.POST)
        form.user = amod.User.objects.get(id=request.urlparams[0])
        if form.is_valid():
            # save data and redirect, create a user object, and set equal to session user variable
            # THIS IS DIFFERENT THAN LOGIN
            u = amod.User.objects.get(id=request.urlparams[0])
            # fill the user object with the data from the form
            u.username = form.cleaned_data.get('username')
            u.email = form.cleaned_data.get('email')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.state = form.cleaned_data.get('state')
            u.postal = form.cleaned_data.get('postal')
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.save()  # required to save twice
            u.groups.clear()
            u.user_permissions.clear()
            # print('Group name:', form.cleaned_data['groups'])
            for group in form.cleaned_data['groups']:
                u.groups.add(group)
            for permission in form.cleaned_data['user_permissions']:
                u.user_permissions.add(permission)
            u.save()
            return HttpResponseRedirect('/manager/users/')
    # show the edit form html
    template_vars = {
        'form': form,
        'u': u,
    }
    return dmp_render_to_response(request, 'users.edit.html', template_vars)


class EditForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}))
    # password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    # password2 = forms.CharField(label='Password Confirmation', required=True, max_length=100, widget=forms.PasswordInput())
    address1 = forms.CharField(label='Address 1', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth = forms.DateField(label='Birthday', required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'id': 'datetimepicker', 'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}))
    phone_number = forms.CharField(label='Phone Number', required=False, widget=forms.TextInput(attrs={'type': 'tel'}))
    groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    user_permissions = forms.ModelMultipleChoiceField(label='Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = amod.User.objects.get(username=username)
            if self.user == user:
                pass
            else:
                raise forms.ValidationError('This username is already taken. Please choose a new username.')
        except amod.User.DoesNotExist as e:
            pass
        return username


@permission_required('account.delete_user', login_url='/homepage/index/')
@view_function
def delete(request):
    '''Deletes a user'''
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')
    # delete the user
    user.delete()
    return HttpResponseRedirect('/manager/users/')


@permission_required('account.change_user', login_url='/homepage/index/')
@view_function
def cpass(request):
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')
    # Process the form
    form = PasswordForm()
    if request.method == 'POST':  # Just submitted the form
        form = PasswordForm(request.POST)
        form.user = amod.User.objects.get(id=request.urlparams[0])
        if form.is_valid():
            # create a user object
            u = amod.User.objects.get(id=request.urlparams[0])
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return HttpResponseRedirect('/manager/users/')
    template_vars = {
        'form': form
    }
    return dmp_render_to_response(request, 'users.cpass.html', template_vars)


class PasswordForm(forms.Form):
    password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', required=True, max_length=100, widget=forms.PasswordInput())

    def clean(self):  # Deals with two or more fields, must be the final method
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match. Please try again.')
        return self.cleaned_data
