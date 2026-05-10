---
title: 如何使用MCP进行自动化漏洞挖掘
url: https://mp.weixin.qq.com/s/iXD6k9US4xyMI8FQ5qcgvg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:53.984171
---

# 如何使用MCP进行自动化漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjK6jXl6x0mP7nGcfkhuMJDCHoBk62sM1IDtdOtHL8htNUrDp02WsI16UBkQe2SUZYZxGntZx9J0VGJSxgmpL9rlCd8psj4icWc/0?wx_fmt=jpeg)

# 如何使用MCP进行自动化漏洞挖掘

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

最近我有一周时间不在我的"日常工作"上，所以决定真正整理一下我的业余项目，处理各种管理任务。不过，写这篇文章，关于那个0day的"机器"，是我几周来一直想做的一件事。

我将深入探讨我是如何使用Claude Code和MCP构建一个自动化漏洞挖掘系统的，以及它在此过程中发现的一些漏洞。从我所在的一个群里还诞生了一句有趣的引语：

> Andy基本上是在让AI充当苦力

这个标题来源于GenAI = Jenny以及这首歌：

我从2026年初就开始构建这个系统，起初是在我的空闲时间，主要是我通常失眠的半夜；最终它演变成了一个成熟的研究工作流。我也会在文章中谈到这点，但这也是我构建TokenBurn的原因，用于计算我在Claude Max和硬件上的投资回报率：

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgQQGz2HLzF7v5U6UYG2DZRlGTGLYTObKWrKh9m4fiazoAZoPiaibPWDr0rZ3by5KdKWmZZGt4BGB5ERxGiaDPvfeliawM3UbA4vYks/640?wx_fmt=png&from=appmsg)

众所周知，使用大型语言模型(LLM)进行安全研究并非新鲜事，构建自定义工具来自动化漏洞挖掘中枯燥的部分也不是什么新鲜事，自动化模糊测试已经存在多年了。早在2014年，我就和Stephen Sims聊过关于他如何进行大规模模糊测试，这与我今天的设置没什么不同，只是当时没有集成LLM。然而，事实证明，结合Claude Code的MCP（模型上下文协议）和一个专门构建的实验环境，效果出奇地好。我知道可能有成百上千的人在做同样的事情，但无论如何，以下是我整合的内容、它是如何工作的，以及一些劳动成果。

最初的动机来自于我在处理工具上花的时间比实际挖掘漏洞还要多。通常的过程大致如下：连接到虚拟机，部署一个二进制文件，反编译它，映射攻击面，设置模糊测试，分析崩溃，编写概念验证(PoC)，起草披露报告，提交给供应商或赏金计划。每一步都有自己的工具、自己的输出格式以及需要传递到下一步的上下文。我希望Claude来处理这些繁琐的工作，而我来进行思考和写作，因为我们都知道AI写出来的东西不像人写的，而且我想在一定程度上保持对自己技术能力的掌控。

## MCP快速概览

在深入细节之前，先为不熟悉的人快速介绍一下MCP。模型上下文协议允许你将工具作为可调用函数暴露给Claude Code。可以把它想象成给Claude提供对你终端命令的原生访问权限，但结构化了输入和输出的类型。每个MCP服务器只是一个注册工具的Python进程，Claude在对话中直接调用它们。无需复制粘贴终端输出，无需切换窗口。

方法相当直接：将我研究工作流中的每个工具都包装成一个MCP服务器。最终，我拥有分布在5个虚拟机上的8个MCP服务器，以及超过300个工具（我不会列出具体细节，但这里是一个粗略概述）：

| 服务器 | 用途 |
| --- | --- |
| **实验控制器** | SSH/WinRM会话，Proxmox虚拟机管理，基础逆向工程(RE) |
| **猎人** | 补丁差异分析，攻击面枚举，10个模糊测试领域，崩溃分析，活动管理 |
| **逆向工程工具** | Ghidra、radare2、Frida及其他工具 |
| **漏洞利用开发** | Shellcode生成，堆喷射，控制流防护(CFG)绕过，PoC汇编，模拟执行 |
| **调试器** | 持久的WinDbg/GDB会话，能够在工具调用之间保持存活 |
| **检索增强生成(RAG)** | 对所有活动数据、发现结果和先前研究的语义搜索 |
| **基础设施** | 在Proxmox上配置和扩展模糊测试虚拟机 |
| **报告** | 披露报告，赏金提交，CVE请求 |

