#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json,datetime
from flask import Blueprint, render_template, session, request, redirect
from main.models import Country,Objeto,Solicitud,Soloriginal
from main.database import engine,session_db
from sqlalchemy import select,insert, between, update
from datetime import datetime

#objeto que tiene la subaplicacion
view = Blueprint('admin_bludprint', __name__)

@view.route('/country/list')
def country_list():
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Country])
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los paises',
            str(e)
        ]
        status = 500
    return json.dumps(resp), status



@view.route('/objeto/list')
def objeto_list():
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Objeto])
        rs = conn.execute(stmt)
        lista = []
        for r in conn.execute(stmt):
            print(r.fecha_hallado)
            row = {
            'id': r.id,
            'cod_objeto':r.cod_objeto,
            'nom_objeto':r.nom_objeto,
            'categoria':r.categoria,
            'estado':r.estado,
            'marca':r.marca,
            'fecha_hallado':str(r.fecha_hallado),
            'fecha_dev':str(r.fecha_dev),
            'lugar':r.lugar,
            'nro_anaquel':r.nro_anaquel,
            'caract_esp':r.caract_esp,
            'cod_usu_entrega':r.cod_usu_entrega
            }
            if(r.estado == 'ALMACENADO'):
                lista.append(row) 
        resp=lista

     
        
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los paises',
            str(e)
        ]
        status = 500

    return json.dumps(resp),status

@view.route('/solicitud/list')
def solicitud_list():
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Solicitud])
        rs = conn.execute(stmt)
        lista = []
        for r in conn.execute(stmt):
            row = {
            'id': r.id,
            'categoria': r.categoria,
            'nom_objeto': r.nom_objeto,
            'cod_objeto': r.cod_objeto,
            'nro_solicitud': r.nro_solicitud,
            'fecha_envio': str(r.fecha_envio),
            'lugar': r.lugar,
            'descripcion': r.descripcion,
            'caract_esp': r.caract_esp,
            'estado': r.estado,
            'fecha_rpta': str(r.fecha_rpta)
            }
            if r.estado == 'EN PROCESO':
                lista.append(row)
        resp=lista
    except Exception as e:
        resp = [
            'Se ha producido un error en listar las solicitudes',
            str(e)
        ]
        status = 500

    return json.dumps(resp),status


@view.route('/objeto/agregar', methods=['POST'])
def objeto_agregar():
    codigo = request.form['cod_objeto']
    nom_objeto=str(request.form['nom_objeto'])
    categoria=str(request.form['categoria'])
    marca=str(request.form['marca'])
    estado=str(request.form['estado'])
    fecha_hallado=request.form['fecha_hallado']
    fecha_dev=request.form['fecha_dev']
    lugar=str(request.form['lugar'])
    nro_anaquel=request.form['nro_anaquel']
    caract_esp=str(request.form['caract_esp'])
    cod_usu_entrega=request.form['cod_usu_entrega']
    print(cod_usu_entrega)
    #conn = engine.connect()
    status = 200
    session = session_db()
    stmt=Objeto(
        cod_objeto=codigo,
        nom_objeto=nom_objeto,
        categoria=categoria,
        marca=marca,
        estado=estado,
        fecha_hallado=fecha_hallado,
        fecha_dev=fecha_dev,
        lugar=lugar,
        nro_anaquel=nro_anaquel,
        caract_esp=caract_esp,
        cod_usu_entrega=cod_usu_entrega)
    session.add(stmt)
    session.flush()
    print('1 ++++++++++++++++++++++++')
    session.commit()
    print('2 ++++++++++++++++++++++++')

    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los items del subtítulo'
      ]
    }
    
    #return  json.dumps(rpta),status
    return redirect('/register')

    '''
INSERT INTO OBJETO(cod_objeto, id_usuario,nom_objeto, categoria, marca, estado, fecha_hallado,fecha_dev, lugar, nro_anaquel, caract_esp, cod_usu_entrega)
 VALUES(1, 5,'CARGADOR HUAWEI', 'TECNOLOGICO','HUAWEI', 'EN PROCESO', '10-04-2020', NULL, 'F', 1,'USB AZUL MARCA HUAWEI', NULL);'''


