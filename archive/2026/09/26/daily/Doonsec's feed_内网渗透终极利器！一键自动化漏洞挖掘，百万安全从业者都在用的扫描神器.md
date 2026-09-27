---
title: 内网渗透终极利器！一键自动化漏洞挖掘，百万安全从业者都在用的扫描神器
url: https://mp.weixin.qq.com/s/BYZ2iH9KbZIUonFj-OaTgw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:22:43.275190
---

# 内网渗透终极利器！一键自动化漏洞挖掘，百万安全从业者都在用的扫描神器

# 内网渗透终极利器！一键自动化漏洞挖掘，百万安全从业者都在用的扫描神器

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

郑重声明：本文仅供技术研究与学习，使用该工具时务必遵守法律法规，取得合法授权。不对非授权目标进行扫描。

## 重点导读概述

fscan是一款Go语言开发的高级内网综合扫描工具，专为企业安全建设场景设计。该工具实现了一键自动化漏洞挖掘功能，集主机发现、端口扫描、服务识别、漏洞检测与利用于一体。代码采用模块化架构，支持插件扩展与SDK嵌入，可集成至现有安全平台。

## 重点导读核心架构

### PART 01模块划分

| 模块 | 路径 | 功能 |
| --- | --- | --- |
| common | common/ | 配置管理、日志输出、网络通信、代理支持 |
| core | core/ | 主机发现、端口扫描、服务探测、Web扫描 |
| plugins | plugins/ | 服务插件、本地插件、Web插件 |
| webscan | webscan/ | 指纹识别、POC扫描 |

### PART 02技术栈

* 语言：Go 1.25
* 并发：ants协程池
* 协议：SMB2/FTP/LDAP/MYSQL等
* POC引擎：CEL规则引擎

## 重点导读功能特性

### PART 03扫描能力

* 主机发现：ICMP/Ping存活探测，支持大网段B/C段
* 端口扫描：TCP全连接，133个内置端口
* 端口分组：web/db/service/all
* 服务识别：20+协议指纹匹配

### PART 04漏洞检测

* 高危漏洞：MS17-010、SMBGhost
* 未授权访问：Redis/MongoDB/Memcached/Elasticsearch
* POC扫描：支持Xray格式POC
* DNSLog外带检测

### PART 05漏洞利用

* Redis：写公钥、写计划任务、写WebShell、主从复制RCE
* MS17-010：ShellCode注入、添加用户、执行命令
* SSH：密钥登录、命令执行

### PART 06本地工具

* 信息收集：系统信息、环境变量、域控信息
* 凭据获取：内存转储、键盘记录、注册表导出
* 权限维持：Systemd服务、Windows服务、计划任务、LD\_PRELOAD
* 反弹Shell：正向、反向、SOCKS5代理
* 杀软检测、痕迹清理

## 重点导读输入输出

### PART 07目标指定

* IP/CIDR/域名/URL
* 文件批量导入
* 排除规则：主机排除、端口排除

### PART 08输出格式

* TXT/JSON/CSV
* 实时刷盘
* 静默模式

## 重点导读网络控制

* HTTP/SOCKS5代理
* 网卡指定（VPN场景）
* 速率限制
* 超时控制
* 并发控制

## 重点导读扩展功能

### PART 09SDK嵌入

`pkg/fscan`提供Go SDK，支持：

* 任务控制（暂停/恢复）
* 实时进度回调
* TaskID追溯
* 嵌入Agent或安全平台

### PART 10Web界面

可视化扫描任务管理，响应式布局，编译标签：`-tags web`

### PART 11多语言

中英文界面切换：`-lang zh/en`

### PART 12性能分析

JSON格式性能报告：`-perf`

## 重点导读使用示例

```
bash./fscan -h 192.168.1.1/24
./fscan -h 192.168.1.1 -p 22,80,443,3389
./fscan -h 192.168.1.1/24 -nobr
./fscan -u http://192.168.1.1
./fscan -local systeminfo
./fscan -h 192.168.1.1 -m redis -rf id_rsa.pub
```

## 重点导读编译

```
bashgo build -ldflags="-s -w" -trimpath -o fscan .
go build -tags web -ldflags="-s -w" -trimpath -o fscan-web .
```

## 重点导读界面展示

![扫描效果](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UojHia6oXunvR9gToWWLX9CoXVI2nHSiaHS5bLQgSQNltydcoyPswpWtmZzvjUcgicewbNw4zSQar6PWIOv1cfat9wQKv7MP7I4M0/640?from=appmsg)

扫描效果

![Redis写公钥](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq0fMk78icNywW0zTvwMRfskHkuE3xd49KtZNaDSnTKedmeibCy0CWZibSCpaNJdzMjcycQBq4j0JtA32QweeMicd7S0CnQFRZRZ7Q/640?from=appmsg)

Redis写公钥

![SSH爆破](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uo7P5johqcpzzLgpQMXrzgfPVNibdmiayEKllpkBOJOgickM6NugK2HjXegba1OBIia9lTStTnqWdich87iaBMpPmdwv1w6k2o0ZgEJ0/640?from=appmsg)

SSH爆破

![存活探测](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Upicd4qykkk20fTmMBHUA0U0gc4yXrZkDWYXqbibor3gYZqQ66myvicxejbe27uXibK2ceY3GS2ibdnib8FBicGHPQ9IO3RZib8ztD2sVo/640?from=appmsg)

存活探测

## 重点导读项目信息

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/shadow1ng/fscan
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UogZx7VfSicfzTibcDTeL9iaxqCJfFLltyyMA2u1P7C0TWFT9NfR6Xic8ibpwsrhH8K7ic8H51pqaTTLdGlEicoBVRiaq4GmVGpVfCaebU/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoiacVDxTxfrnBa83nYRJuLZrz9rfBke5ow0yWNEcxIaKYWiaf2jolp9xUL2sRj5ybm6OiaI2fSoOEiafYAzQLkEHrAd4SMariaqkUo/640?from=appmsg)

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