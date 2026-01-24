---
title: LingOps (灵控)：AWD网络安全攻防竞赛自动化web平台
url: https://mp.weixin.qq.com/s/sMvqBTdPyMG0rAlKv3y90Q
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:23.912949
---

# LingOps (灵控)：AWD网络安全攻防竞赛自动化web平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSsrUf1gHOq7DHBViaet5stae7e6ficaDBJjWiaicicUZnicvPI2VLvhr8XXVw/0?wx_fmt=jpeg)

# LingOps (灵控)：AWD网络安全攻防竞赛自动化web平台

原创

zhanglingling
zhanglingling

迷人安全

![]()

在小说阅读器中沉浸阅读

## 📖 简介

LingOps（灵控） 是一个专为 AWD/AWDP 攻防竞赛设计的竞赛自动化平台，提供 IP探测、WebShell 管理、SSH 终端、基线加固、Flag 读取等核心功能，帮助参赛选手在比赛中高效管理多个目标。

## ✨ 核心功能

### 🔍 目标探测

* **网络扫描** - 快速检测目标主机存活性，支持批量 IP 和 IP 范围探测

### ⚡ 攻击模块

* **Shell 管理** - WebShell/SSH 连接管理，支持虚拟终端、文件管理
* **木马生成** - 生成各种类型的 WebShell 木马
* **权限维持** - 通过不死马、内存马维持已获取的权限

### 🛡️ 防御模块

* **WebShell 扫描** - 基于规则引擎的 WebShell 检测，支持 ZIP 上传和远程扫描
* **WAF 管理** - WAF 规则配置与部署

### 🛠️ 运维模块

* **基线管理** - 网站备份、安全巡检、权限标准化、PHP 安全配置、后门清理、文件差异监控、反弹 Shell 终止、端口封禁、SSH密码修改、Mysql密码修改
* **数据库管理** - MySQL 连接管理、SQL 执行、数据库备份恢复

### 🚩 Flag 读取

* **后台任务模式** - 切换页面不中断
* **定时读取** - 设置间隔自动循环读取
* **历史记录** - 查看所有读取记录和时间

### ⏳ Flag 自动提交（待开发）

> 自动化提交 Flag 的系统，用于竞赛或演练场景。

### ⏳ AWDP 专项（待开发）

> 针对 Attack-Defense Plus 比赛（AWDP）的专项工具集。

### ⏳ 其他功能（待开发）

> 其他辅助工具或扩展功能，具体内容待定。

## 🚀 快速开始

### 1. 发行版本下载

> **下载链接**：https://github.com/zhanglinglingc/lingops

### 2. 启动可执行文件

### 3. 访问

打开浏览器访问 `http://127.0.0.1:8080`

**默认账号密码：**

* 用户名：`admin`
* 密码：`admin123`

## 🔒 部分功能预览

### ✨ 首页

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSRIKVLFEgDyoBm3tkH9EooyeoibJu1O5j8HiaHeqaiaZqbJGMGia0EqWUGA/640?wx_fmt=png&from=appmsg)

### 🔍 目标探测

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSVl93G8ibHQ1kjDHfaYZcd2uKicIZpBrRQZvNnbDNvkUQMqc0DlQKnMnQ/640?wx_fmt=png&from=appmsg)

### ⚡ shell管理

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aS3ggB8TqCkx9QRhQRd6V0ZNJbMdgEKBEFiaJBJyjwOV1SOJtDJXibxhRA/640?wx_fmt=png&from=appmsg)

### 🛡️ WAF管理

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSOWpBER5weER225Jsm9TPkHLe0OW6tg0CETcDrkWlvufx5eb9u9XMSQ/640?wx_fmt=png&from=appmsg)

### 🛠️ 基线管理

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSHjQFsGQSdU9Qa626S61MiaDKsQ3PAM1MOBJGicaN49XGyR5faq9nkbzg/640?wx_fmt=png&from=appmsg)

### 🚩 Flag 读取

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqOulYibIZH5M47Iia2V10ic9aSbY0FNrHqqBTLsV4AaVeOWZj4KcywSO4ohOk3QdmW3iahlbibM4e0Qibsw/640?wx_fmt=png&from=appmsg)

## 🔒 安全说明

⚠️ **本工具仅供授权的安全测试和 CTF 比赛使用！**

* 请勿用于未授权的系统
* 请勿用于非法活动
* 使用者需自行承担法律责任

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqPvCzibggORicOgMhjBp7HVEtlMoDQGga60sr3AsTe5aHRs7bA7yNic8sibicSpXUIzHkWuDoIH3ibESHCQ/0?wx_fmt=png)

迷人安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqPvCzibggORicOgMhjBp7HVEtlMoDQGga60sr3AsTe5aHRs7bA7yNic8sibicSpXUIzHkWuDoIH3ibESHCQ/0?wx_fmt=png)

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