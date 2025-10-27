---
title: 利用旧的ThinkPHP和ownCloud漏洞的攻击事件激增
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581171&idx=1&sn=322267dfcff7b72c9907e1bfeb0e3ac5&chksm=e9146dc9de63e4dff4e79f5350c061c75033f964a32277104652b1f9f46fcf63f657ace60f6d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-18
fetch_date: 2025-10-06T20:40:14.994974
---

# 利用旧的ThinkPHP和ownCloud漏洞的攻击事件激增

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib12eicKmIIRRyKsgeicIBCuEUwAdgq9LtBFDb7ygVAy0FJcnicUVr6DGJNOZgVCCzrTSMlGZHA3yp5A/0?wx_fmt=jpeg)

# 利用旧的ThinkPHP和ownCloud漏洞的攻击事件激增

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

威胁监测平台GreyNoise报告称，越来越多的黑客正试图破坏维护不善的设备。攻击者利用CVE-2022-47945和CVE-2023-49103攻击ThinkPHP框架和开源ownCloud文件共享和同步解决方案。

这两个漏洞都具有临界严重性，可以被利用来执行任意操作系统命令或获取敏感数据（例如管理员密码、邮件服务器凭据、许可密钥）。

第一个漏洞是6.0.14之前的ThinkPHP框架语言参数中的本地文件包含（LFI）问题。未经身份验证的远程攻击者可以利用它在启用了语言包特性的部署中执行任意操作系统命令。

根据威胁监测平台GreyNoise的说法，CVE-2022-47945目前正受到大量利用，攻击的源ip越来越多。

该公告警告说：“GreyNoise已经观察到572个独特的ip试图利用这个漏洞，并且最近几天活动不断增加。”

尽管它的漏洞预测评分系统（EPSS）评级很低，只有7%，而且该漏洞没有被包括在CISA的已知被利用漏洞（KEV）目录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib12eicKmIIRRyKsgeicIBCuEwXT86buEsffFGiardpbvarnuCOFw5C8dpbSNlQkicpmgibxBMHx0RX3pQ/640?wx_fmt=png&from=appmsg)

日常开发活动

第二个漏洞影响了流行的开源文件共享软件，它源于应用程序对第三方库的依赖，该库通过URL公开了PHP环境细节。

在开发者于2023年11月首次披露该漏洞后不久，黑客就开始利用它从未打补丁的系统中窃取敏感信息。

一年后，CVE-2023-49103被FBI、CISA和NSA列为2023年被利用最多的15个漏洞之一。

尽管自供应商发布解决安全问题的更新以来已经过去了2年多，但许多实例仍然未打补丁并暴露在攻击之下。GreyNoise最近观察到CVE-2023-49103的利用增加，恶意活动来自484个唯一的ip。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib12eicKmIIRRyKsgeicIBCuEaK0JIRvCG5Ix6bcp7ibsnZOjib3I3NUA8E4kzePI4lGAOpTZCdn6RyFQ/640?wx_fmt=png&from=appmsg)

每天针对ownCloud的ip

为了保护系统免受主动利用，安全研究员建议用户升级到ThinkPHP 6.0.14或更高版本，并将ownCloud GraphAPI升级到0.3.1或更高版本。并建议将潜在易受攻击的实例离线或放置在防火墙后面，以减少攻击面。

参考及来源：https://www.bleepingcomputer.com/news/security/surge-in-attacks-exploiting-old-thinkphp-and-owncloud-flaws/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib12eicKmIIRRyKsgeicIBCuE5tmrwOG0iaQiaB1UtqUibeuWl9BAeyzjFiclJldKEjkoMPo6Y8qiaAXqbLg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib12eicKmIIRRyKsgeicIBCuEibo6ICU4p5MuAuicg00LQmzYkyp78yW2utO1NJWFUTTQicbicC9TvdlhyA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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