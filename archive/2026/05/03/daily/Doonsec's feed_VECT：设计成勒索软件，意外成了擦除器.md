---
title: VECT：设计成勒索软件，意外成了擦除器
url: https://mp.weixin.qq.com/s/FcGo_5s616CrdrXSZj9wxQ
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:30:00.450602
---

# VECT：设计成勒索软件，意外成了擦除器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcVsJXOiaPjvTHrWUqKaK12YlTSEgqZRicV1G8jAp0J1al7ZcfUxEE6OLiavMFHoK4ZDBiaqxRvZicFH9EVE0uPgLscNRQW8gtBAQvY/0?wx_fmt=jpeg)

# VECT：设计成勒索软件，意外成了擦除器

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Check Point Research发现VECT 2.0勒索软件在加密大文件时存在致命缺陷：它用四个随机随机数加密四个块，但只保存最后一个，导致三个块永远无法解密。实际上，任何超过128KB的文件都会被永久破坏，赎金也救不回来。这个bug跨Windows、Linux、ESXi三个版本一模一样，而且从VECT首次亮相就存在，从未修复。VECT的加密模式宣传也是假的，多线程调度做得比业余选手还差。

## 核心发现

* Check Point Research发现VECT 2.0勒索软件对“大文件”不是加密，而是永久销毁。所有三个平台版本（Windows、Linux、ESXi）在加密实现上都有一个致命缺陷：对任何大于131072字节（128KB）的文件，会丢掉四个解密随机随机数中的三个。无论谁都没法完全恢复，包括攻击者自己。阈值只有128KB，这意味着几乎所有包含有意义数据的文件——企业资产如虚拟机磁盘、数据库、文档和备份——都会被擦除。CPR确认这个bug在所有公开的VECT版本中都存在。
* 公开报告中搞错了加密算法。VECT用的是原始ChaCha20-IETF（RFC 8439），没有认证，而不是好多威胁情报报告（以及VECT最初的广告）声称的ChaCha20-Poly1305 AEAD。没有Poly1305 MAC，没有完整性保护。
* 宣传的加密速度模式根本没实现。Linux和ESXi版本中的--fast、--medium、--secure选项会被解析但被默默忽略。无论操作员选什么，每次执行都使用相同的硬编码阈值。
* 三个平台，一个有缺陷的引擎：Windows、Linux和ESXi版本共享一个基于libsodium的相同加密设计，同样的文件大小阈值，同样的四块逻辑，同样的随机随机数处理缺陷——确认是同一个代码库移植到各个平台。
* 专业的外表，业余的执行：除了随机随机数bug，CPR还在所有版本中发现了多个额外的bug和设计失败，从自抵消的字符串混淆、永远无法到达的反分析代码，到反而降低加密性能的线程调度器。

## 背景

VECT勒索软件是一种勒索软件即服务（RaaS）程序，2025年12月首次出现在一个俄语网络犯罪论坛上。2026年1月宣称前两个受害者后，该团伙因为宣布与TeamPCP合作而再次进入公众视野——TeamPCP是2026年3月几次供应链攻击的幕后黑手。这些攻击将恶意软件注入到流行软件包如Trivy、Checkmarx的KICS、LiteLLM和Telnyx中，影响了一大堆下游用户。在这些攻击成为头条新闻后不久，VECT在BreachForums上发帖，宣布与TeamPCP合作，目标是利用那些受供应链攻击影响的公司。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcoAFnVUMnfQT2LF1sT8x9t4O3L4jCvoc7OFww8EqDF2ApLiack2ibcbCHVkhicOia1wDA5jqVuZGJkibRRBxjxWLB1ibNnpjrxleCxE/640?wx_fmt=png&from=appmsg)

▲ 图1：宣布与BreachForums和TeamPCP合作

此外，VECT还宣布与BreachForums本身合作，承诺每个注册论坛用户都会成为联盟会员，从而能够使用VECT勒索软件、谈判平台和泄露网站进行操作。传统上，大多数勒索软件团伙允许联盟会员通过信誉或支付费用加入。截至2026年4月，这一合作正在全面进行中：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfmBvm3WC9N7KrLnttWOldIB9IFqS0Ilgpop2WRVbhNzkRqv0lBWiahuCu8NLEibibxzHH2S2kC4gxicNqJ0Irax9ol4djupEt4GJU/640?wx_fmt=png&from=appmsg)

