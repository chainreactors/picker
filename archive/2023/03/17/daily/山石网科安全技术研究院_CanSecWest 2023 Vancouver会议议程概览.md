---
title: CanSecWest 2023 Vancouver会议议程概览
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500394&idx=1&sn=1163426ecbf511d9ef6c213667e99cca&chksm=fa5217d4cd259ec2cc2516c1c2339d42a79a983386e912ae2357bc9c8d6d6d3839b2e36b5bc0&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-17
fetch_date: 2025-10-04T09:52:03.645571
---

# CanSecWest 2023 Vancouver会议议程概览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnT4FpT05XCAG96dMMtzMhf3t9PFGCG4FpJiarusqLFxszgzibcQLJYSmFXyeG6LWWIWHDvACNJnuUQQ/0?wx_fmt=jpeg)

# CanSecWest 2023 Vancouver会议议程概览

原创

syuu

山石网科安全技术研究院

国内在本次加拿大温哥华举办的CanSecWest 2023上分享议题的好像只有山石安研院干将实验室和阿里巴巴的潘多拉实验室两个团队，还是三天的议程，Exodus CTF和Pwn2Own都是同期举办的，在第一天的下午有两场Workshop培训活动：信息安全中的AI 编码、应用信号分析和电子战，需要自带Flippers、HackRF、SDRs、频谱分析仪、相控阵波束控制无源雷达、宽带定向天线，培训使用一些最新的应用信号技术和设备，并讨论在乌克兰战争前线的实际应用，看起来还不错。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT4FpT05XCAG96dMMtzMhf34krdMWd1rr3ST0DLlo6vTecWurX57PFyc4A8DnHhs4POH8DSgWAsvw/640?wx_fmt=png)

第一天和第二天分别有一次主旨演讲，第一场是Dino Dai Zavi迪诺·戴·扎维分享的安全成熟度曲线（Hype Cycle），Dino是Block的安全工程师兼Cash App安全主管，也是一位老黑客会棍了，出过几本苹果安全的书。第二场是Wolfgang Hagarty沃尔夫冈·哈加蒂分享的商业战争，主要是分享商业产品和开源平台在战争中的应用，在军用级设备、商业产品和自制工具之间做了差异比较。他是无人机团队负责人，过去九个月一直在乌克兰服役

下面根据CanSecWest官方的日程安排，分别简要介绍一下三天的议题内容和演讲者。

**壹**

**第一天议程**

**1. Kubernetes Bakery 攻击 : 窃取云角色**

Jay Beale是InGuardians的首席技术官和首席执行官。他作为专业威胁行为者和开源维护者和贡献者，致力于Kubernetes、Linux和云原生安全。

也许大家已经看过了Kubernetes集群攻击。然而Kubernetes防御越来越强大，打破完全集群管理的方式并不像以前那么容易了。但在大量集群中，当防御机制不像预期的那样工作时，攻击仍然是有机会实现的。将演示在云单个节点被攻击后如何导致整个集群都受攻击，并通过不断升级的防御选项继续工作。披露一个以前未知的云防御的弱点，以及一些已知但不被广泛理解的弱点。

**2. 使用COSPAS-SARSAT 406MHz进行攻击，航空航天黑客及其日益增长的重要性**

演讲者Andrei Costin博士目前是于韦斯屈莱大学（芬兰中部）网络安全高级讲师/助理教授，特别关注物联网/固件网络安全和数字隐私。

本次议题主要介绍COSPAS-SARSAT 406MHz系统，它用于卫星辅助跟踪（SAT）支持的准全球搜索和修复（SAR）操作，这是全球第一个关于COSPAS-SARSAT 406MHz的公开攻击和利用的演示。介绍其安全弱点和可能的威胁，并将展示一些早期成果（例如，欺骗）以及研究人员在进行此类研究时可能面临的一些挑战。此外，还介绍卫星和航空电子设备/航空航天和海事设备中一些额外的错误和黑客攻击，研究者还建立了一个专门的网络安全测试实验测试平台。

**贰**

**第二天议程**

**3. 微软内部安全人员对整数溢出漏洞的看法**

