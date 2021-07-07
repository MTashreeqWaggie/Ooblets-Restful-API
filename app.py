from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Ooblet, Character, Crop, Food, Tool

from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister

from models.ooblet import get_ooblets, get_ooblet, makeANewOoblet, updateOoblet ,deleteAOoblet
from models.character import get_characters, get_character, makeANewCharacter, updateCharacter ,deleteACharacter
from models.tool import get_tools, get_tool, makeANewTool, updateTool ,deleteATool
from models.crop import get_crops, get_crop, makeANewCrop, updateCrop ,deleteACrop
from models.food_recipes import get_foods, get_food, makeANewFood, updateFood ,deleteAFood

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)



#Connect to Database and create database session
engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# landing page that will display all the ooblets in our database
@app.route('/')
@app.route('/ooblets')
def showOoblets():
    ooblets = session.query(Ooblet).all()
    characters = session.query(Character).all()
    crops = session.query(Crop).all()
    tools = session.query(Tool).all()  
    food_recipes = session.query(Food).all()     
    return render_template("ooblets.html", ooblets=ooblets, characters=characters,crops=crops,tools=tools,food_recipes=food_recipes)

@app.route('/ooblets/docs/')
def docsOoblets():  
    return render_template("doc.html")

@app.route('/ooblets/about/')
def aboutOoblets():  
    return render_template("about.html")
# This will let us Create a new ooblet and save it in our database  
@app.route('/ooblets/new/',methods=['GET','POST'])
def newOoblet():
   if request.method == 'POST':
       newOoblet = Ooblet(ooblet_name = request.form['name'], ooblet_battle_requirements = request.form['ooblet_battle_requirements'],ooblet_location = request.form['ooblet_location'], ooblet_image_link = request.form['ooblet_image_link'])
       session.add(newOoblet)
       session.commit()
       return redirect(url_for('showOoblets'))
   else:
       return render_template('newOoblet.html')


@app.route("/ooblets/<int:ooblet_id>/edit/", methods = ['GET', 'POST'])
def editOoblet(ooblet_id):
   editedOoblet = session.query(Ooblet).filter_by(id=ooblet_id).one()
   if request.method == 'POST':
       if request.form['name']:
           editedOoblet.title = request.form['name']
           return redirect(url_for('showOoblets'))
   else:
       return render_template('editOoblet.html', ooblet = editedOoblet)


@app.route('/ooblets/<int:ooblet_id>/delete/', methods = ['GET','POST'])
def deleteOoblet(ooblet_id):
   OobletToDelete = session.query(Ooblet).filter_by(id=ooblet_id).one()
   if request.method == 'POST':
       session.delete(OobletToDelete)
       session.commit()
       return redirect(url_for('showOoblets', ooblet_id=ooblet_id))
   else:
       return render_template('deleteOoblet.html',ooblet = OobletToDelete)

#-----------------------------------------------------------------------

@app.route('/')
@app.route('/oobletsApi', methods=['GET', 'POST'])
def oobletsFunction():
    if request.method == 'GET':
        return get_ooblets()
    elif request.method == 'POST':
        ooblet_name = request.args.get('ooblet_name', '')
        ooblet_battle_requirements = request.args.get('ooblet_battle_requirements', '')
        ooblet_location = request.args.get('ooblet_location', '')
        ooblet_image_link = request.args.get('ooblet_image_link', '')
        return makeANewOoblet(ooblet_name, ooblet_battle_requirements, ooblet_location, ooblet_image_link)


