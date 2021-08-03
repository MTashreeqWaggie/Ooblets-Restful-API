# Ooblets-Restful-API
![image](https://ooblets.com/images/Metatag_image.jpg)

## Introduction
This is a RESTful API created based on the game name Ooblets. Why? I was curious on how api's work and tried creating one of my own.

## NB!
Gifs still have be added to show users how to make use of endpoints in **postman**. 

## Base URL
```bash
https://ooblets-api.herokuapp.com
```

## Register

**REGISTER a User**

This endpoint registers a user.

HTTP Request

```bash
https://ooblets-api.herokuapp.com/register
```

![Image](https://github.com/MTashreeqWaggie/Ooblets-Restful-API/blob/main/screenshots/Register.PNG)

## Authentication

**AUTHENTICATE a User**

This endpoint authenticates a user and gives a jwt token.

HTTP Request

```bash
https://ooblets-api.herokuapp.com/auth
```

![Image](https://github.com/MTashreeqWaggie/Ooblets-Restful-API/blob/main/screenshots/Authentication.PNG)

## Ooblets
**GET all Ooblets**

This endpoint retrieves all ooblets.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi
```

**GET a Specific Ooblet** (JWT Token needed.)

This endpoint retrieves a specific ooblet.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the ooblet to delete |


**DELETE a Specific Ooblet** (JWT Token needed.)

This endpoint deletes a specific ooblet.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the ooblet to delete |

![Image](https://github.com/MTashreeqWaggie/Ooblets-Restful-API/blob/main/screenshots/Authentication.PNG)

## Characters
**GET all Characters**

This endpoint retrieves all characters.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/charactersApi
```

**GET a Specific Character** (JWT Token needed.)

This endpoint retrieves a specific character.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/charactersApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the character to delete |


**DELETE a Specific Character** (JWT Token needed.)

This endpoint deletes a specific character.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/charactersApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the character to delete |

## Crops
**GET all Crops** 

This endpoint retrieves all crops.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/cropsApi
```

**GET a Specific Crop** (JWT Token needed.)

This endpoint retrieves a specific crop.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/cropsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the crop to delete |


**DELETE a Specific Crop** (JWT Token needed.)

This endpoint deletes a specific crop.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/cropsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the crop to delete |

## Tools

**GET all Tools**

This endpoint retrieves all tools.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/toolsApi
```

**GET a Specific Tool** (JWT Token needed.)

This endpoint retrieves a specific tool.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/toolsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the tool to delete |


**DELETE a Specific Tool** (JWT Token needed.)

This endpoint deletes a specific tool.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/toolsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the tool to delete |

## Errors

The Ooblets API uses the following error codes:

| Error Code |  	 	Meaning |
| ------------- | ------------- |
| 400 | Bad Request -- Your request is invalid. |
| 401 | Unauthorized -- Your not using a JWT token. |
| 404 |  	Not Found -- The specified Ooblet could not be found. |
| 410 | Gone -- The ooblet requested has been removed from our servers. |
| 500 |  	Internal Server Error -- We had a problem with our server. Try again later. |
| 503 |  	Service Unavailable -- We're temporarily offline for maintenance. Please try again later. |
