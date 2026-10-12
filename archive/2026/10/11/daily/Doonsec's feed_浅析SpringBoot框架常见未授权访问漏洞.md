---
title: 浅析SpringBoot框架常见未授权访问漏洞
url: https://mp.weixin.qq.com/s/0Q6MlhAXMwOinskHvyfj8w
source: Doonsec's feed
date: 2026-10-11
fetch_date: 2026-10-12T08:13:23.294713
---

# 浅析SpringBoot框架常见未授权访问漏洞

# 浅析SpringBoot框架常见未授权访问漏洞

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前言

在对 Java 站点进行渗透测试的过程中，经常会遇见各类未授权访问漏洞，本文来总结学习下常见的几类未授权访问漏洞的检测和利用方法。

SpringBoot 站点的简单识别方法：

1） 通过 web 应用程序网页标签的图标（favicon.ico）：如果 web 应用开发者没有修改 springboot web 应用的默认图标，那么进入应用首页后可以看到如下默认的绿色小图标：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goafiaEDomvz6yIOJXYiaoTlicxtaAU6DLBH4ZeKzvcdkCXVDYDrKoQJ4RiaMpKYWXz9l5MEFlRKaexSz5w5lCCDia3woFl0vNfKcKM/640?wx_fmt=png&from=appmsg)

2）通过 springboot 框架默认报错页面；如果 web 应用开发者没有修改 springboot web 应用的默认 4xx、5xx 报错页面，那么当 web 应用程序出现 4xx、5xx 错误时，会报错如下（此处仅以 404 报错页面为例）：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grf0SxMicuXP5gJDNDARm7mwnB6NNA308KAg5ialsKXRArYWcjOQjFGibYv5567PQw5uWbrIfEibgF8YGOicMQ17iaodVMiacvicYlst20/640?wx_fmt=png&from=appmsg)

## Swagger未授权访问

Swagger 是一个用于生成、描述和调用 RESTful API 接口的 Web 服务。通俗的来讲，Swagger 就是将项目中所有（想要暴露的）接口展现在页面上，并且可以进行接口调用和测试的服务。

在平时渗透测试的的时候，经常会发现 Swagger ui（swagger-ui 是将 api 接口进行可视化展示的工具）接口泄露，如下，在这个页面中暴露了目标站点中所有的接口信息，所以可以对这个接口进行漏洞测试，看是否存在未授权访问、sql 注入、文件上传等漏洞。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqtKkQUo9DQygm3ZSl9qGrwDqhpcvNCiboQ6VD58X2s88Xc9p9hsHl3sU8To2vKk8SZkbzaDt68McZfN2eenOBVIIYsbuatUX0o/640?wx_fmt=png&from=appmsg)

```
Fofa搜索语法：title="Swagger UI"
Googlehack语法：intext:"Swagger UI"intitle:"Swagger UI"site:yourarget.com
```

修复 Swagger 未授权访问漏洞的方案：

配置 Swagger 开启页面访问限制；

排查接口是否存在敏感信息泄露（例如：账号密码、SecretKey、OSS配置等），若有则进行相应整改。

Swagger 未授权访问地址可能存在于以下默认路径：

```
/api
/api-docs
/api-docs/swagger.json
/api.html
/api/api-docs
/api/apidocs
/api/doc
/api/swagger
/api/swagger-ui
/api/swagger-ui.html
/api/swagger-ui.html/
/api/swagger-ui.json
/api/swagger.json
/api/swagger/
/api/swagger/ui
/api/swagger/ui/
/api/swaggerui
/api/swaggerui/
/api/v1/
/api/v1/api-docs
/api/v1/apidocs
/api/v1/swagger
/api/v1/swagger-ui
/api/v1/swagger-ui.html
/api/v1/swagger-ui.json
/api/v1/swagger.json
/api/v1/swagger/
/api/v2
/api/v2/api-docs
/api/v2/apidocs
/api/v2/swagger
/api/v2/swagger-ui
/api/v2/swagger-ui.html
/api/v2/swagger-ui.json
/api/v2/swagger.json
/api/v2/swagger/
/api/v3
/apidocs
/apidocs/swagger.json
/doc.html
/docs/
/druid/index.html
/graphql
/libs/swaggerui
/libs/swaggerui/
/spring-security-oauth-resource/swagger-ui.html
/spring-security-rest/api/swagger-ui.html
/sw/swagger-ui.html
/swagger
/swagger-resources
/swagger-resources/configuration/security
/swagger-resources/configuration/security/
/swagger-resources/configuration/ui
/swagger-resources/configuration/ui/
/swagger-ui
/swagger-ui.html
/swagger-ui.html#/api-memory-controller
/swagger-ui.html/
/swagger-ui.json
/swagger-ui/swagger.json
/swagger.json
/swagger.yml
/swagger/
/swagger/index.html
/swagger/static/index.html
/swagger/swagger-ui.html
/swagger/ui/
/Swagger/ui/index
/swagger/ui/index
/swagger/v1/swagger.json
/swagger/v2/swagger.json
/template/swagger-ui.html
/user/swagger-ui.html
/user/swagger-ui.html/
/v1.x/swagger-ui.html
/v1/api-docs
/v1/swagger.json
/v2/api-docs
/v3/api-docs
```