@app.route('/oobletsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def oobletsFunctionId(id):
    if request.method == 'GET':
        return get_ooblet(id)

    elif request.method == 'PUT':
        ooblet_name = request.args.get('ooblet_name', '')
        ooblet_battle_requirements = request.args.get('ooblet_battle_requirements', '')
        ooblet_location = request.args.get('ooblet_location', '')
        ooblet_image_link = request.args.get('ooblet_image_link', '')
        return updateOoblet(id, ooblet_name, ooblet_battle_requirements, ooblet_location,ooblet_image_link)

    elif request.method == 'DELETE':
        return deleteAOoblet(id)


#-----------------------------------------------------------------------------------------


@app.route('/')
@app.route('/charactersApi', methods=['GET', 'POST'])
def chractersFunction():
    if request.method == 'GET':
        return get_characters()
    elif request.method == 'POST':
        character_name = request.args.get('character_name', '')
        character_location = request.args.get('character_location', '')
        character_image_link = request.args.get('character_image_link', '')
        return makeANewCharacter(character_name,character_location, character_image_link)


@app.route('/charactersApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def chractersFunctionId(id):
    if request.method == 'GET':
        return get_character(id)

    elif request.method == 'PUT':
        character_name = request.args.get('character_name', '')
        character_location = request.args.get('character_location', '')
        character_image_link = request.args.get('character_image_link', '')
        return updateCharacter(id, character_name,character_location, character_image_link)

    elif request.method == 'DELETE':
        return deleteACharacter(id)



#-----------------------------------------------------------------------------------------


@app.route('/')
@app.route('/toolsApi', methods=['GET', 'POST'])
def toolsFunction():
    if request.method == 'GET':
        return get_tools()
    elif request.method == 'POST':
        tool_name = request.args.get('tool_name', '')
        tool_description = request.args.get('tool_description', '')
        tool_location = request.args.get('tool_location', '')
        obtain_method = request.args.get('obtain_method', '')
        tool_image_link = request.args.get('tool_image_link', '')
        return makeANewTool(tool_name, tool_description, tool_location, obtain_method, tool_image_link)


@app.route('/toolsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def toolsFunctionId(id):
    if request.method == 'GET':
        return get_tool(id)

    elif request.method == 'PUT':
        tool_name = request.args.get('tool_name', '')
        tool_description = request.args.get('tool_description', '')
        tool_location = request.args.get('tool_location', '')
        obtain_method = request.args.get('obtain_method', '')
        tool_image_link = request.args.get('tool_image_link', '')
        return updateTool(id, tool_name, tool_description, tool_location, obtain_method, tool_image_link)

    elif request.method == 'DELETE':
        return deleteATool(id)

#-----------------------------------------------------------------------------------------


@app.route('/')
@app.route('/cropsApi', methods=['GET', 'POST'])
def cropsFunction():
    if request.method == 'GET':
        return get_crops()
    elif request.method == 'POST':
        crop_name = request.args.get('crop_name', '')
        crop_location = request.args.get('crop_location', '')
        crop_image_link = request.args.get('crop_image_link', '')
        crop_seed_price = request.args.get('crop_seed_price', '')
        growing_time = request.args.get('growing_time', '')
        return makeANewCrop(crop_name, crop_location, crop_image_link,crop_seed_price,growing_time)


@app.route('/cropsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def cropsFunctionId(id):
    if request.method == 'GET':
        return get_crop(id)

    elif request.method == 'PUT':
        crop_name = request.args.get('crop_name', '')
        crop_location = request.args.get('crop_location', '')
        crop_image_link = request.args.get('crop_image_link', '')
        crop_seed_price = request.args.get('crop_seed_price', '')
        growing_time = request.args.get('growing_time', '')
        return updateCrop(id, crop_name, crop_location, crop_image_link,crop_seed_price,growing_time)

    elif request.method == 'DELETE':
        return deleteACrop(id)


#-----------------------------------------------------------------------------------------


@app.route('/')
@app.route('/foodsApi', methods=['GET', 'POST'])
def foodsFunction():
    if request.method == 'GET':
        return get_foods()
    elif request.method == 'POST':
        food_name = request.args.get('food_name', '')
        food_Ingredient_1 = request.args.get('food_Ingredient_1', '')
        food_Ingredient_2 = request.args.get('food_Ingredient_2', '')
        food_Ingredient_3 = request.args.get('food_Ingredient_3', '')
        food_Ingredient_4 = request.args.get('food_Ingredient_4', '')
        food_Ingredient_5 = request.args.get('food_Ingredient_5', '')
        food_image_link = request.args.get('food_image_link', '')
        return makeANewFood(food_name, food_Ingredient_1, food_Ingredient_2,food_Ingredient_3,food_Ingredient_4,food_Ingredient_5,food_image_link)


@app.route('/foodsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def foodsFunctionId(id):
    if request.method == 'GET':
        return get_food(id)

    elif request.method == 'PUT':
        food_name = request.args.get('food_name', '')
        food_Ingredient_1 = request.args.get('food_Ingredient_1', '')
        food_Ingredient_2 = request.args.get('food_Ingredient_2', '')
        food_Ingredient_3 = request.args.get('food_Ingredient_3', '')
        food_Ingredient_4 = request.args.get('food_Ingredient_4', '')
        food_Ingredient_5 = request.args.get('food_Ingredient_5', '')
        food_image_link = request.args.get('food_image_link', '')
        return updateFood(id, food_name, food_Ingredient_1, food_Ingredient_2,food_Ingredient_3,food_Ingredient_4,food_Ingredient_5,food_image_link)

    elif request.method == 'DELETE':
        return deleteAFood(id)

    
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
   app.debug = True
   app.run()
