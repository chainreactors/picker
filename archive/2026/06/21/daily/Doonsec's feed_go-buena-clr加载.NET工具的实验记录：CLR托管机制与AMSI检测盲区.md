---
title: go-buena-clr加载.NET工具的实验记录：CLR托管机制与AMSI检测盲区
url: https://mp.weixin.qq.com/s/aISTS365sNiSMGewWLzBSA
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:01.329889
---

# go-buena-clr加载.NET工具的实验记录：CLR托管机制与AMSI检测盲区

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqMibIH6GTPOfjRu7skhFGnHpZgYkJ9mzNwnpfC1GJvibVuicCUESWRmcBbkcs0Ujjqmib94rQMol4gUF9wCgXG9IogmcYl2Ggaicnr4/0?wx_fmt=jpeg)

# go-buena-clr加载.NET工具的实验记录：CLR托管机制与AMSI检测盲区

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **免责声明**：本文仅供网络安全研究与技术交流，所有实验均在本地虚拟化环境中完成，不涉及任何真实目标系统。严禁将文中技术用于未经授权的网络、系统或数据。

## 一、简要介绍

go-buena-clr[1] 是一个在 Go 语言中实现的自定义 CLR 宿主，能够在加载 .NET 程序集时规避 AMSI 扫描。其核心在于 CLR 托管机制中的加载路径差异：

* • **常规反射加载**：从字节数组加载程序集，此路径会触发 AMSI 扫描
* • **按标识加载**：按程序集标识加载，此路径不触发 AMSI 扫描

go-buena-clr 通过自定义 CLR 宿主，接管程序集加载过程，使用按标识加载的方式完成加载，从而避开触发扫描的路径。

## 二、实验环境与过程

### 2.1 实验环境

| 组件 | 配置 |
| --- | --- |
| 编译环境 | Windows系统 |
| 执行环境 | Windows-11-x64-25H2虚拟机（NAT模式），Windows Defender实时防护开启 |
| 相关工具 | go-buena-clr、SharpCollection[2]（Rubeus.exe等）、Garble[3]、Astral-PE[4] |

### 2.2 实验过程与结果

#### 2.2.1 原始Rubeus.exe

将原始Rubeus.exe下载至Windows 11系统后，Windows Defender实时防护立即将其隔离并告警。

![Windows Defender拦截Rubeus.exe](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqOIMmFWdEWJNsKLcibBPll3zNpp6XrkcDguJQfNnicBoXGz7udNWKcHbcIicp53rdBPeeO0882IzNHv94FptKjWk2cESpYJRnBkhM/640?wx_fmt=jpeg&from=appmsg "Windows Defender拦截Rubeus.exe")

Windows Defender拦截Rubeus.exe

> 结果：被拦截

#### 2.2.2 通过go-buena-clr加载

使用go-buena-clr将Rubeus.exe嵌入Go加载器并编译生成可执行文件。在目标环境中执行，程序成功运行，Windows Defender未产生告警。

![go-buena-clr加载Rubeus执行成功](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqM6wE2l7Zm1OicQ5GuhbzZicicr0mKG8fCNiaEwNuCNAH3YrDNiczFoat3cffd0XLbsB57sDxPibtzJ0LuiaRv2MKic5xPos7oxIMgQzJ0/640?wx_fmt=jpeg&from=appmsg "go-buena-clr加载Rubeus执行成功")

go-buena-clr加载Rubeus执行成功

> 结果：执行成功，未触发告警

#### 2.2.3 结合Garble混淆

为进一步降低二进制文件的可读性，引入 Garble[3] 进行编译混淆。在测试环境中，Garble 编译后的文件被标记为 Trojan:Win32/Gracing.I，这是 Garble 混淆编译的已知特征。

该特征与 Go 编译器在二进制文件中残留的特定元数据有关。通过调整Astral-PE[4] 的处理逻辑，对以下静态特征进行清理：

* • 清理 "Go build ID:" 字符串
* • 清理 "Go buildinf:" 结构
* • 清理运行时字符串
* • 重命名 Go 节区

调整后，二进制文件中的静态特征明显减少。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqMHQ6I3qzBcPfrSh8UxqDaJyEGTYZ4CFfrKP9uDbpJg6ibHBYG7b4QgsiaY5vAfmXia40fjcmjnY88kKNCAUs9RUUI5bBMStUmf1Q/640?wx_fmt=jpeg&from=appmsg "null")

> 结果：执行成功，未触发告警

## 三、结论

go-buena-clr 是一个可用的自定义 CLR 宿主方案，适用于需要以独立 EXE 方式加载 .NET 程序集的场景。它通过利用 CLR 托管机制中的加载路径差异，在不修改 amsi.dll 或 clr.dll 内存的前提下规避 AMSI 扫描。

本次实验仅在特定环境下进行，结果不代表所有场景。

#### 引用链接

`[1]` go-buena-clr项目仓库: *https://github.com/almounah/go-buena-clr*
`[2]` SharpCollection项目仓库: *https://github.com/Flangvik/SharpCollection*
`[3]` Garble Go代码混淆工具: *https://github.com/burrowers/garble*
`[4]` Astral-PE PE结构修改工具: *https://github.com/DosX-dev/Astral-PE*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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