---
title: 工业物联网设备中广为使用的调制解调器易受SMS攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519462&idx=2&sn=e5758c5c284c0a618d66e0c8ef1d4294&chksm=ea94bd8cdde3349af00d2f59bac7cbdd3ef0ff785d58ac07e13b55a5e002ce8d68cb6df350ef&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-12
fetch_date: 2025-10-06T17:16:37.337874
---

# 工业物联网设备中广为使用的调制解调器易受SMS攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSkp2YNGDLVoDIYxbia6Ld7oVMCaAJLvs6fjxPrAdS6ltEqBiaTFQTgwplq06YbIY38aSwE72WeFwng/0?wx_fmt=jpeg)

# 工业物联网设备中广为使用的调制解调器易受SMS攻击

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Telit 公司的Cinterion蜂窝调制解调器中存在多个漏洞，可导致远程攻击者通过短信 (SMS) 执行任意代码。该调制解调器广泛应用于多种行业，包括工业、医疗和电信等。**

在这八个漏洞中，其中7个的编号为CVE-2023-47610至CVE-2023-47616，还有1个未被分配CVE编号。它们由卡巴斯基 ICS CERT团队的安全研究人员在去年11月披露。在发布之前，卡巴斯基已在2023年2月报送给厂商。

研究人员将在当地时间本周六在德国举行的 OffensiveCon 大会上提供低级别的技术详情，以及说明威胁行动者如何利用这些漏洞控制易受攻击的 Telit Cinterion 设备。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSkp2YNGDLVoDIYxbia6Ld7og887PU847jMZbNa332h2OjIlkJ0ehh4lBJYxCzvKSicAv1rnBicKOCHQ/640?wx_fmt=gif&from=appmsg)

**利用短信接管设备**

在这8个漏洞中，最严重的是CVE-2023-47610。它是一个堆溢出漏洞，影响该调制解调器的用户面板位置 (SUPL) 消息句柄。卡巴斯基联合 Telit 详细分析这些技术详情，并将其严重性评估为8.8分，但NIST认为该漏洞具有严重影响，将其严重性评分调高至9.8分。

攻击者可通过特殊构造的短信触发该漏洞，并在无需认证的情况下在该调制解调器上远程执行任意代码。研究人员在报告中提到，该短信消息接口出现在所有调制解调器上，如果该蜂窝运营商网络中的目标调制解调器的订阅号码是已知的，则可访问该接口。

研究人员解释称，运营商的限制有时可能会阻止发送二进制短信，但虚假基站可绕过这一限制。攻击者可利用该漏洞通过短信执行任意代码，获得对调制解调器操作系统的深层访问权限。

尽管研究人员发现的其它漏洞的严重性评分更少，但它们可被攻陷 MIDlets的完整性。卡巴斯基提到，攻击者可绕过数字化签名检查，以提升后的权限实现代码执行后果。这就导致不仅威胁数据机密性和完整性，还威胁更广泛网络的安全性和设备完整性。

尽管研究针对的是 Cinterion EHS5-E 系列的调制解调器，但由于该厂商的其它产品也具有类似软件和硬件架构，因此其它变体也受影响：

* Cinterion BGS5
* Cinterion EHS5/6/7
* Cinterion PDS5/6/8
* Cinterion ELS61/81
* Cinterion PLS62

卡巴斯基表示，Telit 公司修复了其中一些漏洞，不过另外一些仍未修复。卡巴斯基 ICS CERT 的负责人 Evgeny Goncharov 指出，“我们找到的这些漏洞以及这些设备在多个行业的广泛部署说明了造成全球破坏的可能性。”Goncharov 提到，由于这些调制解调器内嵌在其它解决方案中，因此很难判断哪些产品受到影响。

卡巴斯基提到了缓解这些威胁的建议，其中多数均可通过与电信运营商的协作解决。其中一种策略是禁用发送给受影响设备的短信并使用配置安全的私密APN。

卡巴斯基还建议执行应用签名验证，阻止在调制解调器上安装不可信的 MIDIets，并采取措施阻止对设备的越权物理访问。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Realtek 漏洞遭利用：物联网设备受攻击次数超过1.34亿次](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515416&idx=2&sn=5263eb9cbd95cbf0e261aa63fd55a818&chksm=ea948c72dde3056482a3020c8ed8c959bceaecf0fcd513c8b791ecd7b79fbb70f277454f34bf&scene=21#wechat_redirect)

[扩展物联网 (XIoT) 漏洞激增，安全压力倍增](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513786&idx=3&sn=07ef04262f4e5c1f68019bd0eafffe20&chksm=ea9487d0dde30ec6ddb7fffd17fcf18c63f5f07f66769788f6748460497129ab130565fc545c&scene=21#wechat_redirect)

[三年蜜罐实验：黑客想从物联网设备中得到什么？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509831&idx=2&sn=85daf5b71f3529e32628b548b7069d5a&chksm=ea94962ddde31f3b92164d0349c9055c886dc0b41d8f6a9e6eb9ac73639a07b53b0dfa687a1b&scene=21#wechat_redirect)

[联发科固件现窃听漏洞，影响全球约三分之一的手机和物联网设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509419&idx=2&sn=2f9d2960d52a795a5895a28287b29b59&chksm=ea9494c1dde31dd746b7adc04dff58cb689164d449cf30114b367a650a1bdd1c05242ba45a83&scene=21#wechat_redirect)

[BotenaGo 僵尸网络利用33个exploit 攻击数百万物联网设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509127&idx=3&sn=e69a137542da467a447ec6f2f3dd3115&chksm=ea9495eddde31cfb7c33520c05758dbc4263e624569160bb2c9a64a812994d3a6271ec3e0871&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/widely-used-modems-in-industrial-iot-devices-open-to-sms-attack/

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