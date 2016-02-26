# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453583190.1771188
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content', 'content_full']


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
        def content():
            return render_content(context._locals(__M_locals))
        def content_full():
            return render_content_full(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_full'):
            context['self'].content_full(**pageargs)
        

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
        __M_writer('\r\n  Home\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>\r\n    Come checkout some of the amazing ways that we are able to bring history to life!\r\n  </h3>\r\n  <div class="content">\r\n  <div id="bs-carousel" class="carousel fade-carousel slide" data-ride="carousel">\r\n  <!-- Indicators -->\r\n  <ol class="carousel-indicators">\r\n    <li data-target="#bs-carousel" data-slide-to="0" class="active"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="1"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="2"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="3"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="4"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="5"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="6"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="7"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="8"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="9"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="10"></li>\r\n    <li data-target="#bs-carousel" data-slide-to="11"></li>\r\n  </ol>\r\n\r\n  <!-- Wrapper for slides -->\r\n  <div class="carousel-inner" role="listbox" align="center">\r\n    <div class="item slides active" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/2012_GGalbraith_317.jpg" alt="Image 0"/>\r\n')
        __M_writer('    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/IMG_0480.jpg" alt="Image 1"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/IMG_0700.jpg" alt="Image 2"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/IMG_7720.jpg" alt="Image 3"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/Baking_Bread.jpg" alt="Image 4"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/apot4.jpg" alt="Image 5"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/apot3.jpg" alt="Image 6"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/bake3.jpg" alt="Image 7"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/2012_GGalbraith_323.jpg" alt="Image 8"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/bake1.jpg" alt="Image 9"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/IMG_0698.jpg" alt="Image 10"/>\r\n    </div>\r\n    <div class="item slides" id="resp_img">\r\n      <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/IMG_7734.jpg" alt="Image 11"/>\r\n    </div>\r\n  </div>\r\n\r\n  <!-- Controls -->\r\n  <a class="left carousel-control" href="#bs-carousel" role="button" data-slide="prev">\r\n    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\r\n    <span class="sr-only">Previous</span>\r\n  </a>\r\n  <a class="right carousel-control" href="#bs-carousel" role="button" data-slide="next">\r\n    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\r\n    <span class="sr-only">Next</span>\r\n  </a>\r\n  </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_full(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_full():
            return render_content_full(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="jumbotron" style="clear: both; text-align: center;">\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><img border="0" height="90" width="400" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/CHFlogoH2.png">&nbsp;</span>\r\n\r\n    <h4>Come meet history face to face<h4>\r\n    <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/0p.jpg" alt="Boy looking Benjamin Franklin in the eyes"/>\r\n  </div><!-- close jumbotron -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 122, "67": 3, "73": 16, "119": 9, "80": 16, "81": 41, "82": 41, "83": 45, "84": 47, "85": 47, "86": 50, "87": 50, "88": 53, "89": 53, "90": 56, "91": 56, "92": 59, "93": 59, "94": 62, "95": 62, "96": 65, "97": 65, "98": 68, "99": 68, "100": 71, "101": 71, "102": 74, "103": 74, "40": 1, "28": 0, "45": 5, "111": 7, "104": 77, "50": 14, "105": 77, "118": 7, "55": 92, "120": 9, "121": 12, "122": 12, "61": 3}, "source_encoding": "utf-8", "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/index.html", "uri": "index.html"}
__M_END_METADATA
"""
