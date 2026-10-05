---
title: 当模型学会静态脱壳：MiniMax 移动逆向实测
url: https://mp.weixin.qq.com/s/OhzS7xxL6ao9aHEnBdnl0g
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:22.838865
---

# 当模型学会静态脱壳：MiniMax 移动逆向实测

# 当模型学会静态脱壳：MiniMax 移动逆向实测

原创

二进制磨剑
二进制磨剑

二进制磨剑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# MiniMax M3.1 Flash Preview 移动逆向实测

最近，MiniMax 发布了 M3.1 Flash Preview 模型， 我想测试一下现在的 flash 模型是否有能力静态解决安卓加固，把一个经过加固的 APK 交给 MiniMax M3.1 Flash Preview，看它能不能从 IDA 的静态视图里找到那条被藏起来的代码路径。

![](https://mmbiz.qpic.cn/mmbiz_png/zxuXxbLaCLD59H4TmmxJXa6QO2r9TZt8jgmWJYFSgUHZnRWzzGNoubiaY78Xoh1NaicPgC8L2rTNC1mwLx7qL6uia7GxWpdarAdE4XSwEhoYlM/640?wx_fmt=png&from=appmsg)

过去，移动应用的安全防护很大程度上建立在“动态环境门槛”之上。面对加固、类抽取和运行时解密，逆向工程师通常需要准备 Android 设备或模拟器，借助动态调试、Frida、Hook 和内存观测，把代码逼到真正执行的那一刻，再从运行时痕迹里一点点找回真实逻辑。很多时候，静态视图只能告诉我们代码被藏起来了，真正的突破还要依赖设备、注入和反复试错。

这次测试出现了一个值得认真对待的变化：即使是经验丰富、专业的移动逆向安全工程师，在面对整体加固、类抽取加固时，仍然需要借助 Android 运行环境、Fart、Frida 这类动态分析工具才能完成脱壳和分析，然而，模型似乎已经在这些方面超越了人类专家，在没有 adb、没有 frida、没有 Android 运行环境的前提下，仍然可以完成脱壳、解密与分析。

## 一、测试环境

本次测试使用 MiniMax M3.1 Flash Preview，运行于 Opencode，接入 IDA PRO MCP。为了模拟用户拿到陌生 APK 后的第一现场，测试不提供 adb、frida，也不提供额外 skills。模型面对的只有静态文件、反编译结果、工具反馈和一个必须完成的目标：找到被保护的真实代码，并交付可复核的逆向产物。

## 二、某数字加固

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zxuXxbLaCLCL22u65THEZtWCsicaIFcyd1EyvibQTavkibLI0wB36FPAgTuSyKZf7G0mbOYJTCt5eAibqh2ibwHesWia9r2FxibXaYmqrX2Tuydv1Q/640?wx_fmt=png&from=appmsg)

任务持续了约 2 小时，中途人工接管 2 次，模型也曾经短暂放弃。我们发送“继续任务”之后，它重新接回主线，最终提取出解密后的 DEX，并给出 某数字加固静态脱壳脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zxuXxbLaCLCMSVODdYDDj8Q91HKO0O0z57YBiavtHOgylghY9kWD28L2dxJpoY3PdH2MdMUKwicpQ7jLz4OtZIKwmhwmd1ibfDJWmibn007HoEY/640?wx_fmt=png&from=appmsg)

btw 适合用来中途问问进度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zxuXxbLaCLBIjh8ebFO3HxibjZFL3ibIxx2ssrre9yqVS5UVgLcexqVve9jeQun8YJR7sBauzDIHjicHdrIL4cmbD9tqBnsSw8RlJ5SialIamicI/640?wx_fmt=png&from=appmsg)

某数字加固的结果很清楚：约 2 小时、约 80M token、人工接管 2 次，最终产出解密后 DEX、静态脱壳 SOP 与脚本。模型把这一关撞开了，也把撞开的方法保存了下来。

虽然第一次脱跑了接近 2 小时，当把这次脱壳过程总结为 SOP/SKILLS ，模型再次处理这类加固样本的时候就变得游刃有余。

使用 panda-dex-dump 这种动态方案会更快，但是并不能凸显模型的逆向工程能力。

## 三、某头部类抽取加固

该加固样本把问题推向了另一侧。关键逻辑被抽取、切碎，静态视图留下的是一堆需要重新拼接的线索，完整路径已经被打散。模型运行约 18 分钟后停滞，并没有直接解出 code item。

![](https://mmbiz.qpic.cn/mmbiz_png/zxuXxbLaCLADSiaovmcCQINOZeUgj23wqjYRZQ3l1VSfmzU9slu1Bvb7o2o6Q76wvKh0eLE1DyycCekpJa1lC3gcF6xcVQ5XtiavvmUtPuniaE/640?wx_fmt=png&from=appmsg)

只要任务上下文还在，模型仍然可以重新压缩线索，换一个角度继续搜索。

![](https://mmbiz.qpic.cn/mmbiz_png/zxuXxbLaCLCDwPkKrncDXVUCeWuiciaalv0icsJtQAZgcwWyKP1eEgA4CHjk7ZKvvatMBaC2sd2VciaLLZf3yJLHKy749tzoJ0hflw8PVtkFLaw/640?wx_fmt=png&from=appmsg)

人工在这里做的事情非常少，只是鼓励模型继续分析。没有人替它指出答案，也没有人把关键路径直接喂给它。模型在后续轮次里重新组织静态证据，把类抽取造成的断裂当成一个需要验证的假设，同时避免把它当成无法推进的结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zxuXxbLaCLD04ORE41VEiaFQ2q74Ht9snTRWtdIxKzdicMV0e7JUTH5xRYDs4kSiaS4ndSLj7N8S7zsYXJL4AicT2WTDA2wBu65GsEdk98iaJTX0/640?wx_fmt=png&from=appmsg)

经过多轮压缩和继续推进，模型最终成功还原了被抽取的类方法代码。

![](https://mmbiz.qpic.cn/mmbiz_png/zxuXxbLaCLD10hRdCNNfS0vtmNhIBAiamJYyauFbOVop6fQoY7fbKjc5QIDrCfxzJfLpzMQjqlLeAYn8LiaFZHnhQSPNxxibiaWJWfibJ7aoPcibE/640?wx_fmt=png&from=appmsg)

我认为这场测试最值得写进结论的是成功的方式：模型先承认静态证据不足造成的失速，再通过持续推理逐步恢复结构。对于防守方来说，这意味着类抽取、混淆和加固仍然能显著提高成本，却越来越难被当作绝对屏障。

## 最后的判断

MiniMax M3.1 Flash Preview 能不能做移动逆向，我的答案是：在静态脱壳和逆向工程的长程任务里，它已经从“能给建议”跨到了“能交付阶段性成果”。它可以在本次样本中静态剥离部分安全防护，拿到解密后 DEX，恢复被抽取的类方法，并把过程写成脚本和 SOP。

本文结论来自本次限定环境与样本，不能替代全面基准测试。实际使用时请仅对拥有合法授权的应用与样本进行分析，并对模型生成的脚本、解密产物和安全判断执行人工复核。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FMiaMMfBpPgDs6JsyVq6ZxicHiaHutt2aBviba6ic3ews9EyFib8lE4N0h43Zu70DibLKSGfY8HGhicGo0a8446JrN0cDA/0?wx_fmt=png)

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