▲ 图2：BreachForums上的合作发布页面

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibduCMricRLroj3d0GXVib841WLLE01LVExlia8ArkKomc2u8UsFpMKLIzcmNhWbPO2xg5Yxk8xh7arlqD5jc89U6HPYBZWicGj1BcE/640?wx_fmt=png&from=appmsg)

▲ 图3：通过论坛私信向所有BreachForums成员分发访问密钥

虽然这些动作显示了一个雄心勃勃的项目，但该团伙当前的泄露网站只列出了两个受害者，都来自TeamPCP供应链攻击：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcsSMXib1z9KuwKo148icC4NWHJB1MGibj7iaiblibfWbkfEzhkOAo4nxNxFW9LF67ywrwibuXnTeOp26wXyqAGKjqMZZv8E78T8CfzaA/640?wx_fmt=png&from=appmsg)

▲ 图4：VECT暗网泄露网站

VECT勒索软件用C++编写，随着2026年2月发布2.0版本，VECT支持Windows和Linux主机以及ESXi虚拟机管理程序。该团伙声称所有三个锁定器都是从头构建的。另外，一个论坛帖子提到，专门的“云锁定器”（可能针对各种云存储服务）将很快提供给那些通过测试或谜题挑战证明自己能力的联盟会员。

## 前言：勒索软件分析概述

通过一个BreachForums账户，Check Point Research获得了面板和勒索软件构建器。在这里，联盟会员可以选择构建三种不同的有效载荷：Windows、Linux和ESXi（以及一个专门的数据外泄工具，但写本文时还不可用）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdDMhAspHa1IlsKsLeNIeHDxzWwmYudOZRZ9THjUtIqtWUicIHOVX4cGRdtFCZW2V0PKeIy2h3ZA9FoapDL0IlXxkBicEKFfaUEc/640?wx_fmt=png&from=appmsg)

▲ 图5：VECT构建器面板

Check Point Research分析了所有三种有效载荷，发现了各种缺陷和疏忽——暴露出在专业外表背后，VECT勒索软件并非技术复杂的服务。

## 勒索软件跨平台概述

如下各节所述，VECT 2.0通过三个不同的版本（基于共享代码库）针对Windows、Linux和VMware ESXi。虽然平台特定的破坏逻辑不同，但核心加密引擎在所有三个版本中完全相同——这个设计决策确保了下一节描述的缺陷平等地影响每个支持的平台。

所有三个版本都是静态编译的C++可执行文件，嵌入了libsodium加密库，接受操作员提供的命令行参数，支持横向移动，并产生相同的磁盘加密文件格式。下表总结了所有三个版本的关键属性。

| 属性 | Windows | Linux | ESXi |
| --- | --- | --- | --- |
| 架构 | PE64 (x86-64) | ELF64 (x86-64) | ELF64 (x86-64) |
| 工具链 | MinGW-w64 / C++ | GCC / C++ | GCC / C++ |
| 加密库 | libsodium (静态) | libsodium (静态) | libsodium (静态) |
| 加密算法 | ChaCha20-IETF (RFC 8439) | ChaCha20-IETF (RFC 8439) | ChaCha20-IETF (RFC 8439) |
| 密钥大小 | 32字节 | 32字节 | 32字节 |
| 随机随机数大小 | 12字节 | 12字节 | 12字节 |
| 小文件阈值 | 131,072字节 | 131,072字节 | 131,072字节 |
| 大文件块数 | 4 | 4 | 4 |
| 块偏移公式 | file\_size / 4 × index | file\_size / 4 × index | file\_size / 4 × index |
| 最大块大小 | 32,768字节 | 32,768字节 | 32,768字节 |
| 写入磁盘的随机随机数 | 1（仅最后一块） | 1（仅最后一块） | 1（仅最后一块） |
| 加密扩展名 | .vect | .vect | .vect |
| 赎金说明文件名 | !!!READ\_ME!!!.txt | !!!READ\_ME!!!.txt | !!!READ\_ME!!!.txt |
| 默认目标路径 | 所有驱动器 | / | /vmfs/volumes |
| 横向移动 | WMI / DCOM / SMB / SC / Schtasks / PSRemoting | SSH / SCP | SSH / SCP |
| 地理围栏 / CIS绕过 | 否 | 是（区域设置+时区） | 是（区域设置+时区） |
| 反调试 | 进程扫描+内核对象查询 | TracerPid检查 | TracerPid检查 |
| 加密模式标记 | 不适用 | 已解析，未实现 | 已解析，未实现 |

