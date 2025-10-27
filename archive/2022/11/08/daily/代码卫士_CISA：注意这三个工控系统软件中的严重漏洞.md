---
title: CISA：注意这三个工控系统软件中的严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=3&sn=dd3d82b3a03b5b06090e5bc38014da44&chksm=ea948844dde301521b0cb907cb7dc3aadabd0e9a46e67d5b3855a850f580c0124798fa2504ec&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-08
fetch_date: 2025-10-03T21:56:54.823018
---

# CISA：注意这三个工控系统软件中的严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRib1W60OwVsAUicpkzzfC9EItte5As4zz0V4mTq3SVoqEylJr1EPc1XhxD01vIBCQETQI7XTaGoKZg/0?wx_fmt=jpeg)

# CISA：注意这三个工控系统软件中的严重漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRib1W60OwVsAUicpkzzfC9EIYfoIBPnb1PsdkP6hlC1bppKjfsEWwb9vN0EyNGZaBWEJ5MCC2ykIwg/640?wx_fmt=gif)

美国网络安全和基础设施安全局 (CISA) 发布三分工控系统安全公告，提到ETIC 电信、诺基亚和Delta Industrial Automation中存在多个漏洞。

其中最引人注目的是ETIC电信公司的远程访问服务器 (RAS) 受三个漏洞影响，“可导致攻击者获取敏感信息，攻陷易受攻击设备和其它联网机器”。这些漏洞是：

* CVE-2022-3703（CVSS评分9.0）：该严重漏洞因RAS 网络门户无法验证固件的真实性引发，使恶意包可能被攻击者插入，从而获得后门访问权限。
* CVE-2022-41607（CVSS 评分8.6）：该严重漏洞是位于RAS API 中的一个目录遍历漏洞。
* CVE-2022-40981（CVSS评分8.3）：该漏洞可被用于读取任意文件和上传恶意文件，从而攻陷设备。

以色列工业网络安全公司 OTORIO 发现并报告了这些漏洞。所有ETIC 电信RAS 4.5.0和之前版本均受影响。该漏洞已在版本4.7.3中修复。

第二份安全公告关于诺基亚ASIK AirScale 5G Common System Module 中的三个漏洞（CVE-2022-2482、CVE-2022-2483和CVE-2022-2484），可导致任意代码执行和安全引导程序功能不当。所有漏洞的CVSS评分均为8.4。CISA提到，“这些漏洞如遭利用，可导致恶意内核执行、任意恶意程序运行或者遭修改的诺基亚程序运行”。据报道，诺基亚已发布缓解措施。这些漏洞影响 ASIK 版本474021A.101和ASIK47402A.102。CISA建议用户直接联系厂商获取更多信息。

第三份报告和路径遍历漏洞CVE-2022-2969有关，CVSS评分6.9，影响 Delta Industrial Automation 公司的 DIALink 产品，可被用于在目标设备上植入恶意代码。该漏洞已在 1.5.0.0 Beta 4中修复。CISA表示可直接通过厂商获取或者通过Delta现场应用工程 (FAEs)获取。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA：注意影响Advantech 和日立工业设备的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514269&idx=3&sn=42277be117ca4047c20dedbf1712beee&chksm=ea9489f7dde300e1a90950387af6f1655ca62e307fbb6644d0534ad880c3e4b3c475bed3e5fa&scene=21#wechat_redirect)

[CISA要求联邦机构定期追踪网络资产和漏洞情况](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514137&idx=2&sn=3d803ae8e1029afd224613643defdb11&chksm=ea948973dde3006536a10f203f81bedae2b006911e312c4e70bd28d1aded4a00ee678ac3c714&scene=21#wechat_redirect)

[研究员披露影响10家OT厂商工控设备的56个漏洞OT:ICEFALL](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512470&idx=1&sn=9ff886e36269deab3af95b513c60754e&chksm=ea9480fcdde309ea294148ae92264463a822f5a65d3243f576e255cf7f0be60c1126a2ae9b95&scene=21#wechat_redirect)

[工控2月补丁星期二：西门子、施耐德电气修复近50个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510474&idx=2&sn=87818e92c87a947611eea0423026cf83&chksm=ea9498a0dde311b68937435a613ba0af82df0b65e38a1b9c0b21a08820f9abc23d5820d955c0&scene=21#wechat_redirect)

[很多工控产品都在用的 CODESYS 软件中被曝10个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505442&idx=1&sn=645ef4a67cc6372f43f130a8137ab64b&chksm=ea94e748dde36e5e6a22fd7095c3617ac52b1376100a574a8020f04cef31b81c971ae57ad756&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2022/11/cisa-warns-of-critical-vulnerabilities.html

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