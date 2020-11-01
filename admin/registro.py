#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, render_template, session, request, redirect

#objeto que tiene la subaplicacion
view = Blueprint('registro_bludprint', __name__)


@view.route('/registro', methods=['GET'])
def registro():    
    locals = {
        'message': '',
        'categorias': [
            { 'id': "50", 'nombre': 'DIRECCION DE BIENESTAR'},
            { 'id': "50", 'nombre': 'DEPARTAMENTO DE SERVICIO SOCIAL'},
            { 'id': "50", 'nombre': 'DEPARTAMENTO DE PSICOLOGIA'},
            { 'id': "50", 'nombre': 'CENTRO DE EMPRENDIMIENTO '},
            { 'id': "50", 'nombre': 'INSTITUTO DE INVESTIGACION CIENTIFICA'}, 
            { 'id': "50", 'nombre': 'CENTRO DE PRODUCCION DIGITAL'},
            { 'id': "50", 'nombre': 'CENTRO DE CREACION AUDIOVISUAL'},
            { 'id': "50", 'nombre': 'CENTRO DE GOBIERNO CORPORATIVO'},
            { 'id': "50", 'nombre': 'RESPONSABILIDAD SOCIAL'},
            { 'id': "50", 'nombre': 'DEPARTAMENTO ACADEMICO'},
            #{ 'id': "50", 'nombre': 'Pepe'},
        ]
    }
    return render_template(
        '/registro/registro.html',
        
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200

