---
title: 金蝶OA-SQL&任意文件下载
url: https://mp.weixin.qq.com/s/m1B1xS7fGxeH44bYnZMavQ
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:26:40.713775
---

# 金蝶OA-SQL&任意文件下载

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEFia7Y75OrsribWSJIDaJXjWUVIAkWsNfkQIiatujia6Dg53fybppKaIMticyufymlicKibpHuicdFDsNiaibmw/0?wx_fmt=jpeg)

# 金蝶OA-SQL&任意文件下载

原创

SharkSec
SharkSec

SharkSec

![]()

在小说阅读器中沉浸阅读

🔔 **温馨提示**：为了防止走散，不错过每一篇干货内容，请记得将公众号设置为**星标**！🌟

![图片](https://mmbiz.qpic.cn/mmbiz_png/cr9YyS063QrVstianyX9gPA4EZicfkbyKdBQyPtQHPwSLJePicuZmXcBiaLaRSTWrY6UibPpAaeNxLjOSiaeHaSvdHMg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/CGEwnc7DGPkXwCkjLX8HzCgjKO1KuxPTWw8L9BNNTM3b8WVfHQxV3vIibDycqksck67KWnnVu75ctUZFfpde2kw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=gif&tp=webp#imgIndex=1)

【声明】本文所有POC仅用于合法安全测试，严禁在未获得明确授权的情况下对任何系统进行测试。擅自测试所引发的一切后果，由操作者自行承担全部法律责任，作者及团队不承担任何连带责任。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gFxQW0ZLIfNepCJZUicnBrw4fE1YN4dWcVLTlk9Sg3Z7GQQB6NicXCzc7r99xcmBQNKzF0GFFnd0kUuibbGSnABnw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

引     言

近期项目上有点忙，没太多时间，利用工作间隙，再次对金蝶oa做了次审计，并发现了多处安全漏洞。其中部分漏洞的利用条件较为苛刻，对特定环境和权限有严格要求，导致其在真实攻击场景下的可利用性有限。

tips：这套源码中有水洞也有高利用的洞，接口可提供参考。通常，高利用漏洞的发现，其思路衍生于对基础性漏洞的深入分析与理解。

1

**SSRF**

攻击者可利用SSRF端口探测，目标端口开放时，请求会因连接被挂起而长时间无响应；若端口未开放或命中数据库监听，连接会立即被拒绝或完成握手，响应瞬间返回。

![](https://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEFia7Y75OrsribWSJIDaJXjWU4DCKr4m15iaaeM8VWepVVhnIBmVOFNPc3kbiaPh0mDA5o12TY9wJSPDQ/640?wx_fmt=png&from=appmsg)

2

**SQL注入**

![](https://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEFia7Y75OrsribWSJIDaJXjWU7cqr1iafeKBbm5zXpiaY4JncZNCwQiaHwDeJo8rMce6ELKykzkC2WsuFw/640?wx_fmt=png&from=appmsg)

3

**任意文件下载**

前提：需要开启安全阅读器选项

![](https://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEFia7Y75OrsribWSJIDaJXjWUP5WRUqTlRYBwR5icl6xW4GJzvsWcg8y3J27kLWu9DiaicgyN6TE2zqDRw/640?wx_fmt=png&from=appmsg)

上述漏洞详情及审计过程整理后直接上传纷传，感兴趣的师傅可以直接在纷传获取。

如果大家对我们的文章技术有什么建议或者工具使用上的反馈，都欢迎大家在评论区留言交流。对我们分享的文章感兴趣，想要深入探讨、交流并学习更多相关内容，也欢迎各位师傅加入官方技术交流群!!!（关注公众号，点击菜单栏：联系我们->技术交流群，添加管理员微信，备注【加群】，拉您进群）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/66Px0lScLmhsSQ81eCsVKJ3rdZkSvWiajhKcPGVl5T8wjtDrfJwp0JOA6IpdLIBVawKV3q1zsXaOP95lR6Gm0zg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/IEccNBf01KhlXSXZveRicx71HjXRoxf4N3auzMP8luVj3eupK7xS0R7jcBiaWXicawKPpLiamx4icOURtlgUdGjaVSQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

加入圈子，一起进阶！

我们圈子已平稳运营一段时间啦，后续也会持续为大家输送高质量的实战资源：有一线团队的一手攻防经验、私有工具源码（包括咱们公众号发的工具，圈子里能直接拿源码 + 持续迭代），还有漏洞挖掘的 POC/EXP、每月不定期 0day 分享，hw实战攻防遇见高频oa/设备源码都能在这拿到。

对了，圈子里还有些「刚需资源」：FOFA 的 Key 长期能用，Cursor Pro 共享账号登了就能用； 企业 SRC 案例、红队实战经验也会拆解着讲。

现在圈子**现价 129 / 人**，等满 200 人就涨到 150/人 了 —— 入了圈子还能进专属内部群，比咱们公开交流群的资源更新更实时、讨论也更深度。

纷传和知识星球内容是同步的，后期主要运营纷传，所以想进圈子的朋友直接扫描下方二维码就可以啦~

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEGGxGv2s7a5wWickpmEYwNB5WZoIovb1o5WvXx0qCpRweeialWwsvQNkzJwgMPqjVJ7S6cS2YNo06cw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

结束

👉 点击关注不迷路，一起潜入深水区，突破边界，共同精进！🚀

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

SharkSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

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