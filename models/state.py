#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """
               Returns the list of City instances with
               state_id equals to the current State.id
            """
            all_cities = storage.all(City).values()
            city_list = list()
            for city in all_cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
