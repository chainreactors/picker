---
title: 刚刚，Citrix 修复两个易遭利用的0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521471&idx=1&sn=c305cea275e183b3f69b86df88828903&chksm=ea94a5d5dde32cc3de89c8d966920d171d8349630c6c42a4ad744a7ce734c022a357c43519d2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-14
fetch_date: 2025-10-06T19:19:19.753650
---

# 刚刚，Citrix 修复两个易遭利用的0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSbjo2AS8ibZD7esuPKiaiaV9YRPkwx8o059bH2d5TMX4C9jE4RVPxlqLcH8dsNMxsSh7ftl6EQYPIdg/0?wx_fmt=jpeg)

# 刚刚，Citrix 修复两个易遭利用的0day漏洞

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**在漏洞被公开披露后，Citrix 公司终于非常迅速地发布补丁，修复了位于 Citrix Virtual Apps and Desktop 技术中的两个漏洞（CVE-2024-8068和CVE-2024-8069），它们可导致远程攻击者在易受攻击系统上提权或执行代码。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSbjo2AS8ibZD7esuPKiaiaV9YrU3Y3gCc29qqmUt1mNHqFhjzDyxZjmzh7Is36x2L5Glb5riachJ6X7w/640?wx_fmt=gif&from=appmsg)

Citrix 将这两个RCE漏洞描述为仅有之前认证过的攻击者才能滥用的漏洞。然而，在7月份发现并报送漏洞的watchTowr公司的研究人员提到，未认证攻击者即可轻松利用这些漏洞。就在Citrix 和 watchtower 披露这些漏洞的数小时后，ShadowServer Foundation 就表示已发现基于所公开 PoC 的利用尝试。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSbjo2AS8ibZD7esuPKiaiaV9Yjb9tuGkc4U8cib96LKoH0WdeGgPjqRJHI1wvf9CnicuA05dCuXnNn8hg/640?wx_fmt=gif&from=appmsg)

**Citrix 淡化漏洞的严重性？**

这两个漏洞影响瘦客户端技术的 Session Recording Manager 组件。该组件可使管理员捕获、存储和管理用户会话录像。这两个漏洞源自 Session Recording Manager 反序列化或解压缩数据（这些数据已被转化为易于存储和传输的格式）方式中存在的一个弱点。

Citrix 最开始表示无法复现漏洞，但在收到研究人员提供的 PoC 利用后证实了问题的存在。Citrix 公司在11月12日发布安全公告提到，CVE-2024-8068是一个提权漏洞，可导致位于和会话录像服务器同样 Windows 活动目录域中的认证用户获得对 NetworkService Account 的访问权限。CVE-2024-8069对于对易受攻击系统上拥有管理员级别账户访问权限的攻击者而言是“有限的”RCE。Cloud Software Group 强烈督促Citrix Session Recording 的受影响客户安装更新升级版本。

即便如此，Citrix 为这两个漏洞的评分仅为5.1，属于中危级别，而这也是 watchTowr 有争议的地方。watchTowr 公司的首席执行官 Benjamin Harris 提到，“Citrix 公司在淡化该漏洞的严重程度，将其视作中等优先级漏洞，但实际上是非常容易早利用的漏洞。”组合利用这两个漏洞可导致“非常典型的未认证RCE后果”。

他还提到，“Citrix 的Virtual Apps and Desktop 服务是旗舰解决方案，服务对象是对象是全球财富500强组织机构。自我们开始处理反序列化问题时，我们就很肯定我们的exp运行可靠。并不存在复杂的堆操纵或其它熵。”

很多组织机构都在使用 Citrix 公司的 Virtual Apps and Desktop 技术，使用户能够从任何地方使用任何设备，访问其应用程序和桌面环境。它使组织机构能够集中从一个位置部署、更新和保护所有用户应用，让维护更加高效、统一和提升成本效益。Citrix 公司提到的另外一个好处是将应用和数据放在中心化服务器要比放在单个端点设备更安全。该技术的 Session Recording 特性可使管理员监控异常行为并维护用户活动的详细记录，以用于未来的审计和调试工作。

