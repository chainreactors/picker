---
title: 控制台管道注入技术绕过EDR
url: https://mp.weixin.qq.com/s/QsZrl4xxkaZDoGyBDZxTfA
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:12.036087
---

# 控制台管道注入技术绕过EDR

# 控制台管道注入技术绕过EDR

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、这是什么

一种远程进程注入技术，用来把 shellcode 写进另一个进程并让它执行。

它的特别之处在于：全程不调用 WriteProcessMemory 和 VirtualAllocEx—这两个 API 是 EDR 监控跨进程内存操作的重点，绕开它们就能躲过大量检测规则。

## 二、为什么传统注入会被盯上

经典远程注入的固定套路：

```
1

2

3

4

OpenProcess          拿到目标进程句柄
VirtualAllocEx       在目标进程里分配一块内存
WriteProcessMemory   把 shellcode 拷进去
CreateRemoteThread   让目标进程执行这块内存
```

其中 WriteProcessMemory 最致命——它的作用就是"跨进程写内存"。EDR 在用户态（API Hook）和内核态（回调）都对它严密监控，因为它几乎只被恶意软件用来干这件事。

所以攻击者的思路是：

> 能不能找一个本来就"跨进程写数据"、但又不叫 WriteProcessMemory 的 API？

## 三、关键突破口：stdin 缓冲区

当 Windows 运行一个交互式控制台程序（如 nslookup.exe）时：

1. 1. 系统给它分配一个标准输入句柄 hStdInput
2. 2. 这个句柄背后是一个命名管道（连到 conhost.exe）
3. 3. 程序调用 ReadFile 从管道读数据
4. 4. 读到的数据落在该程序自己的内存缓冲区里

由此推出：

> 往这个管道写数据 - 数据进入目标进程内存。
> 而写管道用的是 WriteFile，不是 WriteProcessMemory。

WriteFile 太常用了（写文件、写管道、写设备都用它），EDR 对它的监控远没有对 WriteProcessMemory 那么严。

## 四、完整攻击链

### 1.选定目标程序

找一个"会读 stdin、且把输入缓存在自己内存里"的进程。

典型目标：nslookup.exe、netsh.exe

### 2.建立可控的 stdin 管道

让目标进程的 stdin 指向一个我能写的管道。

```
1

2

3

4

5

CreatePipe(&hRead, &hWrite)                        建匿名管道
SetHandleInformation(hWrite, 不可继承)             写端只留父进程
STARTUPINFO.hStdInput = hRead                      读端给子进程
CreateProcess(..., bInheritHandles=TRUE, ...)      子进程 stdin = 管道
CloseHandle(hRead)                                 父进程不再需要读端
```

### 3.通过管道写入 payload

把 marker + shellcode 写进管道，数据流入目标进程内存。

### 4.在目标进程内存中定位 payload

找到 marker，算出 shellcode 的真实地址。

### 5.给 shellcode 内存加执行权限

让那块内存可以被 CPU 执行。

### 6.劫持线程执行

让目标进程的某个线程跳到 shellcode 去执行。

**整条链的规避逻辑**

| 传统注入步骤 | 本技术对应 | 规避效果 |
| --- | --- | --- |
| VirtualAllocEx 分配远程内存 | 不调用，靠管道缓冲区 | 绕过内存分配监控 |
| WriteProcessMemory 写远程内存 | 改用 WriteFile 写管道 | 核心规避点 |
| CreateRemoteThread 执行 | 改用线程劫持 | 绕过线程创建监控 |

本质：把攻击链从"内存操作链"改造成"I/O 操作链 + 内存权限修改 + 线程上下文修改"。

## 五、POC

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNwEOgyIMQeicnCVV3pzeMIfncickQ1YWJibEXFw2TzBASWUUZawibDdIUAf7JywNvEhDDsLiazibuOQO5JtKkh1CoqmRtIj9HHHT3Bw/640?wx_fmt=png&from=appmsg "null")

获取完整poc,回复`20260930`获取。

## 六、使用场景

1.在企业授权的攻防演习中，验证防守方的检测与响应能力
2.理解各类加载技术的实现机制与运行过程
3.在受控环境中测试安全设备的检出情况，用于优化检测策略

## 七、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1.仅可用于已获得书面授权的目标系统测试；
2.遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOq43RSf7lfRmsfht4j1OYpZFxV2yBmkPGsNJ4ROQHcUkhseQdibY4vbINt7aotxvSXjWxIEmph546T4Ql1zVcJWTgMNBkYib4ibo/0?wx_fmt=png)

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