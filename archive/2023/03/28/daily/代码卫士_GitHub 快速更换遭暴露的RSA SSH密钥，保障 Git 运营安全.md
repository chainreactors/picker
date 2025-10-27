---
title: GitHub 快速更换遭暴露的RSA SSH密钥，保障 Git 运营安全
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516047&idx=3&sn=ec800747d687a834058098d463ea22b1&chksm=ea948ee5dde307f3b3952f794243a30e3d4e59cc11e684605af5470fac945242630786411cf6&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-28
fetch_date: 2025-10-04T10:53:32.662456
---

# GitHub 快速更换遭暴露的RSA SSH密钥，保障 Git 运营安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTshNd2iamlSye8z4iap7MWpr9NxcJ9mR9UUibbXbWYx35rOvtljzhfrW0ia69ibu1ZA0AgfW09oBxro6A/0?wx_fmt=jpeg)

# GitHub 快速更换遭暴露的RSA SSH密钥，保障 Git 运营安全

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**基于云的仓库托管服务GitHub 指出，用于保护Git 操作RSA SSH 托管密钥被短暂暴露在一个公开仓库后，“出于谨慎考虑”，将其替换。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTshNd2iamlSye8z4iap7MWprKtUCD1o6hEWdYha9fceo4ib5OicmOxrADU9YCpeRqr8ibxphPZ10Iq3cA/640?wx_fmt=gif)

RSA SSH密钥替换在UTC（协调世界时）时间2023年3月24日凌晨5点进行，目的是阻止而已人员模拟该服务或者窃听用户通过SSH执行的操作。

GitHub 的首席安全官兼工程高级副总裁 Mike Hanley 指出，“该密钥并无法提供对GitHub 基础设施或客户数据的访问权限。这一变更仅影响使用RSA 经由SSH 的Git 操作。”这一变更并不影响GitHub.com的web流量以及通过HTTPS执行的Git操作。ECDSA或Ed25519用户无需执行任何变更。

GitHub 公司指出，并无证据表明被泄露的SSH密钥遭利用。该公司未说明机密信息遭暴露的时长。该公司强调称，“问题并未由GitHub 系统或客户信息遭攻陷引起“，而是归咎于 ”无意的私密信息发布“。

GitHub 还提醒 GitHub Actions 用户称，如果使用actions/checkout 和ssh-key 选项，则可能发生工作流运行失败的情况，该公司表示目前正在更新所有标记中的这一操作。

就在近两个月前，GitHub 披露称未知威胁行动者设法提取了Mac 版本的GitHub Desktop和 Atom 应用的加密的代码签名证书。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[怕不怕？GitHub 公开库 API 和加密密钥泄漏了这么多秘密](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489511&idx=2&sn=300ab64753c5a2e6cf70f852d2c97d4f&chksm=ea97268ddde0af9b6be9b2412c4af041a4f856c4ef0760c898a1c5d93e6ba47c2d7c4367f718&scene=21#wechat_redirect)

[“松露猪”工具：检测GitHub项目的密钥是否被泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485602&idx=1&sn=348e4e83ae99d8bac2e4b4c6b47c44a7&chksm=ea9739c8dde0b0de4783dc138123e2a8fd44f2fce94dcaeb4111eddb60db9822f609da92ab24&scene=21#wechat_redirect)

[使用弱加密密钥的用户：你的GitHub账户可能被黑了](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485951&idx=1&sn=d1a8f4a5a73e198dd6a8390c2298c83e&chksm=ea973895dde0b18350f214e83414ad5c34afed2d3cc1eff85531d3760d310551d7596bce510e&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/github-swiftly-replaces-exposed-rsa-ssh.html

题图：Pexels License

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