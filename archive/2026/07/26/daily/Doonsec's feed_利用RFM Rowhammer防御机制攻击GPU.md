---
title: 利用RFM Rowhammer防御机制攻击GPU
url: https://mp.weixin.qq.com/s/dM8hOf0rvQsUaAeayhmWxQ
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:41:52.805854
---

# 利用RFM Rowhammer防御机制攻击GPU

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Vcvo4WRFGwU9T3CVKpicD7XY9L0ub8C8c70X1RXNsxrxPfXia1JicNV7k8datLFYzhPlTQZ2vRQlLBVqugvFVBLclEMuzrt390GWwlMibp73hJg/0?wx_fmt=jpeg)

# 利用RFM Rowhammer防御机制攻击GPU

数缘科技
数缘科技

数缘信安社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**FRONTIER INSIGHTS**

**前沿导读**

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwW44jMULnXeO5XreEQ9QiadkloyymwolCR5yvGrNWYMeIyccaLMr62YkHoIfMEXvR27xuzX6WYm25ZN6f49tQm2XJbb0ZAqrqJw/640?wx_fmt=png)

撰文 | 吴涵韬

编辑 | 刘梦迪

**GPU：你竟用我的****防御魔法****RFM对付我？**

**一、**

**背景介绍**

GPU已经从单纯的图形渲染硬件，逐渐变成机器学习训练与推理、科学计算、云端图形渲染等任务中的核心加速资源。为了满足高并行计算带来的带宽需求，商用独立GPU通常使用GDDR显存，数据中心GPU还会采用HBM等高带宽存储技术。GPU显存的结构、访存模型和内存控制器策略与传统CPU系统并不完全相同，因此许多针对CPU内存的侧信道或行缓冲攻击，不能直接迁移到GPU场景中。

在DRAM安全领域，Rowhammer是一类经典攻击手段。攻击者反复访问某些内存行，会造成相邻行受到电气干扰，进而产生比特翻转。为了缓解这类问题，内存行业陆续提出TRR、RFM等防御机制。其中RFM（Refresh Management，刷新管理）由JEDEC标准引入，基本思路是跟踪某个内存区域内的行激活次数，当访问过于频繁时触发额外刷新，避免潜在的Rowhammer比特翻转。GDDR6/6X 是首代引入RFM 的GDDR标准；同时，RFM也已经进入DDR5、HBM3、LPDDR4/4X和LPDDR5等现代DRAM标准。

然而，在USENIX Security 2025论文《Not so Refreshing: Attacking GPUs using RFM Rowhammer Mitigation》中，来自加州大学河滨分校、布鲁克海文国家实验室和太平洋西北国家实验室的研究人员指出：RFM虽然是为了防御Rowhammer而设计的安全机制，却可能在现代GPU显存中引入新的计时泄漏。作者围绕NVIDIA多种GeForce GPU和Jetson AGX Orin SoC展开实验，展示了隐蔽信道、侧信道以及拒绝服务攻击等多种影响。

**二、**

**基本原理**

这篇论文的关键点并不是直接利用Rowhammer产生比特翻转，而是利用RFM防御过程中的“副作用”。当多个进程共享同一个物理bank或sub-bank中的RFM计数器时，一个进程的访问行为会影响该区域的刷新或阻塞状态，另一个进程只需要测量自己的显存访问时间，就可能间接感知到对方的访存活动。

理解论文的核心机制，需要先区分几个概念。GDDR显存可以被看作由多个channel、bank、row和column组成的层次化结构。一个GPU线程发起全局内存访问时，如果数据没有被缓存命中，请求会进入内存控制器，再由内存控制器把物理地址翻译到具体的channel、bank、row和column。bank内部存在row buffer，当同一row已经打开时访问更快；如果需要切换到另一个row，则需要关闭当前row并激活新row。

GDDR6相比GDDR5还引入了独立通道的组织方式。论文中的图示表明，一个GDDR6 bank可被划分为两个独立通道，每个通道具有16bit数据路径，二者共同形成32bit通道。另一方面，RFM机制会针对bank或sub-bank维护激活计数器：当计数达到初始阈值时，内存控制器可以发出RFM命令触发刷新；当计数达到最大阈值时，对应区域甚至会被临时阻塞，直到后续刷新使计数下降。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWgia4yANvp46UPzlwjuNlFj4tDicsTiaZ2yrzdN8RqUNMbdyApS2KEpTG424antp5Ym5I1OUsM530mZ8hicK8jQNsE9NmYiazv7zxw/640?wx_fmt=png)

