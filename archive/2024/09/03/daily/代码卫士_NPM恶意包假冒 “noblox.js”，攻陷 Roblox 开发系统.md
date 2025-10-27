---
title: NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=1&sn=5c21506b72287be7f4b329b57e790e30&chksm=ea94a0efdde329f9ad2d8aeb345bc8abbc9c850e4352100732abc69077d910cccc0ce2259be5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-03
fetch_date: 2025-10-06T18:26:08.711795
---

# NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT7yqfyZ7aKtka4IcuvUMRLIC9ibr0h4r3OfrUT2kuWpgBDRRz0XIgCANmjkQMkvOT9ia2dOFQkaqzg/0?wx_fmt=jpeg)

# NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**攻击者通过 npm 恶意包攻击Roblox 开发人员，再次表明威胁行动者利用该开源生态系统中的信任来传播恶意软件。**

Checkmarx 公司的研究员 Yehuda Gelb 在技术报告中提到，“通过模拟热门 ‘noblox.js’ 库，发布数十个包，窃取敏感数据并攻陷系统。”

该攻击活动的详情由 ReversingLabs 在2023年8月首次记录，它是 Luna Token Grabber 窃取器活动的一部分，被指重现了“两年前（2021年10月）所发现攻击活动”。

自今年开始，另外两个包 noblox.js-proxy-server 和 noblox-ts 被识别为恶意包并模拟热门 Node.js 库来传播窃取器恶意软件和一个远程访问木马 Quasar RAT。

Gelb 表示，“攻击人员利用多种技术如 brandjacking（品牌劫持）、combosquatting（组合式域名仿冒） 和 starjacking （标星劫持）等为其恶意包营造一种合法幻象。”为此，这些包被命名为 noblox.js-async、noblox.js-thread、noblox.js-threads 和 noblox.js-api，以此诱骗不知情的开发人员它们与合法包 “noblox.js”相关。

这些包的下载数据如下：

* noblox.js-async（74次下载）
* noblox.js-thread（117次下载）
* noblox.js-threads（64次下载）
* noblox.js-api（64次下载）

攻击者利用的另外一种技术是starjacking（标星劫持），即恶意包将来源仓库标注为真实 noblox.js 库，以增加其可信度。最近版本中的嵌入式恶意代码是处理托管在 GitHub 仓库上额外payload 的网关，在窃取 Discord 令牌的同时更新微软 Defender杀毒例外列表以躲避检测，并通过 Windows Registry 变更的方式设置可持久性。

Gelb 提到，“该恶意软件的有效性主要体现在持久性方式，它利用 Windows Settings 应用确保持续的访问权限。结果，每当用户尝试打开 Windows Settings app时，系统就不可避免地执行该恶意软件。”

这一攻击链的最终目标是部署 Quasar RAT，使攻击者获得受感染系统的远程控制。信息通过 Discord 网勾被收割到攻击者的 C2服务器中。

这些研究结果表明，尽管已采取下架措施，但仍有稳定的新包流被发布，因此开发人员应保持警惕。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&chksm=ea94a18edde328988758d00a0c6c91218ef60546d92e98647d91c44e557d14c15596b8aff06c&scene=21#wechat_redirect)

[奇安信《软件供应链安全报告》：七成国产软件有超危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520483&idx=1&sn=88f4a392cdd026b85ddfa12a4faa8746&chksm=ea94a189dde3289ffa6b70b463e67d3cc6da669d3540403f5551f944351a8b435d3b9e32a029&scene=21#wechat_redirect)

[JFrog Artifactory 缺陷导致软件供应链易受缓存投毒攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520385&idx=2&sn=af4a594c3080780ffef2c03ee32f72d5&chksm=ea94a1ebdde328fdfc828f63fc0ecbd0128261440aeba197b83f1d8e451ce4507c42bfa4878a&scene=21#wechat_redirect)

[SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=2&sn=7b4dbeae684f3e9a1f79148a5bacf221&chksm=ea94bea8dde337bef23eba6e45455dcd8628e9612a3fe48edfb13b4eb3d31ab510a7d6df1a85&scene=21#wechat_redirect)

[朝鲜黑客利用恶意npm包攻击开发者](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520635&idx=1&sn=bca2e1daf7393a8f8b52a89f78ee82e1&chksm=ea94a011dde329074eb7d1b5ea9606984d8a42e5226d605faf16ab5b0ea9ed8d500e89c3df2b&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html

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