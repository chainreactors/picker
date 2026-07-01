---
title: 当大模型学会逆向拆解EDR，终端安全的天平正在倾斜
url: https://mp.weixin.qq.com/s/nxyq6nAc0hX9Wa9OWPmGhg
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:19:54.136707
---

# 当大模型学会逆向拆解EDR，终端安全的天平正在倾斜

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDro9p8jBZuNgALTkpdF7gCV9mo9Tplatn8MmWzIhhmEbj2IjA3KogqIt6hNPWibIshZjRzn0YQtqCs1jENjibdF3VhJef6HG1egk/0?wx_fmt=jpeg)

# 当大模型学会逆向拆解EDR，终端安全的天平正在倾斜

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在网络安全的攻防对抗里，终端侧的较量始终是最前线的战场。红队成员想在目标主机上站稳脚跟，首先要过的就是 EDR (终端检测与响应系统) 这一关。

过去想要找到 EDR 的检测盲区，研究人员需要熬夜调试内核、逐行拆解二进制文件，靠经验一点点摸索绕过方法，效率完全依赖个人技术积累。

而随着大语言模型能力的迭代，这套耗时耗力的玩法正在被彻底改写。安全厂商 SpecterOps 最新的研究证实，只需要一套极其简单的自动化框架，配合专用安全大模型，就能在无人值守的情况下完整逆向主流 EDR 的本地检测逻辑，提取规则、解密模型甚至直接给出可落地的绕过方案。这场由 LLM 驱动的终端对抗升级，正在把整个行业推向新的节点。

对很多安全研究员来说，拆解 EDR 引擎是个熟悉又磨人的工作。开一台开启内核调试的虚拟机，放着音乐熬几个晚上，才能从层层封装的代码里抠出几条检测规则，找到一个可用的绕过手法。遇到项目赶工期的时候，这种慢节奏的手工逆向经常让人头疼。LLM 的出现给这个场景带来了质变。当大模型具备调用逆向工具的能力之后，原本需要人一步步执行的分析、验证、总结工作，都可以交给模型循环迭代完成。

SpecterOps 团队基于这套思路做了一套分析框架，测试下来主流的五家 EDR 产品，其本地检测体系都能被完整拆解，规则、签名、检测模型都能离线提取出来。在逆向过程中团队还发现一个有意思的现象：很多规则都是专门针对业内常用的红队工具设计的，比如 MythicC2 框架的各类代理、SCCMHunter、甚至识别 BloodHound 采集行为的 LDAP 流量检测规则。他们还专门整理了一份清单，记录这些针对公开工具的检测签名。这次研究团队选择了 Palo Alto 的 Cortex XDR 作为演示样本，不是因为它的防护能力最弱，而是它的实现方式有不少有意思的设计，能更直观地展示 LLM 逆向的效果。需要说明的是，这套方法对所有主流 EDR 厂商都适用，研究团队内部已经完成了多家产品的规则提取。

很多人会以为能拆解 EDR 的自动化系统一定是复杂的多智能体架构，有专门的调度模块、分工明确的不同角色模型。但实际这套被称为 Day Shift 的分析框架，核心逻辑简单到超乎想象。研究团队使用的模型是 OpenAI 的 GPT-5.5-Cyber 安全专用大模型，运行在 Docker 容器内的 Codex-CLI 环境中，通过挂载的本地工作目录持久化数据。整个框架的核心只有四个 Markdown 文件，用来承载分析过程中的所有信息：

REPORT.md 用来汇总模型发现的关键结论，供人工复核

STATE.md 保存分析进度和关键事件，让每次重启的模型都能接上之前的工作

CODEMAP.md 记录逆向过程中发现的关键代码位置，加快后续迭代的分析速度

AGENTS.md 存放指令集，告诉模型分析目标和文件使用规范

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpwXRgD1KwOGmOd5bvCZpWQCf0m2IFHW0lWMoibichtbUKIIicLBVbiaEfhLtZEJjib78mfaZK0lKaV9c1XNmibejiahM05SNMuxtthRM/640?wx_fmt=png)

