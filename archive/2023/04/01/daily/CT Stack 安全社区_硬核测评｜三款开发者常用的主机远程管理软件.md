---
title: 硬核测评｜三款开发者常用的主机远程管理软件
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247496054&idx=2&sn=3a7d7f12a38dd8d7174bfcef11572ca3&chksm=e92ce5d5de5b6cc3ecb34fa1bbb185f8364a0f783a8740ae615cffbbc91f9b534ba2d83f42cd&scene=58&subscene=0#rd
source: CT Stack 安全社区
date: 2023-04-01
fetch_date: 2025-10-04T11:22:31.813923
---

# 硬核测评｜三款开发者常用的主机远程管理软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqov6SACYsynSPZryFEeCtSqkSVCFJVIMIp23FDfIfoPINB2RnA6T896vw/0?wx_fmt=jpeg)

# 硬核测评｜三款开发者常用的主机远程管理软件

侯晨

CT Stack 安全社区

# 01. 背景

作为一位开发者，长期以来对于家里有nas+多台主机+树莓派的我，想要ssh登到家里机器做点什么事情很繁琐，尤其没有公网IP的情况下更是繁琐。

最近发现长亭一款新的软件：牧云·主机管理助手。这款软件体验上比我之前的方案流畅很多。这里对我用过的几种方案做个对比，给有类似需求的人一个参考。

# 02. 方案对比

目前在用或用过的类似产品有：

* Visual studio code 的 remote tunnel 功能
* 开源的jumpserver 的跳板机
* 牧云·主机管理助手

先给没用过上面三个方案的师傅们大概介绍下前两个：

1. Vscode remote tunnel

> https://code.visualstudio.com/docs/remote/tunnels

Vscode server 新版自带的功能，工作逻辑大概是：在家里机器上启动 Vscode server，会和 https://vscode.dev 保持一个长连接。再通过 https://vscode.dev 连接到家里的机器，使用 Vscode 终端功能登录机器。

2. jumpserver

> https://github.com/jumpserver/jumpserver

是飞致云旗下的开源堡垒机，在自己家里机器上运行，使用ssh 协议、或自带的浏览器终端界面登录机器。必须有公网IP。此软件面向小型企业运维场景，配置和操作略复杂，日常运行有一定的维护成本。

# 03. 牧云·主机管理助手

牧云·主机管理助手入手门槛很低。主要功能：

| 打开产品首页：长亭百川云平台 > https://rivers.chaitin.cn  用微信扫码登录 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovnOwzvyTbT8WN9Mv2znmcfAicZsZdTkaOGSkVGmjKweu951jZZY94dRg/640?wx_fmt=png) |
| --- | --- |
| 进来之后，找到牧云·主机管理助手，点绑定主机 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovhdbdcs6vnU6EgVeOlzrFpYI9LN8IU0K9CrDDgNdInGIGvSsuJSvV8A/640?wx_fmt=png) |
| 复制生成的安装命令，在机器上安装，安装完成，机器就会在列表中展示 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovWwOkoiclcib0BDsAeq6soXIRiam6wy66zGLoicFFD5CRjYWGW77LgWZqaQ/640?wx_fmt=png) |
| 点击机器名称，可以看到机器的主要信息。这里的信息展示的也很合理。自带了负载监控、端口监控、docker 容器监控、进程监控 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqov8o5myeSECEFQibnq2YpGv0rrr5g3pP0ZPEn2tJ9rZu9HyiakYsCTwKMQ/640?wx_fmt=png) |
| 文件管理，可以在外网管理家里机器文件，有下载、上传功能。免费版的速度也不差，网速在3M/s，基本够用。收费版可以提速，费用也不贵（一台机器5分钱/天）。 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovQaCOvHTSZJH8NlojvmovMukGaTQNaN9zTaqIIHeoNNEAEgH5Cbe1VQ/640?wx_fmt=png) |
| 终端有常用的配色，暗色、亮色主题基本够用。终端使用比较流畅，和本地使用差异不大。 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovUfl6jULwMlORcqks3EOyJ7iapT2UrINqNDZuib7jWNjbrdyJQZkqibZJw/640?wx_fmt=png) |

价格：

| 5分钱/天的价格不算贵。添加了四台机器，每天2毛钱。基本没收费的感觉。 | ![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovcS5C766D7glpRNG0h7OqO4ickzjKS3kdyphBnsofSTHZRPzibLNEcH7w/640?wx_fmt=png) |
| --- | --- |

# 04. 三个方案对比

|  | Vscode server remote tunnel | 开源jumpserver | 牧云·主机管理助手 |
| --- | --- | --- | --- |
| 上手难度 | 🟢 容易 ，文档齐全，英文 | 🔴 需要配置，文档一般，中文 | 🟢 容易，文档齐全，中文 |
| 配置难度 | 🟢 简单配置 | 🔴 配置多 | 🟢 无配置 |
| 日常维护 | 🔴 需要，无法跟随系统启动 | 🔴 需要，架构复杂 | 🟢 不需要，安装过程完成随系统自动启动 |
| 多主机管理 | 🔴 不支持 | 🟢 支持 | 🟢 支持 |
| 多用户分享 | 🔴 不支持 | 🟢 支持 | 🟢 支持 |
| 网速流畅度 | 🔴 卡顿（需要代理到国外） | 🟢 流畅 | 🟢 流畅 |
| 安全性 | 🟢 安全 | 🔴 需要自己配置和维护证书 | 🟢 安全 |
| 文件管理 | 🟢 支持 | 🟢 支持 | 🟢 支持 |
| 需要公网IP | 🟢 不需要 | 🔴 需要 | 🟢 不需要 |
| 收费 | 🟢 不收费 | 🟢 不收费 | 🔴 收费，3台内免费，3台以上5分钱/天 |
| 面向人群 | 个人使用，有开发经验 | 企业级扩展性，丰富的运维经验 | 个人或小团体使用，不需要经验 |

# 05. 总结

在个人使用、有登录内网机器的场景，牧云·主机管理助手是目前综合体验最好的产品。项目目前还未开源，据官方介绍，计划等功能相对完善后，项目源码会开源到技术社区。

他们的官方交流群，有类似场景需求的师傅可以了解一下：

![](https://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpQAGsZsnM7Hpl8Qv7yqmqovXKWrzIuVzRiaY9ibwicYfLQVCZl5uuCiaEXK9GCtxA3WmNnKJBoiaibwghYg/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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