---
title: F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=1&sn=300b30047d4cb364fa903361e05d3052&chksm=ea948c2edde30538eab915c12ac7b6a1d83fe856638e1a22d727813fb060b9c1ad7f612dfa10&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-04
fetch_date: 2025-10-04T05:41:19.497736
---

# F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTSkv6nKuLlIw8kw8U2PGrDqO2IjiaTEpCBcvuOaZMF0KWFKQOkia40TKD6yYORfcPKve7LtW5Z5g4g/0?wx_fmt=jpeg)

# F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**F5 提醒称，BIG-IP 中存在一个高危格式化字符串漏洞 (CVE-2023-22374)，可导致认证攻击者触发拒绝服务条件并可能执行任意代码。**

该漏洞影响一个公开的API即 iControl SOAP，该API用于赋能系统间的通信。SOAP接口可通过BIG-IP管理端口和/或自己的IP地址从网络访问，且仅限于管理员账户。

发现该漏洞的Rapid 7 公司研究员解释称，攻击者可将格式化字符串规范插入传递到系统日志函数的特定参数中，导致该服务读写栈中所引用的内存地址。不过研究人员解释称，只有对系统日志拥有访问权限，攻击者才能读取内存，“影响特定地址被读取和写入比较难，因此在实际中该漏洞很难被利用（除非服务崩溃）”。

研究人员提到，攻击者可通过 “%s”规则使服务崩溃并使用 ‘%n’ 规则将任意数据写入栈中的任意指针中，从而可能导致远程代码执行后果。

F5 公司在安全公告中指出，利用该漏洞实现代码执行后果的攻击者，首先需要收集运行该易受攻击组件的环境信息，而该漏洞仅暴露了控制面板而非数据面板。研究人员表示，“攻击成功造成的最可能的后果是导致服务器进程崩溃。技能较高的攻击者可能会开发远程代码执行exploit，以root用户身份在F5 BIG-IP设备上运行代码。”

该漏洞影响BIG-IP 版本13.1.5、14.1.4.6到14.1.5、15.1.5.1到15.1.8、16.1.2.2到16.1.3和17.0.0版本。目前该漏洞尚无补丁，不过F5 公司表示已经给出工程热修复方案。

由于该漏洞仅可遭认证用户利用，因此应仅允许受信任用户访问 iControl SOAP API。

CVE-2023-22374对于标准部署模式下的BIG-IP 系统的CVSS评分为7.5，而对于应用模式下的BIG-IP 实例的CVSS评分为8.5。

BIG-IP SPK、BIP-IQ、F5OS-C、NGINX和Traffix SDC不受该漏洞影响。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[F5 BIG-IP 中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=1&sn=2d9be3c3a8cdaf6d29d8a13e49ef8ade&chksm=ea949f0bdde3161d6555a751e3ebbfcafc81bf7054808d430d94245936a2cff9d6591e182d51&scene=21#wechat_redirect)
[F5 多款产品中存在多个RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514661&idx=1&sn=ed03e7c7fed936ce5c82e4583a0df074&chksm=ea948b4fdde302593a589756559c66f23db2dff4547b4b3a335485b1a65abafd877d7bc5310a&scene=21#wechat_redirect)

[F5紧急修复严重的 BIG-IP 预认证 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502189&idx=3&sn=61decbf4d30e5620cdc2da9411057ff4&chksm=ea94f807dde371116d47ae9dcfbe607adfc79f03bb74b3f0af9cdb81963f832173d29c0031c1&scene=21#wechat_redirect)

[F5 以6.7亿美金收购 NGINX](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489404&idx=3&sn=ef5661e9f10525c4b74aeaaf826f89b8&chksm=ea972616dde0af0022d5638e629f41d252f5967779eab21ce079d74e2096a019c20d5dcb1a3a&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/f5-working-on-patch-for-big-ip-flaw-that-can-lead-to-dos-code-execution/

题图：Pixabay License‍

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