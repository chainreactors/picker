---
title: 一个轻量级Web蜜罐
url: https://blog.upx8.com/3319
source: 黑海洋 - WIKI
date: 2023-03-21
fetch_date: 2025-10-04T10:09:09.187306
---

# 一个轻量级Web蜜罐

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 一个轻量级Web蜜罐

发布时间:
2023-03-20

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
13724

# Loki

Releases下载：[https://github.com/TheKingOfDuck/Loki/releases/tag/0.2](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1RoZUtpbmdPZkR1Y2svTG9raS9yZWxlYXNlcy90YWcvMC4y)

## 更新日志

* 20220111 修改了获取部分字段的方式。
* 20210107 实现多端口监听
* 20210103 实现动态配置相关页面
* 20210124 实现配置指定端口指向指定模板文件
* 20210131 捕获所有数据，基本功能实现。修改默认页面。

## 技术栈

springboot + thymeleaf + sqlite

* 自定义注解
* 全局异常捕获，404捕获
* 多端口多页面
* 后台指定端口配置

### 使用

编辑application.yml修改默认后台,端口,账号密码等配置,然后执行`java -jar loki.jar`启动项目。

了解更多: [https://thekingofduck.github.io/post/loki-web-honeypot/](https://blog.upx8.com/go/aHR0cHM6Ly90aGVraW5nb2ZkdWNrLmdpdGh1Yi5pby9wb3N0L2xva2ktd2ViLWhvbmV5cG90Lw)

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
      loki@2333
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
  password: loki@2333                   #后台路径 http://HOST:ADMINPORT/ADMINPPATH
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

[![](https://github.com/TheKingOfDuck/Loki/raw/main/docs/images/admin1.png)](https://github.com/TheKingOfDuck/Loki/blob/main/docs/images/admin1.png)

[![](https://github.com/TheKingOfDuck/Loki/raw/main/docs/images/admin2.png)](https://github.com/TheKingOfDuck/Loki/blob/main/docs/images/admin2.png)

[![](https://github.com/TheKingOfDuck/Loki/raw/main/docs/images/tongda.jpg)](https://github.com/TheKingOfDuck/Loki/blob/main/docs/images/tongda.jpg)

[![](https://github.com/TheKingOfDuck/Loki/raw/main/docs/images/seeyon.jpg)](https://github.com/TheKingOfDuck/Loki/blob/main/docs/images/seeyon.jpg)

### 待处理

* 自定义报错

[取消回复](https://blog.upx8.com/3319#respond-post-3319)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")