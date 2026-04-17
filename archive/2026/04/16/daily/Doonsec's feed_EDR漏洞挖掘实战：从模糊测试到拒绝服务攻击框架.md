---
title: EDR漏洞挖掘实战：从模糊测试到拒绝服务攻击框架
url: https://mp.weixin.qq.com/s/UnI0lIQZOyxJ3Qg4ngcIxw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:21.662478
---

# EDR漏洞挖掘实战：从模糊测试到拒绝服务攻击框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2cj6OI9ZFXsTXkxYGT6oMub0Ltf04VkR4SIIBcl9iaew17SAeJMn2BClWiayVVlPxZGjaHYa1gXyHb7bpEcnJz3ET57clrniaMc70/0?wx_fmt=jpeg)

# EDR漏洞挖掘实战：从模糊测试到拒绝服务攻击框架

原创

aeverj
aeverj

红队工坊

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软 Defender 作为 Windows 系统默认部署的端点安全解决方案，在 2024 年末发现的一起 JAR 文件处理异常事件中，暴露出其代码库中存在的内存损坏漏洞。

这并非恶意软件或针对性攻击，仅为一普通的 Java 归档文件引发的服务进程崩溃。

从安全研究视角审视，这一现象具有一定的反直觉性——Defender 作为 Windows 原生防护组件，因其默认部署、 SYSTEM 权限级别、主动文件扫描机制等特征，反而成为攻击面分析的重点目标。其架构设计中的复杂性因素，包括多格式文件解析、深度模拟执行环境等，使其暴露在内存安全威胁之下。

值得注意的是，当 InfoGuard 安全实验室通过 MSRC （ Microsoft Security Response Center ）报告相关漏洞时，微软官方评估为"中等严重性"，认为"不符合立即修复的标准"。然而，该研究成果公开发布一周内，所有报告的漏洞均得到修复。

## 漏洞挖掘：为什么选择 Defender ？

历史研究记录显示， Google Project Zero 的安全研究员 Tavis Ormandy 于 2017 年首次发现 Defender 存在可利用的远程代码执行漏洞（ CVE-2017-8558 ）。 2021 年，第二个 RCE 漏洞（ CVE-2021-34522 ）被披露。然而， 2023 至 2024 年期间，针对 Defender 的公开安全研究显著减少。

这一现象可以从技术层面进行解释： Defender 的核心引擎组件 mpengine.dll 体积约 20MB ，需要处理数十种文件格式，包括 PE 可执行文件、 JAR 归档、 Office 文档、 Mach-O 二进制等跨平台格式。如此复杂的代码库，配合多解析器架构，从软件工程角度分析，其内存安全漏洞的存在具有较高的统计必然性。

然而，针对 Defender 的安全研究之所以稀缺，存在多重因素：技术复杂度高、漏洞利用链构建困难、厂商响应机制的不确定性。在漏洞挖掘的投入产出比分析中，研究者面临现实考量——发现漏洞后若无法促使厂商及时修复，研究成果的应用价值将受限。

因此，当 p0w1\_于 2025 年重启 Defender 漏洞挖掘项目时，其核心研究问题从"是否存在漏洞"转向"如何构建高效的漏洞发现流程"。

## 模糊测试工具架构对比

模糊测试作为自动化漏洞发现的核心技术，通过向目标程序输入随机或变异的畸形数据，触发内存损坏、逻辑错误等异常行为。然而，针对 Defender 这类复杂软件系统，传统模糊测试框架面临效率瓶颈和技术挑战。

### WTF ： Snapshot Fuzzer 架构

本研究最终采用 WTF （ Windows Testbed Fuzzing ），一种基于进程快照的模糊测试框架。

其核心技术原理包括：首先在目标程序正常启动、加载配置、进入文件扫描关键路径后，对进程状态进行快照保存。后续每个测试用例都从该快照状态恢复执行，避免了重复的初始化开销。

然而， Defender 在文件扫描过程中会调用大量系统 API ，包括文件打开、内容读取、数字签名验证等操作。 WTF 作为纯 CPU 和内存模拟环境，缺乏真实的文件系统支持。

为此，研究团队开发了虚拟文件系统钩子（ hooks ），在`InsertTestcase`函数中实现测试数据注入：

```
boolInsertTestcase(constuint8_t*Buffer,constsize_tBufferSize){std::u16stringGuestFile=uR"(\\??\\C:\Users\User\Downloads\test-files\aspack_Hash.exe)";g_FsHandleTable.MapExistingGuestFile(GuestFile.c_str(),Buffer,BufferSize);}
```

通过 KVM 硬件虚拟化加速后，测试执行速度可达每秒 30-100 次迭代。对于 mpengine 这类复杂目标，该执行效率在可接受范围内。

### kAFL/NYX ：基于符号执行的变异引擎

