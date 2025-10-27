---
title: BlackByte勒索软件：利用VMware漏洞，通过VPN访问发动攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546686&idx=3&sn=db8acc8f9a59c0d4fd98dd11633b5f2f&chksm=fa9381ffcde408e93963dc6a04d139c6d84d7e5dda3d386bacf14604ec386142fa9b58451beb&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-31
fetch_date: 2025-10-06T18:05:24.579964
---

# BlackByte勒索软件：利用VMware漏洞，通过VPN访问发动攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176la9qfxh1pQYNUBn2S4e0Intn0DWQFddib4iaKWib4qIu7rDhfWmRv3CYL9nJRHI26KibXGgLapu5OvFg/0?wx_fmt=jpeg)

# BlackByte勒索软件：利用VMware漏洞，通过VPN访问发动攻击

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtibGOGiaItSByup4R76icOTCUicx8QOibPBq5oFYz3rSMIKEnoC20Q4icaskrSW9dPtBJtyic3A4P5SYhKw/640?wx_fmt=jpeg&from=appmsg)

Hackread报道，近期Cisco Talos（思科威胁情报团队）发现，BlackByte勒索软件正在对全球企业发起新一轮攻击。

BlackByte组织利用VMware ESXi虚拟机监控程序中最近被修补的漏洞，通过VPN访问发动攻击。

思科建议各组织实施多因素认证（MFA）并加强安全措施以降低风险。

被利用的漏洞为CVE-2024-37085，它允许攻击者绕过身份验证并控制易受攻击的系统。

除了这个漏洞之外，还观察到BlackByte组织使用受害者授权的远程访问机制，例如VPN。这种策略使得BlackByte在可见性较低的情况下运营，并逃避安全监控系统。

另一个令人担忧的事态发展是该组织使用被盗的Active Directory凭据来传播其勒索软件。这意味着他们可以更快、更有效地在网络内传播感染，从而增加潜在的损害。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6ymOMJRVJWDsjxerbmuCVRjf4aES348vC9o6hc2PiaNWd5ezYE9R7RX5SViaGVSsdubUfiaojYLZ0rnw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

思科团队研在8月28日星期三研究结果发布前，与Hackread分享了他们的发现。

研究人员认为，BlackByte实际活动比公共数据泄露网站上显示的更活跃。网站只显示了他们成功发起攻击的一小部分，可能掩盖了他们行动的真实范围。

BlackByte针对的5个最主要目标行业：制造业；运输/仓储；专业人士、科学和技术服务；信息技术；公共行政。

研究人员建议各个组织优先考虑修补系统，包括VMware ESXi虚拟机管理程序，为所有远程访问和云连接实施多因素身份验证（MFA），应审核VPN配置，并限制对关键网段的访问。

限制或禁用NTLM的使用，并选择更安全的身份验证方法也非常重要。部署可靠的端点检测和响应（EDR）解决方案可以大大提高安全性。

此外，全面的安全策略应包括主动威胁情报和事件响应能力，以有效保护系统免受BlackByte和类似攻击等威胁。

原文来源：E安全

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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