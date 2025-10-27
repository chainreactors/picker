---
title: API安全学习笔记 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17072527.html
source: 博客园 - 渗透测试中心
date: 2023-01-30
fetch_date: 2025-10-04T05:10:31.721044
---

# API安全学习笔记 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [API安全学习笔记](https://www.cnblogs.com/backlion/p/17072527.html "发布于 2023-01-29 14:00")

# 必要性

前后端分离已经成为web的一大趋势，通过Tomcat+Ngnix(也可以中间有个Node.js)，有效地进行解耦。并且前后端分离会为以后的大型分布式架构、弹性计算架构、微服务架构、多端化服务（多种客户端，例如：浏览器，车载终端，安卓，IOS等等）打下坚实的基础。而API就承担了前后端的通信的职责。所以学习api安全很有必要。
本文的思路在于总结一些api方面常见的攻击面。笔者在这块也尚在学习中，如有错误，还望各位斧正。

# 常见的api技术

## GraphQL

GraphQL 是一个用于 API 的查询语言
通常有如下特征：
（1）数据包都是发送至/graphql接口
[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230129135917968-89120057.png)](https://cdn.nlark.com/yuque/0/2022/png/12672776/1671002336401-b709f7d4-c599-47f2-9198-65240e752286.png#averageHue=%23f1f0ef&clientId=u96982c42-675a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=108&id=u7522f849&margin=%5Bobject%20Object%5D&name=image.png&originHeight=162&originWidth=429&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13941&status=done&style=none&taskId=ucb9c3d18-7b00-4ee7-8f79-4ff9c5a167e&title=&width=286)
（2）其中包含了很多换行符\n

```
{"query":"\n    query IntrospectionQuery {\r\n      __schema {\r\n        queryType { name }\r\n        mutationType { name }\r\n        subscriptionType { name }\r\n        types {\r\n          ...FullType\r\n        }\r\n        directives {\r\n          name\r\n          description\r\n          locations\r\n          args {\r\n            ...InputValue\r\n          }\r\n        }\r\n      }\r\n    }\r\n\r\n    fragment FullType on __Type {\r\n      kind\r\n      name\r\n      description\r\n      fields(includeDeprecated: true) {\r\n        name\r\n        description\r\n        args {\r\n          ...InputValue\r\n        }\r\n        type {\r\n          ...TypeRef\r\n        }\r\n        isDeprecated\r\n        deprecationReason\r\n      }\r\n      inputFields {\r\n        ...InputValue\r\n      }\r\n      interfaces {\r\n        ...TypeRef\r\n      }\r\n      enumValues(includeDeprecated: true) {\r\n        name\r\n        description\r\n        isDeprecated\r\n        deprecationReason\r\n      }\r\n      possibleTypes {\r\n        ...TypeRef\r\n      }\r\n    }\r\n\r\n    fragment InputValue on __InputValue {\r\n      name\r\n      description\r\n      type { ...TypeRef }\r\n      defaultValue\r\n    }\r\n\r\n    fragment TypeRef on __Type {\r\n      kind\r\n      name\r\n      ofType {\r\n        kind\r\n        name\r\n        ofType {\r\n          kind\r\n          name\r\n          ofType {\r\n            kind\r\n            name\r\n            ofType {\r\n              kind\r\n              name\r\n              ofType {\r\n                kind\r\n                name\r\n                ofType {\r\n                  kind\r\n                  name\r\n                  ofType {\r\n                    kind\r\n                    name\r\n                  }\r\n                }\r\n              }\r\n            }\r\n          }\r\n        }\r\n      }\r\n    }\r\n  ","variables":null}
```

## SOAP-WSDL

```
WSDL (Web Services Description Language,Web服务描述语言)是一种XML Application，他将Web服务描述定义为一组服务访问点，客户端可以通过这些服务访问点对包含面向文档信息或面向过程调用的服务进行访问
```

走的是SOAP协议，一般发送的xml格式的数据，然后会有WSDL文件
[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230129135918652-993812695.png)](https://cdn.nlark.com/yuque/0/2022/png/12672776/1671003894888-7aecc898-b376-4f5b-9a8a-be3103e22182.png#averageHue=%23e4e2c7&clientId=u96982c42-675a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=75&id=u4ac24937&margin=%5Bobject%20Object%5D&name=image.png&originHeight=112&originWidth=472&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7345&status=done&style=none&taskId=u6f8e8d9b-0b1e-42c6-96cf-871cd3bf3f3&title=&width=314.6666666666667)
.net中常见的.asmx文件也有wsdl格式 xxx.asmx?wsdl
[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230129135919449-1509316087.png)](https://cdn.nlark.com/yuque/0/2022/png/12672776/1671003840372-a6bebebd-7ead-4b2e-881b-e425452bbcf3.png#averageHue=%23c49f72&clientId=u96982c42-675a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=420&id=u73e62ac2&margin=%5Bobject%20Object%5D&name=image.png&originHeight=630&originWidth=1340&originalType=binary&ratio=1&rotation=0&showTitle=false&size=171288&status=done&style=none&taskId=u6babef20-b6ca-47a1-9c75-054db4ceb0c&title=&width=893.3333333333334)
我们可以使用soapui对这类api进行测试

## WADL

文件里面有很明显的wadl标志

[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230129135920363-2085092611.png)](https://cdn.nlark.com/yuque/0/2022/png/12672776/1671086474308-c8da0013-5965-4623-b0c4-7c6a2a63d810.png#averageHue=%23f3f3f2&clientId=u5753fac2-d2ac-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=593&id=u8dc972f3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=889&originWidth=1559&originalType=binary&ratio=1&rotation=0&showTitle=false&size=186714&status=done&style=none&taskId=u6c3c9a13-691f-46ef-869e-93b84fbacec&title=&width=1039.3333333333333)
同样也可以用soapui的rest功能进行测试

[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230129135921297-1009304781.png)](https://cdn.nlark.com/yuque/0/2022/png/12672776/1671086495338-1eefee6a-7e8e-43bd-8e56-2632760dab6b.png#averageHue=%23f1f0ef&clientId=u5753fac2-d2ac-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=599&id=u9d24c22d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=899&originWidth=1683&originalType=binary&ratio=1&rotation=0&showTitle=false&size=140462&status=done&style=none&taskId=ud7ca314f-4977-4e69-bc13-5221057531e&title=&width=1122)

## REST

rest api并不像前面几种那种特征明显，也是如今使用最多的一种api技术

```
REST 是一组架构规范，并非协议或标准。API 开发人员可以采用各种方式实施 REST。

当客户端通过 RESTful API 提出请求时，它会将资源状态表述传递给请求者或终端。该信息或表述通过 HTTP 以下列某种格式传输：JSON（Javascript 对象表示法）、HTML、XLT、Python、PHP 或纯文本。JSON 是最常用的编程语言，尽管它的名字英文原意为“JavaScript 对象表示法”，但它适用于各种语言，并且人和机器都能读。

还有一些需要注意的地方：头和参数在 RESTful API HTTP 请求的 HTTP 方法中也很重要，因为其中包含了请求的元数据、授权、统一资源标识符（URI）、缓存、cookie 等重要标识信息。有请求头和响应头，每个头都有自己的 HTTP 连接信息和状态码。
```

# 获取端点的方式

对于api的一些安全测试，通常关注api的权限问题，api端点和基础设施的安全问题。
要测试api端点的安全问题，肯定得尽量获取多的api端点

## swagger api-docs泄露

Swagger 是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful 风格的 Web 服务
常见指纹：

```
# swagger 2
/swagger-ui.html
/api-docs
/v2/api-docs

# swagger 3
/swagger-ui/index.html
```

[![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-2023012913...