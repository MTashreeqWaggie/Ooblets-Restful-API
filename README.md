# Ooblets-Restful-API
![image](https://ooblets.com/images/Metatag_image.jpg)

## Introduction
This is a SIMPLE RESTful API created based on the game name Ooblets. Why? I was curious on how api's work and tried creating one of my own based on game I enjoy playing.

## Base URL
```bash
https://ooblets-api.herokuapp.com
```
## Register a User

### Request

`POST /register`

     https://ooblets-api.herokuapp.com/register

     Body: raw - JSON
     
     {
         "username": "joe",
         "password": "asdf"
     }

### Response

    HTTP/1.1 201 CREATED
    Status: 201 CREATED
    Content-Type: application/json

    {
      "message": "User created successfully."
    }

## Authentication

### Request

`POST /auth`

     https://ooblets-api.herokuapp.com/auth

     Headers: 
     Key: Content-Type
     Value: application/json
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json

    {
              "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjgzNTk1NTksImlhdCI6MTYyODM1OTI1OSwibmJmIjoxNjI4MzU5MjU5LCJpZGVudGl0eSI6MX0.rqKtub_R_WFOtUpcA1X3NxGur_jxckaMpOO3DhPAhJM"
    }
    
## Get all Ooblets

### Request

`GET /oobletsApi`

     https://ooblets-api.herokuapp.com/oobletsApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON

    "ooblets": [
        {
            "battle_requirements": "1x Frunbuns Hunbun",
            "description": "Tuds are the semi-aquatic mascot ooblets of the Frunbuns club. They are good at being supportive members of a dance troupe. Wild tuds can only be lured into dances with exclusive Frunbuns treabies.",
            "id": 1,
            "location": "Club selection",
            "name": "Tud",
            "ooblet_image": "https://oyster.ignimgs.com/mediawiki/apis.ign.com/ooblets/b/be/Tud.png?width=640",
            "signature_move_lvl_1_beat_requirement": 1,
            "signature_move_lvl_1_effect": "Gain one hype.",
            "signature_move_lvl_1_name": "Glaze Glide",
            "signature_move_lvl_2_beat_requirement": 0,
            "signature_move_lvl_2_effect": "Gain 1 point each time a move is played during this hand. ",
            "signature_move_lvl_2_name": "Tadpolka ",
            "signature_move_lvl_3_beat_requirement": 3,
            "signature_move_lvl_3_effect": "Gain 4 hype.",
            "signature_move_lvl_3_name": "Hype Tram Jam"
        }, ...
       
       ]
        
## Get Ooblet by ID

### Request

`GET /oobletsApi/<int:id>`
`GET /oobletsApi/7`

     https://ooblets-api.herokuapp.com/oobletsApi/7
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
     "ooblets": {
             "battle_requirements": "1x Quib ",
             "description": "Bristlebuds resemble cute little cacti wearing shorts. Despite their prickly exterior, these ooblets make a solid companion with their solid debuffs. ",
             "id": 7,
             "location": "Mamoonia",
             "name": "Bristlebud",
             "ooblet_image": "https://oyster.ignimgs.com/mediawiki/apis.ign.com/ooblets/5/5b/Bristlebud.png?width=640",
             "signature_move_lvl_1_beat_requirement": 2,
             "signature_move_lvl_1_effect": "Stun target for 2 turns.",
             "signature_move_lvl_1_name": "Prickle Prance",
             "signature_move_lvl_2_beat_requirement": 2,
             "signature_move_lvl_2_effect": "Add three fluster to enemies.",
             "signature_move_lvl_2_name": "Spiny Spin",
             "signature_move_lvl_3_beat_requirement": 4,
             "signature_move_lvl_3_effect": "Increase cost of enemy moves by 2 beats during their next turn .",
             "signature_move_lvl_3_name": "Stompulent "
         }

## Get Ooblet by LOCATION

### Request

`GET /oobletsApi/<string:location>`
`GET /oobletsApi/Mamoonia`
`GET /oobletsApi/Badgetown`

     https://ooblets-api.herokuapp.com/oobletsApi/Mamoonia
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "ooblets": [
        {
            "battle_requirements": "1x Quib ",
            "description": "Bristlebuds resemble cute little cacti wearing shorts. Despite their prickly exterior, these ooblets make a solid companion with their solid debuffs. ",
            "id": 7,
            "location": "Mamoonia",
            "name": "Bristlebud",
            "ooblet_image": "https://oyster.ignimgs.com/mediawiki/apis.ign.com/ooblets/5/5b/Bristlebud.png?width=640",
            "signature_move_lvl_1_beat_requirement": 2,
            "signature_move_lvl_1_effect": "Stun target for 2 turns.",
            "signature_move_lvl_1_name": "Prickle Prance",
            "signature_move_lvl_2_beat_requirement": 2,
            "signature_move_lvl_2_effect": "Add three fluster to enemies.",
            "signature_move_lvl_2_name": "Spiny Spin",
            "signature_move_lvl_3_beat_requirement": 4,
            "signature_move_lvl_3_effect": "Increase cost of enemy moves by 2 beats during their next turn .",
            "signature_move_lvl_3_name": "Stompulent "
        }, ...
        
       ]

## Get all Characters

### Request

`GET /charactersApi`

     https://ooblets-api.herokuapp.com/charactersApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "characters": [
        {
            "character_image": "/static/images/Arah.png",
            "character_location": "Badgetown",
            "character_name": "Arah",
            "gender": "Female",
            "id": 1,
            "occupation": "Operates the Printypress. ",
            "personality": "Arah is a spunky sort of person who marches to the tune of her own drum. She has a very modern dialect, and is generally kind to everyone that she meets. She is particularly fixated on a more dark academia way of life, enjoying activities such as creating potions and spells alongside summoning the occult. "
        }

## Get Characters by ID

### Request

`GET /charactersApi/<int:id>`
`GET /charactersApi/3`

     https://ooblets-api.herokuapp.com/charactersApi/3
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "characters": {
             "character_image": "/static/images/Churles.png",
             "character_location": "Badgetown",
             "character_name": "Churles",
             "gender": "Male",
             "id": 3,
             "occupation": "Runs Kibbonbon . ",
             "personality": "Initially, Churles presents himself as a hypochondriac and germaphobe - he doesn't appreciate it when his personal space is encroached upon, and he makes it abundantly clear that he doesn't like to shake peoples hands. Because of this, he lives a rather isolated lifestyle. "
         }
    
## Get all Clothing

### Request

`GET /clothingApi`

     https://ooblets-api.herokuapp.com/clothingApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "clothing": [
             {
                 "category": "Shirts",
                 "clothing_image": "/static/images/Argyle_Sweater.png",
                 "clothing_location": "Kibbonbon",
                 "clothing_name": "Argyle Sweater",
                 "clothing_price": "50 Gummies",
                 "id": 1,
                 "kibbonbon_lvl": 1
             }, ...
         ]
                
