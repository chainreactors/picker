---
title: 使用Telegram机器人推送网站报警信息
url: https://blog.upx8.com/3059
source: 黑海洋 - WIKI
date: 2022-10-29
fetch_date: 2025-10-03T21:14:20.779911
---

# 使用Telegram机器人推送网站报警信息

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 使用Telegram机器人推送网站报警信息

发布时间:
2022-10-28

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
11904

网站挂了怎么办？有办法实时监控吗？ 一些有时效性的信息我需要第一时间获取他们的信息。 之前一直是在服务器上用脚本监控这些信息，并使用server酱推送到微信的。 这样我就能实时获取到我想要的信息。 可是，前段时间server酱突然被失效，导致网站挂了，我也没能第一时间发现。 于是乎，就想用telegram机器人来代替server酱，再也没有被封的风险 不得不说，telegram的机器人如此强大，各种功能面面俱到

## 创建一个telegram机器人

> 参考官方API:[https://core.telegram.org/bots/api](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTlqYjNKbExuUmxiR1ZuY21GdExtOXlaeTlpYjNSekwyRndhUT09)

1. 找官方机器人之父([@BotFather](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTkwTG0xbEwwSnZkRVpoZEdobGNnPT0))领养一只。 发送`newbot`,按照提示发送机器人昵称，id创建。并可以设置机器人头像，简介等
2. 测试机器人 网页打开:`https://api.telegram.org/bot你的TOKEN/getMe` 成功的话会返回机器人信息

## 简单的发送消息

1. 直接打开网页 [https://api.telegram.org/bot机器人TOKEN/sendMessage?chat\_id=chat\_id&text=发送的消息](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTloY0drdWRHVnNaV2R5WVcwdWIzSm5MMkp2ZEE9PQ)

## 其他

1. sendMessage方法可以发送MarkDown语法以及HTML，具体查看文档：[https://core.telegram.org/bots/api](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTlqYjNKbExuUmxiR1ZuY21GdExtOXlaeTlpYjNSekwyRndhUT09)
2. 可以发送照片视频等等，有一系列有意思的玩法
3. chat\_id这个，可以添加([@userinfobot](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTkwTG0xbEwzVnpaWEpwYm1adlltOTA)) 机器人查看个人id，如果需要群组ID自行百度。
4. [https://github.com/python-telegram-bot/python-telegram-bot/issues/370](https://blog.upx8.com/go/aHR0cHM6Ly9saWFvYnUuZGUvZ28vYUhSMGNITTZMeTluYVhSb2RXSXVZMjl0TDNCNWRHaHZiaTEwWld4bFozSmhiUzFpYjNRdmNIbDBhRzl1TFhSbGJHVm5jbUZ0TFdKdmRDOXBjM04xWlhNdk16Y3c)

[取消回复](https://blog.upx8.com/3059#respond-post-3059)

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