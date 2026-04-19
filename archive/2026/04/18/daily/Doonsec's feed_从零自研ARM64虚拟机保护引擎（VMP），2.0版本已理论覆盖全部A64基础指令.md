---
title: 从零自研ARM64虚拟机保护引擎（VMP），2.0版本已理论覆盖全部A64基础指令
url: https://mp.weixin.qq.com/s/ZaN5juk51pnd9rAu_wINxg
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:49.894068
---

# 从零自研ARM64虚拟机保护引擎（VMP），2.0版本已理论覆盖全部A64基础指令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3FXEym65cAeU0Xop70bZf5E2RaKrnXQeAqf0vibYMS5pU8NyrQfIqeNqoqVFOvNsEL0ibXP9rnPa4OmRIIEF13Nx6Uib7h5akbrg/0?wx_fmt=jpeg)

# 从零自研ARM64虚拟机保护引擎（VMP），2.0版本已理论覆盖全部A64基础指令

LeoChen..
LeoChen..

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

分享一个我最近开源的项目**VMPacker**—— 一套完整的 ARM64 Linux ELF 虚拟机代码保护系统。

不同于动辄数万的商业 VMP 方案，这个项目**完全开源**适合学习和研究 VMP 保护的底层实现原理。

2.0 里程碑：121 条 ARM64 指令全覆盖

经过两天的深度适配，**2.0 版本总算理论覆盖了所有 ARM64 A64 基础指令集——共 121 条**，涵盖：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1icmvG55CpWU8c4NfpIicoAmV2WJicTC1eyObLdcjHhV6b40iazib56jMPoUhAnML9qsFf103mvgdsibZp3cSeRq6ichG7krAr8MohZY/640?wx_fmt=png&from=appmsg)

这意味着**绝大多数用 C/C++ 编译出的 ARM64 函数都可以被直接保护**，不再因为"不支持的指令"而中断。

**研究初衷**

最初做项目时，仅通过 UPX 魔改加固，防护效果极差，程序频繁被破解，让我束手无策。

后来在网上寻找**ARM64 架构的开源 VMP 虚拟化保护方案**，却发现几乎没有成熟可用的项目（付费方案又动辄数万）。

于是我决定**从零自研**一套 ARM64 指令级虚拟化保护引擎，最终才有了 VMPacker —— 专注于从根源上提升程序的抗逆向、防破解能力。

**技术架构**

整个系统分为三个核心模块：

**1. 指令解码器（Go）**

* 基于 ARM Architecture Reference Manual 的 table-driven 模式匹配
* 支持 DP-IMM / DP-REG / Branch / Load-Store 四大指令族
* 解码结果为统一的中间表示（IR）

**2. 字节码翻译器（Go）**

* 将 ARM64 IR 翻译为 63 条自定义 VM 指令
* 处理 PC 相对地址重定位（ADRP/ADR → 绝对地址计算）
* 分支目标地址修正 + Label 引用解析

**3. VM 解释器 Stub（C → flat binary）**

* 编译为位置无关的纯二进制（PIC）
* 通过 PT\_NOTE 段劫持注入到 ELF
* 运行时在栈上构建间接跳转表
* CRC32 完整性校验

##

**五层保护机制**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0duHXH9zRaIfhU4wctuUcrzFOP9fvZNc3jFmoutJ7Mwic0c3P5YY8mCQ6gc9A2N0SWG7n5ibLQoD2MvXw9E9bqCcI5LWIOdLLQs/640?wx_fmt=png&from=appmsg)

##

**可扩展性**

项目采用接口驱动设计，`Decoder`/`Translator`/`Packer`三大接口完全解耦，理论上可扩展支持：

* 其他 ISA：x86\_64, RISC-V
* 其他二进制格式：PE (Windows), Mach-O (macOS)

##

**项目地址**

**GitHub**:https://github.com/LeoChen-CoreMind/VMPacker

AGPL-3.0 协议，学习研究随意用。**如果觉得有帮助，欢迎点个 ⭐ Star 支持一下！**PR 和 Issue 也非常欢迎。

这是2.0版本：
![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1jNwotskxsJJBhBO1KZndH2UUqefKE8wgVkbFYYyQvVlic79mMhPGt7eI4fwosb1UoH0u6ic4W6PzXAjzIWNOYEibVibhX7lnHZdk/640?wx_fmt=other&from=appmsg)![]()

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K26J7Y3bqgv0NB4fGJFXE24icnn75z6Qja7530IficMe9ZSYtGKxpibESqjl6oNs09Vff0via7GEOYibib01eXicicSUicvteRqrZFAJvYc/640?wx_fmt=other&from=appmsg)

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0qT5l6icLHldZ6fhdgrpFHLSHlgiaD34od7D6W4e5vnwGIL58oTDfWicoxyada5SiaGNyicSlWItBYgFDP6iatZzKic4tcwpXibtbFicvE/640?wx_fmt=other&from=appmsg)

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2uZv95PrZLOn3M0fDHesYnqq5M0emxFkJ5RerK7cKgn74Wgs4A6h1FbvMdkUcsP6rR5usNDS39d6gr1NoXfEcOvasbjuyyq1k/640?wx_fmt=other&from=appmsg)![]()

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0ndCwLNK5uNfmukdCX08rPFgytFhCgibhyMZrkEPCCBMf4khibnGN7umX2ibfTDhyPRfjq85F4icba66OUPS5TBF6fibsJDq0HOE7I/640?wx_fmt=jpeg&from=appmsg)

看雪ID：LeoChen..

https://bbs.kanxue.com/user-home-1069137.htm

\*本文为看雪论坛精华文章，由 LeoChen.. 原创，转载请注明来自看雪社区

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2qcLqpRmOMibeYwDybhCLLIjdNicUibsZsCmf4IQWHhSkZ8vaFGSPmKKNcSdD8ansPXR7U0ricmvGqBM3XEmciazwVm1V3Lq4qvQbE/640?wx_fmt=jpeg&from=appmsg)![]()![]()![]()

# 往期推荐

[安卓逆向基础知识之frida Hook](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612348&idx=1&sn=9b1f49187644981e264882dedfde45f9&scene=21#wechat_redirect)

[2025 强网杯和强网拟态部分题解](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612341&idx=1&sn=08f4b531105ec2b3a44360f66169db05&scene=21#wechat_redirect)

[在逆向分析方面-unidbg真的适合 MCP 吗？](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612340&idx=1&sn=0c799826addbc96801752a6c70938bf1&scene=21#wechat_redirect)

[AI静态分析，内核模块隐藏 Frida 特征，绕过linker私有结构遍历崩溃链](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612335&idx=1&sn=ca23336eef45a4993cc6e5b191e62a61&scene=21#wechat_redirect)

[某安全so库深度解析](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612118&idx=2&sn=47fe8a55e77b2ca8f2f8d73c9a9d99d0&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpUHZDmkBpJ4khdIdVhiaSyOkxtAWuxJuTAs8aXISicVVUbxX09b1IWK0g/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

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