@view.route('/objeto/filtro')

def filtro_objeto():
    
    resp = None
    categoria = request.args.get('categoria') #BELLEZA
    lugar = request.args.get('lugar')
    fechaInicio = request.args.get('fechaInicio')
    fechaFin = request.args.get('fechaFin')
    status = 200
    print(fechaInicio)
    print(fechaFin)
    try:
        conn = engine.connect()
        stmt=''
        if(categoria != 'undefined' and lugar == 'undefined' and fechaInicio == 'undefined' and fechaFin == 'undefined' ):
            print(1)
            stmt = select([Objeto]).where(Objeto.categoria == categoria)
        
        elif(categoria == 'TODOS' and lugar == 'TODOS' and fechaInicio != 'undefined' and fechaFin != 'undefined'):
            print(7)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin))

        elif (fechaInicio != 'undefined' and fechaFin != 'undefined'and lugar == 'undefined' and categoria == 'undefined' ):
            print(2)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin))
           
        elif(lugar != 'undefined' and categoria == 'undefined' and fechaInicio == 'undefined' and fechaFin == 'undefined'):
            print(3)
            stmt = select([Objeto]).where(Objeto.lugar == lugar)
        elif(categoria == 'TODOS' and lugar != 'undefined' and fechaInicio == 'undefined' and fechaFin == 'undefined'):
            print(4)
            stmt = select([Objeto]).where(Objeto.lugar == lugar)
        elif(categoria == 'TODOS' and lugar == 'undefined' and fechaInicio != 'undefined' and fechaFin != 'undefined'):
            print(5)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin))

        elif(lugar == 'TODOS' and categoria == 'undefined' and fechaInicio != 'undefined' and fechaFin != 'undefined'):
            print(6)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin))

        elif(lugar == 'TODOS' and categoria != 'undefined' and fechaInicio == 'undefined' and fechaFin == 'undefined'):
            print(8)
            stmt = select([Objeto]).where(Objeto.categoria == categoria)
        elif(lugar != 'undefined' and categoria != 'undefined' and fechaInicio == 'undefined' and fechaFin == 'undefined'):
            print(9)
            stmt =  (select([Objeto])
                    .select_from(Objeto)
                    .where((Objeto.categoria == categoria) &
                    (Objeto.lugar == lugar)))

        elif (fechaInicio != 'undefined' and fechaFin != 'undefined'and lugar != 'undefined' and categoria != 'undefined' ):
            print(10)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin) & (Objeto.categoria == categoria) &
                    (Objeto.lugar == lugar))

        elif(fechaInicio != 'undefined' and fechaFin != 'undefined' and categoria == 'undefined' and lugar != 'undefined' ):
            print(11)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin) &
                    (Objeto.lugar == lugar))

        elif(categoria != 'undefined' and lugar == 'undefined' and fechaInicio != 'undefined' and fechaFin != 'undefined' ):
            print(12)
            stmt = select([Objeto]).where(between(Objeto.fecha_hallado, fechaInicio, fechaFin) & (Objeto.categoria == categoria) )
        
        rs = conn.execute(stmt)
        lista = []
        for r in conn.execute(stmt):
            print(r.categoria)
            row = {
            'id': r.id,
            'cod_objeto':r.cod_objeto,
            'nom_objeto':r.nom_objeto,
            'categoria':r.categoria,
            'estado':r.estado,
            'marca':r.marca,
            'fecha_hallado':str(r.fecha_hallado),
            'fecha_dev':str(r.fecha_dev),
            'lugar':r.lugar,
            'nro_anaquel':r.nro_anaquel,
            'caract_esp':r.caract_esp,
            'cod_usu_entrega':r.cod_usu_entrega
            }
            if(r.estado == 'ALMACENADO'):
                lista.append(row) 
        resp=lista
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los objetos',
            str(e)
        ]
        status = 500

    return json.dumps(resp),status



