---
title: Mozilla 修复Firefox 浏览器的多个高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515956&idx=2&sn=7870f9607adf1541eef5be5402a82ab4&chksm=ea948e5edde307489a6b2a77b80ba248729a3d0dbfd20a6b65ee00d181f4b422bc09fa95eb1c&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-18
fetch_date: 2025-10-04T09:58:08.578656
---

# Mozilla 修复Firefox 浏览器的多个高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRcRU8IrlP0zb5vLhqzT4Iwibj4u1vWqnkIWpqiaeFtK0snyL6TMItRDNibreVO3zhZbFQy74R60t2Fw/0?wx_fmt=jpeg)

# Mozilla 修复Firefox 浏览器的多个高危漏洞

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周，Mozilla发布Firefox 111，修复了13个漏洞，其中一些是严重级别。**

在这13个CVE漏洞中，7个为“高危”级别，3个仅影响安卓版本的Firefox浏览器，可导致黑客隐藏全屏通知，从而导致用户混淆或欺骗攻击，并在无需提示的情况下打开第三方应用。其它高危漏洞可导致任意代码执行和信息泄露后果。

Sophos 公司分析了这些补丁并着重强调了两个漏洞CVE-2023-28161和CVE-2023-28163。

**CVE-2023-28161**：本地文件的一次性权限被扩展到在同样标签下加载的其它本地文件中。如果用户打开本地文件（如下载的HTML内容）想要访问网络摄像头，则用户之后打开的任何其它本地文件都会继承该访问权限而无需询问。Mozilla提到，如果用户通过下载目录中的项目集合查看则会导致问题出现：用户所看到的权限提醒将取决于打开文件的次序。

**CVE-2023-28163****：**Windows“另存为”对话解析了环境变量，这是对清理输入的重要提醒。在Windows命令中，某些字符序列被专门处理如 %USERNAME% （被转换为当前已登录用户的名称）或 %PUBLIC%（表明为共享目录，通常位于C:\Users中）。恶意网站将借此诱骗用户查看并批准下载看似无害但实际上落到预期之外目录中的文件名称。

位于加拿大和美国的网络安全机构已将补丁告知用户，督促用户阅读安全公告并应用必要补丁。

虽然Firefox漏洞不像Chrome漏洞那样易遭攻击，但用户不应忽略潜在风险。在过去的十年中，CISA的已知利用漏洞列表中收录了10个Firefox漏洞。另外，Mozilla在本周还宣布用户将直接可在Firefox中使用Firefox Relay邮件和电话号码掩藏工具。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Firefox 97.0.2 修复两个已遭利用的0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510779&idx=2&sn=ebffc30f51572f1abd513f92b810858b&chksm=ea949b91dde31287dee367059f7db5e2dd338e600e25a7139b08463e0b1acc74d939bf9baf0c&scene=21#wechat_redirect)

[VEGA Stealer恶意软件窃取 Chrome 和 Firefox 浏览器信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487122&idx=5&sn=e6e958bc7546ecc7588b1f90404ed650&chksm=ea973ff8dde0b6eebfd177cdfa05e7bf06c403707f371021d8cc026a3dd3546c94753a43b967&scene=21#wechat_redirect)

[Mozilla 修复跨平台加密库 NSS 中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509515&idx=1&sn=de084c0a573b1575799897a4afda90d2&chksm=ea949761dde31e7713bd234eed45b4eccc02e28f47c9bdfde9a3146db61d58840353b6ae435f&scene=21#wechat_redirect)

[Mozilla 扩展漏洞奖励计划，涵盖利用缓解技术绕过](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494735&idx=2&sn=90cb2d9077304026ffa5f1cca694f349&chksm=ea94dd25dde3543347ed2403d269e6ae610ba9e51e7df2566ef1f3be01394f72e61d40da0fe5&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/mozilla-patches-high-severity-vulnerabilities-with-release-of-firefox-111/

题图：Pexels License

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