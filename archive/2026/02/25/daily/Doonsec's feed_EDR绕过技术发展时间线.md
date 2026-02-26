---
title: EDR绕过技术发展时间线
url: https://mp.weixin.qq.com/s/Jfw3PrTG8lqOIMK5BpznzA
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:17.149279
---

# EDR绕过技术发展时间线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/anKpAVfrylv08ibmQtrXbVvPhAhkFO8HPiaaKle2Uichc1TxqEwmQGmpd8dMFiaTO04SfnDgtOK52UtOG9u3y4Qee3hiasXpAMqvM83V5j9LUSDI/0?wx_fmt=jpeg)

# EDR绕过技术发展时间线

原创

绝对防御局
绝对防御局

绝对防御局

![]()

在小说阅读器中沉浸阅读

> 很好的一个EDR攻防对抗指引路径，原文Block国内IP，内容配合AI翻译进行校对。
>
> 原文：https://www.covertswarm.com/post/timeline-of-edr-bypass-techniques

# EDR绕过技术的发展：历史时间线

终端检测与响应（EDR）解决方案与绕过技术之间的关系代表了网络安全领域最具活力的对抗战场之一。这种关系体现了整个网络安全行业，因为它符合我们经常用来描述该行业的猫鼠游戏比喻。

随着EDR系统从简单的基于签名的检测发展为复杂的行为分析引擎，红队和威胁行为者不断开发创新方法以规避检测。本时间线记录了EDR绕过技术的主要突破，记录了塑造现代攻击性安全的技术演变。

许多变化已经发生，许多想法已被武器化，本文旨在总结这些变化并成为攻击性安全专家的参考。

## 奠基年代 (2010-2015)

### 早期EDR的局限性和基本绕过

第一代EDR解决方案严重依赖基于签名的检测和基本的行为启发式方法。在此期间，绕过方法相对简单，通常涉及简单的混淆技术或进程空洞化方法来规避检测。

### 2012-2013：进程空洞化(Hollowing)和DLL注入

早期EDR绕过领域主要由传统的进程注入技术主导。安全研究人员开始系统地探索以下方法：

* 使用CreateRemoteThread的经典DLL注入
* 进程空洞化（RunPE）技术
* 手动DLL加载以避免导入地址表（IAT）挂钩

这些技术之所以有效，是因为早期EDR解决方案主要监控高级Windows API，而没有深度内核级别可见性。

### 2014：反射式DLL加载

Stephen Fewer的反射式DLL加载技术成为EDR规避的基石。通过手动加载DLL而不使用Windows加载器，攻击者可以绕过许多监控标准DLL加载过程的挂钩机制。这项研究至今仍然相关，并被许多知名的C2框架广泛使用。然而，最近为了规避反射式DLL加载的行为检测，已转向位置无关代码（PIC）。

## 挂钩战争开始 (2015-2017)

### 理解EDR检测机制

随着EDR解决方案的成熟，它们开始实施更复杂的挂钩机制来监控API调用。这一时期标志着EDR供应商和绕过开发者之间所谓的“挂钩战争”的开始。

### 2015-2016：API Hooking 意识

安全研究人员开始系统地分析EDR解决方案如何实现其监控能力：

* 用户态API Hook：EDR解决方案开始挂钩关键的Windows API，如NtCreateFile、NtCreateProcess和NtAllocateVirtualMemory
* 内联挂钩：许多EDR产品使用内联挂钩技术，修补API函数的前几个字节以重定向执行到其监控代码
* IAT挂钩：导入地址表修改成为EDR的常见技术

### 2016：UnHooking 技术的兴起

安全社区开始开发系统方法来检测和移除EDR挂钩：

* 挂钩检测：将内存中的API函数与其磁盘上的版本进行比较
* API解挂钩：从磁盘加载的干净副本中恢复原始API字节
* 手动映射：加载系统DLL的干净副本以访问未挂钩的API

## 直接系统调用革命 (2017-2019)

### 2017：引入直接系统调用（Direct Syscalls）

直接系统调用技术的引入标志着EDR绕过方法论的范式转变。攻击者开始利用底层系统调用，而不是调用EDR解决方案监控的高级Windows API。

