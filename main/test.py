# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. querys
from sqlalchemy.sql import select
from main.database import engine
from main.models import Country,Usuario,Objeto

def countries_list(): # SELECT * FROM countries
    try:
        conn = engine.connect()
        stmt = select([Country]) 
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        print(resp)
    except Exception as e:
        print(str(e))

def get_country_name_by_id(id): # SELECT name FROM countries WHERE id = :id
    try:
        conn = engine.connect()
        stmt = select([Country]).where(Country.id == id)
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        print(resp[0]['name'])
    except Exception as e:
        print(str(e))

def usuario_list(): # SELECT * FROM countries
    try:
        conn = engine.connect()
        stmt = select([Usuario]) 
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        print(resp)
        return resp
    except Exception as e:
        print(str(e))

def get_password_by_id(id): # SELECT password FROM usuario WHERE cod_usuario = :id
    try:
        conn = engine.connect()
        stmt = select([Usuario]).where(Usuario.cod_usuario == id)
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        return (resp[0]['password'])
    except Exception as e:
        return (str(e)) 

def get_rol_by_id(id): # SELECT rol FROM usuario WHERE cod_usuario = :id
    try:
        conn = engine.connect()
        stmt = select([Usuario]).where(Usuario.cod_usuario == id)
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        return (resp[0]['rol'])
    except Exception as e:
        return (str(e)) 

def objeto_list():
    try:
        conn=engine.connect()
        stmt = select([Objeto]) 
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
        return resp

    except Exception as e:
        return (str(e)) 