---
title: 数字人直播 支持BiliBili和抖音直播（GPT vup-Live2D）
url: https://blog.upx8.com/3790
source: 黑海洋 - WIKI
date: 2023-08-18
fetch_date: 2025-10-04T11:59:46.120651
---

# 数字人直播 支持BiliBili和抖音直播（GPT vup-Live2D）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 数字人直播 支持BiliBili和抖音直播（GPT vup-Live2D）

发布时间:
2023-08-17

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
19800

## GPT-vup Live2D数字人直播

GPT-vup Live2D数字人直播是一款虚拟直播工具，支持BiliBili和抖音直播，基于生产者-消费者模型设计，使用了openai嵌入、GPT3.5 api，支持回答弹幕和SC、欢迎入场观众、感谢礼物等等，不过需要自行安装配置，非开箱即用，感兴趣的同学可以自行研究。

项目地址：https://github.com/jiran214/GPT-vup

## 安装方法

### 环境要求

* win 10
* python 3.8
* v屁嗯全局代理

### pip安装依赖

```
git clone https://github.com/jiran214/GPT-vup.git
cd src
# 建议命令行或者pycharm创建虚拟环境并激活 https://blog.csdn.net/xp178171640/article/details/115950985
python -m pip install --upgrade pip pip
pip install -r requirements.txt
```

### 新建config.ini

* 重命名config.sample.ini为config.ini
* 更改api\_key和proxy 其它可以不用管
* 相关配置见后

### 测试网络环境

* src目录下运行：>>`python manager.py test_net`

## 快速开始

### B站直播

* 安装依赖库：>>`pip install bilibili-api-python`
* config.ini 的 room -> id 更改为自己的房间号，可以先随便找个
* src目录下运行：>>`python manager.py run bilibili`

### 抖音直播

* 参考 [抖音弹幕抓取数据推送: 基于系统代理抓包打造的抖音弹幕服务推送程序](https://blog.upx8.com/go/aHR0cHM6Ly9naXRlZS5jb20vaGFvZG9uZzEwOC9keS1iYXJyYWdlLWdyYWIvdHJlZS9WMi42LjUvQmFycmFnZUdyYWI)
* 启动该项目
* 打开web或者桌面端抖音正在直播的直播间，数据开始抓取
* src目录下运行：>>`python manager.py run douyin`
* 教程：[https://www.bilibili.com/video/BV1nV4y1X7yJ?t=426.7](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuYmlsaWJpbGkuY29tL3ZpZGVvL0JWMW5WNHkxWDd5Sj90PTQyNi43)

## GPT-vup Live2D数字人直播地址

详细的使用可遇参考项目地址解说

GitHub地址：[https://github.com/jiran214/GPT-vup](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ppcmFuMjE0L0dQVC12dXA)

[取消回复](https://blog.upx8.com/3790#respond-post-3790)

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