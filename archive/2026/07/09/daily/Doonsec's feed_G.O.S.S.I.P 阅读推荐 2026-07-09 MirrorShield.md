---
title: G.O.S.S.I.P 阅读推荐 2026-07-09 MirrorShield
url: https://mp.weixin.qq.com/s/RnLS_DwWQPUuY5TTK-gGFA
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:54:48.469886
---

# G.O.S.S.I.P 阅读推荐 2026-07-09 MirrorShield

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mibiaYcMd6pdT8KPP97SLca2v4RsndNT1K6FTFrb1QMMicryPXolcbR9DjgLibm1icJ3VcUPFtzSiapuYvw3hlOum1BaQj0uu2YEtvSIDUXYhXjI/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-07-09 MirrorShield

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

来自课程大作业的最佳论文！

以下文章来源于COMPASS Lab
，作者zzh

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5AnfZSQmFEHc22KX7QV8ThTIiaePSXxS5BBusLp4ke6rw/0)

**COMPASS Lab**
.

COMPASS (COMPuter And Systems Security) lab pursues cutting-edge research in systems security (compass.sustech.edu.cn).

近日，南方科技大学计算机科学与工程系 COMPASS 实验室在 Linux 恶意软件分析方向取得进展：论文 "MirrorShield: Cross-Architecture Linux Malware Analysis via Lightweight Emulation and LLM" 被国际入侵检测、恶意软件与漏洞评估会议 DIMVA 2026录用，并获会议唯一一篇**最佳论文奖**。论文第一作者为本科生张子涵，作者还包括林闻起、孙凌娜、汪泓毅等，由张锋巍教授担任通讯作者。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4mibiaYcMd6pdw8vNQiaiakFhoh6yrsRqvhvFiasg0m5mrBFeHncSA2tl1ln7RfWJiaiap2apF08VRG90c0wzVmZP4oXZBV0dL9zdLibNQ9USfePhO8/640?wx_fmt=jpeg&from=appmsg)

会议主席为同学们颁发奖状，从左到右分别是实验室成员：孙凌娜，张子涵，汪泓毅

值得一提的是，这是一项"从课堂走向最佳论文"的工作：团队成员在南科大 CS315《计算机安全》课程中提出最初的构想并将其发展为完整系统，并在课程结束后持续扩展与打磨，完成了这篇论文，并荣获最佳论文奖。

