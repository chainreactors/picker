---
title: F5 多款产品中存在多个RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514661&idx=1&sn=ed03e7c7fed936ce5c82e4583a0df074&chksm=ea948b4fdde302593a589756559c66f23db2dff4547b4b3a335485b1a65abafd877d7bc5310a&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-18
fetch_date: 2025-10-03T23:07:27.931745
---

# F5 多款产品中存在多个RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRRVuZceCBAOzn5DXmYd0zlgutic4hVw3ibiaRpvDktFOSsSmtUszsLfiayp0kiathic88VD0UPw2pLMI5A/0?wx_fmt=jpeg)

# F5 多款产品中存在多个RCE漏洞

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全公司Rapid7表示，F5产品受多个漏洞和其它安全问题影响。**

Rapid7公司在8月中旬将研究成果告知F5，并在F5发布安全公告通知用户并推出工程热补丁之时，发布了相关漏洞详情。

研究人员指出，其中两个漏洞是高危漏洞并已获得CVE编号（CVE-2022-41622和CVE-2022-41800），而F5认为其余的安全绕过方法并非漏洞。

最严重的漏洞是CVE-2022-41622，它是影响 BIG-IP和BIG-IQ产品的一个跨站点请求伪造 (CSRF)漏洞，可导致远程未认证攻击者获得对设备管理接口的根访问权限，即使该接口并未暴露给互联网也不例外。

然而，漏洞利用要求攻击者具备一些目标网络知识，并需要说服已登录管理员访问专用于利用该漏洞的恶意网站。F5指出，“如遭利用，该漏洞可攻陷整个系统。”

第二个漏洞CVE-2022-41800，可导致具有管理员权限的攻击者通过RPM 标准文件执行任意shell命令。

另外，Rapid7 还发现多个安全问题，包括通过恶意Unix套接字权限提升本地权限以及两个SELinux 绕过方法等。该公司认为这些漏洞的利用遭广泛传播的可能性很低。然而，鉴于BIG-IP设备一直都是遭攻击的对象，因此F5客户不应忽视这些漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[F5 BIG-IP 中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=1&sn=2d9be3c3a8cdaf6d29d8a13e49ef8ade&chksm=ea949f0bdde3161d6555a751e3ebbfcafc81bf7054808d430d94245936a2cff9d6591e182d51&scene=21#wechat_redirect)

[F5紧急修复严重的 BIG-IP 预认证 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502189&idx=3&sn=61decbf4d30e5620cdc2da9411057ff4&chksm=ea94f807dde371116d47ae9dcfbe607adfc79f03bb74b3f0af9cdb81963f832173d29c0031c1&scene=21#wechat_redirect)

[速修复！严重的F5 BIG-IP 漏洞 PoC 已发布](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493895&idx=2&sn=a73d5272550172cb1cad1a9db810a29a&chksm=ea94d86ddde3517b3eae98b11015687925d9d6a92f13e5c33177e26200186a048887342c4c2c&scene=21#wechat_redirect)

[F5 以6.7亿美金收购 NGINX](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489404&idx=3&sn=ef5661e9f10525c4b74aeaaf826f89b8&chksm=ea972616dde0af0022d5638e629f41d252f5967779eab21ce079d74e2096a019c20d5dcb1a3a&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/remote-code-execution-vulnerabilities-found-f5-products

题图：Pixabay License‍

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