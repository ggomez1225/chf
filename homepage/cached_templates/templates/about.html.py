# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453517971.2570858
_enable_loop = True
_template_filename = 'D:/Jason/Documents/CHF/CHF/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content', 'content_right']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('<!-- content -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

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
        __M_writer('\r\n  About\r\n')
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
        __M_writer('\r\n  <div class="content">\r\n    <div class="article-content entry-content" itemprop="articleBody"><div class="noborderdv" style="clear: both; text-align: center;">\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><img border="0" height="90" width="400" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/CHFlogoH2.png">&nbsp;</span>\r\n\r\n    </div>\r\n    <h2>\r\n    <span style="font-family: Georgia, Times New Roman, serif;">Colonial Heritage Festival</span></h2>\r\n    <div>\r\n    Join us at the Scera Park in Orem, Utah for the west\'s largest American colonial living and reenactment event. &nbsp;With more than 50 historic exhibits including canon, blacksmith, baker, printing press, cooper, the world\'s largest scale model of the Mayflower, potter and much, much more.&nbsp;</div>\r\n    <div>\r\n    <br></div>\r\n    <div class="separator" style="clear: both; text-align: center;">\r\n    <a href="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/canon.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="213" width="320" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/canon.JPG"></a></div>\r\n    <div>\r\n    <br></div>\r\n    <div>\r\n    <br></div>\r\n    <div>\r\n    Details are at <a href="http://festival.colonialheritage.org/">festival.colonialheritage.org</a>.</div>\r\n    <h2>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span></h2>\r\n    <h2>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Colonial Heritage Foundation</span></h2>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</span><br>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span>\r\n    <br>\r\n    <h3>\r\n\r\n    <a href="http://colonialheritagefdn.blogspot.com/p/blog-page_18.html"><span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">Education Exhibits</span></a></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">At its heart, the Foundation is an educational institution.&nbsp; One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America\'s colonial period and is founding generation.&nbsp; To this end, the Foundation has developed a variety of traveling exhibits.&nbsp; One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.&nbsp; The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence.</span><br>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">Another exhibit focuses on the early colonial period and the ides of self-government that were planted in Jamestowne and Plimoth.&nbsp; At the center of this exhibit is a scale model of the Mayflower. The exhibit also includes replicas of various artifacts from the early colonial period.</span><br>\r\n    <h3>\r\n    </h3>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">\r\n    Reading and Discussion Groups</span></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America\'s historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America\'s current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation. </span><br>\r\n    <h3>\r\n    </h3>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">\r\n    Workshops, Lectures, and Seminars</span></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America\'s founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today\'s population with the freedoms we enjoy. These events&nbsp; seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America\'s founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee. </span><br>\r\n    <h3>\r\n    </h3>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">\r\n    Historical Reenactment</span></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Foundation sponsors the Colonial Heritage Festival, the largest colonial living and reenactment event west of the Mississippi River. This event is located in Orem, Utah as is attended by more than 40,000 people annually.</span><br>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Foundation also coordinates presentations of individual reenactors portraying notable figures from the American founding such as&nbsp; George Washington, Benjamin Franklin, and others.</span><br>\r\n    <br>\r\n    <h3>\r\n    </h3>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">Apprenticeships</span></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The Foundation seeks to help individuals who have developed skills peculiar to America\'s founding era to pass those skills on to others. One way to preserve these skills is to teach them to younger individuals. The Foundation seeks to match skilled artisans and craftsmen with eager young individuals for the purposing of learning trade and artistic skills.&nbsp;</span><br>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span>\r\n    <br>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">\r\n    Internships</span></h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">In conjunction with its educational exhibits, the Foundation offers unpaid internships intended for students studying Museum Studies or History Education.&nbsp; Individuals selected for the program spend one to three months accompanying educational exhibits to schools, teaching students about Colonial American History and portraying notable figures from the period.&nbsp; </span><br>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span>\r\n    <br>\r\n    <h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">Legal</span></h3>\r\n    <div>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">The name "Colonial Heritage Foundation" is another name for the Society for the Preservation of America\'s Founding Values, Inc., which is a 501(3)(c) public charity.</span></div>\r\n    <h3>\r\n    </h3>\r\n    <span style="font-family: Georgia,&quot;Times New Roman&quot;,serif;"><br></span></div>\r\n  </div><!-- content -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"98": 84, "67": 3, "40": 1, "73": 7, "92": 84, "82": 10, "45": 5, "80": 7, "81": 10, "50": 82, "83": 20, "84": 20, "85": 20, "86": 20, "55": 86, "104": 98, "28": 0, "61": 3}, "uri": "about.html", "source_encoding": "utf-8", "filename": "D:/Jason/Documents/CHF/CHF/homepage/templates/about.html"}
__M_END_METADATA
"""
