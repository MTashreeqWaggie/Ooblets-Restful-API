# Ooblets-Restful-API
![image](https://ooblets.com/images/Metatag_image.jpg)

## Introduction
This is a RESTful API created based on the game name Ooblets. Why? I was curious on how api's work and tried creating one of my own.

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
    
    
