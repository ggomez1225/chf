# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456293172.5454962
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/manager/templates/users.edit.html'
_template_uri = 'users.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_right', 'content']


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
        form = context.get('form', UNDEFINED)
        u = context.get('u', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('<!-- content -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        u = context.get('u', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <p><a href="/manager/users.cpass/')
        __M_writer(str( u.id ))
        __M_writer('">Click here to change the password</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <form class="form-horizontal" method="POST">\r\n    <fieldset>\r\n        ')
        __M_writer(str( form.as_p()))
        __M_writer('\r\n        <!-- Button -->\r\n        <div class="form-group">\r\n          <label class="col-md-4 control-label" for="submit"></label>\r\n          <div class="col-md-4">\r\n            <button id="submit" name="submit" class="btn btn-default">Submit</button>\r\n          </div>\r\n        </div>\r\n    </fieldset>\r\n  </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "70": 3, "39": 1, "44": 17, "77": 3, "78": 6, "79": 6, "49": 21, "85": 79, "55": 19, "28": 0, "62": 19, "63": 20}, "source_encoding": "utf-8", "uri": "users.edit.html", "filename": "D:/Jason/Documents/CHF/CHF/manager/templates/users.edit.html"}
__M_END_METADATA
"""
