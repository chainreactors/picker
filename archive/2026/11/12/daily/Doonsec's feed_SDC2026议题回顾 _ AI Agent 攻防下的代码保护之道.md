---
title: SDC2026议题回顾 | AI Agent 攻防下的代码保护之道
url: https://mp.weixin.qq.com/s/415DzW_4fy1jAWUe2zqafw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:32.516428
---

# SDC2026议题回顾 | AI Agent 攻防下的代码保护之道

# SDC2026议题回顾 | AI Agent 攻防下的代码保护之道

SDC2026
SDC2026

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**SDC2026**

议题回顾

随着 AI Agent 能力不断提升，软件逆向分析正从依赖人工经验的逐步探索，向自动化、智能化的分析模式演进。当 AI 能够自主完成代码定位、逻辑还原、动态调试等工作，传统软件保护所面临的攻防平衡也随之发生变化。面对 AI 带来的新挑战，代码保护又该如何应对？

在第十届安全开发者峰会现场，**网易易盾加固技术负责人——赵贝贝**以实际游戏分析案例为切入点，对比人工分析与 AI 分析的差异，深入拆解 AI 的逆向分析思路，并结合技术实践，分享围绕隐藏、复杂化、诱捕、误导及行为识别展开的 AI 行为防御探索，探讨 AI Agent 时代软件代码保护的新思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K30Tib5NBvC7LMiaV1qhXDsacLia0WCYqRv975ic1BGN7TbGa0tA4icDslicTgib0PyibK5FXib3zYOxg90ScdsKdyhibUcdbnGaQuTWETvU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3whMf9Fk35eS6GU1l3IAebXyetqNWQufvUkek2RibHMdGo3XPibzgOxBrTBUqNuacf8nH4S7OxzEDDaKXXRuINcRWOaGACLia1pc/640?wx_fmt=jpeg&from=appmsg)

*赵贝贝*

*网易易盾加固技术负责人*

*\*以下为整理后的速记*

大家下午好，我是来自网易易盾的赵贝贝。今天分享的主题是《AI Agent 攻防下的代码保护之道》。

首先介绍一下团队和个人情况。网易易盾客户端安全团队拥有十余年的安全对抗经验，建立了覆盖游戏全场景、全周期、全链路的应用安全产品体系，在游戏安全、应用加固、账号安全、黑灰产管控等领域形成了专业的技术运营体系，为各类应用提供安全保障。

我于2018年7月加入网易，目前负责加固技术相关工作，长期专注于移动应用和游戏的安全加固与反外挂研究及落地，工作范围包括安卓、鸿蒙及各类前沿系统应用的安全加固，并主导落地了多项客户端安全核心对抗方案。

本次分享主要分为四个部分：首先通过一个游戏分析案例，对比人工分析与 AI 分析的差异；其次介绍 AI 分析背后的思考过程；然后结合这些分析过程，分享我们在 AI 行为防御方面的探索；最后进行总结与展望。

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K0T1iaKqpT62icNXrYPYU8icwqJ0MwFrsNwedmSPSp7LMwT6jkEFkX7s8c1CQib1s8FAwCLrDqLU9ZyybtqsT6iclekibHCoHUme5l4E/640?wx_fmt=gif&from=appmsg)

**一、从分析一个游戏谈起：人工分析与 AI 分析**

先从一个常见的 Cocos 类游戏案例讲起。假设游戏对核心 JS 文件进行了加密保护，同时使用了第三方加固壳。现在需要解决的问题是：运行时，游戏中的 JS 文件究竟通过什么方式解密，并最终还原为可用的 JS 文件？

如果由人工进行逆向分析，首先需要定位关键文件，判断解密逻辑可能位于哪里。它可能由游戏引擎、JS 层、Dex 层或第三方加固壳中的某个模块完成，需要逐一排查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0DmnrTLlM2iamFwFnfSAyicxgJyfFDFrUVbvj09wlCLFbCwMk7lm12pQCGgXpG4Mk6eiaTypCfL29JArWGr9ibeXlWSNibcFrWqscQ/640?wx_fmt=png&from=appmsg)

图1｜人工分析游戏时涉及的关键步骤

在定位过程中，需要依次判断关键文件是否加壳、是否混淆、是否进行了虚拟化处理。如果存在加壳，就要开展脱壳；如果存在混淆，就需要反混淆；如果关键指令或方法经过虚拟化，还需要进行 VMP 还原。完成这些工作后，才能进一步定位具体的解密算法，并通过 Frida 等工具进行动态分析。

