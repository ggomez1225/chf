from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account.models import User


@view_function
def process_request(request):
    # if already logged in.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/account/manage/')

    # Process the form
    form = SignupForm()
    if request.method == 'POST': # Just submitted the form
        form = SignupForm(request.POST)
        if form.is_valid():
            # create a user object
            u = User()
            # fill the user object with the data from the form
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.set_password(form.cleaned_data.get('password'))
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.save()
            u2 = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, u2)
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'SignupForm': form
    }

    return dmp_render_to_response(request, 'signup.html', template_vars)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', required=True, max_length=100)
    # email = forms.CharField(label='Email', required=True)
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', required=True, max_length=100, widget=forms.PasswordInput())
    address1 = forms.CharField(label='Address 1', required=True, max_length=100)
    address2 = forms.CharField(label='Address 2', required=True, max_length=100)
    # I will ask for this information if they go to account Manage Form, but not required
    # state = forms.CharField(label='State', required=True, max_length=100)
    # postal = forms.CharField(label='Zip Code', required=True, max_length=100)
    # birth = forms.CharField(label='Birthdate', required=True, max_length=100)
    # phone_number = forms.CharField(label='Phone Number', required=True, max_length=100)


def clean_username(self):
    # Is the username already taken
    username = self.cleaned_data.get('username')
    # if not username.lower().startswith('a'):
    #     raise forms.ValidationError('Please start your username with the letter "a".') #raise creates an error that will be caught in the is_valid method in the django library.
    # check for uniqueness of the username
    # Method 1 for checking - returns the user or raises exception
    # try:
    #     user = User.objects.get(username=username)
    #     raise forms.ValidationError('This username is already taken. Please choose a new username.')
    # except User.DoesNotExist as e:
    #     pass #This is that we hope for - means unique username
    # return username
    # Method 2
    # users = User.objects.filter(username=username)
    # if len(users)>0:
    #     raise forms.ValidationError('This username is already taken. Please choose a new username.')
    # return username
    # Method 3
    if User.objects.filter(username=username).count() > 0:
        raise forms.ValidationError('This username is already taken. Please choose a new username.')
    return username


def clean(self):# Deals with two or more fields, must be the final method
    if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
        raise forms.ValidationError('Your passwords do not match. Please try again.')
    return self.cleaned_data
