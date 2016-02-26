# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456204486.4553487
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/event/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


from event import models as emod 

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
        venues = context.get('venues', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        venues = context.get('venues', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <!-- Venue -->\r\n    <p class="text-right"><a href="/event/venues.create/" class="btn btn-primary">Create Venue</a></p>\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>City</th>\r\n            <th>State</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for venue in venues:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( venue.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.city ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.state ))
            __M_writer('</td>\r\n                <td>\r\n                    <a href="/event/venues.edit/')
            __M_writer(str( venue.id ))
            __M_writer('">Edit</a>\r\n                    |\r\n                    <a href="/event/venues.delete/')
            __M_writer(str( venue.id ))
            __M_writer('" class="delete_button">Delete</a>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <!-- Modal -->\r\n    <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\r\n        <div class="modal-dialog" role="document">\r\n            <div class="modal-content">\r\n                <div class="modal-header">\r\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                        <span aria-hidden="true"></span>\r\n                    </button>\r\n                    <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\r\n                </div><!-- Modal Header -->\r\n                <div class="modal-body">\r\n                    Are you sure you would like to Delete?\r\n                </div>\r\n                <div class="modal-footer">\r\n                    <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\r\n                    <button class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Current Venues')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "venues.html", "filename": "D:/Jason/Documents/CHF/CHF/event/templates/venues.html", "line_map": {"64": 6, "65": 16, "66": 17, "67": 18, "68": 18, "69": 19, "70": 19, "71": 20, "72": 20, "73": 22, "74": 22, "75": 24, "76": 24, "77": 28, "17": 1, "83": 4, "89": 4, "30": 0, "95": 89, "40": 1, "41": 2, "46": 4, "51": 49, "57": 6}}
__M_END_METADATA
"""
