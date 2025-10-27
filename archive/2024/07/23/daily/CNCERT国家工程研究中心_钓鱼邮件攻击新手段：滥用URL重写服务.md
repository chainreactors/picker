---
title: 钓鱼邮件攻击新手段：滥用URL重写服务
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545967&idx=2&sn=cc5b89917d299c488f3f5847c191984d&chksm=fa9382aecde40bb852491b165803b44fc6f6f6c7f0ad39a346ac1a976019b6def0d19f0864c3&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-23
fetch_date: 2025-10-06T17:43:49.606810
---

# 钓鱼邮件攻击新手段：滥用URL重写服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l2Vl9U17kydomXHhRicg4zeoS82PPu9Dib5zibG39cI6cs2yib04kx9iaBYepdyLHesJaXXeQwrZn2z6A/0?wx_fmt=jpeg)

# 钓鱼邮件攻击新手段：滥用URL重写服务

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l2Vl9U17kydomXHhRicg4zelBiblPfYztxacbEZsTV3jUHiaKM3gE95VFws63OGCcZDHricBticLe763g/640?wx_fmt=png&from=appmsg)

钓鱼攻击一直是企业和个人用户面临的主要威胁之一。为了应对这种威胁，许多电子邮件安全服务引入了URL重写（保护）技术，通过声誉过滤器阻止用户访问已知钓鱼网站。然而，近期的一些钓鱼活动却利用这种保护技术来实施攻击。

安全公司Barracuda Networks最新报告显示：“从2024年5月中旬开始，网络钓鱼攻击者开始利用三种不同的URL重写服务来掩盖钓鱼网站URL。这些URL重写服务由值得信赖的合法品牌提供。到目前为止，此类滥用URL重写服务攻击已经攻击了数百家甚至更多的公司。”

# **URL重写服务的工作原理**

URL重写服务是电子邮件安全供应商在安全邮件网关和云邮件服务中广泛使用的一种对电子邮件中的链接进行即时声誉检查的工具，通过重写传入或传出电子邮件中的链接，使其指向由安全受控的域名和服务。

当用户点击重写的链接时，服务器会检查该链接是否指向已知的钓鱼或恶意软件网站，并根据检查结果决定是阻止访问还是重定向到安全网址。这种方法的好处在于，如果一个网站在稍后被标记为恶意，所有指向它的重写链接都将停止工作，从而为所有用户提供保护。

# **URL重写的技术缺陷与挑战**

尽管URL重写服务在理论上具有保护作用，但其实际效果却存在争议。首先，这种方法会破坏加密电子邮件签名，因为安全电子邮件网关通过更改链接修改了原始电子邮件。其次，重写的链接掩盖了真实的目的地网址，这使得用户无法通过查看链接来识别钓鱼网站。

例如，微软在其Office 365用户中提供了名为“安全链接”的功能，该功能会重写传入电子邮件和应用程序（如Outlook和Teams）中的链接。然而，这一功能过去曾被安全公司批评，原因包括不进行动态扫描或容易被基于IP的流量重定向绕过——微软的IP地址是公开的——或通过使用来自合法和受信任域名的开放重定向URL。

URL重写服务最大的缺点是，其链接声誉检查基于黑名单机制，而一个新钓鱼网站被添加到安全厂商的黑名单所需的时间各不相同。这可能需要几分钟、几小时或几天，取决于是否有人报告。一些安全厂商比其他厂商动作更快，攻击者也知道这一点。域名相当便宜，等到一个域名因托管钓鱼网站而被标记时，可能已经有数百名用户成为其受害者

# **攻击者如何滥用URL重写服务**

目前尚不清楚Barracuda观察到的钓鱼活动如何重写指向钓鱼网站的URL。研究人员推测，他们可能入侵了使用这些服务的企业内部电子邮件账户，然后向这些被入侵的帐户发送电子邮件或从这些被入侵的帐户发送电子邮件以强制进行URL重写。

然后，攻击者只需从生成的电子邮件消息中获取重写的URL，用来制作新的钓鱼电子邮件。

一些使用URL重写技术的钓鱼电子邮件伪装成来自微软的密码更改提醒或来自DocuSign的文档签名请求。这些电子邮件包含被仿冒服务的典型品牌元素，包括使用重写链接将用户重定向的按钮。

面对滥用URL重写服务的钓鱼邮件攻击，Barracuda的研究人员强调，安全措施应与安全意识培训相结合，企业和个人用户应保持警惕，及时更新安全策略，以应对不断变化的网络威胁。

**参考链接：**

https://blog.barracuda.com/2024/07/15/threat-spotlight-attackers-abuse-url-protection-services

原文来源：GoUpSec

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