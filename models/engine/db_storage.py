#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
import os
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """This class manages storage of hbnb models in MYSQL"""
    __engine = None
    __session = None

    def __init__(self):
        """The class constructor"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".format
                                      (user, passwd, host, db),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.meta.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        all_classes = [City, Amenity, Place, Review, State, User]

        obj_list = list()
        if cls:
            if cls in all_classes:
                class_objs = self.__session.query(cls).all()
            else:
                return
        else:
            for cls in all_classes:
                class_objs = self.__session.query(cls).all()
        for instance in class_objs:
            if instance.__dict__['_sa_instance_state']:
                del instance.__dict__['_sa_instance_state']
            obj_list.append((instance))
        return obj_list

    def new(self, obj):
        """
            Adds the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
            Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            Create all tables in the database
        """
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
            Close the session()
        """
        self.__session.remove()
