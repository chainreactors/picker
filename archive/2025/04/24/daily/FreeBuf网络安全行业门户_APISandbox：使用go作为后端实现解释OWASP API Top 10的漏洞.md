---
title: APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞
url: https://www.freebuf.com/articles/web/428164.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:57.127998
---

# APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

APISandbox：使用go作为后端实现解释OWASP API Top 10的漏洞

2025-04-27 11:32:15

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 一、APISandbox靶场说明

https://github.com/API-Security/APISandbox

是一个包含多个场景的API漏洞靶场

目前有以下几个API漏洞场景靶场：

4ASystem: 4A认证系统下的API平行越权

APIVuln: 生产消费流水线中的API缓存投毒

GraphqlNotebook: 一个使用GraphQL的留言板以及经典API漏洞

InfoSystem: WSDL泄露API越权进后台Getshell

OASystem: SpringBoot微服务架构下的API Gateway配置问题

OWASPApiTop10: 使用go作为后端实现解释OWASP API Top 10的漏洞

```
# 下载项目
wget https://github.com/API-Security/APISandbox/archive/refs/heads/main.zip -O APISandbox-main.zip
unzip APISandbox-main.zip
cd APISandbox-main

# 进入某一个漏洞/环境的目录
cd OWASPApiTop10

# 自动化编译环境
docker-compose build

# 启动整个环境
docker-compose up -d

每个环境目录下都有相应的说明文件，请阅读该文件，进行漏洞/环境测试。

# 测试完成后，删除整个环境

docker-compose down -v
```

## 二、OWASPApiTop10: 使用go作为后端实现解释OWASP API Top 10的漏洞

> OWASPAPITOP10
>
> OWASP API Security Project: <https://owasp.org/www-project-api-security/>
>
> API泄漏
>
> 访问首页会跳转到swagger-ui界面，泄漏了所有API。
>
> API1: Broken object level authorization [✔︎]
>
> 普通用户登录后，`/v2/user/getuserinfo/:id`API接口可以遍历用户信息。
>
> API2: Broken authentication [✔︎]
>
> SecretKey: 0waspApiTop10
>
> 没有使用随机值，泄漏后可本地伪造鉴权，导致任意用户登录
>
> gin的session在知道secret之后就可以任意伪造
>
> 这块可以和API7联动，API7泄露源码
>
> API3: Excessive data exposure [✔︎]
>
> 普通用户登录后，`/v2/user/getuseremail`可以获取全部用户邮箱信息，web前端只取当前用户ID的邮箱，过多的数据暴露。
>
> API4: Lack of resources and rate limiting [✔︎]
>
> `/v2/login`可以爆破admin密码:123qweasd，API接口未限制请求速率。
>
> API5: Broken function level authorization [✔︎]
>
> `/v2/user/getuserprofile`返回自己的全部信息。
>
> 用户未知的情况下，`/v2/user/getuserprofiles`返回全部用户信息。
>
> API6: Mass assignment [✔︎]
>
> `/v2/register`
>
> 前端请求有隐藏的admin标签，可以手动加上，admin为true可以注册为管理员权限用户
>
> username=123&password=123&admin=false
>
> API7: Security misconfiguration [✔︎]
>
> `/static`
>
> 设置静态目录的时候设置到了上一级，导致可以下源码或者下载二进制文件。
>
> API8: Injection [✔︎]
>
> `/v2/login`存在sqlite注入，可以得到用户名密码
>
> API9: Improper assets management [✔︎] （资产管理不当）
>
> `/v2/getenv`禁止访问
>
> `/v1/getenv`可以访问
>
> 由于开发历史遗留的API接口没有被取消，导致旧版本的API接口可以看到环境变量。
>
> API10: Insufficient logging and monitoring [✔︎]
>
> `/v1/evil`
>
> 没有日志，无法记录信息。默认情况下无日志

#### swaggerAPI文档暴露

访问ip:58084即为swagger首页

```
1、对象级授权缺失（BOLA, Broken Object Level Authorization）
2、身份认证缺失（Broken Authentication）
3、过度数据暴露（Excessive Data Exposure）
4、资源与速率限制不足（Lack of Resources and Rate Limiting）
5、功能级授权缺失（BFLA, Broken Function Level Authorization）
6、批量分配漏洞（Mass Assignment）
7、安全配置错误（Security Misconfiguration）
8、注入漏洞（Injection）
9、资产管理不当（Improper Assets Management）
10、日志记录与监控不足（Insufficient Logging and Monitoring）
```

