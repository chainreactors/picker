---
title: 人与AI协同的漏洞分析新范式——Copy Fail发现过程解析
url: https://mp.weixin.qq.com/s/gCFqLt0YL3H3cQuqLuGvdQ
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:58.119619
---

# 人与AI协同的漏洞分析新范式——Copy Fail发现过程解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk92xOwqn6xCyk41CaBc9uZNetRcsiaRnyDXDkX0kdPuRLfw6BlLiatgu5ksJQ4Yo4neQDCD0vgt5ZOlNKbwlIgwIhJ67bBibKoEDU/0?wx_fmt=jpeg)

# 人与AI协同的漏洞分析新范式——Copy Fail发现过程解析

安天CERT
安天CERT

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

AI赋能的漏洞挖掘与自动化攻击无疑是2026年的关键重点。此前Anthropic批量爆出FreeBSD远程Root漏洞（潜伏17年）、FFmpeg H.264堆越界写漏洞（潜伏16年）、OpenBSD远程崩溃漏洞（潜伏27年），为Mythos Preview模型和Project Glasswing计划大秀了肌肉。而由于Copy Fail漏洞是一个本地提权漏洞（LPE）等原因，尽管它让全球大量的安全运维者和安全分析者经历了一个加班加点的“劳动节”，但在“一知半解”的AI自媒体眼中，完全没有得到足够的关注。但显然对于安全研究者来说，相较于Mythos Preview的犹抱琵琶半遮面，Copy Fail漏洞的曝光过程拥有更多可参考信息，其“研究者+AI平台”的组合其实是更值得研究的参考样板。

## **1. 背景：发现Copy Fail漏洞代表人机结合的新范式**

##

### **1.1 Copy Fail漏洞的发现过程**

###

2026年3月23日，Theori研究员Taeyang Lee向Linux内核安全团队提交编号CVE-2026-31431的漏洞报告，代号“Copy Fail”，CVSS评分7.8（高危）。该漏洞位于内核crypto子系统的authencesn（Authenticated Encryption with Associated Data Extended Sequence Number）加密模板中，属逻辑缺陷型漏洞，非传统内存破坏类型。攻击者利用它可实现100%稳定的本地权限提升，整个利用过程仅需732字节Python脚本。

从影响范围看，漏洞根因可追溯至2017年1月的commit 72548b093ee3，该提交在algif\_aead模块中引入了AEAD（Authenticated Encryption with Associated Data）解密原地（in-place）处理优化。由此计算，该漏洞已存在超过八年，覆盖2017年至今几乎所有主流发行版，包括Ubuntu 24.04 LTS、RHEL 8/9/10、Amazon Linux 2023、SUSE 16等。安天CERT已在过去两日发布的长篇文献《CVE-2026-31431（Copy Fail）漏洞FAQ》[1]中，完整说明了该漏洞的基本情况、影响范围、利用条件、修复环节检测取证相关措施等，而本文则希望重点分析在生成式大模型技术高度成熟的时代，分析者与人工智能间新的分工范式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHk9zAdK1icYgHuibKKHRWZVUvGI2QQk5gqC7o9IdT2iaa9IxcRhgGLHNmicAgicnUA7npKCbJBwfLVdSgibvTA4STicnwBhDWLUCTuukDQ/640?wx_fmt=png&from=appmsg)

Copy Fail的发现方式比漏洞本身更具范式意义——它既非“AI自动找到”的神话，也非“人类手动审计发现”的传统路径，而**是人类研究员与AI平台精准协同的产物**。

具体过程分为两个紧密衔接的阶段。第一阶段，人类洞察定义攻击面。Taeyang Lee基于其kernelCTF（Kernel Capture The Flag）经验，识别出AF\_ALG（Address Family Algorithm）加密套接字接口与splice()零拷贝系统调用的组合攻击面，提出核心假设：“AF\_ALG + splice等于给无特权用户开了一扇直通内核加密子系统的后门”。第二阶段，AI实现规模化扫描。 Lee使用Xint Code AI代码分析平台对crypto子系统发起定向扫描，Xint Code在约1小时内完成跨文件深度关联分析，遍历algif\_aead与各类加密模板间的全部交互路径，精准定位authencesn模板中的逻辑缺陷。

从深层成因看，Copy Fail是三个独立且各自合理的代码变更间接交互的结果：2011年的authencesn算法实现、2015年的splice零拷贝支持引入，以及2017年的in-place性能优化。任一变更单独审查都无懈可击，组合后却产生致命后果——这种“组合爆炸”式漏洞成因，正是传统人工审计最难覆盖的场景。

