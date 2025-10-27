---
title: 微软修复已遭利用的 Power Pages 0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522309&idx=1&sn=edcb7974ccf436c421f7900223071912&chksm=ea94a96fdde32079df45122f0a57cbf5b416cd2fe68a478a8b0e3a1dd710bcbe0821712d0361&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-22
fetch_date: 2025-10-06T20:37:13.950388
---

# 微软修复已遭利用的 Power Pages 0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTabdpu1MW1FHTdCVdQcl6jgpZribSvGT7KkBFTgicnXSRYPpWfETIKjIkiaiapKTLj2zl8beeUIgqQVA/0?wx_fmt=jpeg)

# 微软修复已遭利用的 Power Pages 0day

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**微软发布安全通告称Power Pages 中存在一个高危提权漏洞CVE-2025-24989，在0day时已遭利用。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTabdpu1MW1FHTdCVdQcl6j6uSoQFzsMTTASUhLbbvUDqXDOPxrGDpvsgTfYoxzWowvqAspZCticaw/640?wx_fmt=gif&from=appmsg)

该漏洞是影响 Power Pages 的访问控制不当问题，可导致越权人员提升权限并绕过用户的注册控制。微软表示已在服务层面解决该风险并通知受影响客户，披露了如何检测潜在攻陷的指南。微软在安全通告中提到，“该漏洞已在服务中缓解，已通知所有受影响客户。该更新修复了注册控制绕过问题。受影响客户已获得如何查看和清理网站中潜在利用的指南。如您未收到该漏洞通知，则您并未受影响。”

微软Power Pages 是一个低代码的基于SaaS 的web开发平台，可使用户创建、托管并管理安全的面向外部的业务网站。它是微软 Power Platform的一部分，后者包括 Power BI、Power Apps和Power Automate等。

由于 Power Pages 是一款基于云的服务，因此利用可能是远程发生的。微软并未透露利用详情。除了该漏洞外，微软还修复了Bing中的一个远程代码执行漏洞 (CVE-2025-21355)，不过该漏洞并未遭利用。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTabdpu1MW1FHTdCVdQcl6jL30dxdsGlwM82GrPNujPKnaQqcxPrlhkN3JIib55TplSDicLoh9uib37Q/640?wx_fmt=gif&from=appmsg)

**需进行安全检查**

微软已向 Power Pages 服务应用修复方案，并以非公开的方式直接与受影响客户分享指南。不过用户仍可考虑一些通用的安全建议。

管理员应当查看活动日志中的可疑操作、用户注册或越权变更。由于CVE-2025-24989是一个提权漏洞，但也应审计用户清单，验证管理员和高权限用户。还应进一步查看权限、安全角色、许可和网页访问控制中的变化。应当立即删除恶意账户或者显示越权活动的账户，重置受影响凭据并在所有账户中执行多因素认证机制。

用户如未收到微软通知，则表明系统并未受影响。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[微软2月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522210&idx=1&sn=05cf8501f67197b21b3eb5ce8849477c&scene=21#wechat_redirect)

[微软扩展Copilot AI漏洞奖励计划范围，提高赏金](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522200&idx=1&sn=7bf07566564fbc663142355517974f16&scene=21#wechat_redirect)

[微软2025年1月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522078&idx=1&sn=fed0749158dda91f61f1f60a96b5230c&scene=21#wechat_redirect)

[微软：macOS 漏洞可导致黑客安装恶意内核驱动](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522060&idx=1&sn=562313e7f413152c3399933007b147f5&scene=21#wechat_redirect)

[未修复的活动目录缺陷可导致任何微软服务器崩溃](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521970&idx=1&sn=cf8414d224a047b09b82ccc71c0bfd45&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/microsoft-fixes-power-pages-zero-day-bug-exploited-in-attacks/

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