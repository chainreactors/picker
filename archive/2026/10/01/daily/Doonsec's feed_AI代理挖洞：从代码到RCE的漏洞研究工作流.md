---
title: AI代理挖洞：从代码到RCE的漏洞研究工作流
url: https://mp.weixin.qq.com/s/ACcihEtNAyF5AaEI2HxQgg
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:47:57.980315
---

# AI代理挖洞：从代码到RCE的漏洞研究工作流

# AI代理挖洞：从代码到RCE的漏洞研究工作流

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MvBIuGh1pHdbC7BgT537ud8HCtqia1pvnKTEbDnyJpnsuNsbwVJnTIibIJxHFFibEUsOMqTiaicTNLyQBHvyZ8atH1l0ewiaD7WK2ic0/640?from=appmsg)
> **导语**：Quarkslab（库尔斯实验室）公开了一套自己搭的漏洞研究流水线，把AI代理塞进8个分阶段的环节里，用FreeRDP做靶子跑了一次。结果挖出两个高危漏洞，能链起来在客户端远程执行代码。整个过程4天，对手是一个被审计和模糊测试（Fuzzing）了多年、接近50万行C代码的RDP（远程桌面协议）客户端。

![Quarkslab漏洞研究工作流架构图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Ozthxk5wQq92BKPvPLtPC6crtcfN4Kraicqas3eaibzEI3v8KhTTLeicR6dHgJmnKBZ3IBC6FXZ8q5k99kge23TvlD3O5jMZzkzQ/640?from=appmsg "Quarkslab漏洞研究工作流架构图")

## 一、问题：研究者的时间才是瓶颈

安全研究员一天里大部分时间都在读代码。成千上万行里找那么几行关键的，真正的工作就那一瞬间——怀疑某个长度字段在这儿校验了但那儿没有、某个状态能进两次、某个循环信任了不该信任的值。这几秒的"灵光一闪"往往要花好几天才能走到那儿。

AI代理能在几分钟内横扫整个代码库，把散在不同文件里的函数串起来，跟踪调用关系。这速度是肉眼看代码拼不出来的。但这里有个真正的问题：跑出来的是真漏洞，还是一堆假阳性让你慢慢筛？

Quarkslab要解决的就是把这种原始算力变成一种方法。他们造了一个"代理框架"（agent harness）——说白了就是套在AI代理外面的一套管理系统，决定怎么调度工具、怎么组织上下文、怎么拆任务、用什么规矩。落到漏洞研究上，这套框架包括：

* 一个可查询的代码图谱
* 一个确定性的分析核心
* 一组专门读取分析结果的"镜头"
* 一条让代理按步骤走的流水线

流水线会提出攻击向量、追代码路径、写PoC（Proof of Concept，概念验证代码），每个关键节点都由人来把关。

Quarkslab明确说，这不是一键挖洞器，而是一套可以运行、可以审查、可以重跑的方法论。代理做苦力活，把发现串起来，把线索摆到研究员桌上；研究员负责验证、引导调查、决定哪条线值得继续追。

> **红队视角**：这套思路跟我自己平时挖洞很像——AI不是替代，是放大器。把"读代码"这种苦力活扔给机器，把"这一行不对劲"这种直觉活留给人。

文章会跟着流水线从第一次扫代码库到跑出能用的漏洞利用工具走一遍，全程贴在FreeRDP上跑的——一个大型开源RDP客户端，目标是在客户端上挖出两个能链起来远程执行代码的漏洞。

## 二、为什么要自己造轮子

Quarkslab先讲了个大背景。

2025年12月底，一个人单挑了墨西哥9个政府机构。不是团队，不是国家级行动。接下来的7周里，这个人输入了1088条指令，触发了5317条命令，分布在34个独立会话里。Claude Code（Anthropic的AI编程助手）处理了305台内部服务器约75%的实时漏洞利用，另一套基于GPT-4.1（OpenAI的大模型）的流水线读窃取来的数据、规划下一步。近2亿条记录流出去：报税数据、民事登记、患者档案、车辆登记、选民名册。

关键数字：每条指令大约对应5条命令。三个月前一个中国关联的APT（高级持续性威胁）组织活动里，这个比例更夸张，模型完成了80%到90%的战术工作。

对防御方来说，真正改变的不是攻击技术，而是一个攻击者能撑得起的工作量。墨西哥那次一个人干的活，以前需要好几个不同技能的人。

