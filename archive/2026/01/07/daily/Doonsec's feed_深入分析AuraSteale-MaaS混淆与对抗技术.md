---
title: 深入分析AuraSteale-MaaS混淆与对抗技术
url: https://mp.weixin.qq.com/s/g6Jp46nUANJj6bTOGNTrug
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:27:46.325451
---

# 深入分析AuraSteale-MaaS混淆与对抗技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1Cj6R04iczen78tNGRAwauj5Ln5DiahYiaQobns7yPte5ceKpUoETHuLJqUg/0?wx_fmt=jpeg)

# 深入分析AuraSteale-MaaS混淆与对抗技术

原创

Ti

TIPFactory情报工厂

![]()

在小说阅读器中沉浸阅读

## 前提要点

---

* AuraStealer 是一种新兴的恶意软件即服务 (MaaS) 信息窃取者。
* 为了阻止静态和动态分析，AuraStealer 采用了广泛的反分析和混淆技术，包括间接控制流混淆和异常驱动的 API 哈希。
* 在这篇技术博客文章中，我们深入探讨了恶意软件的执行流程和功能，并提供了对抗其混淆的实用技巧和工作流程。

## 介绍

---

AuraStealer 是一种快速发展的信息窃取程序即服务，自 2025 年 7 月以来在多个地下论坛上积极推广。该窃取程序采用 C++ 开发，构建大小约为 500-700 kB，针对从 Windows 7 到 Windows 11 的 Windows 系统。它被宣传为高效、占用空间少的窃取程序，能够从 110 多个浏览器、70 个应用程序（包括钱包和 2FA）窃取数据工具），以及超过 250 个浏览器扩展，能够通过可定制的配置进一步扩展其收集范围。与广告宣传相反，AuraStealer 仍然存在多个缺陷，这些缺陷削弱了其隐身和规避能力，为防御者提供了清晰的检测机会。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjlEIPqqHvdfMaICHOgMhWibQuicDWMy4Mw8rUqbjKbfZlavVibEFNj2ZCQ/640?wx_fmt=jpeg&from=appmsg)

图 1：AuraStealer 在地下论坛上推广。

infostealer 通过分层订阅模式提供，**基本****计划** 定价为 $295/month and the **Advanced****plan** at $585/月。这些层的主要区别在于配置灵活性、数据过滤和操作可扩展性。第三层，**团队计划**，目前正在开发中，预计将引入专为协作使用而定制的功能。此外，还提供临时**试用套餐**，两周订阅价格为 165 美元，其中包括 **基本计划** 的所有功能。 **试用版**仅在 30 天的时间内可供购买，旨在在新用户承诺完全订阅之前吸引他们。

订阅包括访问专用网络面板，用于管理和查看基于 Tabler 模板构建的被盗数据。鉴于该面板和窃取程序最初仅以俄语提供，因此可以合理地假设开发人员在俄语网络犯罪社区内运作。然而，这并不一定表明它们的确切起源。该面板现已更新，现在支持俄语和英语。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjmTebceziaEulYQM5DmbYuGqSQTjmPt4InBceAo3V8INPOFGzic9Xo46A/640?wx_fmt=jpeg&from=appmsg)

图 2：AuraStealer 的网页面板概述。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjQVibktZnCay8ia0DhCqbpQWdk7LkjbpibmaTM86FgetwIEoyv43BLr7ag/640?wx_fmt=jpeg&from=appmsg)

图 3：AuraStealer 的网络面板及其日志管理界面，包括过滤选项和被盗记录的详细列表。

## 概览

---

AuraStealer 主要通过 Scam-Yourself 活动进行传播， 抖音视频 伪装成产品激活指南就是其中之一。在这些视频中，受害者被看似简单的教程所吸引，承诺免费激活其他付费软件。观看者被指示在管理 PowerShell 中手动重新键入并运行显示的命令，但是，该命令不会激活软件，而是悄悄下载并执行恶意负载。可以找到这些视频的具体示例以及完整的执行链和其他 IoC 这里.

