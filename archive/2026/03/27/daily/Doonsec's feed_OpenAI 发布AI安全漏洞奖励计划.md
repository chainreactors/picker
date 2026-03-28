---
title: OpenAI 发布AI安全漏洞奖励计划
url: https://mp.weixin.qq.com/s/jJrwgDN6rC3q2beEG-LhpQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:52.789526
---

# OpenAI 发布AI安全漏洞奖励计划

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfVRyPHztdXliaMKFgAxKiahw1YaJsdeWV6O1w6HjreGlb2R3kwicNSXyYwTCtRaicelnAgczrHtUMKGQFpQ6zlRicwqCghfuBcUY2Qg/0?wx_fmt=jpeg)

# OpenAI 发布AI安全漏洞奖励计划

Guru Baran
Guru Baran

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**OpenAI****公司发布公开的安全漏洞奖励计划，旨在识别产品中的AI滥用和安全风险问题。**

该AI漏洞奖励计划在 Bugcrowd 平台上实施，标志着 OpenAI 开始修复传统安全漏洞范围以外但仍然可能造成实际影响的漏洞。该漏洞奖励计划旨在补充 OpenAI 公司现有的安全漏洞奖励计划，任何存在重大滥用和安全风险的问题甚至是这些问题并非传统安全漏洞的漏洞报告均可提交。

OpenAI 公司将与安全漏洞奖励团队共同对这些漏洞进行初审，并根据漏洞的范围和归属，在两个项目之间进行重新分配。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUNibumgaPgaX8dS0CTETfKaUic3PN300tct0wSH6cpC2eRUvWicBIXGNWq8t8SDn8aXh5ecZpfia6ml8A4zJsRGLbjJfNZg02keH4/640?wx_fmt=gif&from=appmsg)

**相关的AI风险类别**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUyy4MyGB2GVpWck4oqibDIkuQFEicIHCj1E6icicN5m5unV5MuH1BWFQTT8RhJJ2jLvVdk3BgLDySW8WNdIjFibicjmJkpL2icdmUMFE/640?wx_fmt=gif&from=appmsg)

该计划针对几种不同类别的AI特定安全场景：

**包括MCP的代理风险**——涵盖第三方提示注入和数据外泄场景，即攻击者控制的文本能够可靠地劫持受害者的AI代理（包括Browser、ChatGPT 智能体及类似的代理型产品），从而执行有害操作或泄露敏感用户数据。如属于该场景，利用行为必须至少有50%的概率可重现。涉及代理型产品大规模执行被禁止或潜在有害行为的报告也在范围内。

**OpenAI****专有信息**——研究人员可报告模型生成内容中无意暴露的推理相关专有信息，以及泄露OpenAI其它保密数据的漏洞。

**账户与平台完整性**——此类别针对账户和平台完整性信号中的弱点，包括绕过反自动化控制、操纵账户信任信号、以及规避账户限制、暂停或封禁等。

OpenAI已明确说明仅导致粗鲁语言或公开已知信息的通用越狱、无明确安全或滥用影响的一般性内容策略绕过将不在奖励范围内。不过，OpenAI会定期开展针对特定危害类型的私有漏洞赏金活动，例如ChatGPT 智能体和GPT-5中的生物风险内容问题，并会在这些项目启动时邀请研究人员申请参与。

对于能够实现超出允许权限范围对功能、数据或功能进行未授权访问的漏洞，研究人员应转向现有的安全漏洞赏金计划进行提交。

本次推出的AI漏洞奖励计划表明，人们越来越认识到AI系统引入了一个全新的攻击面，这是传统安全框架未曾设计去应对的。OpenAI 公司在对传统漏洞披露进行激励的同时，也对关注安全性的研究给予奖励，从而有效地为针对AI的威胁建模建立一个结构化的框架。

有兴趣参与的研究人员可以直接通过OpenAI在Bugcrowd平台上的安全漏洞赏金页面进行申请。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[OpenAI 编程代理中高危漏洞可用于攻击开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524571&idx=2&sn=e4271fa2e064e2011e1b779ac929f05f&scene=21#wechat_redirect)

[第三方供应商导致OpenAI客户数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524535&idx=1&sn=b7fe9e8a785380e376468375bde77bce&scene=21#wechat_redirect)

[看我如何通过 OpenAI o3 挖到 Linux 内核远程 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523149&idx=1&sn=0298267a08369cc3ea9bdbdec81eb788&scene=21#wechat_redirect)

**原文链接**

https://cybersecuritynews.com/openai-safety-bug-bounty/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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