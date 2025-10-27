---
title: Telegram新型0Day漏洞曝光，将BUG藏在视频传播
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545130&idx=2&sn=6529cd7a31a894ac1c8e19045dc11835&chksm=c1e9bd7bf69e346df12084d426da102894bae3128a5642f422d8e693a5cdbbe6729d2026d436&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-30
fetch_date: 2025-10-06T17:45:29.672991
---

# Telegram新型0Day漏洞曝光，将BUG藏在视频传播

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogurLiaCEWV4T9c3nRMOEU6ciaIfLiccEaSWtTQnqf31tDypKmXqGodwWSOmtcuiaO8kZnOKbGom2eg2qQ/0?wx_fmt=jpeg)

# Telegram新型0Day漏洞曝光，将BUG藏在视频传播

关键基础设施安全应急响应中心

* ESET Research在一个地下论坛上发现了一个针对Android Telegram的零日漏洞广告。
* ESET将该漏洞命名为「EvilVideo」，并将其报告给Telegram，Telegram于7月11日更新了该应用程序。
* EvilVideo允许攻击者发送恶意的有效载荷，这些载荷以视频文件的形式出现在Android的旧Telegram应用程序中。
* 该漏洞仅影响Android Telegram 10.14.4及更早版本。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38lEKqDnU7zEMVLQqdAEF9wNchjp5IMKfFp2cpqTpedKHichZycH1IDOr3iaVUlvz4h4409mdBhjtcw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

近日， ESET研究人员发现了一个针对Android Telegram的零日漏洞，该漏洞名为「EvilVideo」，从今年6月开始在一个地下论坛出售，价格不详。利用该漏洞，攻击者可以通过Telegram频道、群组和聊天共享恶意的Android有效载荷，并使其看起来像是多媒体文件。

「我们在一个地下论坛上发现了出售该漏洞的广告。在帖子中，卖家展示了在公共Telegram频道中测试该漏洞的截图和视频。我们识别出了有问题的频道，漏洞仍然可用，因此我们可以获得有效载荷并自己进行测试，」ESET研究员Lukáš Štefanko解释说。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38lEKqDnU7zEMVLQqdAEF9wABW8QSd1f5TIm00ZzlNJDWO3lCyq1ic4yicu1IUVlVFEoSRJRb5tCbWA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

发布在地下论坛的帖子

ESET Research对该漏洞的分析显示，它影响Telegram 10.14.4及更早版本。原因可能是特定的有效载荷是使用Telegram API制作的，因为它允许开发人员以编程方式将特制的多媒体文件上传到Telegram聊天或频道。该漏洞似乎依赖于攻击者能够创建一个有效载荷，将Android应用显示为多媒体预览，而不是二进制附件。一旦在聊天中分享，恶意有效载荷看起来就像是一个30秒的视频。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38lEKqDnU7zEMVLQqdAEF9w5BpsxlmHic5bzm7sgZPoVHnO3cnf2G81MpK5B92Azib2jrMnWtLQ5uJw/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

漏洞利用的例子

默认情况下，通过Telegram接收的媒体文件设置为自动下载。这意味着启用此选项的用户一旦打开共享的对话，就会自动下载恶意负载。虽然默认的自动下载选项可以手动禁用，但在这种情况下，仍然可以通过点击共享视频的下载按钮下载有效载荷。

如果用户试图播放「视频」，会触发真正的Telegram弹出错误信息：「应用程序无法播放此视频，是否尝试使用外部播放器？」这是在合法的Android Telegram应用程序源代码中发现的原始Telegram警告，而不是由恶意负载设计和推送的。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38lEKqDnU7zEMVLQqdAEF9wbGeJPRvTLK3dKyYSUyibKibx9heNSic3nicOJcIbWibOKZ3piaJNBekUcVRQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

警告无法播放「视频」

用户可以选择取消或尝试打开文件。但如果用户选择「打开」，他们还需要允许Telegram安装Android应用程序包（APK）。在安装之前，Telegram会要求用户启用未知应用程序的安装。因此，用户需要执行一系列操作才能激活恶意载荷，但伪装的文件和Telegram的错误分类仍然引起了明显的安全担忧。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38lEKqDnU7zEMVLQqdAEF9wkIibvTBxCuN128DdO2pGCBvpjkXgRXpCnvMLE5rakefDd2UGJBcJsHQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Telegram要求用户允许安装未知的应用程序

在2024年6月26日发现EvilVideo漏洞后，ESET按照协调的披露政策向Telegram报告了该漏洞，但当时没有收到任何回应。7月4日，ESET再次报告了这个漏洞，当天，Telegram联系了ESET，确认其团队正在调查EvilVideo。随后，Telegam修复了这个问题，于7月11日发布了10.14.5版本。该漏洞影响到10.14.4之前的所有版本的Android Telegram，已在10.14.5版本中更新。

**参考资料：**

https://www.eset.com/uk/about/newsroom/press-releases/set-research-discovers-evilvideo-telegram-app-for-android-targeted-by-zero-day-exploit-sending-malicious-videos/

https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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