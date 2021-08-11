import os 

from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Ooblet, Character, Crops, Food, Tools, Badges, Housing , Clothing

from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister

from models.ooblets import get_ooblets, get_ooblet, makeANewOoblet, updateOoblet, deleteAOoblet,  get_ooblet_name
from models.characters import get_characters, get_character, makeANewCharacter, updateCharacter, deleteACharacter, get_character_name
from models.tools import get_tools, get_tool, makeANewTool, updateTool, deleteATool
from models.crops import get_crops, get_crop, makeANewCrop, updateCrop, deleteACrop, get_crop_name
from models.housing import get_housing, get_house, makeANewHouse, updateHouse, deleteAHouse
from models.clothing import get_clothings, get_clothing, makeANewClothing, updateClothing, deleteAClothing, get_clothing_category
from models.badges import get_badges, get_badge, makeANewBadge, updateBadge , deleteABadge,get_badge_category
from models.foods import get_foods, get_food, makeANewFood, updateFood , deleteAFood

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)

engine = create_engine('sqlite:///ooblets-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/ooblets')
def showOoblets():
    return render_template("ooblets.html")

#-----------------------------------------------------------------------

"""Endpoints for Ooblets"""

@app.route('/')
@app.route('/oobletsApi', methods=['GET', 'POST'])
def oobletsFunction():
    if request.method == 'GET':
        return get_ooblets()
    elif request.method == 'POST':
        ooblet_name = request.args.get('ooblet_name', '')
        ooblet_description = request.args.get('ooblet_description', '')
        ooblet_location = request.args.get('ooblet_location', '')
        battle_requirements = request.args.get('battle_requirements', '')
        signature_move_lvl_1_name = request.args.get('signature_move_lvl_1_name', '')
        signature_move_lvl_1_beat_requirement = request.args.get('signature_move_lvl_1_beat_requirement', '')
        signature_move_lvl_1_effect = request.args.get('signature_move_lvl_1_effect', '')
        signature_move_lvl_2_name = request.args.get('signature_move_lvl_2_name', '')
        signature_move_lvl_2_beat_requirement = request.args.get('signature_move_lvl_2_beat_requirement', '')
        signature_move_lvl_2_effect = request.args.get('signature_move_lvl_2_effect', '')
        signature_move_lvl_3_name = request.args.get('signature_move_lvl_3_name', '')
        signature_move_lvl_3_beat_requirement = request.args.get('signature_move_lvl_3_beat_requirement', '')
        signature_move_lvl_3_effect = request.args.get('signature_move_lvl_3_effect', '')
        ooblet_image = request.args.get('ooblet_image', '')
        return makeANewOoblet(ooblet_name,  ooblet_description, ooblet_location, battle_requirements,signature_move_lvl_1_name,signature_move_lvl_1_beat_requirement,signature_move_lvl_1_effect,signature_move_lvl_2_name,signature_move_lvl_2_beat_requirement,signature_move_lvl_2_effect,signature_move_lvl_3_name,signature_move_lvl_3_beat_requirement,signature_move_lvl_3_effect,ooblet_image)


