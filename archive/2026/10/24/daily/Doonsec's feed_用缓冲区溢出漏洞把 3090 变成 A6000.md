---
title: 用缓冲区溢出漏洞把 3090 变成 A6000
url: https://mp.weixin.qq.com/s/wkiF7Mu9nsZUYztqKVRm3Q
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:43.765444
---

# 用缓冲区溢出漏洞把 3090 变成 A6000

# 用缓冲区溢出漏洞把 3090 变成 A6000

原创

tombkeeper
tombkeeper

皮相

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/gsQYvp3Le7WOMicmzsnZABSj5ia9IJdT1VueX9tF4Y7Dc8B8x5c3qKlPNho3ebPFLV9Hp36iahz4t2sIcvKXB82q8hdmGQUr3y0NJCbm5csEoo/640?wx_fmt=png&from=appmsg)

2020 年底，英伟达先后发布了用于游戏的 RTX 30 系列显卡和用于专业计算的 RTX A6000。

很快有人注意到，虽然 RTX 30 系列和 RTX A6000 的核心都是 GA102 芯片，但相对于 RTX A6000，RTX 30 系列的混合精度模式的峰值吞吐被砍掉了一半。

英伟达的 GA102 架构技术白皮书里明确指出：RTX 3090 在 FP16 输入下，累加精度从 FP16 改为 FP32 时，稠密 Tensor Core 峰值吞吐从 142 TFLOPS 降为 71 TFLOPS，稀疏计算的对应吞吐也从 284 降为 142 TFLOPS。但是 RTX A6000 在这两种模式下都是 154.8 TFLOPS，保持不变。

混合精度模式常用于 AI 训练和推理中的矩阵乘法、全连接层和卷积，但对游戏性能影响较小。所以英伟达对 RTX 30 系列砍上一刀，确保游戏卡只用来打游戏，也是可以理解的。

之后有人对比分析了 RTX A6000 和 RTX 30 系列显卡，发现对混合精度模式的限制是通过熔丝 FUSE\_SS\_FMLA32 实现的，设为 1 就会限制，设为 0 就不限制。

你们还记得几个月前我在[用缓冲区溢出漏洞把矿卡变成 A100](https://mp.weixin.qq.com/s?__biz=MzI0NDA5MDYyNA==&mid=2648257342&idx=1&sn=dfb0ede540af1cb3a4b311414e6537a0&token=1116931419&lang=zh_CN&scene=21#wechat_redirect)中提到的矿卡 CMP 17HX 吗？那也是这样被限制的。

于是，硬件社区基于之前对 CMP 17HX 的破解研究，终于也实现了对 RTX 30 系列卡的性能解锁：github.com/Zagitta/gpu-unlock。这个项目同样使用 SEC2 Booter 签名 DMA 溢出漏洞，把 RTX 30 系列显卡的混合精度的吞吐性能恢复到了全速。

在对 RTX 3090 Ti 的性能测试中，解锁前后都采用 450W 功耗上限，做大矩阵乘法并使用 FP32 累加：BF16 输入的算力从 87.50 提高到 157.41 TFLOPS，增加约 80%；TF32 从 42.58 提高到 82.61 TFLOPS，增加约 94%；FP16 也增加了约 35%。

考虑到本来 RTX 3090 就能改成 48G，现在又解锁了性能，就很接近 RTX A6000了。

不过，对于模型推理来说，单并发解码性能的瓶颈是显存的速度，所以 RTX 30 系列显卡即使解锁了性能，在单并发下解码的 tok/s 能也没太大变化，但预填充和多并发的总吞吐则能有约 30% 的提升。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iceZAzI9Y5ntjUN7voRbnCx4S0icGULCtIYicDyhibOcEFoP8SEXMnsMDVYM0sC0zgPjCuRE1ibibEFDeReI8E2GzYicg/0?wx_fmt=png)

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