这种规模产出对防御方来说是另一种麻烦：产出多不等于有用。curl（一个广泛使用的命令行数据传输工具）维护者Daneil Stenberg的案例最有代表性——漏洞赏金计划收到的高质量漏洞占比从超过15%跌到5%以下，2025年提交的报告中大约五分之一是机器生成的噪音，每份报告都要志愿者团队花几小时甄别。最后这个计划被迫关闭。这些报告之所以贵，是因为它们看起来都像那么回事：引用真实函数、真实代码路径、描述攻击场景，调查后才能排除。

> **红队视角**：我见过太多次了。自动化扫洞工具最大的成本不是跑起来，是筛选结果。结果多了，研究员反而成了瓶颈。

结论很清楚：**瓶颈是研究员的注意力，不是系统能跑出多少条发现**。Quarkslab这套工作流的设计思路就是先大范围扫一遍，让机器花时间过滤和验证，最后才把活人请出来看。

## 三、市面上已有的方案，为什么都不够用

市面上有几套系统在解决类似问题：

* Google的Big Sleep（AI辅助漏洞研究）
* OpenAI的Aardvark（代码仓库的持续安全分析）
* DARPA的AIxCC（AI网络挑战赛）上的自主系统

效果都摆在那儿。Big Sleep在SQLite里翻出一个内存破坏漏洞（威胁方其实已经知道了），还在FFmpeg、ImageMagick等项目里报告了20个。Aardvark现在叫Codex Security，会从仓库构建威胁模型，针对模型测试每次提交都不一样，最后在沙箱里验证发现。AIxCC走的是另一条路，系统设计目标就是自主找洞+打补丁。

但这些都不是为Quarkslab要做的活儿设计的：

* **Aardvark**：盯的是你自己的仓库提交历史，自己代码用起来很顺手，但你审一个从没碰过的代码库时它帮不上忙
* **Big Sleep**：Google内部工具
* **AIxCC**：假设已经有模糊测试框架了，而且按"无人值守跑"打分。FreeRDP这种大型目标根本没有现成框架，Quarkslab也没打算无人值守跑

更深层的原因是：一个全自主决策的工具最后给你的就是结论和零碎证据。你要确认它说得对不对，还是得自己重做一遍——成本跟当初直接找这个洞差不多。curl维护者2025年干的就是这事儿，对象是陌生人交上来的报告。Quarkslab不想对自己工具的产出做这种事。

> **红队视角**：这就是为什么Cobalt Strike之类的C2（命令与控制）框架在红队里这么受欢迎——它们是工具不是答案。研究员要的是控制权，不是结论。

## 四、工作流全貌

Quarkslab的架构把两个性质不同的东西分开用：

* **大语言模型**：适合生成和探索假设，但输出不可复现
* **确定性核心**：可复现、可重复，但不会"举一反三"

所以系统分两层。确定性核心负责把代码索引成可查询的图谱、跑从攻击者控制的源到危险点的静态污染分析（Static Taint Analysis，跟踪不可信数据如何在代码里流动）、过一遍已知的CVE/CWE（Common Vulnerabilities and Exposures / Common Weakness Enumeration，公共漏洞和弱点枚举）模式以及针对目标的检查。上面的代理层负责形成假设、读核心吐出来的东西、判断什么是真的、推进到PoC。

**核心追求召回率（recall，能捞出来的都捞出来）而不是精确率（precision，捞出来的是不是都对）**。它故意过度产出，因为一条永远没生成的线索就再也找不回来了。代理层存在的目的就是让这种过度产出变得可控——它不是用来找洞的，是用来消化噪声的，让研究员只看到活下来的东西。

核心是可复现的。代理层不可复现，但也不需要可复现——需要的是可审计。

具体来说，流水线跑8个阶段：

| 阶段 | 干啥 |
| --- | --- |
| graph（图谱） | 把代码库索引成图 |
| recon（侦察） | 把结构变成攻击面 |
| slicing（切片） | 缩到一条假设——代理没法对整个仓库做推理 |
| analysis（分析） | 跑污染分析、模式匹配和其他镜头 |
| triage（分流） | 把结果分成真、模糊、噪声 |
| poc（验证脚本） | 试着让幸存者真的触发 |
| chain（组合） | 看两个弱原语能不能凑成一个强原语 |
| exploit（利用） | 把验证过的原语/链子变成可用的漏洞利用工具 |

