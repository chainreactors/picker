---
title: 微软AI医疗机器人发现严重漏洞，可能泄露隐私
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546480&idx=2&sn=429d11d6b0114a07acaa351b2f01e153&chksm=fa9380b1cde409a7c4fe600f34d4baaf8ae0da3da85d7f1470ce43194ca2549eac0db818971e&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-17
fetch_date: 2025-10-06T18:06:27.038125
---

# 微软AI医疗机器人发现严重漏洞，可能泄露隐私

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mtuibGC6AGcr19Ew2NzEUWB4BuWABWp91onRC1nDF8O7Pdtzf9Yic9oQrSib1uibTeiax198KD0DhL0hQ/0?wx_fmt=jpeg)

# 微软AI医疗机器人发现严重漏洞，可能泄露隐私

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mtuibGC6AGcr19Ew2NzEUWBxmfNgIxsRhjJCTwZaiaB0d4pcjPEwB8YibLXBcdcyITfmicXFcCPqnqkg/640?wx_fmt=png&from=appmsg)

微软的AI医疗聊天机器人服务中存在严重的安全漏洞。漏洞允许未经授权的访问者获取用户和客户的个人信息。

漏洞中其中一个被评定为“严重”等级，攻击者可能利用漏洞在Azure Health Bot服务的网络环境中进行横向移动。

目前，微软已对发现的漏洞采取了缓解措施，无需客户再做行动。

**1、AI聊天机器人被利用**

Azure Health Bot Service是一个云平台，医疗保健组织能够构建和部署AI驱动的虚拟助手，以降低成本并提高效率。

在检查该服务的安全问题时，Tenable研究人员研究了“数据连接”这一功能上，机器人能够从外部数据源获取信息，这可能包括患者医疗信息等敏感数据。

这个数据连接功能是为了使得服务的后端系统能够向第三方应用程序API接口发送请求。

在测试这些连接以查看它们是否可以与服务内部的端点交互时，研究人员发现，发出重定向响应使他们能够绕过这些端点上的一些安全措施，例如过滤机制。

在此过程中发现了两个权限提升漏洞。

**2、漏洞一：严重权限提升漏洞**

Tenable研究人员详述的第一个漏洞是通过服务器端请求伪造的方式被利用，通用漏洞披露CVE编号为CVE-2024-38109。

随后，研究人员配置了这个外部主机，使其对请求以301重定向响应，目标是IMDS（内部元数据服务）。

在接收到有效的元数据响应后，研究人员能够获得一个访问令牌，这个令牌为他们提供了一个微软内部的订阅ID。最后发现访问的资源中包含了数百个属于其他客户的资源。

这些发现在2024年6月17日报告给了微软，并且在一周内，修复措施被引入到受影响的环境中。到7月2日，修复措施已经在全球范围内推出。

修复这个漏洞的方法是完全拒绝数据连接端点的重定向状态码，这消除了这个攻击向量。

微软将这个漏洞评为严重等级，确认它将提供跨租户访问。它已被包含在微软2024年8月的Patch Tuesday出版物中。

没有证据表明这个问题被恶意行为者利用过。

**3、漏洞二：重要权限提升漏洞**

在Microsoft修复第一个漏洞后，Tenable研究人员在Azure Health Bot Service的数据连接功能中发现了另一个权限升级漏洞。

研究人员使用类似的服务器端请求伪造技术来利用FHIR端点向量中包含的漏洞，该向量规定了访问电子病历资源和对资源执行操作的格式。

这个漏洞比IMDS漏洞的严重程度要低，因为它不提供跨租户访问权限。

研究人员在7月9日向微软报告了这个漏洞，微软在7月12日提供了修复措施。这个漏洞被评定为重要级别。

目前没有证据表明这个问题被恶意行为者所利用。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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