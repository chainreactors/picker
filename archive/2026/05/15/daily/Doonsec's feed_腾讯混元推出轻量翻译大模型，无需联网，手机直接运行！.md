---
title: 腾讯混元推出轻量翻译大模型，无需联网，手机直接运行！
url: https://mp.weixin.qq.com/s/IeI8zD8YmCON0BN0YCMu1Q
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:11:31.929705
---

# 腾讯混元推出轻量翻译大模型，无需联网，手机直接运行！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KVER9adz907EKeqSHpm6AcsysWCU4rDmpuvpPWsic368X03BPJtemBO5CruTINJguWFkpHvicicoWfVpVyZEdOIgPqibVoibSmWcictM3YmT0WOias/0?wx_fmt=jpeg)

# 腾讯混元推出轻量翻译大模型，无需联网，手机直接运行！

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

你可能用过各种翻译工具，但是大部分的应用，如果要实现好的翻译效果都有一个共同的条件：必须联网。

设想一下：

你在异国自驾，警笛声骤然响起。还没回过神，警察就在窗边用陌生的语言严厉发问。你心跳漏了半拍：是我违章了？还是前面出了什么大事？你手忙脚乱地掏出手机想翻译询问一下，偏偏此时没信号，屏幕上转圈的界面简直让人绝望。到底发生了什么？我应该挪车，下车还是掉头？

在这关键时刻，翻译软件掉链子真的让人绝望。

针对这些难题，腾讯混元团队带来了一份硬核解决方案。

最近，腾讯混元推出极致量化压缩版本翻译模型 Hy-MT1.5-1.8B-1.25bit，把支持 33 种语言的翻译大模型压缩至 440MB，无需联网，下载即可直接在手机本地运行，翻译质量优于谷歌翻译。

来看看这个演示，翻译速度真的很快，质量也很好：

