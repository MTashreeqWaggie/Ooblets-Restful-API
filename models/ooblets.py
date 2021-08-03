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

def get_ooblet_location(ooblet_location):
    ooblets = session.query(Ooblet).filter_by(location=ooblet_location).all()
    return jsonify(ooblets=[l.serialize for l in ooblets])

def makeANewOoblet(name,  description, location, battle_requirements,signature_move_lvl_1_name,signature_move_lvl_1_beat_requirement,signature_move_lvl_1_effect,signature_move_lvl_2_name,signature_move_lvl_2_beat_requirement,signature_move_lvl_2_effect,signature_move_lvl_3_name,signature_move_lvl_3_beat_requirement,signature_move_lvl_3_effect,ooblet_image):
    add_ooblet = Ooblet(name=name, description=description,location=location, ooblet_image = ooblet_image,battle_requirements=battle_requirements,signature_move_lvl_1_name=signature_move_lvl_1_name,signature_move_lvl_1_beat_requirement=signature_move_lvl_1_beat_requirement,signature_move_lvl_1_effect=signature_move_lvl_1_effect,signature_move_lvl_2_name=signature_move_lvl_2_name,signature_move_lvl_2_beat_requirement=signature_move_lvl_2_beat_requirement,signature_move_lvl_2_effect=signature_move_lvl_2_effect,signature_move_lvl_3_name=signature_move_lvl_3_name,signature_move_lvl_3_beat_requirement=signature_move_lvl_3_beat_requirement,signature_move_lvl_3_effect=signature_move_lvl_3_effect)
    session.add(add_ooblet)
    session.commit()
    return jsonify(Ooblet=add_ooblet.serialize)
    
def updateOoblet(id,name,  description, location, battle_requirements,signature_move_lvl_1_name,signature_move_lvl_1_beat_requirement,signature_move_lvl_1_effect,signature_move_lvl_2_name,signature_move_lvl_2_beat_requirement,signature_move_lvl_2_effect,signature_move_lvl_3_name,signature_move_lvl_3_beat_requirement,signature_move_lvl_3_effect,ooblet_image):
    updatedOoblet = session.query(Ooblet).filter_by(id=id).one()
    if not name:
        updatedOoblet.name = name
    if not description:
        updatedOoblet.description = description
    if not location:
        updatedOoblet.location = location
    if not battle_requirements:
        updatedOoblet.battle_requirements = battle_requirements
    if not signature_move_lvl_1_name:
        updatedOoblet.signature_move_lvl_1_name = signature_move_lvl_1_name
    if not signature_move_lvl_1_beat_requirement:
        updatedOoblet.signature_move_lvl_1_beat_requirement = signature_move_lvl_1_beat_requirement
    if not signature_move_lvl_1_effect:
        updatedOoblet.signature_move_lvl_1_effect = signature_move_lvl_1_effect
    if not signature_move_lvl_2_name:
        updatedOoblet.signature_move_lvl_1_name = signature_move_lvl_1_name
    if not signature_move_lvl_2_beat_requirement:
        updatedOoblet.signature_move_lvl_1_beat_requirement = signature_move_lvl_1_beat_requirement
    if not signature_move_lvl_2_effect:
        updatedOoblet.signature_move_lvl_1_effect = signature_move_lvl_1_effect
    if not signature_move_lvl_3_name:
        updatedOoblet.signature_move_lvl_1_name = signature_move_lvl_1_name
    if not signature_move_lvl_3_beat_requirement:
        updatedOoblet.signature_move_lvl_1_beat_requirement = signature_move_lvl_1_beat_requirement
    if not signature_move_lvl_3_effect:
        updatedOoblet.signature_move_lvl_1_effect = signature_move_lvl_1_effect
    if not ooblet_image:
        updatedOoblet.ooblet_image = ooblet_image
    session.add(updatedOoblet)
    session.commit()
    return 'Updated a Ooblet with id %s' % id

def deleteAOoblet(id):
    bookToOoblet = session.query(Ooblet).filter_by(id=id).one()
    session.delete(bookToOoblet)
    session.commit()
    return 'Removed Ooblet with id %s' % id
