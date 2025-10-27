---
title: GitHub 评论被滥用于推送密码窃取恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520653&idx=2&sn=985604e150b5d7056b6fc8994a7e1bf0&chksm=ea94a0e7dde329f19ea69d43025aac5fd29c4f7b03d47cc44b7c546409395353a6670156ed7f&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-04
fetch_date: 2025-10-06T18:28:01.904075
---

# GitHub 评论被滥用于推送密码窃取恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRDdWtvxiaIKBWPvO0QhcNdadBG5HxZlMg5SVsZoqQxWS3MDpxvicPicR8efI1mfoE8JgpYEBY2qCABg/0?wx_fmt=jpeg)

# GitHub 评论被滥用于推送密码窃取恶意软件

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**恶意人员将 Lumma Stealer 信息窃取恶意软件伪装成GitHub项目评论中的虚假修复方案进行传播。**

该攻击活动率先由 teloxide rust 库的一名贡献人员报告，他在Reddit 论坛上指出在 GitHub issue 中收到了五个试图伪装成修复方案的不同评论，但它们实际上在推送恶意软件。

BleepingComputer 审计发现，数千个类似评论发布在大量 GitHub 项目中，所有的评论都是对其他人问题提供的虚假修复方案。他们在回复中要求从 mediafire.com 或通过 bit.ly URL来下载受密码保护的文档，然后运行其中的可执行文件。在当前的攻击活动中，所有查看的评论中的密码都是 “changeme”。逆向工程师 Nicholas Sherlock 表示，在3天的时间里，超过2.9万个评论都在推送该恶意软件。

点击链接就会到达名为 “fix.zip” 的下载页面，其中包含一些 DLL 文件以及一份可执行文件 “x86\_64-w64-ranlib.exe”。在 Any.Run 上运行该可执行文件显示，它就是 Lumma Stealer 信息窃取恶意软件。

Lumma Stealer 是一款高阶信息窃取器，在被执行时会尝试窃取 cookies、凭据、密码、信用卡并从Chrome、Edge、Firefox和其它 Chromium 浏览器中浏览历史。

该恶意软件还可窃取密币钱包、私钥和文本文件，而这些文本文件的名称包括：seed.txt、pass.txt、ledger.txt、trezor.txt、metamask.txt、bitcoin.txt、words、wallet.txt、\*.txt 和 \*.pdf，它们更可能包含私钥和密码。这些数据被收集到一份文档中并发回给攻击者，供他们执行更多攻击或在网络犯罪市场出售。

虽然 GitHub 员工在检测到这些评论后就一直在删除，但已经有人表示受陷。不慎启动该恶意软件的任何人都应该修改所有账户的密码，为每个站点使用唯一密码并将密币迁移到新钱包。

上个月，Check Point 研究团队披露了一起由 Stargazer Boblin 组织发动的类似攻击活动，后者利用GitHub上超过3000个虚假账户创建了一个恶意软件分发即服务，推送信息窃取恶意软件。

目前尚不清楚二者是否存在关联。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitHub Enterprise Server 中存在严重的认证漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520551&idx=2&sn=c7d2ba1175a4c946fe47679b75e3c64e&chksm=ea94a04ddde3295bb0ef7a0d6531fee1957d5a1ffa8ba19cd572a05c40449b1f4706da88b90a&scene=21#wechat_redirect)

[存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=2&sn=acd4b1226ac3021b5aa91433e3f657f5&chksm=ea94bfd0dde336c6a6ba483f21d5d9572e139fb0e5cd5ac1a9ccde95f91e2330823dfbc71c20&scene=21#wechat_redirect)

[GitHub 仓库遭勒索攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519716&idx=1&sn=1cc54c0f43ba988628e656e06eab74eb&chksm=ea94bc8edde335982822ab433cbd0bb58b06de3536826a77abe9d8bcf3fe4fb0693953f6ddc5&scene=21#wechat_redirect)

[GitHub 企业服务器中存在严重漏洞，可导致认证绕过](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519550&idx=1&sn=c9df29fac4cc88482637824b11ada5e4&chksm=ea94bc54dde335421f9f83bbe6ae67441821408144a318140245acf73e69aa18472aa1fc98fc&scene=21#wechat_redirect)

[GitHub 评论被滥用于推送恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519338&idx=3&sn=ce709d5220bb6c2f682b40e739ddb45a&chksm=ea94bd00dde3341689317ffd9ae079e27052fd9394be372945e3ac51a63d809ddd7ba6f7ee53&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/github-comments-abused-to-push-password-stealing-malware-masked-as-fixes/

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