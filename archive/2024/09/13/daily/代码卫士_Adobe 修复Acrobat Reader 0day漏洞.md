---
title: Adobe 修复Acrobat Reader 0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520782&idx=1&sn=e5eaa66675d142213f7058469e5446bb&chksm=ea94a364dde32a72ce25776dba29053b255994b2a432f179d45b77761bdd6400a0d76195be17&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-13
fetch_date: 2025-10-06T18:27:56.610251
---

# Adobe 修复Acrobat Reader 0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkCXMhlwh1VJicrGMiaTibx5HFM0aqicTmythJhyAQicvU0fAC59JaZ9HiaIQWA/0?wx_fmt=jpeg)

# Adobe 修复Acrobat Reader 0day漏洞

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Acrobat Reader 中存在一个RCE 漏洞 (CVE-2024-41869)，其 PoC 已公开。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkC1m1XU9s28tELgO855dMKBbxLib3OQeZaibrj8kTvXWvCMKttzWNX9QrQ/640?wx_fmt=png&from=appmsg)

该漏洞是一个严重的释放后使用 (UAF) 漏洞，可导致在打开一个特殊构造的 PDF 文档时造成远程代码执行。UAF 漏洞是指当程序尝试访问已被释放或发布的内存位置中的数据时，就会被触发，从而导致异常行为如程序崩溃或冻结。

然而，如果威胁行动者能够在该内存位置存储恶意代码，而且程序后续访问它，就会导致在目标设备上执行恶意代码。该漏洞已在最新版本的 Acrobat Reader 和 Adobe Acrobat 版本中修复。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkClUxTKysgd4a6sb6lmfxJxS1kECB7BxQV80PmLydDKrtnM9SiaFZq0pQ/640?wx_fmt=png&from=appmsg)

**6月已出现PoC利用**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQOpd7wGiaRuOYnMUibGAZpkCZxgwgcUqicrF3NIhNtHNYyR7vfPnVzdbicIuDI0Ay3iboSnZNmOcqUfEw/640?wx_fmt=gif&from=appmsg)

该 Acrobat Reader 0day 漏洞由研究员Haifei Li 创建的基于沙箱的平台 EXPMON 发现。该平台用于检测高阶利用如0day或难以检测（了解）的利用。他指出，“我创建 EXPMON 是因为我注意到市场上没有从利用或漏洞角度专门检测威胁的基于沙箱的检测分析系统。其它系统从恶意软件的角度进行检测，而利用/漏洞角度的检测对于高阶或更早检测而言更有必要。例如，如果因为某些条件，没有释放或执行恶意软件，或者攻击根本没有使用恶意软件，那么从恶意软件角度的检测系统就会错过这些威胁。利用的运行方式和恶意软件大不相同，因此该平台应运而生。”

某个公开来源将大量样本提交到 EXPMON 平台进行分析时，发现了该0day 漏洞。这些样本包含一个导致崩溃的 PoC 利用的PDF文件。虽然该 PoC 利用尚未完成且不含恶意 payload，但它利用的是一个UAF漏洞，而该漏洞可用于远程代码执行。

研究员将该漏洞报送给 Adobe 公司后，后者在8月份发布安全更新。然而，该更新并未修复该漏洞，关闭多个会话后仍然可被触发。EXPMON 平台发布帖子称，“我们在‘已打补丁的’ Adobe Reader 版本上测试了同样的样本，它显示了更多的对话，但如果用户点击/关闭这些会话后，该 app 仍然崩溃！还是同一个UAF漏洞！”昨天，Adobe 发布新的安全更新修复了该漏洞，并分配编号CVE-2024-41869。

研究员将在 EXPMON 博客上发文详述如何检测到该漏洞，并在 Check Point 研究报告中发布更多技术详情。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Adobe Acrobat Reader 高危漏洞加入CISA必修清单](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517855&idx=2&sn=5ea5455de3ad27bd027a363a4b11a95a&chksm=ea94b7f5dde33ee34cdfbb1253dab1a695f4138beb5de5e782328ecbbfdee7df7e80594a5429&scene=21#wechat_redirect)

[补丁星期二：微软、Adobe和Firefox纷纷修复已遭利用的 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517643&idx=1&sn=83e85b6b9bf3a9f0cf0c1843c9589950&chksm=ea94b4a1dde33db74b2b9c5ff5da439c9a2169fcab51d215bdc495affe02787d31ab6bcf7b98&scene=21#wechat_redirect)

[CISA 将Adobe ColdFusion中的这个严重漏洞列入必修清单](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517437&idx=1&sn=561e8ad37f584120784a95e9ad1c33f4&chksm=ea94b597dde33c810a56421fadb562f0a4fbab00589ec4d11a1fb82d61b17dffcab841d4546a&scene=21#wechat_redirect)

[CISA紧急提醒：Adobe ColdFusion漏洞已遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515947&idx=3&sn=76c36938bf1b7401950fc62730020638&chksm=ea948e41dde30757c6826cbbaeba673c04d191b437bd8a20532e2a13614e94562772ade4c057&scene=21#wechat_redirect)

[厂商纷纷主动绕过Adobe发布的CVE-2022-24086安全补丁](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515346&idx=3&sn=7314d6f33c9cc44614100d627ee92de1&chksm=ea948db8dde304aeb1f522231dc8ba2f6cc789d08fd9bc2d2f0964ba7cd303a8233461778c96&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/adobe-fixes-acrobat-reader-zero-day-with-public-poc-exploit/

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