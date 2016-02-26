# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453393509.30046
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\r\n  <div class="content">\r\n    <div class=WordSection1>\r\n\r\n    <h3><span lang=EN-GB>Website usage terms and conditions</span><span\r\n    lang=EN style=\'mso-ansi-language:EN\'><o:p></o:p></span></h3>\r\n\r\n    <p><span lang=EN style=\'mso-ansi-language:EN\'>Welcome to our website. If you\r\n    continue to browse and use this website, you are agreeing to comply with and be\r\n    bound by the following terms and conditions of use, which together with our\r\n    privacy policy govern [business name]’s relationship with you in relation to\r\n    this website. </span><span lang=EN-GB>If you disagree with any part of these\r\n    terms and conditions, please do not use our website.</span><span lang=EN\r\n    style=\'mso-ansi-language:EN\'><o:p></o:p></span></p>\r\n\r\n    <p><span lang=EN style=\'mso-ansi-language:EN\'>The term ‘[business name]’ or\r\n    ‘us’ or ‘we’ refers to the owner of the website whose registered office is\r\n    [address]. Our company registration number is [company registration number and\r\n    place of registration]. The term ‘you’ refers to the user or viewer of our\r\n    website.<o:p></o:p></span></p>\r\n\r\n    <p><span lang=EN style=\'mso-ansi-language:EN\'>The use of this website is\r\n    subject to the following terms of use:<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>The\r\n    content of the pages of this website is for your general information and use\r\n    only. It is subject to change without notice.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>This\r\n    website uses cookies to monitor browsing preferences. If you do allow cookies\r\n    to be used, the following personal information may be stored by us for use by\r\n    third parties: [insert list of information].<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>Neither\r\n    we nor any third parties provide any warranty or guarantee as to the accuracy,\r\n    timeliness, performance, completeness or suitability of the information and\r\n    materials found or offered on this website for any particular purpose. You\r\n    acknowledge that such information and materials may contain inaccuracies or\r\n    errors and we expressly exclude liability for any such inaccuracies or errors\r\n    to the fullest extent permitted by law.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>Your\r\n    use of any information or materials on this website is entirely at your own\r\n    risk, for which we shall not be liable. It shall be your own responsibility to\r\n    ensure that any products, services or information available through this\r\n    website meet your specific requirements.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>This\r\n    website contains material which is owned by or licensed to us. This material\r\n    includes, but is not limited to, the design, layout, look, appearance and\r\n    graphics. Reproduction is prohibited other than in accordance with the\r\n    copyright notice, which forms part of these terms and conditions.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>All\r\n    trademarks reproduced in this website, which are not the property of, or\r\n    licensed to the operator, are acknowledged on the website.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>Unauthorised\r\n    use of this website may give rise to a claim for damages and/or be a criminal\r\n    offence.<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>From\r\n    time to time, this website may also include links to other websites. These\r\n    links are provided for your convenience to provide further information. They do\r\n    not signify that we endorse the website(s). We have no responsibility for the\r\n    content of the linked website(s).<o:p></o:p></span></p>\r\n\r\n    <p style=\'margin-left:.5in;text-indent:-.25in;mso-list:l0 level1 lfo1;\r\n    tab-stops:list .5in\'><![if !supportLists]><span lang=EN style=\'font-family:\r\n    Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;mso-ansi-language:\r\n    EN\'><span style=\'mso-list:Ignore\'>·<span style=\'font:7.0pt "Times New Roman"\'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n    </span></span></span><![endif]><span lang=EN style=\'mso-ansi-language:EN\'>Your\r\n    use of this website and any dispute arising out of such use of the website is\r\n    subject to the laws of England, Northern Ireland, Scotland and Wales.<o:p></o:p></span></p>\r\n\r\n    <p class=MsoNormal><span lang=EN-GB><o:p>&nbsp;</o:p></span></p>\r\n\r\n    </div>\r\n\r\n  </div><!-- content -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "terms.html", "line_map": {"35": 1, "52": 3, "40": 115, "58": 52, "28": 0, "46": 3}, "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/terms.html"}
__M_END_METADATA
"""
