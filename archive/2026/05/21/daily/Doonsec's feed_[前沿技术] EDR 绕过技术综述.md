---
title: [前沿技术] EDR 绕过技术综述
url: https://mp.weixin.qq.com/s/eLwH7lZuPqiz_-Y751voWQ
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:33.300088
---

# [前沿技术] EDR 绕过技术综述

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BasqgWRklkTw2kibp9mMM3cRBY0p08vkXxIia9hUSEia6wWnicu2h0Eo8YSNbnwn0kTTE5cr6EoIEcFs3UJmFicCByXFb2Z8MAEjibkUnQgu0RIiaI/0?wx_fmt=jpeg)

# [前沿技术] EDR 绕过技术综述

原创

Pik安全实验室
Pik安全实验室

Pik安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x00 介绍

EDR（Endpoint Detection and Response）是现代企业安全的核心防线。CrowdStrike、SentinelOne、Microsoft Defender for Endpoint 等产品通过内核驱动持续监控进程行为。攻击者需要在免杀基础上进一步绕过 EDR 的行为检测，本文梳理当前主流的 EDR 绕过技术。

0x01 EDR 检测原理

EDR 主要通过三种机制检测威胁：用户态 API Hook（ntdll.dll）、内核回调（PsSetCreateProcessNotifyRoutine）、ETW（Event Tracing for Windows）。

0x02 绕过技术

Unhooking — 恢复干净的 ntdll.dll

EDR 在 ntdll.dll 函数开头插入 JMP 指令（Hook）。从磁盘读取一份干净的 ntdll.dll 覆盖内存中的 Hook 版本。

// 经典 Unhooking 技术
// 1. 读取磁盘上的 ntdll.dll
HANDLE hFile = CreateFileW(L"C:\\Windows\\System32\\ntdll.dll", ...);
// 2. 映射到内存
HANDLE hSection;
NtCreateSection(&hSection, SECTION\_MAP\_READ, ...);
// 3. 找到进程中的 ntdll .text 段
// 4. 用磁盘版本覆写 Hook 区域

系统调用（Syscall）直连

绕过用户态 Hook，直接从应用层调用内核系统调用。Hell's Gate 和 Halo's Gate 技术可动态提取 syscall 号。

// Direct Syscall 示例
// 从 ntdll.dll 解析 syscall stub
// 提取 syscall 号并自己构造 syscall
asm("mov r10, rcx; mov eax,; syscall; ret");

// 应对 syscall 号变化的 HalosGate
// 向下搜索相邻函数的 syscall 号

ETW 禁用

ETW 是 EDR 获取遥测数据的主要渠道。通过修补 EtwEventWrite 函数或篡改 ETW 提供者可关闭日志。

进程注入变体

Early Bird APC Injection、Process Doppelgänging、Process Herpaderping 等高级注入技术绕过 EDR 的进程创建回调。

回调移除

在驱动层面移除 EDR 注册的内核回调函数。

0x03 防御侧视角

检测 unhooking 行为（ntdll 完整性校验）、监控 syscall 调用频率异常、ETW 事件丢失告警、VBS enclave 隔离。

本文仅作安全研究与学习用途，用于非法行为后果自行承担。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

Pik安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

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