![](https://mmbiz.qpic.cn/mmbiz_gif/7avdgR0YVzJcAfpjnE7akiahmpFm2p1We4DSxjonRXtUedeKjuXiauAyHBLYIqATZp9123YibrOExy1hhbxQeChYgXlCetKe7yWJzFibKzPsicu4/640?wx_fmt=gif&from=appmsg#imgIndex=0)

演示设备：高通骁龙 865，8GB内存

**基于混元翻译大模型Hy-MT1.5打造，翻译效果比肩商用翻译模型**

Hy-MT1.5 是腾讯混元团队打造的专业翻译大模型，原生支持 33 种语言、5 种方言/民汉及 1056 个翻译方向。从常见的中英互译，到法语、日语、阿拉伯语、俄语，甚至藏语、蒙古语等少数民族语言，它都能游刃有余地处理。

仅以 1.8B 参数量，Hy-MT1.5 实现了比肩商业翻译 API 和 235B 级大模型的翻译效果 。在严格的评测基准中，其翻译质量不仅超越了谷歌翻译等主流系统，更证明了在高效优化下，轻量级模型能够迸发出令人印象深刻的翻译能力。

![](https://mmbiz.qpic.cn/mmbiz_png/7avdgR0YVzKO0t9mTJdfkkovzJTlibpNQIPiaKgfiagFcQ0xnnvYrDAZKHsLcFbxXxwlxefaJanWb5JgX2HibqmARmUBjctQibSoUfOYWzQQdN6c/640?wx_fmt=png&from=appmsg#imgIndex=1)

Hy-MT1.5-1.8B翻译效果评分，详情见文末链接「Hy-MT1.5技术报告」

但问题来了：原始的 1.8B 模型即使在 FP16 精度下，依然占用 3.3GB 内存。对于手机上金子般的内存来说，依然太大、太慢，所以需要量化压缩。

**最极致的量化压缩，把模型装进手机**

量化压缩，简单来说就是：把模型里原本用16位数字(16-bit)表示的参数转用更低位数字储存。这就像把一幅高清照片压缩成缩略图，文件小了很多，但你还是能看清楚里面的内容。 针对不同的手机用户，腾讯特别推出了2-bit 与 1.25-bit 两种极致的量化压缩方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7avdgR0YVzKbxmq4ib8nLACxnbTqFIG5jhVKBhicYfW4DUA6sorUDwWuP1mJwLWxGHVfBmZ9LYoeuOs033E90nsCdlkKuZqF3lQ6zrib45z4L0/640?wx_fmt=png&from=appmsg#imgIndex=2)

不同大小的模型在FLORES-200中外互译的效果评分

### 2-bit模型：性能与质量的平衡（适用：中高端机型）

###

2-bit 模型采用了业内顶尖的拉伸弹性量化（SEQ），将模型参数量化至{-1.5，-0.5，0.5，1.5}，并结合量化感知蒸馏，在将模型体积压缩至 574MB 的同时，实现了几乎无损的翻译质量，效果超越上百GB的大模型。在支持 Arm SME2 技术的移动设备上，2-bit 模型能够实现更快速、更高效的推理。

![](https://mmbiz.qpic.cn/mmbiz_gif/7avdgR0YVzLicH4gLiaDLVS9IDcjPD5JBTg3jeTCXFbEDAkmia29qSHXQj8xL2MNIGgr7ZeoCK0AKbDsNbcz0hHGskMCdan2E02ZxHQicicAmBXk/640?wx_fmt=gif&from=appmsg#imgIndex=3)

2-bit模型在SME2及Neon内核的速度对比演示

### 1.25-bit模型：Sherry 极致压缩（适用：全系机型）

###

为了达成极致的轻量化，腾讯推出了基于 Sherry（稀疏高效三值量化） 技术的 1.25-bit 模型。该技术方案已经被NLP顶级学术会议ACL 2026录用。

链接：https://arxiv.org/abs/2601.07892

Sherry 压缩方案的核心逻辑在于“细粒度稀疏”策略：每4个模型参数，3个最重要的用 1-bit 储存，1个用0储存，平均每个参数仅需 1.25-bit。

![](https://mmbiz.qpic.cn/mmbiz_png/7avdgR0YVzIKpDngGHWBRJ1ExdDhBrxsutHDmKtViajp40q3C1ic75EBCh4M7M6ImfFTV8sG0vNCQmK3dCLr1Es9cWrhHYHuNy3w3l90PMAu4/640?wx_fmt=png&from=appmsg#imgIndex=4)

配合腾讯专门为手机 CPU 设计的 STQ内核，该方案实现了对 SIMD 指令集的完美适配。最终，3.3GB 的原始模型被进一步压缩至 440MB，轻松常驻后台，让内存紧张的普通手机也能顺滑进行高质量离线翻译。

![](https://mmbiz.qpic.cn/mmbiz_gif/7avdgR0YVzI6wQQnG94vtoHm3CWH5At3cJmHbfJfUYqoickuFxQzQycUARUqo7ltFQItlODoENfCxjbQxsx7T8SXUGkQAGQiaKdnGzXpjSR4s/640?wx_fmt=gif&from=appmsg#imgIndex=5)

FP16(八倍速)vs.1.25bit速度对比，演示设备：高通骁龙888， 8GB内存

**实际体验：全离线、零成本、零隐私暴露**

本次开源不仅包含模型权重，我们还特别制作了一个实际可用的腾讯混元翻译Demo版，特别适配了“后台取词模式”。无论是在本地查看邮件还是浏览网页，混元翻译都能随叫随到。无需网络，无需订阅，完全本地处理、不涉及个人信息的采集和上传，一次下载永久使用！

![](https://mmbiz.qpic.cn/mmbiz_gif/7avdgR0YVzJcKQMv9AkavBS5OUY9jgZCa1ichR1CFvkYMxpYmwyHDQ3vFfq3hsxdJ4WlYgdLCO7ZoL5G8icN2XnJhtiaa9Q15Ria3oBVfjwacsE/640?wx_fmt=gif&from=appmsg#imgIndex=6)

演示设备：高通骁龙7+gen2，16GB内存

**立即体验**

所有的模型权重、代码及技术报告均已全面开源。（暂时只支持安卓体验demo， 后续正式版会添加对IOS等平台的支持。）

体验链接：

* Huggingface（海外用户）:https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-1.25bit-GGUF/resolve/main/Hy-MT-demo.apk
* 魔搭社区（国内用户）：https://modelscope.cn/models/AngelSlim/Hy-MT1.5-1.8B-1.25bit-GGUF/resolve/master/Hy-MT-demo.apk

模型下载

1、Huggingface（海外用户）：

* 2-bit模型权重：https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-2bit
* 2-bit 模型gguf：https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-2bit-GGUF
* 1.25-bit模型权重：https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-1.25bit
* 1.25-bit 模型gguf：https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-1.25bit-GGUF

2、魔搭社区（国内用户）：

* 2-bit 模型权重：https://modelscope.cn/models/AngelSlim/Hy-MT1.5-1.8B-2bit
* 2-bit 模型gguf：https://modelscope.cn/models/AngelSlim/Hy-MT1.5-1.8B-2bit-GGUF
* 1.25-bit 模型权重：https://modelscope.cn/models/AngelSlim/Hy-MT1.5-1.8B-1.25bit
* 1.25-bit 模型gguf：https://modelscope.cn/models/AngelSlim/Hy-MT1.5-1.8B-1.25bit-GGUF

3、技术报告：

* Sherry论文地址：https://arxiv.org/abs/2601.07892
* AngelSlim 技术报告：https://arxiv.org/abs/2602.21233
* Hy-MT1.5技术报告：https://arxiv.org/abs/2512.24092

4、代码仓库：

* AngelSlim: https://github.com/tencent/AngelSlim

欢迎下载体验，分享你的使用感受~

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYjZ7Hx6Udjjk2BGLzC9ahJq7ibxDd1RGA0c9NYZc1husEsvb3tY4FcWPQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj5q5PQEOc5ibURPb03vnRibrxC3UR8xzdyATfiawTYRV2vJvBnAIcE1FeQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

腾讯技术工程

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

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