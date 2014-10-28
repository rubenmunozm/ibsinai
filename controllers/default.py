# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import jwt
import time
import math
import random
from gluon.debug import dbg
#dbg.set_trace() # stop here!

def index():
  if request.args(0):
      now = int(time.time())
      cakeToken = jwt.encode(
      {
      "iss":"07698772005655753885",
      "aud":"Google",
      "typ":"google/payments/inapp/item/v1",
      "iat":now,
      "exp":now + 3600,
      "request":{
        "currencyCode":"USD",
        "price":request.args(0),
        "name":"Donativo",
        "sellerData":"Antioquia Calvary Chapel",
        "description":"Donación a Iglesia Antioquia Calvary Chapel"
        }
      },"Th-H-LlhHhn9jB9_c_aV3A")
  else:
    pass
  
  form = SQLFORM(db.mensajes)
  if form.process(session=None, formname='contact_form').accepted:
      response.flash = 'form accepted'
  elif form.errors:
      response.flash = 'form has errors'
  return locals()


def tiendita():
  return locals()

def web():
  form = SQLFORM(db.mensajes)
  response.flash = "hola mundo"
  if form.process(session=None, formname='contact_form').accepted:
      response.flash = 'form accepted'
  elif form.errors:
      response.flash = 'form has errors'
  return locals()


def imagenes():
  return locals()

def load():
  random1 = random.randint(1,15)
  random2 = random.randint(1,15)
  while random1 == random2:
    random2 = random.randint(1,15)
  random3 = random.randint(1,15)
  while random3 == random1 or random3 == random2:
    random3 = random.randint(1,15)
  
  verso_biblico1 = db(db.versos_biblicos.numero == random1).select(db.versos_biblicos.ALL).first()
  verso_biblico2 = db(db.versos_biblicos.numero == random2).select(db.versos_biblicos.ALL).first()
  verso_biblico3 = db(db.versos_biblicos.numero == random3).select(db.versos_biblicos.ALL).first()
  return locals()

def QuienesSomos():
  return locals()

def DondeEstamos():
  return locals()

def Creemos():
  return locals()

def CasaAbierta():
  return locals()

def EstudiosBiblicos():
  return locals()

@auth.requires_membership('admin')
def admin():
    visits = db().select(db.visitas.visits).first()
    form_versos = SQLFORM.grid(db.versos_biblicos)
    response.files.append(URL(r=request,c='static/jquery.jqGrid/js/i18n',f='grid.locale-es.js'))
    response.files.append(URL(r=request,c='static/jquery.jqGrid/js/minified',f='jquery.jqGrid.min.js'))
    response.files.append(URL(r=request,c='static/jquery.jqGrid/css',f='ui.jqgrid.css'))
    #include a jquery theme downloaded from http://jqueryui.com/download/all/
    response.files.append(URL(r=request,c='static/css/themes/smoothness',f='jquery-ui.css'))
    response.files.append(URL(r=request,c='static/css/themes/smoothness',f='jquery.ui.theme.css'))
    return locals()

@service.json
def get_rows():
    """ this gets passed a few URL arguments: page number, and rows per page, and sort column, and sort desc or asc
    """
    fields = ['created_on','nombre','correo','telefono','mensaje','eliminar']
    rows = []
    page = int(request.vars.page)  #the page number
    pagesize = int(request.vars.rows)
 
    limitby = (page*pagesize - pagesize,page*pagesize)
    orderby = db.mensajes[request.vars.sidx]
    if request.vars.sord == 'desc':
        orderby = ~orderby
    
    for r in db().select(db.mensajes.ALL,limitby=limitby,orderby=orderby):
        vals = []
        for f in fields:
            if f == 'eliminar':
                vals.append(A(SPAN(_class="fa fa-arrow-right "),T('Eliminar'),_href=URL('default','eliminar', args=r.id,user_signature=True),_class='btn', _style='margin-top: 0em; color:#CE0E0E;'))
            else:
                rep = db.mensajes[f].represent
                if rep:
                    vals.append(rep(r[f]))
                else:
                    vals.append(r[f])
        rows.append(dict(id=r.id,cell=vals))
    total = db(db.mensajes.id>0).count()
    pages = math.ceil(1.0*total/pagesize)
    data = dict(total=pages,page=page,rows=rows)
    #session.query_excell_lic = str(query)
    
    return data

@auth.requires_signature()
def eliminar():
    del db.mensajes[request.args(0)]
    redirect(URL('default','admin'))

@service.json
def get_rows_versos():
    """ this gets passed a few URL arguments: page number, and rows per page, and sort column, and sort desc or asc
    """
    fields = ['numero','verso','cita','eliminar']
    rows = []
    page = int(request.vars.page)  #the page number
    pagesize = int(request.vars.rows)
 
    limitby = (page*pagesize - pagesize,page*pagesize)
    orderby = db.versos_biblicos[request.vars.sidx]
    if request.vars.sord == 'desc':
        orderby = ~orderby
    
    for r in db().select(db.versos_biblicos.ALL,limitby=limitby,orderby=orderby):
        vals = []
        for f in fields:
            if f == 'eliminar':
                vals.append(A(SPAN(_class="fa fa-arrow-right "),T('Eliminar'),_href=URL('default','eliminar', args=r.id,user_signature=True),_class='btn', _style='margin-top: 0em; color:#CE0E0E;'))
            else:
                rep = db.versos_biblicos[f].represent
                if rep:
                    vals.append(rep(r[f]))
                else:
                    vals.append(r[f])
        rows.append(dict(id=r.id,cell=vals))
    total = db(db.versos_biblicos.id>0).count()
    pages = math.ceil(1.0*total/pagesize)
    data = dict(total=pages,page=page,rows=rows)
    #session.query_excell_lic = str(query)
    
    return data

def PazConDios():
  return locals()
  
@service.json
def save_cell_versos():
    """ No doubt there are more elegant ways to detect which field has been updated...
    """
    try:
        id = request.vars.id
        if id:
            row = db(db.versos_biblicos.id==id).select().first()
            for field in db.versos_biblicos.fields:
                if field != 'id' and request.vars[field]:
                    row.update_record(**{field:request.vars[field]})
                else:
                    pass
        # dbg.set_trace()
    except Exception, e:
        pass



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    auth.settings.formstyle = bs3.form('inline')
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())