除了 TikTok Scam-Yourself 活动之外，AuraStealer 还通过所谓的破解游戏或软件进行分发，其交付链的复杂程度各不相同。在最简单的情况下，仅执行 AuraStealer 的 UPX 打包版本，而不需要额外的阶段，而更复杂的活动则采用多阶段执行流程，涉及自定义加载程序、DLL 侧面加载、注入合法进程或其他中间步骤。我们还观察到 AuraStealer 通过恶意 VS Code 扩展与 GlassWorm 一起交付。总而言之，这些观察表明 AuraStealer 纯粹作为窃取器本身出售，没有加载程序层或额外的交付机制。

确定 AuraStealer 威胁的确切范围具有挑战性，因为我们经常在最终有效负载执行之前的早期阶段阻止其传输链。虽然主动防御对于保证用户安全至关重要，但它也会导致许多 AuraStealer 有效负载永远无法到达系统。因此，不仅要观察和量化威胁的全部范围，而且要确定被阻止的有效负载是否确实旨在传递 AuraStealer，本身就变得困难。

例如，如果它通过 ClickFix（最近最广泛采用的交付技术之一）交付，我们将在剪贴板阶段主动防御这些攻击 剪贴板保护 特征。 ClickFix 通常指的是一种技术，向用户呈现人为生成的错误或问题，必须解决这些错误或问题才能继续，同时向用户提供解决问题的分步说明。这些步骤通常包括复制命令并通过 Windows 运行对话框或其他系统提示符运行它，但这并没有解决问题，而是默默地检索并执行恶意负载。

总而言之，AuraStealer 尚未像目前主导威胁领域的更成熟的信息窃取者家族（例如 Lumma Stealer、StealC 或 Vidar）那样广泛和流行。

## AuraStealer 混淆

AuraStealer 融合了多种旨在阻碍静态和动态分析的技术。其中包括控制流混淆、字符串加密、持续混淆以及标准的反调试、反篡改和反虚拟机检查。它还采用了先进的技术，例如异常驱动的 API 哈希、利用 Heaven's Gate 进行可疑的 NTDLL 调用以及执行检查以检测返回地址上的断点。

### 间接控制流混淆

在反汇编程序（例如 IDA Pro）中打开 AuraStealer 时，分析人员可能遇到的第一个混淆技术是其间接控制流混淆。这种混淆不仅可以立即引起注意，而且也是正确分析窃取者必须克服的最麻烦的障碍之一。混淆基于系统地用间接跳转和调用替换直接跳转和调用，其中实际目标地址仅在运行时计算。这种方法有效地破坏了静态分析，因为反汇编程序留下了一组看似不相关的基本块，从而有效地破坏了任何控制流图分析或反编译。

为了演示这种混淆在实践中如何发挥作用以及如何克服它，我们重点关注 `WinMain` 函数，这是窃取器中最长且最复杂的函数。下面的图 4 显示了说明汇编级别的混淆机制的几个示例，其中与计算每个目标地址相关的指令以不同的颜色突出显示。值得注意的是，该屏幕截图还说明混淆成功地混淆了 IDA，导致其误解整个数据 `WinMain`作为单个基本块运行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjQKuXGcqZ2nZapFAlh5neCOCq4Alfll0V8KLQUBiaNfbZE4lf8XP3vTQ/640?wx_fmt=jpeg&from=appmsg)

图 4：WinMain 函数的反汇编代码，通过间接控制流混淆进行混淆。不同的颜色用于标记影响特定间接跳转/调用的指令。

如图所示，根据分支上下文，目标地址以几种不同的方式计算，范围从两个值的简单算术和（以绿色、蓝色和红色突出显示）到更复杂的方式，其中生成的目标地址可能采用多种可能的形式，最终选择由条件指令确定，例如 `cmovz`（以粉红色突出显示）。

此时，读者可以很容易地得出结论，一些模式匹配、模拟和修补就足以消除混淆——这也是我们最初的假设。然而，事实证明，AuraStealer 使用了这些间接控制流混淆方案的多种变体，其中一些采用了更为复杂的模式。例如，目标地址甚至可能取决于多个先前函数调用的返回值，因为其计算涉及由这些结果驱动的条件指令（参见图 5）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjtuMicxJwUIwHR34iaiaibD1XgQbRICzqtVvRbWaias3mWRTf1M7B9z6XuXg/640?wx_fmt=jpeg&from=appmsg)

图 5：用于计算间接条件跳转的目标地址的更复杂的混淆变体的示例。

