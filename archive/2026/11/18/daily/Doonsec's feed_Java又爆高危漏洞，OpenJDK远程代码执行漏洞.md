---
title: Java又爆高危漏洞，OpenJDK远程代码执行漏洞
url: https://mp.weixin.qq.com/s/VYxf_zSggXxIG4Al4KO9NQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:25.900068
---

# Java又爆高危漏洞，OpenJDK远程代码执行漏洞

# Java又爆高危漏洞，OpenJDK远程代码执行漏洞

原创

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 17 日，安全研究机构 Calif Research 公开披露了 OpenJDK 的一处内存破坏漏洞，编号 CVE-2026-114938，代号 Java4Shell。漏洞位于 HotSpot JIT 为 x86-64 平台手写汇编实现的 Base64 解码器 intrinsic 中。攻击者提交一段畸形 Base64 数据，即可触发堆内存越界写入，进而造成堆信息泄露，在部分应用上可实现未经认证的远程代码执行。

同一天，Oracle 与 OpenJDK 分别发布了安全更新。OpenJDK 将该漏洞列为 hotspot/compiler 组件问题，Oracle 在 11 月关键补丁更新中修复了 Java SE 8 至 27 的多条维护线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPprhhdgJaYibO86CPBZyUzjPm0q0aosCZ8fIeIZvibtwcdqp5BY78HL5Iu2CoF5WeEq2lemCZo0eMFFucGdx9r3sqw34omkz022k/640?wx_fmt=png&from=appmsg)

本文要点

01

漏洞概述

02

影响范围

03

POC 与 EXP

01

OVERVIEW

### 漏洞概述

Java 长期以来的卖点之一是内存安全——开发者不必操心指针与越界，JVM 负责内存管理。但这并不意味着 JVM 自身没有内存安全问题。HotSpot 的 JIT 编译器、垃圾回收器、intrinsic 大量使用 C、C++ 和汇编实现，这些底层代码不受 Java 沙箱保护。

Java4Shell 就出现在这里。为了让 Base64 解码跑得更快，HotSpot 把这个函数用 AVX-512 VBMI 指令（VMOVDQU8）重写成 intrinsic，一次能搬移 64 字节数据。这段手写汇编在处理输入末尾的填充字符时，算错了写入掩码。

触发输入简单到有点反直觉：64 个字母 A 加一个等号。

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=

较旧的 OpenJDK 17 版本因为进入该快路径的长度阈值更高，需要 128 个 A 加一个等号。

Java 层面最终会抛出 IllegalArgumentException 拒绝这个非法输入。但抛出异常时，堆内存已经被写坏了——拒绝得再快也来不及。

02

IMPACT

### 危害等级与影响范围

两个分数并存，指向同一个漏洞。

| 评分体系 | 分数 | 来源 |
| --- | --- | --- |
| CVSS 4.0 | 9.2 Critical | Calif Research（披露方） |
| CVSS 3.1 | 8.1 High | Oracle / OpenJDK 公告 |

Calif 尚未公布完整的 CVSS 4.0 向量字符串，因此两个数字目前无法逐项对齐比较。Oracle 采用 CVSS 3.1 评分，攻击复杂度被评估为 High。

漏洞的危害分为两层。

读——JavaBleed。越界写会破坏相邻堆对象的长度字段。攻击者让应用程序把堆内存内容原样吐回响应，这是 Java 版的 Heartbleed。堆里可能包含会话令牌、私钥、个人身份信息，这些都可能随响应泄露出去。

写——远程代码执行。通过覆写数组长度字段这一经典手法，固定值越界写可以升级为可控值的线性写，进而触及 HotSpot 的 Code Cache 与 JVM 钩子，实现任意代码执行。

Calif 在默认配置下完成了远程代码执行验证。

