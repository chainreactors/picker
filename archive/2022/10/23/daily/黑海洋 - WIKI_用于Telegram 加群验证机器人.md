---
title: 用于Telegram 加群验证机器人
url: https://blog.upx8.com/3053
source: 黑海洋 - WIKI
date: 2022-10-23
fetch_date: 2025-10-03T20:41:29.099643
---

# 用于Telegram 加群验证机器人

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 用于Telegram 加群验证机器人

发布时间:
2022-10-22

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
39662

## captcha-bot

用于[Telegram](https://blog.upx8.com/go/aHR0cHM6Ly90ZWxlZ3JhbS5vcmcv) 加群验证机器人，采用golang编写，支持全平台编译运行。

[![license MIT](https://camo.githubusercontent.com/2bb630e2707a04100cd270fd944d22816241c37b68a5a1629257920c65e17891/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c7565)](https://blog.upx8.com/go/aHR0cHM6Ly9vcGVuc291cmNlLm9yZy9saWNlbnNlcy9NSVQ) [![Go version 1.17](https://camo.githubusercontent.com/6041c7736246bb56402865c68b3c544f4714929149936cb5e7c23857b8c69b86/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f6c616e672d312e31372d726564)](https://blog.upx8.com/go/aHR0cHM6Ly9nb2xhbmcub3JnLw) [![telebot v3](https://camo.githubusercontent.com/f9edc9d032aae13f5aea11a112fb5bd4160c879e2a2201e724af062b64160213/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c65626f74204672616d65776f726b2d76332d6c6967687467726579)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R1Y25hay90ZWxlYm90) [![version 1.0.0](https://camo.githubusercontent.com/351b77a6573f7d124ef052b45cb37a57f5ea23d09f2b8591c76818df8129843a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d312e302e302d677265656e)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2Fzc2ltb24vY2FwdGNoYS1ib3QvcmVsZWFzZXMvdGFnLzEuMC4w)

## 项目初衷

`Telegram`(简称：小飞机)，全球知名的非常方便且优雅的匿名IM工具(比微信更伟大的产品)。
但由于该软件的匿名性，导致该软件上各种加群推广机器人满天飞，我们无法无时无刻的判断加入群组的“某个人”是否为推广机器人。
还好`Telegram`为我们提供了非常强大的`Api`，我们可以利用这些Api开发出自动验证的机器人。

如果你是`Telegram`的群组管理员，你可以直接使用本项目部署私有化的验证机器人。
如果你是`开发者`，你可以利用本项目熟悉`Go语言`与`Telegram`的交互式开发，以便后续利用`Api`开发出自己的机器人！

文档参考：
Telegram Api文档：[Telegram Api](https://blog.upx8.com/go/aHR0cHM6Ly9jb3JlLnRlbGVncmFtLm9yZy9ib3RzL2FwaQ)
机器人开发框架：[Telebot](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3R1Y25hay90ZWxlYm90)

## 使用方式

### 一、自行编译

此安装方式多用于开发者，需电脑上安装`go语言`环境。
[go语言官网](https://blog.upx8.com/go/aHR0cHM6Ly9nb2xhbmcub3JnLw)

下载：

```
# 下载项目
git clone https://github.com/assimon/captcha-bot && cd captcha-bot
```

编译：

```
# 编译
go build -o  captcha-bot
# 给予执行权限
chmod +x ./captcha-bot
```

配置：

```
cp .example.config.toml config.toml
```

执行：

```
# 调试启动
./captcha-bot
# nohup
nohup ./captcha-bot >> run.log 2>&1 &
```

### 二、下载已经编译好的二进制程序

此方式可以直接使用，用于服务器生产环境。 进入打包好的版本列表，下载程序：[https://github.com/assimon/captcha-bot/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2Fzc2ltb24vY2FwdGNoYS1ib3QvcmVsZWFzZXM)
配置：

```
cp .example.config.toml config.toml
```

运行：

```
# linux
# 调试启动
./captcha-bot

# windows
captcha-bot.exe
```

### 三、机器人命令

```
/ping       #存活检测，机器人若正常将返回"pong"
# 广告相关
/add_ad     #新增一条广告，格式：广告标题|跳转链接|到期时间(带时分秒)|权重(倒序，值越大越靠前)，例如：/add_ad
```

1. ![星辰](https://gravatar.loli.net/avatar/avatar/28b57d1b6b0a802749a75fe451f51a1c?s=32&r=&d=)

   **星辰**

   2024-02-20 07:31:49

   [回复](https://blog.upx8.com/3053/comment-page-1?replyTo=28941#respond-post-3053)

   不会弄
2. ![db](//q2.qlogo.cn/headimg_dl?dst_uin=2656767341&spec=100)

   **db**

   2022-11-20 00:15:32

   [回复](https://blog.upx8.com/3053/comment-page-1?replyTo=26737#respond-post-3053)

   苹果怎么下载

[取消回复](https://blog.upx8.com/3053#respond-post-3053)

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