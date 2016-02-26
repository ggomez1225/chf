# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456244709.0413878
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/catalog/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


from catalog import models as cmod 

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
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p class="text-right"><a href="/catalog/products.create/" class="btn btn-primary">Create Object</a></p>\r\n\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Type</th>\r\n            <th>Picture</th>\r\n            <th>Quantity</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for product in products:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( product.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( product.__class__.__name__ ))
            __M_writer('</td>\r\n                <td><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/product_images/')
            __M_writer(str( product.image ))
            __M_writer('" style="height:100px"/></td>\r\n                <td>\r\n')
            if isinstance(product, cmod.BulkProduct):
                __M_writer('                    <span class="quantity">14</span>\r\n                    <a href="/catalog/products.get_quantity/')
                __M_writer(str(product.id))
                __M_writer('" class="glyphicon glyphicon-refresh refresh_button"></a>\r\n')
            __M_writer('                </td>\r\n                <td>\r\n                    <a href="/catalog/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('">Edit</a>\r\n                    |\r\n                    <a href="/catalog/products.delete/')
            __M_writer(str( product.id ))
            __M_writer('" class="delete_button">Delete</a>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <!-- Modal -->\r\n    <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\r\n        <div class="modal-dialog" role="document">\r\n            <div class="modal-content">\r\n                <div class="modal-header">\r\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">\r\n                        <span aria-hidden="true"></span>\r\n                    </button>\r\n                    <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\r\n                </div><!-- Modal Header -->\r\n                <div class="modal-body">\r\n                    Delete this product?\r\n                </div>\r\n                <div class="modal-footer">\r\n                    <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\r\n                    <button class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "line_map": {"65": 4, "71": 6, "94": 25, "80": 6, "81": 17, "82": 18, "83": 19, "84": 19, "85": 20, "86": 20, "87": 21, "88": 21, "89": 21, "90": 21, "91": 23, "92": 24, "93": 25, "30": 0, "95": 27, "96": 29, "97": 29, "98": 31, "99": 31, "100": 35, "17": 1, "42": 1, "43": 2, "48": 4, "53": 56, "59": 4, "106": 100}, "source_encoding": "utf-8", "filename": "D:/Jason/Documents/CHF/CHF/catalog/templates/products.html"}
__M_END_METADATA
"""
