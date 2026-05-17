---
title: 正式上线！tool.geek.cab 域名备案通过，网络工具箱全面升级！
url: https://mp.weixin.qq.com/s/CSpwRc7tjOoZYTZ4xxyGpQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:46:56.500865
---

# 正式上线！tool.geek.cab 域名备案通过，网络工具箱全面升级！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dibzmm9niba072BehX59fCskVTAicHSTTrrqrbTrIcORUU1kKolCOlKutibfpeExBe9HEibOzcZiaHichnDYMLfcjvoibl3wa44T4Rib5p7hT0Qu9Y4Q/0?wx_fmt=jpeg)

# 正式上线！tool.geek.cab 域名备案通过，网络工具箱全面升级！

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天有个好消息要分享给大家：

经过一段时间的等待，`tool.geek.cab` 域名终于备案通过了！

**正式访问地址：** https://tool.geek.cab/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba051wJD4pfwsvjIeMmDY9cUYicKhOh4APia44jtVvMtzyMUlLsg25ZNVibm8ecdJVUpPyTS5nBcKUqSXs8GQiaAhnw7rhttdxfWzcAA/640?wx_fmt=png&from=appmsg)

之前用 `tool.geek.cab:8843` 带端口号访问的朋友，现在直接访问上面的地址即可，浏览器输入更简洁，也更方便分享给同事和朋友。记得更新你的书签哦！

## 网络测速全面升级

上一版网络测速上线后，很多朋友反馈说测出来的速度不太对。经过排查，发现问题出在测试方式上——之前测的是**浏览器到服务器的速度**，而不是**用户本机的真实网速**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba048UkUGSnqtCmVHg4PafhUAJ0B3ib7WbuAlc76H0WgA2vrA4UFJFNRNibGXZIOakjKGJPiaiafXsSd9R6O4qWnEplolPEnrvZUkmI4/640?wx_fmt=png&from=appmsg)

这次我们彻底重写了测速引擎：

### 测速原理升级

**之前的问题：**

* 测的是用户到我们服务器的连接速度
* 服务器带宽有限，测速结果不准确
* 不同地域用户测试结果差异大

### 延迟测试

* 多次测量到百度的往返延迟，取平均值
* 同时计算网络抖动值，评估网络稳定性
* 结果分级展示：极低 → 低 → 正常 → 偏高 → 很高

### 可视化仪表盘

* SVG 弧形仪表盘，速度等级颜色区分
* 下载速度、延迟、抖动三项关键指标
* 历史记录自动保存最近 10 次测试结果

## 🩺 全新功能：网络诊断

这次我们还新增了一个很实用的功能——**网络诊断**，直接集成在测速页面下方。

### 功能简介

你有没有遇到过这种情况：网速测试正常，但某个网站就是打不开？网络诊断功能就是帮你排查这类问题的。

### 检测哪些网站

一键检测 8 个国内主流网站的连通性和延迟：

| 网站 | 说明 |
| --- | --- |
| 🔍 百度 | 搜索引擎 |
| 🛒 阿里（淘宝） | 电商平台 |
| 📦 京东 | 电商平台 |
| 📺 B站 | 视频平台 |
| 🎵 抖音 | 短视频平台 |
| 🐧 腾讯 | 综合门户 |
| 📢 微博 | 社交媒体 |
| 💡 知乎 | 知识社区 |

### 健康评分机制

诊断完成后会给出一个 **0-100 分的网络健康评分**：

* 🟢 **90-100 分** → 优秀，网络状态非常好
* 🔵 **70-89 分** → 良好，正常使用没问题
* 🟡 **50-69 分** → 一般，部分网站可能较慢
* 🔴 **0-49 分** → 较差，建议排查网络问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06tNZtyo3bd8ico8ExqDOUPH6UHPvLfPuOZdlqsibyUjM4RJbPjuwC26EsxRO8HkU48OD2lib1co0TnAfzCo6cYdHTBPxDibzvokzM/640?wx_fmt=png&from=appmsg)

每个不可达的网站会扣 15 分，延迟偏高的网站扣 5 分。同时会列出具体的问题，比如"京东 无法访问"、"腾讯 延迟偏高"，方便你快速定位问题。

### 使用场景

* 排查某个网站打不开的问题
* 判断是网站挂了还是自己网络问题
* 日常网络健康巡检
* 对比不同网络环境的质量

---

## 📋 工具总览

目前 NetTools 网络工具箱共包含以下工具：

### 基础工具（5个）

* IP子网计算器
* 公网/私网IP判断
* 子网划分工具
* MAC地址查询
* IP归属地查询

### 诊断工具（6个）

* Ping工具
* Traceroute
* DNS查询
* 端口扫描器
* WHOIS查询
* **网络测速 + 网络诊断** ⚡重点升级

### 配置工具（1个）

* 配置生成器（路由器/交换机模板）

### 其他工具

* 密码生成器、端口列表、HTTP状态码、正则测试、RFC文档库、图解网络术语

## 🔮 接下来做什么

如果大家有任何好的建议或想增加的工具，欢迎在评论区留言，每一条我都会认真看！

**感谢大家的支持！** 如果觉得这个工具箱对你有帮助，欢迎分享给身边的同事和朋友。记得收藏 `https://tool.geek.cab/` 哦！

点赞、在看、转发三连，你们的支持是我持续更新的动力！💪

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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