每个虚拟机旁边的彩色圆点表示其所属的类别及其分配的MCP，这让我可以快速识别每个虚拟机的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgB43HQs5nVlROJIibF3tXW1YjkqOPwiabLChE27u5W3Ny15CIqWDXx2ia0oOznH2lQficibyVo3GiaYGwicfWLT8mMhqemZQ0zxkXBKQ/640?wx_fmt=png&from=appmsg)

所有八个服务器都作为独立的Python进程在Claude Code下运行，并注册在同一个`.mcp.json`文件中。当Claude需要检查Windows目标上加载了哪些驱动程序时，它会调用`tool_surface_kernel_drivers`。当它需要反编译一个函数时，它会调用`tool_re_ghidra_decompile`或众多可用逆向工程工具中的一个。当它需要启动一个模糊测试活动时，它会为我想要选择的领域调用相应的`tool_*_fuzz_start`，该工具会调用直接的工具并开始工作。

每个服务器都是使用FastMCP构建的。服务器文件本身是简洁的`@mcp.tool()`包装器；实际的业务逻辑位于子目录中(`hunter/`、`re_tools/`、`exploit_tools/`、`debug_tools/`)。会话（SSH、WinRM）在对话和子代理中的工具之间持续存在，所以你只需连接一次，之后的一切都会正常工作。

## 实验环境

这项研究运行在一个基于Proxmox的"狩猎"范围上，该范围在隔离的网络段中包含5个虚拟机。我正在重写我的家庭实验室系列文章，但这是我新主机的规格，它将取代我家庭实验室系列中现有的NUC。https://blog.zsec.uk/homelab-clustering-pt1/

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgkYNI9UiavyQib1XlrADIscuPeDz0MbLbmibAypqXzcsxMoRcFlUfvOOAN0UEsrBmbxRtFkiaQThAIfLVrmJj228lA5fickSmRMZZg/640?wx_fmt=png&from=appmsg)

这里没有什么特别新奇的东西（除了它们都拥有相当高的规格，因为它们运行在我的新家庭实验室主机上），只是为工作流量身定制的：

| 虚拟机 | 平台 | 角色 |
| --- | --- | --- |
| **hunt-win11** | Windows 11（最新补丁） | 主要目标 |
| **hunt-win11-n1** | Windows 11（前一版补丁，N-1） | 与前一个"补丁星期二"进行二进制差异分析 |
| **hunt-winserv** | Server 2022 | RPC、服务、Active Directory(AD)攻击面 |
| **hunt-kali** | Kali Linux | Ghidra、radare2、GDB/pwndbg、angr、Volatility3 |
| **hunt-fuzz** | Windows 11 | 专用模糊测试（WinAFL、Jackalope、DynamoRIO） |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiaNaoWzXJQXE6TIomQOTib41kWLd8bM8NibI6PCuiaQYFibmzram0hT7dd82B0E9YQia1Q9rPOTkJN8Ibs3svibrShVZfCibasJdllNf4/640?wx_fmt=png&from=appmsg)

感谢Claude提供的可视化效果

每个Windows虚拟机还设置了一个`lowpriv`标准用户账户。这比你想的更重要。我稍后会详细解释原因，但简而言之，其中一个痛苦的早期教训是发现了从`SYSTEM`上下文看起来很棒，但作为普通用户完全无法触及的漏洞。

Windows的二进制文件通过SFTP(`tool_re_stage`)被部署到`hunt-kali`进行离线分析，这意味着`radare2`和`Ghidra`不需要在Windows目标本身上运行。这两个Windows 11虚拟机（最新和前一版补丁）专门用于支持二进制差异分析：枚举"补丁星期二"之间的变化，对二进制文件进行差异分析，并识别与安全相关的修复，以便针对特定活动进行目标锁定。我还有一个专门用于补丁差异分析的MCP。

## **活动与"幻觉垃圾桶"**

除非你与世隔绝，否则你可能已经深切地意识到，LLM模型会产生幻觉，它们会令人信服地告诉你一个谎言或将你引向歧途，因为它们在某种充满氧气的计算机梦境中产生了幻觉。