关键突破：Jackson T (@Jackson\_T) 的 SysWhispers

SysWhispers项目于2019年发布，通过提供以下功能将直接系统调用民主化：

* 自动生成系统调用存根
* 支持多个Windows版本
* 易于集成到攻击性工具中

技术创新示例：直接系统调用存根 NtAllocateVirtualMemory：

```
1. mov r10, rcx
2. mov eax,18h     ;NtAllocateVirtualMemory的系统调用号
3. syscall
4. ret
```

该技术通过直接过渡到内核模式完全绕过用户态API挂钩，使EDR解决方案在没有内核级组件的情况下极难监控。

### 2018-2019：系统调用的演变

* Hell’s Gate：Am0nsec和Smelly\_\_vx开发了在运行时动态解析系统调用号的技术
* Halos Gate：Reenz0h扩展了Hell's Gate，通过在附近函数中搜索干净的系统调用号来处理挂钩的系统调用
* Tartarus’ Gate：Paul Laîné改进了先前的技术，提高了可靠性和规避能力。

## 间接系统调用时代 (2019-2021)

### 2019-2020：间接系统调用和调用堆栈意识

随着EDR解决方案开始监控直接系统调用，研究人员开发了间接系统调用技术，以维持更自然的调用堆栈。

间接系统调用突破：

间接系统调用不是直接从攻击者控制的代码执行系统调用，而是使用现有的合法代码路径：

* 基于ROP的系统调用：使用返回导向编程从合法模块执行系统调用
* 基于JOP的系统调用：用于系统调用执行的跳转导向编程变体
* 模块踩踏：用系统调用存根覆盖合法模块的代码段

### 2020：调用堆栈欺骗技术

研究人员意识到EDR解决方案开始分析调用堆栈以检测可疑活动：

* 返回地址欺骗：修改返回地址使其看起来合法
* 堆栈切换：更改堆栈指针以使用合法的调用堆栈
* 帧指针操作：修改帧指针以创建令人信服的调用堆栈跟踪

关键工具和研究：

* SysWhispers2：扩展了原始SysWhispers，增加了间接系统调用功能
* Ekko：使用间接系统调用的C5pider睡眠混淆技术
* ThreadStackSpoofer：Mgeeky的调用堆栈欺骗实现

## 高级规避技术 (2020-2022)

### 2020-2021：内存保护和混淆

睡眠技术：

* Ekko睡眠混淆：在睡眠期间加密信标内存
* Zilean：具有多层加密的高级睡眠混淆
* Gargoyle：使用计时器和APC进行隐蔽执行

内存规避：

* 模块重载(Module Overloading)：在合法模块上加载恶意代码
* 幻影DLL加载(Phantom DLL Loading)：加载DLL而不将其注册到PEB中
* Transacted Section Techniques：使用NTFS事务进行隐蔽内存分配

### 2021：基于硬件的规避

硬件断点规避：

* 硬件断点检测：识别并清除EDR设置的硬件断点
* 调试寄存器操作(Debug Register Manipulation)：直接修改调试寄存器以规避监控

性能计数器滥用：

* 基于PMU的检测：使用性能监控单元检测EDR存在
* 基于时间的规避：利用挂钩与未挂钩API的时间差异

## 现代时代：VEH和高级技术 (2022至今)

### 2022：向量异常处理Vectored Exception Handling（VEH）技术

基于VEH的系统调用：

研究人员开始使用向量异常处理程序实现隐蔽的系统调用机制：

* 基于异常的控制流：使用受控异常重定向执行
* VEH劫持：劫持现有的VEH链以实现隐蔽执行
* 硬件异常滥用：使用单步调试等硬件异常

关键创新：FreshyCalls

ElephantSe4l的FreshyCalls技术使用系统调用蹦床和VEH创建高度规避的系统调用实现。

### 2022-2023：内核回调技术

PsSetCreateProcessNotifyRoutine绕过：

* 回调移除：移除EDR注册的进程创建回调
* 回调修补：修改回调函数以绕过监控
* DKOM技术：直接内核对象操作以规避检测

ETW（Windows事件跟踪）绕过：

