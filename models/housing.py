from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Housing

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_housing():
    housing = session.query(Housing).all()
    return jsonify(housing=[b.serialize for b in housing])

def get_house(housing_id):
    housing = session.query(Housing).filter_by(id=housing_id).one()
    return jsonify(housing=housing.serialize)

def makeANewHouse(housing_name, housing_category, housing_price, housing_location, housing_image):
    add_house = Housing(housing_name=housing_name, housing_category=housing_category, housing_price = housing_price, housing_location = housing_location, housing_image = housing_image)
    session.add(add_house)
    session.commit()
    return jsonify(Housing=add_house.serialize)

def updateHouse(id, housing_name, housing_category, housing_price, housing_location, housing_image):
    updatedHouse = session.query(Housing).filter_by(id=id).one()
    if not housing_name:
        updatedHouse.housing_name = housing_name
    if not housing_category:
        updatedHouse.housing_category = housing_category
    if not housing_price:
        updatedHouse.housing_price = housing_price
    if not housing_location:
        updatedHouse.housing_location = housing_location
    if not housing_image:
        updatedHouse.housing_image = housing_image
    session.add(updatedHouse)
    session.commit()
    return 'Updated a House with id %s' % id


def deleteAHouse(id):
    bookToHouse = session.query(Housing).filter_by(id=id).one()
    session.delete(bookToHouse)
    session.commit()
    return 'Removed House with id %s' % id