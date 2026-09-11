---
title: 大华智慧园区综合管理平台queryById接口存在敏感信息泄露 xa0附POC
url: https://mp.weixin.qq.com/s/Nsip3mfrydYirZEZ5kFs2g
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:47:56.400818
---

# 大华智慧园区综合管理平台queryById接口存在敏感信息泄露 xa0附POC

# 大华智慧园区综合管理平台queryById接口存在敏感信息泄露  附POC

2026-9-10更新
2026-9-10更新

南风漏洞复现文库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 大华智慧园区综合管理平台简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

大华智慧园区综合管理平台是一款集视频、报警、门禁、对讲四大安防子系统管理功能于一体的综合管理平台。

## 2.漏洞描述

大华智慧园区综合管理平台是一款综合管理平台，具备园区运营、资源调配和智能服务等功能。平台意在协助优化园区资源分配，满足多元化的管理需求，同时通过提供智能服务，增强使用体验。大华智慧园区综合管理平台queryById接口存在敏感信息泄露。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

![大华智慧园区综合管理平台queryById接口存在敏感信息泄露](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6xDO7icmibm89rzFxtBeflnCtjJ5lyuhRkdUO4LNNe5177WsBicibXh4dYBWUyfCsd9WZibRcDK9HicCakeNYCZd38wvIEMl9cFqRumw/640?wx_fmt=png&from=appmsg)

大华智慧园区综合管理平台queryById接口存在敏感信息泄露

## 4.fofa查询语句

"/WPMS/asset/lib/gridster/"||app="dahua-智慧园区综合管理平台"

## 5.漏洞复现

漏洞链接：https://xx.xx.xx.xx/CardSolution/card/visitor/appointment/..;/..;/..;/card/person/queryById

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zQPmYtW4DrZQOSwoDP42DSzE2xr09qmNxVdpiaD9qvuymytt1ib9pZqxy1elNsdR7aBu7fUq9Ngd03U04U8ic41KNuQY7Ta0XkLI/640?wx_fmt=jpeg&from=appmsg)

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wjY1LSQSxYXjXoKacicCjC96me26cSsGAVo3OYwgGrE1iaACMd5fMB7lxZGW4MMHwdB0zdK0xuQOYnuNUGzFdIR6NEfh0q8z3bI/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yibvjkuyv5nYpnH2tVDY0SlP4hx6xYUDfq4d2tzW5j1o4Joicea1K0rfgTZS4VupIzvUc0ealzwt80q1gVv94ibZ7eI6zOUgBukY/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wrSrUcCoiaFFv0qunic3CqGribiauGVOmzMmPreaK1V1IKJ53LmPu0O8htUU1hjZIYX6AcIkyriaXmiaJbDw7Sf7VjCWwnu9zzhZs5g/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6x149GibDCmQtibZ7Kuv2ictwNd6sUKMjxCBgVWD4KW5OT3fwF5zp26EC2mvZne85UwmHQoKfLsb2Xs9IWlRDfGicM0PzUwD26d9IM/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xW71EvGL63p2z9bzeibUicecMnTBvQkNicnlpic52nb4QMpVkfPctoLCzFojIanWGRSKXDB7IXJpNrb0jJGCqDy6IibrZHjjBB8yZY/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xiavNf7wMiaHg9vEiazMhmPAzKg9UVNjHww2juZ2y0hicjLEkWALzTsdGtpxzQlichzZzfsVPkRRRYO4dOyBGwYysqHiboLRFX9BAP0/640?wx_fmt=jpeg&from=appmsg)

## 7.整改意见

厂商尚未提供相关漏洞补丁链接，请关注厂商主页随时更新： https://www.dahuatech.com/

## 8.往期回顾

预览时标签不可点

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