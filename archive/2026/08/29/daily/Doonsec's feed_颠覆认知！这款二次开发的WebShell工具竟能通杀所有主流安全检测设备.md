---
title: 颠覆认知！这款二次开发的WebShell工具竟能通杀所有主流安全检测设备
url: https://mp.weixin.qq.com/s/tGztplnheREA6uO1miRM5A
source: Doonsec's feed
date: 2026-08-29
fetch_date: 2026-08-30T07:41:40.395161
---

# 颠覆认知！这款二次开发的WebShell工具竟能通杀所有主流安全检测设备

# 颠覆认知！这款二次开发的WebShell工具竟能通杀所有主流安全检测设备

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 重点导读安全规范

本工具仅用于合法的安全研究与测试，请勿用于任何非法用途。使用者应对自身行为承担全部责任。

## 重点导读项目概述

Z-Godzilla\_ekp是基于哥斯拉（Godzilla）WebShell管理工具的二次开发项目，专注于规避流量检测设备。项目作者持续更新至今，已实现内存马注入、多语言自定义免杀加密器以及高度模拟正常流量的混淆功能。该工具在截止2024年4月的测试中，成功穿透国内两家主流安全厂商的态势感知系统，连接与命令执行均无告警。

## 重点导读核心功能

### PART 01流量混淆体系

* 去除Cookie后分号强特征，消除流量识别关键标记
* 去除响应包中MD5前后16位匹配特征，打破固定特征码定位
* 去除UA头等弱特征，消除浏览器指纹暴露风险
* 请求包与响应包完全伪装成正常业务流量

### PART 02免杀能力

#### .NETPayload生成

* bypass1模式生成的WebShell可实现全球主流扫描引擎零报红
* 实测覆盖平台：VirusTotal、微步云沙箱、阿里云安全、玄蜂系等
* 随机HTML模板动态生成，增加静态分析难度

#### AMSI绕过

* 专用版本可绕过AMSI机制检测
* 建议配合命令执行bypass插件使用
* 支持Server 2022及以上版本（自带插件受限为杀软行为，非工具bug）

### PART 03内存马注入

* 支持在运行时动态注入内存马
* 无文件落地痕迹，大幅降低被取证发现的风险

### PART 04多语言支持

* 内置三种语言的自定义免杀加密器
* 允许使用者根据目标环境自行二次开发
* 详细教程通过微信公众号"艾克sec"发布

## 重点导读技术架构

### PART 05双版本兼容机制

* 二开版本生成的WebShell需使用二开版本客户端连接
* 普通哥斯拉客户端无法连接二开版本生成的Shell
* 连接时需选择对应模式进行匹配

### PART 06目录结构

```
Z-Godzilla_ekp/
├── README.md
└── assets/          # 图片资源
```

## 重点导读使用场景

* 合法渗透测试项目
* 安全研究与漏洞验证
* 红队作战与攻防演练
* 应急响应与事后取证分析

## 重点导读更新历史

### PART 07v1.2

针对哥斯拉DLL特征被加入AMSI检测库的问题，发布专用绕过版本，恢复在最新杀软环境下的正常连接能力。

### PART 08v1.1

新增.NET平台Payload生成即免杀功能，配合随机HTML模板实现多引擎零报红。

## 重点导读技术说明

本项目为WebShell安全研究方向的二次开发作品，核心价值在于帮助安全研究人员和渗透测试工程师理解流量检测与规避技术的对抗原理。所有功能均围绕合法安全测试场景设计。

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/ekkoo-z/Z-Godzilla_ekp
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrqrCgqmiaM4LiannGibCk1daLVuPumEWsJkBafqicchMYXjXIKsCTibs2XZIxI2StskpqEETa0HzkuJ8VCALNibUnm4b1F8kmjibyMyU/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrQ1JTibSkZjkicFKpW3UCjVfJRbhlcJOVzaxkS9zTHUtK3KlETGcurTzvxgF3o6WaMibp0UqcOXwpiaWbsLJSCeeicocEKCNnNfEeA/640?from=appmsg)

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