# API 文档

## 说明

API 设计使用RESTful风格，数据交互格式统一使用json，为保持API的请求是无状态的，不使用session或者cookie，采用http basic auth和token来进行认证



## API

- [获取token](#api1)
- [获取projects](#api2)
- [获取指定用户的projects](#api3)
- [获取指定用户的message](#api4)

## 资源格式
- [项目](#项目)
- [消息](#消息)


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


## 项目

### 项目状态
- 字段: status
- 类型: int
- 说明:

```
    0 => 已创建, 等待加人中
    1 => 人员已满, 未开始
    2 => 已向管理员申请开始, 未通过
    3 => 已通过,开始提交资料
```

### 项目名称

- 字段: name
- 类型: String
- 说明: 用户在创建输入项目的名称

### 关键字
- 字段: keyword
- 类型: Array<String>

### 创建者
- 字段: creator
- 类型: Object 
	- id: String 用户账号 
	- name: String 用户名称

### 简介
- 字段: introduction
- 类型: String

### 项目基础
- 字段: basic
- 类型: String
- 说明: 创建项目时用户说明对于该项目已经有的一些准备或者基础

### 希望的项目人数
- 字段: member_number
- 类型: Int 
- 说明: 最大人数

### 截止日期
- 字段: deadline
- 类型: timestamp
- 说明  见example

### 团队
- 字段: team
- 类型: Object
	- member: Array[Obejct] 普通成员
		- id: String 用户账号 
		- name: String 用户名称
	- change_person: Array[Obejct] 负责人
		- id: String 用户账号 
		- name: String 用户名称
	- mentor: Array[Obejct] 导师
		- id: String 用户账号 
		- name: String 用户名称
	- outside_mentor: Array[Obejct] 校外导师
		- id: String 用户账号 
		- name: String 用户名称

### 成员要求
- 字段: member_demand
- 类型: String

### 项目类型
- 字段: type
- 类型: Array<Int>
- 说明:

```
    0 => 国创
    1 => 上创
    2 => sitp
    3 => 挑战杯
    4 => 创新赛事
    5 => 企业课题
    6 => 创业项目
    7 => 其他
    
```

`Example`

	创建时

```json
{
    "status" : 0,
    "name" : "汽车能源分析",
    "keyword" : [ 
        "汽车", 
        "能源"
    ],
    "creator" : {
        "id" : "1352892",
        "name" : "谭靖儒"
    },
    "introduction" : "这是一个实验项目",
    "basic" : "目前还只是有想法, 还没有基础",
    "member_number" : 5,
    "deadline" : 1459777150914, 
    "team" : {
        "member" : [ 
            {
                "id" : "1352863",
                "name" : "张嘉琦"
            }
        ],
        "charge_person" : [ 
            {
                "id" : "1352892",
                "name" : "谭靖儒"
            }
        ],
        "mentor" : [ 
            {
                "id" : "1035423",
                "name" : "刘岩"
            }
        ],
        "outside_mentor" : []
    },
    "member_demand" : "要求了解基本汽车知识",
    "types" : [ 
        0, 
        1
    ]
}
```

	收到时
	
```json
	{
	  "status": 0,
	  "name": "汽车能源分析",
	  "keyword": [
	    "汽车",
	    "能源"
	  ],
	  "creator": {
	    "id": "1352892",
	    "name": "谭靖儒"
	  },
	  "introduction": "这是一个实验项目",
	  "basic": "目前还只是有想法, 还没有基础",
	  "member_number": 5,
	  "deadline": 1459777150,
	  "team": {
	    "member": [
	      {
	        "id": "1352863",
	        "name": "张嘉琦"
	      }
	    ],
	    "charge_person": [
	      {
	        "id": "1352892",
	        "name": "谭靖儒"
	      }
	    ],
	    "mentor": [
	      {
	        "id": "1035423",
	        "name": "刘岩"
	      }
	    ],
	    "outside_mentor": []
	  },
	  "created_time": 1459782397,
	  "member_demand": "要求了解基本汽车知识",
	  "_id": "570282fdc1f2b41f422e4716",
	  "types": [
	    0,
	    1
	  ]
	}
```

## 消息
- 字段: status
- 类型: Int
- 说明:

```
 0 => active
 1 => expire or handled

```

## 申请职位
- 字段: apply_role
- 类型: Int
- 说明

```
	0 => 成员
	1 => 负责人
	2 => 导师
	3 => 校外导师
	
```
## 申请理由
- 字段: apply_reason
- 类型: String
- 说明

## 项目
- 字段: project
- 类型: Obejct
	- id: String 项目id
	- name: String 项目名称
- 说明 

## 发送者
- 字段: sender
- 类型: Obejct
	- id: String 用户账号
	- name: String 用户姓名
- 说明 

## 接受者
- 字段: receiver
- 类型: String
- 说明: 指用户的账号

## 类型
- 字段: type
- 类型: Int
- 说明

```
 0 => 有人想要加入项目
 1 => 消息回复
 
```

## 内容
- 字段: content
- 类型: String
- 说明: 比如 `张三想加入你的项目`


`Example`

```json

{
    "status" : 0,
    "apply_role" : 0,
    "apply_reason" : "我很擅长汽车相关的研究",
    "project" : {
        "name" : "汽车能源研究",
        "id" : "56fb1fb6c1f2b4030e72dc0a"
    },
    "sender" : {
        "name" : "张嘉琦",
        "id" : "1352863"
    },
    "receiver" : "1352892",
    "type" : 0,
    "content" : "张嘉琦想要加入你的项目"
}

```




