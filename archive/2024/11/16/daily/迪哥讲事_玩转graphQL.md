---
title: 玩转graphQL
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496348&idx=1&sn=1b3f4166bf0729fcc6ba83e064c68060&chksm=e8a5f8ffdfd271e9cbf29fa22eece49e068005cc1c6da1c54d861d4e0dc7b52cafeb4c5a3a19&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-16
fetch_date: 2025-10-06T19:20:20.252920
---

# 玩转graphQL

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj76RgkiaRdL3IjDibGkYVviaxib2JeC3X0Z5LewEgh4rfgqic2epNe1Wzy0d9kLHwQDKvX6WNn5NBoamBg/0?wx_fmt=jpeg)

# 玩转graphQL

迪哥讲事

编者荐语：

复习gaphql

以下文章来源于酒仙桥六号部队
，作者先锋情报站

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6h5jOvetH9FCV9SZjkg2PBbViaA8jlNfDJtZqedia3h3UQ/0)

**酒仙桥六号部队**
.

知其黑，守其白。 分享知识盛宴，闲聊大院趣事，备好酒肉等你！

这是 **酒仙桥六号部队**的第 **118**篇文章。

全文共计4257个字，预计阅读时长12分钟。

##

**前言**

##

在测试中我发现了很多网站开始使用GraphQL技术，并且在测试中发现了其使用过程中存在的问题，那么，到底GraphQL是什么呢？了解了GraphQL后能帮助我们在渗透测试中发现哪些问题呢？

在测试中，我们最常见的graphql的数据包就像图中一样：

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16VtYylEbeyo4ShicVOmZ73qLI6ibCtibVPL6vCmWscvg7icvwA8Ext9pApQ/640?wx_fmt=png)

和json类似的格式，但其中包含了很多换行符\n，当你遇到这种结构的请求时，请多留心测试一下GraphQL是否安全。

**前置知识**

### 什么是GraphQL

GraphQL 是一个用于 API的查询语言，使用基于类型系统来执行查询的服务（类型系统由你的数据定义）。GraphQL 并没有和任何特定数据库或者存储引擎绑定，而是依靠你现有的代码和数据支撑。

如果你了解REST API会更快地了解它。像REST API，往往我们的请求需要多个API，每个API是一个类型。比如：http://www.test.com/users/{id} 这个API可以获取用户的信息；再比如：http://www.test.com/users/list 这个API可以获取所有用户的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16lXCDXFVCZbqSM6YHEc4c8jm8vCpicPKId0I6FHqbNmVZwZicYRab5XOA/640?wx_fmt=png)

在graphql中则不需要这么多api来实现不同的功能，你只需要一个API，比如：http://www.test.com/graphql即可。查询不同的内容仅需要改变post内容，不再需要维护多个api。（使用官方的demo进行演示：https://graphql.org/swapi-graphql）

比如查id为1的一个人的生日，可以这么查：

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16eJXL9NO0PYpA5wdnG5v29G7iayA6uYrFWe9hIZ44iblApyJBRZH6tuTg/640?wx_fmt=png)

想查他的身高、发色可以这么查：

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16zBrOFEe4Erur1JNROOt87H0pesibO7QGAeQsbfLXK0IGXpvlgl8Do6g/640?wx_fmt=png)

我想查id为2的人的信息我可以这么查：

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic160K2pMSEofwkcLtmFzib4UIiarnDZaesmRLESMglTxKXOdH6nYP7DA8Kg/640?wx_fmt=png)

通过上面这个例子就可以看出graphql与REST API的区别，仅用一个API即可完成所有的查询操作。并且他的语法和结构都是以一个对象不同属性的粒度划分，简单好用。

### 基本属性

GraphQL的执行逻辑大致如下：

查询->解析->验证->执行

根据官方文档，主要的操作类型有三种：query（查询）、mutation（变更）、subscription（订阅），最常用的就是query，所有的查询都需要操作类型，除了简写查询语法。