![Quarkslab工作流8阶段示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6M5S6r9gOKptWHUjeCn7Af8xGxFSZRmezu61ic13vltsNM7RxIZ4Z5MEicK0P1kD1AeHLjhxyg6OwCpIX2zbdcHKvbKPfxIVCIKM/640?from=appmsg "Quarkslab工作流8阶段示意图")

研究员的活儿在阶段之间，不在阶段内部。这也意味着可以从任意阶段切入：端到端全跑一遍、跑完侦察阶段拿假设走别的路、或者自己手里有个发现扔进流水线让系统做分流和PoC。每个阶段都不假设上一阶段是系统跑的而不是人跑的。

> **红队视角**：这个阶段设计最狠的地方是"切片"——把整个仓库的推理压到一条假设上。任何AI在大型代码库里都容易上下文超载（Context Overload），切小是让它别走神的核心技巧。

## 五、FreeRDP实战

Quarkslab把流水线对准了FreeRDP（开源RDP客户端库）的commit `993499447`，没给任何额外信息——没历史CVE列表、没模糊测试语料库、没提示哪些子系统历史上出过问题。`git clone`，开干。

FreeRDP是大部分Linux RDP客户端的底座：Remmina、GNOME Connections、KRDC，Apache Guacamole的guacd的RDP支持也是它。同一个代码树也实现了服务端，GNOME Remote Desktop和KRDC就用它，所以两端共享的解析代码从两边都能摸到。Quarkslab审的是客户端——每个从网络来的字节都来自用户选择信任的服务器。

### 5.1 第一步：图谱、侦察、切片

Graph把目标代码索引成代理能查询的形式：这次跑出来13506个函数、3105个类型、31705条调用边，包括解析后的函数指针生成的合成边。

Graph不是让人整个读的，它的用处是缩视野。比如`libfreerdp/core/nego.c`处理RDP连接开头的协商交换。把这个文件解析出来，代理就有了它的定义、参数和跟代码库其余部分的关系。

基于此，可达性查询把一个暴露的入口点变成一个工作集：

```
$ sift graph reachable nego_recv --files
libfreerdp/core/nego.c
libfreerdp/core/tpdu.c
libfreerdp/core/tpkt.c
… 6 more
```

从`nego_recv`出发，工作集是9个文件。其他入口点更宽：`rdpgfx_recv_pdu`能到67个文件，`rdp_recv_pdu`能到65个。切片就是用这些关系把每次调查范围压小，让代理不用把整个仓库装进上下文也能推理。

侦察加一层暴露信息：把代码分组到组件里，估计攻击者控制的数据能多直接到达每个组件，输出威胁模型、障碍地图和有序的切片列表。

这次跑出来304个切片。下文要说的两个发现分别来自切片166（`libfreerdp/core/nego`）和切片109（`channels/urbdrc/client/data_transfer`）。纯靠机械排名，这俩都不会被早早选中。研究员把这个排名当地图看，不是当判决书。

![FreeRDP图谱片段](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NXyrHwlTVFJAib5xO6GMYZCZM0ibnqD4fOytynEKxjZRYVFnLpcF2Kt7VAoX4U0SVaUVW0fqPHDic4XMuibIYjicT7OZYwyDpf0k0A/640?from=appmsg "FreeRDP图谱片段")

### 5.2 第二步：分析

每个切片独立分析。确定性核心建一个更深的图、跑静态污染分析、应用配置好的镜头。污染分析跑两遍：第一遍用引擎已知的源和汇，第二遍在代理识别出目标特有的术语（比如FreeRDP的流操作、读宏、内存分配包装函数）之后再跑一遍。

切片166里引擎产出14个发现。两个凑在一起有意思：

```
f-007 攻击者控制的长度存入 nego->RoutingTokenLength
 ↕ ?
f-005 同一字段后来被当作 Stream_Write 的长度
```

引擎能确认两个端点的存在，但连不上`nego`对象整个生命周期里的关系。它把这两条分开报，没有自己编一条数据流边。这种含糊正是下一阶段要解决的。

切片109产出116个发现。两个指向USB重定向完成路径上的一个错误：即便没写入任何数据，错误返回时攻击者提供的`OutputBufferSize`还留在原地。客户端后来发送响应时把这个大小原样用出去，把堆分配里残留的字节泄出来了。

到这一步，两个切片合计产出130个发现，但这些还都是候选，不是确认的漏洞。这一阶段假阳性本来就该有，每个发现都还得单独验证。

### 5.3 第三步：分流与PoC