GDDR6通道组织与RFM机制示意图

RFM引入的安全风险来自“共享计数器”。RFM计数器并不是只属于某一个应用，而是与物理bank或sub-bank相关。只要不同应用的物理页落在同一个区域，它们的访问就可能共同影响这一计数器。刷新和阻塞都会改变访存延迟，因此攻击者可以通过测量访问时间来观察RFM状态变化。

这种泄漏与传统DRAMA类攻击不同。传统攻击通常依赖row buffer命中和冲突之间的时延差异；而本文强调，在GDDR环境下，row buffer超时时间较短，且进程间很难共享同一DRAM row，传统row buffer争用泄漏并不稳定。本文真正利用的是RFM刷新或bank/sub-bank阻塞造成的时延突增，也就是“安全刷新机制”本身带来的可观测副作用。

**三、**

**攻击准备与关键挑战**

论文并不是直接假设攻击者可以任意控制GPU显存，而是先解决了GPU攻击中的四个关键问题：如何控制或推断物理地址、如何绕过GPU cache、如何判断地址落在哪个DRAM bank，以及如何刻画RFM泄漏本身。这四个问题决定了攻击者能否让自己的访问真正到达DRAM，并且能否准确地把访问集中到目标bank或sub-bank。

**（一）**

**虚拟地址到物理地址：利用2MB顺序分配规律**

首先，作者在有root权限的实验环境下插桩NVIDIA开源驱动中的UVM模块，观察GPU全局内存的分配过程。实验发现，GPU显存分配以2MB为粒度，页地址按照2MB对齐，并且在逻辑上按顺序分配。这个规律使攻击者可以构造确定性分配策略：不断申请2MB页面直到失败，再释放前面的页面，只保留最后一个页面，从而在无root权限下稳定获得一个可预测位置的物理页。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWiakMqzibicXMicWf9gmG1mVcqUSnAuAZp2CibTjrqurskibliaR3ZnGtFAqylwEFfPzibn2bOyYg5TpP8lJ6g8mtXqyVnhpxicvQPibgkE/640?wx_fmt=png)

RTX 4060上的确定性物理页分配示意图

这一步对于隐蔽信道尤其重要。发送方和接收方需要约定某个bank作为通信媒介，如果完全不知道虚拟地址背后的物理位置，就很难稳定构造冲突地址组。顺序分配和最后页面策略降低了攻击对特权信息的依赖。

**（二）**

**绕过GPU cache：让访问真正到达DRAM**

第二个问题是cache。若攻击者访问的数据已经被L1或L2 cache命中，请求就不会进入DRAM，也就无法触发或观测RFM计数器。论文指出，对于GPU全局内存，许多情况下L1本来就会被绕过，或者可以通过编译选项关闭；而L2可以利用NVIDIA PTX 7.4中引入的discard指令使对应cache line失效。对于不支持discard的设备，也可以通过访问不小于L2 cache大小的缓冲区进行整体冲刷。

**（三）**

**物理地址到DRAM bank：从时延分组反推映射函数**

第三个问题是地址映射。攻击者需要知道哪些物理地址落在同一个bank或sub-bank。作者利用时延侧信道来筛选地址对：如果两个地址位于同一个bank但不同行，交替访问时会造成row buffer冲突，访问延迟会升高。根据大量地址对的分组结果，作者进一步假设GPU地址映射函数可表示为若干物理地址位的XOR组合，并借助求解工具反推bank映射函数。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWkXB0BduMiaLgduF0JiaKPUwiaoSaHWFIzPoDKblicCIhQlTdtnFknfV5tU5ZFdibGg9qfgFxOoiatZMzab5JFCWsLz7GAqk00bfXlo/640?wx_fmt=png)

同bank地址对造成的访问时延分布差异

论文还观察到，GDDR6中每个1KB内存块会因独立通道设计被分成两部分：cache block 0、1、4、5映射到同一row，cache block 2、3、6、7映射到另一row。这一发现说明GDDR6的地址映射不是简单连续切片，而是通过更复杂的交织和XOR函数把访问分散到不同bank，以提升并行性、降低自然冲突。

**（四）**

**刻画RFM泄漏：区分无竞争、row buffer竞争和RFM阻塞**

