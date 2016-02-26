from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account.models import User

@view_function
def process_request(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/signup')

    #Process the form
    form = ManageForm(initial={
        # 'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'address1': request.user.address1,
        'address2': request.user.address2,
        'state': request.user.state,
        'postal': request.user.postal,
        # 'birth': request.user.birth,
        # 'phone_number': request.user.phone_number,
        }
    )
    if request.method == 'POST': #Just submitted the form
        form = ManageForm(request.POST)
        form.user = request.user
        if form.is_valid():
            #create a user object, and set equal to session user variable
            #THIS IS DIFFERENT THAN LOGIN
            u = request.user
            #fill the user object with the data from the form
            # u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.state = form.cleaned_data.get('state')
            u.postal = form.cleaned_data.get('postal')
            # u.birth = form.cleaned_data.get('birth')
            # u.phone_number = form.cleaned_data.get('phone_number')
            u.save()
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'ManageForm': form
    }

    return dmp_render_to_response(request, 'manage.html', template_vars)

class ManageForm(forms.Form):
    # username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # birth = forms.CharField(label='Birthdate', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(label='Phone Number', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

# def clean(self):#Deals with two or more fields, must be the final method
#     if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
#         raise forms.ValidationError('Your passwords do not match. Please try again.')
#     return self.cleaned_data