| 认证要求 | 产品 |
| --- | --- |
| 免认证 Pre-auth RCE | Keycloak、Atlassian Jira、Atlassian Confluence、JFrog Artifactory、Jenkins、PingFederate |
| 需认证 Post-auth RCE | Apache Kafka Broker、Apache Solr、Elasticsearch、Gerrit、Spinnaker |

研究团队还在基于 Apache Struts 与 Spring Boot 搭建的示例应用上复现了问题。

这份名单不是全部。认证流程、文件上传、令牌解析等日常功能都可能调用到脆弱的解码器，实际暴露面取决于应用自身有没有可到达的解码路径。

客户端侧也存在攻击场景。安全研究员 samczsun 贡献了一条客户端利用链：一个主动连接恶意 TLS 服务器的 Java 程序，即使它本身不对外提供任何服务，也可能被攻破。

03

PRECONDITIONS

### 利用条件

完整的利用链需要多个条件同时成立，缺一不可。

| 条件 | 说明 | 不满足时 |
| --- | --- | --- |
| 运行时版本 | 受影响的 OpenJDK 构建 | 不进入漏洞代码 |
| CPU 指令集 | x86-64 且支持 AVX-512 VBMI | 走不到该快路径 |
| 编译状态 | 解码热点已被 C2 编译到 intrinsic | 不触发漏洞分支 |
| 输入可控 | 攻击者数据能进入该解码器 | 无攻击面 |
| 畸形填充 | 末尾 = 导致长度计算为负 | 无越界写 |

漏洞代码与硬件绑定，要求 x86-64 架构且同时支持 avx512f、avx512bw、avx512vbmi、bmi2 四项指令集。ARM64 平台不受影响。

grep -m1 '^flags' /proc/cpuinfo | tr ' ' '\n' | grep -E '^(avx512f|avx512bw|avx512vbmi|bmi2)$'

四个标志必须齐全，缺一个就不受影响。受影响的主流 CPU 包括 Intel Xeon Ice Lake、Sapphire Rapids、Emerald Rapids、Granite Rapids，以及 AMD EPYC、Ryzen 的 Zen 4 及之后架构。

需要注意的是，云主机的实例规格可能被调整，同一台主机今天不受影响，扩容或换机型之后可能就落入受影响范围。

Datadog 在 OpenJDK 17.0.6 上的测试显示，三个解码器入口的行为并不相同。

| API | 是否进入漏洞路径 |
| --- | --- |
| Base64.getDecoder() | 是 |
| Base64.getUrlDecoder() | 是 |
| Base64.getMimeDecoder() | 否 |

Calif 明确表示不存在通用的一键 payload。每条利用链都需要单独找到：可到达的解码路径、堆上存活的 writer 对象、能回传数据的 reader、合适的堆布局，以及应用层面的具体动作。

因此从「能越界写」到「能跑代码」之间隔着相当一段工程量。Datadog 的评估：更容易实现的影响是拒绝服务。稳定 RCE 需要针对每个目标做定制。

网络条件也是变量。利用对时序敏感，Calif 自己在测试中通过在目标同区域租用 VM 来压低往返延迟。

04

PUBLIC EXPLOIT STATUS

### 是否存在公开的 POC 和 EXP

这是当前最受关注的问题，按公开程度区分如下。

| 项目 | 状态 | 说明 |
| --- | --- | --- |
| 漏洞触发 PoC | 已公开 | Calif 官方自包含 Java 程序，验证 62 字节越界写 |
| 利用原理与技术链 | 已公开 | 堆风水、writer/reader 原语、六阶段利用流程均有详细描述 |
| 具体产品武器化 EXP | 未公开 | 研究方称将留出升级时间后发布 |
| 通用 EXP | 不存在 | 每个目标需定制，不存在指哪打哪的 payload |
| 在野利用 | 未发现 | 截至发稿无任何机构或厂商报告实际攻击 |
| CISA KEV | 未收录 | 尚无在野利用证据；CISA 已发告警要求立即修补 |

