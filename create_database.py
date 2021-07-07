import sys
# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

#for configuration
from sqlalchemy import create_engine

import sqlite3

#create declarative_base instance
Base = declarative_base()

class Ooblet(Base):
    __tablename__ = 'ooblet'

    id = Column(Integer, primary_key=True)
    ooblet_name = Column(String(250), nullable=False)
    ooblet_location = Column(String(250))
    ooblet_battle_requirements = Column(String(250))
    ooblet_image_link = Column(String(250))


    @property
    def serialize(self):
        return {
            'ooblet_name': self.ooblet_name,
            'ooblet_battle_requirements': self.ooblet_battle_requirements,
            'ooblet_location': self.ooblet_location,
            'ooblet_image_link': self.ooblet_image_link,
            'id': self.id,
        }

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    character_name= Column(String(250), nullable=False)
    character_location = Column(String(250))
    character_image_link = Column(String(250))

    @property
    def serialize(self):
        return {
            'character_name': self.character_name,
            'character_location': self.character_location,
            'character_image_link': self.character_image_link,
            'id': self.id,
        }

class Tool(Base):
    __tablename__ = 'tool'

    id = Column(Integer, primary_key=True)
    tool_name= Column(String(250), nullable=False)
    tool_description = Column(String(250))
    tool_location = Column(String(250))
    obtain_method = Column(String(250))
    tool_image_link = Column(String(250))

    @property
    def serialize(self):
        return {
            'tool_name': self.tool_name,
            'tool_description': self.tool_description,
            'tool_location': self.tool_location,
            'obtain_method': self.obtain_method,
            'tool_image_link': self.tool_image_link,
            'id': self.id,
        }

class Crop(Base):
    __tablename__ = 'crop'

    id = Column(Integer, primary_key=True)
    crop_name= Column(String(250), nullable=False)
    crop_location = Column(String(250))
    crop_image_link = Column(String(250))
    crop_seed_price = Column(String(250))
    growing_time = Column(String(250))


    @property
    def serialize(self):
        return {
            'crop_name': self.crop_name,
            'crop_location': self.crop_location,
            'crop_image_link': self.crop_image_link,
            'crop_seed_price': self.crop_seed_price,
            'growing_time': self.growing_time,
            'id': self.id,
        }

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    food_name= Column(String(250), nullable=False)
    food_Ingredient_1 = Column(String(250))
    food_Ingredient_2 = Column(String(250))
    food_Ingredient_3 = Column(String(250))
    food_Ingredient_4 = Column(String(250))
    food_Ingredient_5 = Column(String(250))
    food_image_link = Column(String(250))

    @property
    def serialize(self):
        return {
            'food_name': self.food_name,
            'food_Ingredient_1': self.food_Ingredient_1,
            'food_Ingredient_1': self.food_Ingredient_2,
            'food_Ingredient_1': self.food_Ingredient_3,
            'food_Ingredient_1': self.food_Ingredient_4,
            'food_Ingredient_1': self.food_Ingredient_5,
            'food_image_link': self.food_image_link,
            'id': self.id,
        }


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///ooblets-collection.db')

Base.metadata.create_all(engine)


connection = sqlite3.connect('ooblets-collection.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY ,username text, password text)"
cursor.execute(create_table)

connection.commit()
connection.close()