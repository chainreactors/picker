---
title: MLOps 平台存在20多个供应链漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520605&idx=2&sn=6bd044882cfd8e5f96140c71e26498f4&chksm=ea94a037dde32921016d3ccc578f09450825636f654da7d674940fccba2dbb77ba63a80dd774&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-28
fetch_date: 2025-10-06T18:04:41.217005
---

# MLOps 平台存在20多个供应链漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTZ7BZm7pOqHICJyZx6jc86uSOTPZFMB0ibcfrayoxCHFGGYAwtDh6zBfMLwiaBTiaE5DTvbyh4oo9XA/0?wx_fmt=jpeg)

# MLOps 平台存在20多个供应链漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究人员提醒称，MLOps 的多个平台中存在20多个漏洞，机器学习软件供应链中存在安全风险。**

这些漏洞是内在的实现漏洞，可造成严重后果如任意代码执行、恶意数据集加载等。MLOps 平台提供设计和执行ML模型管道的能力，其中模型注册表当作存储和版本训练ML模型的仓库。这些模型随后被嵌入应用程序或使其它客户端通过API进行查询（即模型即服务）。

JFrog 公司发布报告提到，“内在漏洞是指由目标技术中所用的底层格式和进程所引发的漏洞。”这些漏洞包括利用模型支持加载后自动执行代码的事实，滥用ML模型运行攻击者所选代码。这一行为还可扩展到允许自动代码执行的某些数据集格式和库，从而在加载公开可用的数据集时，执行恶意攻击。

另外一种内在漏洞实例与 JupyterLab（此前成为“Jupyter Notebook”）有关，它可导致用户执行代码块并查看相应结果。研究人员提到，“很多人不知道的一个内在问题是在Jupyter中运行代码块时，处理HTML输出。Python代码的输出可能发出HTML和JavaScript，从而由浏览器渲染。”

问题在于，运行过程中的JavaScript结果并未从父 web 应用中进行沙箱隔离，父web应用可自动运行任意Python代码。换句话说，攻击者可输出恶意 JavaScript代码，在当前 JupyterLab notebook中增加新的cell，在其中注入 Python 代码，之后进行执行。当利用XSS漏洞时，更是如此。

为此，JFrog 表示，在MLFlow中发现一个XSS漏洞（CVSS评分7.5），是因为在运行不可信的recipe时缺乏充分清理造成的，可导致在 JupyterLab中的客户端代码执行后果。研究人员表示，“我们从研究结果中学到的一点是，我们需要将ML库中的所有XSS漏洞都视作潜在的任意代码执行漏洞，因为数据科学家们可能使用会与Jupyter Notebook一起使用这些ML库。”

第二类漏洞与实现弱点有关，如MLOps平台中缺乏认证、可导致具有网络访问权限的威胁行动者通过滥用ML Pipeline特性获得代码执行能力。这些威胁并非存在于理论之中，受利益驱动的攻击者会滥用这类漏洞如未修复的 Anyscale Ray 漏洞CVE-2024-48022（CVSS评分9.8）来部署密币挖矿机。

第二种实现漏洞是针对 Seldon Core的容器逃逸漏洞，不仅使攻击者执行代码，还可在云环境中横向移动并通过将恶意模型上传到引用服务器的方式访问其它用户的模型和数据集。组合利用这些漏洞可使攻击者渗透并在组织机构中进行传播，而且攻陷服务器。

研究人员表示，“如果部署的平台允许模型提供，那么应该知道任何人实际上可在该服务器上运行任意代码。确保运行该模型的环境完全隔离并针对容器逃逸进行加固。”

Palo Alto Networks Unit 42 公司详述了位于开源的 LangChain 生成式AI框架中的两个已修复漏洞CVE-2023-46299和CVE-2023-44467，它们分别可导致攻击者执行任意代码并访问敏感数据。

上个月，Trail of Bits 公司披露了位于 Ask Astro 中的四个漏洞，可投毒该聊天机器人的输出，给出不准确的文档并可能引发拒绝服务攻击。

就在受人工智能驱动的应用中暴露安全问题时，这些技术也被用于投毒训练数据集，最终目标是诱骗大语言模型生成易受攻击的代码。康涅狄格大学的研究团队表示，“和最近将恶意payload嵌入可检测部不相关代码的攻击不同，CodeBreaker 利用大语言模型进行复杂的 payload 转换（不影响功能），确保针对微调和生成代码的投毒数据能够躲避强大的漏洞检测。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&chksm=ea94a18edde328988758d00a0c6c91218ef60546d92e98647d91c44e557d14c15596b8aff06c&scene=21#wechat_redirect)

[奇安信《软件供应链安全报告》：七成国产软件有超危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520483&idx=1&sn=88f4a392cdd026b85ddfa12a4faa8746&chksm=ea94a189dde3289ffa6b70b463e67d3cc6da669d3540403f5551f944351a8b435d3b9e32a029&scene=21#wechat_redirect)

[JFrog Artifactory 缺陷导致软件供应链易受缓存投毒攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520385&idx=2&sn=af4a594c3080780ffef2c03ee32f72d5&chksm=ea94a1ebdde328fdfc828f63fc0ecbd0128261440aeba197b83f1d8e451ce4507c42bfa4878a&scene=21#wechat_redirect)

[SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=2&sn=7b4dbeae684f3e9a1f79148a5bacf221&chksm=ea94bea8dde337bef23eba6e45455dcd8628e9612a3fe48edfb13b4eb3d31ab510a7d6df1a85&scene=21#wechat_redirect)

[NuGet供应链攻击中出现60个新恶意包](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520048&idx=2&sn=3a630b3843ccc737be74aef33ed68cea&chksm=ea94be5adde3374c09c227af0497d92f22ebb7dd6e8b5e6a422233c492ffb7fdb16139152e78&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html

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