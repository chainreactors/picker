---
title: 微软五月补丁星期二值得关注的3个0day及其它
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519497&idx=2&sn=1e1dfda946c84c3456230b9252dc53b1&chksm=ea94bc63dde335758128401d8248286936aecf6b12e9914935af867fdbb2ff0e4494f3b4d849&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-16
fetch_date: 2025-10-06T17:16:18.787849
---

# 微软五月补丁星期二值得关注的3个0day及其它

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTJkFibQ9lloQH3dLpWCft87oib6FolSdfrFtnRzxaM4XfAqUjeQv2WAibGEzITqReOxCsnv88PGWNQw/0?wx_fmt=jpeg)

# 微软五月补丁星期二值得关注的3个0day及其它

综合编译

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**五月补丁星期二，微软共计修复59个CVE漏洞，加上第三方CVE漏洞，则五月共修复63个漏洞。和四月补丁日一致，微软仍未修复Pwn2Own 大赛上披露的多个漏洞。在所修复的漏洞中，只有1个被评级为“严重”等级，57个是“重要”级别，1个是“中危”级别。两个CVE漏洞被标记为已遭活跃利用，另外一个为公开已知。微软并未提供关于攻击规模的任何信息，但CWM Core 漏洞似乎不止是针对性攻击。这些漏洞是：**

* **17个提权漏洞**
* **2个安全特性绕过漏洞**
* **27个远程代码执行漏洞**
* **7个信息泄露漏洞**
* **3个拒绝服务漏洞**
* **4个欺骗漏洞**

**3个0day漏洞**

本月补丁日共修复了2个已遭活跃利用漏洞和1个已公开披露漏洞。微软认为在没有官方修复方案的情况下被公开披露或活跃利用的漏洞即是0day漏洞。

**CVE-2024-30040**是 Windows MSHTML 平台安全特性绕过漏洞。该漏洞是对OLE缓解措施的绕过。微软提到，“攻击者必须说服用户将恶意文件加载到易受攻击的系统，而这通常是通过邮件或即时消息诱骗实现，之后说服用户操纵特殊构造的文件，但不一定需要点击或打开恶意文件。成功利用该漏洞的未认证攻击者说服用户打开恶意文档，获得代码执行权限，在用户上下文中执行任意代码。”

目前尚不清楚该漏洞如何遭滥用以及发现者的身份。

**CVE-2024-30051**是位于 Windows DWM Core 库中的提权漏洞。微软解释称，“成功利用该漏洞的攻击者可获取系统权限。”卡巴斯基表示，最近的 Qakbot 恶意软件钓鱼攻击利用恶意文档来利用该漏洞并获得 Windows 设备上的系统权限。该漏洞由四家公司的多名研究人员发现，说明攻击范围广泛以及漏洞已遭公开。不要等到测试之后才部署更新，因为发布补丁后即可被逆向，那么利用的可能性也在增加。

微软还提到，位于Visual Studio 中的一个拒绝服务漏洞 **CVE-2024-30046** 也遭公开披露。

**其它值得关注的漏洞**

**CVE-2024-30043**是位于 SharePoint Server 中的信息泄露漏洞。认证攻击者可以 SharePoint Farm 服务账户用户权限读取本地文件，利用该漏洞。攻击者也可发动基于 HTTP 的SSRF 攻击，而更重要的是他们可以 SharePoint Farm 服务账号发动 NLTM 中继攻击。这类漏洞说明我们不应当忽视或调低信息披露漏洞的优先级。

**CVE-2024-30033**是 Windows Search Service 提权漏洞。攻击者可创建伪随机系统链接，重定向删除调用，以系统权限删除不同的文件或文件夹。当服务重启时，删除发生。低权限用户无法直接重启服务。然而，组合利用其它漏洞，可使低权限用户终止任何PID的进程。失败后，该服务将自动重启，从而成功触发该漏洞。

**CVE-2024-30050**是 Windows MotW 安全特性绕过漏洞。该漏洞虽然是中危级别，但最近受到勒索团伙的青睐。勒索团伙利用 MotW 绕过躲避 Office 中的 SmartScreen 或 Protected View。虽然并未有证据表明该漏洞已遭利用，但该技术的高频度使用使其脱颖而出。这类漏洞说明为何我们不应当忽视或调低中危漏洞的优先级。

另外，Win32k 提权漏洞CVE-2024-30028由奇安信代码安全实验室研究员发现。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[微软4月补丁星期二值得关注的漏洞：4个0day及更多](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519261&idx=1&sn=1f669e17acccbb5f3a974c466686d164&chksm=ea94bd77dde334619c916fa753497a102ad012bb069cba0cc174d147abf2488f2e649f7953f7&scene=21#wechat_redirect)

[微软2月补丁星期二值得关注的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518852&idx=1&sn=118503a8f9ad674c456c7a1beb026af7&chksm=ea94bbeedde332f84c2d0ebf024af1f8cb2ab422a17c266b9120bc7bbb81c05e8a27b9fc035b&scene=21#wechat_redirect)

[微软补丁星期二值得关注的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518639&idx=1&sn=5eb41017915be58b56c7eef48e7dc4de&chksm=ea94b8c5dde331d3020ca525a644211fa78e7fed0b6f4329c4ed79f060f65c97659843449eae&scene=21#wechat_redirect)

[微软12月补丁星期二值得关注的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518349&idx=1&sn=7d0a830340114bfe063e58557ea01613&chksm=ea94b9e7dde330f1808becf6b96f023942a253bc69753c951113741277557c3cc163d081b25d&scene=21#wechat_redirect)

[微软11月补丁星期二需要关注的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518139&idx=1&sn=941a9da7093fb53ada0f874db9d3ef39&chksm=ea94b6d1dde33fc740734b8dc6fbbcd0d0ea7446e8a8bfa3c8bdb1423e2e2c01536e8adf2960&scene=21#wechat_redirect)

**原文链接**

https://www.zerodayinitiative.com/blog/2024/5/14/the-may-2024-security-update-review

https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2024-patch-tuesday-fixes-3-zero-days-61-flaws/

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