## RESTful API 设计风格

REST，全名 Representational State Transfer (表现层状态转移)，它是一种设计风格，一种软件架构风格，而不是标准，只是提供了一组设计原则和约束条件。RESTful 只是转为形容词，就像那么 RESTful API 就是满足 REST 风格的，以此规范设计的 API。

介绍请参见：《一杯茶的时间，搞懂 RESTful API》、《一文搞懂RESTful API》。

https://apifox.com/blog/a-cup-of-tea-time-to-understand-restful-api/

https://www.cnblogs.com/bigsai/p/14099154.html

举个例子：提供一个订单信息 API，早期程序员为了更方便传递信息全部使用了 POST 请求，使用了定义了 method 表明调用方法：

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grpY7uj1H8F6xXCGTCoqHCntS6yvrTRd82TzOK68Hr8eMmy7PVcPn5QTiadsLQ3VkxfCGhMUnQs8SppqjSop3icTIBwHOv51O6Nc/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpROCIrFal5KNJKBIN7asX37nVBicJ8rqDJ4c2vK2H00gBg0Pa1wZSlf24NQALQxuZLW8huL0K26Ywm6NE5qib1Nria2aS7n0p2eA/640?wx_fmt=png&from=appmsg)

现在来看上述例子会觉得设计上很糟糕，但是在当时大量的 API 是这样设计的。操作资源的动作全部在数据体里面重新定义了一遍，URL 上不能体现出任何有价值的信息，为缓存机制带来麻烦。对前端来说，在组装请求的时候显得麻烦不说，另外返回到数据的时候需要检查 HTTP 的状态是不是 200，还需要检查 status 字段。那么使用 RESTful 的例子是什么样呢：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpmAJNia7oic5WNPV0gwD7S78mEfULtP6ZnjOmfViaTh2cOnY0xrrj09U5gPalopIJibwyJcd2W2IalXm1YQp9kibpXNuxHOg9vNeCU/640?wx_fmt=png&from=appmsg)

上述例子体现的 RESTful API 的优点：

## swagger-ui 未授权访问

下面使用 Java 安全综合靶场搭建 Swagger 漏洞环境：https://github.com/JoyChou93/java-sec-code，直接下载源码后在虚拟机基于 Docker 快速搭建：

