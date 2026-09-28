---
title: 震撼业界的全能扫描神器降临！一款工具搞定端口探测、协议识别、指纹匹配、暴力破解！
url: https://mp.weixin.qq.com/s/xsPNtFNZKYzxdgTPDAqh6w
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:57.141775
---

# 震撼业界的全能扫描神器降临！一款工具搞定端口探测、协议识别、指纹匹配、暴力破解！

# 震撼业界的全能扫描神器降临！一款工具搞定端口探测、协议识别、指纹匹配、暴力破解！

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

郑重声明：本工具仅限授权安全测试使用，任何未授权扫描行为均属违法。

## 重点导读简介

Kscan是一款由纯Go语言开发的多功能网络安全扫描工具，集成端口扫描、协议检测、指纹识别、暴力破解等核心能力。该项目在网络安全领域具有广泛的应用价值，适用于企业安全建设和授权渗透测试场景。

## 重点导读核心能力

### PART 01协议支持

支持协议数量超过1200种，涵盖主流网络服务。协议指纹库规模达10000余条，应用指纹库超过20000条。暴力破解模块支持SSH、RDP、FTP、SMB、MySQL、MSSQL、Oracle、PostgreSQL、MongoDB、Redis等十余种协议。

### PART 02输入模式

三种目标输入方式灵活适配：

* 直接指定IP、IP段、URL地址
* 导入目标文件进行批量扫描
* 对接FOFA搜索引擎获取资产范围
* 网段探测模式自动发现存活主机

### PART 03扫描流程

以端口为单位的资产输出机制，协议识别驱动后续应用层检测。当端口协议识别为HTTP时，自动触发指纹识别和标题获取。当协议为RPC时，尝试获取主机名等关键信息。

## 重点导读技术架构

### PART 04扫描引擎

五大扫描引擎协同工作：

* DomainClient：域名解析与CDN识别
* IPClient：存活主机探测
* PortClient：端口扫描与协议检测
* URLClient：应用指纹识别
* HydraClient：自动化暴力破解

![kscan逻辑图.drawio](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrzvSXKdY7Puw4BvxKZsFl2spoJHzLDEQ4GMd7FUv6wLtJvjpMY2qyTJm0y9qj6JnTVf7zAfXBUK5RicqnUFqbGvhSqSia7qHYno/640?from=appmsg)

kscan逻辑图.drawio

### PART 05指纹识别

集成HTTP指纹库和应用指纹库。NMAP探针用于协议深度检测。指纹匹配结果作为暴力破解任务下发的触发条件。

### PART 06CDN识别

依托纯真IP库实现CDN节点识别。该功能可通过命令行参数关闭。

## 重点导读功能特性

### PART 07存活探测

智能存活性探测机制，默认启用。可使用-Pn参数关闭。

### PART 08CDN识别

自动识别目标是否部署CDN节点。可使用-Dn参数关闭该功能。

### PART 09暴力破解

自动化弱口令检测，支持自定义用户名和密码字典。默认使用内置字典，可通过参数添加或替换。

### PART 10输出格式

支持多种输出格式：

* 普通文本文件
* JSON格式文件
* CSV格式文件

### PART 11代理支持

支持SOCKS5、SOCKS4、HTTPS、HTTP代理协议。

### PART 12线程控制

默认线程数100，最高支持2048。可根据扫描目标规模和网络环境调整。

## 重点导读使用场景

### PART 13端口扫描

快速探测目标网络开放端口，获取存活服务信息。

![端口扫描演示](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UqYcwJ9E5DYibsug4ZXZUiaNRxjM9g7AX1mriac2Gh1zEd9RouzuZ0aKfqW3CwnNTxTjWcoumAThKrNAncmKzPBN3g2KPjK82cGI4/640?from=appmsg)

端口扫描演示

### PART 14网段探测

自动发现内网网段存活主机，适用于内网资产梳理。

![存活网段检测演示](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uo9dd73bibW5LTZEiaibictG90Y6W4TlgccxoDiaYwFHWCxicHzRQFzv3frJl90rfgnZof1aF9hfzFmMVxfbmBmLd6D54KOyeYwiche9U/640?from=appmsg)

存活网段检测演示

### PART 15FOFA对接

直接导入FOFA搜索结果进行深度扫描，结合全探针检测能力。

![Fofa结果检索演示](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrURJqjYpONDibLQ5c71Yfs8HTtO1W6E4PSOE9L4xFAQUgQI9ArUxqajjYLYC7qE0KQtkpusI9yaZSYiaMrqiaPJ1mV67Otb4fuOA/640?from=appmsg)

Fofa结果检索演示

### PART 16暴力破解

对识别出的服务进行自动化弱口令检测。

![Hydra功能演示](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqv9aKDS9llWtZnV1TLInFN19ia0aCdbGEdZeB5ynaIQZXH7yFR9wpZQL0VKSbTc5PND1tOn5KOEycFNQ8HakHeziaY7JmGl3gNw/640?from=appmsg)

Hydra功能演示

### PART 17CDN识别

快速判断目标是否使用CDN服务，辅助资产范围判定。

![CDN识别演示](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur7icqGKZIr9N9iaBqRfqpgBsgIv6fg7zYegW2IneK5aicH7HPVZaVIaQjW7oOaanxiaH8q7OtQz3tubbrztfZtlOrdRmqAHcUUhbY/640?from=appmsg)

CDN识别演示

## 重点导读编译构建

项目基于Go语言开发，要求Go版本1.8及以上。编译流程支持多平台构建。

## 重点导读项目地址

本文介绍的项目开源地址如下：

```
本公众号非项目作者，仅做技术分享。
https://github.com/lcvvvv/kscan
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uoh2TsBrlj2cyLryichdQhCN1zuRctib61z3zYse8VcrcnvfTGhxNCUZkKdzhyfLbpnicxMuz47gW02K9cjqeia98M2lQpDNnS1jvg/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrtECibtXZPvzFb71LHiaSyTbcrB7soiaX4JiaeGCc97Jmia2zhicUJVhQuiamPjhxxgVQ6u0bMUjC6flSib1njrSv0TdGyDTg07hqDoKk/640?from=appmsg)

预览时标签不可点

不喜欢

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