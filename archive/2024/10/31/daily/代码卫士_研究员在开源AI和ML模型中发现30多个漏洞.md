---
title: 研究员在开源AI和ML模型中发现30多个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&chksm=ea94a559dde32c4f32a18c5ad4c3a2fc98f17fb29f69f73cac5c613c67ae28f36ab473d14936&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-31
fetch_date: 2025-10-06T18:54:24.024148
---

# 研究员在开源AI和ML模型中发现30多个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSP1mk8ibDy4h2yria9iaicFE8fSREibjTic4eVvRyHziaiaoMeChMkKibrrVucypuEe6qF5xia7pv6u78Xn8xA/0?wx_fmt=jpeg)

# 研究员在开源AI和ML模型中发现30多个漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**多个开源人工智能 (AI) 和机器学习 (ML) 模型中存在30多个漏洞，其中一些可导致远程代码执行和信息盗取后果。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSP1mk8ibDy4h2yria9iaicFE8fNJI4oe6SgrcQBR8wjVhkXfRV1YZJfMvNFF44C80EOibw47PbQ6Tlcog/640?wx_fmt=png&from=appmsg)

这些漏洞位于多款工具中如 ChuanhuChatGPT、Lunary和LocalAI 中，通过 Protect AI 的 Huntr 漏洞奖励计划报送。其中最严重的是影响大语言模型生产工具包 Lunary的两个漏洞：

* CVE-2024-7474（CVSS评分9.1）：不安全的直接对象引用漏洞，可导致认证攻击者查看或删除外部用户，导致未授权数据访问和潜在的数据丢失。
* CVE-2024-7475（CVSS评分9.1）：该访问控制不当漏洞可导致攻击者更新 SAML 配置，从而以越权用户身份登录并访问敏感信息。

Lunary 中还存在另外一个IDOR 漏洞（CVE-2024-7473，CVSS评分7.5），可导致恶意人员通过操纵受用户控制的参数更新其它用户的提示符。

Protect AI 公司在一份安全公告中提到，“攻击者以用户A的身份登录并拦截该请求以更新提示符。通过将该请求中的参数’id’修改为属于用户B的提示符的’id’，攻击者可在未授权的情况下更新用户B的提示符。”

第三个严重漏洞是位于 ChuanhuChatGPT 用户上传特性中的路径遍历漏洞（CVE-2024-5982，CVSS评分9.1），可导致任意代码执行、目录创建和敏感数据暴露后果。

供用户运行自托管LLMs 的开源项目LocalAI中也存在两个漏洞，可导致恶意人员通过上传恶意配置文件执行任意代码（CVE-2024-6983，CVSS评分8.8）以及通过分析服务器的响应时间猜测合法的API密钥（CVE-2024-7010，CVSS评分7.5）。

Protect AI 公司表示，“该漏洞可使攻击者执行定时攻击。它是一种侧信道攻击，通过了解不同API密钥处理请求所需的时间，攻击者一次一个地推断正确的API密钥。”

最后一个漏洞是影响 Deep Java Library (DJL) 的源自任意文件覆写的远程代码执行漏洞，位于该程序包的untar函数 (CVE-2024-8396，CVSS评分7.8)中。

此前不久，英伟达修复了位于 NeMo 生成式AI 框架中的一个路径遍历漏洞（CVE-2024-0129，CVSS评分6.3），可能导致代码执行和数据篡改后果。建议用户更新至最新版本，保护AI/ML供应链安全，以防遭攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&chksm=ea94a259dde32b4f211fb59ae290ca1daab65c90d84350afe2de36239f2907afe0466021e549&scene=21#wechat_redirect)

[超过三分之一的员工与AI共享工作机密](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520981&idx=1&sn=7350d1b84ce9746dae06aafc5e55e76a&chksm=ea94a3bfdde32aa9a656ece3d6e12959f385a712e4b31e2e665d89a77c0b95cb2e742dbe0d91&scene=21#wechat_redirect)

[普遍存在的LLM幻觉扩大了软件开发的攻击面](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519204&idx=1&sn=8b889973e145d7b438fdc2609171340f&chksm=ea94ba8edde33398d0452d0d8ca3dd715d06faf2ddf0b63ef13a536f320298022b695c36082c&scene=21#wechat_redirect)

[挖出被暴露的1500+APT令牌，破解近千家公司的LLM仓库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518271&idx=2&sn=498e1dc2bb31e36ddbfa4c69c7593122&chksm=ea94b955dde330430a08be2022b6435807998814fbf53040e98c291ad0ffced72b267796d3b1&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/researchers-uncover-vulnerabilities-in.html

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