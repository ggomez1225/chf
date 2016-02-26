# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453578668.9570484
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        __M_writer('\r\n  <div class="content">\r\n  <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">\r\n<div class="panel panel-default">\r\n  <div class="panel-heading" role="tab" id="headingOne">\r\n    <h4 class="panel-title">\r\n      <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">\r\n        What is the Colonial Heritage Foundation?\r\n      </a>\r\n    </h4>\r\n  </div>\r\n  <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">\r\n    <div class="panel-body">\r\n    The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.\r\n    For more information please see our about page <a href="/homepage/about">here:<a/>\r\n    </div>\r\n  </div>\r\n</div>\r\n<div class="panel panel-default">\r\n  <div class="panel-heading" role="tab" id="headingTwo">\r\n    <h4 class="panel-title">\r\n      <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">\r\n        What is the Colonial Heritage Festival?\r\n      </a>\r\n    </h4>\r\n  </div>\r\n  <div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">\r\n    <div class="panel-body">\r\n      This multi-day historic and cultural activity is held each year in the shade of the monumental trees of the Scera Park in Orem.  Attracting in excess of 40,000 visitors annually, the event is the largest of its kind west of the Mississippi River with more than 100 artisans, educators, and re-enactors.  These volunteers establish a Colonial American village and demonstrate everyday life from various periods of era that preceded the American Revolution.  The Blacksmith, the cooper, the potter, the baker, and the coffin maker are just a few of the period shops that come to life with continuous demonstrations of eighteenth century craftsmanship. In addition storytellers and re-enactors portray famous and lesser known Americans who shaped the events that led to forming of a new nation in the new world.  Cannons and a 1700\'s printing press are a couple of the main attractions to the event which helps students, young and old, feel a deep appreciation for history, culture, values and skills of our founding generation.  More information about the Colonial Heritage Festival is available at http://festival.colonialheritage.org.\r\n    </div>\r\n  </div>\r\n</div>\r\n<div class="panel panel-default">\r\n  <div class="panel-heading" role="tab" id="headingThree">\r\n    <h4 class="panel-title">\r\n      <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">\r\n        Do you offer any classes?\r\n      </a>\r\n    </h4>\r\n  </div>\r\n  <div id="collapseThree" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree">\r\n    <div class="panel-body">\r\n      Yes we have a class in Historic Bread Making:  In this class, students learn the basics of making naturally-leavened bread.  We begin with how to culture a start from scratch and proceed to recipes and techniques for making incredibly delicious with the same few ingredients that our colonial forefathers used: wheat, water and salt.  We learn what adaptation need to be made to successfully bake this lean bread in home ovens  Follow our student\'s progress at http://historicbread.colonialheritage.org\r\n    </div>\r\n  </div>\r\n</div>\r\n</div>\r\n  </div><!-- content -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "40": 51, "58": 52, "28": 0, "46": 3}, "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/faq.html", "source_encoding": "utf-8", "uri": "faq.html"}
__M_END_METADATA
"""
