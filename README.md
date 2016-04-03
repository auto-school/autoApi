# API 文档

## 说明

API 设计使用RESTful风格，数据交互格式统一使用json，为保持API的请求是无状态的，不使用session或者cookie，采用http basic auth和token来进行认证



## API

- [获取token](#api1)
- [获取projects](#api2)
- [获取指定用户的projects](#api3)
- [获取指定用户的message](#api4)


<h2 id="api1">获取token</h2>

### URL
	
`/token`

### Method
	
POST

### Description

生成一个token

### URL Params
	
- Required
	- Content-Type `application/json;`
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
	- Content-Type `application/json;`
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



<h2 id="api3">获得指定用户的project</h2>

### URL
	
`/user/<username>/projects`

### Method
	
GET

### Description

得到指定用户project

### URL Params
	
- Required
   - Content-Type `application/json;`
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


<h2 id="api4">获得指定用户的message</h2>

### URL
	
`/user/<username>/messages`

### Method
	
GET

### Description

得到指定用户message

### URL Params
	
- Required
	- Content-Type `application/json;`
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