## 随机随机数缺陷——"大文件"毁灭

### 正确的加密识别

在描述缺陷之前，有必要纠正一下现有的公开报道。几份已发表的分析称VECT的加密是ChaCha20-Poly1305 AEAD。这是错误的——我们确认所有三个版本（Windows、Linux、ESXi）都使用原始的、未经认证的ChaCha20流密码的IETF变体（RFC 8439），通过libsodium的crypto\_stream\_chacha20\_ietf\_xor实现。\_ietf特指标准化的96位（12字节）随机随机数和32位计数器参数化，与Bernstein最初的64位随机随机数形式不同。

ChaCha20-Poly1305 AEAD构造会在每个密文后附加一个16字节的Poly1305认证标签。任何VECT加密的文件中都没有这样的标签。磁盘上的格式只包含原始密文后跟一个12字节的随机随机数——没有MAC，没有完整性保护，没有任何形式的认证加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibclwOVMvibMBia6dWQwrBAG7SOpbwLjdFaRLRd0xHUsjIWIt5qsoEEx1Mic9moicPP6Hvnaf5O2Cib81oXjqudNAxVecrRhFy2w7QEM/640?wx_fmt=png&from=appmsg)

▲ 图6：VECT的每块加密辅助函数——12字节随机随机数由randombytes()生成并直接传入crypto\_stream\_chacha20\_ietf\_xor

这种错误归因很可能源于研究人员相信了威胁行为者自己在最初论坛广告中的说法——VECT自己搞错了他们所用的加密方案名称。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdibpibRbOAHysE9fy9SZEYVjkcicmrxCHpuYJYibQGPSuLEK8ahc3bxEUpJ3uRJSOqFcRWyRbuUp4HgFicANtS5fdllO7zaHmtVTvQ/640?wx_fmt=png&from=appmsg)

▲ 图7：VECT最初的论坛广告——加密方案命名错误

### 概述

所有三个VECT 2.0版本都有一个关键的实现缺陷，导致任何大于131,072字节（128KB，甚至比一个简单的文档还小）的文件被永久且不可恢复地破坏，而不是被加密以便日后解密。恶意软件使用四个新生成的随机12字节随机随机数对每个“大文件”的四个独立块进行加密，但只将最后一个随机随机数附加到磁盘上的加密文件中。前三个随机随机数（每个都需要解密其对应的块）被生成、使用后默默丢弃。它们从未存储在磁盘上、注册表中，也没有传输给操作员。

因为ChaCha20-IETF需要32字节密钥和完全匹配的12字节随机随机数才能反转每个块，所以每个大文件的前四分之三块任何人（包括勒索软件操作员）都无法恢复——即使支付了赎金，操作员也无法提供可用的解密工具。由于绝大多数业务关键文件都超过这个“大文件”阈值，VECT 2.0在实践中就像一个披着勒索软件外衣的数据擦除器。

### 小文件处理

对于不超过131,072字节（128KB）的文件，整个内容被一次性加密。生成一个12字节随机随机数，用于就地加密整个文件，并附加到文件末尾。生成的磁盘布局是：

[ ChaCha20-IETF ciphertext - full file ][ nonce - 12 bytes ]

对于这类大小，格式内部一致，附加的随机随机数足以撤销单次加密传递。这些文件完全可以解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeSXSD7EqHE5dBZRCdIQ02dRiasuibQudRJ37dOE20Nyj9RffVZ9zYbsj4lXwlRSuDnMLnxLT0tibleKibibkMXfUsUdmNnbiciariagUs/640?wx_fmt=png&from=appmsg)

▲ 图8：小文件处理（单次ChaCha20-IEFT传递，12字节随机随机数附加在EOF）

### 大文件处理——缺陷所在

对于超过131,072字节（128KB）的文件，VECT将文件分成四个块，块偏移基于文件大小的四分之一：

* 四分之一大小：文件大小除以4
* 块起始偏移：文件的0、¼、½、¾位置
* 每个偏移处的块大小：最多32,768字节（32KB），如果剩余长度更短则取剩余长度

