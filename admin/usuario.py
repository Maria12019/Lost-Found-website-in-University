#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, render_template, session, request, redirect

#objeto que tiene la subaplicacion
view = Blueprint('usuario_bludprint', __name__)

@view.route('/inicio', methods=['GET','POST'])
def registro():
    #cod_usu=request.args.get('cod_usu')
    cod_usu=request.form['cod_usu']
    print(cod_usu)   
    locals = {
        'message': '',
        'cod_usu':cod_usu
    }   
    return render_template(
        'layouts/aplication.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200
'''@view.route('/principal', methods=['GET','POST'])
def principal():
   
    locals = {
        'message': ''
    }   
    return render_template(
        'layouts/aplication.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200'''

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

@view.route('/sol_dpto', methods=['GET'])
def sol_dpto():
    locals = {
        'message':'',
    }
    return render_template(
        'registro/solicitud_dpto.html',
        locals=locals
    ), 200


@view.route('/dpto_verificar', methods=['GET'])
def dpto_verificar():
    locals = {
        'message':'',
    }
    return render_template(
        'registro/solicitud_dpto_verificar.html',
        locals=locals
    ), 200

@view.route('/donacion', methods=['GET'])
def registro_donacion():    
    locals = {
        'message': '',
        
    }
    return render_template(
        'registro/registro_solicitud.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200


@view.route('/enviado', methods=['GET'])
def enviado():    
    locals = {
        'message': '',
        
    }
    return render_template(
        'registro/enviado.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200