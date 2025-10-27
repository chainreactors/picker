---
title: 安全研究员强调，已删除的GitHub数据仍可被访问
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458565034&idx=2&sn=89488491977b474f61606489d3272e75&chksm=b18d892086fa00366b1af372eb190cb1753a7680aafb17268445e3526f138df0b2e419b3c975&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-27
fetch_date: 2025-10-06T17:43:04.247466
---

# 安全研究员强调，已删除的GitHub数据仍可被访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9mVZG534W4cP54e59D3UBToUVL2kKaO9QlLunqD3PKicgzLChdnvl8aw/0?wx_fmt=jpeg)

# 安全研究员强调，已删除的GitHub数据仍可被访问

看雪学苑

看雪学苑

近日，Truffle Security的研究人员再次强调，已删除的GitHub存储库（公共或私有）以及已删除的存储库副本（分叉）中的数据不一定真会被删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9Z7moz7b71ZYPXMf0JkG3hOiaDskl1TbicwnhNCmHm9D2cUM0DVXKTI7Q/640?wx_fmt=png&from=appmsg)

该机构的安全研究员Joe Leon在周三的一份公告中表示，这种情况是在上周向一家大型科技公司提交一份严重漏洞报告时发现的，该报告涉及员工GitHub 帐户的私钥（该帐户在整个组织中拥有广泛的访问权限），该密钥已公开提交到GitHub存储库。

意识到这一点后，该公司立即删除了存储库。但由于它已被分叉，Leon仍然可以通过分叉访问包含敏感数据的提交，尽管该分叉从未与原始上游存储库同步。Leon还补充说，在审查了来自大型AI公司的三个广泛分叉的公共存储库后，Truffle Security研究人员从已删除的分叉中发现了 40 个有效的API密钥。

Truffle Security联合创始人兼首席执行官Dylan Ayrey解释说，这个问题归根结底是由于所谓的“悬空提交”(dangling commit) 造成的。git 提交捕获存储库在特定时间点的状态快照，包括对代码和数据的更改。每个提交都由加密哈希唯一标识。例如，删除分支会删除对特定提交链的引用，但提交本身不会从存储库的对象数据库中删除。

Ayrey 表示，即使与代码树的连接被切断，如果有直接访问它们的标识符，则仍然可以下载相关数据。例如，以TruffleHog 存储库中的此提交作为示范：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm931Ymd0EDkohY5WKnSBjB1MJC2lSCYZY8TtyNdwficv03GSMJA6NgFyg/640?wx_fmt=png&from=appmsg)

要访问此提交，用户通常会访问包含完整 SHA-1 提交哈希的 URL：https://github.com/trufflesecurity/trufflehog/commit/07f01e8337c1073d2c45bb12d688170fcd44c637

但实际上用户并不需要知道整个 32 个字符的 SHA-1 值。提交哈希可以通过 GitHub 的 UI 进行暴力破解，特别是因为git 协议允许在引用提交时使用短 SHA-1 值。短 SHA-1 值是避免与另一个提交哈希发生冲突所需的最小字符数，绝对最小值为 4。所有 4 个字符 SHA-1 值的密钥空间为 65536 (16^4)。暴力破解所有可能的值可以相对容易地实现。

Truffle Security最后从中得出了如下结论：

① 只要一个分叉存在，对该存储库网络的任何提交（即上游存储库或下游分叉上的提交）都将永远存在。

② 安全修复公共 GitHub 存储库上泄露的密钥的唯一方法是通过密钥轮换。

③ GitHub 的存储库架构决定了其必然存在此缺陷，不幸的是，许多GitHub用户不理解存储库网络的实际工作原理，并且会因此而降低安全性。

编辑：左右里

资讯来源：Truffle Security

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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