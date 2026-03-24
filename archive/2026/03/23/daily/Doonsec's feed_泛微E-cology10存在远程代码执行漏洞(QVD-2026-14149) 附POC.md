---
title: 泛微E-cology10存在远程代码执行漏洞(QVD-2026-14149) 附POC
url: https://mp.weixin.qq.com/s/-IJ-Z2s-pVbkQJHzNSM26w
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:47.195862
---

# 泛微E-cology10存在远程代码执行漏洞(QVD-2026-14149) 附POC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xUUdmR9T1ic9aEmsmcC6Xr9wfy1KcZZ3ic8e4ucIsffGp0yomRXlgaAiaP3yc2K2Ir7LjLZNFh0xgRcPHznmFZCZB7HicIEmXiaszU/0?wx_fmt=jpeg)

# 泛微E-cology10存在远程代码执行漏洞(QVD-2026-14149) 附POC

2026-3-23更新
2026-3-23更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 泛微E-cology10简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

泛微 E-cology10（简称 E10）是上面向中大型组织的数智化协同运营平台

## 2.漏洞描述

泛微 E-cology10（简称 E10）是面向中大型组织的数智化协同运营平台，定位为企业级数字化中枢，核心覆盖协同办公、流程管理、业务集成、知识管理、低代码开发等全场景能力。 未经身份验证的远程攻击者可利用该漏洞向特定接口发送恶意请求，在目标服务器上执行任意代码，进而获取服务器权限。泛微E-cology10 远程代码执行漏洞(QVD-2026-14149)

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

泛微E-cology10
![泛微E-cology10存在远程代码执行漏洞(QVD-2026-14149)](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6yXffgIDwvG4cPy9AbhuqtiaB3t5pQ2Uicib8EEQwGzECusFJrQO25N8x7P3Tn6Zn8p89lzXoebXCBIR6qUaXBLLDic5dxzZGJQqyc/640?wx_fmt=png&from=appmsg "null")

泛微E-cology10存在远程代码执行漏洞(QVD-2026-14149)

## 4.fofa查询语句

icon\_hash="-1619753057"

## 5.漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wQ3f6FMCWUWHoqFmlaMS0DmLMsoJoicQAicWT4OrKQKGbQLY593Wu26IAwt4FlnO5krEEptYobcMNetrrqpYUjiacavIKwRBaDx4/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wqAWPKB8tOJcrODibjICTaNuvYnegJFcvyPJecmxJ2l75yBLjerQNpOG7eVicbKibBN4fJfa8mmjT1lUkJ4hBtL2f0kbacCHP7IA/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6w37UbcZmOIpb7TBhich9wFjIkP9pTQq7TCZo2vs4eiaXDtLsXulfjjElSJ56Jq9zBULBYoF3kMaxlfxhoZuKianWxoFwO3ZvsB6w/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xRTspXMAtxxia0NVKAUJYJ9pR8W4Cgp8HmKIaJF71OsHsqUJBw3hvjSXFXqUtET83YHsLNVcvIUeO3fhDdbFVruq0G2xkj9ZjY/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6z7yltX7RgQGSpwML6biaZF5mXNpL9we7TKZCNTKUJkN7JFq0q8rB7ZCdLcluQmJushWaSjsLbnYe7Os3DBfR2Sib6KwdpOibcHp4/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zfG5ib71P7EOxicR4VEPSBc7CciaoNJX8GfOgQ3ndeEEh5Ws4nEWy7AemepTyTRibEiaUXZUGYzhkmibEzVF3fYPOhumLPfsxSB535c/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xt9p9PWCu7o1ZFKLtTibQFOP0zhAW1o98ODo5N1TjVqGqicxw5daXd4zficQgNFVQOPkXGeNt5ia5hsYxQj630fKq1NM00jCXk6x0/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[Omnissa Workspace ONE UEM存在敏感信息泄漏漏洞（CVE-2025-25231） 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490183&idx=1&sn=8542814477aa13cdb4c824518998af46&scene=21#wechat_redirect)

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