---
title: 黑客利用 macOS 扩展文件属性隐藏恶意代码
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580067&idx=1&sn=1b4cd406b7ac4ce6e199711f557c7808&chksm=e9146999de63e08f18756dcf5c3f0bbda52ce6df0491b706f1a35430cd5891514c9ff4e9bb57&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-05
fetch_date: 2025-10-06T19:39:26.029776
---

# 黑客利用 macOS 扩展文件属性隐藏恶意代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28FaXGha095Ul4bNj7yAxFBxwNuVkAzWI6jfgroQreicEKlXpWIqibDAq29cnobrV73vkR4ibtQvUMAw/0?wx_fmt=jpeg)

# 黑客利用 macOS 扩展文件属性隐藏恶意代码

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

黑客被发现正滥用 macOS 文件的扩展属性来传播一种新的木马，研究人员将其称为 RustyAttr。

威胁分子将恶意代码隐藏在自定义文件元数据中，并使用诱饵 PDF 文档来帮助逃避检测。这项新技术类似于 2020 年 Bundlore 广告软件将其有效负载隐藏在资源分支中以隐藏 macOS 有效负载的方式。安全研究人员在一些野外恶意软件样本中发现了它。

根据他们的分析，由于无法确认任何受害者，研究人员有一定把握将这些样本归因于朝鲜黑客拉扎勒斯。他们认为攻击者可能正在尝试一种新的恶意软件传递解决方案。

这种方法并不常见，现在已被证明可以有效地防止检测，因为 Virus Total 平台上的安全代理都没有标记恶意文件。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBNIVq3K8YgsIZNpPB08N8dEcBib7W3UfgWicvYdZ4OI32sT9BksrUQu9A/640?wx_fmt=png&from=appmsg)在文件属性中隐藏代码

macOS 扩展属性 (EA) 表示通常与文件和目录关联的隐藏元数据，这些元数据在 Finder 或终端中不直接可见，但可以使用“xattr”命令提取以显示、编辑或删除扩展属性。在 RustyAttr 攻击的情况下，EA 名称为“test”并包含 shell 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBIRnSFLa0beLSoZTFI6m1ZwMosjTN2JwibiaCXA0KW3S3RJCzic3FKYtgw/640?wx_fmt=png&from=appmsg)

macOS 扩展属性内的 Shell 脚本

存储 EA 的恶意应用程序是使用 Tauri 框架构建的，该框架结合了可以调用 Rust 后端函数的 Web 前端（HTML、JavaScript）。当应用程序运行时，它会加载一个包含 JavaScript（“preload.js”）的网页，该网页从“测试”EA 中指示的位置获取内容，并将其发送到“run\_command”函数以执行 shell 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFB8icjtqaTRiaTtrecVMib71Mf0aGkdlTdPndO9pvIvb5rragQ46qChC8fQ/640?wx_fmt=png&from=appmsg)

preload.js 的内容

为了在此过程中降低用户怀疑，某些示例会启动诱饵 PDF 文件或显示错误对话框。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBE4I3uWyiclbEDGEJ7fj0xuI8I6MibiaL1dewPwRrfxefljEnRuSxDXGVg/640?wx_fmt=png&from=appmsg)

诱饵 PDF 隐藏恶意后台活动

该 PDF 是从用于公共文件共享的 pCloud 实例获取的，其中还包含名称与加密货币投资主题相关的条目，这与 Lazarus 的目的和目标一致。

RustyAttr 应用程序 Group-IB 的少数样本发现，所有应用程序都通过了 Virus Total 的检测测试，并且应用程序是使用泄露的证书进行签名的，苹果已撤销该证书，但未经过公证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBW8lxqpUCEkIZVTEwbmaZkmQ0ZQ9notzdhxWGhajWsibPSglNDRj2DCw/640?wx_fmt=png&from=appmsg)

应用证书详细信息

Group-IB 无法检索和分析下一阶段的恶意软件，但发现临时服务器连接到 Lazarus 基础设施中的已知端点以尝试获取它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBoRPvnSY4YpPOV92ibCicp1bKmMNfSGvr0YOolmfWvdia7HzaL3We0xLDg/640?wx_fmt=png&from=appmsg)

执行流程

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBNIVq3K8YgsIZNpPB08N8dEcBib7W3UfgWicvYdZ4OI32sT9BksrUQu9A/640?wx_fmt=png&from=appmsg)尝试 macOS 规避

Group-IB 报告的案例与 SentinelLabs 最近的另一份报告非常相似，该报告观察到朝鲜黑客 BlueNoroff 在 macOS 中尝试了类似但不同的规避技术。

BlueNoroff 使用以加密货币为主题的网络钓鱼来引诱目标下载经过签名和公证的恶意应用程序。

这些应用程序使用修改后的“Info.plist”文件来秘密触发与攻击者控制的域的恶意连接，从该域检索第二阶段有效负载。

目前尚不清楚这些活动是否相关，但不同的活动集群通常会使用相同的信息来了解如何有效地破坏 macOS 系统而不触发警报。

参考及来源：https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBrZib2T4yd4ic3Gfz9ZhJFR2CrnCLV7mg2MofFUxvYxzkeavC9tQiayLqg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28FaXGha095Ul4bNj7yAxFBbLgK2aPdEC09wu1SuzG3NUxX72FnG3yShzUFBDaG9wQqicSf0DuuOUQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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