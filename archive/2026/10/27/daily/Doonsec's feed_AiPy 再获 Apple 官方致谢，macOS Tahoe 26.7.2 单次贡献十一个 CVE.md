---
title: AiPy 再获 Apple 官方致谢，macOS Tahoe 26.7.2 单次贡献十一个 CVE
url: https://mp.weixin.qq.com/s/phiCAzweae75lNn3xEnC_g
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:41:47.050646
---

# AiPy 再获 Apple 官方致谢，macOS Tahoe 26.7.2 单次贡献十一个 CVE

# AiPy 再获 Apple 官方致谢，macOS Tahoe 26.7.2 单次贡献十一个 CVE

知道创宇

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI智赋未来 · 安全守护信息化

近日，Apple 发布 macOS Tahoe 26.7.2 安全更新，知道创宇自研开源 AI Agent 产品 AiPy（章鱼哥）在本次公告中获得**11 个 CVE 编号**，创下 AiPy 在单个 Apple 安全公告中的致谢数量新高。

这是继 macOS Tahoe、macOS Golden Gate 27 之后，AiPy 第三次获得 Apple 官方安全公告的公开认可。从最初的三个 CVE，到 Golden Gate 27 的三个 CVE，再到本次的十一个 CVE，AiPy 在 macOS 生态中的安全研究产出正在快速放大。

01 十一项漏洞：横跨六大系统组件

本次 AiPy 发现的 11 个 CVE 分布在 macOS 的六个不同组件中，涵盖媒体解码、视频编码、音频处理、打印服务、字体解析与三维模型处理等多个层面。

AppleAVD:媒体解码框架两处越界写入

AppleAVD 是 macOS 的音频视频解码框架，负责处理各类媒体格式的硬件加速解码。

漏洞编号：**CVE-2026-112416**

漏洞类型：越界写入

影响：处理恶意构造的视频文件可能导致应用程序意外终止

描述：越界写入问题已通过改进边界检查修复

漏洞编号：**CVE-2026-112415**

漏洞类型：越界写入

影响：应用程序可能导致系统意外终止或破坏进程内存

描述：越界写入问题已通过改进输入验证修复

两个漏洞均属于越界写入类型，攻击面来自外部媒体文件。视频解码器需要解析高度复杂的容器格式与编码参数，历来是内存安全问题的集中区域。

AVEVideoEncoder：视频编码器四处缺陷

AVEVideoEncoder 是 Apple 的视频编码组件，负责将原始帧数据编码为压缩视频流。

漏洞编号：**CVE-2026-112470**

漏洞类型：越界写入

影响：应用程序可能导致系统意外终止或破坏内核内存

描述：越界写入问题已通过改进边界检查修复

漏洞编号：**CVE-2026-112468**

漏洞类型：越界写入

影响：应用程序可能导致系统意外终止或破坏内核内存

描述：越界写入问题已通过改进边界检查修复

漏洞编号：**CVE-2026-112469**

漏洞类型：越界写入

影响：应用程序可能导致系统意外终止或破坏内核内存

描述：越界写入问题已通过改进边界检查修复

漏洞编号：**CVE-2026-112466**

漏洞类型：越界读取

影响：应用程序可能导致系统意外终止或读取内核内存

描述：越界读取问题已通过改进输入验证修复

这四个漏洞中有三个可导致**内核内存破坏**，一个可导致**内核内存读取**。编码器组件通常运行在较高的权限层级，与内核共享部分缓冲区，因此其内存缺陷的影响范围会从用户态延伸至内核态。同一个组件中连续发现四处边界问题，说明其参数校验流程存在需要系统性梳理的环节。

CoreAudio：音频框架越界访问

漏洞编号：**CVE-2026-113912**

漏洞类型：越界访问

影响：处理恶意构造的媒体文件可能导致应用程序意外终止或破坏进程内存

描述：越界访问问题已通过改进边界检查修复

CoreAudio 是 macOS 的底层音频服务框架，负责音频设备的驱动、混音与格式转换。该框架需要处理来自各种音频文件与外部设备的原始数据流，输入来源复杂。

CUPS：打印服务沙箱逃逸

漏洞编号：**CVE-2026-84545**

漏洞类型：释放后使用导致沙箱逃逸

影响：受 App Sandbox 限制的应用可能借此逃逸沙箱并以 root 权限执行代码

描述：释放后使用问题已通过改进内存管理修复

这是本次 11 个漏洞中**风险等级最高**的一个。App Sandbox 是 macOS 的核心安全机制，用于限制应用的文件访问与系统调用范围。该漏洞允许受沙箱限制的应用突破隔离边界，并以**root 权限**执行任意代码——这意味着攻击者可以从一个低权限应用起步，直接获得系统的最高控制权。释放后使用问题出现在 CUPS 打印服务中，说明该服务的对象生命周期管理存在可被利用的时序窗口。

FontParser：字体解析两处缺陷

