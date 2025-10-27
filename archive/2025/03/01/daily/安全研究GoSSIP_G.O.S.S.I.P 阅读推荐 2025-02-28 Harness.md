---
title: G.O.S.S.I.P 阅读推荐 2025-02-28 Harness
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499812&idx=1&sn=b22c89c59ff559db016290327823bbf2&chksm=c063eefdf71467eb27e983516d91612cc446536f265400aa74e56603b38f3568402a6e64cf05&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-03-01
fetch_date: 2025-10-06T21:58:58.665192
---

# G.O.S.S.I.P 阅读推荐 2025-02-28 Harness

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvzEicfeHNqPG9ibKUk6CkjkmSoaiauwk8I4T7ObYc6yAxs3c0JLKFIMDMQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-28 Harness

Haochen

安全研究GoSSIP

今天为大家推荐的论文来自浙江大学计算机科学与技术学院常瑞老师研究组在 USENIX Security 2025 上发表的最新工作 **Harness: Transparent and Lightweight Protection of Vehicle Control on Untrusted Android Automotive Operating System**。该工作提出了⼀套可透明部署于Android⻋载系统（AAOS）的轻量化⻋控保护框架，可保护AAOS中的车控链路抵御系统级别的攻击，提升智控车辆安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvgk2RIEsXeZAEormD2m5Njexsd9Bt1mu1EPFoLjBtCW7NTRFFVR59zA/640?wx_fmt=png&from=appmsg)

继提出支持x86/ARM32架构的高效无限域隔离架构 VDom: Fast and Unlimited Virtual Domains on Multiple Architectures (ASPLOS’23) 和支持ARM64架构的轻量级进程内隔离架构 LightZone: Lightweight Hardware-Assisted In-Process Isolation for ARM64（Middleware’24）之后，研究组首次针对AAOS的攻击面进行了系统分析，将基于硬件虚拟化的隔离技术用于AAOS的车控防护中，为当前智能车载系统提供了一种可行的防护方案。该论文主要贡献如下：

1. 首次对 AAOS 车控链路的攻击面展开系统研究，识别并总结了13种潜在攻击策略。
2. 提出了一种基于虚拟化的框架，可以高效保护车控链路免受不可信AAOS的侵害，并支持透明部署使用。
3. 基于Google Cuttlefish虚拟平台实现了原型，通过保护具体样例组件展示方案的可用性。
4. 在真实的硬件平台全面地评估了原型，证明了其安全性和高效性。

## 背景与研究动机

随着汽车智能化发展，现代的车载娱乐系统（In-Vehicle Infotainment，简称IVI），如主流的AAOS，不仅能提供丰富的娱乐功能，还集成了车辆控制功能。这样的集中化设计能够提升用户体验，且有助于资源管理和成本控制，但同时也扩大了攻击面。AAOS具有庞大而复杂的软件栈，且支持无线连接和三方应用等风险功能，这使得攻击者容易利用其中的漏洞获取**系统权限**，并进一步利用车控功能夺取**车辆控制权**，造成严重的安全威胁。在此背景下，如何在不影响AAOS丰富生态功能的前提下保护其中的车控功能，让其符合用户意图，是一个亟待解决的问题。为此，作者分析了AAOS的攻击面并设计了保护方案Harness，让车载系统的车控行为真正“掌控“在用户手中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvqkldKwuGAejQ3Dx8jibgEKOJzIiaKe66NibkqWuoibHGuEAQZ9iaaS2uMEw/640?wx_fmt=png&from=appmsg)

图 1：攻击者可以通过IVI系统控制其他车载系统

### AAOS车控的实现

从用户角度来看，只需点击触摸屏就可以控制车辆（本文不考虑语音控制），但这背后是一个复杂的系统流程。汽车内部有许多电控单元（Electronic Control Unit，简称ECU），分别用于控制车辆的各个子系统，例如车身状态、动力、空调等。另一个重要的部件是车载主机（Head Unit，简称HU），HU通常会**使用虚拟化技术运行多个系统**，包括IVI、仪表系统、智驾系统等。HU和其他ECU通过车内网络互联，因此IVI系统得以通过网络向其他ECU发送控制命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvwJeSYd8YDYBllgyIObtGnvfDBuHVJGYoy0wPqKQSdFW0mrZPQaRUpA/640?wx_fmt=png&from=appmsg)

图 2：AAOS中的车控链路

在AAOS内部，车控的实现可分为三个阶段：

人机交互阶段：用户在屏幕上浏览车控应用的GUI，然后完成一次触控。Android应用在自身进程内渲染GUI，之后由Hardware Composer（HWC）进程合成最终GUI帧，并通过Linux内核的DRM驱动输出至显示器。当用户触摸屏幕时，硬件产生中断，内核输入子系统会读取坐标等硬件数据并将其封装为输入事件，随后由Input Manager Service（IMS）整合并派发至目标车控应用。