但在动态分析过程中，还可能遇到第三方加固壳的检测，需要继续处理检测与绕过问题。因此，整个过程中的每一个环节都依赖经验：脱壳、反混淆和虚拟化还原需要专业知识，绕过检测需要实践经验，修改方法也需要游戏逆向经验。

随后，我们尝试将同样的任务交给 AI Agent。只需要用一句话描述目标，AI 就能够自行开展分析。实际案例中，AI 大约用三四十分钟完成了任务，并给出了静态解密脚本。

我们进一步观察 AI 背后的思考过程：拿到 APK 后，第一步是观察和收集信息，包括 APK 的结构、使用的引擎及其版本，以及是否使用了第三方加固壳。

第二步是提出假设。对于需要解密的 JS 文件，AI 会推测究竟由哪个模块负责解密，可能是游戏引擎，也可能是其他 SO、Dex 或 JS 层代码。随后，它会根据假设逐项开展验证。

第三步是定位锚点。分析过程中，AI 会寻找关键的语义锚点，例如引擎 SO 文件中的关键字符串或函数节点，并以此展开路径探索。找到解密算法后，还会继续追踪控制流，回溯密钥的来源。

第四步是行为决策与结果验证。AI 会选择相应策略执行验证，必要时调用 Frida 等工具；如果遇到第三方加固壳的检测，也会尝试处理。最后，对解密结果进行验证，完成整个分析闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0KPFou0Iu0rXPhzyCeSP3cTRyibX86GsWt35vKQBgZG5lbm8OA1ZuvcZhKZkib0k455B2l7ovFpNFQyOoI8DxBSiaYfLmCKJBSUQ/640?wx_fmt=png&from=appmsg)

图2｜AI 分析过程

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1jDIgeqriaJMqfBtNxNLhXJrWsEv7Tsbiczvte8n3zPvGYxdcfmqORicw4050def8d8TzGSlm1JMolOSYicGWsEWHBl0ccUAhjfh4/640?wx_fmt=gif&from=appmsg)

**二、AI 分析带来的攻防变化**

传统软件保护中，通常默认防守方与攻击方处于相近的能力维度。防守方通过加壳、混淆、虚拟化，以及调试检测、环境检测等方式，对抗攻击方的知识面、经验、记忆力和耐心。双方在这些因素上形成一定的动态平衡。

AI 出现后，这种平衡发生了变化。AI 可以长时间持续工作，拥有较强的记忆能力、耐心和广泛的知识覆盖。原本依赖人工经验和时间成本形成的保护门槛，可能因此被显著削弱，软件保护面临新的动态不平衡。

从前面的案例可以看到，AI 的分析已经呈现出相对清晰的流水线：观察感知、假设推理、定位锚点、行为决策和结果闭环。对应到防御侧，我们认为不能再依赖单一手段，而需要组合使用多种方式，增加 AI 分析路径的数量和验证成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2UORKplnT9Dwvic5smUOkLEbZapZUGy6NKtZTnAWJpIDSvndicyGw12OyeuryVQEsqOjw2iaibAdzHM816gpeHOYtMPucBibLF6ibDo/640?wx_fmt=png&from=appmsg)

图3｜AI 行为防御探索

具体来说，观察感知阶段可以通过隐藏，让真实信息难以被直接看到；假设推理阶段可以通过复杂化，让代码结构和语义难以被准确还原；定位锚点阶段可以通过诱捕，利用蜜罐等方式捕获 AI 行为；行为决策阶段则可以通过误导，让分析沿着错误路径持续消耗。

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1nyjXWPDIf3MoBySIWfjhKQesub7EtbPHT03qAtKxDh5B97D5tLRevIfIicuicYrn15ybsAzvDc1Aanw0ticiaXxJqmQ30uCs1gZY/640?wx_fmt=gif&from=appmsg)

**三、AI 行为防御探索**

**1. 隐藏：降低真实逻辑的可见性**

传统软件保护中的隐藏通常会想到加壳。但在 AI 时代，仅依赖传统加壳可能不够。程序最终运行时，相关代码仍然会在内存中还原；AI 可以结合语义锚点，直接从内存中定位并提取相关内容。对 AI 来说，它未必需要按照传统人工逆向的方式完成“脱壳”，而可能只是为了达成目标，对内存内容进行定位和提取。

因此，在隐藏方面，我们尝试结合具体业务场景，对关键代码采用“运行下发”的方式：运行时通过加密通道按需拉取并校验，代码在内存中执行，执行完成后再从内存中销毁。运行下发所使用的解释器和字节码，也需要进行定制，避免直接采用市面上已有的通用形式。

