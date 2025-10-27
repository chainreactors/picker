---
title: 宝塔面板第三方云端（宝塔破解版）
url: https://blog.upx8.com/3112
source: 黑海洋 - WIKI
date: 2022-11-23
fetch_date: 2025-10-03T23:30:11.933842
---

# 宝塔面板第三方云端（宝塔破解版）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 宝塔面板第三方云端（宝塔破解版）

发布时间:
2022-11-22

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
26026

# 宝塔面板第三方云端

这是一个用php开发的宝塔面板第三方云端站点程序。

你可以使用此程序搭建属于自己的宝塔面板第三方云端，实现最新版宝塔面板私有化部署，不与宝塔官方接口通信，满足隐私安全合规需求。同时还可以去除面板强制绑定账号，DIY面板功能等。

网站后台管理可一键同步宝塔官方的插件列表与增量更新插件包，还有云端使用记录、IP黑白名单、操作日志、定时任务等功能。

本项目自带的宝塔安装包和更新包是7.9.5最新版，已修改适配此第三方云端，并且全开源，无so等加密文件。

觉得该项目不错的可以给个Star~

## 声明

1.此项目只能以自用为目的，不得侵犯堡塔公司及其他第三方的知识产权和其他合法权利。

2.搭建使用此项目必须有一定的编程和Linux运维基础，纯小白不建议使用。

## 环境要求

* `PHP` >= 7.4
* `MySQL` >= 5.6
* `fileinfo`扩展
* `ZipArchive`扩展

## 成品脚本

* **脚本安装**：[https://dk.upx8.com/download](https://blog.upx8.com/go/aHR0cHM6Ly9kay51cHg4LmNvbS9kb3dubG9hZA)

## 部署方法

* **下载最新版的Release包**：[https://github.com/flucont/btcloud/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZsdWNvbnQvYnRjbG91ZC9yZWxlYXNlcw)
* GitHub：[https://github.com/flucont/btcloud](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZsdWNvbnQvYnRjbG91ZA)
* 如果是下载的源码包，需要执行 `composer install --no-dev` 安装依赖，如果是下载的Release包，则不需要
* 设置网站运行目录为`public`
* 设置伪静态为`ThinkPHP`
* 访问网站，会自动跳转到安装页面，根据提示安装完成

## 使用方法

* 在`批量替换工具`，执行页面显示的命令，可将bt安装包、更新包和脚本文件里面的`http://www.example.com`批量替换成当前网站的网址。
* 在`系统基本设置`修改宝塔面板接口设置。你需要准备一个使用官方最新脚本安装并绑定账号的宝塔面板，用于获取最新插件列表及插件包。并根据界面提示安装好专用插件。
* 在`定时任务设置`执行所显示的命令从宝塔官方获取最新的插件列表并批量下载插件包（增量更新）。当然你也可以去插件列表，一个一个点击下载。
* 访问网站`/download`查看使用此第三方云端的一键安装脚本。

## 其他

* [Linux面板官方更新包修改记录](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZsdWNvbnQvYnRjbG91ZC9ibG9iL21haW4vd2lraS91cGRhdGUubWQ)
* [Windows面板官方更新包修改记录](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZsdWNvbnQvYnRjbG91ZC9ibG9iL21haW4vd2lraS91cGRhdGV3aW4ubWQ)
* 宝塔面板官方版与此第三方云端版对比：

  |  | 官方版 | 此第三方云端版 |
  | --- | --- | --- |
  | 版本更新 | 支持 | 支持 |
  | 面板广告 | 有广告 | 无广告 |
  | 是否全开源 | 没有全开源 | 全开源 |
  | 资源占用 | 各种统计上报等任务，资源占用略高 | 去除了很多无用的定时任务，资源占较少 |
  | 兼容性 | 由于编译的so文件有系统架构限制，兼容的系统仅限已编译的so对应的系统架构 | 由于全开源，没有已编译的so文件，因此无系统架构限制 |

[取消回复](https://blog.upx8.com/3112#respond-post-3112)

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