## Get Clothing by ID

### Request

`GET /clothingApi/<int:id>`
`GET /clothingApi/5`

     https://ooblets-api.herokuapp.com/clothingApi/5
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "clothing": {
             "category": "Shirts",
             "clothing_image": "/static/images/Boombox_Sweater.png",
             "clothing_location": "Kibbonbon",
             "clothing_name": "Boombox Sweater",
             "clothing_price": 50,
             "id": 5,
             "kibbonbon_lvl": 1
          }
          
## Get all Badges

### Request

`GET /badgesApi`

     https://ooblets-api.herokuapp.com/badgesApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "badges": [
             {
                 "badge_category": "Helping",
                 "badge_image": "/static/images/Helping_Badge_1.png",
                 "badge_reward": "60 Wishies",
                 "badge_task_description": "Complete 5 Tinstle Tasks.",
                 "id": 1
             }, ...
         ]

## Get Badges by ID

### Request

`GET /badgesApi/<int:id>`
`GET /badgesApi/4`

     https://ooblets-api.herokuapp.com/badgesApi/4
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "badges": {
             "badge_category": "Oobleting",
             "badge_image": "/static/images/Oobleting_Badge_2.png",
             "badge_reward": "80 Wishies",
             "badge_task_description": "Scan 10 Ooblets at the Lernery.",
             "id": 4
         }
         
## Get all Tools

### Request

`GET /toolsApi`

     https://ooblets-api.herokuapp.com/toolsApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "Tools": [
             {
                 "id": 1,
                 "obtain_method": "Meed will give the player a Dirt Scraper.",
                 "tool_description": "Dirt Scraper is a tool that a player used to create plots for crops to grow.",
                 "tool_image": "/static/images/Dirt_Scraper.png",
                 "tool_location": "Badgetown",
                 "tool_name": "Dirt Scraper",
                 "tool_value": 20
             }, ...
         ]


## Get Tools by ID

### Request

`GET /toolsApi/<int:id>`
`GET /toolsApi/1`

     https://ooblets-api.herokuapp.com/toolsApi/1
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "tools": {
             "id": 1,
             "obtain_method": "Meed will give the player a Dirt Scraper.",
             "tool_description": "Dirt Scraper is a tool that a player used to create plots for crops to grow.",
             "tool_image": "/static/images/Dirt_Scraper.png",
             "tool_location": "Badgetown",
             "tool_name": "Dirt Scraper",
             "tool_value": 20
         }
         
## Get all Crops

### Request

`GET /cropsApi`

     https://ooblets-api.herokuapp.com/cropsApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "crops": [
             {
                 "crop_image": "/static/images/Caroot_Seeds.png",
                 "crop_location": "Badgetown",
                 "crop_name": "Caroot",
                 "crop_seed_price": 5,
                 "growing_time": 1.5,
                 "id": 1
             }, ...
         ]
         
## Get Crops by ID

### Request

`GET /cropsApi/<int:id>`
`GET /cropsApi/4`

     https://ooblets-api.herokuapp.com/cropsApi/4
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "crops": {
             "crop_image": "/static/images/Springbean_Seeds.png",
             "crop_location": "Badgetown",
             "crop_name": "Springbeans",
             "crop_seed_price": 6,
             "growing_time": 5,
             "id": 4
         }
      
## Get all Foods

### Request

`GET /foodsApi`

     https://ooblets-api.herokuapp.com/foodsApi
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "foods": [
             {
                 "food_Ingredient_1": "1x sweetiebeetie",
                 "food_Ingredient_2": "1x sporbet",
                 "food_Ingredient_3": "1x shelbo. ",
                 "food_Ingredient_4": "",
                 "food_Ingredient_5": "",
                 "food_energy": 30,
                 "food_image": "/static/images/Clambrosia.png",
                 "food_name": "Clambrosia",
                 "food_value": 20,
                 "id": 1
             }, ...
        ]
 
## Get Foods by ID

### Request

`GET /foodsApi/<int:id>`
`GET /foodsApi/9`

     https://ooblets-api.herokuapp.com/foodsApi/9
     

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: JSON
    
        "foods": {
             "food_Ingredient_1": "3x Zinooka",
             "food_Ingredient_2": "3x Muz Flour. ",
             "food_Ingredient_3": "3x Flooti sauce",
             "food_Ingredient_4": "3x Quib",
             "food_Ingredient_5": "3x Froobtose",
             "food_energy": 150,
             "food_image": "/static/images/Zinooka_Cake.png",
             "food_name": "Zinooka Cake",
             "food_value": 200,
             "id": 9
         }
        