处理决策阶段：车控应用处理用户输入，调用车系统服务的接口。此阶段涉及两个关键组件，CarService和车硬件抽象层VHAL，均以独立进程运行。CarService提供了CarPropertyService等车控服务。车控应用调用这些服务的接口后，服务会进一步使用VHAL的接口。车服务和VHAL的接口则均通过安卓接口定义语言（AIDL）定义，其会通过Binder机制实现进程间通信（IPC）。CarService和VHAL会向ServiceManager注册自身，进而能被其他组件查询并连接。

控制输出阶段：CarService调用VHAL进程的接口后，VHAL最终通过车内网络与其他ECU通信以最终执行车控。VHAL则负责处理车相关的硬件操作，它定义了车辆的属性（如车速、电量油量、门窗状态等），同时也负责管理这些属性。

### 潜在的车控攻击

表 1：IVI系统中车控链路的攻击面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dv6fj4ouybslPQT9TCep27TAcLJhyJlwxCFJvINHlzA0YZrm1Mt8Om0g/640?wx_fmt=png&from=appmsg)

威胁模型与假设：本文假设IVI中存在软件漏洞，三方应用和操作系统均不可信，但硬件和虚拟化技术中的hypervisor可信，同时假设硬件平台为Arm64架构。

车控攻击面：通过对先前工作和车控链路的分析整理，本文总结了13种攻击策略，每一种都可以破坏车控链路的完整性，导致车辆面临失控风险。其中包括隔离类工作最常见的内存攻击、Iago攻击（A1-3，A7），I/O驱动攻击（A4），文件攻击（A9-10），非法接口调用（A8，HA1）。还有针对AAOS这类系统的攻击，例如利用系统组件之间的依赖关系，发起服务伪造（A5），数据伪造（A6）攻击，还可以针对人机交互发起GUI混淆（HA2）、触控伪造（HA3）攻击。

## Harness设计

AAOS存在安全风险的根本原因在于可信计算基（TCB）过于庞大，涵盖了从内核到用户态的大量软件。因此需要将无关软件排除至TCB外，仅保留车控组件，这一点可以通过**隔离执行环境**实现。考虑到可用性，作者倾向于使用**基于硬件虚拟化的隔离执行环境**（如ASPLOS’08的Overshadow和OSDI’22的BlackBox），这类方法支持保护未修改的软件，同时也能兼容更多硬件平台。

### 安全边界定义

Harness首先定义一个保护域，确定纳入TCB并保护的组件。CarService、VHAL，以及具备敏感车控接口访问权限的系统车控应用都应被纳入保护域，确保这些接口仅在域内调用，形成明确的安全边界。此外，由于HWC直接涉及GUI显示，其也应被纳入保护域。IMS虽负责触控输入，但因其运行于庞大且易受攻击的SystemServer进程，不宜纳入保护域。保护域的安全需要满足**4个要求**：

1. 域内发起的车控需要被安全发往目标ECU，保护域外的软件不得发起车控。
2. 域内进程的内存和寄存器需正确加载，并与不可信软件隔离。域内的物理内存页需要被映射到正确的位置。
3. 域内的进程可以安全地通信，防止通信伪造和数据篡改。
4. 车控人机界面需要得到保护，确保用户看到正确的车控GUI，且屏幕操作能准确派发至目标应用。

### Harness架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvTrHuTnNOmvibYtuDzAYxZTibJMyXf4vMHxbkpEE18fSchp8U3WjenUvA/640?wx_fmt=png&from=appmsg)

图 3：Harness架构示意图

Harness在Hypervisor中引入了一个Lowvisor模块，它通过进程级隔离环境（enclave）隔离保护域中的所有组件，同时保护它们之间的协作，并监控它们与域外软件的交互。

Lowvisor为每个enclave分配维护独立的页表和嵌套页表，进而创建了与IVI系统隔离的地址空间，其拥有独立的用户和内核空间。Lowvisor在每个enclave的内核空间映射了受保护的异常向量表，以截获enclave运行期间的异常。类似先前工作，大部分异常（如缺页、syscall）会被交由不可信OS处理，Lowvisor会检查结果并更新enclave状态。此外，Lowvisor会为enclave维护隔离的CPU上下文。

然而，要适配并保护AAOS的车控链路，Harness还有**三个挑战**需要解决：

1. 为促进资源利用和跨进程协作，Android进程依赖共享内存，但这与隔离是相违背的。现有基于软件的隔离方案均不能适配。
2. Android进程会频繁使用Binder，现有的基于加密的IPC保护方案难以适应其复杂的机制，同时会造成很大的性能开销。
3. 透明地保护人机界面存在挑战，若隔离所有相关软件（如SystemServer）会严重扩大保护域的攻击面，隔离相关I/O驱动也十分困难。

为此，作者提出了**三项关键技术**。

共享感知的内存监视器：Harness将进程间共享内存分为隐式和显式。前者指写保护内存，Lowvisor通过嵌套页表强制写保护，并支持写时复制。后者则指进程主动声明内存为共享。对此，Lowvisor首先记录所有enclave打开的资源，并通过令牌控制enclave对资源的访问权限。Lowvisor根据资源拥有者enclave的共享意图授予令牌。同时，Lowvisor监控各enclave的内存管理系统调用，解析其映射意图并记录在虚拟内存映射表中。Lowvisor会为初次映射的物理页创建一份元数据，记录所属资源的令牌等信息。当页再次映射时，Lowvisor通过其元数据和虚拟内存映射表检查映射的合法性。

