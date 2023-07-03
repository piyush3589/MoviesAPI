from distutils.command.config import config

from dotenv import dotenv_values
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

config = dotenv_values("keys.env")

engine = create_engine(config["DATABASE_URL"])
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(config["DATABASE_URL"])
