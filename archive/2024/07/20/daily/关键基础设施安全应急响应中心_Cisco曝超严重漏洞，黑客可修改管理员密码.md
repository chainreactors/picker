---
title: Cisco曝超严重漏洞，黑客可修改管理员密码
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544985&idx=3&sn=04a154860e6a3a0044645583796a7c5c&chksm=c1e9bcc8f69e35de3d606ff5179d3d5265397f54bbc9231163b8c9fdd9c4d406ffe10e575673&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-20
fetch_date: 2025-10-06T17:43:30.750850
---

# Cisco曝超严重漏洞，黑客可修改管理员密码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvXw8TyEFDCxtvnNy2CJganNiaAcnSKV3M04pRyu88JVGH1WRhAd0x1GibnqPTLunjNrRVCYpJWhibicg/0?wx_fmt=jpeg)

# Cisco曝超严重漏洞，黑客可修改管理员密码

关键基础设施安全应急响应中心

近日，思科公司披露了其智能软件管理器本地版（SSM On-Prem）中的一个关键漏洞，该漏洞允许未经身份验证的远程攻击者更改任何用户的密码，包括管理员用户的密码。这个漏洞被追踪为 CVE-2024-20419，其严重程度评分为 10 分。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39t95zyTibcFLI0Whh1yue2Lo2c5ttzOusltwr3iaXRGQiakcVEk89PDM3IU0Ml4xGIicufVHvVYDhx1g/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

据悉，该漏洞是由于思科 SSM On-Prem 认证系统中密码更改过程执行不当造成的。

攻击者可以通过向受影响的设备发送特制的 HTTP 请求来利用这个漏洞。成功利用将允许攻击者以受影响用户的权限访问 Web UI 或 API，从而在未经授权的情况下对设备进行管理控制。

**受影响的产品**

* 思科 SSM On-Prem
* 思科智能软件管理器卫星版（SSM Satellite）

思科 SSM 卫星版已更名为思科智能软件管理器。对于 7.0 版本之前发布的版本，该产品称为思科 SSM 卫星版。从 7.0 版本开始，它被称为思科 SSM On-Prem。

**已修复的软件**

思科已发布软件更新来解决此漏洞。修复的版本如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39t95zyTibcFLI0Whh1yue2LrR4XPCQwA1icMITdhuqn2m6SWtiavPoItsM22uBFVJKfAuv8xiaBNbgIw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

思科建议所有客户升级到修复版本以降低风险，保护其系统安全。

截至目前，尚未有公开的公告或证据表明此漏洞被恶意利用，思科的产品安全事件响应团队（PSIRT）将继续监控这一情况。

另外，拥有服务合同的客户应通过其常规更新渠道获得安全修复程序，没有服务合同的客户可以联系思科技术援助中心（TAC）以获得必要的更新。

**如何检查思科智能软件管理器本地版的版本**

访问管理门户

打开一个 Web 浏览器，输入思科 SSM On-Prem 服务器的 IP 地址和端口号。例如，如果 IP 地址是 172.16.0.1，则输入：https://172.16.0.1:8443/admin

登录

使用管理员凭据登录管理门户。

查找系统运行状况部分

登录后，导航到管理门户的「系统运行状况」部分。此部分通常显示的是思科 SSM On-Prem 安装的当前软件发布版本。

**参考资料：**

https://cybersecuritynews.com/cisco-ssm-password-change-vulnerability/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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