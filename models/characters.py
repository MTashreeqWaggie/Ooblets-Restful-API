from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Character

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_characters():
    characters = session.query(Character).all()
    return jsonify(characters=[b.serialize for b in characters])


def get_character(character_id):
    characters = session.query(Character).filter_by(id=character_id).one()
    return jsonify(characters=characters.serialize)

def get_character_location(location):
    characters = session.query(Character).filter_by(character_location=location).all()
    return jsonify(characters=[l.serialize for l in characters])

def get_character_name(characters_name):
    characters = session.query(Character).filter_by(character_name=characters_name).one()
    return jsonify(characters=characters.serialize)

def makeANewCharacter(character_name, character_location, character_image, character_gender, character_personality, occupation):
    add_character = Character(character_name=character_name, character_location=character_location, character_image = character_image,character_gender=character_gender,character_personality=character_personality, occupation=occupation)
    session.add(add_character)
    session.commit()
    return jsonify(Character=add_character.serialize)


def updateCharacter(id, character_name, character_location, character_image, character_gender, character_personality, occupation):
    updatedCharacter = session.query(Character).filter_by(id=id).one()
    if not character_name:
        updatedCharacter.character_name = character_name
    if not character_location:
        updatedCharacter.character_location = character_location
    if not character_image:
        updatedCharacter.character_image = character_image
    if not character_gender:
        updatedCharacter.gender = character_gender
    if not character_personality:
        updatedCharacter.personality = character_personality
    if not occupation:
        updatedCharacter.occupation = occupation
    session.add(updatedCharacter)
    session.commit()
    return 'Updated a Character with id %s' % id


def deleteACharacter(id):
    bookToCharacter = session.query(Character).filter_by(id=id).one()
    session.delete(bookToCharacter)
    session.commit()
    return 'Removed Character with id %s' % id