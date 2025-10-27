---
title: 恶意npm包利用镜像文件隐藏后门代码
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520084&idx=2&sn=07657bb6d212f2245303aa7ff98e61f2&chksm=ea94be3edde33728bb8224656ce3ac1a88ba9ebb495c26fb1b3a31d7a63bc26b9e33180851f5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-18
fetch_date: 2025-10-06T17:45:08.151034
---

# 恶意npm包利用镜像文件隐藏后门代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRuyPCCn03PoqjFg1NPW9Mq7EkXA43AmmrwXBWCqsRTiarbZkuHcn7BibfZIaabZNpTET7jQBhTj0Mg/0?wx_fmt=jpeg)

# 恶意npm包利用镜像文件隐藏后门代码

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究员在 npm 包注册表中发现了两个恶意包可隐藏后门代码，执行从远程服务器发送的恶意命令。**

这些程序包 img-aws-s3-object-multipart-cope 和 legacyaws-s3-object-multipart-copy 的下载量分别为190次和48次。在本文写作时它们已被 npm 安全团队拿下。

软件供应链安全公司 Phylum 分析指出，“它们包含了隐藏在镜像文件中的复杂命令和控制功能，而这些镜像文件会在包安装过程中执行。”这些包旨在模拟合法npm库 aws-s3-object-multipart-copy，但替换了 “index-js” 文件版本以执行 JavaScript 文件 “loadformat.js”。该JavaScript 文件旨在处理两个镜像（Intel、微软和AMD的企业标识），其中与微软标识对应的镜像用于提取和执行恶意内容。

该代码通过发送主机名和操作系统详情，以C2服务器注册新客户端，之后每隔五秒来执行由攻击者发布的命令。在最后阶段，该命令执行的输出被通过特定端点提取返回给攻击者。

Phylum 公司表示，“在最后几年中，我们看到发布到开源生态系统中的恶意包的复杂度和体量都急剧增长。这些攻击者如果不犯错的话就是成功的。开发人员和组织机构意识到这个问题的存在至关重要，而且应警惕自己所使用的开源库。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[NPM恶意包利用招聘诱骗开发人员安装恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519374&idx=1&sn=3fbf5576659950047d9bc0dcc5ce061e&chksm=ea94bde4dde334f2adf3531901e2c95aea07bf3a099b0125048228dac88779dac4e96a334141&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析（二）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519078&idx=1&sn=eec7bf30c2e7abec80f62c022aa099c5&chksm=ea94ba0cdde3331aeabc6907e171c8b1e46209449d7af19a294d6cabe1260bb3a418ff465eaf&scene=21#wechat_redirect)

[朝鲜黑客被指利用恶意 npm 包攻击开发人员](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518933&idx=2&sn=88861c67e7ee4c7c97899ef4d2b66e36&chksm=ea94bbbfdde332a9650908994ea3fe95eb7a8ac5cc3fbc7088f3ab6be4b4ed800ee707d8136f&scene=21#wechat_redirect)

[NPM 恶意包通过 GitHub 提取数百个开发者SSH密钥](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518740&idx=2&sn=2a19b89ecf0b060ed05766e9be298779&chksm=ea94bb7edde332685fb1f9a65fbeb058226732b9c63abe7ba1afaf4b07814d596475041deaab&scene=21#wechat_redirect)

[NPM 注册表恶作剧导致开发人员无法取消发布程序包](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518582&idx=1&sn=260d22f2c635df2cd1445956f94b7760&chksm=ea94b81cdde3310ad016d3ec97bbb3d0dc5c7c7050fa3c8ab6dd97757d04d0e01161ff8d529e&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/malicious-npm-packages-found-using.html

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