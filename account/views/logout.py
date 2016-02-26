from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from account.models import User

@view_function
def process_request(request):
    #logout the user
    logout(request)
    #redirect to the Homepage
    return HttpResponseRedirect('/homepage/index')