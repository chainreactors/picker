---
title: 四款微软Azure服务存在漏洞，可导致云资源遭越权访问
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515363&idx=3&sn=6c939ad71b9754325cf5e804212ce38e&chksm=ea948d89dde3049f9674c7caff6a7a10ad9243925974600a40bc322cfba7198f6d8f4e045dbf&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-21
fetch_date: 2025-10-04T04:29:27.551778
---

# 四款微软Azure服务存在漏洞，可导致云资源遭越权访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTemklgaj68k6nObQicJq7m7bNLjS34pKfWIiabM0Aicjib7BpJgM0iaoORnRSTlTibPrXMsVwzFDvdfGdQ/0?wx_fmt=jpeg)

# 四款微软Azure服务存在漏洞，可导致云资源遭越权访问

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**四款不同的微软 Azure服务易受服务器端请求伪造 (SSRF) 攻击，可使攻击者获得对云资源的越权访问权限。**

这些漏洞是由Orca公司在2022年10月8日至2022年12月2日在Azure API Management、Azure Functions、Azure Machine Learning 和 Azure Digital Twins 中发现的，目前已修复。

Orca 公司的研究员 Lidor Ben Shitrit 在报告中指出，“这些Azure SSRF漏洞可使攻击者扫描本地端口，查找新服务、端点和敏感文件，获得可能易受攻击服务器和服务中的有价值信息，从而获得初始入口点和敏感信息的位置。”

Azure Functions 和 Azure Digital Twins 中的两个漏洞可在无需任何认证的情况下遭滥用，甚至在无需拥有Azure账号的情况下，攻击者就能够控制服务器。SSRF攻击可使攻击者读取或更新内部资源，甚至跳转到网络的其它部分，攻陷无法触及的系统，提取有价值的数据。

三个漏洞的严重性为“重要”，而影响Azure Machine Learning 的SSRF漏洞为低危级别。所有这些弱点可被用于操纵服务器，从而发动更多攻击。

这四个漏洞的简要说明如下：

* Azure Digital Twins Explorer 中存在未认证的SSRF漏洞，可被用于从任何后缀为 “blob.core.windows[.]net” 的服务中获得响应。
* Azure Functions 中存在未认证的SSRF漏洞，可用于枚举本地端口并访问内部端点。
* Azure API Management 服务中存在认证的SSRF漏洞，可被用于列出内部端口，包括和源代码管理服务相关联的端口，从而访问敏感信息。
* Azure Machine Learning 服务中存在认证的SSRF漏洞，可被用于从任意端点提取内容。

建议组织机构验证所有的输入，确保服务器被配置为仅允许进站和出站流量，避免配置不当并遵循最小权限原则，以缓解这些漏洞。

Ben Shitrit 表示，“这些发现最引人瞩目的地方在于，仅投入最少的精力就发现如此多的SSRF漏洞，这说明这些漏洞是多么普遍以及它们对云环境造成多么大的风险。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[微软悄悄修复Azure跨租户数据访问高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515121&idx=1&sn=a174aa208e22a8d97fae0aa69a4777b2&chksm=ea948a9bdde3038d87dd9ce4fd4207e50cee5c030640d32b5ae879eac287877c6505152caf15&scene=21#wechat_redirect)

[微软Azure SFX漏洞可导致Service Fabric集群遭劫持](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514269&idx=2&sn=61fe8c8c8b4505c23ab577d13989e73c&chksm=ea9489f7dde300e13728eb2f26e16b58db650e35dc327f5498c2e7732678f4cf0397a44ff4b0&scene=21#wechat_redirect)

[微软 Azure FabricScape 漏洞可被用于劫持 Linux 集群](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512652&idx=2&sn=41462de310311abaadf3c81fa66dab19&chksm=ea948326dde30a30b6628410dbec18f7095b4ceac398685c020321f11a956d0d0c573779d4f5&scene=21#wechat_redirect)

[价值4万美元的微软Azure漏洞 ExtraReplica，没有CVE编号](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511627&idx=1&sn=8437c9d6450d98c727d653f1661b090c&chksm=ea949f21dde316375d993c85f24a29825426042f405f05a45d606e25b9d9520b8a6f34fec4d8&scene=21#wechat_redirect)

[200多个恶意NPM程序包针对Azure 开发人员，发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511070&idx=3&sn=a1f87fa84198504a6fd9c1d6d258152f&chksm=ea949d74dde314621963b38e7e1cb232355f633eff9cdb3e6d6989e764ee387af86886c7a87f&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/01/microsoft-azure-services-flaws-couldve.html

题图：Pexels License‍

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