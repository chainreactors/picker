---
title: Citrix悄悄修复相似度极高但严重性不及CitrixBleed的高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=1&sn=3bb85759ff76414bd555bb55aa1b3c16&chksm=ea94bdd1dde334c73add716fd4c17f5d7be8d21d23464d3e187d43446f34d83e52d9482ed5cd&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-08
fetch_date: 2025-10-06T17:16:48.677323
---

# Citrix悄悄修复相似度极高但严重性不及CitrixBleed的高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQABdhUfeeJmcJwiaIU7Bka0QCpl7sfgNNgFPQibicIodICpwXWJAXlSmvGBUoN80rBO4TsTJiagO1Faw/0?wx_fmt=jpeg)

# Citrix悄悄修复相似度极高但严重性不及CitrixBleed的高危漏洞

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Citrix 公司悄悄修复了位于 ADC 和 Gateway 设备中的一个漏洞，它可导致远程未认证攻击者从受影响系统的内存中获得潜在的敏感信息。**

该漏洞与 CitrixBleed (CVE-2024-4966) 极其相似但严重性不及。CitrixBleed 同样位于ADC和Gateway 中，是Citrix 去年披露的一个 0day。本文所述新漏洞由 Bishop Fox 公司的研究人员发现并在1月份将其报送给 Citrix 公司。

**相似度极高但严重性不及**

攻击者大规模利用 CitrixBleed 漏洞部署勒索软件、窃取信息以及实现其它恶意目的。CISA 等机构督促受影响组织机构快速将系统更新至已修复的 NetScaler 版本，并援引多份针对该漏洞的大量报告。波音和 Comcast Xfinity 就是遭针对的多个大型组织机构。

相反，Bishop Fox 公司在1月份发现的漏洞严重程度较低，因为攻击者从易受攻击系统中检索高价值信息的可能性更低。即便如此，位于 NetScaler 版本13.1-50.23中的这个漏洞仍然可导致攻击者抓取敏感信息，包括受影响设备的进程内存中的 HTTP 请求主体。

研究人员指出，Citrix 公司在2月1日证实该漏洞存在，但后者并未分配CVE编号，原因是该公司已在漏洞披露前就在 NetScaler 13.1-51.15中将其修复。目前尚不清楚 Citrix 是否已经私下将漏洞披露给客户，或者是否将所提交的问题视为漏洞。研究人员表示并未直至目前发现对该漏洞的公开披露信息。

Citrix 并未回应上述问题，也并未回应该公司是否在13.1-51.15版本中修复之前披露了该漏洞。

**界外内存问题**

Bishop Fox 公司的研究人员在本周发布的博客文章中，将该漏洞视作未经验证的界外内存问题，可导致攻击者访问程序预期边界之外的内存位置。研究人员表示他们能够利用该漏洞抓取敏感信息，包括从受影响设备的内存中抓取HTTP请求主体。博客文章指出，“它可导致攻击者获取由登录到 NetScaler ADC 和 Gateway 设备的用户提交的凭据，或者获取设备所使用的加密材料。”

和 CitrixBleed 一样，该漏洞影响用于远程访问且用作认证、授权和审计 (AAA) 服务器的NetScaler 组件。具体而言，研究人员发现 Gateway 和 AAA 虚拟服务器以不安全的方式处理 HTTP 主机请求表头，而它就是 CitrixBleed 的底层问题所在。研究人员通过 PoC 展示了攻击者如何利用该漏洞提取潜在有用信息。

Bishop Fox 公司提到，“Bishop Fox 员工分析了易受攻击的 Citrix 部署，发现在实例中，被披露的内存中包含来自HTTP请求的数据，有时候还包括POST请求主体。”Bishop Fox 建议运行受影响 NetScaler 版本的组织机构升级到13.1-51.15或更高版本。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Citrix 提醒注意已遭利用的两个 NetScaler 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518689&idx=1&sn=0c28377e9cd188322fb8de2c9b984d4f&chksm=ea94b88bdde3319d66fb2901eac70e83e8071ee933f5b8bdb067917e92e94c9d23efc23f4ea8&scene=21#wechat_redirect)

[Citrix NetScaler 严重漏洞可泄露“敏感”数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517841&idx=2&sn=de64058a934247781132d8fdd5886240&chksm=ea94b7fbdde33eed8920dc403119072a08ff3f018fc6122497a8acfadfbdcf1fca8ab3aa986b&scene=21#wechat_redirect)

[Citrix 修复 Ubuntu 版本安全访问客户端中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517034&idx=4&sn=6e2b7be2533c1e454539a3b4905483c7&chksm=ea94b200dde33b16f46f5c52b43bc116d9a9ed99bf381bbe9dbd8d1b3902ca57cb785c81a283&scene=21#wechat_redirect)

[Citrix修复位于Gateway 和 ADC 中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514449&idx=1&sn=922716384658e8c52f01a153b1ac8251&chksm=ea94883bdde3012d2ef7c94a1e49690e115082526d0b6bbe2573cce3c6e36bac47b0042b499f&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/cyber-risk/citrix-addresses-high-severity-flaw-in-netscaler-adc-and-gateway

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