Rohit Mothe是微软安全响应中心（MSRC）漏洞和缓解团队的安全研究员，拥有近十年的漏洞研究和利用经验，在不同的角色中进行过研究和利用漏洞。

本演讲将深入探讨Windows上最普遍的内存安全问题之一：整数溢出。在过去的几年中，MSRC已经发现了数百个整数溢出漏洞，涵盖了大小溢出、整数截断、检查溢出以及引用计数溢出等。演讲者将讨论这些类别之间的差异，并探讨漏洞根本原因和其修复的常见陷阱。

**4. 综合内存保护 - 超越 R、W 和 X**

研究者Theo de Raadt 是 OpenBSD 的安全缓解项目和 OpenSSH子项目负责人。近30年来Theo 研究了常规代码的运行时要求，以应对针对攻击方法中使用的运行时要求，为了钝化攻击有效性，一旦这些缓解措施证明有效就会复制到其他系统中。

“Smash the Stack For Fun and Profit”（1996）中描述的攻击方法取决于堆栈是否可执行。在几年内，大多数处理器都带有MMU功能，允许堆栈被标记为不可执行。此功能已扩展为适用于所有内存，并命名为 W^X 策略。攻击者随后转向 ROP 方法，该方法利用堆栈指向必须保持可执行的代码片段（“gadgets”）。作为回应，隐藏gadgets位置的地址空间随机化在接下来的十年中变得司空见惯。可悲的是，其他软件错误可能会产生信息泄漏，从而揭示gadgets的位置，因此引入了“永远不要重用地址空间”的原则（总是fork + execve），但采用仍然缓慢。还发明了各种控制流完整性机制（如RETGUARD）来减少主要的“function-tail”gadgets，但X86风格的多态gadgets仍然是一个问题。OpenBSD是第一个向市场推出这些响应的。本次演讲将简要总结情况，然后描述 OpenBSD 中正在探索的新机制，以使 ROP 利用更加困难。

**5. xIoT黑客演示和打击黑客的策略**

演讲者John Vecchi是Phosphorus Cybersecurity的首席营销官，看介绍不像是搞技术的，在25年的从业经历中跳槽过无数的企业。

演讲中将演示针对xIoT或扩展物联网设备的几种黑客攻击，xIoT包含三个不同但相互关联的设备组，这些设备组使用专用硬件和固件运行，通常连接网络，并且不允许安装传统的端点安全控制。第一组包含企业 VoIP 电话、安全摄像头和打印机，第二组包括PLC、楼宇自动化系统和工业控制系统，第三组由交换机、负载平衡器和无线接入点等网络设备组成。老外的攻击和防御思路还是值得看看。

**6. 隐蔽包过滤Rootkits的演化**

Richard Johnson是一名计算机安全专家，专注于模糊测试和软件漏洞分析。

去年出现了几篇关于“几乎无法检测”的国家网络后门的头条新闻。在过去一年中，来自CIA和NSA泄露的网络后门被首次分析，它们使用的是与数据包过滤器相同的技术进行隐蔽信标。本次演讲将分析国家信标策略，并讨论网络过滤器的工作原理，包括深入研究Linux网络和Linux内核的多个层次。在这些层中，可以进行数据包监视和操作。最后，演讲将展望网络过滤器后门的未来，以及它们将如何使用Linux eBPF工作。并将讨论eBPF可用的低层网络挂子，并演示如果使用对eBPF国家信标策略的现代实现，包括在Linux和Windows上运行的跨平台实现。

**7. 紫队角度分析PowerZure**

Darin是思科Talos的安全研究员，专注于公共云研究。曾就职于亚马逊、美国政府、加州大学戴维斯分校和伦敦国王学院。

从紫队的角度分析一种针对微软Azure的开源攻击安全工具Power Zure。来了解如何将其用于攻击性研究，或如何在Azure的遥测中检测其许多模块（在适用的情况下带有Sigma检测规则）。本次演讲基于演讲者对如何从防御角度检测工具的独立研究，还将包括攻击功能的演示。

**叁**

**第三天议程**

**8. 对ClamAV进行沙盒化**

Jonas Zaddach是Cisco公司的安全研究员和产品研究团队负责人。