除此之外，团队还搭建了一个本地服务，通过 MCP 协议把逆向工具 Binary Ninja 的能力开放给大模型调用，让模型可以直接读取、分析二进制文件，标注函数和代码片段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpaxicgKe1ZkdvadNRiaj1qkASqnwYCow4DTyibUkMcCIqCRsqIeGStMbfAL534PE7PbA7PogyqWXUibVk5Ybgia9KzS5YYjBiaMIoJ0/640?wx_fmt=png)

最后启动整个流程的，只是一段带循环的 Shell 脚本。脚本会反复调用大模型执行分析任务，直到检测到停止文件才退出。之所以要用循环反复执行，是为了解决当前大模型的一个通病：面对开放式目标时很容易中途停止，明明还有很多信息没挖透就提前结束任务。每次循环重启都会清空模型的上下文窗口，让模型重新读取之前的分析记录继续推进，往往能发现上一轮漏掉的线索。不用复杂的多智能体调度，就靠一个循环，就能让模型持续工作，逐步挖出 EDR 的全部底层逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDopvdDV9RsDHg59ZTl0EqqWL5QlPDXN2aylWfFl3ZqcOLtLJQ4DpcLU8QdMQicPTqLB6RvYdDSkt2LnoCLd1b7UI2g4tjI4bK9k/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoeMiaV94MibW62XOCLAgIh5I6Nt2SVeVLia7BtkiaaUSPic0j0rs9XPTH7yYpuu0Zoy1jvNtlDGcA5cl3rnALwauQS1ia02xBCqsw4M/640?wx_fmt=png)

这套框架跑起来之后，Cortex XDR 的本地检测体系被逐层拆解，从最表层的进程注入Hook，到深层的规则引擎和机器学习模型，所有实现细节都被完整还原。

1. 进程内的Hook网络

绝大多数 EDR 都会往目标进程里注入用户态 DLL (动态链接库)，用来挂钩关键系统函数，监控进程内的可疑行为。Cortex XDR 对应的注入模块是 cyinjct.dll，它会在进程启动早期就给 LdrInitializeThunk、NtContinue 等多个关键函数安装内联Hook，作为后续所有检测功能的入口。LLM 不仅定位到了所有Hook的安装位置和对应函数，还直接给出了最高价值的绕过方向：比如通过重映射干净的 ntdll 文件、使用直接系统调用、手动映射 DLL 或者恢复被修改的函数开头，都可以绕过这层用户态拦截，不用逐个去对抗下游的检测功能。

2. 本地 YARA 规则库

除了云端的行为分析，很多 EDR 会在本地内置 YARA (恶意代码特征匹配引擎) 规则，用来快速匹配文件的静态特征，第一时间拦截已知恶意样本。

Cortex XDR 也不例外，它把 YARA 规则加密后存在本地磁盘上。LLM 很快就定位到了规则文件的存储位置，并且找出了加密所用的 AES-128-ECB 密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrib156DTALd0L5MkDbMdjZk1ttdRUiapF4eoBsblMMrohh3ntIPJh0dJEBShjsRicBcnUS4A6B1f4th9iaXIA448vlnbCKKD5TFD0/640?wx_fmt=png)

解密之后一共得到 6358 条 YARA 规则，每条都包含规则 ID、处置动作、威胁等级等完整信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrUIQUwQxxhNSJmicuYyVxFnf9uOYx5ic2DTqx65qSVpS4NnibIP7PicGtIRVQsQgZRm8mrFwCODGMOk9NNWGdH4kibfSXt3LGC631c/640?wx_fmt=png)

不仅如此，模型还自动写出了解密脚本，把所有规则分类整理成了独立的规则文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpgVXdFowEgmKicLIvQX89B6oibFDHHDHpeofUSxFWy7UnY0T1hXQaNtyrFxvTkicvHlY8P9fibJnr2ibNAw6kJe25eJGhsAIian2wCM/640?wx_fmt=png)

