---
title: Rub: 纯 Rust 实现的高性能、轻量级 BOF 加载器
url: https://mp.weixin.qq.com/s/TvlQquO4rVjOo2-_F9KsVQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:36.290746
---

# Rub: 纯 Rust 实现的高性能、轻量级 BOF 加载器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T9Er13QLZqt5Y5xlYNfASt8adYwzENTJksBRic9ciakIymhVnz8IRaYVc1icgcmcbJ2wKs85TGnL2Znvj3DXBmx1icia51f2hu5ro2uQsibQfLMI8/0?wx_fmt=jpeg)

# Rub: 纯 Rust 实现的高性能、轻量级 BOF 加载器

原创

0xNaNa
0xNaNa

0x33 SEC

![]()

在小说阅读器中沉浸阅读

# Rub: 纯 Rust 实现的高性能、轻量级 BOF 加载器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T9Er13QLZqsENUMsJWVXsSOg1pKsFZ6XQt0Ao1BibRRiaPrqOOSKBw2XMkLVuibQePx288bRUPfrJjYCIowwDkkGQlGAxDTFIoHT9r1rLXNDwY/640?wx_fmt=png&from=appmsg)

在红队评估与高级渗透测试中，Beacon Object Files (BOF) 凭借其轻量级、内存加载及良好的隐蔽性，已成为执行敏感操作的首选。

## 0x01 工具概述

**Rub** 是一款专注于 x64 环境的 COFF 目标文件加载器。它能够在内存中直接完成 BOF 的解析、重定位及执行，并提供完整的 Beacon 风格 API 支持。

相较于传统的 C/C++ 实现，Rub 利用 Rust 的内存安全特性，显著降低了在加载恶意代码或复杂 BOF 时可能导致的进程崩溃风险。

## 0x02 核心优势

* **纯 Rust 构建**：零 C/C++ 依赖，逻辑清晰，易于集成到各类 Rust 开发的安全工具中。
* **高度兼容**：完整支持 Beacon Data (Parse/Int/Short/Length/Extract) 及 Beacon Output (Printf) API，确保与 Cobalt Strike 现有生态的 BOF 无缝衔接。
* **动态符号解析**：内置智能符号解析引擎，支持自动加载系统 DLL 并解析导出符号。
* **参数打包**：遵循 CS 兼容的参数打包约定，支持 `z` (string)、 `i` (int32)、 `s` (int16) 等多种数据类型。
* **隐蔽性优化**：内置对关键 API 名称及前缀的简单混淆处理，配合内存权限管理（RW -> RX），提升对抗 EDR/AV 的能力。

## 0x03 实战演示

在针对最新版主流杀软的测试中，Rub 配合内置的 `hashdump.x64.o` 示例，能够稳定绕过内存监控并成功提取系统凭据：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T9Er13QLZqtFZKRM6nxrE0mpSr0OAhsfxjgMf4ofhqUBaoPvxP2HvG5uezAM4ibAIUYB0oibBLtmrnjeD315r4RD04IfGUI7Q6lru0udc3AGI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/T9Er13QLZqvnHic29CrDFUqic5Kn86JzE9qmNPv3quO5WUHy3CprEEVGmhDyEmia8nLmT3W3KHw1nb7ESLvniaagkr8CVJ5sFqGxv7GC3QnxR8A/640?wx_fmt=jpeg&from=appmsg)

此外，项目还提供了 `av_detect` (杀软检测) 及 `screenshot` (截屏) 等常用 BOF 示例，方便快速上手。

## 0x04 快速开始

```
1. use rub::{Load, loadArgs};

3. // 1. 准备 BOF 数据
4. let bof_data = include_bytes!("bof_example/hashdump.x64.o");

6. // 2. 打包参数
7. let raw_args = vec!["i42".to_string()];
8. let packed_args = loadArgs(&raw_args)?.unwrap_or_default();

10. // 3. 执行
11. #[cfg(windows)]
12. let output =Load(bof_data,&packed_args)?;
13. println!("{}", output);
```

## 0x05 法律声明

**本工具仅供已授权的渗透测试、安全审计及网络安全教育研究使用。**

严禁将此工具用于任何未授权的攻击活动或非法用途。使用者应遵守当地相关法律法规，开发者对因不当使用造成的任何直接或间接后果不承担任何法律责任。

---

## 0x06 获取方式

## 后台发送消息20260401

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

0x33 SEC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

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