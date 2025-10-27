---
title: G.O.S.S.I.P 阅读推荐 2024-09-18 攻击eBPF解释流
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498879&idx=1&sn=fd4393b91c53ed3e86854ace77135246&chksm=c063d2a6f7145bb0608e14b914d1fe99107d26d11c5b10b4729b4aa2b87cb153afcb7e9e6f89&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-19
fetch_date: 2025-10-06T18:26:13.202873
---

# G.O.S.S.I.P 阅读推荐 2024-09-18 攻击eBPF解释流

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcOZgicZYyaGNtcx6sCALHKLGcGM2yr9ULK1pS5HZicKbHInibrjhVmGvvA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-18 攻击eBPF解释流

Qirui@ZJU

安全研究GoSSIP

就在大家沉浸在今年的中秋假期时，ESORICS 2024在布尔达河和维斯瓦河之上的比得哥什拉开了帷幕。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6Kc5Ls9OU94OtJgMoWEr5lFbc8cuhOvLZia8OsZ4QgVe3Q6askmD4DibXvg/640?wx_fmt=jpeg&from=appmsg)

今年的ESORICS一共收到了535篇投稿，最终录用了86篇论文。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcIbxYWBBLHrJAhoZNHia1SJz2JJLtmHnxf1WJWVf62XCCUCqOfwukU0w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6Kcrpz7bUfI9qrpZBTPORQCqA3icT0oAQOrXOu5errUv8CMicolxf3OGIjA/640?wx_fmt=jpeg&from=appmsg)

Josef Pieprzyk教授带来的开场keynote

特别感谢申文博老师为我们从波兰发来的现场照片😆！

---

今天为大家推荐的论文正是获得ESORICS 2024唯一一篇杰出论文奖的工作 **Interp-flow Hijacking: Launching Non-control Data Attack via Hijacking eBPF Interpretation Flow**。该工作提出了eBPF解释流劫持攻击，并提出了低开销的防护方案，推进了eBPF安全的最新研究进展，由浙大网安申文博研究组完成并投稿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KceNCtx8zY54Ru7s9co7AZTbdEpTXIBTdfIlXl3H3V1U28GyL4hOgHCA/640?wx_fmt=png&from=appmsg)

该工作深入研究了 eBPF 字节码的可利用性。如表 1 所示，该工作的研究揭示了一个先前未被发现的安全风险：**eBPF 字节码缺少注入与劫持防护，其解释流可以被劫持以执行任意的字节码，可被利用绕过现有内核代码完整性保护机制，实现内核任意代码注入攻击**。为了理解这一风险，该工作提出了一种新型攻击，称为 eBPF 解释流劫持攻击。在控制流劫持中，攻击者主要通过操纵控制（流）数据以达成其预期的控制流。类似地，eBPF 解释流劫持攻击则以可能影响解释流程的数据为主要目标，该工作称其为解释流数据。该攻击通过操纵解释流数据以劫持 eBPF 字节码的解释流，而非内核代码的控制流，绕过内核代码和控制流完整性保护，实现在内核中进行任意代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcEJ9J3tJy2eqmxCdibIjAWv0V2ib1QwYKdZribDibQgiaChlyytLW33JMYcA/640?wx_fmt=png&from=appmsg)

表1 施加在内核代码与 eBPF 字节码防护的比较

该论文的贡献主要包括：

* 新概念：揭示并定义了一种新型的非控制数据攻击，并将其命名为 eBPF 解释流劫持攻击，它可以使攻击者绕过所有的内核防护，获取在内核空间执行任意代码的能力。
* 新技术：提出了 Tailcall Trampoline，利用 eBPF 的尾调用机制和程序数组类型的 map，可以在不违反控制流完整性的前提下劫持 eBPF 解释器执行注入的恶意字节码。
* 可利用性评估：使用来自不同内核子系统的 16 个 CVE（覆盖常见的漏洞类型），评估了 eBPF 解释流劫持攻击的可利用性，展示了它可以增强所有这些漏洞的攻击能力。
* 防护方案：在 eBPF 解释器中开发了一个字节码检查机制，可以在极小的性能开销下防范 eBPF 解释流劫持攻击，弥补现有内核防护的缺失。

**背景**

