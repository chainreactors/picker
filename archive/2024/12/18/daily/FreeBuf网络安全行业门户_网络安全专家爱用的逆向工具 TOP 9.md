---
title: 网络安全专家爱用的逆向工具 TOP 9
url: https://www.freebuf.com/news/417887.html
source: FreeBuf网络安全行业门户
date: 2024-12-18
fetch_date: 2025-10-06T19:42:06.947129
---

# 网络安全专家爱用的逆向工具 TOP 9

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

网络安全专家爱用的逆向工具 TOP 9

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

网络安全专家爱用的逆向工具 TOP 9

2024-12-17 11:42:18

所属地 上海

逆向工程是指解构应用程序的过程，不论使用何种编程语言开发，目的是获得其源代码或其中的任何部分。逆向工程的代码有助于发现任何程序中的安全风险，也能用于解密任何恶意应用以进行干扰。![](https://image.3001.net/images/20241217/1734406966_6760f3360af9160622067.png!small)

在寻找破解敏感数据或加密密钥的过程中，黑客们通常选择逆向工程作为一种选项，以找出整个系统中隐藏漏洞的所在之处。这导致了敏感数据的完全暴露，包括被硬编码到应用程序中的 API 密钥、 URL 和API 机密信息，开发人员用于测试的开发服务器 URL，非标准端口号，以及硬编码到应用程序文件及其子目录中的多个私钥等。

逆向工程涉及一系列步骤，包括数据编译、记录元素和功能、评估数据、记录控制流、提取流结构、审查提取的设计、生成逆向工程文档。

从实时跟踪运行的应用程序，解析二进制代码到汇编代码，管理和编辑二进制文件或嵌入式资源在 exe 文件中，逆向工具有各种各样的类型，根据其应用可以分为以下几类：

* 反汇编器
* 调试器
* 数据包跟踪和分析工具
* 脚本工具
* 文件分析工具

以下分享

## 1.十六进制编辑器

十六进制编辑器是一组用于微软 Windows 的十六进制开发工具，结合了高级的二进制编辑和字处理器的简洁易用性和多功能性。它主要用于操纵构成计算机文件的基本二进制数据。

![](https://image.3001.net/images/20241217/1734422290_67612f123c796f31352aa.jpg!small)

此外，十六进制编辑器还支持查找、替换、比较、计算校验和、添加智能标签、颜色映射，并在一个扇区或文件中生成字符分布。十六进制编辑器还支持拖放功能，并可与所有的 Windows 操作系统集成，无论其迭代版本如何。

根据其不同的功能和应用，有各种不同类型的十六进制编辑器，有些允许它们以可视化方式显示文件的内部结构。因此，您可能需要在最常用的工作空间中进行快速简单的十六进制编辑。

数据检视器非常适合解释、查看和编辑十进制和二进制值。算术、逻辑、 ASCII 过程和位操作可用于帮助操作数据集。

集成结构查看器使您能够直观而充分地编辑和查看数据。结构查看器验证信息结构、对各种网络的引用，以及许多原子数据类型：char 、byte 、ubyte 、word 、uword 、long 、ulong 、longlong 、float 、double 、OLE 日期/时间、 DOSTIME 、DOSDATE 、FILETIME 和time\_t 。

**优点：**

* 进行任何十六进制计算时非常方便
* 提供多种选项

**缺点：**

* 用户友好度不太高
* 有时更新问题

## 2.OllyDbg

OllyDbg 是一个针对 Microsoft Windows 的32 位汇编调试器。任何无法获得源代码的情况下，二进制代码的计算认知使得它在许多情况下都非常适用。此外，OllyDbg 是共享软件应用程序,可以下载使用。

![](https://image.3001.net/images/20241217/1734422314_67612f2ac4b0bcfa1d603.png!small)

OllyDbg 的一些关键特性如下：

> 1.保存补丁以在会话之间返回到可执行文件并进行修补升级
>
> 2.查找对象和库模式
>
> 3.代码分析——跟踪记录、查找过程切换、 API 调用、表和循环常量和字符串
>
> 4.DNow 、MMX 和为 Athlon 等SSE 数据类型和扩展提供指令
>
> 5.识别高级配置，如对事件的请求
>
> 6.用于执行的跟踪系统，日志已知可用于调和冲突
>
> 7.查找错误命令和掩盖关键字
>
> 8.检查和修改内存，设置断点并在不可见的情况下暂停应用程序
>
> 9.在会话之间输入标记，将它们还原到可执行文件并修复更新

**优点：**

* 共享软件，免费使用
* 功能强大的动态调试器
* 相对于 IDA 来说更容易操作
* 允许直接加载和调试 DLL
* 有脚本和插件可用

**缺点：**

* 仅限于 Microsoft® Windows®
* 只适用于 x86（或 32 位）软件
* 不是静态调试器

## 3.APKTool

Apktool 是另一种开源选择，主要用于 Android 逆向工程，可以将资源解码为几乎其原始形式。可以进行修改，并将其转换回二进制 APK/JAR 文件。

![](https://image.3001.net/images/20241217/1734422332_67612f3c9b679df003b26.jpg!small)

此外，Apktool 还允许逐步调试 smali 代码，并且由于项目文件的结构以及对一些重复性操作的自动化，使得处理应用程序变得更加容易。使用该程序需要 Java 7 。

**优点：**

* 在逆向 Android 应用文件方面高效
* 可在网上免费使用
* 社区支持良好

**缺点：**

不如 JEB 反编译工具普遍

## 4.WireShark

Wireshark 是一个知名的网络和网络领域的工具。它是免费和开源的，是一个 Web 调试器，可以拦截和修改 HTTP 请求，并且可以记录 HTTPS 请求。它用于数据包分析和网络故障排除。

![](https://image.3001.net/images/20241217/1734422350_67612f4ecf7beccb79c68.jpg!small)

**优点：**

* 免费且开源的 Web 调试器
* 支持跨平台

**缺点：**

* 对于初学者来说，可能会感到压力山大

## 5.Scylla

Scylla 不是一个独立的工具，而更倾向用于重构 Windows 的x86 和x64 文件的工具。它还具有全 Unicode 支持，并且与 Windows 7 、8 和10 完全兼容。

![](https://image.3001.net/images/20241217/1734422387_67612f73c23cd0280589a.png!small)

**优点：**

* 一个开源的产品
* 支持 x64 和x86

**缺点：**

* 缺乏更新
* 有时会有错误

## 6.Dex2jar

Dex2jar 是一个 API，用于扫描 Dalvik Executable（.dex/.odex）格式。它与 Android 和Java .class 文件兼容。

![](https://image.3001.net/images/20241217/1734422406_67612f864741cda18b4be.png!small)

Dex2jar 包括以下几个组件：

* Dex-reader 用于扫描 Dalvik Executable（.dex/.odex）格式。它具有类似 ASM 的轻量级 API
* Dex-translator 用于执行转换工作。它读取 dex 指令以 dex-or 格式，经过一些优化后，转换为 ASM 格式
* Dex-用于它使用 Dex-translator 表示 dex 指令
* Dex-tools 用于处理.class 文件

示例：修改应用程序、解混淆一个.jar 文件。

**优点：**

* 可以读取 Dalvik Executable 格式
* 轻量级 API

**缺点：**

* 只与 Android 和Java .class 文件兼容

## 7.CCF

CCF 是一个免费的便携式可执行编辑器，支持.NET 文件结构。 CCF 支持 32 位和 64 位PE 文件。 CCF 由NTCore 开发，还可用于解压缩 UPX 打包器。

![](https://image.3001.net/images/20241217/1734422420_67612f9472df301dce201.jpg!small)

**优点：**

* 免费的 PE 编辑器
* 也支持.NET 文件
* 支持 PE 32 位和 64 位
* 包含 PE 重建器
* 可用于解压缩 UPX

**缺点：**

* 免费版本自 2012 年以来未更新

## 8.Oracle VM VirtualBox

Oracle VM VirtualBox 是一个开源的虚拟化解决方案，在 Windows 、Mac 、Linux 等不同平台上皆可使用，用于在安全环境中分析恶意软件。

![](https://image.3001.net/images/20241217/1734422462_67612fbeda0880a813328.jpg!small)

**优点：**

* 免费且开源
* 活跃的开发社区
* 支持虚拟机操作系统

**缺点：**

* 与 VMware 相比，功能略差

## 9.BinaryNinja

目前没有反编译器，但计划在将来的“高级”版本中加入。 Binary Ninja 由Vector 35 开发，以其易用性而自豪，使得自动化比其他解决方案更容易理解。

![](https://image.3001.net/images/20241217/1734422477_67612fcd33269adb7bdcb.png!small)

尽管易于使用，但该软件在反向工程本地主机中仍然存在一些问题。

**优点：**

* 简单易用
* 包含反汇编器

**缺点：**

* 不是调试器或反编译器
* 有时无法加载用户界面
* 免费版本有限

> 参考来源：<https://www.secureblink.com/blogs/top-9-reverse-engineering-hacking-tools-for-cyber-security-experts>

# 工具 # 渗透测试工具

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

1.十六进制编辑器

2.OllyDbg

3.APKTool

4.WireShark

5.Scylla

6.Dex2jar

7.CCF

8.Oracle VM VirtualBox

9.BinaryNinja

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)