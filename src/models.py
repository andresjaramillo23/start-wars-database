import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(String(39), nullable=False)
    model = Column(String(250))
    name = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)

class  Characters(Base):
    __tablename__ = 'characters' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    home_planet_id = Column(Integer, ForeignKey('planets.id')) 
    home_planet = relationship(Planets)
    film_id = Column(Integer, ForeignKey('films.id')) 
    film = relationship(Films)

class Pilots(Base):
    __tablename__ = 'pilots'    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id')) 
    character = relationship(Characters)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id')) 
    vehicles = relationship(Vehicles)

class Appearance(Base):
    __tablename__ = 'Appearances'    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id')) 
    character = relationship(Characters)
    film_id = Column(Integer, ForeignKey('films.id')) 
    film = relationship(Films)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')