from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Ooblet
from flask import jsonify

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_ooblets():
    ooblets = session.query(Ooblet).all()
    return jsonify(ooblets=[b.serialize for b in ooblets])


def get_ooblet(ooblet_id):
    ooblets = session.query(Ooblet).filter_by(id=ooblet_id).one()
    return jsonify(ooblets=ooblets.serialize)


def makeANewOoblet(ooblet_name,  ooblet_battle_requirements, ooblet_location, ooblet_image_link):
    addedooblet = Ooblet(ooblet_name=ooblet_name, ooblet_battle_requirements=ooblet_battle_requirements,ooblet_location=ooblet_location, ooblet_image_link = ooblet_image_link)
    session.add(addedooblet)
    session.commit()
    return jsonify(Ooblet=addedooblet.serialize)


def updateOoblet(id, ooblet_name, ooblet_battle_requirements, ooblet_location, ooblet_image_link):
    updatedOoblet = session.query(Ooblet).filter_by(id=id).one()
    if not ooblet_name:
        updatedOoblet.ooblet_name = ooblet_name
    if not ooblet_battle_requirements:
        updatedOoblet.ooblet_battle_requirements = ooblet_battle_requirements
    if not ooblet_location:
        updatedOoblet.ooblet_location = ooblet_location
    if not ooblet_image_link:
        updatedOoblet.ooblet_image_link = ooblet_image_link
    session.add(updatedOoblet)
    session.commit()
    return 'Updated a Ooblet with id %s' % id


def deleteAOoblet(id):
    bookToOoblet = session.query(Ooblet).filter_by(id=id).one()
    session.delete(bookToOoblet)
    session.commit()
    return 'Removed Ooblet with id %s' % id