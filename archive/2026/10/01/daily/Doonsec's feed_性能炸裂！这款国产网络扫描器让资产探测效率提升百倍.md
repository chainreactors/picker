---
title: 性能炸裂！这款国产网络扫描器让资产探测效率提升百倍
url: https://mp.weixin.qq.com/s/jwd65Gz-neN_34-ACW27Ow
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:45:35.197957
---

# 性能炸裂！这款国产网络扫描器让资产探测效率提升百倍

# 性能炸裂！这款国产网络扫描器让资产探测效率提升百倍

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明：本文介绍工具仅用于授权安全测试，任何未授权扫描行为均违反法律法规。

## 重点导读简介

gogo 是一款使用 Go 语言开发的高性能网络资产探测工具。该工具能够快速完成大规模网段的端口扫描、指纹识别与服务检测任务。

## 重点导读核心特性

### PART 01极速扫描

* Goroutine 并发池驱动，Linux 环境默认 4000 并发
* 最小发包原则，单次探测获取最多信息
* 内存占用极低，CPU 使用率可控

### PART 02智能模式

* Default 模式：标准端口扫描
* Smart 模式：/24 子网智能探测
* SuperSmart 模式：/16 大网段启发式扫描
* 支持 ICMP/ARP 存活检测

### PART 03指纹识别

* 主动指纹：HTTP Server 指纹、Banner 抓取
* 被动指纹：JA3 TLS 指纹、HHTTP 指纹
* 支持框架识别：nginx、Apache、IIS、Spring 等
* 支持服务识别：SSH、MySQL、MongoDB、Redis 等

### PART 04POC 扩展

* 集成 nuclei 漏洞验证引擎
* 支持自定义 POC 编写
* 内置 DSL 配置扩展

## 重点导读架构

### PART 05模块划分

* cmd：命令行入口
* core：扫描调度与结果处理
* engine：各协议扫描实现
* pkg：公共组件与模板

### PART 06核心组件

* Dispatch：扫描任务分发
* TargetGenerator：目标生成器
* Result：结果数据结构
* ants：Goroutine 并发池

## 重点导读使用方式

### PART 07基础扫描

```
gogo -i 192.168.1.1/24 -p top2
```

### PART 08端口配置

* `-p -` 全部端口
* `-p common` 内网常用端口
* `-p top2` 常见 Web 端口
* `-p all` 所有预设端口组合

### PART 09启发式扫描

```
gogo -i 172.16.0.0/12 -m ss --ping -p top2
```

### PART 10工作流

```
gogo -w 10
```

## 重点导读输出格式

* `full`：详细文本输出
* `color`：带颜色输出
* `json`：聚合 JSON 文件
* `jl`：JSON Lines 格式
* `url`：仅 URL

### PART 11结果过滤

* `--filter` 字段值过滤
* `::` 模糊匹配
* `==` 精准匹配
* `!=` 不等于
* `!:` 不包含

## 重点导读编译构建

### PART 12标准编译

```
bashcd gogo/v2
go mod tidy
go generate
go build -tags goregexp -o gogo .
```

### PART 13Windows Server 2003 兼容编译

```
bashGOOS=windows GOARCH=386 go1.11 build -tags "forceposix goregexp" .
```

## 重点导读应用场景

* 企业内网资产梳理
* 安全测试目标发现
* 漏洞 POC 验证
* 网络拓扑测绘

## 重点导读项目地址

本公众号非项目作者，仅做技术分享。

```
https://github.com/chainreactors/gogo
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoXjomdRm8WKEOXT0tTTjXibSz8HjE4W3eJz0gK59UgLuN8rTTic8N4ONmuFN8VMtjYbXib4ywqJ7VQo48eHlZh2I9XnNy1gXNpzY/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uom6qGvUUzYYEu5mctGBy7Gvic0QZ6eh2mjCcanl4blibAdtNngqSpcicCXia4TPU9CPejWKe1ZndI8oNKtj2NAicXic8aj0b8Fem2cQ/640?from=appmsg)

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