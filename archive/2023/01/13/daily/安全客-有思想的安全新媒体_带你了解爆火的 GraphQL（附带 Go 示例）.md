---
title: 带你了解爆火的 GraphQL（附带 Go 示例）
url: https://www.anquanke.com/post/id/285397
source: 安全客-有思想的安全新媒体
date: 2023-01-13
fetch_date: 2025-10-04T03:42:47.354835
---

# 带你了解爆火的 GraphQL（附带 Go 示例）

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 带你了解爆火的 GraphQL（附带 Go 示例）

阅读量**333288**

发布时间 : 2023-01-12 16:30:30

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 背景

2022 年 11 月正式掌管 Twitter 的马斯克发推批判 Twitter 开发团队：Twitter 因批量执行 RPC 调用，导致非美国地区的用户访问延迟较高。

![]()

随后，Twitter 员工对其进行反击，要求马斯克学习 GraphQL 的工作原理。

![]()

> 新闻源地址：https://view.inews.qq.com/a/20221114A041F400

那么，究竟孰是孰非？下面是作者整理的架构图。

![]()

可见，在公网上，用户只向 GraphQL 服务发送 1 个请求。在内部网络中，GraphQL 服务批量地执行 N 个 RPC（或 HTTP）请求。并非马斯克所描述的那样，用户通过公网批量地向推特的服务发送 N 个 RPC 请求。那么 GraphQL 是什么呢？

## GraphQL

GraphQL 既是一种用于 API 的查询语言，也是一个满足你数据查询的运行时。GraphQL 对你的 API 中的数据提供一套易于理解的完整描述，使得客户端能够准确地获得它需要的数据，而且没有任何冗余，也让 API 更容易地随着时间推移而演进，还能用于构建强大的开发者工具。

1. **请求你所要的数据不多不少**

向你的 API 发出一个 GraphQL 请求就能准确获得你想要的数据，不多不少。GraphQL 查询总是返回可预测的结果。使用 GraphQL 的应用可以工作得又快又稳，因为控制数据的是应用，而不是服务器。

1. **获取多个资源只用一个请求**

GraphQL 查询不仅能够获得资源的属性，还能沿着资源间引用进一步查询。典型的 REST API 请求多个资源时得载入多个 URL，而 GraphQL 可以通过一次请求就获取你应用所需的所有数据。这样一来，即使是比较慢的移动网络连接下，使用 GraphQL 的应用也能表现得足够迅速。

1. **描述所有的可能类型系统**

GraphQL API 基于类型和字段的方式进行组织，而非入口端点。你可以通过一个单一入口端点得到你所有的数据能力。GraphQL 使用类型来保证应用只请求可能的数据，还提供清晰的辅助性错误信息。应用可以使用类型，而避免编写手动解析代码。

1. **快步前进，强大的开发者工具**

不用离开编辑器就能准确知道你可以从 API 中请求的数据，发送查询之前就能高亮潜在问题，高级代码智能提示。利用 API 的类型系统，GraphQL 让你可以更简单地构建如同 GraphiQL （https://github.com/graphql/graphiql）的强大工具。

1. **API 演进无需划分版本**

给你的 GraphQL API 添加字段和类型而无需影响现有查询。老旧的字段可以废弃，从工具中隐藏。通过使用单一演进版本，GraphQL API 使得应用始终能够使用新的特性，并鼓励使用更加简洁、更好维护的服务端代码。

1. **使用你现有的数据和代码**

GraphQL 让你的整个应用共享一套 API，而不用被限制于特定存储引擎。GraphQL 引擎已经有多种语言实现，通过 GraphQL API 能够更好利用你的现有数据和代码。你只需要为类型系统的字段编写函数，GraphQL 就能通过优化并发的方式来调用它们。

> 以上内容来自于：https://graphql.cn/。

GraphQL 的中文入门文档，请参阅 https://graphql.cn/learn/；

英文入门文档，请参阅 https://graphql.org/learn/。

可见，GraphQL 可以充当客户端和现有系统之间的接口，能够很方便地集成现有系统。

![]()

## Go GraphQL 快速入门

关于各种编程语言的 GraphQL 实现，请参阅官方网站（https://graphql.org/code/）。接下来我们看一个 Go graphql-go/graphql （https://github.com/graphql-go/graphql）示例。

### **环境说明**

1. 操作系统：macOS 12.6
2. Go：go version go1.19 darwin/amd64

### **创建测试项目**

mkdir graphql-demo

cd graphql-demo

go mod init graphql-demo

go get github.com/graphql-go/graphql

### **项目结构**

% tree .

.

├── go.mod

├── go.sum

├── gql\_type

│ ├── mutation\_type.go

│ ├── post.go

│ ├── post\_type.go

│ ├── query\_type.go

│ ├── user.go

│ └── user\_type.go

├── main.go

└── schema.gql

1 directory, 10 files

go.mod：

module graphql-demo

go 1.19

require github.com/graphql-go/graphql v0.8.0

gql\_type/mutation\_type.go：

package gql\_type

import (

“github.com/graphql-go/graphql”

“strconv”

)