随着越来越多的公司开始采用远程工作和混合工作模式，近年来对此类技术的需求越来越旺盛。研究公司 MarketsandMarkets 预估该市场的规模将从去年的15亿美元左右增加到2028年的17亿美元。更宽泛的桌面即服务 (DaaS) 市场本身有望在2030年达到近190亿美元，而在2021年，该市场规模仅为近40亿美元。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSbjo2AS8ibZD7esuPKiaiaV9Yjb9tuGkc4U8cib96LKoH0WdeGgPjqRJHI1wvf9CnicuA05dCuXnNn8hg/640?wx_fmt=gif&from=appmsg)

**对已知不安全技术的依赖**

这些漏洞是研究人员在审计 Citrix 的 Virtual Apps and Desktop 架构中的潜在安全问题时发现的这些漏洞。审计结果表明，Citrix 公司的应用使用了微软的MSMQ服务来接收记录的用户会话文件并将它们存储在单独的存储管理器组件中。另外，watchTowr 发现Citrix 在必要时利用微软技术 BinaryFormatter对存储管理器组件中的数据进行反序列化。微软已经督促组织机构停止使用BinaryFormatter 技术，因为其中的安全弱点已无法修复。

WatchTowr 发现的这些漏洞涉及组合利用 Citrix Virtual Apps and Desktop 技术的会话记录组件中的互联网可访问 MSMQ 实例以及与 BinaryFormatter 相关的配置不当权限。Harris 表示，“这并非 BinaryFormatter 本身中的漏洞，也并非MSMQ中的漏洞，而是因 Citrix 依赖于本身不安全的 BinaryFormatter 维持安全边界而造成的不幸结果。它是在设计阶段就出现的 bug，即 Citrix 在决定使用哪种清理库时就决定的。”

Harris 表示watchTowr 将该漏洞报送为一个问题，而Citrix 将它当作两个单独的问题处理。Harris 表示，“虽然无法否认 Citrix 使用含不可信数据的 BinaryFormatter 是一个事实漏洞，但我们没有足够的上下文来判断，通过HTTP 暴露MSMQ 队列是否真的是一个bug，是因疏于监控还是一些模糊业务需求带来的有计划的影响。”

Citrix 公司的产品因对企业应用和数据授予较高权限，因此常常是攻击者的目标。最近报送的很多漏洞均影响该公司的 NetScaler ADC 和 NetScaler Gateway 远程访问平台。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Citrix 督促 Mac 用户修复 Workspace App 中的提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519614&idx=1&sn=9e0519627dc928e416d3ba3de0a1941c&chksm=ea94bc14dde335021d4938ffb1183077024f5d791b881b81d21bd3861444796d43d393e33db9&scene=21#wechat_redirect)

[Citrix 提醒管理员手动缓解 PuTTY SSH 客户端漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519453&idx=1&sn=b108366a369534bc2bc55f5a5089d587&chksm=ea94bdb7dde334a1ed46fce3773a11cab5d7d420a9b40d13263be90a5ffc622be738b323c0ec&scene=21#wechat_redirect)

[Citrix悄悄修复相似度极高但严重性不及CitrixBleed的高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=1&sn=3bb85759ff76414bd555bb55aa1b3c16&chksm=ea94bdd1dde334c73add716fd4c17f5d7be8d21d23464d3e187d43446f34d83e52d9482ed5cd&scene=21#wechat_redirect)

[Citrix 提醒注意已遭利用的两个 NetScaler 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518689&idx=1&sn=0c28377e9cd188322fb8de2c9b984d4f&chksm=ea94b88bdde3319d66fb2901eac70e83e8071ee933f5b8bdb067917e92e94c9d23efc23f4ea8&scene=21#wechat_redirect)

[Citrix NetScaler 严重漏洞可泄露“敏感”数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517841&idx=2&sn=de64058a934247781132d8fdd5886240&chksm=ea94b7fbdde33eed8920dc403119072a08ff3f018fc6122497a8acfadfbdcf1fca8ab3aa986b&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/cloud-security/citrix-patches-zero-day-recording-manager-bugs

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