# -*- coding: utf-8 -*-

## Felder für Antwortoptionen ##

def formatsnippet(context, snippet):
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    if context.label:
        snippet = snippet.replace("edi_context_label", context.label)
    if context.einheit:    
        snippet = snippet.replace("edi_context_einheit", context.einheit)
    return snippet


def option(context):
    snippet = """\
<div class="form-check mb-3">
  <input class="form-check-input" type="edi_context_optiontyp" name="edi_context_parentid" id="edi_context_id" value="edi_context_id">
  <label class="form-check-label" for="edi_context_id">
    edi_context_title
  </label>
</div>"""
    return formatsnippet(context, snippet)

def option_group(context):
    snippet = """\
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id" aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_label">
</div>"""
    return formatsnippet(context, snippet)

def option_group_einheit(context):
    snippet = """\
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id" aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_label">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    return formatsnippet(context, snippet)

def option_group_legend(context):
    snippet = """\
<legend>edi_context_title</legend>
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_title">
</div>"""
    return formatsnippet(context, snippet)


def option_group_legend_einheit(context):
    snippet = """\
<legend>edi_context_title</legend>
<div id="edi_context_id" class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_title">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    return formatsnippet(context, snippet)


def option_group_textarea(context):
    snippet = """\
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <textarea name="edi_context_id" class="form-control" aria-label="edi_context_label"></textarea>
</div>"""
    return formatsnippet(context, snippet)


def option_group_legend_textarea(context):
    snippet = """\
<legend>edi_context_title</legend>
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <textarea name="edi_context_id" class="form-control" aria-label="edi_context_label"></textarea>
</div>"""
    return formatsnippet(context, snippet)


## Felder für Kopffragen ##

def textline(id, fieldclass, title, typ):
    snippet = """\
<div class="form-group mb-3">
  <label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
  <input type="edi_context_antworttyp" name="edi_context_id" class="form-control" id="edi_context_id" aria-describedby="edi_context_title">
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    return snippet


def textline_unit(id, fieldclass, title, typ, einheit):
    snippet = """\
<label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
<div id="edi_context_id" class="input-group mb-3">
  <input type="edi_context_typ" name="edi_context_id" class="form-control" aria-label="edi_context_title" aria-describedby="edi_context_einheit">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    snippet = snippet.replace("edi_context_einheit", einheit)
    return snippet


def textarea(id, fieldclass, title):
    snippet = """\
<div class="form-group" mb-3>
  <label class="edi_fieldclass" for="edi_context_id">edi_context_title</label>
  <textarea class="form-control" name="edi_context_id" id="edi_context_id" rows="3"></textarea>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_fieldclass", fieldclass)
    snippet = snippet.replace("edi_context_title", title)
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
