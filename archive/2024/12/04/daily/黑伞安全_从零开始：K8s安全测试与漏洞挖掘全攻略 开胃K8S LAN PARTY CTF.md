---
title: 从零开始：K8s安全测试与漏洞挖掘全攻略 开胃K8S LAN PARTY CTF
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489531&idx=1&sn=b8aa79a6bb356af80069827d5d8a0075&chksm=fb029aa3cc7513b53bf86447e392a74900ffe3ae568fe7882ce569427a18e8b004883290e12a&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-12-04
fetch_date: 2025-10-06T19:39:19.289380
---

# 从零开始：K8s安全测试与漏洞挖掘全攻略 开胃K8S LAN PARTY CTF

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGpP42WfBo5hTxoaTEtBuXQeiasV5nLva6UNJxicyVKMhbLjTSQYiaPzLVOzXHxLMiacn4A3Z57yFHWr6g/0?wx_fmt=jpeg)

# 从零开始：K8s安全测试与漏洞挖掘全攻略 开胃K8S LAN PARTY CTF

原创

枇杷哥

黑伞安全

大家好，我是Umbrella。最近我入手了一台新的MacBook Pro M4芯片版，使用体验非常棒。利用这台新电脑，我在本地搭建了一些Kubernetes（K8s）环境，并测试了一些之前在云上发现的漏洞。

去年或今年年初的时候，我发现了一个CTF平台，它专注于K8s安全挑战。当时因为访问量过大，导致平台运行很卡。现在情况有所改善，所以我决定在这个平台上进行一些小测试，同时分享一下关于CTF挑战的一些实战经验和科普知识。

首先我们来看看recon这一关。通常，在获取到一个K8s Shell后，你需要判断自己是在容器内、Pod内还是直接在主机上。这可以通过执行简单的命令来实现，比如printenv或者env，查看当前系统的环境变量。如果存在特定的Docker相关文件，也可以帮助你确认是否处于Docker环境中。

这里有个技巧，可以参考一位名叫“hello树先生的作者所写的文章”[快速识别指南：如何判断服务器运行的环境](https://mp.weixin.qq.com/s?__biz=Mzg3NzE4NzgzMA==&mid=2247484908&idx=1&sn=5a977f88e50c18d0c875a7637974fd0c&scene=21#wechat_redirect)，文章中详细介绍了如何识别当前系统环境。稍后我会在评论区分享这篇文章链接，因为它对于实际操作非常有帮助。

接下来，当我们谈论收集K8s环境信息时，会提到CDK工具。CDK能够有效地收集包括环境变量、网络命名空间等在内的关键信息。此外，探测API Server的信息也非常重要，尽管有时可能会遇到权限限制，但通过配置正确的认证信息，如使用kubectl命令，可以帮助绕过这些障碍。

当涉及到DNS服务发现时，我们可以利用DNS请求来扫描内部网络。通过这种方式，你可以找到K8s服务所在的IP地址段，然后尝试访问这些服务以获取更多敏感信息。

在某些情况下，如果你能上传像BusyBox这样的多功能工具到目标系统中，那将大大增加你的探索能力。BusyBox提供了许多有用的命令，即便在受限环境中也能发挥作用。

最后，我想强调的是，这些活动应在合法授权的情况下进行，仅供学习交流之用。希望我的分享对大家有所帮助。感谢收听，别忘了点赞支持哦！

建议大家看一下下一篇文章，来自谷安的广子，提我报名打6折。

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起冲，一起学。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGpP42WfBo5hTxoaTEtBuXQeLUWtmGfA1ic3HbXgu686nVcRvSeiaVWmboVVkiaM9MrVY19LZ9x3e6low/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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