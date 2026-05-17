---
title: “分片失忆”——Dirty Frag补丁如何催生了Fragnesia漏洞
url: https://mp.weixin.qq.com/s/KO2L3ZRv43BXQMT0E5PSOQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:10.672997
---

# “分片失忆”——Dirty Frag补丁如何催生了Fragnesia漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkicu1ibY6PtFCVIMmmS5dU8ic44OyJSbkD4KVzVUAr4hTVvlVuibzibtkKYNKwNKngWyAnqxHOiaSwIT0q8a9IX9lh1BIJLibdGvIkeTM/0?wx_fmt=jpeg)

# “分片失忆”——Dirty Frag补丁如何催生了Fragnesia漏洞

安天研究院
安天研究院

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

摘要：Linux 内核近期爆发的 Fragnesia（“分片失忆”）漏洞，揭示了安全补丁可能激活历史代码缺陷的连锁风险。该漏洞因SKB 标记在分片合并过程中静默丢失而得名“分片失忆”：安天研究院研究人员提出了补丁衍生漏洞问题的研究框架，基于大模型的全面辅助，完成本报告编写。旨在深入剖析这一补丁衍生漏洞的技术根因与状态机演化机理，系统梳理同类历史缺陷案例，并针对漏洞挖掘、缺陷修补与补丁审核流程提出优化建议。报告强调：Fragnesia 事件给开发者与安全修复者很深的教益，但其不应导致补丁恐慌心理。其事件证明的是补丁修复机制需要在AI时代升级由传统路径检测进阶至全局状态机一致性校验。但必须明确的是，补丁修复是应对软件安全缺陷的最基础和必备的机制。

**01**

**引言**

## **1.1****事件回溯：从Dirty Frag到Fragnesia的****“漏洞连锁”**

2026年5月，Linux内核安全社区经历了一场罕见的连锁安全事件。5月4日，Kuan-TingChen向netdev邮件列表提交了基于shared-frag方法的修复补丁。该补丁引入SKBFL\_SHARED\_FRAG标记机制，意图在ESP输入路径中识别并阻断来自splice()的共享缓存页。5月7日，独立安全研究员Hyunwoo Kim（@v4bel）通过oss-security邮件列表公开披露了Dirty Frag漏洞——一个通过链式组合xfrm-ESP（CVE-2026-43284）与RxRPC（CVE-2026-43500）两个页缓存写入原语实现的本地权限提升（LPE）漏洞，影响Ubuntu 24.04.4、RHEL 10.1、openSUSE Tumbleweed、CentOS Stream 10、AlmaLinux 10、Fedora 44等全系列主流发行版。该漏洞的破坏性在于其确定性：无需竞态条件，不依赖内核版本差异，单原语即可覆盖setuid二进制文件的内存映像，CVSS评分高达7.8。Linux内核维护者在压力之下迅速响应，5月7日，xfrm子系统维护者Steffen Klassert引导该补丁合入netdev tree；5月8日，补丁（commit f4c50a4034e6）合入mainline。社区一度认为，Dirty Frag的攻击面已被彻底封堵。

然而，约5-6天后的5月13日，安全研究员William Bowling——Zellic公司Head of Assurance、V12 Security团队成员——向netdev邮件列表提交了Fragnesia的修复补丁（Message-ID: 20260513041635.1289541-1-vakzz@zellic.io），正式披露Fragnesia（CVE-2026-46300）。其利用路径直接源于Dirty Frag的修复补丁——SKBFL\_SHARED\_FRAG标记在skb\_try\_coalesce()的合并路径中丢失，导致修复后的内核反而开放了新的页缓存写入窗口。攻击者通过AES-GCM的密钥流异或（keystream XOR）实现逐字节精确写入，PoC成功覆盖/usr/bin/su的前192字节。该漏洞的CVSS评分同样高达7.8。从Dirty Frag到Fragnesia，间隔不是数月，而是短短约一周。这不是巧合，而是补丁衍生漏洞（Patch-Induced Vulnerability）的典型案例：一个旨在“治愈”漏洞的补丁，在特定条件下“催生”了新的攻击面。

## **1.2****演化悖论：安全补丁为何成为新漏洞的温床**

