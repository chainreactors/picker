---
title: Python、npm和开源生态系统中的入口点可用于发动供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&chksm=ea94a22fdde32b396a0c379623e7d047d6762947c21f033e10a0d1e0f8567a584c4d74c12e27&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-16
fetch_date: 2025-10-06T18:53:58.919306
---

# Python、npm和开源生态系统中的入口点可用于发动供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNMOotmexZE7n1gxjlgG7slHGUAqWYcKwPkwo3Ipb9R4vSVhzlfazTdQ/0?wx_fmt=jpeg)

# Python、npm和开源生态系统中的入口点可用于发动供应链攻击

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNQCyjgiaGSFotcrEucz7ibW6rIo7dkHM3nwmpbfxH2y2Qv9SleiayVmOJg/640?wx_fmt=gif&from=appmsg)

**网络安全研究员发现入口点可在多个程序生态系统，如 PyPI、npm、Ruby Gems、NuGet、Dart Pub 和 Rust Crates 中被滥用于发动软件供应链攻击。**

Checkmarx 公司的研究员 Yehuda Gelb 和 Elad Rapaport 在一份报告中提到，“攻击者可利用这些入口点在特定命令运行时执行恶意代码，从而为开源生态系统造成大规模风险。”

研究人员发现，此类入口点攻击可导致威胁行动者获得更加隐秘和持久的系统攻陷方法，绕过传统的安全防御措施。编程语言如 Python 中的入口点是指封装机制，可使开发人员将某种功能暴露为命令行封装器（console\_scripts）。或者它们也可加载增强包特性的插件。

研究人员提到，虽然入口点是改进模块化的一种强大方式，但该特性也可被滥用于将恶意代码分发给不知情的用户，如为多款工具和框架进行命令劫持和创建恶意插件。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNjI4H8uMsO9OPHUNGHQaU0HnwBzwQZxibnAUDdwIvr861iapoEdpD3Nzw/640?wx_fmt=png&from=appmsg)

**命令劫持**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNzvY7EayibWvwhQ2yZoHuKfSXmvL5YovcM8LghsL3VPQcQmEplQgIQpg/640?wx_fmt=gif&from=appmsg)

当假冒程序包使用模拟流行第三方工具和命令（如AWS和容器）的入口点，在开发人员安装程序包时，甚至是当它们作为 wheel (.whl) 文件进行分发时，收割敏感信息，就会发生命令劫持。一些使用广泛的第三方命令可成为命令劫持的潜在目标，如npm、pip、git、kubectl、terraform、gcloud、heroku 和 dotnet。当威胁行动者使用合法的系统命令名称（如 touch、curl、cd、ls和mkdir）作为入口点来劫持执行流时，也可能进行命令劫持。

研究人员认为，“这种方式的成功主要取决于PATH顺序。如果包含恶意入口点的目录出现的时间早于系统目录时，恶意命令而非系统命令就会被执行。这种情况更可能发生在本地包目录被优化的开发环境中。”

不止如此。研究人员还发现可通过更加隐秘的技术即“命令封装”来改进命令劫持的效果，涉及创建入口点作为原始命令的封装器而非完全取而代之。这种方法之所以奏效，是因为它在调用原始、合法的命令并返回执行结果的同时，悄悄执行恶意代码，从而导致其不易被发现。研究人员解释称，“由于合法命令仍在运行而其输出和行为得到保存，因此不会立即出现妥协指标，使得通过正常使用极其难以检测到这种攻击。这种隐秘方式可使攻击者维持长期访问权限，并在不引起怀疑的情况下提取敏感信息。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNjI4H8uMsO9OPHUNGHQaU0HnwBzwQZxibnAUDdwIvr861iapoEdpD3Nzw/640?wx_fmt=png&from=appmsg)

**创建恶意插件**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNzvY7EayibWvwhQ2yZoHuKfSXmvL5YovcM8LghsL3VPQcQmEplQgIQpg/640?wx_fmt=gif&from=appmsg)

另外一种入口点攻击技术是指为能够获得对代码库广泛访问权限的开发者工具，创建恶意插件和扩展，从而使恶意人员有机会更改程序行为或者篡改测试流程，使代码看似按预期运行。

研究人员表示，“开发针对入口点利用的全面安全措施十分重要。通过了解和解决这些风险，我们能够创建更安全的Python 封装环境，保护个体开发人员和企业系统免受复杂供应链攻击。”

前不久，Sonatype 公司发布软件供应链现状报告并指出，自2023年11月起，已经在Java、JavaScript、Python 和 .NET 开源生态系统中发现超过512847个恶意包，同比增长156%。该公司提到，“传统的安全工具通常无法检测到这类新型攻击，使开发人员和自动化构建环境非常易受攻击，从而导致新一轮的下一代供应链攻击活动，它们直接绕过已有的防御措施攻击开发人员。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&chksm=ea94a18edde328988758d00a0c6c91218ef60546d92e98647d91c44e557d14c15596b8aff06c&scene=21#wechat_redirect)

[ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&chksm=ea94a259dde32b4f211fb59ae290ca1daab65c90d84350afe2de36239f2907afe0466021e549&scene=21#wechat_redirect)

[“复活劫持”供应链攻击威胁2.2万个PyPI包的安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=2&sn=18f9b633ae22eab04a32ea14664dde07&chksm=ea94a0c1dde329d773200df4470e2f6dfba305c7c3c4e70dee8ce91ebb53fbf1ea18dd3ea9c1&scene=21#wechat_redirect)

[MLOps 平台存在20多个供应链漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520605&idx=2&sn=6bd044882cfd8e5f96140c71e26498f4&chksm=ea94a037dde32921016d3ccc578f09450825636f654da7d674940fccba2dbb77ba63a80dd774&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/supply-chain-attacks-exploit-entry.html

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