---
title: 东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞 附POC
url: https://mp.weixin.qq.com/s/mpjz1CQ5daPOfSgFkSzJUw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:02.706642
---

# 东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xEK7SyjATneL3wAhy0agvtxNicReNAUZIHHUibmTwZoe7gnuSWRT9Pab5tmWdic8af6U2PhWeVw0kTuubicKVVOsNtOxA96qnIUNI/0?wx_fmt=jpeg)

# 东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞 附POC

2026-5-18更新
2026-5-18更新

南风漏洞复现文库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 东胜物流软件简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

东胜物流软件是一套成熟、完善、易用的货代软件。

## 2.漏洞描述

东胜物流软件是一套成熟、完善、易用的货代软件。软件采用MS-SQLserver大型数据库，采用B/S+C/S相结合的程序架构，流程简捷、严密、灵活，功能强大。东胜系统除具有强大的内部管理功能之外，跟客户的交互功能也是东胜系统的一大特色。利用东胜货代软件开发的数据交换平台，东胜货代软件可以帮助货代企业实现跟客户之间的委托单、各种确认和通知的无纸化传送，同时实现货物状态的在线查询和短信提醒。东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

东胜物流软件
![东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6x8SbrOjxOCuwS0qzNFtv7tEOqg42YicibzMY7K2o4Czr1cNVaBXToBLezlj9Hjo7THQuu0DWD4JQ6ZbtAdq9tib787Aco9vwKWv0/640?wx_fmt=png&from=appmsg "null")

东胜物流软件CrmProxyMailListGridSource.aspx接口存在SQL注入漏洞

## 4.fofa查询语句

body="FeeCodes/CompanysAdapter.aspx"|| body="dhtmlxcombo\_whp.js"|| body="dongshengsoft"|| body="theme/dhtmlxcombo.css"

## 5.漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yyyB9WXQ4lLUb7cRnpSrw645bsLicvNibT9Ir6LmkZ92Sia9ycHjQ5JV8oDWmttarWNuoJyu3jj6bkAIcbFlSS6h91s845d1IFe0/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xkIYbMv8eYL11gSiccuWwwMdGic4Gibcswsber0OGLukyicC0wFtbhpicLBF48GYwiay2WDZNMEEj2kufOe7JbiabgJiavGFicDia3mzxWo/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xlkBx0TjBWOaXLZNGicu0vFqPRfKPJ5TEcv9ck56xLyA8p1bBicxmfOzQ2OlRHvWSghuAKcWlES5WgOptIajB71mics7LhbY0vt4/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6y2Uwv3f9nfTWLsiafqs6AV923Zibooic5jeXNGK2Yia2aTcpoGW4jiaDlzHey1BXsJmrxMmPM9GhwibFATA7UNVSU8wkmA4voQH4K3E/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yLNPjzzpiat82ol0mniavuicDmOFlyUbIhoqtzFn1DZmkdf8h3qqicT6oGibbgffZKCfSeQpRhEm673JLiadrPUoo1lMARSGapiawTSE/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yDcG6eJ5Gib2z0kbEOKr6YS4j2T6Q7uuOPIRriayLBTRLTMlLdogPicLIZiaYrCyLV2rUX4hicYasicTImJw2ED50RslNZdWAAhfay0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xAIFw8FBy7flnx8ibNamcTEVjicRZSgib7AV3eX8IPAYkSPf0HWl52Tbyf1qMElylunnkibD7MCIb7y4bcB1IjkeTe2UJhibdqsppo/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[天锐绿盾审批系统findOnlineUserForPage.do接口存在信息泄露漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490457&idx=1&sn=da12e3c7ee1c3ae2fe4f6c216ae804dc&scene=21#wechat_redirect)

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