为了验证提取的规则是否有效，研究人员做了个简单测试：往一个正常的可执行文件末尾追加字符串github.com/MythicAgents，文件立刻就被 Cortex XDR 拦截，告警信息和提取的规则完全对应，证实了提取结果的准确性。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDogVugv8QSYm94L3D2ha396XWWR0AbIaJ3DxkJfArQiaAC5rgZaZibeP7yzxI0JGgN1YmwqQibcw4P7MtTFAbiaendpGPhoybR7Kj0/640?wx_fmt=png)

3. 行为检测规则

静态特征只是第一层防护，EDR 更核心的能力是行为检测，也就是通过程序的操作轨迹判断是否存在恶意行为。Cortex XDR 的行为检测体系基于 DSE 规则实现，其中包含 BIOC (行为感染指标) 规则。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqBvGe72DgnTeQZWvnmO58hO57K3S5QlWx6iaOaiaVQkwZwice7diaKUMUYvWt1l3D8I7UDSFvVWfn1oAzJSib4JicoUYMgvWra8YGVQ/640?wx_fmt=png)

LLM 通过本地的明文配置文件和日志，还原出了整套行为检测的覆盖范围：主机上默认搭载 9350 条 DSE 规则，其中包含 4209 条 BIOC 规则；加上本地动态禁用的 494 条规则，实际生效的是 8856 条 DSE 规则和 3989 条 BIOC 规则。这些规则里包含大量针对命令行的正则匹配，比如检测通过 cmd 执行 powershell 下载、导出 ntds.dit、临时目录执行脚本等常见攻击动作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqoAyQDZtMqwxXXTdt39DNJWhGpUVjMwhPp56SRYsZsgbrYc2qwfe5UhSzCd1b0mL96Fevry24ZsVXjXqzKe8SKmwxFf8icibdJY/640?wx_fmt=png)

研究人员按照提取的规则构造命令测试，确实触发了对应的拦截告警，验证了规则的真实性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqbzDMkKaB4kKdIV7IfiaWsicvwlVgic1zS6asy0NsAiaDpDvcFP5rfQcY2QoB4N6smVKsjjXWNzDw4FvNjicz7EcNs8ibph37fR1wJw/640?wx_fmt=png)

4. 本地机器学习检测模型

现在很多 EDR 都会加入机器学习模型来辅助检测未知威胁，Cortex XDR 也在本地内置了多套检测模型。LLM 分析后发现，这些模型并不是很多人以为的神经网络，而是典型的决策树集成模型，通过提取样本的特征计算分值，再用 sigmoid 函数输出最终的恶意概率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqiaQLcVMlBHZG4funS68fpvE4xhbBL83foCNYibBjwxZo2iaAKqk8mooAd9qKJyYTLFic4XiapX8KvchTggNc6Tiblc1hSo6SaGjqmE/640?wx_fmt=png)

不同类型的文件对应不同的模型和特征集：

PE 文件模型有 22977 个特征，阈值 0.88

PowerShell 脚本模型有 26142 个特征，阈值 0.65

VBS 脚本模型有 707 个特征，阈值 0.27

JS 脚本模型有 9355 个特征，阈值 0.75

更值得注意的是，LLM 不仅还原了模型的工作原理，还直接写出了可以本地运行的测试工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDo1skY6mpbKRUzAV0VrkRZpGGnCyZQhGbcryInZOLWQzF07SwQe7DZuJ2BuMZpRZTV8SyDYr7tqsqO8ljibRuONAkfWdttMjoQs/640?wx_fmt=png)

这个工具可以加载官方的模型文件，给任意样本计算恶意分值。测试显示正常的计算器程序得分只有 0.003，而恶意驱动文件得分高达 0.987，和官方检测结果完全一致。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpAn5DdEk8XpgJRCIy7GPUVSsvlkkKXv5VMI5333Zkh1A3uib14xwFr8wJvfN3FkhNagHEyeIgs9JrNO9ibEichWk8RlCPiaj60haY/640?wx_fmt=png)

对攻击者来说，知道了模型是决策树结构，就意味着不用盲目修改文件字节，而是针对性地调整特征就能绕过检测，效率会高很多。

5. CLP 规则引擎：最意外的发现