kAFL/NYX 框架集成了 Redqueen 算法，能够处理复杂的条件跳转指令（ CMP ），通过动态污点分析提升变异效率。然而，在实际应用中， kAFL 存在技术瓶颈： libxdc\_decode 模块频繁抛出错误，内存泄漏现象导致 QEMU 虚拟机实例需要定期重启以释放资源。

经过一个月的持续运行，尽管使用了先进的变异策略，新代码覆盖率增长仍然有限，未能发现额外的漏洞实例。

### Jackalope ：持续模式框架的性能局限

Jackalope 作为一种持续模式的模糊测试框架，在应对 Defender 时面临初始化延迟问题。 Defender 的完整初始化流程耗时约 10 秒，在持续测试场景下，这一延迟显著降低了整体测试吞吐量。此外，部分测试用例触发的超时机制导致频繁的进程重启，进一步影响测试效率。

综合分析表明，对于 Defender 这类复杂目标的漏洞挖掘， Snapshot Fuzzing 架构提供了最佳的测试效率和稳定性平衡。

## 快照定位：内存状态捕获的技术细节

快照定位是影响模糊测试效率的关键技术决策。

理想情况下，快照应在文件内容加载到内存并传递给扫描函数的时刻进行捕获：

```
res=readFile(path);scanFile(res.content,res.size);// 理想快照点
```

然而，实际代码结构更为复杂。通过逆向分析发现，`SysIo::OpenFile`函数中`FilterOplock::AcquireOplock`调用后的位置`mpengine+0x15469A`提供了良好的快照切入点。

同时存在性能优化需求： Defender 在扫描过程中会调用`IsTrustedFile`函数验证文件数字签名，该操作涉及证书文件读取，在快照模拟环境中执行效率低下。研究团队采用函数 hook 机制绕过这一瓶颈：

```
g_Backend->SetBreakpoint("mpengine!IsTrustedFile",[](Backend_t*Backend){Backend->SimulateReturnFromFunction(0);});
```

该 hook 函数直接返回成功状态，跳过数字签名验证流程，显著减少了上下文切换开销。

## 测试语料库构建：恶意样本库的规模效应

鉴于 Defender 支持的文件格式繁多，仅依靠随机变异策略难以实现充分的代码路径覆盖。高质量的初始语料库成为提升模糊测试效果的关键要素。

VX-Underground 平台提供了超过 20 万个恶意文件样本，覆盖 Defender 所需扫描的各类文件类型。研究团队投入数天时间，将该样本库导入 WTF 测试框架，代码覆盖率增长超过 10,000 个新路径。

最终实现的基本块覆盖率达到 154,000 个。

技术分析表明，对于支持多格式解析的目标程序，精心构建的初始语料库在测试效率上优于纯粹的覆盖率引导策略。

## 漏洞发现：九个内存安全问题

经过持续的模糊测试， WTF 框架成功发现 9 个不同的漏洞实例。

其中， Crash1 和 Crash2 具有重要研究价值——这两个漏洞无需 PageHeap 即可在标准环境下稳定触发 Defender 服务进程崩溃。

### Crash1 ： JAR 文件解析的越界读取

该漏洞涉及 Java 归档文件处理逻辑，调用栈从`mpengine!strncmp`延伸至`netvm_emulate`。值得注意的是，该漏洞在使用传统流扫描接口（`RSIG_SCAN_STREAMBUFFER`）时无法触发，仅在实际文件扫描场景中暴露。微软在收到漏洞报告后，在后续版本中进行了修复。

### Crash2 ： FilteredTrie 数据结构的空指针解引用

调用栈分析显示，问题出现在`FilteredTrie`数据结构中，`hstr_internal_search_worker`函数访问了空指针。该漏洞具有高度可重现性——Defender 扫描到该类文件时即发生崩溃，表现出稳定的故障模式。

### Crash6 ： Office 文档加密参数异常处理

该漏洞涉及 Office 文档加密参数解析。某个测试文档中的`saltSize`字段存在异常值：

```
Data saltSize="1" salt="..." 0" saltSize="17"
```

Defender 在解析加密参数时执行越界内存读取。该漏洞在 PageHeap 启用时更易触发，但研究团队通过修改测试用例，实现了在标准环境下的稳定复现。

其他漏洞实例（ Crash3 至 Crash8 ）均属于越界读取类型，但通常需要 PageHeap 支持，在生产环境中的触发难度相对较高。

## 攻击向量分析：拒绝服务到防御绕过

这些 DoS 漏洞的实际攻击价值体现在多个场景中。

### 场景一：初始访问与 Defender 绕过

攻击者通过钓鱼链接诱导用户下载伪造的"PDF"文件（实际为 JAR 或 Office 文档）。当 Defender 自动扫描该文件时触发崩溃，恶意代码得以在防护失效的情况下执行。