ClamAV是一款流行的开源杀毒软件，每天更新来自Cisco的Talos团队的签名集。将ClamAV库集成到应用程序中进行自定义扫描非常容易，但也会增加一个来自未知源解析恶意数据的代码片段，从而极大地增加了攻击面。所以尝试将ClamAV扫描器移动到一个单独的沙盒进程中，目标是完全透明地进行沙盒，保持当前的库界面，在所有主要平台上实现沙盒，即Windows、Linux、MacOS和FreeBSD。在文件系统访问、网络访问等方面进一步限制沙盒进程，并使用Rust进行开发，这是一种比C更安全的编程语言。

**9. S3W：Snort 3.0登陆Windows平台**

Alessandro是Cisco安全端点的软件工程师和安全研究员，目前专注于恶意软件研究和Windows攻击性和防御性安全。

横向移动已成为当今的主要攻击方式，恶意软件和攻击框架正在利用Eternal Blue和Eternal Romance等SMB漏洞在网络中传播，而Rotten Potato等NTLM漏洞的漏洞已被集成到Juicy Potato，Mimikatz和Metasploit等工具中。在这项研究中，演讲者想要展示如何通过连接入站和出站网络流信息与应用程序行为来增强端点检测和响应（EDR）系统，所以演讲者将最先进的主机入侵防御系统Snort 3移植到了Windows平台上。

尽管Snort 3在Windows平台上已经达到了Snort 2.X在Windows平台上的成就，但本研究将展示在主动模式/IPS中为Snort 3.0所做的努力。这对于Windows上的Snort也是一个全新的突破，因为Snort 2.X在Windows上也不支持主动模式。

**10.  你梦寐以求的模拟攻击**

演讲者Sebastien Tricaud是Detecteam的创始人兼CEO，也是各种流行软件的作者/贡献者。

他演示的Detecteam是一个新颖的框架，可以从行为构建攻击。通过描述攻击的各个阶段就可以实现即时数据和攻击动作的转换。然后将此攻击数据发送到日志管理系统，以确定哪些有效，哪些无效，从而识别检测差距。这可以改进系统安全性并在为时已晚之前帮助开发团队。

**11. AMI: 用新的Android MRI解释器给你的应用代码拍张照**

SungHyun Song是韩国金融安全研究所（FSI）的安全研究员，负责韩国金融行业的移动安全。

本次演讲提出了一种思路——可以通过简单的过程对应用程序的代码进行断层扫描，并跟踪代码中使用的数据流，这将是查找漏洞的有效方法。基于Android 12执行断层扫描（MRI）功能的新操作系统（解释器、运行时、内核）。在这个新的解释器上，Android应用程序在运行时拍摄dalvik指令和寄存器值的照片，生成一个控制流图（CFG），跟踪目标的前向和后向执行，提供一个有效的环境来分析应用程序和发现漏洞。此外，演讲者还将解释在使用开发的操作系统时移动应用程序中发现的漏洞。

**12.  寻找Windows桌面窗口管理器提权漏洞**

研究者是来自我们山石安研院的Junjie、Wenyue和YiSheng三位研究人员。

作为两个披露0day的压轴演讲之一放到了本次会议的最后，在过去的几年中，Windows win32k提权漏洞不断涌现。研究人员发现了新的攻击面，如win32k Callback、DirectX、Direct Composition等。即便如此，在win32k攻击面内发现新漏洞仍然很困难。Windows图形组件内是否还存在其他攻击面呢？

**13. 一个 PoC 的两个错误：在Android 12至13提权Pixel6**

研究者是来自阿里巴巴潘多拉实验室的Yong Wang。

最后的一个压轴演讲回顾一个古老的公开漏洞，并详细介绍如何逐步创建 PoC。即使没有变量分析，也可以在1分钟以内找到另一个类似的问题并创建一个新PoC。同时，同一个PoC 隐式触发另一个 Use-After-Free漏洞，而不会导致内核崩溃。在深入探讨如何利用这两个漏洞之前，演讲者将简要讨论 Android 12/13 设备root的变化和挑战。之后分别详细说明如何利用这两个漏洞，绕过一般的缓解措施（KASLR、UAO、PAN 等），并以 100% 的成功率root Pixel 6的Android 12和13两个版本。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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