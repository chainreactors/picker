---
title: Mozilla如何用Claude Mythos修复Firefox 中271个潜伏漏洞
url: https://mp.weixin.qq.com/s/35JeIrZM3E4BR_rLbO5hvA
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:03:31.189231
---

# Mozilla如何用Claude Mythos修复Firefox 中271个潜伏漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrwaeiaTRf1ibbVgKFwuxWlm0iarlb2rqBKfH9BCRk774hRCAFTujAVuI689Rwmic798uVlJyceDz6MLsoPN8Vg9UubXTictKXvQWpk/0?wx_fmt=jpeg)

# Mozilla如何用Claude Mythos修复Firefox 中271个潜伏漏洞

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

两周前，Mozilla 宣布借助 Claude Mythos Preview 和其他 AI 模型，在 Firefox 浏览器中识别并修复了数量空前的潜伏安全漏洞。今天，我们深入幕后，看看这一突破性工作是如何完成的，AI 究竟发现了哪些隐藏多年的漏洞，以及这对整个软件行业意味着什么。

就在几个月前，开源项目收到的 AI 生成安全漏洞报告还大多被视为无用的垃圾信息。这些报告看似合理实则错误，给项目维护者带来了不对称的成本负担。用 AI 生成一个 "问题" 既便宜又容易，但验证和响应却耗时又昂贵。

然而，短短几个月内，这种局面发生了翻天覆地的变化。这主要归功于两个因素：

* 模型能力的大幅提升
* Mozilla 团队大幅改进了驾驭这些模型的技术，包括引导、扩展和堆叠模型，以生成大量有效信号并过滤噪音

为了让大家直观了解 AI 的能力，Mozilla 破例公开了部分已修复漏洞的报告样本。这些漏洞涵盖了浏览器的多个子系统，其中许多是传统方法难以发现的。

## AI 发现的 12 个典型高危漏洞

## (https://bugzilla.mozilla.org/show\_bug.cgi?id=(?))

| Bug ID | 漏洞描述 |
| --- | --- |
| 2024918 | 一个不正确的相等性检查会导致 JIT (即时编译器) 优化掉正在使用的 WebAssembly GC (垃圾回收) 结构体的初始化，创建一个假对象原语，可能在经过内部和外部研究人员大量模糊测试的代码中实现任意读写 |
| 2024437 | `<legend>` 元素中存在 15 年历史的漏洞，需要精确编排浏览器多个远程部分的边缘情况才能触发，包括递归栈深度限制、expando 属性和循环回收 |
| 2021894 | 可靠利用 IPC (进程间通信) 上的竞态条件，允许被攻陷的内容进程操纵父进程中的 IndexedDB 引用计数，触发 UAF (释放后使用) 并可能实现沙箱逃逸 |
| 2022034 | 原始 NaN 值跨越 IPC 边界时可以伪装成带标签的 JS 对象指针，将双重反序列化转化为父进程假对象原语，实现沙箱逃逸 |
| 2024653 | 一个复杂的测试用例，通过嵌套事件循环、pagehide 监听器和垃圾回收，触发`<object>`元素属性设置器中的 UAF |
| 2022733 | 通过向 WebTransport 发送数千个证书哈希来延长引用计数密集型复制循环中的竞态条件，然后从被攻陷的内容进程通过 IPC 利用该竞态条件触发父进程 UAF |
| 2023958 | 通过拦截 glibc DNS 函数调用模拟恶意 DNS 服务器，重现 UDP 到 TCP 的回退边缘情况，在 HTTPS RR 和 ECH 解析期间触发缓冲区过度读取和父进程栈内存泄漏 |
| 2025977 | XSLT 中存在 20 年历史的漏洞，可重入的 key () 调用会导致哈希表重新哈希，在原始条目指针仍在使用时释放其后备存储。这是我们修复的多个涉及 XSLT 的高安全级别问题之一 |
| 2027298 | 修补颜色选择器以模拟原本无法自动化的用户选择，然后使用同步输入事件旋转嵌套事件循环，重新进入 actor 销毁过程并在回调仍在展开时释放它，触发内容进程 UAF |
| 2023817 | 被攻陷的内容进程可以发送任意壁纸图像到父进程进行解码，这可能与图像解码器中的假设漏洞结合使用以逃逸沙箱。这需要对父进程中输入的信任级别进行难以自动化的推理 |
| 2029813 | 利用用于将值从沙箱边界的不受信任端复制到受信任端的验证逻辑中的漏洞，逃逸我们用于第三方库的进程内沙箱技术 RLBox |
| 2026305 | 极小的测试用例，通过追加超过 65535 行来绕过限制并溢出 16 位布局位域，利用 HTML 表格中特殊的 rowspan=0 语义。这个漏洞多年来一直未被模糊测试工具发现 |

值得注意的是，这些漏洞中有多个是沙箱逃逸漏洞。这类漏洞需要与其他漏洞结合才能实现完整的 Firefox 攻击链。这些报告假设渲染网站内容的沙箱进程已经被某个单独的漏洞攻陷，并且正在运行攻击者控制的机器代码，试图将控制权提升到特权父进程。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDodH432wkFfjKiaYILq3D8fqF4Om23yOSHKDxcU9Qo5eG8dvOG1VVhMRBuUyke4Zk78TnTFUzIicPzgIRs6I0CibAoyvFYa508oJM/640?wx_fmt=png&from=appmsg)

沙箱逃逸漏洞以传统模糊测试方法极难发现而闻名。虽然 Mozilla 在开发新技术缩小这一差距方面取得了一些成功，但 AI 分析为这一关键攻击面提供了更全面的覆盖。

