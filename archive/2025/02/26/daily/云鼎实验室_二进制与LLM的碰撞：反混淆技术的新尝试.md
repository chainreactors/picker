---
title: 二进制与LLM的碰撞：反混淆技术的新尝试
url: https://mp.weixin.qq.com/s?__biz=MzU3ODAyMjg4OQ==&mid=2247496250&idx=1&sn=228262a07c64030f35aebe2e4ca78d09&chksm=fd790ebcca0e87aacae9748e6ec23d46321f000cf21db2022f429308c50652f6b70b23a43f19&scene=58&subscene=0#rd
source: 云鼎实验室
date: 2025-02-26
fetch_date: 2025-10-06T20:37:16.087526
---

# 二进制与LLM的碰撞：反混淆技术的新尝试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NNSr7XSrt0liaXAo2DlF3bQHV116MNEcvHsdU9qztrvIBXCveHSicskX0NElt3c2Ly7CBjoAJoESFHCk8Hf8ah3A/0?wx_fmt=jpeg)

# 二进制与LLM的碰撞：反混淆技术的新尝试

云鼎实验室

**0****1**

***前言***

云鼎实验室在长期跟踪安全事件中发现，恶意软件为了逃避安全人员的分析，通常会采用混淆技术来隐藏其真实意图和逻辑。这类样本在分析过程中往往耗时耗力，即使使用相关工具，效果也有限且缺乏通用性。然而，Transformer模型的崛起为这一问题提供了新的解决思路。

Transformer最初是为了提升机器翻译的效果而提出的，后来在此基础上发展出的大型语言模型（LLM）已经能够完成对话、推理等复杂任务。而**混淆技术的本质是通过复杂化原有逻辑来阻碍人脑的推理、“**翻译**”和总结过程**，这类问题恰恰可以通过LLM得到统一解决。

**0****2**

***传统方法与不足***

传统去除混淆方法分为静态和动态，以OLLVM为例[quarkslab et al.,2014]对其做过详细的分析，文中去混淆的方法主要是通过寻找控制平坦化，指令替换，虚假控制流的特征，比如找到控制流平坦化的switch 调度器、虚假控制流的条件等，然后进行模拟执行或者符号执行找出原始代码的逻辑。这类方法的局限性是每个混淆工具都需要找到类似上面的特征，然后进行还原，工程难度大且耗时。

**0****3**

***基于LLM的反混淆***

提炼上述传统去混淆的思路，其基本流程可以概括为以下两步：

* **人工分析并识别混淆特征**；

* **通过符号执行或模拟执行提取原始代码**。

这两步工作可以借助现代大型语言模型（LLM）来实现。当前，LLM 已经具备了自动归纳和简单推理的能力，因此通过大量数据的训练，可以将多种编程语言及其去混淆的方法学习到一个统一的模型中。

逆向工程也是类似的工作，而 LLM 在预训练阶段已经学习了远超单个人类知识的内容，这正好可以弥补从低级语言（如汇编）转换到高级语言（如C）过程中信息缺失的问题。

**0****4**

***领域模型训练***

openai 在gpt3.5 提出了instructGPT 3步训练法：

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo70cyx9qia8iaxdQQtYbyicJrUmkKMic7njbfYfsEGWbKEYiaRWN36Afk2MgQ/640?wx_fmt=png&from=appmsg)

经过我们的测试**对于去混淆的这个任务直接进行第一步SFT即可**。开始SFT训练之前需要生成相关的训练数据。为了或得高质量的混淆数据。我们开发了一个AutoGenerator的工具：

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo7xdKO4jqeibdJEFQAKkRh6ofdYG2XkF23B17DAt2Gq1GmPKBxibRLe8ibA/640?wx_fmt=png&from=appmsg)

使用LD\_PRELOAD 将AutoGenerator注入到编译时候的编译器中，提取原始的编译参数生成.o文件保证构建系统运行正常，然后在根据提取到的编译参数生成未混淆的代码、控制流平坦化、虚假控制流、指令替换的代码，最后去重生成训练需要的函数对各120W总计360W。

**模型在32张A100微调后的效果：**

**输入混淆代码**

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo7b9AKJQONDxD12AQM1ZaolKic2JvyRZf5EEWibGD1V83LoZWmkC9Y492Q/640?wx_fmt=png&from=appmsg)

**模型输出**

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo7hBsZjUVY1OTibicyz9HPeD8iaU3hWVYJWbqaOV2yumlVqu50KW1tnHAeQ/640?wx_fmt=png&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo7ZXpJqWoTOzacibxPFibNA5vaMu1OYcQpCTA01LtmsbHkqGgcTUIV36tQ/640?wx_fmt=png&from=appmsg)

微调后的混元7B                GPT-4

**展开与原始文件比较**

![图片](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdenPgwsTTPu7iaXSkx2lMgZo7oetFndqIwPZXJ1wLicjGS80WMwb4xJDJbopiawqerAngqOpRSd8vnHKg/640?wx_fmt=png&from=appmsg)

微调后的模型使用14组未训练的代码进行初步测试，准确率在90%以上，在这类问题上明显要比GPT的效果好。

**0****5**

***未来与展望***

随着大语言模型（LLM）技术的快速发展，例如DeepSeek通过减少监督微调（SFT）并直接采用强化学习的创新训练方法来降低训练成本，LLM在工程实践中的落地应用正变得越来越近。展望未来，我们期待LLM在去混淆、逆向工程以及CTF（Capture The Flag）等领域的应用前景愈发广阔。这些技术的进步有望降低相关领域的门槛，使更多人能够参与到二进制安全的研究和实践中来。

**0****6**

***参考***

1.【deobfuscation-recovering-an-ollvm-protected-program】Deobfuscation: recovering an OLLVM-protected program - Quarkslab's blog

- END -

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

云鼎实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

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