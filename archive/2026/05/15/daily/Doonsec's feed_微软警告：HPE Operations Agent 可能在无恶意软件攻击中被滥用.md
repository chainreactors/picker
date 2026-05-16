---
title: 微软警告：HPE Operations Agent 可能在无恶意软件攻击中被滥用
url: https://mp.weixin.qq.com/s/n9TqWGWGQCfe0MNsIc7u2w
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:53.265982
---

# 微软警告：HPE Operations Agent 可能在无恶意软件攻击中被滥用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OWGyU1icadW7cmIZf10kjFmzOvoMhkicUVRlciafKNsOOqz5pbFqLTS8qsY3PjSurYxah1IhR2cXUiblYX7spkDStz9ShWicj6x7wk/0?wx_fmt=jpeg)

# 微软警告：HPE Operations Agent 可能在无恶意软件攻击中被滥用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软披露了一起隐蔽的入侵活动，攻击者绕过了传统的恶意软件和漏洞利用，而是滥用受信任的企业工具悄无声息地渗透网络。

该技术凸显了网络攻击中日益增长的趋势，即攻击者依靠合法软件和现有的信任关系来逃避检测。

值得注意的是，HPE OA 系统中并未出现任何漏洞。相反，攻击者是通过一家负责管理该组织基础设施的第三方 IT 服务提供商的入侵而获得访问权限的。

这种方法使得攻击者能够完全在正常的管理工作流程中开展活动。通过 HPE OA 执行脚本，他们的活动与常规系统操作难以区分，从而显著延迟了检测和响应。

该攻击符合 MITRE ATT&CK 技术 T1199（可信关系），攻击者利用现有的业务和运营信任路径。

在这种情况下，这种信任不仅延伸到组织内部，还延伸到外部服务提供商，从而有效地扩大了攻击面。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NLGldlpBtKN9Kvy4lHzAmfWWIeW7gY80rpkydicxVNZxmoOh8qvoiac4YKic37eIa0oIxfBIhtqZth0xz0iakZyt2IgZhu1c5oFGc/640?wx_fmt=png&from=appmsg)

微软在一份与 GBhackers 分享的报告中表示，攻击者利用了 HPE Operations Agent (OA)（一款广泛使用且值得信赖的 IT 管理工具）在目标环境中执行恶意操作。

在域控制器上，攻击者安装了一个名为“mslogon”的恶意网络提供程序，从而能够在登录和密码更改期间拦截用户凭据。

微软的分析显示，此次入侵持续了数月之久。攻击者在获得初始访问权限后，通过 HPE Operations Manager (HPOM)部署了 VBScript 有效载荷，进行网络发现并识别 Active Directory 结构。随后，攻击活动升级为凭据窃取。

## **微软警告HPE运营部门**

相关的 DLL 以明文形式捕获用户名和密码并将其存储在本地，使攻击者能够重复使用凭据进行横向移动。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NT2EgV0xpE3nwtMrdlbszLebTRmibZqD0zwaib3xO1k97niaALEjOf2ULVOI6YVgjuKbNoK3jDzTEllJcpIhKPc4kibxiaoT9Ywk7o/640?wx_fmt=png&from=appmsg)

为了加深持久性，攻击者后来部署了第二种机制：一个名为“passms.dll”的恶意密码过滤器 DLL。

该组件集成到 Windows 本地安全机构 (LSA) 中，可在密码更新时捕获凭据。

被盗数据经过编码后通过 SMB 共享或伪装成图像文件泄露，进一步将恶意活动与合法流量混为一谈。

捕获的数据并非以明文形式存储，而是经过双重编码：首先使用 Base64 编码，然后使用嵌入在 DLL 中的自定义编码例程进行编码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PxEr3icTycGqrqh92Rh6xVoCGZSJCkKjsPBnRqYOjtlsohoTsiaYvIJhKW1ibv0fSHklCYEibiaAic05dgU99m4iayZqOq34lA53RcU0/640?wx_fmt=png&from=appmsg)

与此同时，在面向互联网的服务器上建立了Web Shell，其中包括修改后的应用程序文件，例如“Signoff.aspx”。这些Web Shell能够执行远程命令和上传文件，并通过模仿正常的应用程序行为来避免被检测到。

攻击者还部署了 ngrok 隧道工具来维持隐蔽的远程访问。通过创建加密隧道，他们无需暴露开放端口即可启用远程桌面协议 (RDP) 连接，从而有效地绕过了边界防御。

这使得可以在关键系统（包括 SQL 服务器和域控制器）之间进行横向移动。

Windows 管理规范 (WMI) 远程执行进一步支持了横向移动，该功能用于在其他设备上部署和启动 ngrok。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MU2LiapchRvX4YSoZsRJwqHqsto9kEX9nTrkHMCicMPlm61UqvFdEb9iaIPcibhqBsz3wsdeqs1IW4nsQZvVU9BEpWek9jNFSFpXk/640?wx_fmt=png&from=appmsg)

尽管攻击经历了多个阶段，但由于其依赖于可信工具、有效凭证和合法系统进程，因此基本未被察觉。即使在最初被发现后，攻击者也利用先前被攻破的接入点重新建立了持久化防御。

微软强调，此次行动体现了现代网络行动中“隐蔽行动胜于喧嚣行动”的更广泛趋势。

攻击者不再部署会触发警报的恶意软件，而是越来越多地“利用系统资源”，滥用内置工具和信任关系来维持长期访问权限。

为了抵御此类威胁，微软建议在所有系统中部署端点检测和响应 (EDR)，强制执行严格的出站流量控制，并在服务器上启用详细的日志记录。

组织也被敦促采取零信任思维，尤其是在与第三方提供商合作时，并不断验证其环境中受信任工具的行为。

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