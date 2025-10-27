---
title: CISA：黑客滥用F5 BIG-IP cookie 映射内部服务器
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521056&idx=1&sn=87bda00602d2d1a2718a0d4d0aef6585&chksm=ea94a24adde32b5c9d17667624bfb3939b23bdfacadb88d7c4951c0084e42f7a5753504eaf86&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-13
fetch_date: 2025-10-06T18:51:00.510360
---

# CISA：黑客滥用F5 BIG-IP cookie 映射内部服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTO7lrTxib5ryF2M1gII1iaP9ARu8vEvSSGe9nA4kfnLmpXGV1HOdibySsMAibvCSa4ngiaMf9jeR6IA7g/0?wx_fmt=jpeg)

# CISA：黑客滥用F5 BIG-IP cookie 映射内部服务器

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CISA 提醒称，威胁行动者正在滥用未加密的可持久性 F5 BIG-IP cookie 来识别和攻击位于目标网络上的内部设备。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTO7lrTxib5ryF2M1gII1iaP964mCUxtlNwzGQyXvMOzWZJuRwWNtOvuVib2yBLvMFJNDmAky2beRAeQ/640?wx_fmt=gif&from=appmsg)

通过映射内部设备，威胁行动者们在网络安全的规划阶段，可识别网络上的易受攻击设备。CISA提醒称，“CISA 发现网络威胁行动者们利用由 F5 BIG-IP 本地流量管理器 (LTM) 模块管理的未加密可持久性 cookie 来枚举网络上的其它非面向互联网的设备。恶意网络人员可利用从未加密可持久 cookie 中收集的信息来推断或识别其它网络资源并可能利用网络上其它设备中发现的漏洞。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTO7lrTxib5ryF2M1gII1iaP9J0keeaAT2GtLdtRktJyf9VkmBYovw1M3WqGSMFpajiaXmxVEIjjYKkg/640?wx_fmt=gif&from=appmsg)

**F5 可持久性会话 cookie**

F5 BIG-IP 是用于负载均衡 web 应用和提供安全性的应用交付和流量管理工具套件，其中一个核心组件是本地流量管理器 (LTM) 组件，通过提供流量管理和加载平衡在多种服务器中分发网络流量。通过这一特性，客户优化负载均衡的服务器资源和高可用性。

该产品中的LTM模块，每次使用可持久性 cookie，将客户端 (web浏览器)中的流量指向相同的后端服务器（对于负载均衡至关重要），帮助维护会话的一致性。

F5在文档中提到，“cookie可持久性使用HTTP cookie增强可持久性。和所有的可持久性模式一样，HTTP cookie 确保同一个客户端的请求，在BIG-IP系统最初负载均衡后，被定向到相同的资源池成员中。如果该资源池成员不可用，则该系统会做出新的负载均衡决策。”

这些cookie 默认未加密，可能会通过遗留配置或性能考虑来维护操作完整性。从11.5.0版本开始，管理员可通过新的 “必选”选项在所有cookie 上执行加密。未选择该选项的人员可能会暴露到安全风险中。然而，这些 cookie 中包含编码的IP地址、端口号码和内部负载均衡服务器的负载均衡设置。

多年来，网络安全研究人员已分享过如何滥用未加密 cookie 来找到此前隐藏的内部服务器或可能的未知已暴露服务器，以扫描其中的漏洞并攻陷内部网络。BIG-IP 管理员也可借助Chrome 扩展解码这些cookie，调试连接。

CISA 提到，威胁行动者们已经在利用这一可能性，利用可能的配置问题发现网络。CISA 建议F5 BIG-IP 管理员查看厂商指南，了解如何加密这些可持久 cookie。由于中间点“偏好”配置选项生成了加密的 cookie 但还可导致系统接受未加密 cookie，因此该设置可用于迁移阶段来使此前发布的 cookie 在执行加密 cookie 前继续工作。

当设置为“必选”时，所有可持久 cookie 通过AES-192 加密算法进行加密。CISA 还提到F5还开发了一款诊断工具 “BIG-IP iHealth” 来检测产品中的配置不当问题并对管理员发出告警。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[F5修复BIG-IP 和 NGINX Plus 中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520531&idx=1&sn=3711327c08007954c754b1a665f4b963&chksm=ea94a079dde3296fb3e16aed65fdb526227e260cd11c96212ca1fd8bbde8380e989c2c1c2f57&scene=21#wechat_redirect)

[F5修复可导致RCE的 BIG-IP 认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518011&idx=2&sn=bc312f0c5810515223f4c329eb996ee3&chksm=ea94b651dde33f47c81f15553198c52a0b6b0ced84cf7a06c3f8cca4a506c0b5a7b5f9aa959c&scene=21#wechat_redirect)

[F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=1&sn=300b30047d4cb364fa903361e05d3052&chksm=ea948c2edde30538eab915c12ac7b6a1d83fe856638e1a22d727813fb060b9c1ad7f612dfa10&scene=21#wechat_redirect)

[F5 多款产品中存在多个RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514661&idx=1&sn=ed03e7c7fed936ce5c82e4583a0df074&chksm=ea948b4fdde302593a589756559c66f23db2dff4547b4b3a335485b1a65abafd877d7bc5310a&scene=21#wechat_redirect)

[F5 BIG-IP 中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=1&sn=2d9be3c3a8cdaf6d29d8a13e49ef8ade&chksm=ea949f0bdde3161d6555a751e3ebbfcafc81bf7054808d430d94245936a2cff9d6591e182d51&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-hackers-abuse-f5-big-ip-cookies-to-map-internal-servers/

题图：Pexels License

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