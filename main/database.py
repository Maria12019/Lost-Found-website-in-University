# !/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# engine = create_engine('sqlite:///db/app.db')
engine = create_engine('postgres://kfrkfdlhvrgpyy:4b54935ddcdc41587d33b0ed44e2d6d31bf619429fd239afafa1cd3cd47ea138@ec2-18-211-86-133.compute-1.amazonaws.com:5432/de96ac6n8kinvn')
session_db = sessionmaker()
session_db.configure(bind=engine)