---
title: 一个请求头引出的 API 未授权
url: https://mp.weixin.qq.com/s/JHM1v1EZaYpiUG6ISC2-YA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:42:49.169491
---

# 一个请求头引出的 API 未授权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlQsNGAp0iaOILkGRgiaXnjGydsot6fF3THawkvDmyXkXzV9ht7Hy9q1lea9qSEztp7od5luL52d1pPUBjO307HRz1U2aTgPjsO0/0?wx_fmt=jpeg)

# 一个请求头引出的 API 未授权

原创

进击的hack
进击的hack

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 905，阅读大约需 5 分钟

## 前言

做项目时遇到的一个漏洞。

在日常 Web 安全测试中，Spring Boot Actuator 一直都是重点关注对象。

通常情况下，我们都会先枚举一些常见的 Actuator 路径，例如：

```
/actuator
/actuator/env
/actuator/heapdump
/actuator/mappings
/actuator/beans
/actuator/metrics
```

如果全部返回 **404**，很多测试人员便会认为目标没有开启 Actuator，继续测试其他内容。

然而，在一次项目测试过程中，我发现目标网站所有 Actuator 路径均返回 404，但最终仍然成功发现了多个未授权的 Actuator 接口。

整个过程并不是依赖特殊漏洞，而是由于 **不同业务入口对应不同微服务** 所导致。

## 演示图

不同业务入口（PC/H5）导致的路由隔离失效，从而暴露了管理端点。

```
www.example.com
        │
        ▼
     Gateway
        │
  判断请求头
        │
 ┌──────┴────────┐
 │               │
PC(默认)       Mobile
 │               │
PC微服务      H5微服务
```

默认访问 `GET /actuator/env`实际上到了`pc-service`。因为`pc-service`根本没有`/actuator`所以返回 404

但是增加`x-id-finger: mobile`以后 Gateway 改变了路由：

```
GET /actuator/env
          │
          ▼
     mobile-service
```

而`mobile-service`开启了

```
management.endpoints.web.exposure.include=*
```

于是

```
/actuator/env
/actuator/heapdump
/actuator/mappings
/actuator/loggers
```

全部暴露出来了。
Header 将请求路由到了另一个暴露了 Actuator 的后端服务

## 测试过程

正常访问网站，默认是走 PC，不管是直接扫描、枚举 actuator 常见接口，都是 404

```
POST /actuator HTTP/1.1
Content-Type: application/json
Host: www.example.com

{"key": "value"}
```

但是通过枚举子路径，在该网站下发现了一个 H5 页面，给 APP 用的

```
https://www.example.com/xx-h5/#/
```

通过该网站请求，网站为了避免和 PC 端的微服务冲突，H5 发送的请求中添加了请求头

```
x-id-finger: mobile
```

构造如下请求

```
POST /actuator HTTP/1.1
Content-Type: application/json
Host: www.example.com
x-id-finger: mobile

{"key": "value"}
```

再对接口进行枚举，就能成功发现 actuator 常见的未授权接口，比如 heapdump、env、mappings ……

## 如何发现

首先寻找：

```
H5 页面
APP 页面
微信小程序
开放平台
```

然后抓取它们所有请求。
重点观察：

```
Header
Cookie
Token
Host
Path Prefix
```

例如：

```
x-id-finger
x-platform
x-device
clientType
terminal
app-version
channel
x-client
x-source
```

有时网关都会根据这些 Header 做路由。
一旦找到类似 Header，就可以重新测试：

```
/actuator/*
```

很多隐藏接口就是这样发现的。

# 防御建议

针对类似问题，可以从两个层面进行修复。

**网关层：**

* • 不应仅依据客户端可控 Header 决定敏感路由。
* • 对 `/actuator/**` 等管理路径进行统一拦截。
* • 将管理接口与业务接口彻底隔离。

**应用层：**

* • 不对公网暴露 Actuator。
* • 仅开放必要端点，例如：

```
health
info
```

* • 对管理接口启用身份认证与授权。
* • 使用独立管理端口，仅允许内网访问。
* • 禁止暴露 `heapdump`、`env`、`mappings` 等高风险端点。

## 总结

这次测试最大的收获并不是发现了 Actuator，而是验证了一个容易被忽略的测试思路：

> **404 并不一定意味着接口不存在，也可能意味着你访问的是错误的后端服务。**

在微服务架构下，同一域名可能对应多套后端，不同终端（PC、H5、APP、小程序）仅通过 Header、Cookie 或路径进行路由。如果只测试默认入口，往往只能看到整个系统的一部分攻击面。

因此，在进行安全测试时，不妨多关注不同业务入口之间的差异，分析它们的请求特征，再结合常见敏感接口进行验证，往往能够发现那些隐藏在不同路由后的真实攻击面。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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