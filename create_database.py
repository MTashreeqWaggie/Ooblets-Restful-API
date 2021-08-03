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
    name = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    location = Column(String(50), nullable=False)
    battle_requirements = Column(String(50), nullable=False)
    signature_move_lvl_1_name = Column(String(50), nullable=False)
    signature_move_lvl_1_beat_requirement = Column(Integer, nullable=False)
    signature_move_lvl_1_effect = Column(String(100), nullable=False)
    signature_move_lvl_2_name = Column(String(50), nullable=False)
    signature_move_lvl_2_beat_requirement = Column(Integer, nullable=False)
    signature_move_lvl_2_effect = Column(String(100), nullable=False)
    signature_move_lvl_3_name = Column(String(50), nullable=False)
    signature_move_lvl_3_beat_requirement = Column(Integer, nullable=False)
    signature_move_lvl_3_effect = Column(String(100), nullable=False)
    ooblet_image = Column(String(250), nullable=False)



    @property
    def serialize(self):
        return {
            'name': self.name,
            'battle_requirements': self.battle_requirements,
            'description': self.description,
            'location': self.location,
            'signature_move_lvl_1_name': self.signature_move_lvl_1_name,
            'signature_move_lvl_1_beat_requirement': self.signature_move_lvl_1_beat_requirement,
            'signature_move_lvl_1_effect': self.signature_move_lvl_1_effect,
            'signature_move_lvl_2_name': self.signature_move_lvl_2_name,
            'signature_move_lvl_2_beat_requirement': self.signature_move_lvl_2_beat_requirement,
            'signature_move_lvl_2_effect': self.signature_move_lvl_2_effect,
            'signature_move_lvl_3_name': self.signature_move_lvl_3_name,
            'signature_move_lvl_3_beat_requirement': self.signature_move_lvl_3_beat_requirement,
            'signature_move_lvl_3_effect': self.signature_move_lvl_3_effect,
            'ooblet_image': self.ooblet_image,
            'id': self.id,
        }

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    character_name= Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    personality = Column(String(250), nullable=False)
    character_location = Column(String(50), nullable=False)
    character_image = Column(String(250), nullable=False)
    occupation = Column(String(50), nullable=False)

    @property
    def serialize(self):
        return {
            'character_name': self.character_name,
            'gender': self.gender,
            'personality': self.personality,
            'character_location': self.character_location,
            'character_image': self.character_image,
            'occupation': self.occupation,
            'id': self.id,
        }

class Clothing(Base):
    __tablename__ = 'clothing'

    id = Column(Integer, primary_key=True)
    clothing_name= Column(String(50), nullable=False)
    category= Column(String(50), nullable=False)
    clothing_price = Column(Integer, nullable=False)
    kibbonbon_lvl = Column(Integer, nullable=False)
    clothing_location = Column(String(50), nullable=False)
    clothing_image = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'clothing_name': self.clothing_name,
            'category': self.category,
            'clothing_price': self.clothing_price,
            'kibbonbon_lvl': self.kibbonbon_lvl,
            'clothing_location': self.clothing_location,
            'clothing_image': self.clothing_image,
            'id': self.id,
        }

class Housing(Base):
    __tablename__ = 'housing'

    id = Column(Integer, primary_key=True)
    housing_name= Column(String(50), nullable=False)
    housing_category= Column(String(50), nullable=False)
    housing_price = Column(Integer, nullable=False)
    housing_location = Column(String(50), nullable=False)
    housing_image = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'housing_name': self.housing_name,
            'housing_category': self.housing_category,
            'housing_price': self.housing_price,
            'housing_location': self.housing_location,
            'housing_image': self.housing_image,
            'id': self.id,
        }

class Crops(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    crop_name= Column(String(30), nullable=False)
    crop_location = Column(String(30), nullable=False)
    crop_image = Column(String(250), nullable=False)
    crop_seed_price = Column(Integer, nullable=False)
    growing_time = Column(Integer, nullable=False)


    @property
    def serialize(self):
        return {
            'crop_name': self.crop_name,
            'crop_location': self.crop_location,
            'crop_image': self.crop_image,
            'crop_seed_price': self.crop_seed_price,
            'growing_time': self.growing_time,
            'id': self.id,
        }

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    food_name= Column(String(50), nullable=False)
    food_Ingredient_1 = Column(String(50), nullable=False)
    food_Ingredient_2 = Column(String(50), nullable=False)
    food_Ingredient_3 = Column(String(50), nullable=False)
    food_Ingredient_4 = Column(String(50), nullable=False)
    food_Ingredient_5 = Column(String(50), nullable=False)
    food_value = Column(Integer, nullable=False)
    food_energy = Column(Integer, nullable=False)
    food_image = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'food_name': self.food_name,
            'food_Ingredient_1': self.food_Ingredient_1,
            'food_Ingredient_2': self.food_Ingredient_2,
            'food_Ingredient_3': self.food_Ingredient_3,
            'food_Ingredient_4': self.food_Ingredient_4,
            'food_Ingredient_5': self.food_Ingredient_5,
            'food_image': self.food_image,
            'food_value': self.food_value,
            'food_energy': self.food_energy,
            'id': self.id,
        }

class Tools(Base):
    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    tool_name= Column(String(50), nullable=False)
    tool_value = Column(Integer, nullable=False)
    tool_location = Column(String(200), nullable=False)
    tool_description = Column(String(200), nullable=False)
    obtain_method = Column(String(200), nullable=False)
    tool_image= Column(String(200), nullable=False)
    
    @property
    def serialize(self):
        return {
            'tool_name': self.tool_name,
            'tool_value': self.tool_value,
            'tool_location': self.tool_location,
            'tool_description': self.tool_description,
            'obtain_method': self.obtain_method,
            'tool_image': self.tool_image,
            'id': self.id,
        }

class Badges(Base):
    __tablename__ = 'badges'

    id = Column(Integer, primary_key=True)
    badge_image= Column(String(250), nullable=False)
    badge_reward = Column(Integer, nullable=False)
    badge_category = Column(String(200), nullable=False)
    badge_task_description = Column(String(200), nullable=False)
    
    @property
    def serialize(self):
        return {
            'badge_image': self.badge_image,
            'badge_reward': self.badge_reward,
            'badge_category': self.badge_category,
            'badge_task_description': self.badge_task_description,
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