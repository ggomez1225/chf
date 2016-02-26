# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456204486.5158415
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/event/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['navbar_list', 'navbar_list_right']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_list():
            return render_navbar_list(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def navbar_list_right():
            return render_navbar_list_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_list'):
            context['self'].navbar_list(**pageargs)
        

        __M_writer('<!-- navbar_list -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_list_right'):
            context['self'].navbar_list_right(**pageargs)
        

        __M_writer('<!-- navbar_list_right -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_list():
            return render_navbar_list(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'products' else ''))
        __M_writer('"><a href="/catalog/products">Products</a></li>\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'manager' else ''))
        __M_writer('"><a href="/manager/users">Users</a></li>\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'events' else ''))
        __M_writer('"><a href="/event/events">Events</a></li>\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'venue' else ''))
        __M_writer('"><a href="/event/venues">Venue</a></li>\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'areas' else ''))
        __M_writer('"><a href="/event/areas">Area</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_list_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def navbar_list_right():
            return render_navbar_list_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated():
            __M_writer('        <li class="dropdown">\r\n          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Welcome ')
            __M_writer(str( request.user.first_name))
            __M_writer(' <span class="caret"></span></a>\r\n          <ul class="dropdown-menu">\r\n            <li><a href="/account/manage">My Account</a></li>\r\n            <li><a href="#">My preferences</a></li>\r\n            <li><a href="#">Payment Info</a></li>\r\n            <li role="separator" class="divider"></li>\r\n            <li><a href="/account/logout">Logout</a></li>\r\n          </ul>\r\n        </li>\r\n')
        else:
            __M_writer('        <!-- Do not add a link to the login link, this is handled by the JavaScript, and ajax modal associated with the id -->\r\n        <li><a href="/account/signup">Register as new user</a></li>\r\n        <li><a href="#" type="submit" value="send" id="loginbutton"><button></a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "app_base.htm", "filename": "D:/Jason/Documents/CHF/CHF/event/templates/app_base.htm", "line_map": {"64": 5, "65": 5, "66": 6, "67": 6, "68": 7, "69": 7, "70": 8, "71": 8, "77": 11, "84": 11, "85": 12, "86": 13, "87": 14, "88": 14, "89": 23, "90": 24, "28": 0, "96": 90, "38": 1, "43": 9, "48": 28, "54": 3, "61": 3, "62": 4, "63": 4}}
__M_END_METADATA
"""
