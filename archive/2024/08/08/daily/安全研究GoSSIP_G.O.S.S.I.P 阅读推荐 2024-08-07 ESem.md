---
title: G.O.S.S.I.P 阅读推荐 2024-08-07 ESem
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498614&idx=1&sn=9e0254d7c7866adf0d7bcc031c4aa32f&chksm=c063d5aff7145cb9daf27d576bda48633f28cdec6e2c1bbb356fd9445b168975c23c67f00a11&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-08
fetch_date: 2025-10-06T18:05:49.936930
---

# G.O.S.S.I.P 阅读推荐 2024-08-07 ESem

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJrDEYGzicsKauGGQFlg1ELiaI22ibEgGCToZAOxgp0uyibzha5Ex07Kfeog/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-07 ESem

安全研究GoSSIP

以下文章来源于COMPASS Lab
，作者zhanjx

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5AnfZSQmFEHc22KX7QV8ThTIiaePSXxS5BBusLp4ke6rw/0)

**COMPASS Lab**
.

COMPASS (COMPuter And Systems Security) lab pursues cutting-edge research in systems security (compass.sustech.edu.cn).

大家好，今天分享 COMPASS Lab 在 AsiaCCS'24 上发表的一篇论文。

题目：ESem: To Harden Process Synchronization for Servers

会议：AsiaCCS 2024

作者：Zhanbo Wang, Jiaxin Zhan, Xuhua Ding, Fengwei Zhang\*, Ning Hu

**Motivation**

对于服务器，没有可信的进程同步机制（甚至包括 TEE 和 TEE LibOS），这将导致进程同步完全依赖于内核实现。然而，来自内核的攻击者可以很容易地攻击进程同步，从而破坏视图一致性。

视图一致性意味着不同用户在同一时刻看到的数据是正确且一致的。针对现有的系统，视图一致性很容易遭到攻击者的破坏。例如，在生产者和消费者模型中，两者受其 enclave 保护，对内存缓冲区具有独占访问权。攻击者会在消费者获取数据之前释放锁。如果生产者即将写入数据，它可以获取锁并成功写入。此时，消费者取出的数据是生产者新写入的数据，而不是希望的数据，从而产生视图不一致的情况，导致 enclave 内部的执行流错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJ21NoAiceHWhQBDc4AppmR2HGgokicYNqNFN8SRLd1FyM0UVgcIwA6ib3A/640?wx_fmt=gif&from=appmsg)

图1：攻击者破坏视图一致性示意图。

**Attack Model**

ESem 假设攻击者可以操纵同步对象来破坏进程，并且应用程序和 ESem 之间的安全信道无法被拦截。ESem 不考虑拒绝服务攻击和应用程序的保护。

**Overview**

在 ESem 的设计方案中，使用 SGX 保护进程同步，并选择 semaphore 作为受保护的同步原语。对于传统的 semaphore，它由内核管理，应用程序可以通过 glibc 提供的接口来调用它，从而使用 semaphore 操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJUibZhnFvJN7ZrNAUuHx01l9Im7zUxrKStZibUQ61TU2vK72ae04DKngg/640?wx_fmt=png&from=appmsg)

图2：传统 semaphore 架构图。

在 ESem 架构中，包括 s-enclave、ESem glue code 和 ESem Manager。其中 s-enclave 存储 semaphore 对象和操作，并且还包含 Authenticator 和 TCS Allocator。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJyjKq8fS4jficC5wRz5PU9mgEke9TAa1efDcdye0Ficb64zjhqUjwBBdg/640?wx_fmt=png&from=appmsg)

图3：ESem 架构图。

对于 ESem 的工作流程，首先应用程序通过 glue code 提供的接口调用 Manager，Manager 将 s-enclave 映射到应用程序进程页表，并初始化 s-enclave。之后应用程序可以通过 glue code 提供的接口进入 s-enclave，使用 P/V 等操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJURdqGcL9UprTGvsobAanztR2gdq0887EJlOwVzFUtibVvIKICOHfsWA/640?wx_fmt=png&from=appmsg)

图4：ESem工作流程示意图。

ESem 所面对的主要挑战是 enclave 提供的进程内隔离和希望的进程间同步相冲突。即进程同步涉及多个进程的管理，如果希望使用 enclave 来保护 semaphore，则需要 enclave 能够同时被多个进程访问，然而 enclave 只能为单个进程服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJHAHXAtuXGrrgbibkM9d3SJUxb3IChLdpCibqCJILjibUWmI2lbShDaamA/640?wx_fmt=png&from=appmsg)

图5：Enclave 仅服务单个进程示意图。

**Enclave Management**

为了解决上述的主要挑战，ESem 引入 enclave roaming 机制。Enclave roaming 由 ESem Manager 管理，即 ESem Manager 将 s-enclave 的 PDPT page entry 复制到进程的 PDPT page。当进程关闭其 e-semaphore 时，ESem Manager 会删除映射。从而保证所有进程共享相同的 s-enclave 映射，打破了 enclave 单次只能服务于单个进程的限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJmkTiaHkOicbyjmib74S7icqe7rU4AFtJMRibBdqMiajPYsbo3oONH7KZfyJg/640?wx_fmt=png&from=appmsg)