var MutationType = graphql.NewObject(graphql.ObjectConfig{

Name: “Mutation”,

Fields: graphql.Fields{

“createUser”: &graphql.Field{

Type: UserType,

Args: graphql.FieldConfigArgument{

“email”: &graphql.ArgumentConfig{

Description: “New User Email”,

Type: graphql.NewNonNull(graphql.String),

},

},

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

email := p.Args[“email”].(string)

user := &User{

Email: email,

}

InsertUser(user)

return user, nil

},

},

“removeUser”: &graphql.Field{

Type: graphql.Boolean,

Args: graphql.FieldConfigArgument{

“id”: &graphql.ArgumentConfig{

Description: “User ID to remove”,

Type: graphql.NewNonNull(graphql.ID),

},

},

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

i := p.Args[“id”].(string)

id, err := strconv.Atoi(i)

if err != nil {

return nil, err

}

RemoveUserByID(id)

return true, nil

},

},

“createPost”: &graphql.Field{

Type: PostType,

Args: graphql.FieldConfigArgument{

“user”: &graphql.ArgumentConfig{

Description: “Id of user creating the new post”,

Type: graphql.NewNonNull(graphql.ID),

},

“title”: &graphql.ArgumentConfig{

Description: “New post title”,

Type: graphql.NewNonNull(graphql.String),

},

“body”: &graphql.ArgumentConfig{

Description: “New post body”,

Type: graphql.NewNonNull(graphql.String),

},

},

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

i := p.Args[“user”].(string)

userID, err := strconv.Atoi(i)

if err != nil {

return nil, err

}

title := p.Args[“title”].(string)

body := p.Args[“body”].(string)

post := &Post{

UserID: userID,

Title: title,

Body: body,

}

InsertPost(post)

return post, nil

},

},

“removePost”: &graphql.Field{

Type: graphql.Boolean,

Args: graphql.FieldConfigArgument{

“id”: &graphql.ArgumentConfig{

Description: “Post ID to remove”,

Type: graphql.NewNonNull(graphql.ID),

},

},

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

i := p.Args[“id”].(string)

id, err := strconv.Atoi(i)

if err != nil {

return nil, err

}

RemovePostByID(id)

return true, err

},

},

},

})

gql\_type/post.go：

package gql\_type

import (

“errors”

“sync”

)

type Post struct {

ID int

UserID int

Title string

Body string

}

var postMtx sync.RWMutex

var posts = make(map[int]\*Post)

var postID = 0

func InsertPost(post \*Post) {

postMtx.Lock()

defer postMtx.Unlock()

postID += 1

post.ID = postID

posts[post.ID] = post

}

func RemovePostByID(id int) {

postMtx.Lock()

defer postMtx.Unlock()

delete(posts, id)

}

func GetPostByID(id int) (\*Post, error) {

postMtx.RLock()

defer postMtx.RUnlock()

post, found := posts[id]

if !found {

return nil, errors.New(“not found”)

}

return post, nil

}

func GetPostsForUser(userID int) []\*Post {

postMtx.RLock()

defer postMtx.RUnlock()

var res []\*Post

for \_, v := range posts {

if v.UserID == userID {

res = append(res, v)

}

}

return res

}

gql\_type/post\_type.go：

package gql\_type

import (

“github.com/graphql-go/graphql”

)

var PostType = graphql.NewObject(graphql.ObjectConfig{

Name: “Post”,

Fields: graphql.Fields{

“id”: &graphql.Field{

Type: graphql.NewNonNull(graphql.ID),

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

if post, ok := p.Source.(\*Post); ok {

return post.ID, nil

}

return nil, nil

},

},

“title”: &graphql.Field{

Type: graphql.NewNonNull(graphql.String),

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

if post, ok := p.Source.(\*Post); ok {

return post.Title, nil

}

return nil, nil

},

},

“body”: &graphql.Field{

Type: graphql.NewNonNull(graphql.ID),

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

if post, ok := p.Source.(\*Post); ok {

return post.Body, nil

}

return nil, nil

},

},

},

})

func init() {

PostType.AddFieldConfig(“user”, &graphql.Field{

Type: graphql.NewNonNull(UserType),

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

if post, ok := p.Source.(\*Post); ok {

return GetUserByID(post.UserID)

}

return nil, nil

},

})

}

gql\_type/query\_type.go：

package gql\_type

import (

“github.com/graphql-go/graphql”

“strconv”

)

var QueryType = graphql.NewObject(graphql.ObjectConfig{

Name: “Query”,

Fields: graphql.Fields{

“user”: &graphql.Field{

Type: UserType,

Args: graphql.FieldConfigArgument{

“id”: &graphql.ArgumentConfig{

Description: “User ID”,

Type: graphql.NewNonNull(graphql.ID),

},

},

Resolve: func(p graphql.ResolveParams) (interface{}, error) {

i := p.Args[“id”].(string)

id, err := strconv.Atoi(i)

if err != nil {

return nil, err

}

return GetUserByID(id)

},

},

},

})

gql\_type/user.go：

package gql\_type

import (

“errors”

“sync”

)

type User struct {

ID int

Email string

}

var userMtx sync.RWMutex

var users = make(map[int]\*User)

var userID = 0

func InsertUser(user \*User) {

userMtx.Lock()

defer userMtx.Unlock()

userID += 1

user.ID = userID

users[user.ID] = user

}

func RemoveUserByID(id int) {

userMtx.Lock()

defer userMtx.Unlock()

delete(users, id)

}

func GetUserByID(id int) (\*User, error) {

userMtx.RLock()

defer userMtx.RUnlock()

user, found := users[id]

if !found {

return nil, errors.New(“not found”)

}

return user,...