@view.route('/objeto/filtroNombre')
def filtro_nombre():
    resp = None
    nombre = request.args.get('nom_objeto')
    status = 200
    try:
        conn = engine.connect()
        stmt = ''
        if(nombre != 'undefined'):
            stmt = select([Objeto]).where(Objeto.nom_objeto == nombre)
        else:
            stmt = select([Objeto])
        
        rs = conn.execute(stmt)
        list = []
        for item in conn.execute(stmt):
            print(item.nom_objeto)
            row = {
                'id': item.id,
                'cod_objeto':item.cod_objeto,
                'nom_objeto':item.nom_objeto,
                'categoria':item.categoria,
                'estado':item.estado,
                'marca':item.marca,
                'fecha_hallado':str(item.fecha_hallado),
                'fecha_dev':str(item.fecha_dev),
                'lugar':item.lugar,
                'nro_anaquel':item.nro_anaquel,
                'caract_esp':item.caract_esp,
                'cod_usu_entrega':item.cod_usu_entrega
            }
            if(item.estado == 'ALMACENADO'):
                list.append(row) 
        resp=list
    except Exception as e:
        resp=[
            'Se ha producido un error',
            str(e)
        ]
        status = 500
    return json.dumps(resp),status


@view.route('/solicitud/filtroNombreSol')
def filtro_nombre_sol():
    resp = None
    nombre = request.args.get('nom_objeto')
    status = 200
    try:
        conn = engine.connect()
        stmt = ''
        if(nombre != 'undefined'):
            stmt = select([Solicitud]).where(Solicitud.nom_objeto == nombre)
        else:
            stmt = select([Solicitud])
        
        rs = conn.execute(stmt)
        list = []
        for item in conn.execute(stmt):
            print(item.nom_objeto)
            row = {
                'id': item.id,
                'categoria': item.categoria,
                'nom_objeto': item.nom_objeto,
                'cod_objeto': item.cod_objeto,
                'nro_solicitud': item.nro_solicitud,
                'fecha_envio': str(item.fecha_envio),
                'lugar': item.lugar,
                'descripcion': item.descripcion,
                'caract_esp': item.caract_esp,
                'estado': item.estado,
                'fecha_rpta': str(item.fecha_rpta)
            }
            if(item.estado == 'EN PROCESO'):
                list.append(row)
        resp=list
    except Exception as e:
        resp=[
            'Se ha producido un error',
            str(e)
        ]
        status = 500
    return json.dumps(resp),status

@view.route('/solicitud/filtro')
def filtro_soli():
    resp = None
    categoria = request.args.get('categoria')
    lugar = request.args.get('lugar')
    status = 200
    try:
        conn = engine.connect()
        stmt = ''
        if(categoria != 'undefined' and lugar == 'undefined'):
            stmt = select([Solicitud]).where(Solicitud.categoria == categoria)
        elif(lugar != 'undefined' and categoria == 'undefined'):
            stmt = select([Solicitud]).where(Solicitud.lugar == lugar)
        elif(categoria == 'TODOS' and lugar != 'undefined'):
            stmt = select([Solicitud]).where(Solicitud.lugar == lugar)
        elif(lugar == 'TODOS' and categoria != 'undefined'):
            stmt = select([Solicitud]).where(Solicitud.categoria == categoria)
        elif(lugar != 'undefined' and categoria != 'undefined'):
            stmt =  (select([Solicitud])
                    .select_from(Solicitud)
                    .where((Solicitud.categoria == categoria) &
                    (Solicitud.lugar == lugar)))
        
        rs = conn.execute(stmt)
        list = []
        for item in conn.execute(stmt):
            row = {
                'id': item.id,
                'categoria': item.categoria,
                'nom_objeto': item.nom_objeto,
                'cod_objeto': item.cod_objeto,
                'nro_solicitud': item.nro_solicitud,
                'fecha_envio': str(item.fecha_envio),
                'lugar': item.lugar,
                'descripcion': item.descripcion,
                'caract_esp': item.caract_esp,
                'estado': item.estado,
                'fecha_rpta': str(item.fecha_rpta)
            }
            if(item.estado == 'EN PROCESO'):
                list.append(row)
        resp=list
    except Exception as e:
        resp=[
            'Se ha producido un error',
            str(e)
        ]
        status = 500
    return json.dumps(resp),status


