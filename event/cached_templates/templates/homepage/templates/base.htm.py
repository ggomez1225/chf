# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456037047.9850876
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main_body', 'navbar_list_right', 'content_left', 'content_full', 'title', 'navbar_list', 'alert', 'message', 'main_header', 'content_right', 'content', 'footer', 'navbar_brand']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_body():
            return render_main_body(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def navbar_list():
            return render_navbar_list(context._locals(__M_locals))
        def message():
            return render_message(context._locals(__M_locals))
        def main_header():
            return render_main_header(context._locals(__M_locals))
        def navbar_brand():
            return render_navbar_brand(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def navbar_list_right():
            return render_navbar_list_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_full():
            return render_content_full(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <link rel="shortcut icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/ink-and-feather-quill-clipart.jpg">\r\n\r\n    <title>\r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n    </title>\r\n\r\n')
        __M_writer('    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css"/>\r\n    <!-- <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap-datetimepicker.min.css"/> -->\r\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/datepicker.css"/>\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.min.js"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_body'):
            context['self'].main_body(**pageargs)
        

        __M_writer('<!-- main_body -->\r\n\r\n')
        __M_writer('    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\r\n    <!-- <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/js/bootstrap-datetimepicker.min.js"></script> -->\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap-datepicker.js"></script>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_body():
            return render_main_body(context)
        def navbar_list_right():
            return render_navbar_list_right(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_left():
            return render_content_left(context)
        def footer():
            return render_footer(context)
        def content_full():
            return render_content_full(context)
        def navbar_list():
            return render_navbar_list(context)
        def alert():
            return render_alert(context)
        def main_header():
            return render_main_header(context)
        def message():
            return render_message(context)
        def navbar_brand():
            return render_navbar_brand(context)
        def content():
            return render_content(context)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n      <div class="container-fluid" id="message">\r\n        <div class="row">\r\n          <div class="col-md-12">\r\n            <h1>\r\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        __M_writer('<!-- message -->\r\n            </h1>\r\n          </div>\r\n        </div>\r\n      </div><!-- Message -->\r\n\r\n      <header>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_header'):
            context['self'].main_header(**pageargs)
        

        __M_writer('<!-- main_header -->\r\n      </header>\r\n\r\n      <div class="container-fluid">\r\n        <div class="row">\r\n          <div class="col-md-12" id="content_full">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_full'):
            context['self'].content_full(**pageargs)
        

        __M_writer('\r\n          </div>\r\n        </div>\r\n      </div><!-- container-fluid -->\r\n\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-2"  id="content_left">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('<!-- content_left -->\r\n          </div><!-- left -->\r\n          <div class="col-md-8" id="content">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('<!-- content -->\r\n          </div><!-- Center -->\r\n          <div class="col-md-2" id="content_right">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('<!-- content_right -->\r\n          </div><!-- Right -->\r\n        </div><!-- row -->\r\n      </div><!-- container -->\r\n\r\n      <footer>\r\n          <nav class="navbar navbar-default navbar-fixed-bottom">\r\n              <div class="container">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('<!-- footer -->\r\n              </div>\r\n            </nav>\r\n      </footer>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_list_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_list_right():
            return render_navbar_list_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <li><a href="#">Login</a></li>\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_full(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_full():
            return render_content_full(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n        homepage\r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_list():
            return render_navbar_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Test navbar_list\r\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="alert alert-warning alert-dismissible" role="alert" id="alert_message">\r\n                <button type="button" class="close" data-dismiss="alert" aria-label="Close">\r\n                <span aria-hidden="true">&times;</span></button>\r\n                <strong>Warning!</strong> Better check yourself, you\'re not looking too good.\r\n              </div>\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def message():
            return render_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Test message\r\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_list_right():
            return render_navbar_list_right(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navbar_brand():
            return render_navbar_brand(context)
        def navbar_list():
            return render_navbar_list(context)
        def alert():
            return render_alert(context)
        def main_header():
            return render_main_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('<!-- alert -->\r\n\r\n          <nav class="navbar navbar-default">\r\n            <div class="container-fluid">\r\n              <!-- Brand and toggle get grouped for better mobile display -->\r\n              <div class="navbar-header">\r\n                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n                  <span class="sr-only">Toggle navigation</span>\r\n                  <span class="icon-bar"></span>\r\n                  <span class="icon-bar"></span>\r\n                  <span class="icon-bar"></span>\r\n                </button>\r\n                <a class="navbar-brand" href="/homepage/index">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_brand'):
            context['self'].navbar_brand(**pageargs)
        

        __M_writer('\r\n                </a>\r\n              </div>\r\n\r\n              <!-- Collect the nav links, forms, and other content for toggling -->\r\n              <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                <ul class="nav navbar-nav">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_list'):
            context['self'].navbar_list(**pageargs)
        

        __M_writer('<!-- navbar_list -->\r\n                </ul>\r\n                <ul class="nav navbar-nav navbar-right">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_list_right'):
            context['self'].navbar_list_right(**pageargs)
        

        __M_writer('<!-- navbar_list_right -->\r\n                </ul>\r\n              </div><!-- /.navbar-collapse -->\r\n            </div><!-- /.container-fluid -->\r\n          </nav>\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('                  ')

        import datetime
        current_year = datetime.date.today()
                          
        
        __M_writer('\r\n                  Copyright &copy; Colonial Heritage Foundation ')
        __M_writer(str( current_year.year ))
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_brand(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navbar_brand():
            return render_navbar_brand(context)
        __M_writer = context.writer()
        __M_writer('\r\n                  <img class="media-left media-object media-bottom" alt="CHF Logo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/CHFlogoH2.png" height="35"/>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"328": 125, "130": 33, "334": 129, "341": 69, "135": 41, "140": 91, "270": 48, "17": 4, "19": 0, "350": 70, "150": 107, "280": 71, "201": 97, "155": 111, "285": 80, "160": 115, "290": 85, "219": 78, "207": 15, "165": 130, "296": 114, "348": 69, "326": 123, "171": 83, "333": 128, "302": 114, "349": 70, "177": 83, "308": 110, "53": 2, "54": 4, "55": 5, "314": 110, "59": 5, "60": 12, "61": 12, "320": 123, "66": 17, "67": 21, "68": 21, "69": 21, "70": 22, "71": 22, "72": 23, "73": 23, "74": 25, "75": 25, "76": 26, "77": 26, "78": 29, "79": 29, "80": 29, "335": 129, "85": 134, "86": 137, "87": 137, "88": 137, "89": 138, "90": 138, "91": 139, "92": 139, "93": 141, "94": 141, "95": 141, "225": 78, "327": 125, "356": 350, "101": 33, "195": 97, "145": 98, "275": 56, "231": 50, "237": 50, "189": 106, "243": 39, "249": 39, "255": 48, "183": 106, "213": 15}, "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/base.htm", "source_encoding": "utf-8", "uri": "/homepage/templates/base.htm"}
__M_END_METADATA
"""
