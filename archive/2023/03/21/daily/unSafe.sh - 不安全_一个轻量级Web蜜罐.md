---
title: 一个轻量级Web蜜罐
url: https://buaq.net/go-154412.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:15.234861
---

# 一个轻量级Web蜜罐

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

一个轻量级Web蜜罐

server: port: 80 #多端口配置 multiPorts: 81-90,7000-10000,65535 ssl: enabled: false
*2023-3-20 23:43:33
Author: [blog.upx8.com(查看原文)](/jump-154412.htm)
阅读量:60
收藏*

---

```
server:
  port: 80
  #多端口配置
  multiPorts: 81-90,7000-10000,65535
  ssl:
    enabled:
      false                             #SSL协议配置开开关
    key-store:
      loki.keystore
    key-alias:
      loki
    key-store-password:
      [email protected]
    key-store-type:
      JKS

spring:
  #出现错误时, 直接抛出异常(便于异常统一处理，否则捕获不到404)
  mvc:
    throw-exception-if-no-handler-found: true
    static-path-pattern: /**

  web:
    resources:
      add-mappings: false
  datasource:
    url: jdbc:sqlite:data/loki.db # 创建的sqlite数据库所在路径
    username: # 因为没有用户名和密码，所以这两个参数就没有值
    password:
    driver-class-name: org.sqlite.JDBC # sqlite驱动
  thymeleaf:
    prefix: classpath:/templates/

# mybatis配置
mybatis:
  mapper-locations: classpath:mybatis/mapper/*Mapper.xml # 配置mapper.xml文件路径
  type-aliases-package: net.thekingofduck.loki.entity # 实体类包名

loki:
  adminPath: lokiadmin                  #后台路径 http://HOST:ADMINPORT/ADMINPPATH
  adminPort: 65535                      #后台端口 这个端口如果不在上面的端口列表里则后台无法访问
  username: loki                        #后台路径 http://HOST:ADMINPORT/ADMINPPATH
  password: [email protected]                   #后台路径 http://HOST:ADMINPORT/ADMINPPATH
  templates: /resources/templates/      #模板渲染的路径 在jar包同级目录
  statics: /resources/statics/          #模板静态资源(images,js,css)的路径 在jar包同级目录

templates:
  list:
    default:
      - maps: {
        port: '80',
        path: 'default/index.html',
        code: '200',
        header: {
          X-Powered-By: "PHP/5.4.7",
          Server: "phpstudy"
        },
        respbody: 'error',
      }
    tongda:
      - maps: {
        port: '8080',
        path: 'tongda/index.html',
        code: '200',
        header: {
          Set-Cookie: "phpsession=123",
          Server: "apache"
        },
        respbody: 'error',
      }
    seeyon:
      - maps: {
        port: '8090',
        path: 'seeyon/index.html',
        code: '200',
        header: {
          Set-Cookie: "jsessionid=123",
          Server: "nginx"
        },
        respbody: 'error',
      }
```

文章来源: https://blog.upx8.com/3319
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)