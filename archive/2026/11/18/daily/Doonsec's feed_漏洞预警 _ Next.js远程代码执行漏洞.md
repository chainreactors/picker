---
title: 漏洞预警 | Next.js远程代码执行漏洞
url: https://mp.weixin.qq.com/s/DwgTvBTzsmseGN9GFnvVKg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:42.800389
---

# 漏洞预警 | Next.js远程代码执行漏洞

# 漏洞预警 | Next.js远程代码执行漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x00 漏洞编号**

* # CVE-2026-126187

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

Next.js是Node.js生态中基于React的开源Web框架，其通过Server Actions功能提供了后端开发能力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXuxF6aeAAAcJpby4ECRt8pVzjgiaOP6LdpyObdiaUPjyEbpZGFArqpsIRJFreSTW9NOahpf6QNRnbw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

**0x03 漏洞详情**

**CVE-2026-126187**

**漏洞类型：**远程代码执行

**影响：**执行任意命令

**简述：**Next.js存在远程代码执行漏洞，由于其Flight序列化器在处理多个TypedArray视图共享同一个ArrayBuffer的场景时存在逻辑缺陷，未经验证的攻击者可通过构造单个未认证请求触发服务端代码执行，进而执行任意代码。

**0x04 影响版本**

* 16.0.0 <= Next.js <= 16.4.0

**0x05****POC状态**

* 已公开

**0x06****修复建议**

********目前官方已发布漏洞修复版本，建议用户升级到安全版本**************：******

https://nextjs.org/

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7stTqD182SVPICJDGr5sbVNZO1lo2JnwVDrPBcvzPxiaiamvVZWxcxxcqQYeAiaAnXS26Hyp0wxEx5uXESx0NBQMg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过