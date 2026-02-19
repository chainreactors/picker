---
title: 在 Firefox 中，将“|”误写为“&amp;”会导致零日远程代码执行漏洞
url: https://mp.weixin.qq.com/s/xsfskiYUocOU6sdiBAdU2w
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:13:55.866830
---

# 在 Firefox 中，将“|”误写为“&amp;”会导致零日远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OajerVK6OTL6bGZStelxl7fBGSvRUBENDqmicQfUicmMIZ6C5h5Liaiae1ic9ib0JNicZAuRsU5dVrx4NDYLhMFm7bQe1CB7LK7T6UqE/0?wx_fmt=jpeg)

# 在 Firefox 中，将“|”误写为“&”会导致零日远程代码执行漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Mozilla Firefox 中的一个严重远程代码执行 (RCE)漏洞是由 SpiderMonkey JavaScript 引擎的 WebAssembly 垃圾回收代码中的一个单字符拼写错误引起的，开发人员错误地输入了“&”（按位与）而不是“|”（按位或）。

安全研究员 Erge 在研究 Firefox 149 Nightly 源代码以寻找 CTF 挑战的灵感时发现了这个漏洞，并成功利用该漏洞在 Firefox 渲染器进程中执行了代码。

该漏洞是在重构文件中的 WebAssembly GC 数组元数据时，在提交 fcc2f20e35ec 中引入的。`js/src/wasm/WasmGcObject.cpp` 有问题的行读取的是，`oolHeaderOld->word = uintptr_t(oolHeaderNew) & 1;`而它应该是`oolHeaderOld->word = uintptr_t(oolHeaderNew) | 1;`。

由于指针对齐的原因，与 1 进行按位与运算的结果始终为 0，导致代码存储零而不是存储预期的、最低有效位已设置的转发指针。

这个单字符错误造成了内存损坏漏洞，因为它错误地将行外 (OOL) WebAssembly 数组标记为行内 (IL) 数组，导致垃圾回收器错误地处理内存引用。

## **Firefox RCE漏洞**

SpiderMonkey 的 WebAssembly GC 实现中存在一个 bug，该 bug 会具体影响`WasmArrayObject::obj_moved()`垃圾回收器在内存位置之间移动 Wasm 数组时调用的函数。

当一个 OOL 数组被重定位时，垃圾回收器必须在旧缓冲区头部留下一个转发指针，以便 Ion（SpiderMonkey 的 JIT 编译器）能够找到数据的新位置。转发指针与普通头部的区别在于，它的最低有效位 (LSB) 设置为 1。

该拼写错误导致转发指针被设置为 0，无意中满足了函数中将数组标识为内联数组的条件`isDataInline()`：`return (headerWord & 1) == 0;`。

此漏洞只能在 Ion 优化的 WebAssembly 函数中触发，因为 Baseline 编译器中不存在此机制。

研究人员 Erge 开发了一种概念验证漏洞利用程序，通过以下步骤实现了任意读/写原语和完全远程代码执行：

1. 触发了一次小型垃圾回收，导致转发指针中存储了 0。
2. `wasm::Instance::updateFrameForMovingGC`由于零转发指针，Ion 的函数错误地将数组识别为内联数组。
3. 该函数返回了旧的数组地址而不是新的地址，从而阻止了栈帧的更新。
4. 由于 Ion 继续使用已释放的阵列内存，因此产生了释放后使用 (UAF) 的情况。
5. 使用类似这样的值执行堆喷射，`0x41414141`以回收已释放的内存
6. 通过控制解释型 OOL 数组的基地址，实现了任意读/写操作。
7. 通过喷射包含二进制相对指针的对象来绕过ASLR
8. 覆盖虚函数表以劫持 RIP 并执行任意系统命令

最终的漏洞利用`/bin/sh`通过调用 system() 函数成功生成了一个 shell ( )。

## **披露和修补时间表**

漏洞披露过程十分迅速：

| 事件 | 日期 |
| --- | --- |
| 漏洞由提交 fcc2f20e35ec 引入 | 2026年1月19日 |
| 独立研究人员提交了漏洞报告2013739 | 2026年2月3日（预计） |
| Erge提交了bug报告201401472小时内 | 2026年2月3日 |
| 漏洞已通过提交 05ffcde 修复 | 2026年2月9日 |
| 安全赏金已发放并分配 | 2026年2月11日 |

该漏洞仅影响 Firefox 149 Nightly 版本，从未出现在任何正式版中，因此避免了被广泛利用。Mozilla 的安全团队迅速修复了该漏洞，两位独立发现该漏洞的安全研究人员平分了漏洞赏金。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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