eBPF, 全称扩展伯克利数据包过滤器，允许在不对内核进行修改的前提下，动态加载并安全地执行不受信任的用户自定义扩展程序。由于验证器提供的安全性保障，eBPF已成为扩展内核功能的主流手段，并在众多领域被广泛地应用。

作为新兴的内核子系统，eBPF 不应引入新的攻击向量。特别的，它的字节码不应辅助漏洞的利用，以绕过内核的保护机制。然而，现有的 eBPF 安全相关的工作集中于提升其验证器,如 google 发起的buzzer项目，旨在发现并消除eBPF验证器中的错误，而忽视了对eBPF字节码的可利用性的研究。

Di Jin等人提出滥用 eBPF 的字节码以辅助内核控制流劫持攻击，但是他们所提出的攻击劫持内核的控制流，因此会被CFI所阻止，并且只展示了如何利用 classic-BPF（eBPF的子集，只具备有限的功能），而忽视了 eBPF 中添加的扩展特性。因此，eBPF字节码的可利用性仍未被充分探索。

**威胁模型**

攻击者的能力。该工作假设攻击者是一个没有任何特权的普通用户。并且，该攻击者可以访问 eBPF 的非特权功能。这一假设是合理的，如表 2 所示，该工作发现大多数在服务的LTS Linux 版本 (4.19–5.15)默认启用非特权的eBPF及其解释器，并且多个架构（包括ARM和RISC-V）受到影响，该问题已向Linux社区报告并得到Linux开发者的确认。该工作假设 Linux 内核存在常见的漏洞（类似于其他内核漏洞利用的相关工作）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcDibqtaiaL9sn0XjEGW986j02dEZfNLDo6vF8o7DqbFHfRq2ue30g3RvQ/640?wx_fmt=png&from=appmsg)

表2 不安全的内核配置

部署的内核防护。该工作假设 Linux 内核实施了主流的保护措施，包括（1）W⊕X 以防止内核机器代码被篡改和机器代码注入。（2）SMEP以禁止内核跳转执行用户空间代码。（3）CFI以保护返回地址和函数指针。另一方面，本文假设敏感的内核数据对象如进程凭证和页表也被施加保护。SMAP也被启用以阻止内核直接访问用户空间数据。并且假设内核启用了KASLR，使得攻击者难以推断内核空间的内存布局。

**eBPF解释流劫持攻击**

实施 eBPF 解释流劫持攻击，首先需要首先识别出可以被攻击利用的对象（解释流数据）。该工作提出了Interp-PC Tracing，该技术通过追踪 eBPF 解释器程序计数器的数据流识别所有的解释流数据。通过分析识别的结果，发现eBPF尾调用实现中的控制流数据 bpf\_prog \* prog 可以被利用，因此深入分析了 eBPF 的尾调用机制，提出了 Tailcall Trampoline 技术，以在不违反控制流完整性的前提下触发恶意字节码。

如图 1 所示，Tailcall Trampoline 技术的实施分为三个步骤：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcWLuRbzCticDP9Ql1HU1jA3xfE2nEZGiaA9cHCcGITIQzBT8vC0ZVhwaQ/640?wx_fmt=png&from=appmsg)

图1 解释流劫持攻击的步骤

1. 创建prog-array map 。首先，攻击者需要通过调用 sys\_bpf(BPF\_MAP\_CREATE,uattr, size) 来创建一个prog-array map 。uattr->map\_type 被赋值为 BPF\_MAP\_TYPE\_PROG\_ARRAY，以指定所创建的 map 是程序数组类型。该 map 与一个文件结构体关联并可以通过其文件描述符被访问，内核将该文件描述符（mapfd）返回给发出创建请求的用户进程。
2. 加载具有尾调用指令的 eBPF 程序。通过 sys\_bpf(BPF\_PROG\_LOAD, ...)加载一个 eBPF 程序。该 eBPF 程序有一条尾调用指令，攻击者将 mapfd 编码进该指令。该指令从与 mapfd 对应的 map 的数据区加载指向子程序的指针（即 bpf\_prog ptrs[x]）。该步骤中加载的 eBPF 程序是合法的，可以通过验证器的检查。步骤1和2中的操作不需要攻击者具备任何特殊的权限。
3. 利用内核漏洞覆写程序数组类型的 map 中的 eBPF 程序指针。bpf\_prog ptrs[x] 被覆写为一个指向攻击者伪造数据的指针。字节码的解释流被劫持，即尾调用的目标变成了攻击者构造的恶意字节码。bpf\_prog ptrs[x] 是一个数据指针，因此是非控制数据，覆写该指针没有修改内核的控制流。由于内核缺乏对 eBPF 字节码的全面保护，eBPF 的解释器可以执行任意数据，因此最终 eBPF 将会执行攻击者指定的恶意字节码。

