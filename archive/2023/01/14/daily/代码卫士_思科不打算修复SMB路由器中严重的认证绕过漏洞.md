---
title: 思科不打算修复SMB路由器中严重的认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515297&idx=2&sn=460499858dd7355f4569e49b316d18b4&chksm=ea948dcbdde304dd13d7b674af7f35b59b16dd02b31770de7ae9738688f20bcc072fae10dce9&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-14
fetch_date: 2025-10-04T03:53:26.992175
---

# 思科不打算修复SMB路由器中严重的认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRsopR0py9qMwUUEVviawsjfmKnHvLrudoP6hibtPibBc1PCl6MFFLzKicXAQGjaQic7eqcQLVVet25zcQ/0?wx_fmt=jpeg)

# 思科不打算修复SMB路由器中严重的认证绕过漏洞

Tara Seals

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfRslITzFHvzvVSmaPAQ7kEozCzmmy06V2N0k7OeI2jJWib0Ze8yIvEZw/640?wx_fmt=gif)

**思科SMB路由器中存在两个严重的漏洞（CVE-2023-20025和CVE-2023-20026），可导致未认证攻击者完全控制目标设备，以root权限运行命令。遗憾的是，即使已存在在野PoC exploit，思科仍然不打算修复。**

漏洞如遭成功利用，可导致攻击者窃听或劫持VPN和会话流量，在企业网络中进行横向移动站稳脚跟或者运行密币挖矿僵尸网络客户端或其它恶意软件。Bugcrowd 公司的创始人兼首席技术官 Casey Ellis 指出，“从技术角度来看，它是一个具有吸引力的目标。作为攻击者，如果你能够设法在核心路由或网络基础设施上执行远程代码，则横向移动的能力呈指数级增长。”

**0****1**

**可获取root权限**

第一个漏洞是严重的认证绕过漏洞CVE-2023-20025，位于设备的Web 管理接口中，CVSS评分为9分。第二个漏洞CVE-2023-20026可导致远程代码执行后果，不过攻击者需要在受影响设备上具有合法的管理员凭据才能利用成功，因此该漏洞被评级为“中危”，CVSS评分为6.5。

这两个漏洞均影响RV016、RV042、RV042G和RV082路由器，它们已达到生命周期期限。因此思科在1月11日发布的安全公告中提到将不会发布安全更新。公告中提到，这两个漏洞都是因为“在进站HTTP数据包中对用户输入验证不当造成的”，因此攻击者只需要向基于Web的管理接口发送构造的HTTP请求即可获得底层操作系统上的root访问权限。

思科“已发现本安全公告中相关漏洞的PoC利用代码”，不过目前尚未发现在野攻击迹象。思科提到，虽然目前不存在相关应变措施，但可以禁用路由器的远程管理并拦截对端口443和60443的访问作为缓解措施。也就是说路由器仅可通过LAN接口访问。

Netenrich 公司的首席威胁猎人John Bambenek 指出，“不允许远程管理可从开放互联网访问的网络设备一直都是最佳实践，不过使用某些MSP/MSSPs的小企业必须将其为服务提供商打开。也就是说，PoC代码公开可用而无补丁的情况是最糟糕的。”

替换相关设备是保护企业不受威胁的最佳方式。

**0****2**

**巨大影响**

研究人员表示，相关路由器的安装数量非常庞大，即使它们已停用。过期设备仍然用于业务环境中的情况并不少见，而这就提供了庞大的攻击面。

Vulcan Cyber的高级技术工程师 Mike Parkin 提到，“受影响的思科小企业路由器的使用仍然广泛，尽管它们已被官方认为到达生命周期期限。未来的挑战就是这些设备一般存在于资源有限的小企业中或者为没有替换预算的个体使用。”

Ellis 提到，受影响的并非只有中小企业，“SMB路由器的部署非常广泛，而且在疫情后的远程工作情境下，它不仅仅是SMB的问题。它的潜在用户是分公司办公室、卓越中心、甚至是家庭办公室。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[思科提醒：很多严重漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515090&idx=1&sn=331cbd89b5964aa09cd03b9468ba13a5&chksm=ea948ab8dde303ae69139bb78ecfe2cb40235baf8d8e9fbffac6b7eebb2340100e8e16c3dd86&scene=21#wechat_redirect)

[思科ISE多个漏洞可用于一次点击exploit](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514814&idx=1&sn=4b21aca000d15beda25426bb096a28d7&chksm=ea948bd4dde302c24b745c39ef1eac1f344225d97e67e0eea5c1563b626468ec92c838104593&scene=21#wechat_redirect)

[思科决定不修复已达生命周期路由器中的认证绕过0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513869&idx=2&sn=7199bcc2306ffa52728d244b3157c9c6&chksm=ea948667dde30f7126092d37c3a6b6ec03c1517c0a95065187739d5cfc9e2b810e54fa40d8b9&scene=21#wechat_redirect)

[思科ASA防火墙中存在多个漏洞，可被用于供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513544&idx=2&sn=6c9886f2668674b71400b4eb1ccba93b&chksm=ea9484a2dde30db499db8f0b34a1e531a5db4571bb73988dfbc334e6409862d01a8840d94942&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/remote-workforce/critical-cisco-smb-router-bug-authentication-bypass-poc-available

题图：Pexels License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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