为了对抗这些"计算机毒瘾患者"，所有的狩猎工作都被组织成一个个活动。一个活动本质上是`hunts/campaigns/`下的一个目录，具有结构化的布局，用于存放发现、崩溃、覆盖数据、笔记和披露信息。使用`tool_campaign_create`创建一个活动，其他所有东西都附属于它。

现在，这是整个系统中最重要的设计决策，也是我希望在第一天就做出的决策：**所有发现都始于幻觉**。

每一个新发现都会进入`hallucinations/`目录，而不是`findings/`目录。只有在通过验证关卡后，它才会被提升：

**关卡 0:** 存在PoC并可编译**关卡 1:** PoC在干净的虚拟机快照中复现了崩溃**关卡 2:** 崩溃是可利用的（不仅仅是空指针解引用或优雅退出）**关卡 3:** 漏洞触发条件为普通用户，非SYSTEM或管理员

这听起来很偏执，而且有充分的理由，因为我在寻找可利用的漏洞，我希望系统拥有一定程度的自我认知能力，从我对它施压转为它对自己施压来识别缺陷。这让我免于向供应商提交无意义的东西，而且在流程中有人类的干预和思考也有帮助，这样就不会向项目和公司发送大量的报告和邮件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZia2MpInKeMJ9icJ65AfnNBgCcI8NOeiaxHf9rqestJ6Wt2KrxNoIpK43O8pq6uTWahAMULtYbcPlD6I4RhOeAbSKcOU9eGVga7ao/640?wx_fmt=png&from=appmsg)

例如，在一次早期的狩猎会话中，自主引擎通过手动分析标记了6个发现，日志和反编译输出中看起来很有希望，但经过手动审查和干预后，所有6个都在动态分析中被推翻，"幻觉垃圾桶"在它们接近最终报告之前就捕获了每一个。

提升流程是`tool_finding_promote` (`hallucinations/` → `findings/`)和`tool_finding_demote`（如果后续有东西被证明无效，则退回到原处）。很简单，但它强制执行了一个纪律：没有证据，任何东西都不能离开这个流水线。

## **知识循环**

这是我最满意的部分。每个模糊测试启动工具在启动前都会查询我自己的检索增强生成(RAG)索引，寻找先前的发现。每次崩溃和发现之后都会记录结果，目标是建立一个连续反馈循环，让系统随着每次狩猎而真正变得更智能。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiajOQjhBqryPQdUx4BPH4HVrC9rqCAfJVH1KvH5K1WRLPLuDCia0cdya8wYQRQFnK3KMhEGrH3sK0G1WyBI2fyNEjyEzqYW12LA/640?wx_fmt=png&from=appmsg)

早期RAG和模型的迭代版本

该循环的工作方式如下：

1. **狩猎** - 在开始一个活动前，查询知识库："我们以前在这个二进制文件或应用程序类型中看到过崩溃吗？哪些技术奏效了？哪些防御措施阻止了我们？"
2. **收集** - 所有10个领域中的每一次崩溃都会随着领域、目标和崩溃类别被记录。
3. **丰富** - 供应商安全公告、补丁差异、变体分析匹配、赏金提交以及覆盖平台期事件都会作为输入。
4. **学习** - 所有内容都会自动索引到一个带有句子的FAISS向量存储中。
5. **重复** - 下一次狩猎从更丰富的上下文开始。

如果我在一个活动中对`ntoskrnl.exe`进行模糊测试并发现了一个崩溃模式，那么下一个针对`ntoskrnl.exe`的活动就会知道它。跨活动的重复出现的漏洞类型通过语义相似性自动显现。去重无需手动操作。

该系统还维护一个已知防御数据库。当目标被证明是强化的反恶意软件保护进程(AM-PPL)、并行（SxS）保护、严格的Authenticode验证时，这些都会被记录。这些防御措施会成倍地降低目标在未来狩猎中的优先级分数，防止系统在相同的死胡同里浪费循环。在最初的几个活动撞上AM-PPL墙之后，系统就完全不再推荐这些目标了。