### **1.2 人机新范式的确立**

###

Copy Fail的发现揭示了一种新的安全工作范式：**没有卓越分析师的洞察，AI平台不会知道将扫描资源聚焦于哪个方向；没有Xint Code，Lee不可能在合理时间内完成对复杂的规模代码所有交互路径的穷举扫描。**

这一范式区别于两种误解。它并未满足对“ AI独立发现重大漏洞”的期待——AI在此处展现的是规模化执行能力，而非战略方向判断能力；同时也表明，在软件复杂度已经远远超越人的设计能力，包括Linux内核都超过3000万行代码的规模下，纯粹依赖人类手动审计已面临根本性瓶颈。**人类研究员与AI工具之间形成的“方向设定—规模执行—结果验证”闭环，代表了一条更为现实且高效的前进路径**。

## **2. 从发现Copy Fail的五大原因看人机分工**

##

### **2.1 原因一：研究者先验知识的精准聚焦转化为直觉判断**

###

#### *2.1.1 Taeyang Lee在kernelCTF中系统性绘制AF\_ALG攻击面的先验知识构建过程*

####

Copy Fail的发现并非偶然，而是Theori研究员Taeyang Lee在kernelCTF中**积累的AF\_ALG攻击面知识的直接延伸**。kernelCTF要求参与者深入理解内核子系统的交互边界，Lee在此过程中系统性地梳理了AF\_ALG（Address Family ALG，内核加密套接字地址族）接口的调用链、权限模型及数据流路径。Theori团队自2013年以来持续斩获DEF CON等顶级CTF赛事冠军，这种高强度竞技训练**塑造了对“低权限入口、高权限内核操作”型非对称接口的敏感嗅觉**。

|  |  |  |  |
| --- | --- | --- | --- |
| **知识/经验** | **具体内容** | **转化为攻击面直觉的路径** | **对发现Copy Fail的贡献** |
| kernelCTF竞赛实践 | 系统性绘制AF\_ALG套接字完整攻击面，包括socket创建、splice、sendmsg/recvmsg等代码路径 | 识别AF\_ALG为“低权限入口、高权限操作”的非对称接口，判断其交互组合存在未审计的脆弱地带 | 将搜索范围从数百个子系统收窄至crypto/子系统 |
| splice()零拷贝机制深度理解 | splice()将只读文件的页缓存页面以引用方式直接传入内核子系统 | 页缓存页面的只读属性可能在目标子系统内部被重新诠释 | 构成operator prompt的核心技术假设 |
| scatterlist内存模型知识 | 内核加密子系统使用scatterlist管理非连续物理页面的机制 | scatterlist中页面可写性与来源属性的不一致可被利用 | 指导AI关注页面来源与destination SGL可写性间的安全假设断裂 |
| CTF攻击思维模式 | “最小权限到最大影响路径”的系统性思维 | AF\_ALG + splice被判定为“给无特权用户直通内核加密子系统的后门” | 假设定向精准，AI一小时扫描命中最高危漏洞 |

四层知识相互叠加，收敛为精准假设：AF\_ALG + splice构成无特权用户向内核加密子系统注入页缓存页面的隐蔽通道，scatterlist页面来源的属性错位是最具漏洞潜力的环节。

#### *2.1.2 核心假设的形成与独特价值*

Lee的核心假设实质是识别了三要素交互中的安全假设断裂：splice()传入页缓存页面的只读引用，而2017年in-place优化（commit 72548b093ee3）将页面链入可写的destination scatterlist，为authencesn模板的越界写入创造条件。

这一假设的非凡之处在于其精准方向性。它并非泛化要求“审计crypto/子系统”，而是明确指出“splice()可以将只读文件的页缓存引用传递给加密TX散射列表”。这种定向是AI无法自发形成的——即便掌握AF\_ALG和splice()的独立语义，AI也无法将二者关联为跨子系统攻击面。Xint Code的总结极为精确：“a researcher identifies the attack surface, XC analyzes it”。人类研究员的核心价值，正是为AI提供无法算法化的直觉焦点，使其计算能力投向真正具备漏洞可能性的代码区域。

### **2.2 原因二：AI的规模化和关联能力可以泛化研究者直觉洞见**

#### *2.2.1 AI平台在接到操作员提示后完成的传统审计方法不可能完成的任务*