尽管如此，尽管这些混淆方案具有多样性和潜在的复杂性，但仍然有办法处理它们并重建原始控制流。首先，用于混淆函数调用的最基本方案，该方案仅依赖于两个值的总和，可以通过 IDA Pro 中的一个简单技巧来解决。在这些情况下，向 IDA 提示有助于求和运算的偏移量实际上是恒定的就足够了。一旦被视为常量操作数，IDA 就可以自行评估算术并相应地对其进行优化，从而允许反编译器揭示实际调用的目标地址。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjtdqKNDjeh7Bb2sYAolYbUBLiamzxAOJTwFg2xcrQ751fib4U03BSvdug/640?wx_fmt=jpeg&from=appmsg)

图 6：使用 IDA Pro 中的“Set type”命令（快捷键 Y）将偏移标记为常量。

图 7 和图 8 说明了该技巧的效果以及反编译输出中产生的差异。可以看出，即使是这样的微小调整也可以显着改善分析，因为它用对实际目标函数的直接引用取代了这些原本无意义的偏移和计算。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1Cj94kYV8svPaKiaOc2MOSe9XBsf7FBps5a3DU1lW7vRsiapQVjyL2yZmlQ/640?wx_fmt=jpeg&from=appmsg)

图 7：将偏移量标记为常量之前 WinMain 函数的反编译代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjSzsEIF39uibu9OPicfKicaxhzuGNibRoLWQuia9buEB0ric6OI8abqia31fvg/640?wx_fmt=jpeg&from=appmsg)

图 8：将偏移量标记为常量后 WinMain 函数的反编译代码。

由于这些偏移引用通常出现在连续的块中（图 9），因此自动化它们的处理是很实用的，图 10 中所示的 IDA Python 片段对此特别有用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1Cj1jibsqW6feyGtL4azh47XZ8FGBiapdXXlmtpOkSgGbeTCbmm4eG2H3yg/640?wx_fmt=jpeg&from=appmsg)

图 9：用于间接 jmp/call 计算的长偏移序列。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1Cjx55A83Sp2icHNb9WfjnSJYC3qVP16AYdSFoqicQkzHkq5MficxfQOry4A/640?wx_fmt=jpeg&from=appmsg)

图 10：将多个偏移引用标记为常量的 IDA Python 片段。

不幸的是，仅此技巧不足以解决 AuraStealer 间接控制流混淆的条件跳转和其他方案。尽管如此，考虑到有多少调用被这个简单的方案混淆，应用它仍然提供了有意义的进展，并且可以作为进一步反混淆的坚实起点。此外，AuraStealer 还应用相同的混淆方案来隐藏某些函数参数，使其也适用于这些情况。

为了解决更复杂的模式，**向后切片**被证明是最有效的方法。对于那些有兴趣更详细地解释该技术如何工作的人，可以阅读以下文章 *LummaC2：通过间接控制流进行混淆* 作者：Nino Isakovic 和 Chuong Dong，以及 *Rhadamanthys 加载器反混淆* Melissa Eckardt 的著作提供了出色的解释，绝对值得一读。

简而言之，向后切片是一种程序分析技术，它通过跟踪数据和控制依赖性来识别可能影响特定程序点处的特定寄存器或内存地址的指令。然后，所得指令集（也称为“切片”）可用于进一步分析，例如仿真或符号执行，以恢复目标寄存器或内存位置的值。

在我们的例子中，我们采用了一种启发式方法，其灵感主要来自向后切片，但经过简化并专门为 AuraStealer 量身定制。该启发式可以概括为以下步骤：

1. 找到间接的 `jmp/call` 操作说明。
2. 添加用作该间接的目标操作数的寄存器 `jmp/call` 指示给 `tracked_regs`放。
3. 反向迭代指令（从间接 `jmp/call` 朝向较低地址），分析每条指令是否影响任何被跟踪的寄存器。

1. 如果指令**修改**跟踪的寄存器，则将其标记为**相关**。
2. 对于相关指令，确定它是否完全覆盖跟踪的寄存器（例如， `MOV reg, imm`, `XOR reg, reg`\_**,**\_etc.)，如果是这样，则从中删除该寄存器 `tracked_reg`，结束其依赖链。
3. 否则，识别该相关指令的所有源寄存器并将它们添加到 `tracked_reg`设置为进一步传播依赖关系。