Binder通信保护与认证：Harness扩展了AIDL，允许开发者灵活标记需要保护的接口。这些接口只能由enclave内的组件实现和调用，其他接口则不受额外限制。扩展的AIDL编译器会为调用双方生成调用门（call gate）。调用方的调用门会在Binder通信数据中嵌入保护标识以提示Lowvisor需要保护。Lowvisor会追踪enclave注册和获取的服务，从而基于此判断目标enclave，同时确保通信双方为互相信任。Lowvisor还负责传递受保护通信数据，目标enclave接收通信前，Lowvisor将数据拷贝到其地址空间，并依据通信发起方是否可信在数据中嵌入保护标识。该enclave继续执行时，其调用门确保仅在检测到标识时执行接口。

基于校验的人机界面保护：车载系统通常采用virtio实现I/O虚拟化，包括触控、渲染与显示。本文首先提出了virtio设备绑定机制，其将受保护的设备与信任的enclave绑定（如将virtio-gpu与HWC绑定），防止攻击者通过其他软件控制I/O设备。Harness还会隔离保护virtio-gpu、HWC和车控应用间共享的缓冲区，避免GUI被篡改。对于触控，本文设计了一种基于校验的保护机制。用户触控车控GUI后，Lowvisor通过队列记录硬件生成的触控事件，并在车控应用接收到触控信息时，通过与先前记录匹配校验事件的真实性。队列中的过期事件会被及时删除，防止重放等攻击。

其他保护：除了这三项技术之外，Harness还支持一些基本的安全保护，包括enclave可执行文件的完整性校验，enclave身份认证，VHAL与ECU通信的加密保护等。这些都利用了相对成熟的技术，详细设计可以在论文查看。

## 实验评估

作者实现了Harness原型并基于树莓派5展开实验，将树莓派OS作为host（内核版本rpi-6.6.y），并通过Google Cuttlefish启动虚拟设备作为IVI（Android版本android-13.0.0\_r41，内核版本common-android13-5.15）。

### 安全性评估

本文首先从理论上评估了Harness的安全性，分析了其如何抵御前述的攻击策略，以及现实中的攻击案例和26个相关的CVE。然后，本文通过实验模拟了前述的所有攻击策略，进一步证实了Harness的安全性。

表2：IVI系统中的CVE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvjlJb72wrlrjuDSxvbO72wyxfPCicld3icYzaMIvr0gOghbJcYzTfOkcQ/640?wx_fmt=png&from=appmsg)

### 性能评估

本文首先使用LMBench微基准测试评估了基本系统功能的开销，性能开销主要源于enclave和内核之间的上下文切换、缺页处理，以及enclave创建（fork相关测试）。

表 3：LMBench测试结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dva7RC6qYBWKnib5HkBtSoyvBw64toXj2IpBFNVjvCsViaMEKYX6qEb6OQ/640?wx_fmt=png&from=appmsg)

对于微操作，本文还评估了Binder保护、人机界面保护引入的性能开销，以及受保护应用的启动时延和受保护接口的调用时延，开销均可接受。其中Binder保护的性能较先前工作中基于加密的方法快7.5倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibUVTy5IoMRpzg2nl8f9dvgqX1ZaKHDeFxvoXuc1hHKvsvU8wicIziaINs3CzF71XWgyPNfECYfhvQ/640?wx_fmt=png&from=appmsg)

图 4：Geekbench单核/多核测试性分数标准化结果

之后，本文使用Geekbench评估了实际应用的性能开销，平均而言，Harness在单核/多核测试中分别引入了3.35%和6.09%的性能开销。最后，测试还表明，Harness的内存开销不超过4%，且部署Harness不会影响系统中未受保护部分的性能。

## 总结

Harness是一种可透明部署使用且轻量化的保护框架，它可以保护AAOS的车控链路，让车控执行符合用户意图。本文首先分析了AAOS中车控的执行流程并总结了潜在的攻击面。基于硬件虚拟化，Harness创建了隔离执行环境以保护车控相关的安全攸关组件。通过三项关键技术，即共享感知的内存监视器、Binder通信保护与认证和基于校验的人机界面保护，Harness可以高效无感地保护车控组件之间的协作，确保整个车控链路的完整性。

更多交流欢迎与作者联系。

#### 投稿作者介绍

宫浩辰：浙江大学计算机科学与技术学院博士生，导师为常瑞老师。研究方向主要为操作系统安全，在 USENIX Security, TIFS 上发表过研究成果。曾获全国大学生计算机系统能力大赛龙芯杯一等奖和OS设计赛一等奖。联系邮箱：gonghaochen@zju.edu.cn。

常瑞：浙江大学副教授，博士生导师，研究方向为系统安全与形式化方法，在ASPLOS、CCS、USENIX Security、TIFS等体系结构与安全领域的顶级会议/期刊发表论文30余篇。邮箱：crix1021@zju.edu.cn。主页：*https://person.zju.edu.cn/changrui*。

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