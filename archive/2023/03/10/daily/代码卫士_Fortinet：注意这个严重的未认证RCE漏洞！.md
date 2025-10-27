---
title: Fortinet：注意这个严重的未认证RCE漏洞！
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=1&sn=d2ef6b5ab51eba3e97af531d1a8b212b&chksm=ea948fbcdde306aa2d71b31b492175fc0c01a69233601e35fc9fee73fbfbae62668f3aaaffb2&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-10
fetch_date: 2025-10-04T09:10:34.371815
---

# Fortinet：注意这个严重的未认证RCE漏洞！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRMrrWLnahV80FeT4ZDEGsIo8uicUwdGVFnhU9tUibTicFzhh2YMnSPUxWfZaibRxnjtx63unDk84Cs2Q/0?wx_fmt=jpeg)

# Fortinet：注意这个严重的未认证RCE漏洞！

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Fortinet 披露了影响FortiOS和FortiProxy的一个严重漏洞 (CVE-2023-25610)，它可导致未认证攻击者通过特殊构造的请求，在易受攻击设备的GUI上执行拒绝服务。**

该缓冲区溢出漏洞的CVSS评分为9.3分，是“严重”等级的漏洞。当程序尝试从内存缓冲区中读取的数据多于可用数据时就会触发，导致访问邻近的内存未知，引发风险行为或崩溃后果。

Fortinet 发布安全公告称，尚未发现该漏洞遭在野利用的迹象，并提到影响如下产品：

* FortiOS 7.2.0至7.2.3
* FortiOS 7.0.0至7.0.9
* FortiOS 6.4.0至6.4.11
* FortiOS 6.2.0至6.2.12
* FortiOS 6.0，所有版本
* FortiProxy 7.2.0至7.2.2
* FortiProxy 7.0.0 至 7.0.8
* FortiProxy 2.0.0 至 2.0.11
* FortiProxy 1.2，所有版本
* FortiProxy 1.1，所有版本

修复该漏洞的目标升级版本为：

* FortiOS 7.4.0及以上
* FortiOS 7.2.4及以上
* FortiOS 7.0.10及以上
* FortiOS 6.4.12及以上
* FortiOS 6.2.13及以上
* FortiProxy 7.2.3及以上
* FortiProxy 7.0.9及以上
* FortiProxy 2.0.12及以上
* FortiOS-6K7K 7.0.10及以上
* FortiOS-6K7K 6.4.12及以上
* FortiOS-6K7K 6.2.13及以上

Fortinet 公司表示，在安全通告中列出的50款设备机型并不受该漏洞任意代码执行部分的影响，仅受拒绝服务部分的影响，即使它们运行的是易受攻击的FortiOS 版本也不例外。

未在公告中列出的设备机型同时受任意代码执行和拒绝服务影响，因此管理员应当尽快应用可用的安全更新。如无法应用，则建议禁用HTTP/HTTPS管理员接口或限制可远程访问该接口的IP地址，这些都是可用的应变措施。安全公告中提供了如何应用这些应变措施的指南。

威胁行动者密切关注影响 Fortinet 产品的严重漏洞，尤其是无需认证即可利用的漏洞，因为它们可借此获得对企业网络的初始访问权限。因此快速缓解该漏洞十分重要。例如，2月16日，Fortinet公司修复了影响 FortiNAC和FortiWeb 产品的两个严重的远程代码执行漏洞，呼吁用户立即应用这些安全更新。四天之后，利用该漏洞的PoC exploit 就出现，而活跃的在野利用始于2023年2月22日。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Fortinet修复两个严重的RCE漏洞，其中一个两年前就发现？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515647&idx=1&sn=b8f00a46755a56f7d9aed5ae56c1b4e4&chksm=ea948c95dde305837c4ef5d418e236f9718061ffd9b877fde4fc8a267a7bf0b9910d885f6ea4&scene=21#wechat_redirect)

[Fortinet 两款产品FortiTester和FortiADC中存在高危命令注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515203&idx=1&sn=0154c72722b8b2c44432c3c779bc5ce6&chksm=ea948d29dde3043f88a8f390467e5fe9417ffdbb15210cc62b5ca63cb1bb7d11d80897439b47&scene=21#wechat_redirect)

[Fortinet 紧急修复已遭利用的VPN漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514989&idx=1&sn=d69be3f378da5be4993977d510a35a5b&chksm=ea948a07dde303111a95aab98531af127bcaa9ad279aa46a8fbf4f7e56f0053a9bc6ba7c4ac8&scene=21#wechat_redirect)

[Fortinet 修复6个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514392&idx=2&sn=d3a167944c3d8a1d891c716450e26210&chksm=ea948872dde3016465bc0576d1de3d5f0be89e0a4cf7ef01370a82224cb557ef613a3252ccd8&scene=21#wechat_redirect)

[Fortinet：立即修复这个严重的认证绕过漏洞！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514120&idx=2&sn=e9b6c1a8e128a9eee70880b0fc3cce94&chksm=ea948962dde300745ee1435a5b05de3016d29440d127c2f0dad65ea6b5b80bc83b6a301afaec&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-critical-unauthenticated-rce-vulnerability/

题图：Pixabay License

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