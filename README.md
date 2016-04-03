# API 文档

## 获取token

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

