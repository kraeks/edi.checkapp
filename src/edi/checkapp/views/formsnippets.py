# -*- coding: utf-8 -*-

def option(context):
    snippet = """\
<div class="form-check mb-3">
  <input class="form-check-input" type="edi_context_optiontyp" name="edi_context_parentid" id="edi_context_id" value="edi_context_id">
  <label class="form-check-label" for="edi_context_id">
    edi_context_title
  </label>
</div>"""
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    return snippet
           

def option_group(context):
    snippet = """\
<div class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id" aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_einheit">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_label", context.label)
    snippet = snippet.replace("edi_context_einheit", context.einheit)
    return snippet


def option_group_label(context):
    snippet = """\
<label for="edi_context_id">edi_context_title</label>
<div id="edi_context_id" class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <input type="text" class="form-control" aria-label="edi_context_title">
</div>"""
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_title", context.title)
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_label", context.label)
    return snippet


def option_group_label_einheit(context):
    snippet = """\
<label for="edi_context_id">edi_context_title</label>
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
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_label", context.label)
    snippet = snippet.replace("edi_context_einheit", context.einheit)
    return snippet


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
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_label", context.label)
    return snippet


def option_group_label_textarea(context):
    snippet = """\
<label for="edi_context_id">edi_context_title</label>
<div id="edi_context_id" class="input-group mb-3">
  <div class="input-group-prepend">
    <div class="input-group-text">
      <input name="edi_context_parentid" type="edi_context_optiontyp" value="edi_context_id"  aria-label="edi_context_title">
    </div>
    <span class="input-group-text">edi_context_label</span>
  </div>
  <textarea name="edi_context_id" class="form-control" aria-label="edi_context_label"></textarea>
</div>"""
    snippet = snippet.replace("edi_context_id", context.getId())
    snippet = snippet.replace("edi_context_optiontyp", context.aq_parent.antworttyp)
    snippet = snippet.replace("edi_context_title", context.title)
    snippet = snippet.replace("edi_context_parentid", context.aq_parent.getId())
    snippet = snippet.replace("edi_context_label", context.label)
    return snippet

def textline(id, title, typ):
    snippet = """\
<div class="form-group mb-3">
  <label for="edi_context_id">edi_context_title</label>
  <input type="edi_context_antworttyp" name="edi_context_id" class="form-control" id="edi_context_id" aria-describedby="edi_context_title">
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    return snippet

def textline_unit(id, title, typ, einheit):
    snippet = """\
<label for="edi_context_id">edi_context_title</label>
<div id="edi_context_id" class="input-group mb-3">
  <input type="edi_context_typ" name="edi_context_id" class="form-control" aria-label="edi_context_title" aria-describedby="edi_context_einheit">
  <div class="input-group-append">
    <span class="input-group-text">edi_context_einheit</span>
  </div>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_context_title", title)
    snippet = snippet.replace("edi_context_antworttyp", typ)
    snippet = snippet.replace("edi_context_einheit", einheit)
    return snippet

def textarea(id, title):
    snippet = """\
<div class="form-group" mb-3>
  <label for="edi_context_id">edi_context_title</label>
  <textarea class="form-control" name="edi_context_id" id="edi_context_id" rows="3"></textarea>
</div>"""
    snippet = snippet.replace("edi_context_id", id)
    snippet = snippet.replace("edi_context_title", title)
    return snippet
