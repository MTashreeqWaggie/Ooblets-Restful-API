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