分流在分类前先把相关发现聚到一起。这次130个发现聚成36簇：20个真且可达、3个潜伏、3个混合、10个假阳性。

分类结果再动态检查一遍。流水线给每个候选搭一个小测试程序，接上FreeRDP，在ASan（AddressSanitizer，内存错误检测工具）下跑。这是决定一条看起来合理的静态发现到底是真能测量还是该扔的环节。

切片166里，分流把f-007和f-005重新捏到一起。f-007指向`nego_set_routing_token`，从网络数据派生的长度存进了`nego->RoutingTokenLength`。f-005后来接上同一字段，在`nego_send_negotiation_request`里被传给`Stream_Write`当长度参数。

连起来看是个候选路径，但还不算漏洞。`nego->RoutingTokenLength`有两种填充方式。第一种其实安全：协议里的长度字段把路由令牌限制在一个不会溢出目标缓冲的大小。PoC确认了这个边界，这条路被抛弃。

第二种从Server Redirection PDU（协议数据单元）进来。恶意服务器能提供`LoadBalanceInfo`，后面FreeRDP建立重定向连接时它被当成路由令牌再用一遍。这条路没有同样的长度限制。

Quarkslab用一台恶意服务器和一个插了ASan的FreeRDP客户端复现了它。服务器发了600字节的`LoadBalanceInfo`负载，包上cookie头变成615字节的路由令牌。到`Stream_Write`时，FreeRDP试图把这615字节拷进`nego_send_negotiation_request`创建的512字节分配：

```
==4514==ERROR: AddressSanitizer: heap-buffer-overflow
WRITE of size 615

#2 Stream_Write
#4 nego_send_negotiation_request libfreerdp/core/nego.c:1098
#9 rdp_client_redirect libfreerdp/core/connection.c:715

0x75e976227180 is located 0 bytes after 512-byte region
[0x75e976226f80,0x75e976227180) allocated by thread T2 here:

#1 Stream_New
#2 nego_send_negotiation_request libfreerdp/core/nego.c:1083
```

`rdp_client_redirect`这一帧确认了：溢出是通过服务器驱动的重定向路径触发的，不是测试程序直接调漏洞函数本身。

测试用的是`WITH_VERBOSE_WINPR_ASSERT=OFF`配置，Debian和Ubuntu的编译包都用这个。如果开着详细断言，边界检查会在越界写入到达`memcpy`前先中止客户端。

USB重定向那个发现走的是同样的验证流程。这次的候选原语是未初始化的堆内存泄漏。Quarkslab把ASan配置成用`0xcd`填充新分配的堆内存，FreeRDP发出去的PDU里出现了同样的模式：

```
[poc] heap pattern bytes (0xcd) in region [36..100): 64 / 64
```

只有扛过动态验证的发现才会被推进组合阶段。

![FreeRDP分析结果列表](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NaKRw3HZIxicgHA9J2GmKVpuFekaqzjvTug2PwtesUNkVguMAqU71BTAXaMHga2RAkYwesqjVdy8gEDJWw7G1JfKk3pGdqnHVY/640?from=appmsg "FreeRDP分析结果列表")

### 5.4 第四步：链式组合

链式阶段只对验证过的簇下手。协商那个洞给的是一次攻击者控制的、但是盲写的堆写入；USB重定向那个洞给的是堆内容可见。泄漏在会话建立后还能用，服务器重定向能逼客户端重连触发写入。这俩原语凑一起，远程代码执行的可能性就出来了，但还没真打出来。

### 5.5 第五步：漏洞利用

到利用阶段，代理和研究员的分工开始变化。前几个阶段产出的东西都很容易检查——一条路径、一个源码位置、一段ASan跟踪、一次测量。利用就没那么宽容了。举个例子，假设的堆布局猜错了，失败信息往往说不清为啥错的。

Quarkslab给利用阶段配了自己的框架，没让通用代理随便迭代。框架里塞了利用相关的知识，把过程拆成一组必须验证才能继续的关卡。

这样代理在有限任务上还能用：解释泄漏出来的字节、枚举写入能到达的对象、测试堆布局假设、给单次实验搭测试程序。同时过程可审查。一步成功意味着测出了一个预期属性，不是模型觉得"看起来对"就行。

但还是有边界。这次跑下来，代理自己没拼出完整的漏洞利用。Quarkslab在两个地方插了手：第一次是从泄漏推导libc（标准C库）基址，第二次是把两个原语组合成可用的payload（攻击载荷）。

漏洞利用走过这些关卡...