---
title: Rabbitmq 配置开发 测试不同环境
url: https://blog.upx8.com/3376
source: 黑海洋 - WIKI
date: 2023-03-30
fetch_date: 2025-10-04T11:07:49.556722
---

# Rabbitmq 配置开发 测试不同环境

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Rabbitmq 配置开发 测试不同环境

发布时间:
2023-03-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
13252

## 1.vhost 介绍

每一个RabbitMQ服务器都能创建虚拟消息服务器，我们称之为虚拟主机。每一个vhost本质上是一个mini版的RabbitMQ服务器，拥有自己的交换机、队列、绑定等，拥有自己的权限机制。

vhost之于Rabbit就像虚拟机之于物理机一样。他们通过在各个实例间提供逻辑上分离，允许为不同的应用程序安全保密的运行数据，这很有，它既能将同一个Rabbit的众多客户区分开来，又可以避免队列和交换器的命名冲突。

RabbitMQ提供了开箱即用的默认的虚拟主机“/”，如果不需要多个vhost可以直接使用这个默认的vhost，通过使用缺省的guest用户名和guest密码来访问默认的vhost。

vhost之间是相互独立的，这避免了各种命名的冲突，就像App中的沙盒的概念一样，每个沙盒是相互独立的，且只能访问自己的沙盒，以保证非法访问别的沙盒带来的安全隐患。

## 2.vhost 创建 删除

bash

```
RabbitMq 安装路径 ./sbin 目录中的rabbitmqctl工具来创建,如果是docker直接进入容器即可
# 创建vhost,用来区分不同环境的队列
rabbitmqctl add_vhost [vhost_name]
# 删除vhost
rabbitmqctl delete_vhost [vhost_name]
# 查看
rabbitmqctl list_vhosts
# 配置最大连接限制，0：表示不可用，-1：无限制
rabbitmqctl set_vhost_limits -p vhost_name '{"max-connections": 256}'
# 配置队列最大数，-1：无限制
rabbitmqctl set_vhost_limits -p vhost_name '{"max-queues": 1024}'
```

## 3.vhost 授权

bash

```
# 创建账号
rabbitmqctl add_user root root123456
# 设置用户角色
rabbitmqctl set_user_tags root administrator
# 设置用户权限
rabbitmqctl set_permissions -p [vhost_name] root ".*" ".*" ".*"
```

## 4.vhost 配置

bash

```
# Spring
spring:
  # rabbitmq
  rabbitmq:
    host: 192.168.6.1
    # rabbitmq的端口
    port: 5672
    # rabbitmq的用户名
    username: root
    # rabbitmq的用户密码
    password: root123456
    # 虚拟主机，用来区分不同环境的队列
    virtual-host: dev
    #开启重试机制
    listener:
      retry:
        enabled: true
        #重试次数，默认为3次
        max-attempts: 3
```

[取消回复](https://blog.upx8.com/3376#respond-post-3376)

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