类型语言TypeLanguage，type来定义对象的类型和字段，理解成一个数据结构，可以无关实现graphQL的语言类型。类型语言包括Scalar（标量）和Object（对象）两种。并且支持接口抽象类型。

Schema用于描述数据逻辑，Schema就是对象的合计，其中定义的大部分为普通对象类型。一定包括query，可能包含mutation，作为一个GraphQL的查询入口。

Resolver用于实现解析逻辑，当一个字段被执行时，相应的 resolver 被调用以产生下一个值。

### 内省查询

简单来说就是，GraphQL内置了接口文档，你可以通过内省的方法获得这些信息，如对象定义、接口参数等信息。

当使用者不知道某个GraphQL接口中的类型哪些是可用的，可以通过\_\_schema字段来向GraphQL查询哪些类型是可用的。

```
{  __schema {    types {      name    }  }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16QBZO6EVhtLXwq8QjBZo5hjmnym1fGrYngKziaoQj92qNibWtiadke9BJw/640?wx_fmt=png)

```
{  __type(name: "Film") {    name    fields {      name      type {        name        kind        ofType {          name          kind        }      }    }  }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16A9VymskkPoPGWJ1XGaNedu7lHP9icRNmSnwicOMYiamoLlQ0WgiciaMuiaBQ/640?wx_fmt=png)

具体可以参考GraphQL文档学习。

**GraphQL中常见的问题**

### 内省查询问题

这本来应该是仅允许内部访问，但配置错误导致任何攻击者可以获得这些信息。

还是拿官网的demo来测试。

一个正常的查询请求如下。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16HJC0zcmc60b2VbwOpPcAIyBPf1PWDjcEKKups8mGVEjc56FQaFSiciaA/640?wx_fmt=png)

通过内省查询获得的数据如下：

```
{"query":"\n    query IntrospectionQuery {\r\n      __schema {\r\n        queryType { name }\r\n        mutationType { name }\r\n        subscriptionType { name }\r\n        types {\r\n          ...FullType\r\n        }\r\n        directives {\r\n          name\r\n          description\r\n          locations\r\n          args {\r\n            ...InputValue\r\n          }\r\n        }\r\n      }\r\n    }\r\n\r\n    fragment FullType on __Type {\r\n      kind\r\n      name\r\n      description\r\n      fields(includeDeprecated: true) {\r\n        name\r\n        description\r\n        args {\r\n          ...InputValue\r\n        }\r\n        type {\r\n          ...TypeRef\r\n        }\r\n        isDeprecated\r\n        deprecationReason\r\n      }\r\n      inputFields {\r\n        ...InputValue\r\n      }\r\n      interfaces {\r\n        ...TypeRef\r\n      }\r\n      enumValues(includeDeprecated: true) {\r\n        name\r\n        description\r\n        isDeprecated\r\n        deprecationReason\r\n      }\r\n      possibleTypes {\r\n        ...TypeRef\r\n      }\r\n    }\r\n\r\n    fragment InputValue on __InputValue {\r\n      name\r\n      description\r\n      type { ...TypeRef }\r\n      defaultValue\r\n    }\r\n\r\n    fragment TypeRef on __Type {\r\n      kind\r\n      name\r\n      ofType {\r\n        kind\r\n        name\r\n        ofType {\r\n          kind\r\n          name\r\n          ofType {\r\n            kind\r\n            name\r\n            ofType {\r\n              kind\r\n              name\r\n              ofType {\r\n                kind\r\n                name\r\n                ofType {\r\n                  kind\r\n                  name\r\n                  ofType {\r\n                    kind\r\n                    name\r\n                  }\r\n                }\r\n              }\r\n            }\r\n          }\r\n        }\r\n      }\r\n    }\r\n  ","variables":null}
```

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16uRzu4roh8s3nNMVWCqhXh97RxkMzFm5lktSYoQYo16YLgib4SYXDV1w/640?wx_fmt=png)

