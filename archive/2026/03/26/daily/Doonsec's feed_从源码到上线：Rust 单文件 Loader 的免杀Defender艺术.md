---
title: 从源码到上线：Rust 单文件 Loader 的免杀Defender艺术
url: https://mp.weixin.qq.com/s/RQgVUZcThbeTy-EB0I3KPg
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:40.599522
---

# 从源码到上线：Rust 单文件 Loader 的免杀Defender艺术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cGhMn4Bj3bYt7kA7ddpSeuQfGkrF6G3UV9qFIf76LjzrOUJy3sZwNdbyiaZDWV3IMNaWeoIgq3tPxqfvYAm51cowjaWUBUU5gicbqmMhJQers/0?wx_fmt=jpeg)

# 从源码到上线：Rust 单文件 Loader 的免杀Defender艺术

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器中沉浸阅读

高成功率的 Rust 注入器实现指南

**为什么用Rust过杀软**

在如今红队工程化对抗中，传统的 C++/C# Loader 往往难逃静态特征库的围剿。**Rust** 凭借其底层的控制力、极高的自定义程度以及原生对 LLVM 的支持，正逐渐成为开发免杀载具的首选语言。

今天，我们要分享的是一种**单文件、高性能、针对 Windows Defender** 的免杀 Loader 实现思路。

**环境准备**

在追求极致便携和免杀时，**`rustc` 直接编译**往往更具优势：

* **单文件依赖：** 一个 `.rs` 源码，一个 `.exe` 成品。
* **环境要求：** 仅需安装 Rust 工具链及 Windows MSVC 目标。
* **核心编译命令：**

```
rustc agent_2_enum_locals.rs --target x86_64-pc-windows-msvc -C opt-level=2 -o agent_2_enum_locals.exe
```

![291b7d18990a86539894f17d7aa57c5f.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnu2Gv3hiaym8R3UnJVjVpCkCejx66HXSH68mSvsJaGnMIgm6bz4N3wEqtFL1Fggd9gbtiaoOicavBQ7KpOeKnRBDKmncC1LePR2Rc/640?from=appmsg)

**测试流程**

1. 关闭自动提交样本（存活率大幅提高）

   ![8ea3ebf34e929e4e46ccfe5611788afc.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnvv1oYDh9PqaPThvZFOYeGpTuYJYnhHicnX8hzcticmHWrlknPmWBSia61picxCCMqFiadH0V9AhXvFQzKia3U2k6qfx0tkQbetujfU8/640?from=appmsg)

2.对文件进行静态扫描

![6a3be4e826740a36e1ea214465af7690.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnvNZky63MZMl1GU1u8UnNaIkBs3DgKloBG2aeBX3rdRtVxvNTM3XJQtcM2nt7LYBOwZMial59brt2d0tY8N90AzXpjNkiagE6F0g/640?from=appmsg)

3.点击，Adaptix 接收 Beacon，成功上线！

![474c9efa172611fad8b780662b4927e7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnvhQSn7FlFvLD9bLmJ3lHicxG1oNY48qkSJXdoMKVYxPXjLc3HMBIHwlfqibzIseTfb48RzsS6SexUic8MfTZMicibG7rHicTDYSQ4YY/640?from=appmsg)

![9d9b31200201400efe3fbe31dd7cc559.png](https://mmbiz.qpic.cn/mmbiz_png/T5wSZNgEHnuU2yjiaOqD9Qm210VfnkNP9v9ppsJG2YZCOw8Aqjbd6OCJzsxH0W3RLribPqLkC8iajH8fbn6eDNbeYKxYsyoDv5lxdCrUVEQMZQ/640?from=appmsg)

**学习高级免杀技术**

由于技术敏感性，文中对于**Shellcode 的具体加密逻辑、动态注入的具体 API 序列**进行了脱敏处理。
![00bdb0de62127495b560d27da433581c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnst7NfcVlvfqCchtwvRlP2pSNfaST8msVpqmwHxj7YaCGkS440611u5ibPz0LtSnMN8diaibnY3kibIrLCx6DkRCmgcoZPup7Teq3I/640?from=appmsg)

如果你对这套 **Rust 免杀技术栈** 感兴趣，想要获取，加入我们的纷传，我们会：

1. **持续更新bypass各种杀软完整 Loader 源码**
2. **源码对应详细技术分析文档，可供学习各种规避bypass技术**
3. **后续持续更新的终端对抗的各种项目插件**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T5wSZNgEHnuzlEib0ByYWoyzia8P5E3XsH5n1hHcuDc9mMkVLhVkicmxkicYSGCH5veZDMXY6XJEgiaMZLDDAqdGicUic4q0kD6ibJ4MmiaB1BGKBoRw/640?wx_fmt=jpeg)

# 最后

🌟感谢您看到这里，您的支持与关注，是我们持续输出内容的最大动力

🌟欢迎加入我们的交流群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbxhYcEDxJCdN0iaSCBicGm5ibUmiaXYOeow0Kp7tEAGgaxFicVNT0YfTHLaTADxV2OTamBV9BjP4AFvjFuJJ7vkglUcUwTKqge7ibHg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

信益安信息安全研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

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