#!/usr/bin/env python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage(Base):
    """This class manages storage of hbnb models in MYSQL"""
    __engine = None
    __session = None

    def __init__(self):
        """The class constructor"""
        if os.environ.get("HBNB_MYSQL_USER"):
            user = os.environ.get("HBNB_MYSQL_USER")
        if os.environ.get("HBNB_MYSQL_PWD"):
            passwd = os.environ.get("HBNB_MYSQL_PWD")
        if os.environ.get("HBNB_MYSQL_HOST"):
            host = os.environ.get("HBNB_MYSQL_HOST")
        if os.environ.get("HBNB_MYSQL_DB"):
            db = os.environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine("""mysql+mysqldb://{}:{}@{}:3306/
                                      {}""".format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == "test":
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

        obj_dict = dict{}
        if cls:
            if cls in all_classes:
                class_objs = self.__session.query(cls).all()
            else:
                return
        else:
            class_objs = self.__session.query(State, City).all()
        for instance in class_objs:
            key = (str(cls)).split('.')[2].rstrip(">'") + '.' + instance.id
            obj_dict[key] = instance
        return obj_dict

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
