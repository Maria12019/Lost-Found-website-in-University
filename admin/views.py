#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json,datetime
from flask import Blueprint, render_template, session, request, redirect
from main.models import Country,Objeto
from main.database import engine,session_db
from sqlalchemy import select,insert, between
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
            lista.append(row) 
        resp=lista
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los objetos',
            str(e)
        ]
        status = 500

    return json.dumps(resp),status



