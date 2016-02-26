# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454787943.5365615
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/account/templates/ChangePassword.html'
_template_uri = 'ChangePassword.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        PasswordForm = context.get('PasswordForm', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('<!-- content -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        PasswordForm = context.get('PasswordForm', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <form class="form-horizontal" method="POST">\r\n    <fieldset>\r\n\r\n        <!-- Form Name -->\r\n')
        __M_writer('        ')
        __M_writer(str(PasswordForm.as_p()))
        __M_writer('\r\n        <!-- Button -->\r\n        <div class="form-group">\r\n          <label class="col-md-4 control-label" for="submit"></label>\r\n          <div class="col-md-4">\r\n            <button id="submit" name="submit" class="btn btn-default">Submit</button>\r\n          </div>\r\n        </div>\r\n\r\n    </fieldset>\r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"36": 1, "57": 44, "54": 3, "55": 44, "56": 44, "41": 56, "63": 57, "28": 0, "47": 3}, "filename": "D:/Jason/Documents/CHF/CHF/account/templates/ChangePassword.html", "uri": "ChangePassword.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