![image](https://image.3001.net/images/20250421/1745222728_6805fc4857f8548595ee5.png!small)

拿到api清单，考虑是否可以登录获取访问权限，再考虑其他api的漏洞利用点

![image](https://image.3001.net/images/20250421/1745222730_6805fc4a133905c5f1289.png!small)![image](https://image.3001.net/images/20250421/1745222731_6805fc4b9eece00344cca.png!small)

### 方法一：自己构建请求包

尝试请求，构造登录请求包，有返回，开搞

![image](https://image.3001.net/images/20250421/1745222733_6805fc4d54d9bfb0c5939.png!small)

![image](https://image.3001.net/images/20250421/1745222735_6805fc4f1457ff995367c.png!small)

```
POST /v2/login HTTP/1.1
Host: 192.168.80.131:58084
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 45

{
"username":"admin",
"password":"admin"
}
```

### 方法二：通过APIkit进行api文档解析扫描

APIKit：Discovery, Scan and Audit APIs Toolkit All In One

安装APIKit，步骤见（https://github.com/API-Security/APIKit/tree/main）

访问目标网站，抓包，右键-扩展-APIkit-目标API扫描

![image](https://image.3001.net/images/20250421/1745222737_6805fc512bb18da1b9927.png!small)

选择api指纹、填url（需要以 / 结尾）、填api文档地址（json格式）

![image](https://image.3001.net/images/20250421/1745222739_6805fc531e40498e62546.png!small)

![image](https://image.3001.net/images/20250421/1745222740_6805fc54ac66f17588a4f.png!small)

扫描后得到结果，就可以愉快地去api去渗透了

![image](https://image.3001.net/images/20250421/1745222742_6805fc566b11688fabb12.png!small)

## API 4【登录接口爆破】 Lack of resources and rate limiting（未限制请求速率）

`/v2/login`可以爆破admin密码:123qweasd，API接口未限制请求速率。

查看靶场md以及APIkit扫描结果，/v2/login接口存在两个问题

4、资源与速率限制不足（Lack of Resources and Rate Limiting）——可以爆破

8、注入漏洞（Injection）——存在注入点

爆破的得到登录账密

![image](https://image.3001.net/images/20250421/1745222744_6805fc5856b54e193397c.png!small)

拿到cookie

![image](https://image.3001.net/images/20250421/1745222746_6805fc5a2b240de78d244.png!small)

## API 1【越权漏洞 】 Broken object level authorization（遍历用户信息）

普通用户登录后，`/v2/user/getuserinfo/:id`API接口可以遍历用户信息。

从api4拿到cookie，遍历用户信息

![image](https://image.3001.net/images/20250421/1745222748_6805fc5c18a9ec2919bf9.png!small)

![image](https://image.3001.net/images/20250421/1745222749_6805fc5df1cd7d1713f18.png!small)

## API 7【目录遍历获取敏感数据】Security misconfiguration（安全配置错误）

`/static`

设置静态目录的时候设置到了上一级，导致可以下源码或者下载二进制文件。

目录扫描，发现源码

![image](https://image.3001.net/images/20250421/1745222752_6805fc60e0f13de2af314.png!small)

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Content-Category, AccessToken, X-CSRF-Token, Authorization, Token, Content-Type
Access-Control-Allow-Methods: POST, GET, OPTIONS, PATCH, DELETE
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Category
Content-Type: text/html; charset=utf-8
Last-Modified: Mon, 31 Mar 2025 07:58:50 GMT
Date: Tue, 08 Apr 2025 08:37:44 GMT
Content-Length: 291
Connection: close

<pre>
<a href="api/">api/</a>
<a href="go.mod">go.mod</a>
<a href="go.sum">go.sum</a>
<a href="main.go">main.go</a>
<a href="owaspapitop10">owaspapitop10</a>
<a href="route.go">route.go</a>
<a href="sessions/">sessions/</a>
<a href="sql.db">sql.db</a>
<a href="swagger/">swagger/</a>
</pre>
```

![image](https://image.3001.net/images/20250421/1745222754_6805fc62c5b0e1ab64562.png!small)

```
GET /static/main.go HTTP/1.1
Host: 192.168.80.131:58084
User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Cookie: APIKit=APISecurity;
Content-Type: application/json
Accept: */*
Connection: close
```

```
HTTP/1.1 200 OK
Accept-Ranges: bytes
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Content-Category, AccessToken, X-CSRF-Token, Authorization, Token, Content-Type
Access-Control-Allow-Methods: POST, GET, OPTIONS, PATCH, DELETE
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Category
Content-Length: 2106
Content-Type: text/plain; charset=utf-8
Last-Modified: Thu, 10 Mar 2022 13:12:25 GMT
Date: Mon, 07 Apr 2025 14:01:11 GMT
Connection: close

package main

import (
	"fmt"
	"os"
	"os/signal"
	"owaspapitop1...