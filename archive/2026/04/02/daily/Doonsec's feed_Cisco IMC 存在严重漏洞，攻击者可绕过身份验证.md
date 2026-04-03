---
title: Cisco IMC 存在严重漏洞，攻击者可绕过身份验证
url: https://mp.weixin.qq.com/s/jjN4GtZjaxNhqnIf9f6WTg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:17.284716
---

# Cisco IMC 存在严重漏洞，攻击者可绕过身份验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PMBdcmMq3n4l9I9iaAUyxCkUkyEdP9jepF6IdnX7SqIOYuZIKX3kMCQAH40m32NlaZqd29vUnCTqmzwXibMOTRUqsTjnpicm15iaA/0?wx_fmt=jpeg)

# Cisco IMC 存在严重漏洞，攻击者可绕过身份验证

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

思科最近披露了一个影响其集成管理控制器 (IMC)的严重安全漏洞，促使其发布了紧急软件更新。

该漏洞的官方编号为 CVE-2026-20093，其 CVSS 基本评分为 9.8，属于严重级别。

此安全漏洞存在于思科IMC软件的密码更改功能中。核心问题在于系统对传入的密码更改请求处理不当。

利用此漏洞，远程未经身份验证的攻击者可以直接向受影响的设备发送 恶意构造的 HTTP请求。

如果攻击成功，攻击者可以完全绕过标准身份验证检查。一旦身份验证被绕过，攻击者就可以修改系统中任何现有用户的密码。

这包括主管理员帐户，该帐户实际上允许攻击者劫持系统并以该用户的身份获得完全的管理权限。

## **受影响的系统和硬件**

如果思科硬件产品运行的思科 IMC 软件存在漏洞，则该漏洞会影响多个思科硬件产品。

受影响的独立产品包括：

* 5000系列企业网络计算系统（ENCS）
* Catalyst 8300 系列边缘 uCPE
* UCS C系列M5和M6机架式服务器（独立模式）
* UCS E系列服务器M3和M6

此外，许多依赖于预配置的受影响UCS C系列服务器的思科设备也面临风险。如果这些设备暴露了思科IMC用户界面，它们就会受到攻击。

该广泛列表包括应用程序策略基础架构控制器 (APIC) 服务器、Catalyst Center 设备、安全防火墙管理中心设备和安全网络分析设备。

思科已确认，某些较新且配置不同的产品，例如 UCS B 系列刀片服务器、UCS X 系列模块化系统以及 UCS C 系列 M7 和 M8 机架服务器，不受此缺陷的影响。

目前，尚无任何临时性变通方案或缓解措施可以阻止此漏洞。唯一有效的解决方案是应用思科提供的官方软件更新。

强烈建议管理员立即将受影响的系统升级到已修复的软件版本。

更新过程因设备而异；例如，升级 5000 系列 ENCS 和 Catalyst 8300 系列上的 IMC 需要升级底层 Cisco 企业 NFV 基础设施软件 (NFVIS)。

对于独立服务器，管理员通常可以使用 Cisco主机升级实用程序(HUU) 来安装修复后的 IMC 版本。

思科公司对报告此漏洞的安全研究人员表示感谢，并指出目前没有证据表明有人正在积极利用此漏洞，也没有公开声明有人恶意使用此漏洞。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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