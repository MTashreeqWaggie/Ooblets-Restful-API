from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Clothing

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_clothings():
    clothing = session.query(Clothing).all()
    return jsonify(clothing=[b.serialize for b in clothing])

def get_clothing(clothing_id):
    clothing = session.query(Clothing).filter_by(id=clothing_id).one()
    return jsonify(clothing=clothing.serialize)

def makeANewClothing(clothing_name, category, clothing_price, kibbonbon_lvl, clothing_location, clothing_image):
    add_clothing = Clothing(clothing_name=clothing_name, category=category, clothing_price = clothing_price, kibbonbon_lvl = kibbonbon_lvl, clothing_location = clothing_location, clothing_image = clothing_image)
    session.add(add_clothing)
    session.commit()
    return jsonify(Clothing=add_clothing.serialize)

def updateClothing(id, clothing_name, category, clothing_price, kibbonbon_lvl, clothing_location, clothing_image):
    updatedClothing = session.query(Clothing).filter_by(id=id).one()
    if not clothing_name:
        updatedClothing.clothing_name = clothing_name
    if not category:
        updatedClothing.category = category
    if not clothing_price:
        updatedClothing.clothing_price = clothing_price
    if not kibbonbon_lvl:
        updatedClothing.kibbonbon_lvl = kibbonbon_lvl
    if not clothing_location:
        updatedClothing.clothing_location = clothing_location
    if not clothing_image:
        updatedClothing.clothing_image = clothing_image
    session.add(updatedClothing)
    session.commit()
    return 'Updated a Clothing with id %s' % id


def deleteAClothing(id):
    bookToClothing = session.query(Clothing).filter_by(id=id).one()
    session.delete(bookToClothing)
    session.commit()
    return 'Removed Clothing with id %s' % id