#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, render_template, session, request, redirect

#objeto que tiene la subaplicacion
view = Blueprint('objeto_bludprint', __name__)

@view.route('/verificar', methods=['GET'])
def registro():    
    locals = {
        'message': '',
        'categorias': [
            { 'id': "50", 'nombre': 'DIRECCION DE BIENESTAR'},
           
            #{ 'id': "50", 'nombre': 'Pepe'},
        ]
        
    }
    return render_template(
        
        '/objeto/verificar_objeto.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200

@view.route('/verificar/detalle', methods=['GET'])
def registro_agregar():    
    locals = {
        'message': '',
        'categorias': [
            { 'id': "50", 'nombre': 'DIRECCION DE BIENESTAR'},
            
            #{ 'id': "50", 'nombre': 'Pepe'},
        ]
        
    }
    return render_template(
        '/objeto/detalle_objeto.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200
