---
title: 爆炸性发现！CF-Hero 让 Cloudflare 保护的所有资产在 30 秒内曝光
url: https://mp.weixin.qq.com/s/T3lc6t-hLjDbxGcCMqjkAw
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:25:23.902183
---

# 爆炸性发现！CF-Hero 让 Cloudflare 保护的所有资产在 30 秒内曝光

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UqNZPLYYZlXlFDWa9PK9XqtVNOkkuFYsrBBnHbfSo0N31wrmeJ7MIg90icq2wVaUkpElB9MW8Y0yBwvvp2wrx0ONzZxzcPz1RsY/0?wx_fmt=jpeg)

# 爆炸性发现！CF-Hero 让 Cloudflare 保护的所有资产在 30 秒内曝光

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

郑重声明：本文仅做技术研究与安全合规探讨，使用本文所涉及技术工具时，请严格遵守法律法规，严禁用于任何未经授权的渗透测试、入侵行为或非法数据获取。

## 重点导读简介

CF-Hero 是一款 Cloudflare 资产识别工具，核心功能为定位受 Cloudflare CDN 保护的真实 IP 地址。该工具通过 DNS 侦察、OSINT 情报源、历史记录分析等多种技术手段，实现多维度资产发现。

## 重点导读核心技术

### PART 01DNS 侦察

* A 记录解析
* TXT 记录解析
* 非 Cloudflare IP 段识别

### PART 02情报源

* ZoomEye
* Censys
* Shodan
* SecurityTrails

### PART 03关联分析

* 历史 DNS 记录
* 同公司域名关联
* 子域名列表比对

## 重点导读技术架构

### PART 04模块

```
cmd/cf-hero/main.go
internal/scanner/
internal/dns/
internal/http/
internal/config/
pkg/models/
```

### PART 05并发

workerpool

### PART 06验证

HTML Title 比对

## 重点导读功能

* JA3 指纹
* 代理支持
* User-Agent
* 管道输入
* 进度条
* 彩色输出

## 重点导读场景

* 渗透测试
* 资产管理
* 应急响应

## 重点导读安装

```
go install -v github.com/musana/cf-hero/cmd/cf-hero@latest
```

## 重点导读用法

```
cat domains.txt | cf-hero
```

多数据源：

```
cf-hero -f domains.txt -zoomeye -censys -shodan -securitytrails
```

子域名关联：

```
cf-hero -td https://target.com -dl subdomain_list.txt
```

配置文件 `~/.config/cf-hero.yaml`：

```
yamlzoomeye:
  - "api_key_here"
securitytrails:
  - "api_key_here"
shodan:
  - "api_key_here"
censys:
  - "censys_pat_here"
  - "organization_id_here"
```

## 重点导读项目展示

![扫描界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uo7cZe9mXhfeu9kQq3snAX0hkNicnnZZjRugib90eobg7ibwPBRQeqzs2oa9Tq5pV8GZmr3icUqLUmdIT2mx8R9hweX5rWwmfanqlQ/640?from=appmsg)

扫描界面

![扫描结果](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UresJVP8eT5rGDib4ibueib5xXzVvic4asDLnjwVOTm73XCDNmbYDjZlOOTa22xdDsFT5iagp2xEq4wtbYpdWNg7ibicEf4dyYzv4wib0A/640?from=appmsg)

扫描结果

## 重点导读项目地址

本文介绍的项目开源地址如下：

```
https://github.com/musana/CF-Hero
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UptaQVuv3dPTPv2ryZQia38l6V1eQSDIxc1jkLpkd5XULtJwNibyibHLLacs5icPO51uTd9Mpiczhs1BhtfRqKQxHicb7vdKgNXcuhCY/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoiaWZj6y9KCibKhMr7fzNqqtXraWkIyA9qrULDx7hGia6MiaWHnYrsOXsSMZYQ9iavIgzUBEYdicGzHCEl9iayPnxKNUPRMpTevvuuuE/640?from=appmsg)

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