from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Tool

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_tools():
    tools = session.query(Tool).all()
    return jsonify(Tools=[b.serialize for b in tools])


def get_tool(tool_id):
    tools = session.query(Tool).filter_by(id=tool_id).one()
    return jsonify(tools=tools.serialize)


def makeANewTool(tool_name, tool_description, tool_location, obtain_method, tool_image_link):
    addedTool = Tool(tool_name=tool_name, tool_description=tool_description, tool_location = tool_location, obtain_method =obtain_method,tool_image_link=tool_image_link)
    session.add(addedTool)
    session.commit()
    return jsonify(Tool=addedTool.serialize)


def updateTool(id, tool_name, tool_description, tool_location, obtain_method, tool_image_link):
    updatedTool = session.query(Tool).filter_by(id=id).one()
    if not tool_name:
        updatedTool.tool_name = tool_name
    if not tool_description:
        updatedTool.tool_description = tool_description
    if not tool_location:
        updatedTool.tool_location = tool_location
    if not obtain_method:
        updatedTool.obtain_method = obtain_method
    if not tool_image_link:
        updatedTool.tool_image_link = tool_image_link
    session.add(updatedTool)
    session.commit()
    return 'Updated a Tool with id %s' % id


def deleteATool(id):
    bookToTool = session.query(Tool).filter_by(id=id).one()
    session.delete(bookToTool)
    session.commit()
    return 'Removed Tool with id %s' % id