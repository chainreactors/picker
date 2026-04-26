---
title: 看懂银狐源码需要安全工程方面哪些知识？如何学习？
url: https://mp.weixin.qq.com/s/bisf7j87tV8lbNvdK8BuxA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:29.103022
---

# 看懂银狐源码需要安全工程方面哪些知识？如何学习？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxS4k4HDMlQf3Uicxg7j3RQEry2gKF45sWcPKqfcSID74tLEB2l2icxYOW6vh0IfjeBRyOkiaBx5Xwib4WSjNAjXPJKBMAibrFqChfe0/0?wx_fmt=jpeg)

# 看懂银狐源码需要安全工程方面哪些知识？如何学习？

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一些做安全工程方面的同学，在学习银狐源码时，一些关键逻辑看不懂，交谈中发现缺少一些安全工程方面的知识。

特别申明：

**本文内容仅限于用作技术交流，请勿使用本文介绍的技术做任何其他用途，否则后果自负，与本号无关。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GSweNIrkicYuO7qxZCEZEPIa3STMW4wa20ylAJb7YVeqK8MAV71BZaDEV1eIvcZ4r2N5mr9pMJwnuiav2c0dTTEg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

这里花了几周时间精心给大家整理一份学习书单，希望能帮助有需要的小伙伴。

本文整理了一份涵盖 Shellcode 开发、逆向工程、Rootkit 技术、漏洞利用与防御规避等领域的 PDF 学习资料清单。这些资料从入门到进阶层次分明，适合希望系统性构建安全工程知识体系的读者。

---

## 一、汇编语言基础

打牢汇编基础是理解 Shellcode、逆向工程乃至整个底层安全领域的前提。

### 1. The Art of 64-Bit Assembly, Volume 1

* **作者**：Randall Hyde
* **定位**：x86-64 汇编入门经典
* **内容概要**：从机器组织架构讲起，系统介绍 x86-64 指令集、寄存器模型、内存布局、过程调用约定等核心概念。Randall Hyde 是汇编语言教学领域的标杆人物，其写作风格清晰严谨，非常适合作为第一本汇编读物。
* **推荐理由**：如果你之前从未接触过汇编，从这本书开始是最稳妥的路线。书中大量示例和练习帮助你真正理解 CPU 如何执行指令。

### 2. x64 Assembly Language Step-by-Step: Programming with Linux (4th Edition)

* **作者**：Jeff Duntemann
* **定位**：x64 汇编实战教程
* **内容概要**：以 Linux 为平台，手把手带你编写 x64 汇编程序。从最简单的 Hello World 到系统调用、内存管理，循序渐进。
* **推荐理由**：与上一本互补。如果你日常工作环境是 Linux，这本书能让你直接在真实系统上练习，理解汇编与操作系统的交互方式。

---

## 二、Shellcode 开发

Shellcode 是渗透测试和漏洞利用的核心载荷。这一部分的资料从原理到实战，覆盖完整。

### 3. The Shellcoder's Handbook (2nd Edition)

* **出版社**：Wiley, 2007
* **定位**：Shellcode 领域的"圣经"
* **内容概要**：全面覆盖 Shellcode 编写、缓冲区溢出利用、堆溢出、格式化字符串漏洞等经典攻击技术。虽然出版年份较早，但其中讲解的底层原理至今仍然是理解现代攻防的基石。
* **推荐理由**：这是安全研究人员书架上的必备之作。即使现代系统引入了 DEP、ASLR 等缓解措施，理解经典攻击手法仍然是绕过新防护的思维起点。

### 4. Offensive Shellcode From Scratch

* **作者**：Rishalin Pillay
* **出版社**：Packt, 2022
* **定位**：现代 Shellcode 开发实战
* **内容概要**：从零开始教你编写攻击性 Shellcode，包括 Windows 和 Linux 平台的 Shellcode 构造、编码与测试。内容紧跟现代操作系统环境。
* **推荐理由**：如果说 *The Shellcoder's Handbook* 是经典理论，这本就是现代实践。2022 年出版意味着它考虑了当前的安全机制和编译器行为，实操性极强。

### 5. Penetration Testing with Shellcode

* **作者**：Hamza Megahed
* **定位**：渗透测试视角下的 Shellcode 应用
* **内容概要**：将 Shellcode 技术融入完整的渗透测试流程，涵盖网络层和操作系统层的漏洞检测、利用与防御。
* **推荐理由**：这本书的特色在于它不是孤立地讲 Shellcode，而是放在渗透测试的完整上下文中。适合想要将 Shellcode 技能应用到实际红队工作中的读者。

### 6. WiShMaster — Windows Shellcode Mastery (BlackHat Europe 2009)

* **作者**：Benjamin Caillat (ESIEA - SI&S lab)
* **内容概要**：提出了 WiShMaster 框架，用于自动化 Windows Shellcode 的生成流程。白皮书详细讨论了 Shellcode 在病毒学中的应用、编写方法（栈方式、全局数据方式、汇编修补方式）、Shellcode 加密（XOR、AES-CBC）以及反向 Shell 的开发。
* **推荐理由**：虽然是 2009 年的 BlackHat 研究，但其中关于 Shellcode 自动化生成和加密技术的思路至今仍有借鉴价值。学术风格的论文写作也便于理解底层设计思想。

