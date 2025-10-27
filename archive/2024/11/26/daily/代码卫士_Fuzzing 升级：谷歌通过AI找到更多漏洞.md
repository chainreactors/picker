---
title: Fuzzing 升级：谷歌通过AI找到更多漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521578&idx=1&sn=0f7082c24d8e05dca215004ae796d61e&chksm=ea94a440dde32d56ec3122aaba3a62cee4ca60aa29749436b95da39412ef8c8c80b43a0fc000&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-26
fetch_date: 2025-10-06T19:20:25.510102
---

# Fuzzing 升级：谷歌通过AI找到更多漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQTNyIq9lHg7ReSleicIApiah9ibibgWTpdAFwSdlibWBVgia4EvkBKdFLibfIjDvzmRxOOZeFSHEQOmqfjA/0?wx_fmt=jpeg)

# Fuzzing 升级：谷歌通过AI找到更多漏洞

Thomas Claburn

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**谷歌的 OSS-Fuzz 项目使用大语言模型 (LLMs) 助力找到代码仓库中的漏洞，目前已识别出26个漏洞，包括在使用广泛的 OpenSSL 库中的一个严重漏洞。**

该 OpenSSL 漏洞 (CVE-2024-9143) 在9月中旬报送，并在一个月之后修复。一些（并非所有）漏洞也已得到修复。谷歌认为其受AI驱动的fuzzing（模糊测试，将异常或随机数据注入软件中以捕获错误）工具找到了人类无法通过fuzzing找到的错误。

谷歌开源安全团队的研究员 Oliver Chang、Dongge Liu 和 Jonathan Metzman 在一份博客文章中提到，“就我们所知，这个漏洞可能已存在20年且以人类编写的现有fuzz目标而言是无法发现的。”如所言属实，那么安全研究真的应该纳入AI的使用，以免威胁人员已经这么做了，并找到人类无法找到的缺陷。谷歌还援引了另外一个案例，即位于 cJSON 项目中的一个 bug 据称也是由AI发现但被人类所编写的fuzzing测试错过的 bug。

因此，AI协助似乎对于安全专业人员而言价值巨大。谷歌本月早些时候宣布，另外一个基于LLM的捕获工具 Big Sleep 首次从真实软件中找到一个此前未知的可利用的内存安全缺陷。10月份，Protect AI 也发布了一款开源工具 Vulnhuntr，它利用 Anthropic 公司研发的 Claude LLM 从基于Python的项目中找到 0day漏洞。

OSS-Fuzz 团队在2023年8月引入基于AI的fuzzing，旨在fuzz 更大比例的代码库，以提升fuzzing覆盖率即所测试的代码数量。Fuzzing的流程涉及编写 fuzzing 目标，即“接受字节数组并使用在测的API与这些字节共同做一些有趣事情的函数”，之后处理潜在的编译问题和运行fuzzing目标查看其如何执行、修正和重复该流程，查看这些崩溃能否追溯到特定的漏洞。

OSS-Fuzz 最初处理了前两个步骤：（1）编写初始fuzz目标，和（2）修复引发的任何编译问题。之后在2024年开始，谷歌开源了 OSS-Fuzz 并尝试改进该软件处理后续步骤的方法：（3）运行 fuzz 目标以查看其如何执行并修复任何可引发运行时问题的明显错误；（4）在更长的时间内运行已修正的 fuzz 目标并对崩溃情况进行分类，判断其根因；以及（5）修复漏洞。

谷歌提到，其LLM目前可处理前四个fuzzing流程，计划不久后处理第5个步骤。Chang、Liu 和 Metzman 提到，“目标是通过LLM生成漏洞补丁建议，完全自动化整个工作流。虽然我们今天没有任何可以分享的内容，但我们正在与各个领域的研究员协作实现这一目标并期待不久可以分享结果。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[从Naptime到Big Sleep：通过大语言模型捕获真实代码中的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521381&idx=1&sn=dda99ba77206503fe0e0b1c0e5a0a35b&chksm=ea94a50fdde32c1962a406f9ce6e4f93f34ce95f0f4a77c0ceb6e383f9a6284d442c57816e28&scene=21#wechat_redirect)

[DHS发布在关键基础设施安全开发部署AI的框架](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521523&idx=2&sn=9222522f67aa6bada64bed055a3adfeb&chksm=ea94a599dde32c8f8d8f5599323d8cc50d3bb12bb0716412c69e77986c4f0d238aea4efec5fa&scene=21#wechat_redirect)

[谷歌AI平台存在漏洞，可泄露企业的专有LLMs](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521484&idx=1&sn=19327f5e0d0275273114fd7a7e37da3f&chksm=ea94a5a6dde32cb0f0b1bd0f310958066fd5a8549d8aedabac5528fbd6f1b55d985e8385ecf6&scene=21#wechat_redirect)

[研究员在开源AI和ML模型中发现30多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&chksm=ea94a559dde32c4f32a18c5ad4c3a2fc98f17fb29f69f73cac5c613c67ae28f36ab473d14936&scene=21#wechat_redirect)

[超过三分之一的员工与AI共享工作机密](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520981&idx=1&sn=7350d1b84ce9746dae06aafc5e55e76a&chksm=ea94a3bfdde32aa9a656ece3d6e12959f385a712e4b31e2e665d89a77c0b95cb2e742dbe0d91&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/11/20/google\_ossfuzz/

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