@app.route('/oobletsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def oobletsFunctionId(id):
    if request.method == 'GET':
        return get_ooblet(id)

    elif request.method == 'PUT':
        ooblet_name = request.args.get('ooblet_name', '')
        ooblet_description = request.args.get('ooblet_description', '')
        ooblet_location = request.args.get('ooblet_location', '')
        battle_requirements = request.args.get('battle_requirements', '')
        signature_move_lvl_1_name = request.args.get('signature_move_lvl_1_name', '')
        signature_move_lvl_1_beat_requirement = request.args.get('signature_move_lvl_1_beat_requirement', '')
        signature_move_lvl_1_effect = request.args.get('signature_move_lvl_1_effect', '')
        signature_move_lvl_2_name = request.args.get('signature_move_lvl_2_name', '')
        signature_move_lvl_2_beat_requirement = request.args.get('signature_move_lvl_2_beat_requirement', '')
        signature_move_lvl_2_effect = request.args.get('signature_move_lvl_2_effect', '')
        signature_move_lvl_3_name = request.args.get('signature_move_lvl_3_name', '')
        signature_move_lvl_3_beat_requirement = request.args.get('signature_move_lvl_3_beat_requirement', '')
        signature_move_lvl_3_effect = request.args.get('signature_move_lvl_3_effect', '')
        ooblet_image = request.args.get('ooblet_image', '')
        return updateOoblet(id, ooblet_name,  ooblet_description, ooblet_location, battle_requirements,signature_move_lvl_1_name,signature_move_lvl_1_beat_requirement,signature_move_lvl_1_effect,signature_move_lvl_2_name,signature_move_lvl_2_beat_requirement,signature_move_lvl_2_effect,signature_move_lvl_3_name,signature_move_lvl_3_beat_requirement,signature_move_lvl_3_effect,ooblet_image)

    elif request.method == 'DELETE':
        return deleteAOoblet(id)


@app.route('/oobletsApi/<string:ooblet_name>', methods=['GET','PUT'])
def oobletsFunctionName(ooblet_name):
    if request.method == 'GET':
        return get_ooblet_name(ooblet_name)





#-----------------------------------------------------------------------------------------

""" Endpoints for Characters """

@app.route('/')
@app.route('/charactersApi', methods=['GET', 'POST'])
def charactersFunction():
    if request.method == 'GET':
        return get_characters()
    elif request.method == 'POST':
        character_name = request.args.get('character_name', '')
        character_location = request.args.get('character_location', '')
        character_personality = request.args.get('character_personality', '')
        character_gender = request.args.get('character_gender', '')
        character_image = request.args.get('character_image', '')
        occupation = request.args.get('occupation', '')
        return makeANewCharacter(character_name, character_location, character_image, character_gender, character_personality, occupation)


@app.route('/charactersApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def charactersFunctionId(id):
    if request.method == 'GET':
        return get_character(id)

    elif request.method == 'PUT':
        character_name = request.args.get('character_name', '')
        character_location = request.args.get('character_location', '')
        character_personality = request.args.get('character_personality', '')
        character_gender = request.args.get('character_gender', '')
        character_image = request.args.get('character_image', '')
        occupation = request.args.get('occupation', '')
        return updateCharacter(id, character_name, character_location, character_image, character_gender, character_personality, occupation)

    elif request.method == 'DELETE':
        return deleteACharacter(id)

@app.route('/charactersApi/<string:character_name>', methods=['GET'])
def charactersFunctionName(character_name):
    if request.method == 'GET':
        return get_character_name(character_name)




#-----------------------------------------------------------------------------------------


""" Endpoints for Clothing """

@app.route('/')
@app.route('/clothingApi', methods=['GET', 'POST'])
def clothingFunction():
    if request.method == 'GET':
        return get_clothings()
    elif request.method == 'POST':
        clothing_name = request.args.get('clothing_name', '')
        clothing_category = request.args.get('clothing_category', '')
        clothing_price = request.args.get('clothing_price', '')
        kibbonbon_lvl = request.args.get('kibbonbon_lvl', '')
        clothing_location = request.args.get('clothing_location', '')
        clothing_image = request.args.get('clothing_image', '')
        return makeANewClothing(clothing_name, clothing_category, clothing_price, kibbonbon_lvl, clothing_location, clothing_image)


@app.route('/clothingApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def clothingFunctionId(id):
    if request.method == 'GET':
        return get_clothing(id)

    elif request.method == 'PUT':
        clothing_name = request.args.get('clothing_name', '')
        clothing_category = request.args.get('clothing_category', '')
        clothing_price = request.args.get('clothing_price', '')
        kibbonbon_lvl = request.args.get('kibbonbon_lvl', '')
        clothing_location = request.args.get('clothing_location', '')
        clothing_image = request.args.get('clothing_image', '')
        return updateClothing(id, clothing_name, clothing_category, clothing_price, kibbonbon_lvl, clothing_location, clothing_image)

    elif request.method == 'DELETE':
        return deleteAClothing(id)

@app.route('/clothingApi/<string:clothing_category>', methods=['GET'])
def clothingFunctionCategory(clothing_category):
    if request.method == 'GET':
        return get_clothing_category(clothing_category)

#-----------------------------------------------------------------------------------------

""" Endpoints for Housing """

@app.route('/')
@app.route('/housingApi', methods=['GET', 'POST'])
def housingFunction():
    if request.method == 'GET':
        return get_housing()
    elif request.method == 'POST':
        housing_name = request.args.get('housing_name', '')
        housing_category = request.args.get('housing_category', '')
        housing_price = request.args.get('housing_price', '')
        housing_location = request.args.get('housing_location', '')
        housing_image = request.args.get('housing_image', '')
        return makeANewHouse(housing_name, housing_category, housing_price, housing_location, housing_image)


@app.route('/housingApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def housingFunctionId(id):
    if request.method == 'GET':
        return get_house(id)

    elif request.method == 'PUT':
        housing_name = request.args.get('housing_name', '')
        housing_category = request.args.get('housing_category', '')
        housing_price = request.args.get('housing_price', '')
        housing_location = request.args.get('housing_location', '')
        housing_image = request.args.get('housing_image', '')
        return updateHouse(id, housing_name, housing_category, housing_price, housing_location, housing_image)

    elif request.method == 'DELETE':
        return deleteAHouse(id)



#-----------------------------------------------------------------------------------------

""" Endpoints for Badges """

@app.route('/')
@app.route('/badgesApi', methods=['GET', 'POST'])
def badgesFunction():
    if request.method == 'GET':
        return get_badges()
    elif request.method == 'POST':
        badge_image = request.args.get('badge_image', '')
        badge_reward = request.args.get('badge_reward', '')
        badge_category = request.args.get('badge_category', '')
        badge_task_description = request.args.get('badge_task_description', '')
        return makeANewBadge(badge_image, badge_reward, badge_category, badge_task_description)


@app.route('/badgesApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def badgesFunctionId(id):
    if request.method == 'GET':
        return get_badge(id)

    elif request.method == 'PUT':
        badge_image = request.args.get('badge_image', '')
        badge_reward = request.args.get('badge_reward', '')
        badge_category = request.args.get('badge_category', '')
        badge_task_description = request.args.get('badge_task_description', '')
        return updateBadge(id, badge_image, badge_reward, badge_category, badge_task_description)

    elif request.method == 'DELETE':
        return deleteABadge(id)

@app.route('/badgesApi/<string:badge_category>', methods=['GET'])
def badgeFunctionCategory(badge_category):
    if request.method == 'GET':
        return get_badge_category(badge_category)

#-----------------------------------------------------------------------------------------

""" Endpoints for Tools """

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
        tool_image = request.args.get('tool_image', '')
        tool_value = request.args.get('tool_value', '')
        return makeANewTool(tool_name, tool_description, tool_location, obtain_method, tool_image, tool_value)


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
        tool_image = request.args.get('tool_image', '')
        tool_value = request.args.get('tool_value', '')
        return updateTool(id, tool_name, tool_description, tool_location, obtain_method, tool_image, tool_value)

    elif request.method == 'DELETE':
        return deleteATool(id)

#-----------------------------------------------------------------------------------------

""" Endpoints for Crops """

@app.route('/')
@app.route('/cropsApi', methods=['GET', 'POST'])
def cropsFunction():
    if request.method == 'GET':
        return get_crops()
    elif request.method == 'POST':
        crop_name = request.args.get('crop_name', '')
        crop_location = request.args.get('crop_location', '')
        crop_image = request.args.get('crop_image', '')
        crop_seed_price = request.args.get('crop_seed_price', '')
        growing_time = request.args.get('growing_time', '')
        return makeANewCrop(crop_name, crop_location, crop_image, crop_seed_price,growing_time)


@app.route('/cropsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def cropsFunctionId(id):
    if request.method == 'GET':
        return get_crop(id)

    elif request.method == 'PUT':
        crop_name = request.args.get('crop_name', '')
        crop_location = request.args.get('crop_location', '')
        crop_image = request.args.get('crop_image', '')
        crop_seed_price = request.args.get('crop_seed_price', '')
        growing_time = request.args.get('growing_time', '')
        return updateCrop(id, crop_name, crop_location, crop_image, crop_seed_price,growing_time)

    elif request.method == 'DELETE':
        return deleteACrop(id)

@app.route('/cropsApi/<string:crop_name>', methods=['GET'])
def cropFunctionName(crop_name):
    if request.method == 'GET':
        return get_crop_name(crop_name)

#-----------------------------------------------------------------------------------------

""" Endpoints for Foods """

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
        food_image = request.args.get('food_image', '')
        food_value = request.args.get('food_value', '')
        food_energy = request.args.get('food_energy', '')
        return makeANewFood(food_name, food_Ingredient_1, food_Ingredient_2, food_Ingredient_3, food_Ingredient_4, food_Ingredient_5, food_image, food_value, food_energy)


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
        food_image = request.args.get('food_image', '')
        food_value = request.args.get('food_value', '')
        food_energy = request.args.get('food_energy', '')
        return updateFood(id, food_name, food_Ingredient_1, food_Ingredient_2, food_Ingredient_3, food_Ingredient_4, food_Ingredient_5, food_image, food_value, food_energy)

    elif request.method == 'DELETE':
        return deleteAFood(id)


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
   app.debug = False
   app.run()
