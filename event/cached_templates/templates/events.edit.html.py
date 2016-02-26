# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456291407.626148
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/event/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        event = context.get('event', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        event = context.get('event', UNDEFINED)
        def content():
            return render_content(context)
        areas = context.get('areas', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form class="form-horizontal" method="POST">\r\n    <fieldset>\r\n        ')
        __M_writer(str( form.as_p()))
        __M_writer('\r\n        <!-- Button -->\r\n        <div class="form-group">\r\n          <label class="col-md-4 control-label" for="submit"></label>\r\n          <div class="col-md-4">\r\n            <button id="submit" name="submit" class="btn btn-default">Submit</button>\r\n          </div>\r\n        </div>\r\n    </fieldset>\r\n  </form>\r\n  <!-- Area -->\r\n  <p class="text-right"><a href="/event/areas.add/')
        __M_writer(str( event.id))
        __M_writer('" class="btn btn-primary">Create Area</a></p>\r\n  <table class="table table-striped">\r\n      <tr>\r\n          <th>Name</th>\r\n          <th>Place Number</th>\r\n          <th>Actions</th>\r\n      </tr>\r\n')
        for area in areas:
            __M_writer('          <tr>\r\n              <td>')
            __M_writer(str( area.name ))
            __M_writer('</td>\r\n              <td>')
            __M_writer(str( area.place_number ))
            __M_writer('</td>\r\n              <td>\r\n                  <a href="/event/areas.edit/')
            __M_writer(str( area.id ))
            __M_writer('/')
            __M_writer(str( event.id ))
            __M_writer('/">Edit</a>\r\n                  |\r\n                  <a href="/event/areas.delete/')
            __M_writer(str( area.id ))
            __M_writer('" class="delete_button">Delete</a>\r\n              </td>\r\n          </tr>\r\n')
        __M_writer('  </table>\r\n  <!-- Modal -->\r\n  <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\r\n      <div class="modal-dialog" role="document">\r\n          <div class="modal-content">\r\n              <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                      <span aria-hidden="true"></span>\r\n                  </button>\r\n                  <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\r\n              </div><!-- Modal Header -->\r\n              <div class="modal-body">\r\n                  Are you sure you would like to Delete?\r\n              </div>\r\n              <div class="modal-footer">\r\n                  <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\r\n                  <button class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n              </div>\r\n          </div>\r\n      </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "D:/Jason/Documents/CHF/CHF/event/templates/events.edit.html", "line_map": {"64": 25, "65": 26, "66": 26, "67": 27, "68": 27, "69": 29, "70": 29, "71": 29, "72": 29, "73": 31, "74": 31, "75": 35, "81": 75, "28": 0, "38": 1, "43": 56, "49": 3, "58": 3, "59": 6, "60": 6, "61": 17, "62": 17, "63": 24}, "source_encoding": "utf-8", "uri": "events.edit.html"}
__M_END_METADATA
"""