此外，还可以在真实逻辑之外植入控制流等价、语义等价的诱饵实现，通过不透明谓词和路径切换，使真实分支与隐藏分支难以区分。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K35QynnIib7ahWu6ic1AiazVLg3Nia515xpP7qJSMBgko70zzVibde4rViaXAmmKbF3JxGsHQRicK7Fr7XpibU6dIpWqzKCdRIV73gjFHc/640?wx_fmt=png&from=appmsg)

图4｜隐藏策略

**2. 复杂化：提高代码还原成本**

传统软件保护中的复杂化，主要对应代码混淆，例如控制流平坦化、间接跳转和虚假控制流等。我们尝试基于中间表示（IR）指令进行处理，以适应不同业务场景，而不是针对不同二进制逐一适配。

在具体实现上，主要探索了自定义栈虚拟机和自定义寄存器虚拟机两种方式。栈虚拟机将 LLVM SSA 值映射为栈虚拟机的局部变量，再通过解析 IR 获取操作数并生成栈指令，加入干扰信息，对操作码进行随机置换和序列化，最后生成对应解释器。

不过，栈虚拟机的执行方式具有一定规律性，AI 比较容易识别解释器中的模式，分析成本相对有限。因此，我们进一步尝试基于寄存器的虚拟机：为每个 SSA 值分配虚拟寄存器，将原始指令翻译为微指令，并在指令结构中加入操作码、干扰位、结果槽位、操作数列表和数据类型等字段。

在生成自定义字节码时，可以加入诱导字段，并对操作码进行随机置换、加密映射和序列化。例如，原始加法指令在翻译过程中可以被转换为其他形式，再通过解释器中的映射和跳转逻辑完成实际运算。最终生成的字节码中包含多种干扰信息，使 AI 不容易快速识别其规律。对于每个函数，虚拟化处理后的结果也具有随机性。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1kXLtCLzj2nwkkOj0GmeosoMBtPamKPgYxzwP0zrD0ShXuqIfrTBuVtncCPc6204dudzxC17BKVP3CpficHEDHlvDK90sNzicv4/640?wx_fmt=png&from=appmsg)

图5｜基于 IR 的自定义栈虚拟机与寄存器虚拟机处理流程

我们对这一方案进行了测试。测试集包括20个第三方算法和10个自定义算法，涉及148个方法。由于 AI 分析存在不稳定性，以下数据仅供参考。

在未混淆情况下，算法覆盖率为93.3%，方法覆盖率为85.3%，还原准确率为87.3%；采用传统混淆后，三项数据分别为73.3%、75.3%和71.3%；采用新型混淆（VMP）后，分别下降至30.3%、28.3%和16.2%。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3sNbaLbQUS448wTAZ2Yjd7NLVTXmcr5icCo2jd73vlVCEVBGNo1qqib1cnnwxQSUSMKIVNoMKUbwNfvSzpccfX5ia0sfnaU7WTII/640?wx_fmt=png&from=appmsg)

图6｜不同保护方式下的算法覆盖率、方法覆盖率与还原准确率对比

从测试结果看，第三方算法的还原正确率高于自定义算法；经过自定义 VMP 处理后，还原准确率明显下降。因此，对于业务中使用的算法，可以考虑进行自定义处理，而不是直接使用第三方算法实现。

**3. 诱捕：让 AI 进入错误分析路径**

诱捕的思路，是构建一个面向 AI 分析行为的“蜜网”。首先让 AI 进入预设的错误逻辑；其次增加它在错误路径中的分析成本，使其持续探索而不容易得到正确结果；同时记录 AI 的行为指纹，再结合风控和具体业务数据进行识别与后续处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K18VicMj9ZfEM8DSC5O45T5KnNoW4PzTmiaun2cshibCHlALDoC9HcDBQsOs59yvXn5r5ibPaXxLqufXm8IPFWtBVWibXlNmGvsxheQ/640?wx_fmt=png&from=appmsg)

图7｜蜜网的基本流程

一种方式是伪造诱捕 API。以两个 SO 模块之间的调用关系为例，业务模块会调用另一个常见算法库中的导出函数。由于 AI 可能基于已有知识和经验识别常见库及其导出函数，我们可以对相关实现进行混淆，同时伪造看起来真实的导出函数名，再修复模块之间的调用关系。这样，AI 可能会依据熟悉的函数名和调用关系作出错误判断，拿到看似真实、实际却是伪造的内存数据，进而沿着错误逻辑继续分析。

