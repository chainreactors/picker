---
title: WeChat Selkies：把微信/QQ搬进浏览器的 Linux Docker
url: https://blog.upx8.com/4888
source: 黑海洋 - Wiki
date: 2025-10-27
fetch_date: 2025-10-28T02:58:59.557778
---

# WeChat Selkies：把微信/QQ搬进浏览器的 Linux Docker

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# WeChat Selkies：把微信/QQ搬进浏览器的 Linux Docker

发布时间:
2025-10-27 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
2686

## WeChat Selkies概览

**WeChat Selkies** 将官方微信/QQ 的 Linux 客户端封装进 Docker 容器，通过 **Selkies 的 WebRTC** 技术把界面投送到浏览器。用户无需在本机安装微信/QQ，即可在 Chrome、Firefox、Safari 等现代浏览器中直接使用，适合服务器端部署与远程办公场景。
开源地址：https://github.com/nickrunning/wechat-selkies

![](https://cdn.skyimg.net/up/2025/10/27/91ff06cd.webp)

## 核心特性

* **浏览器直达**：打开网页即可用微信/QQ，无需本地安装。
* **容器化部署**：Docker 一键拉起，环境隔离更可控。
* **数据持久化**：配置与聊天记录可落盘保存。
* **中文体验完善**：内置中文字体，本地中文输入法可用。
* **图片复制与文件传输**：侧边栏面板开启后即可完成粘贴与传输。
* **多架构兼容**：原生支持 **AMD64** 与 **ARM64**。
* **可选硬件加速**：按需启用 **GPU 加速**。
* **窗口切换器**：左上角新增悬浮窗，便于切换后台窗口。
* **自动启动**：可配置开机自启微信与 QQ（可选）。

## 环境与访问

### 环境要求

* Docker
* Docker Compose
* 支持 WebRTC 的现代浏览器（如 Chrome、Firefox、Safari）

### 典型使用场景

* 轻量化企业或个人的 **远程办公与服务器常驻登录**
* 多终端随时接入的 **无客户端运维环境**
* 需要 **ARM 服务器/树莓派** 等场景的跨架构使用

## 升级与故障排查

升级后若出现功能缺失，可先清空本地挂载目录中的 `openbox` 目录（示例：`./config/.config/openbox`），再重启容器以恢复组件加载。

## WeChat Selkies项目链接

GitHub地址：[https://github.com/nickrunning/wechat-selkies](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL25pY2tydW5uaW5nL3dlY2hhdC1zZWxraWVz "WeChat Selkies GitHub地址")

[取消回复](https://blog.upx8.com/4888#respond-post-4888)

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