# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455034777.6976087
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['navbar_list_right', 'navbar_list']


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
        request = context.get('request', UNDEFINED)
        def navbar_list_right():
            return render_navbar_list_right(context._locals(__M_locals))
        def navbar_list():
            return render_navbar_list(context._locals(__M_locals))
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


def render_navbar_list_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_list_right():
            return render_navbar_list_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def navbar_list():
            return render_navbar_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'manage' else ''))
        __M_writer('"><a href="/account/manage">Manage Account</a></li>\r\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page ==  'ChangePassword' else ''))
        __M_writer('"><a href="/account/ChangePassword">Change Password</a></li>\r\n  <li><a href="/account/logout">Logout</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "line_map": {"67": 3, "38": 1, "28": 0, "74": 3, "75": 4, "76": 4, "77": 5, "78": 5, "48": 28, "43": 7, "84": 78, "54": 9, "60": 9, "61": 27}, "filename": "D:/Jason/Documents/CHF/CHF/account/templates/app_base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
