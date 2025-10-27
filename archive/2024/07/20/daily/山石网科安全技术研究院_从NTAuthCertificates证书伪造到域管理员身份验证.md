---
title: 从NTAuthCertificates证书伪造到域管理员身份验证
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507134&idx=1&sn=8e215bde89ea3906ec21b7997e7ec365&chksm=fa520900cd258016e3af15cb4553291ddb89a3abb184246c41100893eab9cca0a69589f32da5&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-07-20
fetch_date: 2025-10-06T17:43:46.940089
---

# 从NTAuthCertificates证书伪造到域管理员身份验证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1ezau6IdDI4dkNb5HjCRXPfc58iasicXldWoibFyodsC0KYuRIobObXRZjQ/0?wx_fmt=jpeg)

# 从NTAuthCertificates证书伪造到域管理员身份验证

原创

th1e

山石网科安全技术研究院

还记得我之前的文章吗？我们探索了域控制器上的默认 DCOM 权限，用一些自定义的 Powershell 脚本，整理出了一个包含我所需全部信息的 Excel 表。

但是当我发现这两个应用程序 ID 时，我感到非常震惊：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eWnxDhKzPRTez4CdlS2GbAaCwAgJ42kf27NFlHicgU1wPKjECGaiaFXEQ/640?wx_fmt=png&from=appmsg)

第一个应用程序 ID 是 sppui，编号为：{0868DC9B-D9A2-4f64-9362-133CEA201299}，它因为模拟了交互式用户而显得格外引人注目。再加上授予所有人从远程激活这个应用程序的权限，这可能会导致一些意外的权限提升。

DCOMCNFG 工具的输出结果证实了我的分析...

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eS14bs9GCia7wiassRJIRC9lN8VRSDaCmuG9Lfk5mKiclqnhUTey3OpziaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eo4C0wlCia5oeOlcA2j1I853KlNrbC0oBQFvoia7UWWGHxpSib8hvrkARQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1e6j9prC2Dqpa8QZoMceszJiaPF9OmZHyYytY5b2y52r8nib04Bgb5KDug/640?wx_fmt=png&from=appmsg)

但是，这并不意味着所有人都可以远程激活这个 DCOM 应用程序。我们还需要看看对everyone设置的默认限制：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1ezDlG5L9RicykEF1xajdlR8amcOmv4tQnibVRzibW4psdDwic5qAN5CXaGQ/640?wx_fmt=png&from=appmsg)

Everyone只能在本地激活和启动应用程序，但是，这里有两个特别的组，Distributed COM Users 和 Performance Log Users，他们可以远程激活和启动应用程序：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eMluSGCzytr74uqdjiauPJIJVvJeBJiauO3KD8nq0N6LYN5GU6BU0VVDw/640?wx_fmt=png&from=appmsg)

结合了所有人的权限，这就很有意思了！但在深入探讨之前，我们需要先看下sspui 这个应用程序是做什么的？

借助Oleview 工具，我们可以得到更多信息：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eYy1BX44usLxSyDSUWXqpiaicfP6wxicicW2JZDauQGAAX2WoanX4xZ8nkA/640?wx_fmt=png&from=appmsg)

这个应用程序的 CLSID 是 F87B28F1-DA9A-4F35-8EC0-800EFCF26B83 - SPPUIObjectInteractive Class，它作为一个本地服务器运行：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1etJclmkRsvhRUansBRichlfP5BTZwrQhf1l7m02QzMSWHn8ThykLHscg/640?wx_fmt=png&from=appmsg)

slui.exe 与许可激活服务相关，并提供了一些接口：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eKHKmgsH3IU92t83TnUm25HIb5TOOfoSO3phyhumH5iaT4dRUMwy448A/640?wx_fmt=png&from=appmsg)

乍看之下，这些实现的方法对攻击者来说似乎并不太有吸引力。

然而，我们有这个 DCOM 对象，在交互式用户的环境中运行，可以被这两个组的成员远程访问。那么，为什么不尝试利用我们的 \*potato exploit 来强制认证呢？

如果成功，我们就能截获连接到域控制器的用户的认证，而这个用户理论上应该是域管理员。

这和我之前在 ADCCoercePotato 中做的非常相似，不同的是，如果我们想指定用户登录的特定会话 ID，我们可能还需要实现跨会话激活。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eoyibW0yvyjtv36DfDR0Aru8HXYtEgm4Cq4icPPRbZ5REBxIYp6kW10eA/640?wx_fmt=png&from=appmsg)

关键是有两个认证过程：第一个在 oxid resolve 调用时发生，第二个在受害者尝试连接恶意端点时发生。

## unsetunset第一个认证unsetunset

我首先尝试了第一种方法，很容易就触发并截获了连接到目标域控制器的域管理员的 NTLM 认证。

为了测试，我冒充了我的用户“simple”，他是一个普通的域用户，也是“Performance Log Users”域组的成员：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eGekPmr8SPvO1oPckrErjkPOmibXMSPuDtTntA5bYupSXVhXafKCDqGw/640?wx_fmt=png&from=appmsg)