通过上述步骤，尾调用劫持技术可以将 eBPF 尾调用的目标成功重定向到任何字节码。此外，尾调用劫持技术没有修改任何会被 eBPF 解释器使用的函数指针或返回地址，因此可以完全绕过控制流完整性保护。

**评估**

为了更清晰地说明实施 eBPF 解释流劫持攻击对 CVE 的能力需求（能够覆写 prog-array map），该工作以 CVE-2018-18445 为例，演示完整的利用过程。如图 2 所示，利用过程包括三个步骤：➀ 内存布局操纵，➁ 覆写 prog-array map 和 ➂ 触发payload。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6Kccic1P1ySiabjXMeOgJTqaUCOZCZcbTZkQ6vfm3tSjHibTbIEXibEasX3Jw/640?wx_fmt=png&from=appmsg)

图 2 利用 CVE-2018-18445 实施 eBPF 解释流劫持攻击的步骤

该工作概述了针对一般 CVE的能力要求,发现广泛存在的 eBPF、DF/OOB/UAF 漏洞都可以被利用。为了展示其通用性,该工作使用 16 个真实 CVE 评估了解释流劫持攻击的可利用性。具体而言,该工作从 eBPF 子系统中选择了 7 个 CVE,从内核的其他子系统中选择了 9 个 CVE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcVrzJq9zuU77PExXeD8ooPz8m3IZDjEAkUJtWXgKBzs1w5d6SWNNv2w/640?wx_fmt=png&from=appmsg)

表 3 可利用性评估

如表 3 所示，解释流劫持攻击可以增强它们绕过内核保护以实现提权的能力。此外,该工作将 解释流劫持攻击与现有的漏洞利用方法进行了比较,分析了它们绕过内核保护的能力,证明了 Tailcall Trampoline 可以赋予这些 CVE 在不破坏关键数据的情况下绕过 CFI 并提权的能力。考虑到 CFI 和数据保护的广泛部署,这些有利的特性使得解释流劫持攻击成为一种更实用、更有效的攻击方式。

**防护**

该工作提出了低开销的防护方案，为解释器添加了一个运行时检查,确保只有经过验证的合法字节码会被执行。其基本思路是解释器在每次解引用 bpf\_prog 指针时,都要通过搜索已验证的字节码集合来检查该指针是否合法。一个关键的挑战是如何识别要解释的数据是否为合法的字节码,因为内核并不区分字节码和普通数据。为了克服这一点,我们提出了基于 idr 匹配的字节码验证方法。具体来说,它使用要解释的字节码的 id 作为键,在已验证的字节码集合中搜索该字节码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GibZ51Crb5ekf16ZkiaibM6KcYR4iaNUCjib5ib8ScqFxJrCMDTgnb0zKSLhmtHPfKoIPKmvXcUeAoRrFA/640?wx_fmt=png&from=appmsg)

图 3 实施防护后的性能开销

该工作在原版/加固内核上评估了来自 Linux 源代码树的 eBPF 示例程序和 BCC 中的 eBPF 用户空间应用程序。结果表明,基于 idr 匹配的字节码验证方法可以以很小的性能开销防御解释流劫持攻击。

论文pdf：https://link.springer.com/chapter/10.1007/978-3-031-70896-1\_10

投稿作者简介：

刘骐瑞，2021 级浙江大学硕士研究生，导师为申文博老师。研究方向为操作系统安全，eBPF和虚拟化技术，在 ESORICS，TDSC 上发表过相关研究成果。

申文博，浙江大学百人计划研究员，博士生导师，研究方向为操作系统安全，芯片安全机制，云原生系统安全，软件供应链安全，个人主页：https://wenboshen.org/

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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