在所有分析结果里，CLP 规则的解密是最让人意外的收获。Cortex XDR 使用了一套基于 CLIPS 语言的规则引擎，CLIPS 是一种衍生自 LISP 的规则编程语言，在安全产品里非常少见。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoclv2TZbvmnibXbKotg6Ipk2KwsOjAicpxuchULZqMttcSxbH3TNLdibVHvUgqWibV4AnEZfwE0WrEkW6V9sic56dphV3UsxHEJmeU/640?wx_fmt=png)

研究人员也是第一次在 EDR 里见到这种实现，甚至专门买了教材来研究这套规则体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrqIkKel5G7RwibyNlSdN3Y0SWckvkMNbojP3ia8GSkJdjOdTloIVphTE56fFib9VvRJMb0ibp1NgjQWpGERFGMctIYuhCkh3iacIgc/640?wx_fmt=png)

这些规则被加密成.clp 格式的二进制文件存储在本地。LLM 完整还原了这套文件的解密流程：

从 cysvc.dll 里提取 64 字节的内置密钥

从配置文件里读取派生参数

按照官方逻辑派生 AES-256-CBC 的密钥和初始向量

解密文件后去除 PKCS#7 填充

解压 gzip 数据流得到明文 CLIPS 规则

解密之后，整套行为判定的逻辑完全暴露在眼前，里面不仅有各种检测规则，还包含了大量白名单逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoJg1N4PzBp1wDtucjXmNwcCBAS2WiaytUgtow1FvMoPnvF2hSicbY4dRjaj4kico7CV986yb6pjARuG6mFjcXM15Ft9ZxylDoRfg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrPFBwgONcQaaS3Z5BUic5NNCGNCo5zNzap4Hian96nY6LdHzFCUxc6vey6vUY88aVy36Z0yj5LnjOibSvCEicicujYmYexff7OicW9E/640?wx_fmt=png)

研究人员在规则里发现了一条针对注册表导出的白名单：当执行 reg save HKLM\SAM 命令导出 SAM 注册表蜂巢文件时，如果目标路径是 C:\rcoc\sam.hive，就会被放行。实际测试也证实了这一点：普通路径下执行 reg save 导出 SAM 会被直接拦截，换成白名单路径之后，操作可以顺利完成，没有任何本地告警。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpDkFLlMib29dskAzuKC9QF86icX7qniavgUjMEzaTExlZ4Hh3hjuzE98DlRAN1qdxcbRANnYmQ9lUs9TYmRmSdVs8xgNR8LocKHk/640?wx_fmt=png)

这种精准的白名单绕过，靠手工逆向往往需要很久才能发现，而 LLM 只需要跑完解密和规则分析就能直接定位。

接下来就是用 LLM 搭建虚拟攻防靶场，自动生成绕过。

提取规则只是第一步，SpecterOps 团队还在尝试更激进的玩法：用 LLM 模拟完整的终端环境和 EDR 检测逻辑，打造一个虚拟的攻防测试平台，自动生成并验证绕过方案。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDohMh2bEibFtk6j3SbVqkWx5Emp08g2eQZAm3FJIvBIHvxGtsfbpbTTH5JxfSToJobRMRnNRNgibayiadLUqm4bqzRoViaicsypeDmA/640?wx_fmt=png)

这套被称为 Upside Down 的框架里有两个核心子智能体：一个负责模拟 Windows 系统的运行环境，处理 API 调用和进程逻辑；另一个负责加载提取出来的 EDR 规则，模拟检测逻辑判定动作是否触发告警。在这个虚拟环境里，你可以像在真实主机上一样输入命令，系统会模拟执行流程，同时同步判断会不会被 EDR 检测到。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpAuUdrMDH9VrTTsQKqjS4Hcicy6jVLTQdT09dk97E1434QRevUicl7DZfR174a5icwnZf1xdwYEalR8wmtKe8bDR7bEnibRgzg7SY/640?wx_fmt=png)

测试中输入导出 SAM 的命令，模拟器立刻识别出对应的 BIOC 检测规则，判定动作会被拦截，同时还给出了绕过思路的分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDriaxZtqyj8CWmRkc4dRHb9Vy3pufYn3pIhs...