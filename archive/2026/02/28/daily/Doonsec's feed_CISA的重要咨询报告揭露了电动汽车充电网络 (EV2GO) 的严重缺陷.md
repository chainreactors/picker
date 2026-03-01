---
title: CISA的重要咨询报告揭露了电动汽车充电网络 (EV2GO) 的严重缺陷
url: https://mp.weixin.qq.com/s/3XB-2oiDUen4LgB_AY5O9Q
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:23:59.122169
---

# CISA的重要咨询报告揭露了电动汽车充电网络 (EV2GO) 的严重缺陷

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/y1BJgHFkOkoqdEhOurAGtAAjZyR0ndeNLicF8PU9afPaOgZUXUay3f5qYDrlicFDMwEicpXPyB9qB5AEbLNHKnOe69KVOeicfCFQLGKgFHwVcto/0?wx_fmt=jpeg)

# CISA的重要咨询报告揭露了电动汽车充电网络 (EV2GO) 的严重缺陷

sec随谈
sec随谈

sec随谈

![]()

在小说阅读器中沉浸阅读

电动汽车正迅速成为道路上的新标配，但为其提供动力的基础设施正面临着严峻的新型数字威胁。美国网络安全和基础设施安全局 (CISA) 发布了一份重要的工业控制系统 (ICS) 安全公告，指出EV2GO 充电平台存在严重漏洞。

该警报（ICSA-26-057-04）于2026年2月26日发布，指出了一系列安全 漏洞，这些漏洞可能使网络犯罪分子对电动汽车充电网络拥有惊人的控制权。随着电动汽车普及速度的加快，保护这些公共和私人充电站的安全与保护电网本身的安全同等重要。

核心问题在于这些充电站如何与中央网络通信和进行身份验证。根据美国网络安全和基础设施安全局 (CISA) 的官方咨询，“成功利用这些漏洞可能使攻击者能够冒充充电站、劫持会话、抑制或错误路由合法流量以造成大规模拒绝服务攻击，以及篡改发送到后端的数据”。

该公告明确指出，目前所有产品线均受到影响。本次披露中追踪的具体漏洞包括：

* CVE-2026-24731 (CVSS 9.4)：WebSocket 端点缺乏适当的身份验证机制，攻击者可利用此漏洞冒充充电站并篡改发送到后端的数据。未经身份验证的攻击者可以使用已知或已发现的充电站标识符连接到 OCPP WebSocket 端点，然后以合法充电站的身份发出或接收 OCPP 命令。由于无需身份验证，这可能导致权限提升、对充电基础设施的非法控制以及向后端报告的充电网络数据遭到破坏。
* CVE-2026-25945 (CVSS 7.5)：WebSocket 应用程序编程接口缺少对身份验证请求数量的限制。这种速率限制的缺失可能允许攻击者通过抑制或错误路由合法的充电器遥测数据来发起拒绝服务攻击，或者发起暴力破解攻击以获取未经授权的访问权限。
* CVE-2026-20895 (CVSS 7.3)：WebSocket 后端使用充电站标识符来唯一关联会话，但允许多个端点使用相同的会话标识符进行连接。这种实现方式导致会话标识符可预测，并允许会话劫持或会话影子攻击，即最近建立的连接会取代合法的充电站，并接收原本发给该充电站的后端命令。此漏洞可能允许未经授权的用户冒充其他用户进行身份验证，或者允许恶意攻击者通过向后端发送大量有效的会话请求来造成拒绝服务攻击。
* CVE-2026-22890 (CVSS 6.5): 充电站认证标识符可通过基于网络的地图平台公开访问。

由于这些站点连接了消费技术、汽车行业和市政电网，因此它们对网络犯罪分子来说极具吸引力。

EV2GO 充电网络运营商和基础设施维护者必须优先审查 CISA 的建议，以保护电网和依赖安全、稳定充电的日常驾驶员。

参考链接：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-04

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

sec随谈

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

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