---
title: CNNVD通报OpenSSH安全漏洞情况
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651130970&idx=2&sn=fbce5a8193aba744bdff50c3be2e899d&chksm=bd15bc898a62359fb9b9ff7e749aaba4843671818fd3332d91ccaeeb67212a43b1419e7268c7&scene=58&subscene=0#rd
source: 安全牛
date: 2024-07-05
fetch_date: 2025-10-06T17:43:57.433896
---

# CNNVD通报OpenSSH安全漏洞情况

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB4OjKeicE6QMV5DNFj91lSzzXr8H5m6Xk781awb7FY3EIxibVAYbtCCM90TfUqkrGFP4guf1mGSibgA/0?wx_fmt=jpeg)

# CNNVD通报OpenSSH安全漏洞情况

安全牛

**漏洞情况**

近日，国家信息安全漏洞库（CNNVD）收到关于OpenSSH安全漏洞(CNNVD-202407-017、CVE-2024-6387)情况的报送。攻击者可以利用该漏洞在无需认证的情况下，通过竞争条件远程执行任意代码并获得系统控制权。OpenSSH多个版本受该漏洞影响。目前，OpenSSH官方已发布新版本修复了该漏洞，CNNVD建议用户及时确认产品版本，尽快采取修补措施。

## 一 **漏洞介绍**

OpenSSH是加拿大OpenBSD计划组的一套用于安全访问远程计算机的连接工具。该工具是SSH协议的开源实现，支持对所有的传输进行加密，可有效阻止窃听、连接劫持以及其他网络级的攻击。该漏洞源于信号处理程序中存在竞争条件，攻击者利用该漏洞可以在无需认证的情况下远程执行任意代码并获得系统控制权。

## 二 **危害影响**

OpenSSH 8.5p1版本至9.8p1之前版本均受该漏洞影响。

## 三 **修复建议**

目前，OpenSSH官方已发布新版本修复了该漏洞，CNNVD建议用户及时确认产品版本，尽快采取修补措施。官方更新版本下载链接：

https://www.openssh.com/txt/release-9.8

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。联系方式: cnnvdvul@itsec.gov.cn

![](https://mmbiz.qpic.cn/mmbiz_gif/tV4JDvMn6RMFN7ExSt7AEhx1DPNW68Bt8SXrAelC5L01auTNJkN19gJn8zP0hPAhSMHibfRNj70fV2aDD6u681Q/640?&wx_fmt=gif&tp=wxpic&wxfrom=5&wx_lazy=1)

文章来源：CNNVD安全动态

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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