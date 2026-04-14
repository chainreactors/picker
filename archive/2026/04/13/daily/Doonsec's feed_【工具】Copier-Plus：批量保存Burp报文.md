---
title: 【工具】Copier-Plus：批量保存Burp报文
url: https://mp.weixin.qq.com/s/3jSK5Nya9YFExgeiehe0zA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:32.446964
---

# 【工具】Copier-Plus：批量保存Burp报文

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fL1TQ0l0Qw29dOgecRStQjDXPiaOFLnMtpicZWJicpfN0dRMtk1Y2xd2lBJic0hLNfZ81KOl4vKXv9ZZFbSlCCvpOh9H3oCgLxTpMKglwI3DdLI/0?wx_fmt=jpeg)

# 【工具】Copier-Plus：批量保存Burp报文

原创

酒零
酒零

NOVASEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZABNHic6I2k8vayq06GiaN0PjuJtkhP7vxlCDuQbSnofqkMWgjtQCZqKTrdm330DH5kk8NgibIR3cNQQ/640?wx_fmt=png&from=appmsg)

**0x00 前言**

**免责声明：继续阅读文章视为您已同意[****[NOVASEC免责声明](http://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489726&idx=1&sn=e5459d91f53caf90e76c6558dc8b4ac9&chksm=fad4c5a9cda34cbf0d02c24383827a906e7d08d5694d452a0cc18988f130abab371735ee1843&scene=21#wechat_redirect)****].**

*****注：本文属于推荐系列文章，所推荐内容并非全部由本团队开源实现。文章旨在分享各类优质项目，提升其关注度与影响力，文中观点仅代表作者个人看法。若您有更合适的替代项目，欢迎在留言区推荐分享，共同推荐优质项目资源。*****

项目介绍

Copier 是 Burp Suite 的一个扩展，允许用户轻松复制请求和回复，同时使用自定义规则进行自动修改。使得请求和响应可以轻松复制到报告中，无需编辑去大 Cookie 值、多余的头部或敏感数据

原项目仅支持Copy清理后的报文，但没有提供文件保存功能，在原项目的基础下，实现了批量报文保存功能。

支持设置配置多种方式，批量复制指定报文的指定部分，比如复制请求url和响应体,  复制请求和响应 等等

我的使用主要是实现一些批量报文的保存。

扩展功能

```
1、允许正则替换内容框为空2、增加 LocateRule, 用于标记仅提取 Location部分报文3、增加 EnabledBase64, 用于确定是否对报文内容进行Base64编码4、增加 jsonFormat框 , 用于确定是否输出Json格式的结果5、支持多种方式保存【剪贴板、单文件、多文件】
```

常用配置：复制请求行和响应体

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fL1TQ0l0Qw0Ma57sRT1I8cdQiayIfQHhWtHb1J9lI1rpLMdlOCicoh7PREorU8iaoEAWpiaz0bx3yViccrIkMrRpnVQIC7lH2uiaicbOdAibpCXVB98/640?wx_fmt=png&from=appmsg)

****原项目地址****

```
https://github.com/Tib3rius/Copier
```

****本项目地址****

```
https://github.com/winezer0/Copier-Branch
```

注意：该插件使用的是高版本 montoya-api Jdk 较高版本语法 需要使用新版burp (2024+)

![](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZD7m4f7uBkNfCG8BjypNEukTBkZDVyuJ2K8UM07dDyQxKM0XEyUgJ0pgl3BlrFLntreOnoe3uTwaw/640?wx_fmt=jpeg)

NOVASEC

![](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZD7m4f7uBkNfCG8BjypNEukN0Ht6Ha0XsryrmS5PAmaVeyzb3JzsH5ibx6DmpHq9e8agwMkccrwNSQ/640?wx_fmt=jpeg)

WINEZER0

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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