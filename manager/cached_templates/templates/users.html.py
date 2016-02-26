# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456201874.1674933
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/manager/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


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
        users = context.get('users', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Current Users')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p class="text-right"><a href="/manager/users.create/" class="btn btn-primary">Create User</a></p>\r\n\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th>Username</th>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Email</th>\r\n            <th>Groups</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for user in users:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( user.username ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n                <td>\r\n')
            for group in user.groups.order_by('name'):
                __M_writer('                    ')
                __M_writer(str( group.name ))
                __M_writer('\r\n')
            __M_writer('                </td> <!-- Print user group memeberships -->\r\n                <td>\r\n                    <a href="/manager/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('">Edit</a>\r\n                    |\r\n                    <a href="/manager/users.delete/')
            __M_writer(str( user.id ))
            __M_writer('" class="delete_button">Delete</a>\r\n                    |\r\n                    <a href="/manager/users.cpass/')
            __M_writer(str( user.id ))
            __M_writer('">Password</a>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <!-- Modal -->\r\n    <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\r\n        <div class="modal-dialog" role="document">\r\n            <div class="modal-content">\r\n                <div class="modal-header">\r\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                        <span aria-hidden="true">&times;</span>\r\n                    </button>\r\n                    <h4 class="modal-title" id="myModalLabel">Please Confirm Delete</h4>\r\n                </div><!-- Modal Header -->\r\n                <div class="modal-body">\r\n                    Delete this user?\r\n                </div>\r\n                <div class="modal-footer">\r\n                    <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\r\n                    <button class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "users.html", "line_map": {"66": 5, "73": 5, "74": 17, "75": 18, "76": 19, "77": 19, "78": 20, "79": 20, "80": 21, "81": 21, "82": 22, "83": 22, "84": 24, "85": 25, "86": 25, "87": 25, "88": 27, "89": 29, "90": 29, "91": 31, "28": 0, "93": 33, "94": 33, "95": 37, "101": 95, "38": 1, "92": 31, "43": 3, "48": 58, "54": 3, "60": 3}, "filename": "D:/Jason/Documents/CHF/CHF/manager/templates/users.html"}
__M_END_METADATA
"""