---

## 三、逆向工程

理解二进制、拆解程序逻辑是安全分析和漏洞挖掘的基本功。

### 7. Reverse Engineering for Beginners

* **定位**：逆向工程入门百科
* **内容概要**：这是一本广受好评的免费/开源逆向工程教材，覆盖 x86/x64/ARM 架构的反汇编分析，从简单的 C 代码编译产物讲起，逐步深入到复杂数据结构和控制流的逆向。
* **推荐理由**：篇幅虽大但结构清晰，覆盖面极广，常被称为逆向工程领域的"百科全书"。无论你是学生还是从业者，都值得反复翻阅。

### 8. Mastering Reverse Engineering

* **作者**：Reginald Wong
* **定位**：逆向工程进阶
* **内容概要**：在入门基础之上，深入讲解实际恶意软件样本的分析方法、反调试对抗、加壳脱壳等高级主题，帮助读者建立完整的逆向分析工作流。
* **推荐理由**：适合已有一定基础、希望在恶意软件分析方向深耕的读者。实战案例丰富，能帮助你将理论知识转化为分析能力。

### 9. C++ Reverse Engineering

* **定位**：C++ 程序逆向专题
* **内容概要**：专门针对 C++ 编译产物的逆向分析，包括虚函数表、对象内存布局、模板实例化、异常处理机制等 C++ 特有结构在二进制层面的表现。
* **推荐理由**：现实世界中大量关键软件（浏览器、游戏引擎、安全产品）使用 C++ 编写。C++ 的逆向比 C 复杂得多，这本专题书填补了一个重要的知识空白。

---

## 四、Windows 内核与 Rootkit 技术

内核安全是攻防对抗的制高点。这几本书从不同角度剖析了 Windows 内核的攻击面。

### 10. Rootkits: Subverting the Windows Kernel

* **作者**：Greg Hoglund, James Butler
* **定位**：Windows Rootkit 经典
* **内容概要**：系统讲解 Windows 内核 Rootkit 的设计与实现，包括 DKOM（直接内核对象操控）、SSDT Hook、IRP Hook、驱动程序隐藏等技术。
* **推荐理由**：Rootkit 技术的开山之作，虽然部分技术在新版 Windows 上已被 PatchGuard 等机制限制，但其中的内核编程思维和攻防博弈思路永不过时。

### 11. Professional Rootkits（中文版 + 英文版）

* **定位**：Rootkit 技术实战手册
* **内容概要**：本书目录中同时提供了中文版和英文原版。内容涵盖 Rootkit 的各种实现方式，从用户态到内核态，从文件隐藏到网络通信隐匿。
* **推荐理由**：中文版降低了阅读门槛，英文原版可用于对照理解专业术语。两个版本搭配阅读效果最佳。

---

## 五、Windows 安全与漏洞利用

### 12. Windows APT Warfare: Identify and Prevent Windows APT

* **作者**：Sheng-Hao Ma, Ziv Chang, Federico Maggi (2023)
* **定位**：Windows APT 攻防全景
* **内容概要**：这可能是本合集中最全面的一本。从 C 程序的编译流程、进程内存与 PE 解析、动态 API 调用、Shellcode 导出函数解析、PE 模块重定位、PE 转 Shellcode、软件加壳、数字签名验证到 UAC 绕过，几乎覆盖了 Windows 平台攻防的全栈知识。本目录中还附有配套的中文章节笔记（第1-10章）。
* **推荐理由**：2023 年出版，内容极为新颖和全面。配套的中文笔记进一步降低了学习曲线。如果只能选一本书深入学习 Windows 平台安全，选这本。

### 13. Windows: The Undiscovered Country — Hacking Windows and SQL Server

* **来源**：DEF CON 演讲材料
* **作者**：Chuck Easttom
* **定位**：Windows 与 SQL Server 攻击技术速览
* **内容概要**：来自 DEF CON 25 的演讲幻灯片，快速介绍了 Windows 和 SQL Server 的攻击面。演讲者 Chuck Easttom 拥有超过 25 年安全经验，参与创建了 CompTIA Security+、CEH 等知名认证。
* **推荐理由**：作为演讲材料，信息密度高、篇幅简短，适合快速了解 Windows 攻击面的全貌，可作为深入学习前的导航图。

### 14. Windows Exploitation using Windows API's

* **定位**：利用 Windows API 进行漏洞开发
* **内容概要**：聚焦于如何利用 Windows 原生 API 实现漏洞利用，包括内存操作、进程注入、权限提升等常见攻击场景。
* **推荐理由**：Windows API 是 Shellcode 和恶意软件的基础设施。这份资料帮助你理解攻击者如何"合法地"使用系统功能达成非法目的。

---