* ETW提供者修补：禁用EDR解决方案使用的ETW提供者
* ETW会话劫持：控制ETW会话
* 跟踪篡改：实时修改ETW跟踪

### 2023：高级内存操作

CRT挂钩绕过：

* CRT函数替换：替换C运行时函数以绕过监控
* 静态与动态CRT：利用CRT链接方法的差异

高级进程注入：

* 进程Doppelgänging：使用NTFS事务进行隐蔽进程创建
* 进程Herpaderping：加载后覆盖进程镜像
* 幽灵写入(Ghost Writing)：通过文件映射写入进程内存

## 当前状态和新兴技术 (2024至今)

### 2024：AI和机器学习规避

行为模仿：

人工智能在网络安全中的出现代表了EDR绕过方法论的重大转变，自直接系统调用以来。与传统的静态混淆不同，AI驱动的规避技术可以创建实现行为真实性的恶意软件，生成对自动化系统和人类分析师都显得真正良性的执行模式。

基于机器学习的行为克隆可以允许攻击者系统地研究和复制合法应用程序模式，创建高度针对性的模仿，可以欺骗针对特定应用程序配置文件训练的EDR系统。更令人担忧的是自适应规避系统，它们从失败的检测尝试中学习，实时不断进化其策略。这创造了一个反馈循环，每次检测尝试都可能教会规避系统如何更好地避免未来的检测。TrustedSec在2022年关于用户行为分析的研究表明，这是一个现在感兴趣的研究领域，因为技术已经发展到系统可以利用这个概念的程度。

## 著名工具和框架

### 历史工具时间线

2015-2017：基础工具

* PowerShell Empire：具有EDR规避能力的早期C2框架
* Cobalt Strike：推动了许多创新的商业C2平台
* Metasploit：具有不断发展的规避模块的开源框架

2018-2020：系统调用时代工具

* SysWhispers：直接系统调用生成工具
* Hell’s Gate：动态系统调用解析
* Halos Gate：增强的系统调用解析与挂钩规避

2021-2023：高级规避工具

* SysWhispers2：间接系统调用实现
* Ekko：使用系统调用的睡眠混淆
* ThreadStackSpoofer：调用堆栈欺骗实现
* FreshyCalls：基于VEH的系统调用实现

2024至今：现代框架

* SysWhispers3：最新演变，具有增强的规避能力
* Nighthawk：具有多种规避技术的高级C2
* Brute Ratel：内置EDR规避的现代C2框架
* 开源C2：Adaptix和Havoc推动商业C2框架创新

## 关键技术

### 直接系统调用

直接系统调用通过直接调用内核服务绕过用户态API挂钩。该技术涉及：

* 解析目标API的系统调用号
* 根据调用约定设置处理器寄存器
* 执行系统调用指令以过渡到内核模式

### 间接系统调用

间接系统调用通过从合法代码位置执行系统调用来维持自然的调用堆栈：

* 在合法模块中找到以syscall; ret结尾的小工具
* 设置堆栈以返回到这些小工具
* 跳转到小工具而不是直接执行系统调用

### 调用堆栈欺骗

调用堆栈欺骗通过以下方式创建令人信服的调用堆栈跟踪：

* 分析合法的调用堆栈模式
* 操纵返回地址以匹配预期模式
* 使用ROP/JOP链保持堆栈一致性

### VEH技术

向量异常处理技术使用Windows的异常处理机制：

* 注册自定义异常处理程序
* 触发受控异常以重定向执行
* 使用单步调试等硬件异常实现隐蔽性

## 军备竞赛：EDR响应和反演变

### EDR适应

内核级监控：

现代EDR解决方案通过以下方式响应用户态绕过：

* 内核回调：进程、线程和镜像加载通知
* 过滤驱动程序：文件系统和注册表监控
* ETW集成：全面的事件跟踪

行为分析：

* 机器学习模型：检测异常行为模式
* 调用堆栈分析：识别可疑执行流
* 内存模式识别：检测内存中的已知攻击签名

硬件集成：

* Intel CET支持：利用控制流强制技术
* 硬件断点：使用调试寄存器进行监控
* 性能计数器：通过时间分析检测规避

