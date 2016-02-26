from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account.models import User

@view_function
def process_request(request):
    #if already logged in.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/account/manage/')

    #Process the form
    form = LoginForm()
    if request.method == 'POST': #Just submitted the form
        form = LoginForm(request.POST)
        if form.is_valid():
            #Log the user in here
            login(request, form.user)
            return HttpResponse('''
                <script>
                    window.location.reload();
                </script>
            ''')

    template_vars = {
        'Loginform': form
    }

    return dmp_render_to_response(request, 'login.html', template_vars)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())

    def clean(self):#Deals with two or more fields, must be the final method
        User = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if User == None:
            raise forms.ValidationError('This username and password do not match our records.')
        self.user = User
        return self.cleaned_data
