#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, session, request, redirect
from datetime import datetime
from main.filters import if_session_active_go_home, if_session_not_active_go_login

from main.test import get_password_by_id,get_rol_by_id

view = Blueprint('access_bludprint', __name__)

@view.route('/', methods=['GET'])
@if_session_active_go_home()
def login():
    locals={
        'message': '',
    }
    return render_template(
        'acceso/login_sgop.html',
        locals=locals
        ), 200



@view.route('/', methods=['POST'])
def login_access():
    user = request.form['user']
    password = request.form['password']
    #if user == 'root' and password == '123':
    rol = get_rol_by_id(user)

    '''if rol == 1:
        if user[0] == '1' or user[0]=='2':
            rolUsuario = "alumno" 
        else:
            rolUsuario = "docente"
    elif rol == 2:
        rolUsuario = "jefe" 
    elif rol == 3:
        rolUsuario = "secretaria"
    elif rol == 4:
        rolUsuario = "area de seguridad"
    else: 
        rolUsuario = "departamento"'''


    if password == get_password_by_id(user):
       
        # crear session
        session['status'] = 'active'
        session['user'] = user
        session['time'] = datetime.now()
        session['rol'] = rol
        locals = {}
        print(session['rol'])
        '''return render_template(
            'layouts/aplication.html',
            locals=locals
            ), 500'''
        return redirect('/inicio')
    else:
        locals={
            'message': 'El usuario y/o no existen'
        }
        print(session)
        return render_template(
            'acceso/login_sgop.html',
            locals=locals
            ), 500

    """if password == get_password_by_id(user):
        if rol == 1:
            if user[0] == '1' or user[0]=='2':
               return redirect('/inicio')
            else:
                return redirect('/inicio')
        elif rol == 2:
            rolUsuario = "jefe" 
        elif rol == 3:
            return redirect('/verificar')
        elif rol == 4:
            return redirect('/verificar')
        else: 
            return redirect('/registro')
    else:
        locals={
            'message': 'El usuario y/o no existen',
        }
        print(session)
        return render_template(
            'acceso/login_sgop.html',
            locals=locals
            ), 500"""

@view.route('/logout', methods=['GET'])
def logout():
    session.clear()
    locals={
        'message': 'Su sesión ha sido destruida',
    }
    return redirect('/')
'''
@view.route('/', methods=['GET'])
def home():
    locals={ }
    return render_template(
        'acceso/login_sgop.html',
        locals=locals
        ), 200
    user = request.form['user']
    password = request.form['password']
    #if user == 'root' and password == '123':
    rol = get_rol_by_id(user)
    if password == get_password_by_id(user):
        
        # crear session
        session['status'] = 'active'
        session['user'] = user
        session['time'] = datetime.now()
        session['rol'] = rol
        locals = {}
        print(session)
        return render_template(
            'layouts/aplication.html',
            locals=locals
            ), 500
    else:
        locals={
            'message': 'El usuario y/o no existen',
        }
        print(session)
        return render_template(
            'login_sgop.html',
            locals=locals
            ), 500



'''

#@view.route('/', methods=['GET'])
'''def home():
    locals={ }
    return render_template(
        'home.html',
        locals=locals
        ), 200'''


@view.route('/cerrar',methods=['POST'])
def cerrar():
    return redirect('/login')