PoC 本身是安全的。Calif 提供的触发程序把解码结果写入一个真实分配的 4096 字节数组，所有写入都落在数组内部。这段程序做的事情很单纯：先用合法数据反复解码，把 JIT 逼进那条脆弱的 intrinsic 快路径；再把目标数组填成 0x5a；然后解码畸形输入，检查缓冲区之后的 62 个字节有没有被改写。

import java.nio.charset.StandardCharsets; import java.util.Arrays; import java.util.Base64;  public final class Base64Trigger {     private static volatile int sink;      public static void main(String[] args) {         Base64.Decoder decoder = Base64.getDecoder();         byte[] valid = "A".repeat(64).getBytes(StandardCharsets.US\_ASCII);         byte[] malformed = ("A".repeat(64) + "=").getBytes(StandardCharsets.US\_ASCII);         byte[] target = new byte[4096];          // 把 JIT 逼进脆弱的 intrinsic 快路径         for (int i = 0; i < 200\_000; i++) {             sink += decoder.decode(valid, target);         }          Arrays.fill(target, (byte) 0x5a);         boolean rejected = false;         try {             decoder.decode(malformed, target);         } catch (IllegalArgumentException expected) {             rejected = true;         }          int changed = 0, first = -1, last = -1;         for (int i = 50; i < target.length; i++) {             if (target[i] != (byte) 0x5a) {                 changed++;                 if (first < 0) first = i;                 last = i;             }         }         System.out.printf("rejected=%s changed=%d first=%d last=%d%n",             rejected, changed, first, last);     } }

在受影响 JDK 上输出如下，异常照常抛出，越界写照常发生。

runtime=25.0.5.0.3+1-3-24.04.1-Ubuntu vm=OpenJDK 64-Bit Server VM rejected=true changed=62 first=50 last=111 REPRODUCED

下载提醒

漏洞公开后，GitHub 上出现了大量以 CVE 编号命名的仓库。截至发稿，这些仓库里是版本检测脚本和扫描器，不是利用代码。有研究机构提醒，高关注度漏洞披露后，假冒 PoC 仓库是常见的恶意软件传播方式。下载任何「exploit」前先读代码，在沙箱里跑。

05

ROOT CAUSE

### 漏洞原理

HotSpot 用 intrinsic 实现热点函数，用专用 CPU 指令替代通用编译代码。x86-64 的 Base64 intrinsic 使用 AVX-512 VBMI 指令，一次处理 64 字节。问题出在处理末尾填充的那几行。

这段汇编用 bzhiq 指令构造掩码，作用是保留低 n 位为 1、其余清零。关键缺陷在于：填充处理没有对减法结果做非负校验。

input\_mask := bzhiq(-1, input\_length) output\_len := (input\_length / 4) \* 3  // 处理填充 if input[input\_length - 1] == '=':     output\_len -= 1     input\_mask >>= 1     if input[input\_length - 2] == '=':         output\_len -= 1         input\_mask >>= 1  output\_mask := bzhiq(-1, output\_len)

当剩余输入是 =、==、X=、X==、XY=、=== 这几种形态时，初始 output\_len 已经是 0，处理填充再减 1 或减 2，得到 -1 或 -2。

bzhiq 只从最后一个操作数的低 8 位读取位计数。-1 的低字节是 255，-2 的低字节是 254，两者都超过 64 位操作数宽度，于是掩码保持全 1，也就是 output\_mask == -1u64。

| 项目 | 数值 |
| --- | --- |
| 输入 | 65 字节（64 个 A + 1 个 =） |
| Java 侧分配的缓冲区 | 50 字节 |
| 实际写入起点 | 偏移 48 |
| 实际写入长度 | 64 字节 |
| 越界写入量 | 62 字节 |

Datadog 的独立测试用的是 128 个 A 加等号，分配 98 字节缓冲区，同样越界写 62 字节。

越界写出来的 64 字节里，可控程度很有限。

| 字节位置 | 可控性 |
| --- | --- |
| 第 0 字节 | 完全可控 |
| 第 1 字节 | 可控 4 bit |
| 字节 2–47 | 不可控 |
| 字节 48–63 | 固定 0x9a |

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPqP1mqXXULswy6Pk8qICbVfVicb6P28KW0DEJGvnPKEYXes9DmxBRcCbDzNzTvjllBIzcxrdlHWvUmanoLcicQVichNXpL4pXbx40/640?wx_fmt=png&from=appmsg)

— 畸形输入从解码器到 62 字节越界写的完整路径

研究团队用的是 JavaScript 引擎漏洞利用中的经典技术——覆写数组长度字段。把被改写长度的数组称为 writer：长度一旦被撑大，它就会继续接受写入数据。如果在它后面放置另一个对象，就能用可控值破坏那个邻居，固定值越界写因此升级为可控值的线性写。再破坏第二个数组的长度，让它的内容随响应返回，就得到了 reader，也就是前面提到的 JavaBleed 堆泄露原语。

剩下的难点是让这些对象在堆上「恰到好处」地相邻。G1 垃圾回收器把堆划分为固定大小的 region，HotSpot 为每个线程分配私有 TLAB，不同请求线程的分配顺序不可控。团队采用的策略是经典的 Spray and Pray：用对象大小和 padding 把偏移固定在 region 内，喷洒多组 writer/reader 对作为候选邻居，命中失败就重试。

远程利用还要解决分配时机的控制问题。做法是把请求分两段发送：先发到触发关键分配的位置，等 TCP ACK 确保数据已经进入目标机器缓冲区，再发剩余部分。小包分片效果更好。

完整流程分六个阶段。

| 阶段 | 动作 |
| --- | --- |
| WARM | 用合法 Base64 反复解码，把 JIT 逼进脆弱的 intrinsic 快路径，此时无内存破坏 |
| REHEARSE | 可选的一轮校准 |
| TRIGGER | 发送畸形尾部，对象位置正确时固定溢出撑大 writer |
| DISCLOSE | 继续写入，将选定字节灌入 reader，从响应收集堆数据 |
| REPAIR | 用泄露到的原始数据恢复临时改坏的对象头和邻居，避免 JVM 崩溃 |
| FINISH | 执行应用层面的动作，用真实请求验证代码执行成功 |

一个常见误解

关闭 nginx 的 request buffering 不是通用缓解措施。Elasticsearch 的一条链是单个完整请求跑完整个流程，缓冲机制挡不住；WebSocket 升级后的帧走隧道，请求体缓冲那套也不适用。

06

MITIGATION

### 缓解措施

OpenJDK 安全通告与 Oracle 补丁已于 2026 年 11 月 17 日发布。

| 发行线 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| Java 17 | 17.0.6 及以上 | 17.0.21.1 (+4) |
| Java 21 | 修复前全部版本 | 21.0.13.1 (+4) |
| Java 25 | 修复前全部版本 | 25.0.5.1 (+4) |
| Java 27 | 修复前全部版本 | 27.0.1.1 (+4) |
| Java 8 | 8u511b33-perf | 8u513-perf |
| GraalVM | 17.0.21.0.3 / 21.0.13.0.3 | 17.0.21.1 / 21.0.13.1 |

OpenJDK 公告同时列出 8u514、11.0.33.1、17.0.21.1、21.0.13.1、25.0.5.1、27.0.1.1 为已修复版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPqrsC3shI1ibxZoDicW9xmtVFSUgiaZ66vkyNCuXQa9LVFpjyCyibWLP7ZRmcz8DTZsTlVKyHHeIQ7fuRRRVhw9aTibJkuibfYzdzCTA/640?wx_fmt=png&from=appmsg)

— 下游发行版修复版本与两个易错点

容器环境需要...