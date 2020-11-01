#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json,datetime
from flask import Blueprint, render_template, session, request, redirect
from main.models import Country,Objeto
from main.database import engine,session_db
from sqlalchemy import select,insert
from datetime import date,datetime,timedelta


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
            lista.append(row) 
        #resp = [dict(r) for r in conn.execute(stmt)]
        resp=lista
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los paises',
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
    #users.insert().values({"name": "some name"})
    
    #conn.execute(stmt)
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

@view.route('/objeto/filtrar', methods=['GET','POST'])
def buscar():
    print("aaaaaa")
    lugar=str(request.form['lugar'])
    categoria=str(request.form['categoria'])
    fecha_inicio=request.form['trip-inicio']
    print(fecha_inicio)
    fecha_fin=request.form['trip-fin']
    #dt_object1 =datetime.strptime(fecha_inicio, '%Y-%m-%d')
    #dt_object2 =datetime.strptime(fecha_fin, '%Y-%m-%d')
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Objeto])
        rs = conn.execute(stmt)
        lista = []
        for r in conn.execute(stmt):
            print(fecha_inicio)
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
            if r.categoria==categoria or r.lugar==lugar:
                lista.append(row) 
       
        rpta=lista
    except Exception as e:
        rpta = [
            'Se ha producido un error en listar los paises',
            str(e)
        ]
        status = 500
     

    return json.dumps(rpta),status


 


'''def generar_rango_fechas(fecha_1, fecha_2,fecha_3):
    fechas = []
    dias = (fecha_2 - fecha_1).days + 1

    for i in range(0,len(dias)):
        fechas.append(fecha_1 + timedelta(dias[i]))
    
    for r in range(0,len(fechas)):
        if fechas[r]==fecha_3:
            return True
    return False'''


    