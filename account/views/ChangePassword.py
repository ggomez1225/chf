from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account.models import User

@view_function
def process_request(request):
    #Process the form
    form = PasswordForm()
    if request.method == 'POST': #Just submitted the form
        form = PasswordForm(request.POST)
        form.user = request.user
        if form.is_valid():
            #create a user object
            u = request.user
            #fill the user object with the data from the form
            #When set password is called the user is logged out.
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            u2 = authenticate(username=u.username, password=form.cleaned_data.get('password'))
            login(request, u2)
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'PasswordForm': form
    }

    return dmp_render_to_response(request, 'ChangePassword.html', template_vars)

class PasswordForm(forms.Form):
    CurrentPassword = forms.CharField(label='Current Password', required=True, max_length=100, widget=forms.PasswordInput())
    password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', required=True, max_length=100, widget=forms.PasswordInput())

    def clean_current_password(self):
        if not self.user.check_password(self.cleaned_data.get('CurrentPassword')):
            raise forms.ValidationError('Try your current password again.')

    def clean(self):#Deals with two or more fields, must be the final method
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match. Please try again.')
        return self.cleaned_data
