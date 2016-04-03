# API 文档

## 内容

- [获取token](#api1)
- [获取projects](#api2)


<h2 id="api1">获取token</h2>

### URL
	
`/token`

### Method
	
POST

### Description

生成一个token

### URL Params
	
- Required
	- http basic auth
		  - username
		  - password
		
### Data Params

None
	
### Success Response
	
- Status Code: 200 
- Content-Type: `application/json; charset=utf-8`
	  
	
#### body example

```json
{
  "data": {
    "duration": 600,
    "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1OTY3MzMyNCwiaWF0IjoxNDU5NjcyNzI0fQ.eyJpZCI6NjAwfQ.4VEW6OI1Bi8kusdQ4erISA6vwXiI5Jss665PXOzZX7U"
  }
}
```


### Error Response
	
- Status Code: 401 UNAUTHORIZED


<h2 id="api2">获取projects</h2>

### URL
	
`/projects`

### Method
	
GET

### Description

得到所有的project

### URL Params
	
- Required
	- http basic auth
		  - username
		  - password
	- token
	     - token
	     - `anything`
		
### Data Params

None
	
### Success Response
	
- Status Code: 200 
- Content-Type: `application/json; charset=utf-8`
	  
	
#### body example

```json
{
  "data": [<project json format>,]
}
```


### Error Response
	
- Status Code: 401 UNAUTHORIZED
- Status Code: 405 METHOD NOT ALLOW



<h2 id="api3">根据指定用户的project</h2>

### URL
	
`/user/<username>/projects`

### Method
	
GET

### Description

得到指定用户project

### URL Params
	
- Required
	- http basic auth
		  - username
		  - password
	- token
	     - token
	     - `anything`
		
### Data Params

None
	
### Success Response
	
- Status Code: 200 
- Content-Type: `application/json; charset=utf-8`
	  
	
#### body example


```json
{
  "data": [<project json format>,]
}
```



### Error Response
	
- Status Code: 401 UNAUTHORIZED
- Status Code: 405 METHOD NOT ALLOW


<h2 id="api4">根据指定用户的message</h2>

### URL
	
`/user/<username>/messages`

### Method
	
GET

### Description

得到指定用户message

### URL Params
	
- Required
	- http basic auth
		  - username
		  - password
	- token
	     - token
	     - `anything`
		
### Data Params

None
	
### Success Response
	
- Status Code: 200 
- Content-Type: `application/json; charset=utf-8`
	  
	
#### body example


```json
{
  "data": [<message json format>,]
}
```


### Error Response
	
- Status Code: 401 UNAUTHORIZED
- Status Code: 405 METHOD NOT ALLOW