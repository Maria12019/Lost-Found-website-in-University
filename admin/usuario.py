#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, render_template, session, request, redirect

#objeto que tiene la subaplicacion
view = Blueprint('usuario_bludprint', __name__)

@view.route('/inicio', methods=['GET'])
def registro():    
    locals = {
        'message': '',
        
    }
    return render_template(
        'layouts/aplication.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200


@view.route('/register', methods=['GET'])
def register():    
    locals = {
        'message': '',
        
    }
    return render_template(
        'registro/registro_objeto.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200


@view.route('/sol_usu', methods=['GET'])
def sol_usu():
    locals = {
        'message': '',
    }
    return render_template(
        'registro/solicitud_usuario.html',
        locals=locals
    ), 200

@view.route('/sol_usu/verificar', methods=['GET'])
def verificar_sol_usu():
    locals = {
        'message': '',
    }
    return render_template(
        'verificacion/detalle_sol_usu.html',
        locals=locals
    ), 200