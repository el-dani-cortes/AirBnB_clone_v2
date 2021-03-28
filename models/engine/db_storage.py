#!/usr/bin/python3
"""
Script that creates a new engine to communicate with database
"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


# All enviroment varibles
env = {
    "USER": os.environ.get('HBNB_MYSQL_USER'),
    "PWD": os.environ.get('HBNB_MYSQL_PWD'),
    "HOST": os.environ.get('HBNB_MYSQL_HOST'),
    "DB": os.environ.get('HBNB_MYSQL_DB'),
    "STORAGE": os.environ.get('HBNB_TYPE_STORAGE'),
    "ENV": os.environ.get('HBNB_ENV')
}

class DBStorage:
    """New engine class definition"""
    __engine = None
    __session = None


    def __init__(self):
        """Constructor for instance of this class"""
        self.__engine =  create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                       .format(env['USER'],
                                               env['PWD'],
                                               env['HOST'],
                                               env['DB']),
                                       pool_pre_ping=True)
        if env['ENV'] == 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to query all objects depending of the class"""
        classes = [User, Place, State, City, Amenity, Review]

        if cls == None:
            query = self.__session.query(*classes).all()
        else:
            query = self.__session.query(cls).all()
        dictionary = {}
        for obj in query:
            obj_dict = obj.to_dict
            for key, val in obj_dict:
                dictionary[key] = eval(val["__class__"])(**val)
        return dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
