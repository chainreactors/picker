---
title: CNNVD | 关于Fortinet FortiOS和FortiProxy安全漏洞的通报
url: https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664234775&idx=3&sn=82b000440fa4c60ceae4b17d4472d670&chksm=8b59fdeebc2e74f8f1e114cc8a17881077bd3708e814560f198b1085ef506d998bb5bd1dec9b&scene=58&subscene=0#rd
source: 中国信息安全
date: 2025-01-17
fetch_date: 2025-10-06T20:11:17.493999
---

# CNNVD | 关于Fortinet FortiOS和FortiProxy安全漏洞的通报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yhw0GnfOW6tXc2djenonWyttRzqsqgjHJD0ZrGFPwdKGW6DiaLicLsU5TgguiajEFLicuTb1nwAOypGg/0?wx_fmt=jpeg)

# CNNVD | 关于Fortinet FortiOS和FortiProxy安全漏洞的通报

中国信息安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yhw0GnfOW6tXc2djenonWyyicavSOBEX2dXm5WzVyYLxvcQpibIQF3UBZhYzAwWqN9W7vybTic0UEVA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yhw0GnfOW6tXc2djenonWy0vaDdicbo7DNHD5h9q6fOFVPF5UAnon9s7L0ExFm2ewcm02GwX6wZbQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yhw0GnfOW6tXc2djenonWyyicavSOBEX2dXm5WzVyYLxvcQpibIQF3UBZhYzAwWqN9W7vybTic0UEVA/640?wx_fmt=gif&from=appmsg)

**扫码订阅《中国信息安全》**

邮发代号 2-786

征订热线：010-82341063

**漏洞情况**

近日，国家信息安全漏洞库（CNNVD）收到关于Fortinet FortiOS和FortiProxy安全漏洞（CNNVD-202501-1747、CVE-2024-55591）情况的报送。未经身份验证的远程攻击者可以通过向Node.js websocket模块发送特制请求，进而获得超级管理员权限。FortiOS和FortiProxy多个版本均受此漏洞影响。目前，Fortinet官方已发布新版本修复了漏洞，建议用户及时确认产品版本，尽快采取修补措施。

## 一 **漏洞介绍**

Fortinet FortiOS和Fortinet FortiProxy都是美国飞塔（Fortinet）公司的产品。Fortinet FortiOS是一套专用于FortiGate网络安全平台上的安全操作系统。Fortinet FortiProxy是一种安全的网络代理，通过结合多种检测技术，如Web过滤、DNS过滤、DLP、反病毒、入侵防御等保护用户免受网络攻击。

FortiOS和FortiProxy中存在一个身份认证绕过漏洞。未经身份验证的远程攻击者可以通过向Node.js websocket模块发送特制请求利用该漏洞，进而获得超级管理员权限。

## 二 **危害影响**

FortiOS 7.0.0版本-7.0.16版本，FortiProxy 7.2.0版本-7.2.12版本，FortiProxy 7.0.0版本-7.0.19版本均受漏洞影响。

## 三 **修复建议**

目前，Fortinet官方已发布升级补丁修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方参考链接如下：

https://fortiguard.fortinet.com/psirt/FG-IR-24-535

本通报由CNNVD技术支撑单位——奇安信网神信息技术（北京）股份有限公司、浪潮电子信息产业股份有限公司、锐捷网络股份有限公司、中孚安全技术有限公司、北京神州绿盟科技有限公司、西安交大捷普网络科技有限公司、深信服科技股份有限公司、中国电信股份有限公司网络安全产品运营中心、山西轩辕信息安全技术有限公司、贵州粟詈网络科技有限公司、京铁云智慧物流科技有限公司、北京国科数安科技有限公司、北京门石信息技术有限公司、沥泉科技（成都）有限公司、北京时代新威信息技术有限公司、杭州安恒信息技术股份有限公司、广州非凡信息安全技术有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。

联系方式：cnnvd@itsec.gov.cn

（来源：CNNVD）

**分享网络安全知识 强化网络安全意识**

**欢迎关注《中国信息安全》杂志官方抖音号**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yhw0GnfOW6tXc2djenonWy5GtnHBgZzK3S3qhfGIaUkHHE8sy2S0gC6jzM5RIjRITxcNRibbRkekw/640?wx_fmt=jpeg&from=appmsg)

**《中国信息安全》杂志倾力推荐**

**“企业成长计划”**

**点击下图 了解详情**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yhw0GnfOW6tXc2djenonWyMLSOZjZSwicMNxprYJCSWldCSxD9e4tWVeK7eVvec8We7YJt5EX6VdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664162643&idx=1&sn=fcc4f3a6047a0c2f4e4cc0181243ee18&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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