4. 如果发生以下任何情况，请停止该过程：

1. 这 `tracked_regs`设置为空（所有依赖项均已解决）。
2. 遇到控制流指令（`call`, `jmp`, `ret`），表示基本块边界。
3. 达到最大指令限制（故障安全）。

5. 最后，返回找到的最早（最低地址）相关指令的地址，标记切片的开始。

为了清楚起见，这种启发式并不意味着实现完全的向后切片。它故意省略内存写入跟踪并仅关注寄存器流。然而，值得注意的是，这种限制是有意为之的，因为寄存器级分析足以对 AuraStealer 使用的间接控制流混淆进行反混淆。我们仅使用启发式方法来识别切片的起始地址，然后使用 Angr 执行符号执行来计算目标地址。也就是说，如果 AuraStealer 的混淆方式发生变化，启发式方法可以很容易地扩展到也能解释记忆交互。

我们选择符号执行而不是仿真的原因是符号执行本质上是为了探索所有可能的执行路径而设计的，使其更容易实现。就计算要求而言，它仍然可行，因为我们仅象征性地执行小代码块。

细心的读者可能已经注意到这种方法有一个小缺陷。启发式在遇到以下情况时终止 `call` 操作说明。然而，如图5所示，一些目标地址 `jmps` 可能依赖于先前函数调用的结果，这可能导致错误识别切片开始。为了处理这种情况，每当寄存器不受约束时，我们都会为其分配一个符号布尔值（0或1），假设任何影响此类跳转的函数都会返回一个布尔值。然而，这种情况相对较少。

整个过程可以通过一些脚本实现自动化，并且恢复的目标地址可以作为注释推回 IDA，这已经为导航代码提供了良好的基线。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjmWmDY8faY2dJKxRVN2icicZmVLPpWGhhu8XIIM1Ls7W8q7nv5IaBhzrQ/640?wx_fmt=jpeg&from=appmsg)

图 11：恢复的目标地址在 IDA Pro 中设置为注释。

然而，我们可以更进一步——我们真正的目标是让 IDA 重建原始的控制流图，而不仅仅是对其进行注释。一旦间接的目标地址 `jmps/calls` 检索后，有多种方法可以继续。一种选择是修补二进制文件。 However, due to the variability of the patterns involved and the presence of an anti‑tamper protection in AuraStealer, we have opted for a different approach.

我们没有对具有破坏性且容易被恶意软件检测到的二进制文件进行修补，而是利用 IDA SDK 直接挂钩指令分析过程。这个想法很简单——我们不是让 IDA 自己分析指令，而是干预分析过程并修改指令的解码方式。为此，IDA 提供 `post_event_visitor_t`，一个类，允许通过重写虚函数来监听 IDA 中的特定事件并做出反应 `handle_post_event`.

![](https://mmbiz.qpic.cn/mmbiz_jpg/aPCLBuONer7O5YxHwQ09ibw3ibPyiauJ1CjiaKcjv5cJL9ge9tctZX2X4icqhkjA8rvaBnZOdkh4bSLeuBuD0BwhKsg/640?wx_fmt=jpeg&from=appmsg)

图 12：handle\_post\_event 虚函数的声明。

在所有可能的事件代码中，有趣的是 `processor_t::ev_ana_insn` （分析指令），在 IDA 调用处理器模块的指令解码器之后、结果之前立即触发 `insn_t` 结构最终确定并提交到数据库。此时，我们可以检查甚至修改解码后的指令。换句话说，我们可以改变 IDA 对代码的感知，而无需触及底层二进制文件。

在这一点上，有几点值得强调：

* 间接调用几乎总是有一个目标。
* 许多条件跳转只有两个目标，其中之一是紧随其后的指令。

因此，解决间接调用混淆很简单。每当我们拦截 `processor_t::ev_ana_insn` 事件，我们检查分析的指令是否是间接调用（`call reg`）。如果目标地址已知并且它是唯一可能的目标，我们将替换 `call reg` 指令与 `call <calculated_target_address>`.

对于间接条件跳转，原则上可以通过分析用于计算目标地址的条件移动并替换 `jmp` 指令与相应的条件跳转指令。然而，我们...