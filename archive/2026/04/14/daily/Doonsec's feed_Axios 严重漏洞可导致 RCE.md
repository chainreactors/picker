---
title: Axios 严重漏洞可导致 RCE
url: https://mp.weixin.qq.com/s/zkBXYkmDlHMNQtxkdCOwZQ
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:42:22.173179
---

# Axios 严重漏洞可导致 RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfUOeKKaIrhvP20yNRsYjHoNGicxKbIvOKxDIUQHGzDiaxrBCQ1t7CjZlicu9agdjmGxeWPMu1ibDXag5jFcDibN9Cro11Xriad0TMOgA/0?wx_fmt=jpeg)

# Axios 严重漏洞可导致 RCE

Abinaya
Abinaya

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**使用最为广泛的 HTTP 客户端库之一 Axios中存在一个严重安全漏洞CVE-2026-40175（CVSS评分9.9）可导致应用程序面临远程代码执行（RCE）风险，并可能使整个云基础设施遭攻击。该漏洞可导致攻击者绕过 AWS IMDSv2 安全控制，从而窃取敏感的云元数据。**

该漏洞由安全研究员 raulvdv 发现，随后由 jasonsaayman 公开发布了概念验证。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWX5lRnfGGticQ64Kv1icSbMXLbJsmByiaIx0NfK4daS4F0oftZx3yYZAiapDS5QXu5dFwGLL1l4ZibOVvsGYjLG1367dIOquetMcNs/640?wx_fmt=gif&from=appmsg)

**攻击链**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWLvgibgyyQB5f6UaqicJkbUNHNRwqZYBKWBRBvgPzQ58RAdxrC0qibP3lA983QiaYb8gaEt4rCaicgAVgmIB2gAXWqkCGZPT81X5nI/640?wx_fmt=gif&from=appmsg)

该漏洞的根本原因在于 axios npm 包中通过头部注入链实现的无限制云元数据窃取漏洞。

安全公告提到，该漏洞的核心问题存在于该库的头部处理组件中，具体位于 lib/adapters/http.js 文件内，与HTTP 头部完全缺乏净化处理（CWE-113）相关。当与默认存在的服务器端请求伪造（SSRF）能力（CWE-918）及请求走私（CWE-444）相结合时，形成了一个高度可利用的攻击向量。该漏洞之所以特别危险，是因为无需任何用户直接输入，整个利用过程完全依赖于一条“Gadget” 攻击链。

如果攻击者通过应用程序技术栈中的任何其它第三方依赖（例如 body-parser、qs 或 minimist）成功污染了 Object.prototype，则 Axios 会在其配置阶段自动合并这些被污染的属性。由于 Axios 未能对这些合并后的值进行回车换行 (CRLF) 字符的净化处理，该属性便会转化为一个极具破坏性的 HTTP 请求走私载荷。

已发布的概念验证演示了一个针对云环境的严重攻击场景。当开发者发起一个完全安全的、硬编码的出站请求时，Axios 会无意中将被污染的原型属性（例如x-amz-target）合并到请求头部中。这些恶意头部随后被直接写入套接字，而未经任何结构性验证。这就使得攻击者能够走私一个指向 AWS EC2 元数据服务（地址为 169.254.169.254）的次级 PUT 请求。该被走私的请求包含了必需的 X-aws-ec2-metadata-token-ttl-seconds头部，从而成功绕过了 AWS IMDSv2 的会话令牌保护机制。随后，攻击者可以检索到有效的会话令牌，窃取 IAM 凭证，并实现完整的云账户接管，同时还会引发诸如认证绕过和缓存投毒等次级影响。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUcEtbuwCVbvfOXcWJ3vFNnLHwV774icRGWPSiaNE6xbeUfHMab4Q2J4PRiayhtEGFCB7SupKdFJU4KQ1yYkBlGWsYia9ibrGLTYCRc/640?wx_fmt=gif&from=appmsg)

**受影响版本与修复措施**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVH5SndqlibfLaNrxRunLoPLRIy7hu3qwgINotBCcpZWNGl3ticIe9RcdmzFH7Ticib3YFNFKqlUSmZOVLonniap4xvUMBfoQHPlibUM/640?wx_fmt=gif&from=appmsg)

该漏洞影响范围广泛，涵盖了旧有分支和现代分支中的大量 Axios 部署。所有 1.13.2 版本之前的 Axios 版本均明确易受此 Gadget 攻击链的影响。为了缓解这一严重威胁，开发团队必须立即将 Axios 依赖项升级至 1.15.0 或更高版本。补丁通过在对所有头部值传递到底层请求函数之前实施严格校验，修复了该漏洞。如更新后的库检测到任何无效的 CRLF 字符，它将立即抛出安全错误，从而有效阻断注入链，阻止请求走私攻击。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Axios npm 包遭投毒，发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525629&idx=2&sn=b076315a014fe06f2a8b6eeec62f33c2&scene=21#wechat_redirect)

[Marimo 高危预认证 RCE 漏洞已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525746&idx=2&sn=777605c08e8d6f2e0dbad63e8f408da4&scene=21#wechat_redirect)

[Progress ShareFile 漏洞可用于发动预认证 RCE 攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525643&idx=2&sn=46f21b64114594cdb5db7473129e09a8&scene=21#wechat_redirect)

[Grafana 多个严重漏洞可用于实现 RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525587&idx=2&sn=a18525fe72676659d744674b7d8fdd16&scene=21#wechat_redirect)

**原文链接**

https://gbhackers.com/critical-axios-vulnerability-poc-released/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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