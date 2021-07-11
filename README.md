# Ooblets-Restful-API
## Introduction

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

## Authentication

**AUTHENTICATE a User**

This endpoint authenticates a user and gives a jwt token.

HTTP Request

```bash
https://ooblets-api.herokuapp.com/auth
```

## Ooblets
**GET all Ooblets**

This endpoint retrieves all ooblets.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi
```

**GET a Specific Ooblet**

This endpoint retrieves a specific ooblet.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the ooblet to delete |


**DELETE a Specific Ooblet**

This endpoint deletes a specific ooblet.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/oobletsApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the ooblet to delete |

## Characters
**GET all Characters**

This endpoint retrieves all characters.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/charactersApi
```

**GET a Specific Character**

This endpoint retrieves a specific character.

HTTP Request
```bash
https://ooblets-api.herokuapp.com/charactersApi/<id>
```

URL Parameters

| Parameter |  	Description |
| ------------- | ------------- |
| id | The id of the character to delete |


**DELETE a Specific Character**

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

## Tools

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
