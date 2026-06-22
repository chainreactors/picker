---
title: 工具推荐 | 网站篡改、暗链、死链监测工具
url: https://mp.weixin.qq.com/s/zK4kS4CH1wI38orgYg16sA
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:16.093061
---

# 工具推荐 | 网站篡改、暗链、死链监测工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVliaOAa6nicicPukIMYILDn6lWV4Z40erUPAFX9mdoM9d9jDicEVibeHFrokeyOU8KwGNEnODfTtGib2Pu0Vv25rPib25x4MyYJicTow5c/0?wx_fmt=jpeg)

# 工具推荐 | 网站篡改、暗链、死链监测工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 920，阅读大约需 5 分钟

## 前言

Libra [天秤座] 是一个功能全面的网站安全监测与分析平台，专注于网站篡改、黑链、后门、违规内容、死链等安全威胁的自动化检测。

项目地址：https://github.com/rabbitmask/Libra

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkqSu7HDFzI3XuTXocCLAaCtNbYRhwhjwibicjGovHW3chlZuyxCr0WmqwY88GvbDPiaB2icQcV9Fd7nxICaCWTUjPTnibrMsN8B3YU/640?wx_fmt=png&from=appmsg)

## 核心功能

### 安全检测模块

| 模块 | 重要等级 | 功能描述 |
| --- | --- | --- |
| 🔗 黑链检测 | ⭐⭐⭐⭐⭐ | 检测隐藏的恶意外链和 SEO 黑链 |
| 🚪 后门检测 | ⭐⭐⭐⭐ | 识别 Webshell 和后门文件 |
| ⚠️ 违规检测 | ⭐⭐⭐⭐ | 检测违法违规内容 |
| 💔 死链检测 | ⭐⭐ | 识别失效链接 |

### 扫描类型

* • **HomePage\_Scan**: 首页检测 - 快速检测网站首页安全状况
* • **SecondPage\_Scan**: 二级页面检测 - 深入检测子页面
* • **AllSite\_Scan**: 全站扫描 - 全面扫描整个网站
* • **CustomPage\_Scan**: 自定义页面检测 - 指定页面检测

## 使用

### 环境要求

* • Python 3.6+
* • SQLite (内置)

### 安装依赖

```
pip install -r requirements.txt
```

### 基本用法

#### 1. 显示帮助信息

```
python Libra.py
```

#### 2. 快速检测网站首页

```
python Libra.py -u http://example.com
```

#### 3. 指定检测类型

```
# 首页检测
python Libra.py -u http://example.com -t HomePage_Scan

# 二级页面检测
python Libra.py -u http://example.com -t SecondPage_Scan

# 全站扫描
python Libra.py -u http://example.com -t AllSite_Scan

# 自定义页面检测
python Libra.py -u http://example.com -t CustomPage_Scan
```

## 检测报告

系统将生成详细的安全检测报告，包括：

* • **检测概览**: 目标 URL、检测类型、检测状态
* • **页面信息**: 响应状态、内容哈希、页面标题
* • **链接分析**: 内链、外链统计与分析
* • **安全威胁**: 发现的黑链、后门、违规内容等

## 原理

**数据采集 → 特征比对 → 异常判定 → 告警 / 验证**

### 1. 网站篡改监测

**核心逻辑**：基于「基准特征库」与「实时采集内容」的一致性校验

* • 第一步：初始化阶段，对目标网站的正常页面采集核心特征（如 HTML 源码哈希值、关键 DOM 节点指纹、文本特征值、页面资源 MD5 等），存入 Libra.db（项目中的数据库）；
* • 第二步：定时（通过 Framework/Tools 模块的调度功能）爬取目标页面，重新计算特征值；
* • 第三步：对比实时特征与基准特征的差异率，若超过阈值（如哈希值不一致、关键节点缺失 / 篡改），判定为 “篡改”；

### 2. 暗链监测

**核心逻辑**：基于「黑特征库 + 异常链接检测」识别隐蔽违规链接

* • 特征库匹配：ORM 模块管理黑词 / 黑域名库（如博彩、色情域名、违规关键词），爬取页面时解析所有标签、iframe、JS 跳转、CSS 隐藏链接，比对特征库；
* • 异常行为识别：检测 “隐蔽属性”（如链接文字与背景色一致、position:absolute 脱离可视区、display:none 隐藏、z-index 负值），或非业务相关的外链（如突然新增的陌生域名跳转）；
* • 深度检测：解析页面内嵌 JS（Tools 模块可能集成 JS 解混淆工具），识别动态生成的暗链（如加密的跳转代码、定时加载的违规链接）。

### 3. 死链监测

**核心逻辑**：基于「HTTP 状态码 + 资源可达性验证」

* • 链接遍历：爬取目标网站所有内链 / 外链（页面链接、图片、脚本、样式表等），构建链接池；
* • 可达性检测：对每个链接发送 HTTP/HTTPS 请求（Libra.py 核心爬虫逻辑），判断状态码：

+ • 4xx（404/403/401）、5xx（500/502/503）判定为死链；
+ • 3xx 需跟进跳转，最终跳转至无效地址也判定为死链；

* • 时效性校验：定时重测疑似死链（排除临时服务器故障），确认后标记为死链。

## 总结

项目地址：https://github.com/rabbitmask/Libra

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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