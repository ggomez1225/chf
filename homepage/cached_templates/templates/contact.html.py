# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454486488.057995
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/chf/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <form class="form-horizontal" method="POST">\r\n<fieldset>\r\n\r\n<!-- Form Name -->\r\n<legend>Contact Us</legend>\r\n\r\n<!-- Text input-->\r\n<div class="form-group">\r\n  <label class="col-md-4 control-label" for="full_name">Full Name</label>\r\n  <div class="col-md-4">\r\n  <input id="full_name" name="full_name" type="text" placeholder="John Doe" class="form-control input-md" required="">\r\n  <span class="help-block">Please enter your full name</span>\r\n  </div>\r\n</div>\r\n\r\n<!-- Text input-->\r\n<div class="form-group">\r\n  <label class="col-md-4 control-label" for="email">Email Address</label>\r\n  <div class="col-md-4">\r\n  <input id="email" name="email" type="text" placeholder="John@doe.com" class="form-control input-md">\r\n  <span class="help-block">Please enter your email address so that we can respond to your inquiry.</span>\r\n  </div>\r\n</div>\r\n\r\n<!-- Text input-->\r\n<div class="form-group">\r\n  <label class="col-md-4 control-label" for="subject">Subject:</label>\r\n  <div class="col-md-5">\r\n  <input id="subject" name="subject" type="text" placeholder="Questions about Colonial Heritage Foundation" class="form-control input-md">\r\n\r\n  </div>\r\n</div>\r\n\r\n<!-- Textarea -->\r\n<div class="form-group">\r\n  <label class="col-md-4 control-label" for="comments">Comments</label>\r\n  <div class="col-md-4">\r\n    <textarea class="form-control" id="comments" name="comments" placeholder="I have a question about the Colonial Heritage Foundation."></textarea>\r\n  </div>\r\n</div>\r\n\r\n<!-- Button -->\r\n<div class="form-group">\r\n  <label class="col-md-4 control-label" for="submit"></label>\r\n  <div class="col-md-4">\r\n    <button id="submit" name="submit" class="btn btn-default">Submit</button>\r\n  </div>\r\n</div>\r\n\r\n</fieldset>\r\n</form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "D:/Jason/Documents/CHF/chf/homepage/templates/contact.html", "line_map": {"35": 1, "52": 3, "40": 56, "58": 52, "28": 0, "46": 3}, "source_encoding": "utf-8", "uri": "contact.html"}
__M_END_METADATA
"""
