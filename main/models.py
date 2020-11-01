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
    id = Column(Integer, primary_key=True)
    cod_objeto= Column(Integer)
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


