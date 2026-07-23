---
title: HollowByte：11字节 payload 耗尽 OpenSSL 服务器内存
url: https://mp.weixin.qq.com/s/7UZpHD2ODjF-HBUyARQB-w
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:48.335127
---

# HollowByte：11字节 payload 耗尽 OpenSSL 服务器内存

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfX81MZo99OXJpTteGhUiah0iaSkLXzlrFwJibOQibnnYlR7FOdd3GgmlyoVSpDicPxQMEYiatOiblppc87OHBITpV09aOibeeVkMvicXZcg/0?wx_fmt=jpeg)

# HollowByte：11字节 payload 耗尽 OpenSSL 服务器内存

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**一个名为****“HollowByte****（空心字节）”****的漏洞可导致未认证攻击者，通过仅有****11****个字节大小的恶意****payload****在****OpenSSL****服务器上触发拒绝服务条件。****OpenSSL****团队已悄悄修复该漏洞（无编号）并将补丁向后移植到老旧版本。**

由于OpenSSL 软件是安全互联网通信的基础性支柱，各组织机构应优先切换到已修复版本的库。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUvFzSNLqAiahQtXN6zkViamZ4eJ16077QzyFPYu0b66B1z37Xabh2aPqSxAVbErYxneDD1jibR5LEDZtIiabWdCTZhRAic6g6SCMO0/640?wx_fmt=gif&from=appmsg)

**“空心字节”详情**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUrCC29FFWTc0KMpPGTJQEVQzmLl1au7K53t6FX56GIpdhTnI1ynjDDwibx4TJRaUhLI8y1Tg03zw6Jooleic5icA7ewnWicqKMhnA/640?wx_fmt=gif&from=appmsg)

前不久，Okta 公司发布公告说明了“空心字节” DoS漏洞的工作原理及其在实际场景中的影响。研究人员解释称，在TLS握手过程中，每条消息都有一个4字节的标头，用于声明传入消息的大小。然而，受影响的OpenSSL版本在接收 payload 并检查大小之前，会先按声明的长度分配内存。每条TLS握手消息均以一个4字节的握手标头开始，其中包含一个三字节的长度字段，用于说明后续握手数据的大小。服务器在没有验证 payload 的情况下，会信任数据包的声明并按指示分配内存。“工作线程随后阻塞，无限期地等待永远不会到达的数据”。

未经身份验证的攻击者可以通过打开一个TLS连接并发送一个11字节的恶意输入来触发“空心字节”，该输入在标头中声明将有一个大得多的消息体紧随其后。攻击者在多个连接上重复相同过程，导致服务器通过相对少量的已传输数据分配大量内存。

研究人员指出，虽然OpenSSL在连接断开时会释放缓冲区，但GNU C库（glibc）对内存的处理方式不同，“不会立即将小到中等大小的分配归还给操作系统，而是保留它们以备将来重用。通过发起一系列连接，并随机化声明的大小，攻击者可以阻止分配器重用那些已被释放的内存块。堆被严重碎片化，导致服务器的常驻集大小（RSS）持续攀升。即使在攻击者断开连接后，服务器仍然永久性地膨胀。”完全回收这些空间的唯一方法是重新启动进程。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfU7EtyfQmuEvvrQpkKSSRMEziclhMPzNK7ZWAWudcs0ibCHPxoCW2j7ILv7x39eoPkFVmDzsficfe2iap5ibHr7FofZMd08icfukFN54/640?wx_fmt=gif&from=appmsg)

**影响与修复**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVtPhuluMBGiaLDKTBicMe5MdQickVD1LGBW2ZchaHJjb8kEXstzhSP7CsEzlHYvPYKmlgd3yKq5ic52Cvme6GEOfJnfam3Tib4ibnRM/640?wx_fmt=gif&from=appmsg)

OpenSSL开源库被嵌入到流行的软件项目中，如NGINX和Apache Web服务器、语言运行时（例如Node.js、Python、Ruby、PHP）以及数据库（MySQL、PostgreSQL）中。它预装在大多数Linux发行版中，用于TLS加密和证书处理。

Okta对NGINX的测试表明，低容量环境可以很容易地通过“空心字节”耗尽内存，而更高规格的服务器可能会损失多达25%的内存，同时攻击带宽仍低于安全告警阈值。尽管DoS漏洞被视为不如数据窃取或代码执行漏洞严重，但它们可能导致运营中断和声誉损害。

OpenSSL 已在 4.0.1 版本中修复“空心字节” DoS 问题，并向后移植到3.6.3、3.5.7、3.4.6和3.0.21版本，这些版本现在仅在数据到达时才扩展缓冲区，而忽略标头中的大小声明。尽管该问题被作为“加固修复”而非安全漏洞处理，但研究人员仍建议“立即升级所用发行版的OpenSSL软件包”。

开源卫士试用地址：https://oss.qianxin.com/

代码卫士试用地址：https://sast.qianxin.com/

---

**推荐阅读**

[OpenSSL 漏洞可导致密钥恢复、代码执行、DoS 攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524150&idx=2&sn=340e39d88a6552181d0f4433ab94ef67&scene=21#wechat_redirect)

[OpenSSL 高危漏洞可用于中间人攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522210&idx=2&sn=98a6271cd5d293a67b756477a83dfab3&scene=21#wechat_redirect)

[戴尔、惠普等设备被指使用过期的OpenSSL版本，易引发供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514771&idx=3&sn=c830e03f4b8b8fc4ad7c8ce0406d934a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hollowbyte-ddos-flaw-bloats-openssl-server-memory-with-11-byte-payload/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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