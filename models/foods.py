from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Food

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_foods():
    foods = session.query(Food).all()
    return jsonify(foods=[b.serialize for b in foods])


def get_food(food_id):
    foods = session.query(Food).filter_by(id=food_id).one()
    return jsonify(foods=foods.serialize)


def makeANewFood(food_name, food_Ingredient_1, food_Ingredient_2,food_Ingredient_3,food_Ingredient_4,food_Ingredient_5,food_image, food_value, food_energy):
    addedFood = Food(food_name = food_name, food_Ingredient_1 = food_Ingredient_1, food_Ingredient_2 = food_Ingredient_2, food_Ingredient_3 = food_Ingredient_3,food_Ingredient_4 = food_Ingredient_4, food_Ingredient_5 = food_Ingredient_5, food_image = food_image, food_value = food_value, food_energy=food_energy)
    session.add(addedFood)
    session.commit()
    return jsonify(Food=addedFood.serialize)


def updateFood(id, food_name, food_Ingredient_1, food_Ingredient_2, food_Ingredient_3, food_Ingredient_4, food_Ingredient_5, food_image, food_value, food_energy):
    updatedFood = session.query(Food).filter_by(id=id).one()
    if not food_name:
        updatedFood.food_name = food_name
    if not food_Ingredient_1:
        updatedFood.food_Ingredient_1 = food_Ingredient_1
    if not food_Ingredient_2:
        updatedFood.food_Ingredient_2 = food_Ingredient_2
    if not food_Ingredient_3:
        updatedFood.food_Ingredient_3 = food_Ingredient_3
    if not food_Ingredient_4:
        updatedFood.food_Ingredient_4 = food_Ingredient_4
    if not food_Ingredient_5:
        updatedFood.food_Ingredient_5 = food_Ingredient_5
    if not food_image:
        updatedFood.food_image = food_image
    if not food_value:
        updatedFood.food_value = food_value
    if not food_energy:
        updatedFood.food_energy = food_energy
    session.add(updatedFood)
    session.commit()
    return 'Updated a Food with id %s' % id


def deleteAFood(id):
    bookToFood = session.query(Food).filter_by(id=id).one()
    session.delete(bookToFood)
    session.commit()
    return 'Removed Foods with id %s' % id