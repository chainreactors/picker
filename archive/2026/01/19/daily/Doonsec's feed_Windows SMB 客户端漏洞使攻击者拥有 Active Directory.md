---
title: Windows SMB 客户端漏洞使攻击者拥有 Active Directory
url: https://mp.weixin.qq.com/s/czIlh7tQrNqXTdayQqbe1A
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:33:04.073774
---

# Windows SMB 客户端漏洞使攻击者拥有 Active Directory

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGSicTaNUE3WtkGFZh6uFws1o9fQI0r97LADOXibNsWRA770mnOA3keCUicw/0?wx_fmt=jpeg)

# Windows SMB 客户端漏洞使攻击者拥有 Active Directory

原创

O安全研究员
O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGSyEn9cVibs1DLllGibcjT6gZ7aLHPnfFOibCRPxk8Y4R9nZVwCXcic2lpSA/640?wx_fmt=png&from=appmsg)

这是Windows SMB客户端认证中的一个关键漏洞，使攻击者能够通过NTLM反射攻击攻破Active Directory环境。

该漏洞被归类为不当访问控制漏洞，允许授权攻击者通过精心编排的认证中继攻击，在网络连接上升级权限。

在2025年6月安全补丁发布七个月后，研究显示企业基础设施中普遍存在未被采纳的情况。

几乎在域控制器、零级服务器和工作站的渗透测试中，都能识别出易受攻击的主机。该漏洞利用了Windows NTLM本地认证中的一个基本机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGS8VEGkRVE8zXwOJPibBZLpHks9pVMuVxja5uesZSySMPEHHmxic92LMuA/640?wx_fmt=png&from=appmsg)

当客户端收到标记为本地认证的NTLM\_CHALLENGE消息时，系统会创建一个上下文对象，并在保留字段中插入上下文ID。

该机制结合 PetitPotam、DFSCoerce 和 Printerbug 等强制技术，迫使lsass.exe（以 SYSTEM 形式运行）向攻击者控制的服务器进行认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGSVX5o1SojlZFgEEiafw1vCicOY8fgd7H2iaaB7n0FicGf10zKTtkRHpsVMg/640?wx_fmt=png&from=appmsg)

随后服务器冒充SYSTEM令牌进行后续作，实际上实现了系统全面入侵。

**攻击需求****与利用路径**

利用需要在AD DNS中注册恶意DNS记录（默认允许认证用户），或在本地网络内进行DNS毒害。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGS2FkDLortCLltARZmS5GtGPcK7uUpVIWycb4YsZHtm9yZJ4wWf5Iiclw/640?wx_fmt=png&from=appmsg)

这些低权限要求从根本上增加了攻击面，因为大多数组织并未限制认证用户在 AD DNS 区域创建任意 DNS 记录。

传统的缓解措施对高级利用途径效果不足。

虽然SMB签名通常能防止中继攻击，但研究表明SMB到LDAPS之间成功实现跨协议中继，同时强制签名和信道绑定。

该绕过涉及剥离特定的NTLMSP标志（协商始终标志、协商印章、协商标志），同时保留消息完整性代码。该技术使攻击者能够同时绕过多个安全控制。

**超越中小企业签名的攻击面**

这种脆弱性不仅限于传统的中小企业间中继。DepthSecurity的研究人员证实，通过跨协议中继技术，成功攻击了ADCS注册服务、MSSQL数据库和WinRMS。

更令人担忧的是，SMB到LDAPS的反射攻击允许攻击者直接控带有系统权限的Active Directory对象。

通过DCSync作实现组成员修改和凭据采集。

基于RPC的中继尝试揭示了与SMB签名类似的会话密钥加密要求，表明Windows的基本认证机制加剧了漏洞的影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGSQDJAEeFrGHMhQfjyIHwUkpVkd7coTehQ8lxXLWeuoIDY2UmDOtNjrA/640?wx_fmt=png&from=appmsg)

攻击者成功认证了RPC服务，但在后续作中遇到访问控制，暗示了通过Net-NTLMv1认证可能被利用的途径。

根据DepthSecurity，组织必须立即应用2025年6月的Windows安全更新作为主要缓解措施。此外，应在所有协议中启用签名和信道绑定强制执行，而非仅限于SMB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxS3s81SxzzTuURnCLQibiaGSCHlWkYunyIgHS1xaoctgy82o05tNaibaIXJoT75wNEl7eFviajPBibibKA/640?wx_fmt=png&from=appmsg)

重新配置Active Directory DNS区域访问控制列表以限制认证用户创建DNS记录，显著降低了利用的可行性。

安全团队必须优先快速修补NTLM强制攻击技术，并对其基础设施内的NTLM中继攻击手段进行全面审计。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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