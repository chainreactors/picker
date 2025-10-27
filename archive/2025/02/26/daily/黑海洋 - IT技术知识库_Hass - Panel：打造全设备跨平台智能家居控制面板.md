---
title: Hass - Panel：打造全设备跨平台智能家居控制面板
url: https://blog.upx8.com/4699
source: 黑海洋 - IT技术知识库
date: 2025-02-26
fetch_date: 2025-10-06T20:36:55.438237
---

# Hass - Panel：打造全设备跨平台智能家居控制面板

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Hass - Panel：打造全设备跨平台智能家居控制面板

发布时间:
2025-02-25

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
49220

## Hass-Panel介绍

Hass-Panel是一款基于React开发的智能家居控制面板，深度集成Home Assistant的Websocket API，支持作为HAOS插件部署，提供灯光、空调、窗帘、传感器、摄像头（WebRTC/ONVIF/RTSP协议）及用电量统计等全屋设备控制功能。该面板采用响应式设计，适配移动端与桌面端，支持PWA安装及暗色模式切换，内置多用户管理系统与JWT认证机制，保障数据安全。从v1.3.2版本起，系统通过SQLite数据库实现配置存储，优化初始化流程与摄像头地址配置要求，并强化密码加密存储机制。开发者可自由拖拽布局界面，灵活扩展设备支持类型，满足智能家居场景化控制需求，适用于家庭自动化与物联网设备集中管理场景。

## Hass-Panel界面截图

![](https://i0.wp.com/cdn.skyimg.de/up/2025/2/25/zjb4a4.webp)

## Hass-Panel主要特性

* 📱 响应式设计，支持移动端和桌面端
* 🔧 高度可配置，自由拖拽布局
* 🚀 PWA支持，可安装到桌面
* 🎨 美观的用户界面，支持暗色模式
* 👥 多用户管理系统，支持JWT认证
* 🔐 安全的密码加密存储
* 🎥 强大的摄像头支持，包括WebRTC/ONVIF/RTSP
* 🔌 丰富的设备支持:
  + 灯光控制
  + 空调控制
  + 窗帘控制
  + 传感器监控
  + 摄像头查看
  + 场景控制
  + 用电量统计
  + 插座控制
  + 更多设备支持中…

## Hass-Panel如何使用/部署

### 重要提示

从 v1.3.2 版本开始:

* 系统使用 SQLite 数据库进行配置存储
* 首次使用需要完成系统初始化流程
* 摄像头功能需要正确配置 ONVIF/RTSP 地址

### Docker方式 正式版

```
docker run \
  --name hass-panel \
  --restart unless-stopped \
  --network host \
  -v ./data/:/config/hass-panel \
  -d \
  ghcr.io/mrtian2016/hass-panel:latest
```

安装完成后直接打开机器的5123端口即可使用

## Hass-Panel项目地址

GitHub：[https://github.com/mrtian2016/hass-panel](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21ydGlhbjIwMTYvaGFzcy1wYW5lbA)

[取消回复](https://blog.upx8.com/4699#respond-post-4699)

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