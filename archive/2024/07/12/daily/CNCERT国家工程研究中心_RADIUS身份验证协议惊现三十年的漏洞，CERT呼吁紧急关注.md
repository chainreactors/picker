---
title: RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545807&idx=3&sn=7f6db24ad10a606511a85329be57f3f9&chksm=fa93850ecde40c18b691df71506bee2aadd9fac8fddba238c8564b80869a3005d642b3301149&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-12
fetch_date: 2025-10-06T17:44:21.411059
---

# RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kbOqsIucNT7iaVaCsqYaLw65LFlnibicQX5fv6ib757rQ1ibdJJmGmLOlvfqst7bv0bp5EAzmiaayE3JHg/0?wx_fmt=jpeg)

# RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注

网络安全应急技术国家工程中心

近日，网络安全研究人员发现RADIUS网络身份验证协议中存在一个安全漏洞，Blast-RADIUS可以利用该漏洞发动中间人（MitM）攻击，并在特定情况下绕过完整性检查，CERT、InkBridge Networks等多个安全机构呼吁积极关注该漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38iaaGpAwJUOYX6ESmk89p2TGKACyXjjzODGwn9fXIPYggUrwdTmOBrq0xKJw1w2pstL2ktx7sR4lQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

# **关于Blast-RADIUS**

Blast-RADIUS是目前广泛应用的RADIUS/UDP协议中的一种认证绕过技术，可以使攻击者在中间人MD5冲突攻击中攻破网络和设备。
InkBridge Networks的首席执行官、FreeRADIUS项目的创始人Alan DeKok在一份声明中说：RADIUS 协议允许某些访问请求信息无需进行完整性或身份验证检查。

> RADIUS是远程身份验证拨号用户服务的简称，是一种客户端/服务器协议，为连接和使用网络服务的用户提供集中身份验证、授权和记账（AAA）管理。

RADIUS的安全性依赖于使用MD5算法导出的哈希值，由于存在碰撞攻击的风险，截至2008年12月，MD5算法被认为在密码学上已被破解。

因此，攻击者可以在不被发现的情况下修改这些数据包，将能够强制任何用户进行认证，并给予该用户任何授权（例如VLAN等）。

这意味着访问请求数据包可能会受到所谓的选定前缀攻击，使得可以修改响应数据包，以便它通过原始响应的所有完整性检查。

需要注意的是，要使攻击成功，攻击者必须修改在客户端和服务器之间传输的RADIUS数据包。那么，通过互联网发送数据包的组织将面临该漏洞带来的风险。

# **漏洞利用细节**

Blast-RADIUS利用了一个新的协议漏洞CVE-2024-3596和MD5碰撞攻击，允许访问RADIUS流量的攻击者操纵服务器响应并添加任意协议属性，这使他们无需暴力或窃取凭证即可获得RADIUS设备的管理权限。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38iaaGpAwJUOYX6ESmk89p2TIwCia4mcad7lGZMrZYo3SLfiaF6bPSVib6MQtwJ518o1BZanC8W1ias4qQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Blast-RADIUS研究人员解释说：Blast-RADIUS攻击允许位于RADIUS客户端和服务器之间的中间人对失败的认证请求伪造有效的「访问接受」响应。攻击者通过向有效的客户端请求中注入恶意的「代理状态」属性来实现这一点。这个「代理状态」属性肯定会在服务器的响应中被回显。攻击者构造「代理状态」，使得有效响应和攻击者希望伪造的响应之间的响应验证器值相同。这种伪造将导致NAS（网络访问服务器）在攻击者不猜测、暴力破解密码或共享机密的情况下授予对手对网络设备和服务的访问权限。

研究人员表示：「利用此攻击的攻击者可以将部分网络访问权限升级为能够登录任何使用RADIUS进行身份验证的设备，或为自己分配任意网络权限。」

研究人员的概念验证漏洞（尚未共享）计算了伪造有效「访问-接受」响应所需的MD5选择前缀哈希冲突，以表示成功的身份验证请求。然后，利用中间人攻击将伪造的MD5哈希值注入网络通信，使攻击者能够登录。

伪造这个MD5哈希值需要3到6分钟，比RADIUS在实践中常用的30到60秒超时要长。

不过，攻击中使用的碰撞算法的每个步骤都可以有效地并行化，并适合硬件优化，这将使资源充足的攻击者能够使用GPU、FPGA或其他更现代、更快速的硬件来实施攻击，从而实现更快的运行时间，可能快数十倍或数百倍。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38iaaGpAwJUOYX6ESmk89p2Tdutib9GVu3rZcCbichuBUhR6sbOTxLw4GwVIac0dTfiahbF3YR6M95cpQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

攻击流程（Blast-RADIUS 研究团队）

研究团队表示，虽然MD5哈希碰撞在2004年已首次被证实，但当时仍有人对在RADIUS协议中加以利用表示质疑。

# **缓解措施**

由于这种攻击不会危及最终用户的凭证，因此最终用户无法采取任何防范措施。

不过，BlastRADIUS是一个基本设计缺陷的结果，据说会影响所有符合标准的RADIUS客户端和服务器，具体来说，PAP、CHAP和MS-CHAPv2认证方法是最脆弱的，建议使用该协议的互联网服务提供商(isp)和组织更新到最新版本。

网络运营商可以升级到RADIUS over TLS (RADSEC)，转而采用「multihop 」RADIUS 部署，并使用限制访问管理VLAN 或 TLS/ IPsec隧道将RADIUS流量与互联网访问隔离。

另外，还可以通过Message-Authenticator属性提高数据包安全性。

**参考资料：**

https://www.blastradius.fail/attack-details

https://www.bleepingcomputer.com/news/security/new-blast-radius-attack-bypasses-widely-used-radius-authentication/

https://thehackernews.com/2024/07/radius-protocol-vulnerability-exposes.html

原文来源：FreeBuf

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