我使用了“SilverPotato”工具，这是 ADCSCoercePotato 的改进版本：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1evNiasI6GlTIbkNqFVJHcmwU2ostT957R3cqolpUCRpF9PfzupKkvCpA/640?wx_fmt=png&from=appmsg)

在这个例子中，我用 -m 指定了目标域控制器的 IP 地址，用 -k 指定了运行 socat 重定向器和 ntlmrelayx 的 Linux 服务器的 IP 地址：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eF9jXKyncBht6CwpLuO7rzN7bNKhguT86ibMQvD07EvJw1qBC3eLxh6A/640?wx_fmt=png&from=appmsg)

结果证明，我获得了在第一个会话中连接的管理员的认证。

我决定将认证转发到 ADCS 服务器的 SMB 服务，默认情况下，该服务没有启用签名，并且我转储了本地 SAM 数据库：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eDPLOp7RTa1QtKdmZxV8EwH4EjwdGcEwZx0e84urUicyGQA87pMeUN2g/640?wx_fmt=png&from=appmsg)

有了本地管理员的 NT 哈希，我就可以通过哈希传递（Pass The Hash）方式访问 ADCS 服务器，备份 CA 的私钥/公钥，并获取 CRL 配置。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eRmQK3LShbEcyay24CntDL0slwSy4LRaYgp4mnRPOmje6OcKFQd2pkA/640?wx_fmt=png&from=appmsg)

PS：当然，还有其他方法可以在目标服务器上实现远程代码执行。例如，利用 ntlmrelay 将我带有反向 shell 的恶意 wbemcomn.dll 文件复制到 c:\windows\system32\wbem 目录。这个文件被加载，就可以赋予我以 SYSTEM、Network Service 或已登录用户的权限的 shell。

在此之后，我用 ForgeCert 工具成功代表域管理员请求了一个证书，使用的是 CA 的备份文件。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1ek61ib2ZbTKoCCneDqMF5GYLYAcqJxjU6ANVnicySbcT0cAHnvhkv8wQA/640?wx_fmt=png&from=appmsg)

最后，我用 Rubeus 请求了一个 TGT，并以管理员的身份登录到域控制器。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eEWib84EWLjMX2GWKCh5ATOzGlajWAvib5sdu7WtLyzLZDRrxFAClHkdw/640?wx_fmt=png&from=appmsg)

## unsetunset第二个认证unsetunset

接下来，我尝试利用我们在RemotePotato0中部署的第二种认证方法。

但出乎意料的是，这次得到的模拟级别仅限于识别，这对于SMB或HTTP来说没有任何作用，而且由于存在签名标志，它对LDAP/LDAPS也无法使用。

否则，如果服务主体名称（SPN）处于攻击者的控制之下，本可以利用Kerberos中继来代替NTLM。

## unsetunset在第一次认证中使用KERBEROS中继？unsetunset

理论上，你可以在Marshalled Interface Pointer的“双字符串”数组的安全绑定字符串中的首次调用时指定服务主体名称（SPN）：

```
typedef struct tagSECURITYBINDING
{
    unsigned short    wAuthnSvc;     // 必须非 0
    unsigned short    wAuthzSvc;     // 必须非 0
    unsigned short    aPrincName;    // 以 NULL 结束
} SECURITYBINDING
```

我使用 -y 参数来指定 SPN：![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1edRibmIbXQzNUrbmQhIQtjH0DcAAxWorgExrjicZj4g06J82QkiaYS6bJA/640?wx_fmt=png&from=appmsg)

但我的测试并不成功，我总是在 NTLM3 消息中收到 SPN：RPCSS/IP：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1eVGomRVXltpo1fR291qv6ldlNWJUCnGu6h5ezicUibw3jZH6tXUOcqfFQ/640?wx_fmt=png&from=appmsg)

我尝试了一些测试，在 KrbRelay 工具的基础上增加了一层复杂性，使得 SilverPotato 这个强大的工具能够运行。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQtHTTccuTrpW74icACpMF1e2jODw40picyd8Wa4dMpaIROgvDoAtEvVqsy63L4YUA50Bba8OTL5dmA/640?wx_fmt=png&from=appmsg)

## unsetunset结论unsetunset

这个“漏洞”可能已经存在多年了，那么它到底有多危险？

像“分布式COM用户”和“性能日志用户”这样的组成员并不普遍，尤其是在整个域中。而且，“分布式COM用户”组有时被视为最高级别的资产。

但思考一下：能够远程强制和中继（NTLM）高权限账户的认证，这是极其危险的。这是将特权账户纳入受保护用户组的又一个理由！

另一个需要考虑的点是这种方法也适用于本地的“分布式COM用户”和“性能日志用户”组。所以，这实际上取决于当时谁登录到服务器。

我建议仔细审查这些组的成员身份，一定要将这些组视为最高级别！

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