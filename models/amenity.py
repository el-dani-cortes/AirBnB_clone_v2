#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class with attributes"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

   if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place", secondary='place_amenity',
                                       viewonly=False,
                                       back_populates='amenites')
