# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from gluon.debug import dbg
import time
import datetime

import socket
import sys
import time
import datetime
def pruebas():
  grid_historial = SQLFORM.grid(db.historial, paginate=5, csv=False)
  return locals() 
 
def send_messages_tcp(server_address, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Send data
        #print >>sys.stderr, 'sending "%s"' % message
        sent = sock.sendto(message, server_address)
 
    finally:
        pass
    pass

def web2py_sockets():
    servidor = '10.21.4.30'
    puerto = 10000
    mensaje = "Hola"
    server_address=(servidor , puerto )
    message = mensaje
    send_messages_tcp( server_address=server_address, message=message)        ##Enviar el mensaje por TCP/IP
    return locals()

#dbg.set_trace() # stop here!
@auth.requires_login()
def historial():
  grid_historial = SQLFORM.grid(db.historial)
  return locals()

@auth.requires(auth.requires_signature() and auth.has_membership(group_id='admin'))
def adm():
  botones = db(db.botones).select().last()
  form = SQLFORM(db.botones, botones)
  if form.accepts(request.vars, session):
       response.flash = 'Actualizado'
  elif form.errors:
       response.flash = 'Sucedió un error'
  else:
        pass
  return locals()

@auth.requires_login()
def index():
    #b1 = db(db.botones.etiqueta=='boton1').select
    db.botones.out_1_label.writable = False
    db.botones.out_1_cmd.readable = False
    db.botones.out_1_cmd.writable = False
    db.botones.out_1_hide.readable = False
    db.botones.out_1_hide.writable = False
    db.botones.out_2_label.writable = False
    db.botones.out_2_cmd.readable = False
    db.botones.out_2_cmd.writable = False
    db.botones.out_2_hide.readable = False
    db.botones.out_2_hide.writable = False
    db.botones.out_3_label.writable = False
    db.botones.out_3_cmd.readable = False
    db.botones.out_3_cmd.writable = False
    db.botones.out_3_hide.readable = False
    db.botones.out_3_hide.writable = False
    db.botones.out_4_label.writable = False
    db.botones.out_4_cmd.readable = False
    db.botones.out_4_cmd.writable = False
    db.botones.out_4_hide.readable = False
    db.botones.out_4_hide.writable = False
    db.botones.out_5_label.writable = False
    db.botones.out_5_cmd.readable = False
    db.botones.out_5_cmd.writable = False
    db.botones.out_5_hide.readable = False
    db.botones.out_5_hide.writable = False
    db.botones.out_6_label.writable = False
    db.botones.out_6_cmd.readable = False
    db.botones.out_6_cmd.writable = False
    db.botones.out_6_hide.readable = False
    db.botones.out_6_hide.writable = False
    db.botones.out_7_label.writable = False
    db.botones.out_7_cmd.readable = False
    db.botones.out_7_cmd.writable = False
    db.botones.out_7_hide.readable = False
    db.botones.out_7_hide.writable = False
    db.botones.out_8_label.writable = False
    db.botones.out_8_cmd.readable = False
    db.botones.out_8_cmd.writable = False
    db.botones.out_8_hide.readable = False
    db.botones.out_8_hide.writable = False
    

    botones = db(db.botones).select().last()
    form = SQLFORM(db.botones, botones)
    row = db(db.botones).select().last()
    if form.accepts(request.vars, session):
       response.flash = 'Actualizado'
        #Seleccionar el registro
       dicc={}
       dicct={}
       for field in db.botones.fields:                       #Recorremos cada campo
            if row[field] != form.vars[field]:    #Comparamos el valor que recibimos con el almacenado
                
  
                if 'value' in field:
                  label=field.replace('_value','_label')
                  dicct  = {row[label]:form.vars[field]}
                  cmd=field.replace('_value','_cmd')
                  if form.vars[field] == True:
                    prender=row[cmd]+'1:35'
                    send_messages_tcp( server_address=('10.21.4.30', 10000), message=prender)
                  elif form.vars[field] == False:
                    apagar=row[cmd]+'0:35'
                    send_messages_tcp( server_address=('10.21.4.30', 10000), message=apagar)

                dicc.update(dicct)
            else:

                pass
       
         
       for key in dicc.keys():
          db.historial.insert(fecha=datetime.datetime.now(),usuario=auth.user.first_name+" "+auth.user.last_name,out_num=key,accion=dicc[key])

    elif form.errors:
       response.flash = 'Ocurrió un error'
    else:
        pass
    
    grid_historial = SQLFORM.grid(db.historial,paginate=8,orderby=~db.historial.fecha,
                                  deletable=False,create=False,editable=False, searchable=False, csv=False, 
                                  details=False, headers={'historial.out_num' : 'Salida'})   

    return locals()

def allon():
  row = db(db.botones).select().last()
  
  dicc={}
  dicct={}
  for field in db.botones.fields:                       
    if 'value' in field:
      if row[field] == False:
        hide=field.replace('_value','_hide')
        if row[hide] == False:
          label=field.replace('_value','_label')
          dicct = {row[label]:True}
          row.update_record(**{field:True})
          cmd=field.replace('_value','_cmd')
          prender=row[cmd]+'1:35'
          send_messages_tcp( server_address=('10.21.4.30', 10000), message=prender)
           
    dicc.update(dicct)
   
          
  for key in dicc.keys():
    db.historial.insert(fecha=datetime.datetime.now(),usuario=auth.user.first_name+" "+auth.user.last_name,out_num=key,accion=dicc[key])
  redirect(URL('default','index'))
  return locals();

def alloff():
  row = db(db.botones).select().last()
  
  dicc={}
  dicct={}
  for field in db.botones.fields:                       
    if 'value' in field:
      if row[field] == True:
        hide=field.replace('_value','_hide')
        if row[hide] == False:
          label=field.replace('_value','_label')
          dicct = {row[label]:False}
          row.update_record(**{field:False})
          cmd=field.replace('_value','_cmd')
          apagar=row[cmd]+'0:35'
          send_messages_tcp( server_address=('10.21.4.30', 10000), message=apagar) 
    dicc.update(dicct)
   
          
  for key in dicc.keys():
    db.historial.insert(fecha=datetime.datetime.now(),usuario=auth.user.first_name+" "+auth.user.last_name,out_num=key,accion=dicc[key])
  redirect(URL('default','index'))
  return locals();

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


def insert_person():
    form = SQLFORM(db.person,
                   formstyle=bs3.form('horizontal', 'inline'),
                   buttons=[INPUT(_value=T('Submit'), _type="submit"),
                            TAG.button('Cancel', _type="reset")])
    # add an extra row
    extra_row = bs3.build_row('extra_row',
                              T('Choice on submit:'),
                              DIV(DIV(LABEL(T('No insert')),
                                      INPUT(_id="choice-one", _name="choices",
                                            _type="radio", _value="1",
                                            value="1")),
                                  DIV(LABEL(T('Overwrite previous')),
                                      INPUT(_id="choice-two", _name="choices",
                                            _type="radio", _value="2")),
                                  DIV(LABEL(T('Rename and insert')),
                                      INPUT(_id="choice-three",
                                            _name="choices", _type="radio",
                                            _value="3")),
                                  _class="web2py_radiowidget"),
                              'Action to execute if person is present in db.',
                              form, 'horizontal', 'stacked')
    form[0].insert(-1, extra_row)

    if form.process().accepted:
       response.flash = T('form accepted')
    elif form.errors:
       response.flash = T('form has errors')
    else:
       response.flash = T('please fill out the form')

    response.view = 'default/display_form.html'

    return dict(form=form)


def insert_dog():
    form = SQLFORM(db.dog, formstyle=bs3.form(''))

    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
       response.flash = 'form has errors'
    else:
       response.flash = 'please fill out the form'

    response.view = 'default/display_form.html'

    return dict(form=form)


def update_person():
    record = db.person(request.args(0)) or redirect(URL('index'))
    url = URL('download')
    link = URL('list_records', args='db')
    form = SQLFORM(db.person, record, 
                   formstyle=bs3.form(),
                   readonly=False,
                   upload=url, linkto=link, 
                   labels={'dog.the_owner':"This person's dogs"})

    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
       response.flash = 'form has errors'
    response.view = 'default/display_form.html'

    return dict(form=form)


def update_dog():
    record = db.dog(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.dog, record, formstyle=bs3.form('horizontal'))

    if form.process().accepted:
       response.flash = 'form accepted'
    elif form.errors:
       response.flash = 'form has errors'

    response.view = 'default/display_form.html'

    return dict(form=form)


def list_records():
    import re
    REGEX = re.compile('^(\w+).(\w+).(\w+)\=\=(\d+)$')
    match = REGEX.match(request.vars.query)
    if not match:
        redirect(URL('error'))
    table, field, id = match.group(2), match.group(3), match.group(4)
    records = db(db[table][field]==id).select()
    return dict(records=records)


def about():
    test_tabs = [
        ('', False, A(T('home'), _href='#home')),
        ('', False, A(T('profile'), _href='#profile')),
        ('', True, A('Dropdown', _href='#'), [
            ('', False, A('@fat', _href='#dropdown1')),
            ('', False, A('@mdo', _href='#dropdown2'))
            ])
        ]
    return locals()


def help():
    return dict()
