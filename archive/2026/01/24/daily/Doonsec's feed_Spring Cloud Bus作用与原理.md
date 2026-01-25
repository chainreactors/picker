---
title: Spring Cloud Bus作用与原理
url: https://mp.weixin.qq.com/s/xJMxtTnZkwUd1xNrecoLYw
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:13.037500
---

# Spring Cloud Bus作用与原理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKm9gicx0dWOiaMo9niaANEib34gTlAia5MN8rDnDJ6icDtDgicYkLXYxaUf1PQ/0?wx_fmt=jpeg)

# Spring Cloud Bus作用与原理

原创

静观云起
静观云起

码云精炼

![]()

在小说阅读器中沉浸阅读

Spring Cloud Bus是Spring Cloud生态中的一个分布式消息总线组件，主要用于**在微服务架构中实现配置变更的广播与通知，或者进行跨服务的事件通信。**

**一 主要作用**

**1. **动态刷新配置****

****当使用Spring Cloud Config做集中配置管理时，如果某个配置发生了变化，可以通过Spring Cloud Bus**将配置更新的指令广播到所有相关的微服务实例**，从而触发这些服务**自动刷新配置**，无需手动重启每个服务。常配合`/actuator/bus-refresh`端点使用，实现配置热更新****

****2. **事件广播与通信******

******除了配置刷新，也可以用来在微服务集群中**广播自定义事件**，实现服务间的轻量级事件驱动通信******

****二 核心原理****

基于消息中间件(如RabbitMQ、Kafka)实现消息的广播。

当某个服务节点触发配置更新(比如调用bus-refresh)，该事件会通过消息总线发送到所有连接到总线的服务，收到事件的服务会执行相应的逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKZCF3FffJKq1pXFNgOsuG5nWZK5ovInIAWNrzzfgnZA3bFJ4PUe0SHw/640?wx_fmt=png&from=appmsg)

三 实时配置刷新

1. 客户端发起通知

借助**Spring Cloud Bus**‌的广播功能，让**Config Client‌都订阅配置更新事件。当配置更新时，触发其中一个端的更新事件，Spring Cloud Bus就把此事件广播到其他订阅客户端，以此来达到批量更新。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKGp4dH1L1GL3mdf3ic9W09wXnJ5zUkcIZNwPuqdusBJ3ErH0vYxDRoCA/640?wx_fmt=png&from=appmsg)

```
<!-- spring cloud starter bus amqp依赖，默认用rabbitmq --><dependency>    <groupId>org.springframework.cloud</groupId>    <artifactId>spring-cloud-starter-bus-amqp</artifactId></dependency>
```

添加配置文件

```
# 消息队列 rabbitmq:host: 192.168.10.101port: 5672username: guestpassword: guestvirtual-host: /# 度量指标监控与健康检查management:  endpoints:    web:      # 访问端点根路径，默认为/actuator      base-path: /actuator          exposure:        # 需要开启的端点        include: bus-refresh
```

### 客户端发起通知缺陷

********✅********打破了微服务的职责单一性。微服务本身是业务模块，它本不应该承担配置刷新的职责。

********✅********破坏了微服务各节点的对等性。

********✅********存在一定的局限性。例如，微服务在迁移时，它的网络地址常常会发生变化，此时如果想要做到自动刷新，就不得不修改Webhook的配置

2. 服务端发起通知

为了解决客户端发起通知的缺陷，采用服务端发起通知

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKmPxyuq6lsicMk0mlEsydZ2fF2fxicGbhibXNVooJLy761dtmuaiakqxnicA/640?wx_fmt=png&from=appmsg)

********✅********Webhook监听被触发，给ConfigServer发送bus-refresh请求刷新配置。

********✅********ConfigServer发送消息给Bus。

********✅********Bus接收消息后广播通知所有ConfigClient。

********✅********各ConfigClient收到消息重新读取最新配置。

3.局部刷新

假设有这样一种场景，我们开发了一个新的功能，此时需要对该功能进行测试。我们只希望其中一个微服务的配置被更新，等功能测试完毕，正式部署线上时再更新至整个集群。但是由于所有微服务都受Spring Cloud Bus的控制，我们更新了其中一个微服务的配置，就会导致其他服务也被通知去更新配置。这时候局部刷新的作用就体现出来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnLT9yZszIwTLHia1m6mRuHKpfwwMeOiarfwbF4EibCukvzLibACSssH2JtmBTeJSQD94ibUGa6BgRCrXg/640?wx_fmt=png&from=appmsg)

********✅********刷新单个指点微服务

请求地址：/bus-refresh/{微服务名}:{端口号}

请求方式：post

********✅********刷新指定集群

假设现在功能测试完毕，需要正式部署线上更新至整个集群。但是由于Spring Cloud Bus控制着多个微服务集群(订单微服务、商品微服务等)，而我们只想更新指定集群下的配置，这个时候就可以使用Bus提供的通配符更新方案。

****请求地址：/bus-refresh/{微服务名}:\*\*

请求方式：post

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1Bibfnia4huCODlTdyh6PTbL1pic45RaY9PANbJVIia0XOz1gV28f9BHd4341P1lpqQwn0cRGBjHPbHYmYIQ/640?wx_fmt=jpeg&from=appmsg)****

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

码云精炼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

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