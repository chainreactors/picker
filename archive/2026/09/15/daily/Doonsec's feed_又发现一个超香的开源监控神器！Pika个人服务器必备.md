---
title: 又发现一个超香的开源监控神器！Pika个人服务器必备
url: https://mp.weixin.qq.com/s/Ph6GO2y6H1a3mJWpYeapow
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:47.690714
---

# 又发现一个超香的开源监控神器！Pika个人服务器必备

# 又发现一个超香的开源监控神器！Pika个人服务器必备

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

开源神器预计阅读 4 分钟 · 共 1307 字

又发现一个超香的开源监控神器！Pika个人服务器必备

轻量 · 干净 · 部署简单

#Go#VictoriaMetrics#Docker

READING PATH

阅读路线

3 个章节

01

核心功能一览

-

02

超简单部署方法

-

03

为什么推荐它？

最近又挖到一个真正实用的开源监控项目——Pika。它用 Go 写的，轻量、干净、部署简单，支持`SQLite`和`PostgreSQL`，时序数据直接丢给`VictoriaMetrics`。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyQe3TsN6Bf9ek2kqaeMQ72EicGOkMpO6rxtxeJEdhuWoUwYQVTKcKnORdxVol6v5PBkMV7iaJGVMWXpDdxALveQGicsNOQ4oYK3k/640?wx_fmt=png&from=appmsg)

CHAPTER 01

**01****🛠️ 核心功能一览**CORE FEATURES

实时性能监控服务存活检查文件防篡改安全风险审计多种登录一键部署

01

📊 实时性能监控

CPU、内存、磁盘、网络、GPU、温度，支持历史趋势回溯。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwzM03STXkkib4PRbuum8r1QERmhNJc4mCjMtH6qJMSIgHqEZ2DXddpBTPg02oYIfFR2USaJ0EzWYdc4icMdPbDHYgbFue8ZMJBc/640?wx_fmt=png&from=appmsg)

02

🔍 服务存活检查

HTTP、TCP、ICMP 多协议探测，自动检测 **SSL 证书过期**。

03

🛡️ Linux 文件防篡改

实时监控关键目录，属性巡检 + 告警 双重保障。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyo2pTZibm6tz1V7t2Jnc4fm4O0wIt8ic3l6ucqbROVsPA03iavbIs8VAWGVfREOU269dKrNp1KpTFPtPGpYKqVhmUpE68t97nPSQ/640?wx_fmt=png&from=appmsg)

04

🔒 资产清单 + 安全风险审计

自动收集资产并按风险等级分级：`Critical` / `High` / `Medium` / `Low`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfw8zmZyNXdKlj2xgBPrqdxH4Wq7atKyPSbwl5zFwpcqbVjucMy5SQpHWrYO9L2U916TbZjvCodE9IVicsPVJMMh8C2zDj7Q6xSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxYdAu2FKSz25iaBlIW27qwmgNLvFdz60Iicy2a4TcGRXBXjsVa0kficxYEf82utvrpTic2gbiagibUk4wcBILkyUmj52uvIsgJVKoqA/640?wx_fmt=png&from=appmsg)

05

🔐 多种登录方式

Basic Auth、OIDC、GitHub OAuth 三种认证方案。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfweOtjCcPnAdrQtX10E0LJxBazfYrdCC4mW6gfmHRH0Lky8Kh55libicmzj28Jhv76zoTK5lgRUpCicfSvdOmRen7S3OvusmUMEOc/640?wx_fmt=png&from=appmsg)

06

📦 Docker Compose 一键部署

资源占用极低，个人服务器、小型项目、轻量运维，用它刚刚好。

CHAPTER 02

**02****🚀 超简单部署方法**复制粘贴就能跑

DEPLOY

SQLite 版部署流程

推荐个人 / 小项目使用

1

下载配置

curl 拉取 docker-compose 与 config 文件

2

改密钥

修改 config.yaml 中的 JWT Secret 和管理员密码

3

启动服务

docker compose up -d 一键拉起

4

访问面板

http://localhost:8080，默认 admin / admin123

bash

# 下载配置文件

curl -O https://raw.githubusercontent.com/dushixiang/pika/main/docker-compose.sqlite.yml

curl -o config.yaml https://raw.githubusercontent.com/dushixiang/pika/main/config.sqlite.yaml

# 重要：修改 config.yaml 里的 JWT Secret 和管理员密码

# 然后启动

docker compose -f docker-compose.sqlite.yml up -d

访问：`http://localhost:8080`

默认账号：`admin` / `admin123`

DEPLOY

PostgreSQL 版部署流程

数据量大了再切

1

下载配置

curl 拉取 postgresql 版 compose 与 config

2

改密钥

修改数据库密码、JWT Secret 和管理员密码

3

启动服务

docker compose up -d 拉起完整栈

bash

# 下载配置文件

curl -O https://raw.githubusercontent.com/dushixiang/pika/main/docker-compose.postgresql.yml

curl -o config.yaml https://raw.githubusercontent.com/dushixiang/pika/main/config.postgresql.yaml

# 同样记得修改数据库密码、JWT Secret 和管理员密码

docker compose -f docker-compose.postgresql.yml up -d

两种方式都支持，前期用 SQLite 随便玩，后期无缝升级 PostgreSQL。

CHAPTER 03

**03****💡 为什么推荐它？**WHY PIKA

BEFORE

传统方案

市面上监控方案要么太重（Prometheus + Grafana），要么功能单一，个人服务器用起来总是大材小用或不够用。

AFTER

Pika

Pika 刚好卡在中间：**够用、轻量、还带安全能力**。文件防篡改 + 安全审计这两点，对个人服务器尤其实用。

一个面板全搞定，个人服务器监控的甜蜜点

GITHUB

想自己搭一个干净好用的监控面板？

立即复制下方代码

**GitHub 地址**：`https://github.com/dushixiang/pika`

已经开源，文档清晰，持续更新中。直接冲就完事了。

觉得有用的话，记得给作者点个 Star ⭐

也欢迎转发给需要的朋友～ 💚

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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