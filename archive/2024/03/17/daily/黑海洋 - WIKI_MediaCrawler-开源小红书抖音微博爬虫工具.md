---
title: MediaCrawler-开源小红书抖音微博爬虫工具
url: https://blog.upx8.com/4112
source: 黑海洋 - WIKI
date: 2024-03-17
fetch_date: 2025-10-04T12:09:57.414056
---

# MediaCrawler-开源小红书抖音微博爬虫工具

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# MediaCrawler-开源小红书抖音微博爬虫工具

发布时间:
2024-03-16

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
37253

## MediaCrawler是什么

MediaCrawler是一个在线开源的小红书抖音微博爬虫工具，支持目前能抓取小红书、抖音、快手、B站、微博的视频、图片、评论、点赞、转发等信息。工具原理是利用playwright搭桥，保留登录成功后的上下文浏览器环境，通过执行JS表达式获取一些加密参数 通过使用此方式，免去了复现核心加密JS代码，逆向难度大大降低，使用需要一定的技术知识。

## MediaCrawler功能列表

![](https://img.imgdd.com/f210f3.7e9e84a5-600a-4952-b464-41bb7e669931.png)

## MediaCrawler如何使用

### 创建并激活 python 虚拟环境

```
# 进入项目根目录
cd MediaCrawler

# 创建虚拟环境
python -m venv venv

# macos & linux 激活虚拟环境
source venv/bin/activate

# windows 激活虚拟环境
venv\Scripts\activate
```

### 安装依赖库

```
pip3 install -r requirements.txt
```

### 安装 playwright浏览器驱动

```
playwright install
```

### 运行爬虫程序

```
# 默认没有开启评论爬取模式，有需要请到配置文件中指定
# 从配置文件中读取关键词搜索相关的帖子并爬去帖子信息与评论
python main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
python main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例, 执行下面的命令查看
python main.py --help
```

### 数据保存

* 支持保存到关系型数据库（Mysql、PgSQL等）
* 支持保存到csv中（data/目录下）
* 支持保存到json中（data/目录下）

## 开源小红书抖音微博爬虫工具

源码备份：[国内网盘](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy83OGM1MmQ4ZDQzNjg)

GitHub：[https://github.com/NanmiCoder/MediaCrawler](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL05hbm1pQ29kZXIvTWVkaWFDcmF3bGVy)

1. ![我要](//q2.qlogo.cn/headimg_dl?dst_uin=1500276311&spec=100)

   **我要**

   2024-06-15 01:19:05

   [回复](https://blog.upx8.com/4112/comment-page-1?replyTo=29778#respond-post-4112)

   想要一个 fucaige888 我的微

[取消回复](https://blog.upx8.com/4112#respond-post-4112)

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