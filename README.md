# Ooblets-Restful-API
## Introduction

## Base URL
```bash
https://ooblets-api.herokuapp.com
```

## Register a User

## Authentication

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