Taeyang Lee基于kernelCTF经验提出假设：AF\_ALG套接字与splice()零拷贝的组合，可为无特权用户打开直通内核加密子系统的通道。将这一直觉转化为可验证发现，面临规模化困境。

Linux内核crypto子系统由数十个源文件、多个算法模板层和异步调用构成，涉及AF\_ALG套接字层、AEAD模板层、scatterlist（SGL）管理及页缓存子系统的多向交互。传统静态应用安全测试（SAST）依赖预定义规则和模式匹配，存在两个缺陷：规则库仅覆盖已知漏洞模式，无法识别“多个独立合理设计组合后产生不合理结果”的涌现性缺陷；缺乏跨文件语义理解能力，难以追踪同一操作在splice()层为”零拷贝引用”、algif\_aead层为“in-place（原地）解密优化”、authencesn层为”HMAC验证前4字节标签写操作”的完整语义链条。

Xint Code AI平台约1小时完成crypto子系统全量扫描，突破了传统审计工具的三个能力边界：跨文件语义关联——将algif\_aead.c的in-place标志、authencesn.c的标签写逻辑与splice()引用的页缓存建立安全语义映射；攻击路径组合推理——识别出AF\_ALG→splice()零拷贝→in-place解密→认证前写操作的完整攻击链；全子系统覆盖——发现Copy Fail（CVSS 7.8，该次扫描最高严重性）及其他处于协调披露阶段的高危缺陷。

#### *2.2.2 AI平台能够在多个源文件之间建立安全语义关联*

Copy Fail的发现揭示AI辅助审计的本质优势：大型语言模型（LLM）具备语义层面理解跨文件上下文的能力，能识别传统SAST无法捕捉的“设计组合型”缺陷。学术界将传统工具无法覆盖的空间称为“语义鸿沟”（semantic gap）——介于模糊测试输入覆盖与规则匹配已知模式之间的盲区。Copy Fail正位于该鸿沟核心：commit 72548b093ee3的in-place优化局部合理，splice()零拷贝是标准行为，authencesn的标签处理符合AEAD规范，三者独立审查均不会触发SAST告警。

人类审计师理论上可经深度走读发现跨组件缺陷，但面对crypto子系统量级的交互路径分析，认知规模存在天然上限。AI平台的价值并非替代人类安全直觉——Lee的攻击面假设仍是逻辑起点——而是将人源性洞见规模化泛化：单点假设扩展为面状扫描，“这可能有问题”转化为跨数十个源文件的安全语义图遍历。SAST做不到跨文件语义推理，人类审计难以穷举全子系统路径，AI平台恰好填补了二者间的结构性空白。

### **2.3 原因三：人机结合能突破传统漏洞分析方法的盲区**

#### *2.3.1 Copy Fail作为跨子系统逻辑缺陷的难以发现性*

Copy Fail（CVE-2026-31431）并非传统内存破坏漏洞，而是一种涌现性漏洞（emergent vulnerability）。其根源于三个独立且合理的内核设计决策的叠加：2011年authencesn借用目标缓冲区作临时草稿；2015年AF\_ALG接口向非特权用户开放；2017年commit 72548b093ee3引入原地操作（in-place）优化。三者各自合理，但组合后致命：用户通过splice()将页缓存传入AF\_ALG套接字时，页缓存被链入可写输出scatterlist，authencesn解密时写入4字节临时数据篡改页缓存。该漏洞本质是跨子系统语义交互失配，传统单组件检测方法几乎无效。

#### *2.3.2 传统漏洞检测方法的盲区分析*

|  |  |  |
| --- | --- | --- |
| **检测方法** | **核心原理** | **无法发现Copy Fail的根本原因** |
| 模糊测试（Fuzzing） | 随机/变异输入触发崩溃 | 难以构造跨越crypto、VFS和splice三个子系统的精确输入；不产生异常信号 |
| 内存安全检测（ASan/KASan） | 监测内存越界和UAF | 不涉及内存破坏，写入语义上“合法”——scatterlist标记为可写 |
| 静态分析（规则型） | 预定义规则匹配危险模式 | 无法识别splice()页缓存引用与authencesn临时写入的跨子系统隐含关联 |
| 传统SAST工具 | AST遍历和污点分析 | 粒度限于单函数或文件，难以追踪跨越splice.c、algif\_aead.c和authencesn.c的数据流 |
| 人工代码审查 | 依赖审查者经验 | crypto子系统逾数十万行，难以覆盖全部跨子系统路径 |

