---
title: 从NTAuthCertificates证书伪造到证书服务 DCOM 强制身份验证
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247506013&idx=1&sn=5c3bf641a9e7d123b2c034c3da94ed02&chksm=fa520de3cd2584f540193597c5c750be8a5aeffc9d1187e5a54017a8ec453839966fde237675&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-05-11
fetch_date: 2025-10-06T17:17:55.350302
---

# 从NTAuthCertificates证书伪造到证书服务 DCOM 强制身份验证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIzZnlhCYNH1jVAQ8AzL6Kh90sqd6M7COKVVV1PqaJPEAS8Xz2O8HARQ/0?wx_fmt=jpeg)

# 从NTAuthCertificates证书伪造到证书服务 DCOM 强制身份验证

原创

th1e

山石网科安全技术研究院

# 书接上回，之前我们在探索与 Windows Active Directory 认证服务 (ADCS) 相关的所有组件和配置时，对Cert Publishers组进行了研究，这次我决定看一下“**证书服务 DCOM 访问**”组。

当服务器安装Active Directory Certification Services (ADCS)角色并承担证书颁发机构（CA）服务器的角色时，它会被特殊的NT AUTHORITY\Authenticated Users身份组填充，代表了每个可以成功登录到域的域用户账户。

“DCOM Access”组引起了我的注意，因为它可能涉及到潜在的漏洞和利用方法。

简单来说，这个组可以通过DCOM注册证书。因此，所有经过身份验证的用户和计算机都可以访问特定的应用程序。

每当用户或计算机注册或自动注册证书时，它会联系CertSrv Request应用程序的DCOM接口，这些接口通过MS-WCCE协议（Windows Client Certificate Enrollment Protocol）公开。

还有一套特定的接口用于Certificate Services Remote Administration Protocol，如MS-CSRA中所述。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB0e3sBArhGibjJ5Ll17eibDjldFwKleurb7XePaKicKtregQd5Kj6UHwEQ/640?wx_fmt=png&from=appmsg)

这里我们着重来看DCOM服务器的激活权限

DCOMCNFG工具为我们提供了很多有用的信息。在计算机级别，“Certificate Service DCOM Access”组被“限制”为本地和远程启动权限：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBf9HTvQ0lImqAwkUAEnOkXwczCWjbMYFE8DicS1C5UcrN9ARyaTaXgDw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBoIVv9BsrmOOD4YoODhnLb352OP8yMYFpQINFeGjjdPuCADdqvzhYLw/640?wx_fmt=png&from=appmsg)

这并不意味着这个组可以激活所有的DCOM对象，我们需要查看特定应用程序，例如CertSrv Request：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBeSAeIlYuibwkZ4Og67KTNJib9LYWzZ0qYNArxmzX5icH4maZhO1n4YzSA/640?wx_fmt=png&from=appmsg)

每个人都可以从远程激活这个DCOM服务器。坦率地说，鉴于这个组仅限于本地启动和本地激活权限，我本以为会在这里找到“Certificate Service DCOM Access”组，而不是Everyone：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB5X0WxjUFp30CtIvgHULw5wRS97zPMQKsVp4O7otJcfpHulAdWNzg1Q/640?wx_fmt=png&from=appmsg)

所以这里也许还会评估某种组合权限和嵌套成员身份。

另一个有趣的方面是：从我观察到的情况来看，“Certificate Service DCOM Access”组是少数几个被授予远程激活权限的组之一，与Distributed COM Users和Performance Log Users组一样。

我们也来看看身份：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBicqazYN6yWNGgvqiaLzkqEYCrwqyB4DVLXicicwNlfjTa1uVoQKJOhKLbw/640?wx_fmt=png&from=appmsg)

这个DCOM应用程序以SYSTEM账户的身份运行，它代表了最高本地特权身份。

因此，我们有一个特权的DCOM服务器，可以被任何经过身份验证的域用户远程激活。这让我想到了potato漏洞攻击。

总之，大多数这些漏洞依赖于在高特权上下文中运行的DCOM激活服务，通过取消序列化IStorage对象，并将NTLM身份验证反射回本地RPC TCP端点，以实现本地权限提升。

还有这种攻击的变体，涉及使用LDAP、HTTP或SMB等协议将用户或计算机的NTLM（和Kerberos）身份验证中继到远程端点，最终实现高达域管理员的权限提升。

