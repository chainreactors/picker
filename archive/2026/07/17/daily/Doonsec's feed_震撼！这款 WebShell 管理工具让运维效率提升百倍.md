---
title: 震撼！这款 WebShell 管理工具让运维效率提升百倍
url: https://mp.weixin.qq.com/s/Fdw4mzDm3xmqGdDd4VgyHw
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:43:38.487915
---

# 震撼！这款 WebShell 管理工具让运维效率提升百倍

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UqB3Cib8wCYNlFNBDoCH5mjhHRvj72fs6Gh56rLGPAsQP7Mm2GvJjlU6BlwTTjY8D45Akh8jZH4Ousx7C4mUsbaKMkHNIYiajW6A/0?wx_fmt=jpeg)

# 震撼！这款 WebShell 管理工具让运维效率提升百倍

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 重点导读安全声明

本工具仅授权于合法渗透测试与安全研究场景。未经授权使用将违反相关法律法规。

## 重点导读概述

CtG 是一款基于 Web 架构的 Shell 终端管理器，提供浏览器端的远程Shell访问能力。该项目采用 Docker 容器化部署方式，支持快速启动与跨平台运行。核心技术栈基于 Go 语言开发，前端界面通过 WebSocket 协议实现实时双向通信。CtG 集成了 MCP 协议扩展接口，可对接多种大语言模型服务商，实现 AI 辅助的Shell操作体验。

## 重点导读核心功能

### PART 01终端管理

WebShell 管理模块支持创建、修改、删除Shell会话。用户可通过Web界面同时维护多个终端连接，会话状态实时监控。该模块基于 Spark 项目二次开发，保留了原生的交互体验。

### PART 02文件管理

内置文件管理器提供远程主机上的文件浏览、编辑、上传、下载功能。界面集成于Web控制台，无需额外FTP或SMB协议即可完成日常文件操作需求。

### PART 03MCP 集成

支持 Model Context Protocol 扩展，可连接 OpenAI、Claude、Ollama、DeepSeek、GLM、MiniMax、Kimi 等主流大语言模型平台。AI能力可辅助命令执行与结果分析。

## 重点导读双层认证

| 层级 | 类型 | 配置项 |
| --- | --- | --- |
| 第一层 | Nginx Basic Auth | NGINX\_USER / NGINX\_PASS |
| 第二层 | 应用登录 | CTG\_USERNAME / CTG\_PASSWORD |

浏览器弹窗完成第一层认证，应用内控制台完成第二层认证。双因素架构增强安全隔离效果。

## 重点导读部署架构

### PART 04Docker 部署

容器环境基于 Alpine Linux 构建，镜像体积精简。数据持久化采用本地卷挂载方式，数据库与日志存储于宿主机指定目录。健康检查机制确保服务可用性。

### PART 05Wails 桌面版

除 Docker/Web 版本外，项目提供 Windows 桌面客户端。桌面版内嵌本地服务进程，无需浏览器或外部服务，独立窗口即可完成全功能操作。该版本面向个人本地使用场景。

## 重点导读快速启动

```
bashcp .env.example .env
docker compose up -d
```

## 重点导读项目地址

本文介绍的项目开源地址如下：

```
texthttps://github.com/din4e/CtG
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Upj4YF6JegZ6qxatvq8Q8icp9vkCquWAticcGibt5OaFNpHcHCKI3Ab5K0ZlCIrSSZ8YicgyqwMA4umqicLvBic39hnAbWHynuh88fMw/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq3K6IAbTeeweFiaraq8HjKzgf0HcD2RlrHwNsMxwPBChx5yIzGJL6hpnPmj5NcEkZnB33pAic9M52FSkUOBlpicJoGbz18iaqzwUg/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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