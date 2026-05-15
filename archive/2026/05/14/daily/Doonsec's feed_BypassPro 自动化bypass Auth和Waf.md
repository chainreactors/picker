---
title: BypassPro 自动化bypass Auth和Waf
url: https://mp.weixin.qq.com/s/V5NJMWePGlf31dTUFrdr8A
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:38.960773
---

# BypassPro 自动化bypass Auth和Waf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnpNbFlrGc63fl0WyVoUibRnaSDIW0MkG3Bj1icjibWKnu4icGcn4uvkJ5RveCrSOQaJHt0zSb0SRCf85XgVZicl4WqCVng1KDWxSOI/0?wx_fmt=jpeg)

# BypassPro 自动化bypass Auth和Waf

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 406，阅读大约需 3 分钟

## 前言

**BypassPro** 对 Auth/Waf 自动化 bypass 的 burpsuite 插件
项目地址：https://github.com/0x727/BypassPro

![17bc66f818591d8f7464e6a28dfd8923.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkDxZoqHKDqoDcIroB7tMnOulszZEAnlAgQHJNELkRqpXlvMLoXAoyMkZ2HAnB6A3IicfWQwB7o0cVrKYgeWVcibcyJsho0k2Lbw/640?from=appmsg "null")

17bc66f818591d8f7464e6a28dfd8923.png

BypassPro 5.1 进行了一次大版本重构：从单一的 403 bypass 工具，扩展为“自动权限绕过 + 自动 WAF 绕过 + 手动 WAF 工作台”的组合型 Burp 插件。本版本重点增强了手动构造能力、Ghost Bits 测试能力、Raw Socket 发包能力和配置可维护性。

## 使用

Burpsuite 安装插件
![88fe8d17165c934dd8053819039d9a81.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmnW05TmxElu6h5gJf2WMTiccAL4dlbpP9TT1A6hib8XJyJ6TtL4F9NwhicHyrLyQ468TdhqVnpeic5EWicMIJ8SxmPBJHKAarkZ8pE/640?from=appmsg "null")

88fe8d17165c934dd8053819039d9a81.png

选择请求包
![f431d4441ce655fa65fa9146c2717cda.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk2eu6yu7GSmC2y31iarfJXWHVbmyAQ1Yq7XxpNWrem3syvLQ3qFgU1u5gUxqGwx9YsSMqyrvibxQCUXibtcgENtEIibNxopVo8UBc/640?from=appmsg "null")

f431d4441ce655fa65fa9146c2717cda.png

第一种，**访问控制绕过**
![0fd80000724f7702c7a6f1490f976161.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnd0NI9TiaNT8mLicpIRlL3UnSclH4PsqujPE3LibxQK8FTQeGKx9TzLBFhEAxeJH13eTdIvlIKtqazBxjBgkmOdjKXZuZ4jWECmc/640?from=appmsg "null")

0fd80000724f7702c7a6f1490f976161.png

第三种，WAF 绕过
![afb422aa8f77bbe286003d87971130c6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlSnIZ82SxMIdbMtd41lJNr6SoAXvk02C5Gp0AGHbiciaRkDxiayXkdl3Fg6naUxgXqSwI0udkoRGcgRP7Vicrtia0lyNWNvTCPlbMI/640?from=appmsg "null")

afb422aa8f77bbe286003d87971130c6.png

## 介绍

**Auto-权限绕过**

* • 入口：`Send to BypassPro (Access Control)`，以及 Dashboard 中的 Auto Scan。
* • 配置：`profiles.auto_access_bypass`。
* • 用途：面向 401/403、权限绕过、访问控制绕过场景。
* • 规则：suffix / prefix / boundary\_insert / headers。

**Auto-WAF 绕过**

* • 入口：`Send to BypassPro (WAF)`。
* • 配置：`profiles.auto_waf_bypass`。
* • 用途：对指定请求自动生成 WAF 绕过变体。
* • 能力：

+ • Path / Header 规则变形。
+ • Body Charset 编码：UTF-16 / UTF-16BE / UTF-16LE / UTF-32 / UTF-32BE / UTF-32LE / IBM037。
+ • Body Transform：Gzip。
+ • Content-Type 伪装：form-urlencoded / multipart / text/plain。
+ • Ghost Bits 自动绕过：基于原请求已有 token 生成 `eq` / `parser` 候选，场景模板默认关闭。

**Manual-WAF 工作台**

* • 入口：`Send to BypassPro (Manual WAF)`。
* • 用途：把请求送入手动工作台，像 Repeater 一样编辑、组合、发送，但工具栏专门面向 WAF/解析差异绕过。
* • 特点：

+ • 使用 Burp 原生 `IMessageEditor`，支持 Pretty / Raw / Hex。
+ • 支持 Host / Port / HTTPS 手动修改。
+ • 支持 Send / Cancel / Reset / Undo / Redo。
+ • 支持 Follow Redirect，最大跳转次数读取 `general.max_redirects`，默认 3。
+ • 支持 History，便于回放和对比。

## 总结

项目地址：https://github.com/0x727/BypassPro

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

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