@view.route('/objeto/solicitar', methods=['POST'])
def objeto_solicitar():
    nom_objeto=str(request.form['post'])
    cod_usu=str(request.form['cod_usu'])
    cod_objeto=str(request.form['post2'])
    categoria=str(request.form['post3'])
    lugar=str(request.form['post4'])
    caract_esp=str(request.form['post5'])
    print(nom_objeto)
    status = 200
    rpta = {
      'tipo_mensaje' : 'success',
      'cod_objeto': cod_objeto,
      'cod_usu':cod_usu,
      'nom_objeto': nom_objeto,
      'categoria': categoria,
      'lugar': lugar,
      'caract_esp': caract_esp,
      'mensaje' : [
        'Se ha registrado los cambios en los items del subtítulo'
      ]
    }
    '''return  json.dumps(rpta),status'''
    
    return render_template(
        '/registro/blank.html',
        rpta=rpta
        ), status


@view.route('/solicitud/agregar', methods=['POST'])
def solicitud_agregar():
   
    nom_objeto=str(request.form['nom_objeto'])
    descripcion=str(request.form['descripcion'])
    cod_objeto=request.form['cod_objeto']
    categoria=request.form['categoria']
    lugar=str(request.form['lugar'])
    caract_esp=str(request.form['caract_esp'])
    cod_usu=request.form['cod_usu']
    nro_solicitud=1003
    print(nom_objeto)
    print(descripcion)
    status = 200
    session = session_db()
    stmt=Soloriginal(
        id_objeto=cod_objeto,
        id_usuario=cod_usu,
        nro_solicitud=nro_solicitud,
        fecha_envio='2020-04-21',
        estado='EN PROCESO',
        fecha_rpta='2020-04-21',
        descripcion=descripcion)

    session.add(stmt)
    session.flush()
    print('1 ++++++++++++++++++++++++')
    session.commit()
    print('2 ++++++++++++++++++++++++')
    #users.insert().values({"name": "some name"})'''
    
    #conn.execute(stmt)
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los items del subtítulo'
      ]
    }
    
    return  json.dumps(rpta),status


@view.route('/sol_usu/detalle')
def verificar_sol_usu():
    resp = None
    soliId = request.args.get('soliId')
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Solicitud]).where(Solicitud.id == soliId)
        
        rs = conn.execute(stmt)
        list = []
        for item in conn.execute(stmt):
            print(item.nom_objeto)
            row = {
                'id': item.id,
                'categoria': item.categoria,
                'nom_objeto': item.nom_objeto,
                'cod_objeto': item.cod_objeto,
                'nro_solicitud': item.nro_solicitud,
                'fecha_envio': str(item.fecha_envio),
                'lugar': item.lugar,
                'descripcion': item.descripcion,
                'caract_esp': item.caract_esp,
                'estado': item.estado,
                'fecha_rpta': str(item.fecha_rpta)
            }
            list.append(row)
        resp=list
    except Exception as e:
        resp=[
            'Se ha producido un error',
            str(e)
        ]
        status = 500
    return json.dumps(resp),status

@view.route('/sol_usu/actualizar', methods = ['GET', 'POST'])
def actualizar_sol_usu():
    status = 200
    soliId = request.args.get('soliId')
    estado = request.args.get('estado')
    fechaRpta = request.args.get('fechaRpta')
    rpta = None
    session = session_db()
    print(soliId, estado, fechaRpta)
    try:
        session.query(Soloriginal).filter_by(id = soliId).update({
          'estado': estado,
          'fecha_rpta': fechaRpta,
        })
        session.commit()
        rpta = {
        'tipo_mensaje' : 'success',
        'mensaje' : 'Se han registrado los cambios en la tabla Solicitud'
        }
    except Exception as e:
        status = 500
        session.rollback()
        rpta = {
        'tipo_mensaje' : 'error',
        'mensaje' : [
            'Se ha producido un error en guardar los cambios en la tabla Solicitud',
            str(e)
        ]
        }
    return json.dumps(rpta),status