漏洞响应修复模型遵循“发现-修复-验证-关闭”的线性逻辑。然而，Fragnesia的事件轨迹呈现了一个非线性悖论：**修复行为本身改变了系统的状态空间，使得原本休眠的缺陷获得新的语义上下文，从而被“激活”为可利用漏洞**。这一悖论的可以视为一个状态机复杂性问题。状态机是固定状态基于触发条件和迁移规则的行为逻辑模型， Linux 内核整套资源、数据结构、网络缓冲区、协议流程共同构成的复杂的全局运行状态流转体系，因此其内核并非静态代码集合，而是动态演化的状态机网络。任何安全补丁——尤其是**引入新标记、新检查点、新分支路径的补丁****——****都会改变状态迁移规则**。若补丁设计者对状态机的全局拓扑缺乏完整认知，新引入的状态变量可能在某些迁移路径中“丢失”或“变异”，产生补丁设计者未预期的可达状态。Dirty Frag的修复补丁正是如此：它引入了一个二元标记SKBFL\_SHARED\_FRAG，假设该标记会随skb（socket buffer）在其全生命周期内正确传播。

然而，skb在内核网络栈中经历分配、克隆、合并、分片、释放等数十种操作，每种操作都可能改变其内部状态。补丁设计者验证了ESP输入路径的标记检查，却遗漏了skb\_try\_coalesce()合并路径中的标记传播——一个自2013年（commit cef401de7be8）即存在、13年间从未被触发的古老缺陷。Fragnesia补丁同时指向了两个Fixes标签：2013年的cef401de7be8和2026年的f4c50a4034e6，需要特别澄清的是：从技术真相来看，Fragnesia并非由Dirty Frag补丁“引入”新bug，而是Dirty Frag补丁添加了依赖SKBFL\_SHARED\_FRAG标记正确的代码路径，使得一个已有13年历史的coalescing bug首次变得可被利用。

## **1.3 “****分片失忆****”****：Fragnesia根因的精确比喻（skb分片合并中的标记丢失）**

**Fragnesia****是****William Bowling****基于****Fragment****（碎片、内核网络分片）和****nesia = Amnesia****（失忆、遗忘）两个词的拼接构造，因此本漏洞也被中译为“分片失忆”。**skb\_try\_coalesce()是内核中负责将两个相邻skb的分片区合并的函数，其设计目标是减少内存分配开销、提升网络吞吐量在Linux内核网络栈中，skb（socketbuffer）是网络数据包的核心载体。当数据包较大或经过零拷贝路径时，skb的数据区可能由多个分片（fragment，简称frag）组成，这些分片指向独立的内存页。这个记忆在ESP输入路径中被读取，若存在则强制触发COW（Copy-On-Write），阻止原地解密对共享页的篡改Dirty Frag修复补丁为skb引入了一个“记忆”——SKBFL\_SHARED\_FRAG标记，定义于include/linux/skbuff.h（SKBFL\_SHARED\_FRAG = BIT(1)），用于标识该skb包含来自用户态splice()的共享缓存页，然而，当两个skb经过skb\_try\_coalesce()合并时，这个“记忆”被选择性遗忘了。合并后的skb继承了合并前的数据内容，却丢失了共享页标记。于是，一个本应被标记为“危险”的缓存页，在合并后以“清白”身份进入ESP-in-TCP解密路径，接受AES-GCM的原地异或操作——**分片失忆，标记归零**，**攻击由此发生。**

**02**

治愈与**副作用****：补丁的****正反双重属****性**

## **2.1****Dirty****Frag修复的****关键****逻辑：SKBFL\_SHARED\_FRAG标记机制**

##

Dirty Frag的攻击核心在于：攻击者通过splice()将setuid二进制文件（如/usr/bin/su）的缓存页注入网络skb的分片区，随后skb进入xfrm-ESP或RxRPC解密路径，原地解密操作直接覆盖共享缓存页实现提权。为修复该漏洞，Kuan-Ting Chen提交的修复补丁（commit f4c50a4034e6），由Steffen Klassert等维护者审核后合入主线，该补丁采用了“标记-检查”策略。标记阶段：在splice()将缓存页注入skb分片区时，为skb设置SKBFL\_SHARED\_FRAG标记；传播阶段：假设该标记会随skb的克隆、引用、传递等操作正确传播；检查阶段：在ESP输入路径（esp\_input()→esp\_input\_done2()）中，检查skb是否携带该标记。若携带，则对涉及的原地解密操作强制触发skb\_cow\_data()进行私有复制，避免在共享frag上执行原地解密。这一策略在单一路径验证中看似完备：只要标记正确设置并在ESP路径前未被篡改，攻击者的共享页注入即被阻断。

