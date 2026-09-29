---
title: 全球安全动态日报｜20260928｜早
url: https://mp.weixin.qq.com/s/NkrEO5aYF4qKMAGNCBNavQ
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:17.416273
---

# 全球安全动态日报｜20260928｜早

# 全球安全动态日报｜20260928｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260928｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年9月27日共收录2条安全动态，内容涵盖Lunex Stealer 窃取浏览器凭据与 Citrix NetScaler 零日漏洞遭利用。

The Hacker News **2**  ·  HackerOne **0**

## The Hacker News

### 01 Lunex Stealer 滥用 AMD 驱动禁用安全监控并窃取浏览器凭据

**公开时间：**2026年09月27日 02:22

AI 解读

Ontinue称，针对乌克兰语用户的攻击链通过遭入侵网站投放仿Cloudflare验证的ClickFix诱饵和虚假MSI安装包，部署LunexLoader及Psychedelic Stealer。该恶意软件利用存在CVE-2023-20598漏洞的AMD驱动实施BYOVD，通过使安全进程失去监控能力来规避防护，并窃取七种Chromium浏览器的凭据、会话Cookie及加密货币钱包数据。它还可通过注册表、计划任务和Chrome原生消息主机持久化，获得文件读写、下载及运行程序等远程控制能力。Lunex是向多个犯罪团伙提供服务的MaaS平台，相关控制面板数量已扩展至13国。

原文：https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html

### 02 警告：两个未修复的 Citrix NetScaler RCE 零日漏洞正遭活跃利用

**公开时间：**2026年09月27日 00:00

AI 解读

Citrix于9月27日确认，NetScaler ADC和NetScaler Gateway中的两个严重漏洞已在修复公开前遭到利用：CVE-2026-88771为无需认证的输入验证缺陷，所有受影响版本部署均受影响，可执行任意命令；CVE-2026-88772为内存溢出漏洞，可导致远程代码执行或拒绝服务，默认启用DTLS的VPN虚拟服务器通常受影响。两者CVSS v4均为9.5。Citrix未披露攻击范围、攻击者或起始时间，并同时发布了这两项及另外六项漏洞的修复版本。

原文：https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR11faXJ0UdaBIUhfHacBNtw8Z6Iks164OUibPoicia0Jy5fMQhge26aRftv1Ky9GC7QBCibIciaqzLIZHibSaXVYXpwApbic3sWOAxsib4/640?from=appmsg)

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1oKre7rbnJe6BxfvWUT6Uibz0WwGqXuvtRFYicibfTQDhDymFj0rTsyTLlVvOFdzm3wDV9TlqibHDG5UHRfLBPKMiadz3SYOjk0Bo4/0?wx_fmt=png)

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