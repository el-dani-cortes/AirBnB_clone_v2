#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')
    elif getenv("HBNB_TYPE_STORAGE") == "file":
        cities = self.cities

        @property
        def cities(self):
            """Getter the cities for FileStorage
            """
            city_list = []
            for obj in FileStorage.all(City).keys():
                if obj.state_id == self.id:
                    city_list = city_list.append[obj]
            return city_list