![](https://mmbiz.qpic.cn/mmbiz_png/4mibiaYcMd6pcxN9Q0Ng7WUUIlmAI31qctYm7J2mKaNWNjPlqbWXpN8AuxSgTxk7OOTibo5EbZ1a9ibM7JFNEpXgUyg1u7ibKVG24xspXFr7BkHA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mibiaYcMd6pdicF8byVOibiaU4KMbVRrvzwsibaiaJHrzeMzicUfNujQOJyXLV424qbvuP4mbW9Xpo0cuoJgicubAst9H6PzESFRINnCciaMJuWRCvC4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/4mibiaYcMd6pelfWJSO50xENs6wZSW3gdx3Vu9tbKiaDZ7XNbJJGZvpbpz9qibKnxVLq2EPSc1NRA7H0fKicZcy87bw6Q3hOPQVpCAibOIuyQLLRM/640?wx_fmt=png&from=appmsg)

**01**

**背景与动机**

恶意软件的重心正在从 Windows 转向 Linux 操作系统。累计样本量已突破 15 亿并持续攀升，而攻击目标进一步碎片化到 ARM、MIPS、RISC-V 等多种 CPU 架构。**恶意样本都会被编译成不同的架构的样本，给检测系统的兼容性带来了挑战。**

动态分析主要涉及两个核心环节。一是把样本运行起来（静态分析只能看到代码，动态分析必须在目标架构上执行样本）。二是对收集到的日志进行深入分析，检测样本是否存在恶意行为。

![](https://mmbiz.qpic.cn/mmbiz_png/4mibiaYcMd6pdicQ2myicaVutDYFyMRWGEr3Z62pRA0sfic6OAJo5GO6ibHOyQYkVR1vh1Favw8FW6Uumkk9YGgpriczMsO9vs77AltHEPggTK3KlY/640?wx_fmt=png&from=appmsg)

现有方案恰恰在这两点之间被迫取舍，一条轻量、可复现、可审计的跨架构取证路径始终缺失。

**02**

**系统设计**

镜鉴系统的样本行为收集与检测系统都运行在单台 x86 主机上，串联了四个阶段。执行层先将异构架构的执行命令重定向到预先固定的指令翻译器，Docker 提供目标用户态环境与资源隔离，eBPF 程序挂载在宿主机内核上，记录容器内的系统调用事件。这一组合避开了完整 VM 的启动开销，同时监控点位于内核层，更难被样本规避。最后，将系统收集到的日志进行多轮去噪，压缩和初步检测后，利用大语言模型，进行进一步的判断和分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mibiaYcMd6pfGPwiaFiadSGvTupLSmrftBiazGWnv3IyG0PJv6Tj0MIrN7woBjyR04Qxacgg0SrQVhDpoa2QXb5EhXIa0vqkibibSzRfa2w4D4aDg/640?wx_fmt=png&from=appmsg)

为了获得更精准，可审计的分析报告，我们采用了大语言模型来根据系统调用重建样本的行为，分析其中的恶意行为链。由于大语言模型的上下文有限，而真正的恶意信号往往被良性噪声淹没在上下文中，对原始日志的多层去噪和压缩是这项工作着重解决的问题。因此整个系统分为执行、采集、裁剪三步，让日志中的行为信号密度最大化。同时，我们设计了20 个带时序状态的分析器，持续匹配一些基础的攻击模式，产出告警。从而进一步把 LLM 的注意力钉在攻击行为上。

![](https://mmbiz.qpic.cn/mmbiz_png/4mibiaYcMd6peT7mmhzXialpJ9TWCtJd9SA9dWg5JFHT963K3TAfiaDjSNRuBIIqPib1ayWtxuYVWXX35GHYm0TbKw7nyx6XgfWm9CnnQ6fNf7yc/640?wx_fmt=png&from=appmsg)

**03**

**实验结果**

**案例研究**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mibiaYcMd6pcNibWBEBal7QZtyqG0096ibkR9QicHDKsKXLaSpqXOu91GIwQ0G80q9Ph83Nec5S7APd2xXXUhNAVChoFxQiaCHxSHSQWSTAibQgbQ/640?wx_fmt=png&from=appmsg)

一个运行早期即崩溃的恶意软件直观展示了系统间的差距，镜鉴系统凭借崩溃前捕获的 syscalls 重建出攻击链，相较于其他分析软件，并给出了更加准确，详细的报告。

**实验评估**

基于一个平衡数据集：844 个恶意样本与 844 个良性 ELF 二进制（覆盖11种架构）。在完全相同的日志与提示词下，四个大语言模型全部落在 91.6%–94.7% 区间。

我们的核心结论是：在恶意软件分析时，输入证据的质量决定了LLM 推理的可靠性。

![](https://mmbiz.qpic.cn/mmbiz_png/4mibiaYcMd6pexHnlOicsEdEetWzQRGTfV5P0vtIxYW2Wb4wsich6qpumzrC9k5pic47NZXHhI6dctj9xLG1jjxTs6yQPOSRLZ4fg0WwNWkPHlEs/640?wx_fmt=png&from=appmsg)

同时，镜鉴系统具有以下优势：

* 跨 11 种 ISA 稳定：主流架构 92.4%–94.5%，长尾架构（RISC-V、PowerPC、SPARC 等）89.3%–100%。
* 抗噪声：注入至恶意行为 2000 倍的背景噪声后，检测率仍高于 90%，采样机制天然为 LLM 输入设置了上限。
* 可审计：评估显示，81.4%–95.0% 的报告关键论断能够逐条对应到原始 trace 记录，输出的不只是判定，而是可复核的取证对象。
* 轻量：单次 syscall 开销仅 4.4倍（QEMU 全系统模拟+ strace 高达 6063 倍），每 100 个样本的 LLM 分析成本约0.29 美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mibiaYcMd6pdjkT0Licw8KicRsw1Wjze4zLe0RVNbYAbvwqNKVmVTV1icI7fPzwSBITan5aMUDfzYiankjibxt8rq8bFyVuXaYUBJBte3KYp4kWIg/640?wx_fmt=png&from=appmsg)

**04**

**结论**

本文提出了 MirrorShield（镜鉴），一种轻量级的跨架构 Linux 恶意软件分析框架。通过将容器化，用户态模拟与 eBPF 内核监控相结合，该系统在可扩展性与基于证据的解释之间取得了平衡。实验结果表明，系统在多种架构上均具有高准确率与鲁棒性，且四个 大语言模型在相同证据和提示下表现相近，说明分析质量主要由输入的结构化证据驱动，而非模型选择。此外，即使执行不完整，系统仍能捕获足够的行为特征进行可靠分析，并提取出跨恶意软件家族的可复用行为指纹。这些发现表明，跨架构恶意软件分析完全可以在轻量化的前提下实现可靠检测。

论文地址：https://www.xxbai.space/files/MirrorShield.pdf

仓库：https://github.com/shentoumengxin/MirrorShield

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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