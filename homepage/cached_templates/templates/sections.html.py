# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453581317.4682388
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


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
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"33": 1, "28": 0, "39": 33}, "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/sections.html", "source_encoding": "utf-8", "uri": "sections.html"}
__M_END_METADATA
"""