最后，作者用两个CUDA线程构造实验。线程A访问固定地址并测量耗时，线程B持续访问另一个地址。根据B地址与A地址的关系，可得到三种情形：B位于不同bank时，A几乎看不到竞争；B位于同一bank但不同RFM sub-bank时，A可能看到row buffer相关的波动；B位于同一bank且同一RFM sub-bank时，B会共同推高RFM计数器，从而让A观察到明显的RFM阻塞延迟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwUE0XeqQPe4oTFG7X7yYt0ZkJpw4EWxyUTXVoOo5Dsr5LUsvGNvX7uxJw9BA9rz9hfsBTzZsg87Uxm0JZyzsB4dADTVdb1JZas/640?wx_fmt=png)

无竞争、row buffer竞争与RFM阻塞三种时延模式对比

这个实验说明，RFM泄漏不是普通缓存命中差异，也不只是row buffer冲突。RFM阻塞会带来数量级更明显、更可识别的访问时间变化。只要攻击者能够把访问集中到同一RFM计数区域，就可以把这种延迟变化用作通信信号、指纹信号或性能干扰手段。

**四、**

**攻击实现**

**（一）**

**隐蔽信道攻击**

隐蔽信道攻击中，发送方和接收方是两个共享GPU的进程，它们不通过正常通信接口传递数据，而是借助RFM导致的访存延迟变化完成“隔空通信”。发送方若要发送1，就反复访问同一RFM区域中的多个row，推动计数器达到刷新或阻塞状态；若要发送0，则保持空闲或降低访问强度。接收方持续测量自己访问同一RFM区域时的延迟，高延迟代表1，低延迟代表0。

为了稳定同步，论文设计了预先约定的启动模式和结束模式。接收方先通过确定性分配拿到最后一个2MB物理页，发送方随后拿到相邻页面，双方由此拥有可预测的物理相对位置，并在约定bank上建立通信。论文还利用CUDA的多进程服务让多个CUDA kernel并行运行，以提高隐蔽通信带宽。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwUzrqooXBFMPBy55e1pzF0L0Lr2YU8vuEialc6mxUQwtClWTnneBxc2hz5ZnZWkq8tVrCTMKlqj0A3DAicfCKVuuic8TiavYicd4y0w/640?wx_fmt=png)

RTX 3080上隐蔽信道的带宽与错误率变化

**（二）**

**侧信道攻击：应用程序和3D渲染指纹**

侧信道攻击中，攻击者并不主动和受害者通信，而是在后台持续采样多个bank的RFM泄漏。作者把64个GDDR bank在时间维度上的访问延迟图像称为memorygram。不同CUDA应用的访存模式不同，会在memorygram中留下不同的时序纹理；不同3D角色在Blender中渲染时，由于几何结构、材质、光线追踪路径等差异，也会形成可区分的RFM泄漏图案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwVBxbQLeXRKbnuAUibIW0FZgBCf59yITMT3qptjksicAGibQ2eqhial2PsibMd9Z9Jibwom3sZ25CZVPI2w97mywFkUobWibbibvHr58AQ/640?wx_fmt=png)

不同CUDA应用与Blender角色对应的memorygram示例

在实验中，作者使用20个CUDA应用和40个Blender Studio角色作为分类对象。分类器采用修改后的ResNet-152，将memorygram调整为单通道图像输入，并使用交叉验证评估。实验结果显示，在多种RTX GPU上，应用程序指纹和3D渲染内容指纹都能达到较高F1分数。

**（三）**

**GPU到CPU攻击：LPDDR5上的跨模块侧信道**

论文进一步把攻击从独立GPU扩展到Jetson AGX Orin SoC。该平台中CPU、GPU和加速器共享LPDDR5内存，因此GPU上的攻击者可以通过共享内存系统感知CPU侧工作负载。作者展示了CPU应用指纹识别、网站指纹识别和视频指纹识别三类攻击，说明RFM泄漏不只存在于“GPU看GPU”的场景，也可能出现在SoC中“GPU看CPU”的跨模块场景。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUoOVetFo2eYKZ34jStAzGpNZQfLribdA2shZAgdZ7NRuv5zCd3ceEQLS2gd4fmPugaXTSjMjicbcFHBic4Pw7swTrMqcpdkjGhwg/640?wx_fmt=png)

Jetson LPDDR5上CPU应用指纹结果与RFM信号示例

**（四）**