同样有趣的是 AI 没有发现的东西。这不是因为它们没有尝试，而是因为它们无法绕过 Firefox 的分层防御。例如，近年来 Mozilla 收到了一些安全研究人员的巧妙报告，他们通过在特权父进程中触发原型污染来逃逸进程沙箱。Mozilla 没有逐个修复这些问题，而是进行了架构更改，默认冻结这些原型。在审计工具日志时，我们看到许多尝试沿着这条逃逸路线的攻击都被这一设计挫败了。

Mozilla 在过去几年中一直在内部试验 LLM 代码审计。早期尝试使用 GPT 4 或 Sonnet 3.5 等模型对高风险代码进行静态分析以查找漏洞。这些实验显示出一些希望，但高误报率使其无法大规模应用。

能够可靠检测安全问题的智能代理工具的出现彻底改变了这一局面。这些工具可以发现真正的漏洞并排除不可重现的推测。这种工具的关键特性是，在获得正确的接口和指令后，它可以创建并运行可重现的测试用例，以动态测试关于代码中漏洞的假设。

在修复了 Anthropic 在 2 月份发送给 Mozilla 的初始问题集之后，Mozilla 在现有模糊测试基础设施之上构建了自己的工具。团队从使用 Claude Opus 4.6 寻找沙箱逃逸的小规模实验开始。即使使用这个模型，他们也发现了大量以前未知的漏洞，这些漏洞需要对多进程浏览器引擎代码进行复杂推理。

起初，团队在终端中监督整个过程，实时观察并调整提示和逻辑。一旦运行良好，他们就将作业并行化到多个临时虚拟机上，每个虚拟机负责在特定目标文件中寻找漏洞并将结果写回存储桶。

发现子系统是必要的，但还不够。为了扩展这项工作，Mozilla 需要将其与完整的安全漏洞生命周期集成。这包括确定要查找什么、在哪里查找以及如何处理发现的内容。最后一部分包括与已知问题去重、跟踪漏洞、分类和发布修复程序。虽然模型是驱动工具的核心原语，但完整的管道对于使其在规模上有用是必要的。

虽然工具可能在不同项目之间可重用，但这个管道本质上是项目特定的，反映了每个代码库的语义、工具和流程。建立这个管道需要大量的迭代，以及与处理传入漏洞的 Firefox 工程师的紧密反馈循环。

一旦端到端管道就位，当新模型可用时，替换它们变得非常简单。早期构建这个管道帮助 Mozilla 使用公开可用的模型发现了许多严重漏洞，也让他们在有机会评估 Claude Mythos Preview 时能够迅速上手。

根据 Mozilla 的经验，模型升级提高了整个管道的有效性。系统在发现潜在漏洞、创建概念验证测试用例以演示漏洞以及阐明其病理和影响方面同时变得更好。

除了在 150 版本中修复 Claude Mythos Preview 识别的 271 个漏洞外，Mozilla 还在 149.0.2、150.0.1 和 150.0.2 版本中发布了更多这些修复程序。他们还继续通过其他内部手段发现漏洞，并且与其他项目类似，在过去几个月中看到外部报告显著增加。

最终，每个漏洞都需要仔细关注才能正确修复。应对这一前所未有的漏洞数量在过去几个月中带来了大量工作和漫长的工作日。超过 100 人参与了这项工作，以发布有史以来最安全的 Firefox。除了编写和审查补丁外，其他人还在构建和扩展这个管道、分类、测试修复程序以及管理每个漏洞的发布过程。

任何构建软件的人今天都可以开始使用带有现代模型的工具来查找漏洞并加固他们的代码。Mozilla 建议现在就开始。你会发现漏洞，并且你将为新模型一出现就利用它们做好准备。

你可以从非常简单的提示开始，然后观察和迭代。Mozilla 的初始提示与这里描述的没有太大不同。通过迭代，他们构建了大量编排和工具来优化和扩展管道，但内部循环的本质保持不变：这部分代码中有一个漏洞，请找到它并构建一个测试用例。

Mozilla 还没有找到 Firefox 中所有的潜伏漏洞，但对目前的进展非常满意。今天，他们的扫描主要集中在代码的特定区域，包括文件和函数，基于人类判断和自动化信号的混合。在不久的将来，他们打算将这种分析集成到持续集成系统中，在补丁提交到代码库时进行扫描。模型对提供的上下文形式非常灵活，Mozilla 预计基于补丁的扫描效果将与基于文件的扫描相当甚至更好。

当前时刻既危险又充满机遇。让我们共同努力保护互联网。

----

老老实实弄东西这么久，可算又被人抓到个莫名其妙的点，然后触发关键词，投诉成功，下架文章，申诉都申诉不了，下次别被我的探针和蜜罐捕获到你。

再举报直接丢你去月球见UFO

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq3nRVrJn5cuSGRqKrx0ic8xkA4LXTbicsHWbdc1baTyhrHG7vE42pcx0Q6OCR2SG6Nib5vHyAsmx6ic2RR0dPW7ggKKibMrhibO0N0U/640?wx_fmt=png&from=appmsg)

https://www.war.gov/UFO/

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoibImln0iaicUkgiaBTNJdiaqjzmOmCWX5ibmOwX9eQP8iaDcjdbhvLe6gibdQBdLKzJWaVj8YgicQZ7sRQePuItxMMeFGiaKOfZvACOiceU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqGbnTyylceicUPEmspda4XfvCHC4KKHJA1yLKclVgnY1iaNwRticoOSXJrvABQ3MFUmMplNFcGpt7dGmfMRh3MnVLlzgmVzTekFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDobLde8BSBEgniaBs9ib2Vpb8OSPaX2NjJrsib6NxHDXYCudSPktiaexiaOfDhe1LJDzF9WXGZeNFtBFtxKHTTbIGXhwGuTlLOopseo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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