from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Badges

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_badges():
    badges = session.query(Badges).all()
    return jsonify(badges=[b.serialize for b in badges])


def get_badge(badge_id):
    badges = session.query(Badges).filter_by(id=badge_id).one()
    return jsonify(badges=badges.serialize)


def makeANewBadge(badge_image, badge_reward, badge_category, badge_task_description):
    add_badge = Badges(badge_image=badge_image, badge_reward=badge_reward, badge_category = badge_category, badge_task_description=badge_task_description)
    session.add(add_badge)
    session.commit()
    return jsonify(Badges=add_badge.serialize)


def updateBadge(id, badge_image, badge_reward, badge_category, badge_task_description):
    updatedBadge = session.query(Badges).filter_by(id=id).one()
    if not badge_image:
        updatedBadge.badge_image = badge_image
    if not badge_reward:
        updatedBadge.badge_reward = badge_reward
    if not badge_category:
        updatedBadge.badge_category = badge_category
    if not badge_task_description:
        updatedBadge.badge_task_description = badge_task_description
    session.add(updatedBadge)
    session.commit()
    return 'Updated a Badge with id %s' % id


def deleteABadge(id):
    bookToBadge = session.query(Badges).filter_by(id=id).one()
    session.delete(bookToBadge)
    session.commit()
    return 'Removed Badge with id %s' % id