FontParser 是 macOS 的字体解析组件，负责读取并渲染各类字体文件。

漏洞编号：**CVE-2026-86970**

漏洞类型：越界读取

影响：处理恶意构造的字体可能导致进程内存泄露

描述：越界读取问题已通过改进输入验证修复

漏洞编号：**CVE-2026-112683**

漏洞类型：越界写入

影响：处理恶意构造的字体可能导致应用程序意外终止或破坏进程内存

描述：越界写入问题已通过改进边界检查修复

字体文件格式历史悠久，包含大量可选的表结构与变长字段，解析逻辑分支众多。字体解析器通常被系统服务直接调用，一旦出现越界问题，影响范围会超出单个应用。

Model I/O：三维模型整数溢出

漏洞编号：**CVE-2026-112565**

漏洞类型：整数溢出

影响：处理恶意构造的三维模型可能导致内存破坏

描述：整数溢出问题已通过改进输入验证修复

Model I/O 是 Apple 的三维模型处理框架，支持 USD、OBJ、PLY 等多种格式。三维模型文件中的顶点数量、索引偏移等字段常以整数形式存储，若未对取值范围做严格校验，在后续内存分配计算中就可能发生溢出，进而导致分配尺寸与实际写入量不匹配。

02 致谢名单中的 AiPy 身影

Apple 在安全公告中对漏洞报告者表示了感谢。本次 11 个 CVE 的致谢信息如下：

**CVE-2026-112416**
an anonymous researcher, Meta Red Team X - Nik Tsytsarkin, Narendra Singh (@\_3P1C), Hcamael and 章鱼哥@aipy (aipyaipy.com), Dohyeon An @PILAB Technology, Inc

**CVE-2026-112415**
Rahul Raj, Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112470**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112468**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112469**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112466**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-113912**
an anonymous researcher, 章鱼哥@aipy (aipyaipy.com), Roman Zabicki, Anna Groza (@pwnlambda) of Calif.io

**CVE-2026-84545**
Jurre van Bergen - Threatnotify, Mathis Mansière, 章鱼哥@aipy (aipyaipy.com), Redon Gashi (Sentry)

**CVE-2026-86970**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112683**
Hcamael and 章鱼哥@aipy (aipyaipy.com)

**CVE-2026-112565**
Musaab Khan (@bxff), Hcamael and 章鱼哥@aipy (aipyaipy.com), Saoud Khalifah, stratan (@5tratan), Niels Hofmans

03 从单点到批量：macOS 研究能力的跃迁

macOS 作为闭源操作系统，安全研究门槛显著高于开源项目。研究者无法直接阅读源码，需要依靠逆向工程、动态调试与模糊测试来还原组件的内部逻辑。而本次 11 个漏洞覆盖了六个完全不同的组件——媒体解码、视频编码、音频框架、打印服务、字体解析、三维模型处理——每个组件的输入格式、内存模型与权限层级都不相同。

这种跨组件的批量产出，说明 AiPy 的分析流程已经具备了一定的通用性：面对一个陌生的闭源组件，能够自主完成输入面识别、样本构造、异常定位与影响评估的完整链条，而不是依赖针对单一模块的人工经验积累。

从漏洞类型来看，本次 11 个 CVE 中有**6 个属于越界写入**、**3 个属于越界读取**、**1 个释放后使用**、**1 个整数溢出**。这些都是内存安全领域最基础也最核心的缺陷类别，也是实际攻击中最常被利用的类型。

04 持续深耕，跨平台战绩持续积累

从 Mozilla Firefox 的多轮致谢，到 F5 NGINX 的堆缓冲区溢出、OpenVPN 的四连击、PostgreSQL 18.6 的六项 CVE、Google Chrome 的高危漏洞、QEMU 的虚拟化缺陷，以及 Apple macOS 的三次官方致谢——AiPy 已经横跨浏览器、应用交付、VPN、数据库、虚拟化平台和操作系统等多个关键领域。

每一次致谢背后，都是真实的技术产出。具备安全基因的 AI Agent，正在实战中持续证明自己的价值。

知道创宇将继续推动**可信 AI 技术**与**安全能力**的深度融合，以自主可控的 AI 安全方案，为更多关键基础设施组件和底层系统安全提供保障，致力于成为各行业、全场景可信赖的**AI 安全伙伴**。

参考资料

Apple 安全公告（macOS Tahoe 26.7.2）：support.apple.com/en-us/149522

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdgOPSY3Fa7Wj3d5pqVXwK5eDeiaAnkTOMpBTA6b6pNV6CPiayjSqZ8reThLpX2icBCI0UibClGMk6uibB1WGQPDZO4ibISUAgkwrAYIk/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oan15mBs7fOYe1ETMicrrK5eEreO2UU1sxFQL4Eebn6tthroecicEQrsbZ8qRzV2xMGpvCyU3lWjJwASBPD5QpBg/0?wx_fmt=png)

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