---
title: 漏洞预警 | Copy Failh和Dirty Frag的好兄弟fragnesia来了
url: https://mp.weixin.qq.com/s/3eRqRxiI9zVAc-irKZEThQ
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:47:12.877535
---

# 漏洞预警 | Copy Failh和Dirty Frag的好兄弟fragnesia来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hvMQKkLOqzO1h8pVIsbxrDrsxu6sIia9G0cnb0ibLB2zgPmjrqCUuUajwjmCaDv5xoOKKqClEJMjHXO6XcrjMhYA/0?wx_fmt=jpeg)

# 漏洞预警 | Copy Failh和Dirty Frag的好兄弟fragnesia来了

永恒之锋实验室
永恒之锋实验室

Eonian Sharp

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## Fragnesia

### 漏洞介绍

Fragnesia 是 Dirty Frag 漏洞家族的独立新变种，源自修复 Dirty Frag 时引入的新缺陷。漏洞利用计算 TCP 中密码传输的 iv ，通过密码逻辑缺陷覆盖内存中 /bin/su 的缓存, 不同于前置CVE-2026-43284 dirtyfrag通过堆栈溢出进行篡改

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibqMe2MTXibicGdfO0wIib62XyYtCwn38OQ6RIwwzdZctC27bicoic21p1mzfX8DUdudOTgMrF0MDOybVvZ7ubm2ibwia9XHR7GP9gbiass/640?wx_fmt=png&from=appmsg)

### 影响版本

```
cef401de7be8 到本次修复之间的所有相关内核版本
```

### 修复建议

应用供应商提供的修复底层 XFRM ESP-in-TCP 漏洞的内核补丁（一旦可用）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hvMQKkLOqzNNkekloMAmic2Mib0ykvxKXS5LvtwtGCgvvoKr4ODdarNPTRia5SMqCGsKiclafYGuQW4uqrdeMUFkuQ/0?wx_fmt=png)

Eonian Sharp

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hvMQKkLOqzNNkekloMAmic2Mib0ykvxKXS5LvtwtGCgvvoKr4ODdarNPTRia5SMqCGsKiclafYGuQW4uqrdeMUFkuQ/0?wx_fmt=png)

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