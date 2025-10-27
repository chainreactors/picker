---
title: Progress：尽快修复 WhatsUp Gold 中的多个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520960&idx=1&sn=919fb43b3860018ef3997b0e4159dee6&chksm=ea94a3aadde32abc1b1672f51c4f96ac9221aa568d099da519cf4bbabc756923465716a0ad6e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-30
fetch_date: 2025-10-06T18:25:15.527476
---

# Progress：尽快修复 WhatsUp Gold 中的多个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTpW93fIuQEo02Wmht3Ckx75A10CuZJra3yq3e60SALdKzq6uYlOKfjn1Prv6GuemEDFQ6gfrvNmw/0?wx_fmt=jpeg)

# Progress：尽快修复 WhatsUp Gold 中的多个严重漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Progress Software 公司提醒客户，尽快修复 WhatsUp Gold 网络监控工具中的多个严重和高危漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTpW93fIuQEo02Wmht3Ckx7GQ6ZsdRNIPMHFh85E1UZeCzK8v1KyIlmwYFa9iacvjz01WDiczMuYcXw/640?wx_fmt=png&from=appmsg)

然而，尽管 Progess 公司已发布 WhatsUp Gold 24.0.1，在上周五修复了这些问题并在上周二发布安全公告，但尚未发布任何漏洞详情。

该公司提醒客户称，“WhatsUp Gold 团队在24.0.1以下版本中发现了6个漏洞。我们提醒所有 WhatsUp Gold 客户尽快将环境升级至在9月20日周五发布的版本24.0.1。如果你运行的版本低于24.0.1且未更新，则环境依然是易受影响的。”

Progress 公司给出的唯一信息是这六个漏洞是由 Summoning 团队的 Sina Kheirkhan、趋势科技的Andy Niu 和 Tenable 公司的研究人员发现的，CVE 编号和CVSS基础分如下：

* CVE-2024-46905: CVSS 8.8/10（Sina Kheirkhah报送）
* CVE-2024-46906: CVSS 8.8/10（Sina Kheirkhah报送）
* CVE-2024-46907: CVSS 8.8/10（Sina Kheirkhah报送）
* CVE-2024-46908: CVSS 8.8/10（Sina Kheirkhah报送）
* CVE-2024-46909: CVSS 9.8/10（Andy Niu报送）
* CVE-2024-8785: CVSS 9.8/10（Tenable 报送）

用户如需更新至最新版本，则需要下载 WhatsUp Gold 24.0.1，在易受攻击的 WhatsUp Gold 服务器上运行并根据提示操作。Progress 公司并未就要求给出更多漏洞详情进行回应。

从8月30日开始，攻击者一直在利用 WhatsUp Gold SQL 注入漏洞CVE-2024-6670和CVE-2024-6671。研究员 Sina Kheirkhah 在5月22日通过ZDI 计划提交给 Progress 公司后，后者在8月16日将其修复。漏洞修复两周后，研究员发布的这两个漏洞的 PoC 利用代码，而趋势科技认为该利用代码已被用于绕认证并实现远程代码执行。

8月初，威胁监控组织 Shadowserver Foundation 也尝试利用在6月25日披露的 WhatsUp Gold 严重RCE漏洞CVE-2024-4885。Kheirkhah 也在两周后发布了该漏洞的完整细节。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Progress 紧急修复影响 LoadMaster 的超危RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520732&idx=1&sn=8fafa0f4d8f56d2a8361866cce3ac84c&chksm=ea94a0b6dde329a0b734a3f78a7d08346686d7c08491cae9150d82ce56df6a5d2aa9356b6d2b&scene=21#wechat_redirect)

[Progress 提醒注意Telerik Report Server中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=1&sn=d9e2734ebb4a13c747b20000c240d7bd&chksm=ea94be8edde33798e81c133dacfe538263083021026fe777545f067b211569e604c359b9c639&scene=21#wechat_redirect)

[速修复！Progress Telerik 中存在严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519654&idx=1&sn=22b4f342e957ddb68acf5d7dabc14f7b&chksm=ea94bcccdde335da0a488c11021c8d947834829e062cbd4a5917bc946b3037f54a151014c361&scene=21#wechat_redirect)

[速修复Progress Flowmon中的这个CVSS满分漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519358&idx=2&sn=398290f1e1cbf32a9f72ff26e3d708c4&chksm=ea94bd14dde334025bccac4bf83cd4b90113971ba22d26184385ccc5d530c62314ca6d06d349&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/progress-urges-admins-to-patch-critical-whatsup-gold-bugs-asap/

题图：Pixabay License

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