## **2.2 修复的边界假设：标记会随skb全生命周期正确传播**

##

修复补丁隐含了三个边界假设，这些假设共同构成了“充分性幻觉”的基础。

**假设一：标记的持久性。**SKBFL\_SHARED\_FRAG作为skb私有标志的一部分，应在skb的所有操作中保持持久，直至skb释放。

**假设二：标记的遗传性。**当skb被克隆（skb\_clone()）、复制（skb\_copy()）或引用时，标记应被正确继承。

**假设三：标记的封闭性。**skb的分片区操作（如分片添加、删除、合并）不应导致标记丢失，除非操作显式清除了分片的共享属性。每一步迁移都可能涉及skb的重新分配、分片重组或标志位操作。

这三个假设在线性路径中成立，但在非线性状态迁移中失效。skb在内核网络栈中的生命周期并非简单的线性传递，而是经历复杂的图状状态迁移：网络中断接收→GRO（Generic Receive Offload）聚合→skb\_try\_coalesce()合并→协议栈处理（TCP/UDP）→ULP（Upper Layer Protocol）切换（如espintcp）→xfrm解密。

## **2.3****被忽视的角落：高性能合并路径中的标记静默丢失**

|
|  |

skb\_try\_coalesce()的合并路径，其核心功能是将两个相邻的skb（to和from）合并为一个，以减少分片数量、提升缓存局部性。skb\_try\_coalesce()是内核网络栈中的高频优化函数，位于net/core/skbuff.c。

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHk8x6UkvDe0RWSj5ujOn7dOVtH8OxBWcg1dNNbG8Wm4ppcqChE6SOfYh5YJkT9UNalGcnLdJiamyuICmdVEInIt1TMTxtLJ78vn8/640?wx_fmt=png&from=appmsg)

在Dirty Frag修复之前，这一行为无关紧要——网络栈中不存在需要跨skb传播的共享页标记。但修复补丁引入SKBFL\_SHARED\_FRAG后，skb\_try\_coalesce()的“标志位不传播”行为从“无害的设计选择”变成了“危险的标记丢失”。该函数自2013年引入以来，历经数十次优化迭代，但其核心逻辑始终未变：合并时复制分片指针，但不复制或合并源skb的标志位补丁设计者未同步审计skb\_try\_coalesce()的原因在于性能敏感路径的“修复免疫性”：该函数是每包处理的热路径（hot path），增加任何额外检查（如标志位传播）都会引入分支预测失败和内存访问延迟。开发者在修复Dirty Frag时，本能地回避了对热路径的修改，选择了在“足够安全”的ESP路径入口处增加检查点。

## **2.4 标记****“****失忆”：合并后SKBFL\_SHARED\_FRAG丢失的代码机理**

##

标记丢失的精确机理如下：设定场景为skb\_a由攻击者通过splice()注入并携带SKBFL\_SHARED\_FRAG标记，分片区包含/usr/bin/su的缓存页。skb\_b为正常网络数据包，无共享页标记，分片区为内核私有页。其合并过程如下：

1.TCP接收路径中，skb\_a和skb\_b因数据连续被送入skb\_try\_coalesce()；

2.函数将skb\_a和skb\_b的分片区合并为新的分片数组；

3.函数释放skb\_a和skb\_b的独立结构，返回合并后的skb\_merged；

4.skb\_merged未继承SKBFL\_SHARED\_FRAG——标记丢失；

5.合并后的skb\_merged进入TCP ULP切换路径，被标记为espintcp（ESP-in-TCP）；

6.skb\_merged进入xfrm ESP-in-TCP解密路径；

7.由于SKBFL\_SHARED\_FRAG已丢失，esp\_input\_done2()中的skb\_has\_shared\_frag()检查返回false；

8.AES-GCM原地解密执行，密钥流异或覆盖共享缓存页；

9./usr/bin/su的内存映像被篡改，下次执行时触发提权；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHkicwbdFtC77z5MlbojttvHxf9qLHKvweu7e3bejI2ozLMXcyYfvBibhnHJBw8686M6gnQF1uZZHb60S5U0iaVyV0ScE6GQJDLacqI/640?wx_fmt=png&from=appmsg)

图1 Fragnesia攻击链路：从splice()到权限提升

