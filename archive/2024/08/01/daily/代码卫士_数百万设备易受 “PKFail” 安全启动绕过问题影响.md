---
title: 数百万设备易受 “PKFail” 安全启动绕过问题影响
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520274&idx=1&sn=5cfd7e9114bc219b747a5f41013cd669&chksm=ea94a178dde3286ef8da98f37ad7eb2f0155810f6a1cd9d0e5d11ad496e274b9a09751ab2267&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-01
fetch_date: 2025-10-06T18:04:52.164818
---

# 数百万设备易受 “PKFail” 安全启动绕过问题影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRsfqzszffxYMRuMkibfxnics0iaibjfiblHZoOOXmFJzKaQuRBcBgiboJlZYHIUgH1DeMJYEyK59ic26icUg/0?wx_fmt=jpeg)

# 数百万设备易受 “PKFail” 安全启动绕过问题影响

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**攻击者可绕过多家厂商提供的数百万台基于 Intel 和 ARM 微处理器的计算机系统，因为它们均使用设备启动进程中曾遭泄露的密钥。**

American Megatrends International (AMI) 的该平台密钥 (PK) 是安全启动PC启动链的信任根，验证设备固件和启动软件的真实性和完整性。遗憾的是，固件安全厂商 Binarly 的安全研究员发现该密钥已被泄露在2018年发生的一起数据泄露事件中。Binarly 公司提到，“该密钥可能包含在 AMI 的引用实现中，可能会被该供应链中的下游实体的另外一个安全生成密钥所取代。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsfqzszffxYMRuMkibfxnicsP6mUMKqZdia4z6us8WlyacOKYibwX8EfhKCGIZicoL8DFyxKcJBakpysA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsfqzszffxYMRuMkibfxnicsibzrnS43e3MI5VxwmGDvics1elRlOcCJsVOou0fCLibDljUbia4ib5xQ3oA/640?wx_fmt=png&from=appmsg)

**PKFail 安全启动问题**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsfqzszffxYMRuMkibfxnicsibzrnS43e3MI5VxwmGDvics1elRlOcCJsVOou0fCLibDljUbia4ib5xQ3oA/640?wx_fmt=png&from=appmsg)

原始设备制造商 (OEM) 使用它为Intel 和基于 ARM 的设备厂商生成的固件的AMI测试密钥。结果，全球可能有数百万太消费者和企业设备都在安全启动流程中使用同样的受陷 AMI PK。受感染的厂商包括联想、华硕和 SuperMicro 等。

Binarly 公司的首席执行官兼创始人 Alex Matrosov 将该问题称为 “PKFail”。他提到，“对PK非公开部分具有访问权限的攻击者可操纵 Key Exchange Key 数据库、Signature Database 和 Forbidden Signature Database，轻松绕过安全启动。”攻击者可利用该问题，部署如去年 BlackLotus  一样的 UEFI 后门。

Matrosov 表示，“修复方案很简单：替换受陷密钥，设备厂商需要进行固件更新。”他提到，多个厂商已经这样做了。然而，在很多情况下，和数据中心服务器一样，如对于用于关键应用中的系统而言，固件更新的部署需要一些时间。

他提到，“如果设备受影响，则该问题的利用也很简单。”他提到，Binarly 公司已为 PKFail 漏洞开发出 PoC。他建议组织机构在部署固件升级前，断开设备与 AMI PK 与关键网络的连接。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsfqzszffxYMRuMkibfxnicsP6mUMKqZdia4z6us8WlyacOKYibwX8EfhKCGIZicoL8DFyxKcJBakpysA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsfqzszffxYMRuMkibfxnicsibzrnS43e3MI5VxwmGDvics1elRlOcCJsVOou0fCLibDljUbia4ib5xQ3oA/640?wx_fmt=png&from=appmsg)

**万能钥匙和重大问题**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsfqzszffxYMRuMkibfxnicsibzrnS43e3MI5VxwmGDvics1elRlOcCJsVOou0fCLibDljUbia4ib5xQ3oA/640?wx_fmt=png&from=appmsg)

荷兰 Hadrian 公司的首席执行官 Rogier Fischer 表示，PKFail 问题很重要，因为黑客可轻松利用该漏洞绕过安全启动，就像拥有能打开很多房子的万能钥匙。他提到，“由于同样的钥匙可用于不同设备，因此一次事件泄露可影响很多系统，导致该问题产生广泛影响。”

Matrosov 表示，PKFail 是唯一一个最近已存在十多年的问题，而原始设备制造商和设备厂商在生产固件和设备中使用非生产和测试密钥形成了趋势。该AMI PK 明显完全不受信任，但它最终仍然出现在了很多厂商中。

Binarly 公司在报告中提到了发生在2016年的一起事件，所设计的漏洞是CVE-2016-5247.安全研究员发现多台相关设备共享同样的 AMI 测试PK。当时，美国国家漏洞库将其描述为可允许“本地用户或物理接近的攻击者通过利用一个 AMI 测试密钥的方式，绕过 Secure Boot 防护机制”。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[技嘉固件组件可被滥用为后门，影响700万台设备，易触发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516632&idx=1&sn=00206835fa830496a1dd6fcc2e973d43&chksm=ea94b0b2dde339a4a3c374021bc551a9a3a0437410aaa7f195784d4034dfaeed4cd6b7d5dafb&scene=21#wechat_redirect)

[命令注入漏洞可导致思科设备遭接管，引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515439&idx=1&sn=bb8d8abcbaaf7e2be431ab9cd0712617&chksm=ea948c45dde30553179da977f93800b8c57d85c6185257361358931ab913191be82c3079d54c&scene=21#wechat_redirect)

[严重的“Access:7”供应链漏洞影响100多家厂商150多款联网设备等产品](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510841&idx=1&sn=da6b1e1cc6a3680ad2a372d33cd90005&chksm=ea949a53dde31345e39247fa7def2e6013c0ae321c37e584cb27b58ac9c5bdbab3d5b5f201c7&scene=21#wechat_redirect)

[Realtek WiFi SDK 被曝多个漏洞，影响供应链上至少65家厂商近百万台IoT设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507215&idx=1&sn=7c95fd8598c4f33e573e12e6f92c9808&chksm=ea94ec65dde36573649c4936289838a96ef4d81fe5a5b17b6c5f3603897fa056588850c946ae&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/endpoint-security/millions-of-devices-vulnerable-to-pkfail-secure-boot-bypass-issue

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