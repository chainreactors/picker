---
title: Fortinet发布紧急补丁修复FortiClient零日漏洞
url: https://mp.weixin.qq.com/s/S7sD1d1VS_ZK-7AjxcZRFQ
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:57.417882
---

# Fortinet发布紧急补丁修复FortiClient零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7M0TUd2IhTDYuCA4uxJ0ic87xxWUyibJv7yo1NEtCPdh5FOy56MH2zH50NPLNYx0fuIbia6ich1OtLkfEGs0jHJQFcmnIp882QphD8/0?wx_fmt=jpeg)

# Fortinet发布紧急补丁修复FortiClient零日漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Fortinet针对另一个已被实际利用的零日漏洞部署了紧急补丁。

周六，Fortinet披露了CVE-2026-35616漏洞，称其为FortiClient端点管理服务器（EMS）软件中一个访问控制不当的漏洞。该严重漏洞的CVSS评分为9.1分，如果被利用，未经身份验证的攻击者可以通过精心构造的请求执行代码或命令。

网络安全厂商在其安全公告中确认该漏洞已被实际利用，并敦促客户为 FortiClient EMS 7.4.5 和 7.4.6 版本安装热修复程序。“即将发布的 FortiClient EMS 7.4.7 版本也将包含此问题的修复程序。在此期间，上述热修复程序足以完全防止该问题发生。”该公司在公告中表示。

Fortinet公司将漏洞的发现和报告归功于网络安全厂商Defused的创始人兼首席执行官Simo Kohonen和安全研究员Nguyen Duc Anh。Kohonen告诉Dark Reading，目前尚不清楚是谁在幕后操纵攻击，但此次攻击似乎范围有限，因为攻击活动似乎源于单个漏洞。

此次利用的零日漏洞紧随另一个 FortiClient EMS 漏洞之后，该漏洞编号为 CVE-2026-21643，于上月底遭到攻击。Defused发现有人利用这个严重的 SQL 注入漏洞进行攻击，该漏洞于 2 月 6 日首次披露并修复。Kohonen 表示，目前尚未发现这两个 CVE 漏洞存在重叠的威胁活动，并补充道：“到目前为止，除了最初的攻击者之外，我们还没有发现其他人利用这个零日漏洞（这是个好消息，因为我估计很多人由于周末/节假日还没有打补丁）。”

## CVE-2026-35616 利用活动

Defused在社交媒体平台 X 上发帖称，CVE-2026-35616 是一个“预认证 API 访问绕过”漏洞，允许攻击者完全绕过 API 授权。该公司表示，他们通过即将推出的 Radar 功能发现了该漏洞。

Kohonen解释说：“雷达本质上是一个大规模异常检测器，它试图从我们接收的大量蜜罐数据中发现零日漏洞和其他有趣的趋势。其目的是向Defused用户展示有趣的事件、有效载荷等等，因为即使我们拥有所有过滤选项，接收到的原始事件数量仍然非常庞大。”

Kohonen 表示，Radar 将于未来几天内公开发布，此前已标记出CVE 2026-3055 的利用活动，这是 Citrix NetScaler ADC 和 NetScaler Gateway 中的一个严重漏洞。

美国网络安全和基础设施安全局 (CISA) 于周一将 CVE-2026-35616 添加到其已知已利用漏洞(KEV) 目录中。联邦民事行政部门 (FCEB) 通常有两周时间来修复或缓解已利用的漏洞，但此次必须在 4 月 9 日之前解决 FortiClient 的零日漏洞。

Tenable公司高级工程师Scott Caveza周一在其博客文章中指出，GitHub上发现了一个公开的概念验证（PoC）漏洞利用程序，但Tenable的研究人员尚未对其进行验证。Caveza写道：“鉴于Fortinet设备过去曾被利用，并且之前也曾发布过多个漏洞的利用代码，我们预计随着更多漏洞利用程序的发布，此类漏洞的利用将会持续增加。”

## 攻击者正猛攻 Fortinet 产品

Fortinet 产品已成为各种威胁行为者的热门目标，他们经常迅速利用已披露的漏洞，使组织几乎没有时间进行修补。

今年1月，Fortinet证实，攻击者利用了一个严重的零日漏洞，通过FortiCloud的单点登录（SSO）功能登录到客户系统。同月早些时候，Fortinet FortiSIEM平台中的一个严重命令注入漏洞CVE-2025-64155也遭到广泛利用。

12月初，Fortinet披露了其FortiOS、FortiWeb、FortiProxy和FortiSwitchManager产品中的两个严重身份验证绕过漏洞，其中一个漏洞（CVE-2025-59718）在大约一周后被CISA的关键漏洞报告（KEV）目录收录。11月，攻击者利用了CVE-2025-64446，这是该公司FortiWeb产品线中的  一个关键路径遍历漏洞。

即使没有新的CVE漏洞可供利用，攻击者仍然会以Fortinet产品为目标。今年2月，亚马逊网络服务(AWS)的研究人员发现，攻击者利用人工智能技术入侵了数百台FortiGate设备，利用了薄弱的凭证、暴露的端口和其他安全漏洞。

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