**其关键问题在于：**标记丢失不是“数据损坏”，而是语义断裂。缓存页仍然是共享的（\_refcount>1），但skb的元数据不再反映这一事实。内核的安全决策依赖于元数据而非物理内存状态，元数据的“失忆”直接导致安全策略的失效。正如William Bowling在Fragnesia补丁描述中指出的：skb\_try\_coalesce()在将分页frag从@from附加到@to时，如果@from设置了SKBFL\_SHARED\_FRAG标记，合并后的@to仍会保留原有的外部归属或页缓存关联分片，却无法继承共享页标记。标记静默丢失直接破坏了后续解密路径原地写入防护机制所依赖的内核不变量。

**03**

**古老缺陷的****“****激活”**

## **3.1 2013年的沉睡代码：skb\_try\_coalesce()标记传播缺陷的历史**

##

skb\_try\_coalesce()的标记传播缺陷并非新引入的代码错误，而是自2013年即存在的设计惯性。Fragnesia补丁中的Fixes标签明确指向两个commit：

Fixes: cef401de7be8 ("net: fix possible wrong checksum generation") ←2013年提交
Fixes: f4c50a4034e6 ("xfrm: esp: avoid in-place decrypt on shared skb frags")  ← Dirty Farg修补丁

2013年，Linux内核网络栈面临10GbE乃至40GbE网络接口的吞吐压力。skb\_try\_coalesce()的引入是为了解决高带宽场景下skb分片过多导致的缓存抖动和内存分配开销。其设计哲学是最小化元数据操作：仅复制分片指针，不复制标志位，不更新引用计数以外的任何状态 在当时的设计语境中，这一选择是合理的：-skb->shinfo->tx\_flags主要用于发送路径的硬件卸载标记（如VLAN、TSO、checksum offload），与接收路径的内存安全无关；-不存在“共享缓存页”的概念需要跨skb传播；-合并操作追求极致性能，任何额外的位操作都被视为不必要的开销。因此，skb\_try\_coalesce()的“标志位不传播”不是bug，而是设计假设——一个在当时完全成立、在13年后被Dirty Frag修复补丁推翻的设计假设。

## **3.2 为何13年间未被触发：无标记机制时的****“****无害性”**

##

一处潜伏长达13年的逻辑缺陷，之所以长期未爆发安全风险，原因是漏洞依赖的前置约束始终不存在。skb\_try\_coalesce()自2013年落地以来，始终遵循合并分片时只拷贝分片数据、不同步传递SKB标志位的固有逻辑。在内核未引入SKBFL\_SHARED\_FRAG安全标记的漫长周期里，网络栈无需跨skb流转共享页属性与安全元数据，仅frag数据合并即可满足业务与性能需求。此时标记不传播的行为只是普通的历史设计习惯，不存在安全危害。这个问题可类比为：一扇原本无需上锁的门，没有锁具、也无需上锁，“不能上锁”本身算不上缺陷；直到后续为安全防护加装门锁，才发现门体结构先天存在，无法适配锁具逻辑。Dirty Frag修复补丁引入SKBFL\_SHARED\_FRAG后，相当于给网络栈增设了共享页防护校验，而skb\_try\_coalesce()遗留的标志位不传播短板，立刻turned从无害设计变为致命缺陷，最终造成防护标记静默丢失、安全策略被绕过。

## **3.3 Dirty Frag补丁的****“****激活效应”**

##

新标记使古老缺陷首次成为攻击路径Fragnesia的悖论在于：修复补丁不是修补了缺陷，而是激活了缺陷。Dirty Frag修复补丁引入SKBFL\_SHARED\_FRAG标记，本意是增加安全状态机的维度。然而，这一新增维度与旧有代码路径（skb\_try\_coalesce()）发生了不兼容交互的状态机演化：新状态机中，skb\_try\_coalesce()成为未定义迁移（undefined transition）——补丁设计者未考虑该路径下标记应如何传播，旧代码也未处理新标记。结果，系统退回到旧状态机的默认行为（skb\_normal），绕过了新引入的安全检查。这种“激活效应”是补丁衍生漏洞的典型模式：新代码赋予旧缺陷新的语义上下文，使其从“不可达状态”跃迁至“可达且可利用状态”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHk8VjbCAzVox5gian9nHHdQdK7wJC5YdM1vzgAauPjiaGsbkqtGtG5WB9xRYMIccbpSZ...