**拒绝服务攻击**

拒绝服务攻击则直接利用RFM阻塞的性能副作用。攻击者持续对不同RFM sub-bank发起高强度访问，使bank进入频繁刷新或阻塞状态。由于受害者与攻击者共享物理显存资源，受害者访问这些bank时会被迫等待，从而出现显著变慢。论文在Blender渲染基准上展示，正常情况下所有benchmark总耗时约23分钟；攻击者同时运行时，总耗时增加到约1小时52分钟，平均减速超过4.8倍，个别任务最高接近7倍。

**五、**

**实验结果**

论文在四块NVIDIA独立GPU上评估GDDR6场景，包括两块RTX 4060（Samsung和SK Hynix GDDR6）、一块RTX 3080（Micron GDDR6）和一块RTX 3070 Ti（Micron GDDR6）。此外，作者还在NVIDIA Jetson AGX Orin 64GB上评估LPDDR5共享内存场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwWo8c1EYuIHLdKJbVKFIHa628PJ7XCtKgW1JGNyM3cyxicyoTbZW2hDuWOXdEbbHMZ9l2Mah4X30GhhQcdJwFta3PURMdNqTdD4/640?wx_fmt=png)

隐蔽信道攻击性能

可以看到，单个bank上的隐蔽信道带宽已经超过50KBps，且错误率较低。论文还指出，通过多个bank并行通信可进一步提高带宽；在RTX 4060上，双通道并行可把带宽提升到约110KBps，但错误率会有所上升。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUyS34mTcBgiaOQGGKHOtlGcpt2lPScYsdAZNF8exdXjibyaZ9ic5G6PhIfKXzSxQRzsLYibUVEO7lOMjYGpYkIk2PGf8QsT7PDkH8/640?wx_fmt=png)

GDDR6独立GPU上的侧信道指纹识别结果

应用指纹攻击的对象是20个CUDA应用，3D渲染指纹攻击的对象是40个Blender角色。结果显示，即使不同GPU厂商的显存实现存在差异，RFM泄漏仍然能提供足够稳定的模式信息，使分类模型获得较高准确率。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWR3uMvdeVGyG3UVk1icyQRibY9qL27sb2JpSnVVG3nSWiauicwU1Qv1iaGfeh30WwlW8iaWVZVN9ictBP0swCLmNDtmM3ianwZsbSrLiac/640?wx_fmt=png)

Jetson AGX Orin LPDDR5上的GPU到CPU侧信道结果

这些实验说明，RFM泄漏的影响范围并不局限于独立显卡。在CPU、GPU共享同一LPDDR5内存系统的SoC中，GPU上的攻击进程同样可能通过RFM时延模式推断CPU侧应用、网页和视频内容。

**六、**

**总结**

这篇论文展示了一个非常典型的“安全机制副作用”问题。RFM通过统计行激活次数、触发刷新和阻塞来缓解Rowhammer，但这些操作会改变内存访问时延；而时延又可以被共享GPU或共享SoC中的其他进程观察到。于是，一个原本用于增强内存可靠性和安全性的机制，反而成为隐蔽信道、侧信道和拒绝服务攻击的基础。

从研究贡献看，作者不仅发现了RFM计时泄漏，还完成了GPU物理页分配、cache绕过、GDDR bank映射和RFM sub-bank结构的逆向分析，并在真实NVIDIA GPU和Jetson SoC上实现了端到端攻击。实验结果表明，该泄漏足以支持高带宽隐蔽通信、CUDA应用识别、3D渲染内容识别、CPU应用/网站/视频指纹识别以及明显的性能拖慢。

因此，本文的价值不只是指出某一类GPU存在风险，更重要的是提醒硬件设计者：在共享计算平台中，任何共享计数器、共享刷新状态或共享阻塞行为，都可能成为攻击者观察系统活动的窗口。未来的内存防御机制需要在可靠性、性能和隔离性之间做整体设计，而不能只把“防御Rowhammer”作为唯一目标。

**参考资料**

[1] Ravan Nazaraliyev, Yicheng Zhang, Sankha Baran Dutta, Andres Marquez, Kevin Barker, Nael Abu-Ghazaleh. Not so Refreshing: Attacking GPUs using RFM Rowhammer Mitigation. Proceedings of the 34th USENIX Security Symposium, 2025.

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwXKW7hVTeFI0E6EaD0y8akRNR2Ft5tSSZx...