### 反制措施

攻击性安全社区通过以下方式回应EDR的改进：

* 内核级规避：直接操作内核结构
* 基于硬件的绕过：利用处理器特性进行规避
* 供应链攻击：使用合法的签名二进制文件
* 活用系统工具：滥用合法的系统工具

## 挑战和考虑

### 伦理影响：

EDR绕过技术的进步引发了关于以下重要问题：

* 负责任的披露实践
* 红队能力和实际威胁行为者工具之间的平衡
* 恶意行为者滥用的潜在风险

### 检测与规避平衡：

检测和规避技术之间的持续军备竞赛继续推动攻击性和防御能力的发展，最终通过对抗性测试改善整体网络安全态势。

## 结论

EDR绕过的历史代表了对抗性网络安全研究中的一个引人入胜的案例研究。从简单的API unhooking 到复杂的基于硬件的规避，每次突破都推动攻击者和防御者开发更先进的技术。理解这种演变对双方的安全专业人员都至关重要，因为它提供了对端点安全基本挑战和对抗压力下出现的创造性解决方案的洞察。

时间线显示了清晰的模式：随着EDR解决方案实施新的检测机制，攻击性安全社区会以创新的绕过技术作出回应。这种改进循环通过识别弱点和推动防御技术创新使整个网络安全生态系统受益。

展望未来，人工智能、硬件安全特性和云原生技术的集成可能会定义这场持续军备竞赛的下一阶段。组织必须了解这些发展，以在日益复杂的威胁环境中保持有效的安全态势。

## 参考文献

1. Fewer, S. (2014). “Reflective DLL Injection.” Harmony Security. https://github.com/stephenfewer/ReflectiveDLLInjection
2. Jackson\_T. (2019). “SysWhispers: On-disk and in-memory evasion techniques.” https://github.com/jthuraisamy/SysWhispers
3. Am0nsec & Smelly\_\_vx. (2019). “Hell’s Gate: Dynamically retrieving system call numbers.” https://github.com/am0nsec/HellsGate
4. Reenz0h. (2020). “Halos Gate: A new technique for dynamically retrieving syscall numbers.” https://blog.sektor7.net/#!res/2021/halosgate.md
5. Laîné, P. (2021). “Tartarus’ Gate: 利用地狱之门绕过 EDR。” https://github.com/trickster0/TartarusGate
6. C5pider. (2021). “Ekko: 睡眠混淆。” https://github.com/Cracked5pider/Ekko
7. Mgeeky. (2021). “ThreadStackSpoofer: 模拟线程调用栈的 PoC。” https://github.com/mgeeky/ThreadStackSpoofer
8. ElephantSe4l. (2022). “FreshyCalls: 使用 VEH 的系统调用。” https://github.com/crummie5/FreshyCalls
9. modexp. (2020). “进程注入技术。” Modexp 博客。 https://modexp.wordpress.com/
10. Red Canary. (2021). “EDR 逃避技术及应对措施。” Red Canary 威胁检测报告。
11. MITRE ATT&CK 框架. “防御逃避技术。” https://attack.mitre.org/tactics/TA0005/
12. Sektor7 恶意软件开发课程资料. (2020-2022). https://institute.sektor7.net/
13. Maldev Academy. (2022-2024). “恶意软件开发技术与 EDR 规避.” https://maldevacademy.com/
14. SpecterOps. (2021-2023). “对手模拟与红队研究.” 多篇博客文章和研究论文。
15. Elastic Security Labs. (2022-2024). “EDR 规避研究与检测工程.” 研究出版物和博客文章。

感谢关注 :)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rHFBVJjhUm1jM8mibjH9GRSRsI8weEH4KSrpsf6ygGmvTYt7DKTicgkYvbG9oDLTadzoktibS8UHjciaElJKIIHicgw/0?wx_fmt=png)

绝对防御局

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rHFBVJjhUm1jM8mibjH9GRSRsI8weEH4KSrpsf6ygGmvTYt7DKTicgkYvbG9oDLTadzoktibS8UHjciaElJKIIHicgw/0?wx_fmt=png)

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