另一种方式是通过欺骗常见算法的识别经验进行诱捕。我们选取 MD5、SHA-1、SHA-256、AES、XXTEA、CRC32、LZMA 解压和 protobuf 等常见算法，对第三方算法进行细微修改，例如调整位序、字节序、常量表，或保留结构但改变其实际语义。外部仍保留常用语义名称，中间实现经过小幅修改，内部再叠加自定义虚拟化保护。

在一组实验中，20个第三方算法经过自定义魔改和虚拟化处理后，交由 DeepSeek 分析约三个小时。最终有19个算法被分析出来，其中17个被判断为标准算法，欺骗混淆成功率达到85%。这一结果说明，AI 可能会依据已有经验将经过修改的算法识别为标准算法。对于开发中使用的算法，可以在适当情况下进行微小的自定义改动，再结合虚拟化保护，以迷惑 AI 并保护私有算法。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0Au0OVGUZM8liajkyQh4x9wbFQQrcBDiaiauvKQUQ80s0JW5hkc1jm2mLSUTZaEibVibG2JcHs8JLleUn2XHibtlwsdA16Viaae3iazHg/640?wx_fmt=png&from=appmsg)

图8｜第三方算法经自定义处理和虚拟化后，AI 分析结果及欺骗混淆效果

**4. 误导：让 AI 对功能作出错误判断**

误导主要是通过语义干扰，让 AI 沿着错误方向理解代码。我们尝试让 AI 自定义一个解释器，用于执行自定义 bytecode。这里的解释器与前面介绍的 VMP 并不是同一个概念，可以理解为类似 JVM 或 WebAssembly 的执行形式。通过动态执行变换，使 AI 每次面对的执行过程有所不同；同时，在真实方法附近加入语义相近的干扰功能。

当 AI 分析这类代码时，可能会避重就轻，将语义聚合的干扰功能当作模块的真实功能，并据此给出结论。为实现这一点，需要将检测逻辑从 native 代码迁移到自研字节码虚拟机中，并对魔数、版本、段 ID、操作码等格式进行置换；同时消除符号、日志、敏感字符串和敏感导入等语义锚点。此前的实验中，如果仍然暴露少量语义锚点，AI 可能在几分钟内就完成分析。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1gP8iauNaTfhEQoz8299wAFL8kHYZTFSkwDgH0hbuaKT5fwoB7gahxEQP6oGqEOAia8NhDEO9KDMuMDMXf7YK4As29PhDmbgkkQ/640?wx_fmt=png&from=appmsg)

图9｜语义误导

我们还做过一个反调试相关实验：编写一个反调试功能，并使用自定义解释器执行；在外围增加 Frida Hook 检测相关功能，但不对该 Frida 检测功能本身进行保护。随后使用此前开发的虚拟化保护处理，再交给 AI 分析。AI 最终将其判断为 Frida 检测功能，却没有分析出其中的反调试逻辑。这个实验主要是想说明，语义误导可以作为一种思路，尝试应用到具体业务场景中。

此外，我们还尝试通过内存切割来误导分析。首先解析 /proc/self/maps，定位目标内存区间并获取起始地址和权限；随后备份内存内容，通过 MAP\_FIXED 匿名映射进行原地覆盖，再将备份内容写回。对于原本可读写的内存，可以将其权限伪装为仅写，以隐藏真实的可读属性。

之后，按页对齐将整段内存切割为多个小段，并通过 prctl(PR\_SET\_VMA\_ANON\_NAME) 为不同内存段设置伪造名称。处理完成后，原本连续的一段内存会呈现为多个分散的小段，名称也被打散，从而增加 AI 识别真实内存布局的难度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3NIkX6sFLzXMYuAKHKLzUnRMftQRdKrIpVxqKUaCjnQ2lVvOBm7v9iaX10j7CJJsDZ7VRRNDWQ5vGCJYKpNX4hpjqGJMBrznHs/640?wx_fmt=png&from=appmsg)

图10｜内存切割误导

**5. 行为识别：捕捉 AI 的行为指纹**

在 AI 分析 APK，尤其是连接手机设备开展动态分析时，AI Agent 会表现出一定的行为特征。例如，模拟点击时可能倾向于点击控件中心，出现零时间戳间隔、整数坐标或同一像素重复点击等情况。这些操作与真实用户的触控行为存在差异。

在工具调用方面，AI 可能通过 adb、monkey 或 instrumentation 等方式启动和控制应用，并呈现频繁重启、调用规律明显等特征。这些工具的生命周期和调用行为，也可以作为识别线索。

此外，还可以关注内存检测行为。例如，在设置陷阱页后，结合 MADV\_DONTNEED 和 mincore 等机制，观察相关内存页面是否被读取。...