## 六、安全工具开发与漏洞利用

### 15. Writing Security Tools and Exploits

* **作者**：James C. Foster, Vincent T. Liu
* **出版社**：Syngress, 2006
* **定位**：安全工具与漏洞利用开发
* **内容概要**：教你编写"别的书只教你用"的安全工具。涵盖 Metasploit 高级载荷生成、漏洞开发的完整过程（为什么代码有漏洞、如何利用、如何修复），以及使用 Ethereal、WinDump 等工具进行 Shellcode 逆向分析。
* **推荐理由**：市面上大多数安全书籍教你使用工具，而这本教你造工具。对于想要提升到"武器开发者"层次的安全从业者，这是必读之作。

---

## 七、防御规避

### 16. Antivirus Bypass Techniques

* **作者**：Nir Yehoshua, Uriel Kosayev
* **出版社**：Packt, 2021
* **定位**：杀毒软件绕过技术实战
* **内容概要**：系统讲解杀毒软件的检测原理（签名检测、启发式分析、行为分析、沙箱）以及对应的绕过方法，包括代码混淆、内存执行、进程注入等技术。
* **推荐理由**：攻防从来都是一体两面。理解 AV 的绕过手法，既能帮助红队提升攻击能力，也能帮助蓝队理解防御盲区。2021 年出版，时效性较好。

---

## 八、内存分析与调试

### 17. Memory Thinking for C & C++ Linux Diagnostics

* **作者**：Dmitry Vostokov
* **定位**：C/C++ 程序内存诊断思维
* **内容概要**：从内存的视角分析 C/C++ 程序的运行行为，包括内存布局、内存损坏、内存泄漏等问题的诊断方法。虽然以 Linux 为平台，但其中的内存思维模型对 Windows 安全分析同样适用。
* **推荐理由**：安全研究的核心就是理解内存。无论是漏洞利用还是恶意软件分析，"内存思维"都是底层能力。这本书帮助你建立从内存角度思考程序行为的直觉。

---

## 推荐学习路线

根据以上书目，建议按以下路线循序渐进：

```
汇编基础 (#1, #2)
    │
    ▼
Shellcode 开发 (#3, #4, #5, #6)
    │
    ├──► 逆向工程 (#7, #8, #9)
    │
    ├──► Windows 安全 (#12, #13, #14)
    │        │
    │        ▼
    │    内核与 Rootkit (#10, #11)
    │
    ├──► 工具开发 (#15)
    │
    ▼
防御规避 (#16) + 内存分析 (#17)
```

**入门者**可以从 #1 + #7 + #3 三本起步，先建立汇编、逆向和 Shellcode 的基础认知。

**有经验的从业者**可以直接从 #12 (Windows APT Warfare) 切入，结合 #4 和 #16 快速补齐攻防两端的现代知识。

看到这么多书，不知道是否劝退了部分小伙伴？

源码获取

如果对银狐（winos）有兴趣，可以通过下面的方式获取全套源码：

关注后回复【winos】即可获取源码

特别申明：

**1. 本文介绍的内容仅做技术上的交流，请勿使用本文介绍的技术做其他用途，违者与本号无关。**

**2. 作者不提供任何支持免杀版本的银狐源码，不做任何黑产，有此需求的读者请勿联系作者。**

推荐阅读

[银狐远控问题排查与修复——Viusal Studio集成Google Address Sanitizer排查内存问题](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500025&idx=1&sn=62b234c8bddb267c6eb784fd8d3399b5&scene=21#wechat_redirect)

[银狐远控代码中差异屏幕bug修复](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500193&idx=1&sn=c7587c2b9d369f8a2bac15b4c648a343&scene=21#wechat_redirect)

[银狐远程屏幕内存优化方法探究](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500211&idx=1&sn=b022b7b171b8cddebef644b6fa26ee11&scene=21#wechat_redirect)

[银狐远程软件bug修复记录 第03篇](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500231&idx=1&sn=832d03b96f7c1713360c348c7ecce1de&scene=21#wechat_redirect)

[银狐远程软件 UDP 断线无法重连的bug排查和修复](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500363&idx=2&sn=1295e4610a5ff1ecc88f945b6767bd25&scene=21#wechat_redirect)

[银狐远程软件代理映射功能优化思路分享](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500374&idx=1&sn=cb33088e888e38b22f47b9ced854f29b&scene=21#wechat_redirect)

[银狐远程软件去后门方法](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500417&idx=1&sn=a9341ca6ac543ec4d1d53f1ce202934a&scene=21#wechat_redirect)

[银狐远控一键编译调试与开发教程](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500459&idx=1&sn=040336ebb05520aaf8bc8e96f224b921&scene=21#wechat_redirect)

[银狐远控免杀与shellcode修复思路分析 01](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500498&idx=1&sn=4b65c471f42785cb7157e807bb9ea12d&scene=21#wechat_redirect)

[银狐ShellCode混淆怪招](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500526&idx=1&sn=43dc3ebdd4d5277fd0bc6ffd0a5a0356&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关...