from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):

    print('>>>>>>Your name is: ', request.POST.get('full_name')),
    print('>>>>>>Your email is: ', request.POST.get('email')),
    print('>>>>>>Your subject is: ', request.POST.get('subject')),
    print('>>>>>>Your comments is: ', request.POST.get('comments')),
    print('>>>>>>in contact.py'),

    template_vars = {

    }

    return dmp_render_to_response(request, 'contact.html', template_vars)
