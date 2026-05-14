---
title: 【项目实战】|从 /graphql 到未授权：另一种Swagger测试思路
url: https://mp.weixin.qq.com/s/kCV7-wwdhhpRnBwdgDbS1w
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:13.214326
---

# 【项目实战】|从 /graphql 到未授权：另一种Swagger测试思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwTEOaaRw7V1g8RUDEpEUwV9jnV6jxvfpbU5Sq6Ons7lvV6DCD3UZ9DW46eOfiadNPFLsXiaFbPzCtcTYp7sTibh29LGJeOfCHgy9s/0?wx_fmt=jpeg)

# 【项目实战】|从 /graphql 到未授权：另一种Swagger测试思路

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于隐雾安全
，作者隐雾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

📝 **编者语**

很多人在做接口测试时，第一反应是：

找**Swagger**文档

但在实际项目中，越来越多的系统开始使用：

* GraphQL
* 内置调试面板（console / playground）

这些东西，本质上就是：

**另一种“接口文档”**

这篇文章，我们用一个真实案例，走一遍：

**从一个功能点 → 找到 GraphQL → 拿到接口结构 → 发现未授权接口**

1

GraphQL 和 Swagger 是什么关系？

很多人会把这两个当成完全不同的东西，其实可以这样理解：

🔹 **Swagger（传统接口文档）**

提前写好接口说明：

* URL
* 参数
* 返回

🔹 **GraphQL（动态接口文档）**

接口是“自描述”的：

* 可以查询接口结构
* 可以动态拼请求
* 可以直接调试

***🧠 核心区别***

|  |  |
| --- | --- |
| **类型** | **特点** |
| Swagger | 静态文档 |
| GraphQL | 可查询的接口结构 |

所以在挖洞时：

**GraphQL = 自带“接口枚举能力”的文档系统**

2

实战案例（500）

***第一步：发现入口***

🔍 起点：一个普通功能点

在测试过程中，点到了一个功能：

删除地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4mlR36rRDwMVEhibUGuZ3xSEmFC0oiaOuBmSibYXDHO8fRzIX7iaZ0cian9KbCCTUqkzRobhteH57rfQKuS71EerhYSOVf2aM69m198/640?wx_fmt=png&from=appmsg)

顺手做了一件事

看目录结构

发现一个路径：

/graphql

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4n60JbsS6TKsBYpzVVRSNDU1HbcDVN9cbGYe8VUcuXCvsTfn7OYwe2SlXNpL8uIVM3771VRwVxVdphkwRcKic9pyAZD0Hs6JPg8/640?wx_fmt=png&from=appmsg)

⚠️ 这个路径意味着什么？

在经验里：

出现 /graphql，基本可以判断：

* 存在 GraphQL 服务
* 可能有调试接口
* 很可能存在接口暴露

***第二步：探测 GraphQL 是否可用***

接下来就是一个标准动作：

发一个 introspection 查询

📦 请求数据（核心）

```
{"query":"query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4n75oZBQ081nRFDJj9gicgDsTwFoiaNqQQDZNribj7CwRiaGBg5ZZKraSHKqibnzkxMX9B5awP2EZXj3dInes5eGUV9xeSqt0y9jE1U/640?wx_fmt=png&from=appmsg)

🔍 返回结果

如果返回结构信息，比如：

* type
* query
* mutation

👉 就说明：

**GraphQL introspection 开启了**

📌 这一步的意义

👉 相当于：

**拿到了整个接口结构**

***第三步：目录扫描***

对 /graphql 目录进行扫描

🔎 扫描结果

发现多个接口：

/api/graphql/console

/api/graphql/graphql

/api/graphql/graphql-playground

/api/graphql/v1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4m6BJvgXMKWtHIlTpoSaiaQHPGrT8FTmLyvkPo24LLqmaTPmagAdibj9j9esgCXPh8iaS4VYlwGdYbK4ticQL3TKDqbE1EFIzeU0Dk/640?wx_fmt=png&from=appmsg)

⚠️ 这些路径意味着什么？

逐个解释👇

路径

作用

console    调试控制台

playground    图形化测试工具

graphql    主接口

v1    版本接口

👉 重点来了：

这些“调试接口”，很多情况下是没有鉴权的

***第四步：直接打 console***

选择了一个最典型的接口：

POST /api/graphql/console

📦 请求内容

```
POST /api/graphql/console HTTP/2 {"query":"query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4lFX6pengvMtaJMm9vlNLg3Dm6zAo0SejajJfzTfU5Cz6Q8anvyOQJic1EECDfpxQqq057bs7k4lWzKwbxup6NKxVkSv6gbk1xQ/640?wx_fmt=png&from=appmsg)

🔍 返回结果

成功返回接口结构数据。

⚠️ 这个时候其实已经可以确认：

👉 存在未授权访问

3

总结漏洞本质

如果总结一下，其实是三层问题叠加：

🧩 问题拆解

**1️⃣ GraphQL introspection 未关闭**

👉 可以直接获取接口结构

**2️⃣ 调试接口暴露**

👉 console/playground 对外开放

**3️⃣ 未做鉴权**

👉 任何人都可以访问

📌 最终效果

👉 外部用户可以：

* 枚举接口
* 构造请求
* 直接调用

***整个挖掘流程***

🧭 挖洞流程

功能点（删除地址）

       ↓

发现 /graphql

       ↓

发送 introspection 查询

       ↓

确认 GraphQL 开启

       ↓

扫描目录

       ↓

发现 console / playground

       ↓

直接访问接口

       ↓

未授权成功

***这个思路可以怎么复用？***

这个案例最有价值的，其实不是漏洞本身，而是：

**一套可以复用的测试方法**

固定动作

现在只要看到这些：

* /graphql
* /api/graphql
* /playground
* /console

做三件事：

**1️⃣ 先打 introspection**

判断：

👉 能不能拿到 schema

**2️⃣ 扫目录**

找：

* console
* playground
* 版本接口

**3️⃣ 测未授权**

直接发请求：

👉 看是否需要登录

***一个很重要的认知***

做接口测试时，不要局限在：

* 参数
* 权限
* 越权

**接口文档本身，就是攻击面**

**建了个**src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "null")

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTahgbr35OD8B1WCHW2uGMetuDzTPJiaHibhWhMm8UQ5iboDmNKqrRfjIrXQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaTWxLibDHdqdx6IahjVWr6ficJWskIMjdrbYaLGBIVsbONxbb5ibDS5trQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTafQtWhe2qhicQCvx8XaDyp6Kb4eeWBnhZLlGKcAvxKausLKc2YYggykQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWWIDTric5u0Q03o25wLLgNBwFd6t4ud64ACo8icCdQRzrEGezUzIKSvEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwTwGlGVzNXsrzvmAQZPAYml7mNFiaPun3MGdwqm4SlxShf8erQ8YSAJGb4tvzcQmibiafWTeltAjz8ullUsSia8f08mwsAQQtUqQWk/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过