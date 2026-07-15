---
title: 攻击者全网扫描MCP服务器与Claude凭据，AI系统面临数据泄露风险
url: https://mp.weixin.qq.com/s/ai-cKrpYywXSrME1uv1CXQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:20.019500
---

# 攻击者全网扫描MCP服务器与Claude凭据，AI系统面临数据泄露风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX37w6o1G1eFkcpiaiaWCHP5Jjux9t29YzIiaSsRUxM9Q6gx0lrOhjjLqu4F8x51FXtzZpEBE8cTydr5u9VqoQgXGX6N1zicnltcAb8/0?wx_fmt=jpeg)

# 攻击者全网扫描MCP服务器与Claude凭据，AI系统面临数据泄露风险

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX1H3PibnMUry8hYJSWCWSW8j5FkFxLdap0wyBnYKv0E2w6bz97H032qqdmIQQ1AGkLUS3XGZdtJ9EKySGxVASrmSUAMAoVXxice8/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1kDkCrPjn2gcmyUjuNsCYCP7A5ibmUTdWZds10Ib5du3HY8aDa1rbiaZuLI4CxP7Ev3XibUzybMywrqZvWnVn5Hfpxnx8mbkHnSI/640?wx_fmt=jpeg)

面向互联网的AI系统正成为机会主义攻击者的新目标。安全专家发现，威胁行为者正在积极搜索Model Context Protocol（MCP，模型上下文协议）服务器、AI助手配置文件以及暴露在外的本地语言模型服务。

这一活动发生在流量较低的网站上，这些网站似乎并未托管AI基础设施。这一点之所以重要，是因为它表明这是一次广泛的侦察行动，而不是针对特定组织或开发者的定向入侵。

互联网风暴中心（Internet Storm Center）的分析师在审查一个小型网络托管商两周的Apache和ModSecurity日志时发现了这一活动。研究人员共发现约200次与AI Agent侦察相关的请求，其中MCP握手探测请求来自49个不同的源IP地址。

互联网风暴中心在与Cyber Security News（CSN）分享的报告中指出，这些扫描反映出AI部署领域日益严重的安全问题。开发者可能在不经意间暴露MCP服务、将助手设置留在公共Web目录中，或让本地模型可从互联网访问，而攻击者已经在寻找这些配置失误。

Part01

攻击者进行全文扫描

此次活动最值得注意的部分是使用了有效的MCP初始化请求，而非简单的路径检查。扫描器并不是简单地询问某个Web地址是否存在然后继续下一步，而是发送了格式正确的JSON-RPC消息，旨在启动MCP对话。

这种攻击方式使攻击者能够判断某个可达服务是否表现得像MCP服务器。如果服务器响应，下一阶段可能涉及识别可用的工具、连接的数据源以及AI Agent有权执行的操作。

MCP服务器可以让AI Agent访问数据库、内部API、文件系统、工单系统以及其他业务资源。当MCP服务器暴露在外且未使用身份验证时，实质上为外部人员提供了一份机器可读的服务和数据地图，显示了Agent能够访问的资源。

这些探测的广泛分布也表明这是一场更大规模的行动。

![侦察类别（来源：互联网风暴中心）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0ibm5fVhOnxLVRnWDjEUI2DDnkuNhPG4lhKjUOMn9Bs7Uq72wR4Qq5bJ0tYW8ZQaoMgbrBiavWyyickufJNIBqdiaNCJx0icib3b934/640?wx_fmt=jpeg)

请求来自许多不同的IP地址，这使得活动看起来不像学术测试，而更像分布式全网扫描，旨在大规模发现存在漏洞的部署。

组织应审查访问日志中可疑的MCP流量。不使用MCP的系统应将此类请求视为有用的侦察信号，并在适当位置予以阻止。

确实运行MCP服务器的组织应确认其要求强身份验证，并且除非严格必要，否则不得直接从公共互联网访问。限制网络访问还能降低扫描器首先发现服务的可能性。

Part02

凭据与模型面临风险

同一扫描活动还搜索与AI编码助手相关的文件，包括开发者可能无意中放在已部署Web目录中的设置文件和凭据文件。这些文件可能包含连接细节、服务设置以及可能具有价值的密钥。

![模型上下文协议（来源：互联网风暴中心）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0nD8GGNmOE7kesnnGW9qNsR8x4ib5A23cJITGVsjwEO911XGzQ2Ro8825EZtPD55YKga0C9jickicQtF4HiaRDLz4JyqfHW0e8odI/640?wx_fmt=jpeg)

使用轻量级存在性检查来探测凭据相关文件，表明操作者正在针对大量目标优化扫描。他们并非下载每个可能的文件，而是首先检查潜在有用资源是否存在。

研究人员还观察到重复尝试定位未经过身份验证的模型服务接口。一个公开可访问的模型端点可能让攻击者免费使用计算资源、了解已安装的模型，或成为在环境中进行进一步活动的立足点。

这些扫描还伴随有尝试滥用服务器端请求伪造（SSRF）来攻击云元数据服务的行为。这种技术对AI工具尤其相关，因为Agent和辅助服务通常包含从用户提供的Web地址获取内容的功能。

防御者应从外部网络检查面向公众的系统，确保AI相关配置文件不被Web服务器提供，并审查URL获取功能，确保其具备针对内部和云元数据目的地的保护措施。云环境还应尽可能启用元数据服务保护，包括GCP头部强制和AWS IMDSv2。

入侵指标（IoCs）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX021fE4WDM4MCXNeXuOqNBGJl8KyL8dw7gx2H9QC64xcPbFBpkFY8jmLJt7WXTaHSB0fuVKw9oITdqHjStdJyZBryIibzzbkicLw/640?wx_fmt=png&from=appmsg)

注意：IP地址和域名已进行去毒化处理（例如\_[.]\_），以防止意外解析或超链接。仅在受控的威胁情报平台（如MISP、VirusTotal或SIEM）中进行还原。

参考来源：

Internet-Wide Scans Target MCP Servers, Claude Credentials, and Exposed AI Models

https://cybersecuritynews.com/internet-wide-scans-target-mcp-servers-claude-credentials/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0d7KoyEHYsPfbgBgXYQmHS9EgIpOAxfibDrVp8uYPQd3yzGxCrUKcoiajc9NX5KNwMKmib2nnrSsnDa8POob7G5mibuxwMMez0bfI/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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