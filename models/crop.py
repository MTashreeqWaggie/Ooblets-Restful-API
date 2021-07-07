from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Crop

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_crops():
    crops = session.query(Crop).all()
    return jsonify(crops=[b.serialize for b in crops])


def get_crop(crop_id):
    crops = session.query(Crop).filter_by(id=crop_id).one()
    return jsonify(crops=crops.serialize)


def makeANewCrop(crop_name, crop_location, crop_image_link,crop_seed_price,growing_time):
    addedCrop = Crop(crop_name=crop_name, crop_location=crop_location, crop_image_link = crop_image_link, crop_seed_price=crop_seed_price, growing_time=growing_time)
    session.add(addedCrop)
    session.commit()
    return jsonify(Character=addedCrop.serialize)


def updateCrop(id, crop_name, crop_location, crop_image_link,crop_seed_price,growing_time):
    updatedCrop = session.query(Crop).filter_by(id=id).one()
    if not crop_name:
        updatedCrop.crop_name = crop_name
    if not crop_location:
        updatedCrop.crop_location = crop_location
    if not crop_image_link:
        updatedCrop.crop_image_link = crop_image_link
    if not crop_seed_price:
        updatedCrop.crop_seed_price = crop_seed_price
    if not growing_time:
        updatedCrop.growing_time = growing_time
    session.add(updatedCrop)
    session.commit()
    return 'Updated a Crop with id %s' % id


def deleteACrop(id):
    bookToCrop = session.query(Crop).filter_by(id=id).one()
    session.delete(bookToCrop)
    session.commit()
    return 'Removed Crop with id %s' % id