# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2. creacion de modelos 
from sqlalchemy import Column, Integer, String,DateTime,ForeignKey
from main.database import Base

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    cod_usuario = Column(String)
    password = Column(String)
    correo_electronico = Column(String)
    rol = Column(Integer)
    id_dpto = Column(Integer)

class Dpto(Base):
    __tablename__ = 'dpto'
    cod_dpto=Column(Integer, primary_key=True)
    dpto_name= Column(String)
    email=Column(String)
    telefono=Column(Integer)
    anexo=Column(Integer)
    edificio=Column(String)
    piso=Column(Integer)
    
class Donativo(Base):
    __tablename__ = 'DONATIVO'
    cod_donativo=Column(Integer, primary_key=True)
    cod_dpto=Column(Integer,ForeignKey('dpto.cod_dpto'))
    fecha_envio=Column(DateTime)
    descripcion=Column(String)
    cantidad= Column(Integer)
    email=Column(String)
    telefono=Column(Integer)

class Objeto(Base):
    __tablename__='objeto'
    id = Column(Integer, primary_key=True,autoincrement=True)
    cod_objeto = Column(Integer)
    nom_objeto = Column(String)
    categoria = Column(String)
    marca = Column(String)
    estado = Column(String)
    fecha_hallado=Column(DateTime)
    fecha_dev=Column(DateTime)
    lugar=Column(String)
    nro_anaquel=Column(Integer)
    caract_esp=Column(String)
    cod_usu_entrega=Column(Integer)
    cod_donacion=Column(Integer)


class Solicitud(Base):
    __tablename__='solicitud_prueba'
    id=Column(Integer, primary_key=True,autoincrement=True)
    categoria=Column(String)
    nom_objeto = Column(String)
    cod_objeto= Column(Integer)
    nro_solicitud=Column(Integer)
    fecha_envio=Column(DateTime)
    lugar=Column(String)
    descripcion=Column(String)
    caract_esp=Column(String)
    estado=Column(String)
    fecha_rpta=Column(DateTime)
    cod_usuario = Column(String)
    nombre_persona = Column(String)

class Soloriginal(Base):
    __tablename__='solicitud'
    id=Column(Integer, primary_key=True,autoincrement=True)
    id_objeto= Column(Integer)
    id_usuario= Column(Integer)
    nro_solicitud=Column(Integer)
    fecha_envio=Column(DateTime)
    estado=Column(String)
    fecha_rpta=Column(DateTime)
    descripcion=Column(String)
    
class SolicitudDpto(Base):
    __tablename__='solicitud_dpto'
    id=Column(Integer, primary_key=True)
    codigo_dpto=Column(Integer)
    estado=Column(String)
    categoria=Column(String)
    descripcion=Column(String)
    cantidad_objeto=Column(Integer)
    fecha_envio=Column(DateTime)
    fecha_rpta=Column(DateTime)



class NombreDpto(Base):
    __tablename__ = 'nombre_dpto'
    id_usuario = Column(Integer, primary_key=True)
    id_dpto = Column(Integer)
    dpto_name = Column(String)

class ObjetoDispoDon(Base):
    __tablename__='obj_disp_don'
    id = Column(Integer, primary_key=True)
    cod_objeto = Column(Integer)
    nom_objeto = Column(String)
    categoria = Column(String)
    marca = Column(String)
    estado = Column(String)
    fecha_hallado=Column(DateTime)
    fecha_dev=Column(DateTime)
    lugar=Column(String)
    nro_anaquel=Column(Integer)
    caract_esp=Column(String)
    cod_usu_entrega=Column(Integer)

class Donacion(Base):
    __tablename__ = 'donacion'
    id = Column(Integer, primary_key=True,autoincrement=True)
    soli_id = Column(Integer)
    fecha_crea = Column(DateTime)