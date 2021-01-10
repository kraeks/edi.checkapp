# -*- coding: utf-8 -*-

## Felder für Antwortoptionen ##

def formatsnippet(context, snippet):
    snippet = snippet.replace("edi_context_id", 'edi'+context.UID())
    snippet = snippet.replace("edi_context_parentid", 'edi'+context.aq_parent.UID())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    if context.platzhalter:
        snippet = snippet.replace("edi_context_platzhalter", context.platzhalter)
    else:
        snippet = snippet.replace("edi_context_platzhalter", u"")
    if context.label:
        snippet = snippet.replace("edi_context_label", context.label)
    if context.einheit:    
        snippet = snippet.replace("edi_context_einheit", context.einheit)
    if context.xseinheit:
        snippet = snippet.replace("edi_context_xseinheit", context.xseinheit)
    if context.dep_fields:
        targetid = 'edi'+context.dep_fields.to_object.UID()
        target = 'data-toggle="collapse" data-target="#%s"' % targetid
        snippet = snippet.replace("edi_data_toggle", target)
    else:
        snippet = snippet.replace("edi_data_toggle", u"")
    return snippet


def option(context):
    snippet = """\
<div class="form-check mb-3">
  <input class="form-check-input" type="edi_context_optiontyp" name="edi_context_parentid" id="edi_context_id" value="edi_context_id"
    placeholder="edi_context_platzhalter" edi_data_toggle>
  <label class="form-check-label" for="edi_context_id">
    edi_context_title
  </label>
</div>"""
    return formatsnippet(context, snippet)

def option_group(context):
    snippet = """\
<div class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id" aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input placeholder="edi_context_platzhalter" type="text" class="form-control" aria-label="edi_context_label">
</div>"""
    return formatsnippet(context, snippet)

def option_group_einheit(context):
    snippet = """\
<div class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id" aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input placeholder="edi_context_platzhalter" type="text" class="form-control" aria-label="edi_context_label">
  <div class="input-group-append d-none d-sm-block">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
  <div class="input-group-append d-block d-sm-none">
    <span class="input-group-text">edi_context_xseinheit</span>
  </div>
</div>"""
    return formatsnippet(context, snippet)

def option_group_legend(context):
    snippet = """\
<legend>edi_context_title</legend>
<div class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" placeholder="edi_context_platzhalter" class="form-control" aria-label="edi_context_title">
</div>"""
    return formatsnippet(context, snippet)


def option_group_legend_einheit(context):
    snippet = """\
<legend>edi_context_title</legend>
<div id="edi_context_id" class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" placeholder="edi_context_platzhalter" class="form-control" aria-label="edi_context_title">
  <div class="input-group-append d-none d-sm-block">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
  <div class="input-group-append d-block d-sm-none">
    <span class="input-group-text">edi_context_xseinheit</span>
  </div>
</div>"""
    return formatsnippet(context, snippet)


def option_group_textarea(context):
    snippet = """\
<div class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <textarea placeholder="edi_context_platzhalter" name="edi_context_id" class="form-control" aria-label="edi_context_label"></textarea>
</div>"""
    return formatsnippet(context, snippet)


def option_group_legend_textarea(context):
    snippet = """\
<legend>edi_context_title</legend>
<div class="input-group mb-3" edi_data_toggle>
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title" 
      placeholder="edi_context_platzhalter" edi_data_toggle>
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <textarea placeholder="edi_context_platzhalter" name="edi_context_id" class="form-control" aria-label="edi_context_label"></textarea>
</div>"""
    return formatsnippet(context, snippet)


## Felder für Kopffragen ##

def textline(id, fieldclass, title, typ, platzhalter=u""):
    snippet = """\
<div class="form-group mb-3">
  <label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
  <input type="edi_context_antworttyp" name="edi_context_id" class="form-control" id="edi_context_id" 
         placeholder="edi_context_platzhalter" aria-describedby="edi_context_title">
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    if platzhalter == None:
        platzhalter = u""
    snippet = snippet.replace("edi_context_platzhalter", platzhalter)
    return snippet


def textline_unit(id, fieldclass, title, typ, einheit, platzhalter=u""):
    snippet = """\
<label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
<div id="edi_context_id" class="input-group mb-3">
  <input type="edi_context_typ" name="edi_context_id" class="form-control" aria-label="edi_context_title" 
         placeholder="edi_context_platzhalter" aria-describedby="edi_context_einheit">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    snippet = snippet.replace("edi_context_einheit", einheit)
    if platzhalter == None:
        platzhalter = u""
    snippet = snippet.replace("edi_context_platzhalter", platzhalter)
    return snippet


def textarea(id, fieldclass, title, platzhalter=u""):
    snippet = """\
<div class="form-group" mb-3>
  <label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
  <textarea placeholder="edi_context_platzhalter" class="form-control" name="edi_context_id" id="edi_context_id" rows="3"></textarea>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
    if platzhalter == None:
        platzhalter = u""
    snippet = snippet.replace("edi_context_platzhalter", platzhalter)
    return snippet


def select(id, fieldclass, title, options):
    snippet = u"""\
<div class="form-group mb-3">
  <label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
  <select class="form-control" id="edi_context_id">"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_context_title", title)
    for i in options:
        snippet += u"<option>edi_opt</option>".replace('edi_opt', i) 
    snippet += u"</select></div>"
    return snippet

def radiobutton(id, fieldclass, title, options):
    snippet = """\
<legend class="mt-3">%s</legend>""" %title
    for i in options:
        snippet += """\
<div class="form-check form-check-inline">
  <input class="form-check-input" type="radio" name="%s" id="%s" value="%s">
  <label class="form-check-label" for="%s">%s</label>
</div>""" %(id, id, i, id, i)
    return snippet

def checkbox(id, fieldclass, title, options):
    snippet = """\
<legend class="mt-3">%s</legend>""" %title
    for i in options:
        snippet += """\
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="%s" value="%s">
  <label class="form-check-label" for="%s">%s</label>
</div>""" %(id, i, id, i)
    return snippet
