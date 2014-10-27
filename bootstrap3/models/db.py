# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

# bootstrap3 theme for web2py
from gluon import current
current.auth = auth
import bootstrap3 as bs3

from plugin_jqueryui import iToggleWidget
widget_itoggle = iToggleWidget()

db.define_table('historial',
    Field('fecha', 'datetime'),
    Field('usuario','string'),
    Field('out_num','string'),
    Field('accion','string'))


db.define_table('botones',
        Field('out_1_value', 'boolean', widget= widget_itoggle.widget),
        Field('out_1_label', 'string', length=20),
        Field('out_1_cmd', 'string', length=30),
        Field('out_1_hide', 'boolean', default=False),
        Field('out_2_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_2_label', 'string', length=20),
        Field('out_2_cmd', 'string', length=30),
        Field('out_2_hide', 'boolean', default=False),
        Field('out_3_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_3_label', 'string', length=20),
        Field('out_3_cmd', 'string', length=30),
        Field('out_3_hide', 'boolean', default=False),
        Field('out_4_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_4_label', 'string', length=20),
        Field('out_4_cmd', 'string', length=30),
        Field('out_4_hide', 'boolean', default=False),
        Field('out_5_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_5_label', 'string', length=20),
        Field('out_5_cmd', 'string', length=30),
        Field('out_5_hide', 'boolean', default=False),
        Field('out_6_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_6_label', 'string', length=20),
        Field('out_6_cmd', 'string', length=30),
        Field('out_6_hide', 'boolean', default=False),
        Field('out_7_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_7_label', 'string', length=20),
        Field('out_7_cmd', 'string', length=30),
        Field('out_7_hide', 'boolean', default=False),
        Field('out_8_value', 'boolean',widget= widget_itoggle.widget),
        Field('out_8_label', 'string', length=20),
        Field('out_8_cmd', 'string', length=30),
        Field('out_8_hide', 'boolean', default=False),auth.signature)