图6：Enclave roaming 示意图。

**Access Control**

ESem 在 s-enclave 中设计了 Authenticator，它用来维护一个 semaphore metadata table 来存储进程信息并执行访问控制。在创建 e-semaphore 期间，如果进程具有 enclave 应用程序，它可以与 s-enclave 共享密钥，并且通过修改 semaphore metadata table，将 e-semaphore 的访问权限授予该进程。否则，它只能通过 PID 进行身份验证。

表1：Semaphore metadata table 示意表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJzdkKmZ1G6qx3fMLFjH915DHVj7OJMT3m9SQql9JkgNva67w9WohU1g/640?wx_fmt=png&from=appmsg)

**Thread Management**

ESem 设计两种 TCS 管理模式。在 Thread-Semaphore Binding 模式下，访问 e-semaphore 需要竞争 TCS，所以不需要锁定 e-semaphore；在 Thread-Process Binding 模式下，进程只能访问绑定的 TCS，从而减少对 TCS 的竞争，但是 TCS 会竞争 e-semaphore，所以 ESem 在这种模式下引入自旋锁来进行访问保护。另外，ESem 还支持 SGX Switchless 模式，这将提高某些场景下的性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJEykhBBlMzJnkia0ovdibCVBpJWYI3fI5etoVmhwN4iaCMS9bxRbP9fYNg/640?wx_fmt=png&from=appmsg)

图7：TCS两种管理模式示意图。

**Performance Evaluation**

针对 ESem 的性能评估，从三个方面展开，包含微观、宏观和真实应用场景的评估。结果展示表明 ESem 不会对系统造成过大开销。

（1）针对 ESem 的关键操作进行评估，每个操作都在15微秒内。

表2：ESem 关键操作评估表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJPQIwP7EmRV4aMpKp81JusLKTSLLzLeuoiavMj0yNKialUqFibEA9ibZoSA/640?wx_fmt=png&from=appmsg)

（2）使用 PTS-NG 和 LMBench 进行基准测试，结果表明 ESem 不会对系统性能产生过大影响。

表3：PTS-NG 评估表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJSEZXm83HrySX5px0kTwibCK3taAF5KqmeKjApBEZBapiboBtPBPLANlw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJhCCI4B64ibBmQvhGObasTMVyjicwYl8melsNVFWm0PchZ0jE4eZBib5eg/640?wx_fmt=png&from=appmsg)

图8：LMBench 评估图

（3）将 ESem 投入到实际应用中进行性能评估，发现性能下降不到3%。

表4：真实应用场景评估表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJxRLzEq1mfPpYhp59J8c6fbZXN0d5ibaibDrIljnS3GvWOEvnLdO2Utlg/640?wx_fmt=png&from=appmsg)

**Application of ESem**

ESem 选用 File Vault 作为一个示例应用。因为它使用 SGX 来保护文件系统，但它不保护文件系统所依赖的进程同步。对于普通的 File Vault，我们进行两种攻击。

第一种是 file tree race。来自内核的攻击者忽略了 semaphore 对象的真实值。线程0请求 semaphore，它可以直接获取 semaphore。然后，它在 enclave 中插入一个新的 file tree 节点。在关键操作完成之前，线程1也可以直接获取 semaphore 并对 file tree 进行操作。此时，就会出现竞争条件，enclave 中的 file tree 将被破坏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJhPF9kW0y3iaia07HNjwibGto2KC2W9k4BZ7o2cqEGib9icuKA5s0D5FNw3Q/640?wx_fmt=png&from=appmsg)

图9：File tree race 示意图。

第二种是 service thread blocking，这种攻击方式和第一种类似，但后果不同，由于 TCS 数量受限，且忽略 semaphore 的值，导致所有进程都能获得 semaphore，并等待进入 enclave，会导致服务线程阻塞，性能降低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJhnvibxdx3Gc6IcsMu5d4qR9svf6D8jtUUfXEfMsa7wk5LiaraCyAMUcQ/640?wx_fmt=png&from=appmsg)

图10：Service thread blocking 示意图。

ESem 在 File Vault 中引入 s-enclave，将进程同步服务放入其中，从而防御上述攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Veiafam9G7EXaJNy3icOWP2khcEMWwokxJHa7BgLfBt20N4C0Q52DQS0sl9EAxJ98wtYOtdxwc4v4b21WttUtdIA/640?wx_fmt=png&from=appmsg)

图11：ESem 针对 File Vault 的保护示意图。

**Conclusion**

ESem 通过硬件辅助隔离技术保护进程同步免受内核特权攻击。具有平衡的安全性和性能，符合 POSIX API 标准，拥有高兼容性且适用于实际应用。

在未来的工作中，我们将继续探索同步机制，并尝试保护 enclave 内的共享资源以及与其他基于 TEE 的解决方案进行比较，以进一步增强 ESem 的安全性和适用性。

如果您对此项工作感兴趣，欢迎阅读论文原文或者联系我们，谢谢。

论文地址：https://dl.acm.org/doi/10.1145/3634737.3657025

笔者邮箱：zhanjx@mail.sustech.edu.cn

张老师邮箱：zhangfw@sustech.edu.cn

**END**

预览时标签不可点

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