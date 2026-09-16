---
title: 已复现 | 搜狗输入法“1点击”远程代码执行漏洞（视频）
url: https://mp.weixin.qq.com/s/Sf9ns4WBGhxVNjOpQ1IqBg
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T06:59:09.392407
---

# 已复现 | 搜狗输入法“1点击”远程代码执行漏洞（视频）

# 已复现 | 搜狗输入法“1点击”远程代码执行漏洞（视频）

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、这是什么？

2026年4月，美国网络安全公司 Gen Digital 披露搜狗输入法一个一键点击远程代码执行漏洞[1],编号CVE-2026-51990，受影响的版本为V16.3.0.3498以下，目前腾讯已修复。

经过2天（晚上）研究，`本人已成功复现该漏洞`。

经分析，搜狗输入法内置浏览器基于Chromium 80版本，沙箱被禁用，由于该版本早已过时且存在多个V8致命漏洞，攻击者通过 sgbiz: 协议注入诱导用户点击，在浏览器实现远程代码执行。

> Gen Digital是一家美国上市公司，知名杀毒软件Norton（诺顿）、Avast 都是出自这个公司。

## 二、漏洞复现

基于V15.8.0.2239(2025年8月版本)基础上复现。
![](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqMuWxRAnBuvk99ThUmygFXCJNMwPUy2YibUCicoTwTR2tgKQbA6wCAEO4kf2LCQhsvibWsZAmicrFVXTaVT37YKdGMsnicicHqYIeZKo/640?wx_fmt=png&from=appmsg "null")

演示视频：

由于该漏洞已在野利用，本人建议立即检查版本并确保自动更新。

## 三、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1.仅可用于已获得书面授权的目标系统测试；
2.遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 引用链接

`[1]` : *(https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou)*

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOq43RSf7lfRmsfht4j1OYpZFxV2yBmkPGsNJ4ROQHcUkhseQdibY4vbINt7aotxvSXjWxIEmph546T4Ql1zVcJWTgMNBkYib4ibo/0?wx_fmt=png)

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