返回包返回的就是该API端点的所有信息。复制返回包到以下网址可以得到所有的对象定义、接口信息。

https://apis.guru/graphql-voyager/

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic164er4IRQCiboPHTrrM9SxdpLbGXFXWzCyYjboCrTIfTGJrPNXSkIoibMQ/640?wx_fmt=png)

github也有很多工具可以直接绘制接口文档：

https://github.com/2fd/graphdoc

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16lULQm1SBwu8uMrb2QdMOnU9COlqmOhKlZDRcF9zd8xvB8hSUicVPia0A/640?wx_fmt=png)

https://github.com/graphql/graphql-playground

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16MFqLvIDHt8fzBW4iaAo5ibwkQzwVZPWsYEvDQttKicgFNKuaao0pxrGFg/640?wx_fmt=png)

这是garphql最常见的一类问题，通过这些文档我们就能很轻松的找到存在问题的对象了。通过遍历，即可发现很多安全问题。不过这个问题可以通过配置来解决，让攻击者无法获得敏感信息，或者其他攻击面。

### 信息泄露

通过内省查询，我们可以得到很多后端接口的信息。有了这些信息通过排查便可能发现更多的安全问题，比如信息泄露。

查询存在的类型：

```
{  __schema {    types {      name    }  }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16y4Qsiarr2nQGqxjCaGXQxS2wuahiayWicnIrHedM7PS605EUlqW5EBibDw/640?wx_fmt=png)

查询类型所有的字段：

```
{  __type (name: "Query") {    name    fields {      name      type {        name        kind        ofType {          name          kind        }      }    }  }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16csnkzo9QDyeqeFaaIPS11lD5IoGcmV5ibzaAYMbibsmjb4LsmSibn3okA/640?wx_fmt=png)

在查找字段里是否包含一些敏感字段：

Email、token、password、authcode、license、key、session、secretKey、uid、address等。

除此以外还可以搜索类型中是否有edit、delete、remove、add等功能，来达到数据编辑、删除、添加的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16dVlwdmZovlTx2RFxyicOrcyAKyZHs9fueeUfEe0jgqOZYoaqfIPWKPQ/640?wx_fmt=png)

### SQL注入

graphql的sql注入与一般的sql注入类似，都是可以通过构造恶意语句达到注入获取数据或改变查询逻辑的目的。p神在先知大会上讲过该类问题，借用p神的2张PPT。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16LMIFrHSxHgkawibK7cEDWuQFhDPL8HDVTpsDIf69EUNBQnnM7o7s1Og/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16ibN6BJLOlhETP66LfcFY1kHTiay8IS8vRiclM91l8IuN95Alibpm1TeJ1w/640?wx_fmt=png)

只有直接使用graphql进行查询才会出现的问题，正确的使用参数化查询，不会遇到sql注入的问题。

### CSRF

在Express-GraphQL中存在CSRF漏洞。如果将Content-Type修改为application/x-www-form-urlencoded ，再将POST请求包内容URL编码并生成csrf poc 即可实施csrf攻击，对敏感操作如mutation（变更）造成危害。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16CPicnVGURR3J0SlicLrhEsRbrJkEw9kHmUyCPjD4s1CxGCDC2SSRym8g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54B52X8UPybZgzLeupG5ic16oRhJozAfsPJyVJAZDDNzJwtIvRbicngw73F4MDdficVySGopMKL8Rxcw/640?wx_fmt=png)

修复方式可以考虑将CORS配置为仅允许来自受信任域的白名单的请求，或者确保正在使用CSRF令牌.实施多种保护将降低成功攻击的风险.

### 嵌套查询拒绝服务

当业务的变量互相关联，如以下graphql定义为这样时，就可能无限展开，造成拒绝服务。

```
type Thread {  messages(first: Int, after: String): [Message]}
type Message {  thread:...