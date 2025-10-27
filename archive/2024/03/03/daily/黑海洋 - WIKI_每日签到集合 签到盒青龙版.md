---
title: 每日签到集合 签到盒青龙版
url: https://blog.upx8.com/4087
source: 黑海洋 - WIKI
date: 2024-03-03
fetch_date: 2025-10-04T12:08:12.601533
---

# 每日签到集合 签到盒青龙版

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 每日签到集合 签到盒青龙版

发布时间:
2024-03-02

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
42710

## 介绍

每日签到脚本，支持多账号使用，支持的网站众多

![](https://img.imgdd.com/f210f3.d4b8837f-65cb-43db-ab07-50d383c49db6.png)

##

## 支持的签到列表

支持列表：[https://sitoi.gitee.io/dailycheckin/](https://blog.upx8.com/go/aHR0cHM6Ly9zaXRvaS5naXRlZS5pby9kYWlseWNoZWNraW4v)

可以在各文件夹查看

#### 1.dailycheckin\_scripts：

该文件夹下是 [sitoi/dailycheckin](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NpdG9pL2RhaWx5Y2hlY2tpbg) 该项目的全部支持脚本

[配置方式查看](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3l1eGlhbjE1OC9jaGVjay9ibG9iL21hc3Rlci9kYWlseWNoZWNraW5fc2NyaXB0cy9SRUFETUUubWQ)

AcFun | 百度搜索资源平台 | Bilibili | 天翼云盘 | CSDN | 多看阅读 | 恩山论坛 | Fa米家 | 网易云游戏 | 葫芦侠 | 爱奇艺 | 全民K歌 | MEIZU 社区 | 芒果 TV | 小米运动 | 网易云音乐 | 一加手机社区官方论坛 | 哔咔漫画 | 吾爱破解 | 什么值得买 | 百度贴吧 | V2EX | 腾讯视频 | 微博 | 联通沃邮箱 | 哔咔网单 | 王者营地 | 有道云笔记 | 智友邦 | 机场签到 | 欢太商城 | NGA | 掘金 | GLaDOS | HiFiNi | 时光相册 | 联通营业厅

## 使用方法

**进入容器后运行以下命令**（docker exec -it ql bash）修改ql为你的青龙容器名字

以下命令全部都是进入容器后输入

### 1.拉取仓库

只使用dailycheckin\_scripts：

```
ql repo https://github.com/yuxian158/check.git "ck_" "" "checksend|utils"
```

只使用others\_scripts：

```
ql repo https://github.com/yuxian158/check.git "oc_" "" "checksend|utils"
```

我全都要:

```
ql repo https://github.com/yuxian158/check.git "ck_|oc_" "" "checksend|utils"
```

### 2.运行以下命令

旧版(青龙v2.12以下)

```
cd /ql/repo/yuxian158_check && python3 utils.py
```

新版

```
cd /ql/data/repo/yuxian158_check && python3 utils.py
```

然后不出意外的话你可以在青龙面板的配置文件下找到check.toml或check.json文件

然后根据各文件夹下REDEME修改配置[这里](https://blog.upx8.com/go/aHR0cHM6Ly9zaXRvaS5naXRlZS5pby9kYWlseWNoZWNraW4vc2V0dGluZ3Mv)

### 3.说明

1.本仓库在12.21日的更新中同时支持了json和toml两种格式的配置文件，但是推荐使用toml格式配置文件

2.当toml和json配置文件共存时优先使用toml文件

3.为避免未设置的签到项目推送，请禁止该签到任务，或注释掉配置文件中关于这个任务的配置项目

4.在运行修改运行时间后若出现未知错误

**请先确认database.sqlite.back或crontab.db.back是否存在**,然后

```
cd /ql/data/db/ && rm database.sqlite && cp database.sqlite.back database.sqlite #v2.12+
```

```
cd /ql/db/ && rm database.sqlite && cp database.sqlite.back database.sqlite #v2.11+
```

```
cd /ql/db/ && rm crontab.db && cp crontab.db.back crontab.db #v2.11-
```

### 4.**更新支持了多账号**

toml配置方式

```
[[ACFUN]]
password = "Sitoi"
phone = "188xxxxxxxx"

[[ACFUN]]
password = "123456"
phone = "135xxxxxxxx"
```

json配置方式

```
  "ACFUN" : [
    {
    "password": "Sitoi",
    "phone": "18888xxxxxx"
    },
{
"password": "多账号 密码填写，请参考上面",
"phone": "多账号 手机号填写，请参考上面"
}
],
```

### 5.通知配置

来自于青龙的config.sh

**在2022.4.10更新接入消息推送APP**

环境变量为设置别名的内容

```
export MI_PUSH_ALIAS="********"
```

## 其他

#### 1.关于 toml 的语法参考：

* [toml-lang/toml](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3RvbWwtbGFuZy90b21s)
* [中文知乎介绍](https://blog.upx8.com/go/aHR0cHM6Ly96aHVhbmxhbi56aGlodS5jb20vcC81MDQxMjQ4NQ)
* [TOML 教程中文版](https://blog.upx8.com/go/aHR0cHM6Ly90b21sLmlvL2NuL3YxLjAuMA)

#### 2.排错指引

1.在sitoi/dailycheckin的某次更新中修改了键名，请尽量删除原配置文件后重新配置

2.本库找配置文件时使用了正则表达式,在最外层配置时可以不区分大小写，且只要包含字段就可以，甚至可以写中文(强烈不建议这么写,貌似toml不支持)

3.很多脚本并没有测试

**github项目地址：[https://github.com/yuxian158/check](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3l1eGlhbjE1OC9jaGVjaw)**

1. ![Schumacher](https://gravatar.loli.net/avatar/avatar/8002bdb9001f7b925a7ab8a8c1037e6c?s=32&r=&d=)

   **Schumacher**

   2024-07-19 19:14:02

   [回复](https://blog.upx8.com/4087/comment-page-1?replyTo=29959#respond-post-4087)

   Кулинарный сайт волшебника правильных рецептов и здоровой пищи.
   Мясо: рецепты мясных блюд из свинины, говядины, курицы, баранины и дичи готовим с GoodwinFood.ru

[取消回复](https://blog.upx8.com/4087#respond-post-4087)

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