但这个场景有所不同，因为作为一个低权限的域用户，我们希望激活一个在高特权上下文中运行的远程DCOM应用程序，并强制它对我们机器上运行的远程侦听器进行身份验证，以便我们可以捕获并中继此身份验证到另一个服务。

我们希望获得远程计算机本身的认证，当DCOM应用程序在SYSTEM或Network Service上下文中运行时。

那么，我们应该采取哪些具体步骤来实现这一点？

从最初的JuicyPotato开始，我做了一些小改动：

* 在端口135上设置一个Linux机器上的重定向器（socat），将所有流量重定向到我们的攻击机器上的专用端口（例如9999）。您当然知道，我们不能再为Oxid Resolution指定自定义端口了。
* 在JuicyPotato代码中：

+ 初始化一个COSERVERINFO结构，并指定我们想要激活DCOM对象（ADCS服务器）的远程服务器的IP地址
+ 初始化一个COAUTHIDENTITY并填充用户名、密码和域属性。
+ 将COAUTHIDENTITY分配给COSERVERINFO结构
+ 在IStorageTrigger::Marshallinterface中指定重定向器IP地址
+ 在CoGetInstanceFromIStorage()中传递COSERVERINFO结构：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBcG0LXicmjxk2fA5eprT8ZLXJuy4RXY5dbjpaFrMCbBEa0GI7IhpjmEA/640?wx_fmt=png&from=appmsg)

在我们套接字服务器上收到的NTLM消息转储中，我们可以看到我们从远程CA服务器（SRV1-MYLAB）收到了一个身份验证类型的消息：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBQKZHHiazrJZHlDdXZribnczXopPYkTCThWl3Dl7ic6wf3o2v9mHa8USSw/640?wx_fmt=png&from=appmsg)

网络捕获显示，我们的低权限用户请求的远程激活成功了：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBrcRAmB4glmTwEDM6Sr2mXx1omcbjOIOWPLQXicQqT8nb4tyBvWFtZqQ/640?wx_fmt=png&from=appmsg)

最后一步是将NTLM身份验证转发到外部中继，如ntlmrelayx，使其能够以CA计算机本身的身份对另一个服务进行身份验证。

最后，由于我们有一个RPC客户端进行身份验证，我们必须使用ntlmrelayx中已经实现和支持的协议来封装和转发身份验证消息，如HTTP。

那么现在，又出现了一个新的问题

普通域用户可以强制ADCS服务器的认证从远程，拦截身份验证消息，并中继，但这真的有用吗？

考虑到存在其他未修补的方法来强制域控制器的身份验证，例如DFSCoerce，它的实用性确实非常堪忧。

还有一个问题是，由于微软最近在DCOM中加强的安全措施，目前可以中继的协议只有HTTP和SMB。

在我的实验室中，我针对运行在不同机器上的CA web注册服务器的HTTP /CertSrv端点进行了中继测试。在没有NTLM缓解措施的情况下，我为CA服务器请求了一个机器证书。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBiccrSWITukllLAGuwGics9ZzoAA4RUhNDqQWBssxs4HEicPIaSHqVqFPQ/640?wx_fmt=png&from=appmsg)

攻击流程如下图所示：![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB9cia9gTJFcvSeWbNyCqJy7LbXE4hOwQaRlakHX7iaGsddIsibBswsC2iag/640?wx_fmt=png&from=appmsg)        通过利用DCOM和身份验证中继技术来获取ADCS服务器的机器证书，这可能导致攻击者获得对证书颁发机构的控制权，并伪造证书。

## 结论

虽然我描述的强制认证的方法可能不是开创性的，但它提供了利用普通域用户被授予的远程激活权限来强制远程服务器认证的替代方法。

这种能力仅限于“Certificate Service DCOM Access”组，该组仅在运行ADCS服务时填充。然而，可能有遗留的DCOM应用程序授予每个人远程激活权限。

想象一下，DCOM应用程序以“交互用户”的上下文运行，远程激活对普通用户可用。通过跨会话实现，还可以检索已登录用户的身份验证。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB3LyXbVBFXefLibpvQ03NUlgMLyhJTo6bDIDjPe1hiaib3EvaSct4Ew3hA/640?wx_fmt=png&from=appmsg)

避免在域控制器上安装不必要的服务！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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