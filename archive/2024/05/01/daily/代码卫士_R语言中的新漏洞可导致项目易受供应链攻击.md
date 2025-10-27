---
title: R语言中的新漏洞可导致项目易受供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519400&idx=1&sn=66cec4a7fd3d72c14f92738147c6d83a&chksm=ea94bdc2dde334d4b90886120c2d35848bb06c0cb45b93d2e709e6ceeacef8ea6b680ebbac16&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-01
fetch_date: 2025-10-06T17:18:53.257135
---

# R语言中的新漏洞可导致项目易受供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWabr5o4ic05fn5PD4RibKovQaF5JsUFNCEgL8xM1npdvu7pib13Nl6sT0Cn6SaHhcP9EIC7IE85cfQ/0?wx_fmt=jpeg)

# R语言中的新漏洞可导致项目易受供应链攻击

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**R编程语言中存在一个漏洞，可被威胁行动者用于创建一个恶意RDS（R数据序列化）文件，从而在加载和引用时导致代码执行后果。**

AI应用安全公司 HiddenLayer 在报告中提到，该漏洞的编号是CVE-2024-27322，“涉及使用R中的 promise 对象和惰性评估。” RDS类似于Python 中的 pickle，是一种用于对R中数据结构或对象状态进行序列化并保存的格式。R语言是一种开源编程语言，用于统计计算、数据可视化和机器挖掘。

这种序列化流程（serialize() 或 saveRDS()）和反序列化（unserialize() 和 readRDS()）也用于保存和加载R包。CVE-2024-27322的根因在于，在反序列化不可信数据时会导致任意代码执行，从而可使用户通过特殊构造R包被暴露给供应链攻击。因此，武器化利用该缺陷的攻击者可利用R包通过RDS格式保存和加载数据的方法，在程序包被解压和反序列化时自动执行代码。

安全研究员 Kasimir Schulz 和 Kieran Evans 表示，“R包易受该利用影响，因此能够用作经由包仓库发动的供应链攻击的一部分。攻击者要接管R包，他们所需做的就是以恶意构造的文件覆写 rdx 文件，而当宝加载时，它会自动执行代码。”

该漏洞已于2024年4月24日的版本4.4.0中修复。

HiddenLayer 公司指出，“攻击者利用该漏洞的方式是，构造 RDS 格式的文件，其中内含一个promise 指令，将值设为 unbound\_value以及将表达式设为包含任意代码。由于惰性评估的原因，该表达式只有在与 RDS 文件相关联的符号被访问时，才会被评估和运行。因此，如果它只是一个RDS文件，当用户为其分配一个符号（变量）进行运作时，当用户引用该符号时，任意代码将会被执行。如果该对象是在R宝中编译的，则该包可被添加到 R 仓库中如 CRAN，而该表达式将得到评估，当用户加载该包时，任意代码就会运行。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[在线阅读版：《2023中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&chksm=ea94b543dde33c55c168c44e830d62b03e9b34ca072871d10156273a3f282cab7ccc42b9b430&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[NSA 发布关于集成SBOMs 提升网络安全的指南](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518431&idx=2&sn=dbc1902cbf3e9d6194ae9f2f2a78be9b&chksm=ea94b9b5dde330a3da280c0904d15ce182856b4c061ace87deb7a86f9a8b7417cd8fffbde14d&scene=21#wechat_redirect)

[CISA、NSA等联合发布关于SBOM的软件供应链安全保护新指南](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518114&idx=1&sn=fc054c7175c91a0884dd651f6f50d979&chksm=ea94b6c8dde33fde6f7e4daf2b5d2667ce13135554b2b3e871158dca1999c5b1a93fc84cd6b0&scene=21#wechat_redirect)

[《软件供应商手册：SBOM的生成和提供》解读](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511570&idx=1&sn=a8eda02cab19a290202dd91895bd3887&chksm=ea949f78dde3166e104a4d6a2c2c9e1b32d673f6589993a2f2bfb94740bdc6cdc0088dc8c273&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（上）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509892&idx=1&sn=f149d024a5a8742859d3b08d90a9111e&chksm=ea9496eedde31ff8e60949842119828151d8a0200b56b5f524e2851e9a5913ba90b605ad7fed&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（中）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509894&idx=1&sn=b4815181d043ae4843fd1d3cea5e196b&chksm=ea9496ecdde31ffa29e43cbaf6c60811908b0eb21e9fd1e23d7c161ae675cb83b35359bcfb08&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（下）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509930&idx=1&sn=3573aa307f009e3709fcbb2ac5498e66&chksm=ea9496c0dde31fd6d2f330cd5526fe409c08648ef2236d4674ae043a9939d95df908121c8f93&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/04/new-r-programming-vulnerability-exposes.html

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