### 场景二：内网横向移动

在横向移动攻击场景中，攻击者已攻陷一台主机，需要向其他目标机器传输工具。然而，目标主机的 Defender 会拦截并删除传入的可疑文件。攻击者可先传输畸形文件触发 Defender 崩溃，随后传输实际攻击工具。

### 风险评估

基于 CVSS v4.0 标准评估，部分漏洞的评分为 6.8/10 （向量：本地/低复杂度/无权限要求/需用户交互/可用性影响高）。虽然未达到严重级别，但其防御绕过能力具有实际攻击价值。

## 调试分析：绕过 Defender 自保护机制

Defender 实现了进程保护（ PPL ）和内核回调机制，阻止常规调试器的访问。针对这一安全限制，存在两种技术绕过方案。

### 方法一： PPL 权限提升与内核回调修改

使用 PPLControl 工具将调试进程提升至 PPL-WinSystem 级别：

```
PPLControl.exe-elevatePPL-WinSystem
```

同时需要 patch Def ender 内核驱动`WdFilter.sys`中的回调函数，否则仍会阻止调试器 attach ：

```
0:kd>aWdFilter!MpObPreOperationCallbackfffff807`1e5cd100xoreax,eaxfffff807`1e5cd102ret
```

该回调函数原负责进程访问权限检查， patch 后的实现直接返回 0 ，相当于向内核传递"操作允许"的信号。

### 方法二：内核级调试

通过 WinDBG 建立内核调试会话，直接 attach 到`MsMpEng.exe`进程：

```
kd>!process00MsMpEng.exe kd>.process/i/pffffb385a10d0080 kd>g kd>bp/pffffb385a10d0080mpengine!UfsScannerWrapper::ScanFile
```

建立断点后即可对 Defender 的扫描逻辑进行单步调试分析。

## 厂商响应与漏洞处理机制

当研究团队通过 MSRC （ Microsoft Security Response Center ）报告相关漏洞时，微软的官方回复呈现标准化表述：

"After careful investigation, this case has been assessed as moderate severity and does not meet MSRC's bar for immediate servicing."

该评估将漏洞严重性定位为"中等"，认为"不符合立即修复标准"。然而，该研究成果公开发布一周内，所有报告的漏洞均得到修复。

这一现象表明，公开披露的压力能够有效影响厂商的漏洞修复优先级，相较于内部评估机制，外部舆论和行业关注具有更强的推动作用。

## 研究结论与未来方向

Defender 作为研究对象仅是一个起点。 CrowdStrike 、 Symantec 、 SentinelOne 等主流 EDR 产品面临相似的技术挑战：复杂代码库、多格式文件解析、高权限运行环境。

本研究验证了 Snapshot Fuzzing 方法论的有效性：在一个月测试周期内发现 9 个 DoS 漏洞。虽然未达到远程代码执行级别，但其防御绕过能力足以支撑实际攻击场景。

### 未来研究方向

1.**符号执行结合**：集成符号执行技术，分析代码逻辑层面的潜在漏洞路径

2.**智能化变异策略**：探索基于大语言模型（ LLM ）的智能变异算法，提升测试效率

3.**跨产品方法论应用**：将该模糊测试框架扩展至其他 EDR 产品

### 防御策略思考

当 EDR 产品本身构成攻击面时，传统防御策略面临新的挑战。多层防御架构、白名单机制、最小权限原则等安全措施需要重新评估其在对抗环境下的有效性。

完全安全的目标可能难以实现，但通过持续的安全研究和负责任的漏洞披露，能够推动厂商提升产品安全性，这是比假设"不可攻破"更务实的安全理念。

**如果你对网络安全、红队攻防技术充满热情，渴望学习更多实战技巧，例如渗透测试、自动化脚本编写、免杀技术等， 欢迎关注我的公众号**

**在这里，我会持续分享更多原创高质量的技术文章，与你一同探索网络安全的奥秘，提升实战技能！ 让我们一起在队攻防的道路上，不断精进，突破边界！**

> **免责声明：** 本文仅供安全技术研究与学习交流之用。 严禁将本文所提及的技术用于任何非法用途，包括但不限于未经授权的渗透测试、网络攻击、恶意代码传播等。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9QEM1M4pZoC2fAL6iaEWeibYnmGtM1yg4JiaDP1QBBYbMtpGpnrJGhYsiaS38X3DCznMpyKv8ujQXc1WwISaVjqUEw/0?wx_fmt=png)

红队工坊

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9QEM1M4pZoC2fAL6iaEWeibYnmGtM1yg4JiaDP1QBBYbMtpGpnrJGhYsiaS38X3DCznMpyKv8ujQXc1WwISaVjqUEw/0?wx_fmt=png)

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