```
1）Startdocker:
docker-composepull
docker-composeup

2）Stopdocker:
docker-composedown

3）登录地址与密码：
http://localhost:8080/login，admin/admin123
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqfKmiaHxOmyWdVibmD3g55r0FMuiaEyXTIBwNHZ7Eyqf9B2iaXcwNkr6XnwTk3ia40hFibU0eukNbib1iaQxLjB6ciacIS2monbWXFI8fo/640?wx_fmt=png&from=appmsg)

实际上 java-sec-code 靶场并不存在 Swagger-ui 未授权访问漏洞，需要用户登录以后才能访问到 swagger-ui，此处我们假设无需登录即可访问：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1go8GxPIibFbtbWu9aSK8XkC8E09aTfsPYWJnoEwdnNFVDozicgfa4FqKHicuaPuC432XZm3ibufloQu4gFplzG0kQWu8qZQATzpKII/640?wx_fmt=png&from=appmsg)

路由 swagger-ui.html#/ 列举了所有的 api 接口，以 login 接口为例：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gprMZuiaG4lS1NPsicIF116icDQqdGqwxYknicjfpK2Lw6Dg4Hib2TIXlje6l2jibqvA5H7Uhq32uyzibYUFP6T4A7A5z75c7gmpTTQHw/640?wx_fmt=png&from=appmsg)

点击 Try it out --> Execute 可以调用接口并查看服务器返回数据：

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqRK3jLjYMQR6h3V9OaSDonyPicsEOzQv532SNt36t4tnpicrYC7ty2VKyKUZqhZ5SRY0kkok5HLS5n67Wcqq4PZ5GSUPV9lZCwk/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grRWibqNo5KFqHibjq3UUsNezVFn94zyDzwicv0SYyiaGU3ywNRYfHPJ7bmopYArl0sibkiaCV59sYAFDozLA1cneOVIcdic6STAib4ia9Q/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqjKxICal9KZiaIQFp8w5AWyb9HuL5z436ewISfibGP3guaKiaaLgNrAagevuSoPkA7CBHdFb6zZ0CBuaBicmicYtO0k6r6WGfGA13s/640?wx_fmt=png&from=appmsg)

Swagger-ui 提供的 Restful API 接口也会同步提供相应的，发起模拟请求时可以填入具体参数值后再发送请求，比如 SSRF 漏洞示例接口 http://ip:8080/ssrf/urlConnection/vuln?url=XXX：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpEGsx9LyxJPp3kEM278MLNSRZmp7U51IM6mYlv6VHWms65D7hk59zN2euvSc128wDrDl1ibjBTTeTicEicEgqGiauEartgSLiaex4k/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1go6kBdONvXl9kfdGXMicNxA6d4mSciahPNWbeDyPhIl3qkfUZNFBY8t27hB5ZKJ73A0L68NF6LRW3icavvAZqTFTpwh7btur4f7wY/640?wx_fmt=png&from=appmsg)

## swagger 接口批量探测

通过访问 api-docs 或者 swagger.json 可以直接获取 Json 格式的全部接口文档：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grVGpWfDQYKK09tDXT3N9Xma4icWj8zicPed1vicmFoSxDqJzHCWUSC3LM1xQb5aBSib5O0ic0UR6Fia4ibWgjL4weeCPrkZ0nUVywiayQ/640?wx_fmt=png&from=appmsg)

具体地址可在 swagger-ui 页面上找到：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grEHQKricO3SjZicMClGTcibdjvAGJvrYBSvadvjBUMWMSIg3admzdzsGTPIMqqnaxIZ1JHWCTlbdpmTGGEzbmyhDEicjGyHbFU2Oc/640?wx_fmt=png&from=appmsg)

在目标系统存在大量 API 接口的情况下，逐一进行手工测试的话会消耗大量精力，可以使用一些现成的自动化工具来快速完成此项工作。

### 0x01 Postman API工具

第一种方案是借助 Postman 工具（或者 Apifox 工具：https://apifox.com/），利用思路：

```
将 Swagger ui 中所有的接口导入到 Postman；
在 Postman 设置代理，将流量转发给 Burpsuite，方便观察发包情况；
对导入的所有 api 自动运行测试，让 Postman 自动对每个 api 进行请求；
Burpsuite 可挂上 Xray，进行自动化漏洞检测；
```

具体演示请参见：《Swagger ui接口自动化批量漏洞测试》、《Actuator内存泄露及利用&Swagger未授权&自动化测试实现》。

Postman 导入数据总是失败，此处用 Apifox 应用导入目标 Swagger API 接口：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1go9lbQ8fclM5TQvIwG2dtmHmYZZHHvOxhQ1JZV4tlZYJVdEkd5ibbaVyTstOVrJbgrCYuWx0AiaArMPxV8a9XSPuST3lLDojOHcc/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqJmrh7K5dCfvGd31UdiaGkS1FQPswlicQW4n6aHmzricRmJGJjr5LK35wK5D21lZmQ7jN55CKUvB4IxGpbO6ZT0RFAmDP0LicZB7k/640?wx_fmt=png&from=appmsg)

发送测试请求（下面是单独一个接口，实际上可以批量发送请求）：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goXxFXptFJ8O1JvP0S1cZbZMbFUjpP6EqIDJNwv9wRFY2WOzc1wErrEicMgt8YGVCl3s72K5ex65J1GWYAHI8kGlxviaNiapBWia9E/640?wx_fmt=png&from=appmsg)

接下来设置网络代理将流量转发到 Burpsuite：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gooib6ic5DcVic9jg91rTQRMxcR1jBfUzicib9QiaENAUq5OzdCVDELf6AEqbMwibeOu47buMGiaTf7YIucS0EdGUsiapzAmfqRaaIQhno8/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oF...