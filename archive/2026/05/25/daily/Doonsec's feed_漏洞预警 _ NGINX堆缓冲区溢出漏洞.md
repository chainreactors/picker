---
title: 漏洞预警 | NGINX堆缓冲区溢出漏洞
url: https://mp.weixin.qq.com/s/RpBBkWt-hF5fLf9X-lskAQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:34.345554
---

# 漏洞预警 | NGINX堆缓冲区溢出漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NQlfTO30Mhy9VAFcJqlicnMTsfDRiaDBwcQnkUwVgl5VkAnCkoKM6PXs64MvIZ21OovpC5HVXtsdUWa1bkThIibSXOWx6GC4RjTE1qMQUn5KsQ/0?wx_fmt=jpeg)

# 漏洞预警 | NGINX堆缓冲区溢出漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0x00 漏洞编号**

* CVE-2026-42945

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

NGINX是一款高性能、轻量级的开源Web服务器与反向代理服务，广泛用于静态资源托管、负载均衡、API网关、缓存加速等场景，支持HTTP/HTTPS、WebDAV、HTTP/3等多种协议。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NQlfTO30MhzLVibYx3rAJIicLhHQzCQicjAKKFn5kyAPdiaEYPLic3UYeMKEbjHcPKrPiaXRc8gw5YV9vW0StiaicicfDK6YqnGomxUH1TkPD3F9LCn8/640?wx_fmt=png&from=appmsg)

**0x03 漏洞详情**

**CVE-2026-42945**

**漏洞类型：**堆缓冲区溢出

**影响：**远程代码执行

**简述：**NGINX ngx\_http\_rewrite\_module存在堆缓冲区溢出漏洞，由于其处理特定rewrite指令时，由于内部标志位管理错误，导致堆缓冲区分配长度与实际写入长度不一致，从而引发堆缓冲区溢出。未经身份认证的攻击者可通过发送构造的HTTP请求触发漏洞，造成Worker进程崩溃，在特定环境下还可实现远程代码执行。

**0x04 影响版本**

* 1.0.0 <= NGINX Open Source <= 1.30.0
* 0.6.27 <= NGINX Open Source <= 0.9.7
* R32 <= NGINX Plus < R32 P6
* R36 <= NGINX Plus < R36 P4
* 2.16.0 <= NGINX Instance Manager <= 2.21.1
* 5.9.0 <= F5 WAF for NGINX <= 5.12.1
* 4.9.0 <= NGINX App Protect WAF <= 4.16.0
* 5.1.0 <= NGINX App Protect WAF <= 5.8.0
* F5 DoS for NGINX 4.8.0
* 4.3.0 <= NGINX App Protect DoS <= 4.7.0
* 1.3.0 <= NGINX Gateway Fabric <= 1.6.2
* 2.0.0 <= NGINX Gateway Fabric <= 2.5.1
* 3.5.0 <= NGINX Ingress Controller <= 3.7.2
* 4.0.0 <= NGINX Ingress Controller <= 4.0.1
* 5.0.0 <= NGINX Ingress Controller <= 5.4.1

**0x05 POC状态**

* 已公开

**0x06****修复建议**

******目前官方已发布漏洞修复版本，建议用户升级到安全版本************：******

https://nginx.org/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7stTqD182SVPICJDGr5sbVNZO1lo2JnwVDrPBcvzPxiaiamvVZWxcxxcqQYeAiaAnXS26Hyp0wxEx5uXESx0NBQMg/0?wx_fmt=png)

浅安安全

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
在看
，轻点两下取消在看
分享
留言
收藏
听过