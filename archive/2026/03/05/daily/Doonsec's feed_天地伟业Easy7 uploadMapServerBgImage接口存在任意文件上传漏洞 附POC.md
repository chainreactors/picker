---
title: 天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞 附POC
url: https://mp.weixin.qq.com/s/Ex11CFBLvrsb3cV6-R3_lw
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:27.365242
---

# 天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wUv6D6LY7ib2E4QiaGvk6T50rHvYuYE9BS0RaiaIuMwUkYWC4FwFftyQB6yvLSJL4FP50DFLYFuxBExnu90OCnGDpQoGBP1TxFiaI/0?wx_fmt=jpeg)

# 天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞 附POC

2026-3-5更新
2026-3-5更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 天地伟业简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

天地伟业Easy7

## 2.漏洞描述

天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞，攻击者可上传任意文件导致服务器被控制。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

天地伟业Easy7
![天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6wUdcOvy9VGRuqevGTkI1K4aaCBOKFcJ2dGfxhCRPZMaIoU35wmay2j9FVsYOVDTkzLib0XrYBkUeAcMk0Ficqx5ibA4CK81ZfVVU/640?wx_fmt=png&from=appmsg "null")

天地伟业Easy7 uploadMapServerBgImage接口存在任意文件上传漏洞

## 4.fofa查询语句

app="Tiandy-Easy7"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/Easy7/rest/file/uploadMapServerBgImage

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6ypicnLuic9XUVMGiaUY6Q1I0USXPsDQtWLa5rpXRY1yjAmcHWFSjiatxO6sWnskFIUFTbSCJbbQMKMiaMkqWxY3rMvicKLjMiccnIQo0/640?wx_fmt=jpeg&from=appmsg "null")

访问上传的文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yBoDDTlCKppFLJMJGCDpZr7M8nEb0ITswSxyjucepn7YzKOz5b9OfxjxYQNc3zwZiagXaYPNNK1ABwh7BDlQQ8uA2odzD4Xfbk/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xEKY3GA2LQ9ibYGNhxtodSw0ZbaQa2OyaZJDoAibXWxyJ8uoScCicwPErZSYuicUZVJ7nRVfsiaxk023oy1HWB5dx8EZubGJvRGYZ0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zhJJfLxcx6sqmLic6cZnxJY2GOR6rDcJsYAiarmM0Dehx5Gm6BnbKXCukRlicmtic0OEeKF8ibNIARfbeA3ibjMUcuhG2Gdf9icC2PB0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xpqbtcEHGHdFtCNnBFe0sj5yJokkVOMfF0MRr9Km78r1ePLrMr8hJlK0HbKcPeZ2pSSIOOob9t0vU8NS2bJWovbqdqqU0ffvE/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wiclkgibgHMHayWrCxkic8PYpxsUIwqlnt332g93LWFCgXKiaDtYISUr1LBlkR4jPZF2Ddic8f2BD0PhG1IqKGKQdv4MDLFWPSs08Y/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yrxRBI43EIwPe6yykyTEklLYVCbPQCM09qycDRCjKRTyuuSnamrnBICXiby10asdt9FZ22kmozU98uCXia69Qt1icIbFAIia0beQ0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yA3SaxbPlJx8Gyxxe2gkK3ibv3oto7I7m0WZa1GzAOcaRejATU9wGFDOKbl0l3NjVBe4DjXL3oxVrqJZXZ7DicJDkiazibrqkH0Hw/640?wx_fmt=jpeg&from=appmsg "null")

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