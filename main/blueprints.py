#!/usr/bin/env python
# -*- coding: utf-8 -*-

from access.views import view as access_view
from access.views2 import view as access_view2
from admin.views import view as admin_view
from admin.registro import view as registro_view
from admin.objeto import view as objeto_view
from admin.usuario import view as usuario_view

def register(APP):
    # register blueprints
    APP.register_blueprint(access_view)
    APP.register_blueprint(access_view2)
    APP.register_blueprint(admin_view)
    APP.register_blueprint(registro_view)
    APP.register_blueprint(objeto_view)
    APP.register_blueprint(usuario_view)