除了实验室的RAG索引，我还构建了一个单独的本地RAG系统，它索引了我过去十五年的笔记"大脑转储"以及5800多条公共Sigma规则、1025个精选的GitHub仓库、工具文档等总计超过561,000个数据块。它在本地使用Ollama运行，并且也作为一个MCP服务器工作，所以Claude可以在狩猎期间内联查询我的整个攻击性安全知识库。当我询问某个技术时，我得到的是我自己的方法论及我使用的确切命令，而不是来自训练数据的通用摘要，并且它像我一样不断学习新东西。

## **赏金智能**

除了RAG，我还有一个MCP，它跟踪跨多个平台的100多个漏洞赏金计划，并评估跨漏洞类别的投资回报率(ROI)（远程代码执行(RCE)、本地权限提升(LPE)、认证绕过、类型混淆、释放后使用(UAF)、堆溢出）。在为一个目标投入时间之前，它会根据以下几点估算预期支出：

* 目标二进制文件的补丁历史（频繁打补丁 = 被发现的攻击面越多 = 可发现的漏洞越多）
* 漏洞类别和严重性等级
* 计划的支出范围和历史接受率，加上基于特定类型发现结果的"分析人员知识"
* 目标上存在的已知防御机制

这些信息会输入到目标排名中，自主狩猎引擎使用它来决定下一步模糊测试什么。虽然不完美，因为赏金计划的范围和支出会变化，但它可以防止犯下典型的错误，比如为一个最高赏金仅500美元的目标花费一周时间，而旁边可能有一个价值25万美元的超管理器逃逸赏金。

## 劳动成果

现在架构已经分解完毕，你可能想知道，嗯，这很酷，但是值得吗？

### 多个Go标准库CVE

针对Go的`golang.org/x/image`包的模糊测试活动在两周内产生了两个CVE。两者都是OOM漏洞，会导致任何处理不受信任输入的Go进程崩溃。这些漏洞存在于标准库的扩展图像包中，这意味着任何处理用户提供图像或字体的程序（Web服务器、聊天平台、持续集成(CI)流水线）都可能受到影响。

#### CVE-2026-33809 - `x/image/tiff`: 恶意IFD偏移导致的OOM

Go issue #78267

一个特意构造的8字节TIFF文件，其IFD偏移地址设置为`0xFFFFFFFF`，会导致通过`io.Reader`路径（非`ReaderAt`）解码时，`buffer.fill()`分配约4 GB内存，从而导致进程因OOM被杀。

载荷实际上只有8个字节：

```
\x49\x49\x2a\x00\xff\xff\xff\xff
```

这是一个有效的TIFF头（小端序，魔数`0x002A`），后跟一个指向32位地址空间末尾的IFD偏移地址。当`buffer.fill()`尝试读取到该偏移地址时，它会分配一个足以容纳整个范围的缓冲区，对于一个8字节的文件，大约分配了4 GB的零。发生这种分配是因为`safeReadAt`（CVE-2022-41727的修复）没有覆盖`reader.go:477`处的IFD偏移地址读取，这是一个独立的代码路径。

**受影响版本：**`golang.org/x/image`从v0.0.0到v0.37.0的所有版本，即每个曾经发布的版本。Go模块图谱显示有945+个下游包引入了易受攻击的代码。

**修复：** 分块读取数据并分配缓冲区，将增长上限设定为输入的实际大小，而不是信任IFD偏移地址。我提交的修复是golang/image#25，合并为提交`23ae9ed`。

**下游影响：** 已向多个下游消费者报告，因为最终影响的就是它们。并通过供应商的开源漏洞奖励计划提交给了上游。

#### CVE-2026-33812 - `x/image/font/sfnt`: 未检查的GPOS类数量乘积导致的OOM

Go issue #78382

一个特制的字体文件在解析GPOS PairPos表时会触发数十亿字节的分配。在`parsePairPosFormat2`中，`numClass1`和`numClass2`作为`uint16`值直接从字体文件中读取，并且它们的乘积未经检查就传递给`source.view()`。当两个值都为65,535时，乘积乘以2达到约8 GiB，立即导致OOM。只有`io.ReaderAt`路径受到影响（`[]byte`路径受到切片长度的限制）。在调查过程中，我还发现了同一代码中的另外两个问题：

* `makeCachedPairPosGlyph`和`makeCachedPairPosClass`在索引之前，并未验证从字体文件派生的索引是否在已解析的缓冲区内。
* `source.varLenView`在计算总...