传统检测方法均指向局部缺陷识别，而Copy Fail的exploitability分布于三个子系统的交互边界。模糊测试期望触发崩溃，但此漏洞写入在底层完全“合法”；静态分析期望匹配危险模式，但该组合不在任何已知模式库中。这正是漏洞潜伏近9年的根因。

#### *2.3.3 AI漏洞分析的本质差异*

人机协同实现了分析范式的根本转换。Taeyang Lee基于kernelCTF攻击面理解提出假设——“AF\_ALG与splice()的组合为无特权用户打开了直通内核加密子系统的通道”，这是跨子系统语义关联的直觉判断。随后Xint Code平台利用LLM扫描crypto子系统，约1小时完成跨文件语义关联分析。

LLM优势在于语义层面的上下文理解，而非语法树遍历。LLM能同时“理解”splice()的零拷贝语义、AF\_ALG的接口契约及authencesn的缓冲区约定，识别“多个独立合理设计组合产生不合理结果”——splice()将页缓存传入加密路径时，in-place优化使页缓存从“只读输入”变为“可写输出”，authencesn的临时写入转化为“对页缓存的未授权修改”。这种设计意图与实现语义张力的识别，传统方法无法企及14。正是这种人机结合使Copy Fail这类涌现性逻辑缺陷浮出水面。

### **2.4 原因四：多种组合条件的成熟**

Copy Fail的发现是算力基础设施、AI能力临界点、研究者经验积累与攻击者经济学变迁等多重条件在2026年交汇的结果。

#### *2.4.1 算力发展为AI辅助漏洞发现提供基础支撑*

大规模语言模型（Large Language Model，LLM）辅助代码分析对计算资源的需求远超传统静态分析。Linux内核加密子系统约6.8万行C代码，涉及数十个AEAD（Authenticated Encryption with Associated Data）模板及复杂跨文件调用。GPU集群与云计算的普及使1小时内完成对整个子系统的深度语义扫描成为可能。

#### *2.4.2 2026年LLM理解跨子系统语义复杂度的临界点*

2026年标志着LLM能力的关键拐点。Copy Fail的根因涉及AF\_ALG（Address Family Algorithm）套接字接口、splice()零拷贝机制与authencesn模板三个子系统的交互。Xint Code接收研究员的关键观察后，于约1小时内完成跨文件关联分析，识别2017年in-place优化（commit 72548b093ee3）与authencesn越界写之间的致命交互。Brumley指出，这种跨子系统语义推理能力的突破表明“发现深层逻辑缺陷的成本可能已下降约一个数量级”。

#### *2.4.3 专项研究者经验持续积累与页缓存漏洞模式认知成熟*

人类研究者的领域专长构成AI分析的方向锚点。Theori研究员Taeyang Lee在kernelCTF（Kernel Capture The Flag）中勾勒出AF\_ALG攻击面图谱，据此形成关键假设：AF\_ALG与splice()的组合为无特权用户创建了直通内核加密子系统的路径。

安全社区对页缓存（Page Cache）漏洞模式的理解经历了十年成熟。2016年Dirty Cow（CVE-2016-5195）揭示通过竞态条件写时复制机制篡改页缓存的可能；2022年Dirty Pipe（CVE-2022-0847）展示通过管道缓冲区注入数据的路径。这两个漏洞积累了页缓存攻击的经验，使研究者能识别页缓存引用在加密子系统的异常。

#### *2.4.4 副作用主动暴露与攻击者经济学变化*

Copy Fail的三个构成要素——2011年AF\_ALG套接字引入、2017年algif\_aead的in-place优化、splice()零拷贝机制——历经近十年才被关联为攻击链。容器化与云原生架构的普及使这些接口调用频率上升，攻击面自然扩展。

更深层的驱动力来自攻击者经济学的结构性变化。云环境中，本地权限提升（Local Privilege Escalation，LPE）漏洞价值发生跃迁——页缓存在宿主机与容器间共享，一次篡改即可影响整个节点。Brumley将此形容为“足以换取一栋房子的级别”。与此同时，HackerOne旗下Internet Bug Bounty项目因AI工具带来的报告量激增于2026年3月暂停受理，反映发现端与修复端的失衡。这种激励结构的变迁推动了更多资源投向内核级逻辑缺陷的挖掘，促成了Copy Fail的发现。

### **2.5 原因五：披露方式的*...