---
title: 基于Craft-anything逆向Themida加壳程序
url: https://mp.weixin.qq.com/s/IzdWmDNHIg-KZuv0GAKxYg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:13:36.420494
---

# 基于Craft-anything逆向Themida加壳程序

# 基于Craft-anything逆向Themida加壳程序

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

服了！！！

一、Themida介绍

Themida 是一款面向 Windows 平台的商业软件保护系统，主要用于防止程序被逆向工程、破解或篡改。它面向软件开发者，尤其适合需要保护核心逻辑、授权机制或防止盗版的商业软件。

### 核心保护技术

Themida 的防护不依赖单一加密，而是组合了多种技术来增加分析难度：

* **代码虚拟化**：这是它的标志性功能。它可以把指定的代码段转换成只有 Themida 自己才能理解的虚拟机指令，让反编译工具无法还原出原始的 x86 汇编逻辑。你可以通过源码宏（如 `#VM_START`）或界面来标记需要虚拟化的函数。
* **反调试与反监控**：内置机制会检测调试器（如 OllyDbg、x64dbg）、内存转储工具或虚拟机环境。一旦发现异常，程序可能会终止运行或触发保护响应。
* **代码混淆与加密**：它会扰乱代码结构、API 调用和资源数据，并在运行时动态解密关键代码段，让静态分析难以入手。API Wrapping 技术会对程序调用的系统 API 做一层包装，加大分析者通过 API 调用关系来理解程序行为的难度。-
* **多版本与授权管理**：Themida 通常与同公司的 WinLicense 协同工作。开发者可以利用其 SDK（支持超过 50 种函数）来实现机器锁定、国家锁定、试用期控制以及自定义注册码生成等授权管理功能。

二、Craft-anything

Craft Anything 是一个开源的“净室”逆向工程与 AI 重建工具。它的核心目标是：让你在**不直接读取目标软件内部代码**的前提下，仅通过观察其外部表现，就能让 AI 编码代理帮你“复刻”出一个功能或外观相似的新版本。

三、正题

1、Craft-anything逆向一个毫无保护的程序时，非常丝滑地完成；

2、我们用最新版的Themida加壳保护了程序。今天，利用Craft-anything来逆向一个用Themida加壳保护的程序，复制其功能。

样本：先用delphi写一个弹窗程序，再用Themida加壳一下。

给出提示词：利用craft-anything-cli.exe对当前目录下的Project1\_protected.exe进行逆向，逆向工具为Tools\Disassemblers\ghidra里工具，可以使用reverse-skill技能。请你复制出它的功能，并用py实现。加壳工具为Themida。

经过漫长地等待。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7dXaEKKDYqlNe3UvXamRDvxTPPhBtxqX6DzSoEfibL0fpUibIbbDgmJIKORibU8zdtfj8EDZ902320lTFZ0P5sUtialPhzWR1JB5o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN40ibbUmtE6rZKBbbQsnibzH7vKcX0p45bibyuhBRTm0Y2xeTXMa3260GOIRAkGMmTwjN1PzbofUC9MbdoSZSc6bgAJUQPWsSBksE/640?wx_fmt=png&from=appmsg)

已经找到了窗体中包含了Button，且有Click行为，但是Click内容是什么没有找出来。并给出了建议：若你希望进一步还原 `Button1Click` 的精确行为，可尝试在反调试较弱的环境下用 Frida 动态 Hook Delphi VCL 的 `TButton.OnClick`——需要时我可继续推进。

3、继续上Frida

继续下指令：“有点正确了，但点击Button1时，没有弹出显示内容。它不是一个空弹窗，是有内容的。可以尝试用Frida来深入到ButtonClick中。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7NQLEBHA0gUiaoAwpF4qBqpge9WGPqA6IstxY7OmsZpH4TdKxMPVvsKljo2fhE4AKv2gD4ibysy0JZGU7OMz9vaCpUgibWSf8tQU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN5qAbbU69W0uKXBf7IJMG3dn5SajbAM7mpb6ibrPibEdpIIoje04zzeicGIvLf8gxw4ROQoXyiaLic6oiar2mFOEb8pu55WlNF3ia4x8Y/640?wx_fmt=png&from=appmsg)

结果出来了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN5icfLyOrZd75dXfibKkwh9xSpkHgHvutVZ5KdNMzQnSDmExS5BVZ3SRMvZWC12HK3XhxlVnbJrhJyeELPK3XZWiaxHGuV36sLCb4/640?wx_fmt=png&from=appmsg)

拿到了ButtonClick的内容：OK!123

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6NnwEvR767qZqiaicIVicUPBjwkL4rYRlZjiaYPxvu4diactyaM4Eb55nR1ic8YIhPCr5IV9hD3iar0DL1EVcHiaDWnP2XYFhWVWEoDibM/640?wx_fmt=png&from=appmsg)

三、总结

对Craft-anything是彻底地服了，这也太强悍了。它联合Ghidra、Reverse-skill、Frida，真的把商业加壳程序Themida给秒了，完美地实现了“复刻”。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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