加密循环依次处理每个块。每次迭代都会调用每块加密辅助函数，每次调用都会通过libsodium的randombytes()生成一个新的加密随机12字节随机随机数，并将其写入调用者传递的同一个共享输出缓冲区。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibesfepuuiaZ5KibibJt8kAhzVYLacSnBiczUFhLiaiaGUlOzzYPWYB2SpUcT5uFGialJoKcUNKOjqPewfx4libibKFwJDgpDqhwnH1icDsqg/640?wx_fmt=png&from=appmsg)

▲ 图9：每块加密辅助函数

因为所有四次调用都接收到同一个缓冲区地址，每个新随机随机数都会覆盖前一个。循环完成后，缓冲区中只保留第四次/最后一块的随机随机数，这是唯一附加到文件中的随机随机数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdE3ahKibko6YibwJr3licJ1ZaLNnE4voGrnBUSpNG5gDFeNqAxsfmc8yx8D8iauGKyn9uKe8ic4up61NhFicpqicsUbJ96L5ycAr5D4k/640?wx_fmt=png&from=appmsg)

▲ 图10：大文件处理（4个块用4个唯一的随机随机数加密；只有一个随机随机数附加在EOF）

这三个被丢弃的随机随机数是randombytes()的输出（在Windows上内部解析为SystemFunction036 / RtlGenRandom，在advapi32.dll中，转发到bcryptprimitives.dll中的ProcessPrng；在Linux和ESXi上通过libsodium的safe\_read()从内核CSPRNG读取数据），是加密不可预测的值，在缓冲区被覆盖后从未存储在任何地方。在所有三个版本中，没有侧边文件，没有注册表项，也没有随机随机数材料的网络外泄。

### 跨平台确认

该缺陷在所有三个平台版本中结构相同。每种情况下，每块加密辅助函数每次调用都会生成一个新的随机随机数，并将其写入同一个调用者提供的12字节缓冲区；循环的所有四次迭代共享这个缓冲区；循环结束后向文件末尾写入单个12字节。

ESXi版本还在每次加密调用前执行零块检查，其中完全由零字节组成的块会被跳过（这是对稀疏VMDK文件的优化）。这不会影响随机随机数缺陷；共享缓冲区仍然会在每次非跳过调用时被覆盖，只有最后一个幸存的随机随机数到达磁盘。

该缺陷早于VECT 2.0。CPR对一个在2.0版本发布前已在野发现的较旧ESXi变体[1]的分析确认了相同的四块循环、四分之一偏移计算、共享随机随机数缓冲区和单个EOF随机随机数写入——从操作员首次公开观察到的部署到每个已知版本，从未改变。

### 影响

| 文件区域 | 磁盘上的随机随机数 | 可恢复性 |
| --- | --- | --- |
| 小文件 ≤ 128 KB – 全部内容 | 是 – 附加在EOF | 完全可恢复 |
| 大文件 – 偏移0处的块（最多32 KB） | 否 | 永久丢失 |
| 大文件 – 偏移¼处的块（最多32 KB） | 否 | 永久丢失 |
| 大文件 – 偏移½处的块（最多32 KB） | 否 | 永久丢失 |
| 大文件 – 偏移¾处的块（最多32 KB） | 是 – 附加在EOF | 仅最后一块 |
| 大文件 – 四个块之外的所有字节 | 不适用 – 未加密 | 明文，未变 |

通常超过128KB的文件几乎涵盖了一切：从典型的办公文档、电子表格和图像，到虚拟机磁盘映像、数据库文件、归档和备份——正是那些对业务连续性最关键、勒索软件操作员最常瞄准的文件。对于这类占主导地位的文件类别，VECT 2.0无法作为可恢复的勒索软件运作；它在操作上是一个数据擦除器。支付赎金的受害者无法得到针对他们最关键的文件的可用解密器——不是因为操作员不合作，而是因为解密所需的随机随机数已经不存在了。

## Windows锁定器

Windows版本针对本地、可移动和网络可访问的存储，将加密文件重命名为.vect扩展名，丢弃赎金说明和品牌桌面壁纸，并执行防御规避、持久化和横向移动例程。特别值得注意的是一个全面的反分析套件，针对44种特定的安全和调试工具，以及一个安全模式持久化机制和多种...