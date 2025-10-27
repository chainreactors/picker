---
title: ATT&CK实践进入深水区 ---不要再迷信ATT&CK覆盖率
url: https://mp.weixin.qq.com/s?__biz=MzUzMDk0MjY2NQ==&mid=2247484282&idx=1&sn=62aa133d5a186f3555d7ee49d52483e2&chksm=fa4b5cdccd3cd5cab0d6f99804bdf9a5541a2b3cc70d475dd210fc810e13785a9ad25e2c52fb&scene=58&subscene=0#rd
source: 安全喷子
date: 2024-12-27
fetch_date: 2025-10-06T19:37:45.808543
---

# ATT&CK实践进入深水区 ---不要再迷信ATT&CK覆盖率

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcq1ibph8acEcVkZM0dtxib6ZiaPWtibPjkrrgKoVaearWjWaHe7SKMY3WZQ/0?wx_fmt=jpeg)

# ATT&CK实践进入深水区 ---不要再迷信ATT&CK覆盖率

原创

程度

安全喷子

**引言**

ATT&CK除了版本更新的常规内容外，研究机构、学术界和产业界都有更深入的实践，检测方面的内容有了更多深入的实践和检验，从实际情况“祛魅”了ATT&CK覆盖率这个数字。除了检测工程之外，在威胁预测和威胁情报方面也有亮眼的进展。ATT&CK更像是一个“活框架”，它的源头是各种威胁情报和攻击方法的更新，比如勒索软件的猖獗；也有科技进展带来新的威胁也是ATT&CK可以覆盖的方向，比如ATT&CK的矩阵也扩展到AI安全领域、汽车安全、无人机和卫星安全领域。

**ATT&CK在检测工程中的应用**

**CISA关于云安全和紫队测试的实践**

紫队测试的基本原理，遵循"知己知彼"的战略思想，结合两个关键方面："了解敌人"：模拟攻击者工具、战术和程序，获取可观察数据；"了解自己"：开发和测试检测机制，识别技术差距和局限性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzML4ZZXcLVPopic0mb8BFkraRyeNvTPBicOVTibURHPuBHJibiamJtleEHyKAA/640?wx_fmt=png&from=appmsg)

图1  紫队的定义

**紫队的意义在于大多数攻击者缺乏原创性，主要使用：**

1.N-day CVEs（已知漏洞）

2.漏洞利用概念验证(POC)

3."安全审计"工具

**防御者需要避免自满：**

1.可能缺失关键取证数据

2.SIEM和分析模型可能过度调优

3.EDR/MSSP性能可能存在差异

**根据云环境安全事件案例分析**

1.Storm-0558 (2023年案例)

（1） 利用了多种技术：私钥窃取、Web凭证伪造、云账户访问等

（2）展示了复杂的攻击链条

2.NOBELIUM (2024年案例)

（1）使用密码喷洒、云账户访问、应用程序访问令牌等技术

（2）影响到联邦机构系统

紫队的知识来源于ATT&CK（红队）和D2FEND（蓝队）的相关内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLsXleBGric3jiawquPo3dar1ziaNfQ9gJ4V0z9sVQtTBS26IsQCTTVXHGw/640?wx_fmt=png&from=appmsg)

图2  紫队的工作过程

**紫队测试流程详解**

1.ATT&CK计划制定

（1）利用威胁情报和案例研究

（2） 构建红队行动手册

2.模拟环境要求

（1） 网络基础设施

（2）用户角色设置

（3）应用和服务配置

3.取证需求确定

（1）主机级别日志

（2）网络级别数据

（3）应用程序日志

4.对抗性模拟

（1）红队执行技术

（2）跟踪IOC和C2活动

5.蓝队响应

（1）使用现有工具和流程进行威胁狩猎

（2）追踪发现和检测方法

6.紫队测试

（1） ATT&CK覆盖分析

（2）识别已采取/遗漏的D3FEND防御措施

（3）基于完整取证和红队活动知识开发检测机制

（4）识别额外的防御措施

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLq9ntRic8iczuX7DTtlap1ax5icSKdV5RpGMyDB9ftJAeOsaQQJMbXD0ng/640?wx_fmt=png&from=appmsg)

图3  紫队的完整工作流程

**ATT&CK在Linux勒索软件中的应用**

Cisco Talos的安全研究人员关于Akira Linux变体勒索软件的分析报告中说明了Linux勒索软件的现状：

* Linux在关键系统中的普及

* 向混合云和云环境的转移

* 针对虚拟化平台
* 可能存在较弱的防御
* 双重勒索方式的增加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLbQaIQkLLDrcA5XIyJBprRkzJeZPS80okT6yMr9oHbz9pWgL4dudGPQ/640?wx_fmt=png&from=appmsg) 图4  Linux 勒索软件全景

**1.Akira版本演进**

（1）Akira\_v2:

* 专门针对ESXi的加密器
* 使用Rust语言编写
* 文件扩展名为".akiranew"
* 改进了命令行参数功能
* 使用rust-crypto 0.2.36库进行加密

（2）Akira\_v1:

* 使用C++编写，使用Crypto++库进行加密
* 基本功能较简单
* 文件扩展名为".akira"
* 可能是从Windows版本移植

**2.分析Akira勒索软件使用的多个ATT&CK技术编号**

（1）初始访问：

* T1078 (有效账户)
* T1190 (利用面向公众的应用程序)

（2）执行：

* T1569.002 (服务执行)
* T1059.001 (命令和脚本解释器：PowerShell)

（3）持久性：

* T1547.001 (注册表运行键/启动文件夹)

（4）权限提升：

* T1548.002 (滥用提权控制机制：绕过用户账户控制)

（5）防御规避：

* T1562.001 (削弱防御：禁用或修改工具)
* T1222 (文件和目录权限修改)

（6）横向移动：

* T1021.002 (SMB/Windows管理共享)
* T1021.001 (远程服务：远程桌面协议)

（7）收集与渗出：

* T1560.001 (归档收集的数据：通过工具归档)
* T1567.002 (通过Web服务渗出：渗出到云存储)

通过威胁追踪到检测工程完成对Linux下勒索软件的检测，首先通过ATT&CK框架，研究人员能够系统地记录和分析Akira的攻击链路；映射攻击者的战术技术和程序(TTPs)；跟踪威胁演变过程。然后从事件响应到威胁情报，再到检测工程的工作流程，这与ATT&CK框架的应用理念相符，有助于建立基于ATT&CK的检测策略；评估防御覆盖范围；识别防御差距。

**ATT&CK在各个产品的覆盖率**

这是一篇2024年USENIX Security 的一篇文章《How does Endpoint Detection use the MITRE ATT&CK Framework?》，主要探讨了端点检测产品如何整合和使用MITRE ATT&CK框架。研究人员分析了Carbon Black、Splunk和Elastic等端点检测产品如何使用ATT&CK框架。围绕3个主要问题:产品如何使用ATT&CK、为什么不能检测所有ATT&CK技术、产品间应用ATT&CK检测的一致性如何。技术覆盖范围并没有告诉我们可以检测到多少程序级威胁，ATT&CK 90% 覆盖率 == 90% ATT&CK 技术至少有 1 个检测规则。

主要发现：

**1.产品使用ATT&CK的情况:**

（1）产品优先考虑类似的战术和技术

（2）即使把所有产品结合起来,也无法实现100%的技术覆盖率

（3）厂商经常宣传高覆盖率,但这可能给人虚假的安全感

（4）过滤掉低、中严重性/风险规则，Splunk和Elastic的 ATT&CK 技术和覆盖范围均减半

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLjkhyYh5o7TiaEVVRowTzjJ4ZnmsfO0RKfD8AFo8ARso1aE6E6j5Hxfg/640?wx_fmt=png&from=appmsg)

图5  ATT&CK在各个产品的覆盖率和所有产品合并的覆盖率

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLWcwicibY5fLbHmfm4bruu1CAXSWN8h94VYSu2m1siadJe2VpS7T13CufA/640?wx_fmt=png&from=appmsg)

图6  过滤低、中严重性/风险规则的各产品ATT&CK覆盖率

**2.无法全面检测的原因:**

（1）某些技术本质上很难检测

（2）约53种技术未在任何商业产品中实现

（3）主要障碍包括:检测方法无效(39.6%)、针对非主机基础设施(24.5%)、需要客户特定知识(17%)等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzML5QS5zGO1mdWb6NWjoRG80kv6Tvk3Rjzn5aicoZl4YYGH5nic6l0HfeSQ/640?wx_fmt=png&from=appmsg)图7  安全产品的ATT&CK规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLw1ahJliaibDTGtttLVreDs7awvTMfshWjG4ffElw9AV1gicDgibVbTFhNQ/640?wx_fmt=png&from=appmsg)

图8  ATT&CK攻击技术无法检测的原因

**3.产品间的一致性问题:**

（1）即使检测相同的威胁,产品很少使用相同的ATT&CK技术来描述

（2）ATT&CK本身的模糊性和重叠导致了分歧

（3）不同产品可能将相同的系统日志活动归因于完全不同的战术动机

下图可以解释可能得分歧情况，展示了一个与 Meterpreter（一种攻击工具）相关的命名管道模拟行为，具体命令是：cmd.exe /c echo 4 sgryt3436 > \\.\ pipe \5 erg53

Elastic 的检测规则：将其归类为 T1134 (Access Token Manipulation)

Splunk 的检测规则：将同样的行为归类为T1059 (Command and Scripting Interpreter)和T1543 (Create or Modify System Process)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLcz8WBOfb5NElXZHC4mQoCd4A1SxlsicUIJGfpmkL5icVBkFiahiac3haeA/640?wx_fmt=png&from=appmsg)

图9  Elastic和Splunk的归类分歧

**ATT&CK在预测方面的应用**

MITRE的威胁通告防御中心（Center for Threat-Informed Defense）机构为了使用ATT&CK框架可以全面了解攻击者，开发了攻击技术推理引擎 (TIE) ，这个引擎根据一组观察到的技术推断攻击者可能使用的技术。网络防御者可以使用这些数据来确定威胁搜寻特定技术的优先级，事件响应者可以使用这些信息来突出显示对于威胁驱逐和恢复至关重要的重要横向移动和持久行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLOhWvnicOkKgCiaiaPePEEjlRcCEl3AA9oMNvT6ncroS96gdvDPuagfIUQ/640?wx_fmt=png&from=appmsg)

图10  TIE的产品界面：以钓鱼技术为例，预测后续可能得攻击技术

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLgv0l8mONgkybe6u8FKPe7gUkz7ZBwAZPianXa13UtrdicmGMaNU3dDjg/640?wx_fmt=png&from=appmsg)

图11  TIE导出的结果通过Navigator可视化

**1. 技术原理**

TIE是一种基于机器学习模型的工具，它通过训练在网络威胁情报上，推荐可能的TTPs（战术、技术和程序）基于已知的输入TTP。这种技术能够帮助分析人员快速理解在已知TTP之后可能发生的情况，基于广泛的威胁情报语料库。

**2. 应用场景**

（1）优先级排序：在网络紧急响应事件中，TIE可以帮助确定首先寻找哪些技术。

（2）事后分析：通过突出潜在的感知、检测和报告缺口，改善事后事件分析。

（3）攻击向量建议：作为网络保证的一部分，建议类似或相关的攻击向量。

（4）攻击者仿真计划：帮助创建攻击者仿真计划，以提高防御能力。

**3. 优势**

（1）提高效率：TIE通过减少分析人员在随机性上的时间投入，而将注意力集中在可能的入侵方法上，从而提高调查效率。

（2）适应性：随着新活动的检测，TIE的模型可以被重新训练以适应新的或以前未见过的攻击者TTPs。

（3）未知活动发现：TIE旨在协助安全团队发现基于观察到的攻击者活动的以前未知的攻击者活动。

4.与传统安全分析的比较

TIE与传统安全分析相比，更侧重于使用机器学习技术来预测和识别潜在的威胁行为序列，而不是仅仅依赖于已知的攻击模式和签名。这种方法可以更有效地适应不断变化的威胁环境，并能够识别出新的或未知的攻击行为。

**ATT&CK在痛苦金字塔的应用**

攀登金字塔（Summiting the Pyramid）是一个研究项目，来源于痛苦金字塔，专注于工程网络分析，使对手的规避更加困难。该项目由 MITRE 威胁通告防御中心创建和维护，推动全球威胁知情防御的技术水平和实践水平。

金字塔的前四层专注于短暂的值，对手很容易改变这些值。下一个级别的重点是对手在攻击期间尝试使用的工具类型。最后，顶层重点关注对手在攻击期间表现出的行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLSMIfibfQ6MgOChV7g03Yrmu4np5DTxpuaZ0KG5TsTlLBibThhLhtDwJQ/640?wx_fmt=png&from=appmsg)

图12  痛苦金字塔和攀登金字塔的的联系

威胁检测规则的质量评估结果，采用了分层的StP(Summiting the Pyramid)框架：

**1.分层结构（从上到下）：**

（1）StP 5 (年级别): 能检测大多数子技术攻击

（2）StP 4 (月级别): 能检测部分攻击程序

（3）StP 3 (周级别): 能检测一些内部工具滥用

（4）StP 2 (天级别): 能检测常见恶意软件和黑客工具

（5）StP 1 (分钟级别): 容易被绕过的检测规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLicA7AcN0MakvXXwERibqUr6LraJd0VxJYS8LTmKQFANzVO9n7qIfB6qg/640?wx_fmt=png&from=appmsg)

图13  攻击者绕过时间示意图

**2.整体评估：**

（1）平均StP评分：1.63/5分

（2）大多数规则(849个)属于最低级别(StP 1&0)

（3）高质量的规则(StP 5)数量最少，仅8个

这个数据说明当前的检测规则质量普遍较低，大部分规则容易被绕过，而高质量、持久有效的检测规则较少。这表明需要改进检测规则的质量，提升整体防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLvkyWskOIaBXWTg4WWkDPp0wTLFTsFV4jTrVwLoiaaeDQPMZmgRVkibpQ/640?wx_fmt=png&from=appmsg)

图14  检测规则示意图

针对T1003.001（OS凭证转储 - LSASS内存）攻击技术的分层检测规则示例，从StP1到StP5每个层级的具体检测特征：

**1.StP5（最高层）- 核心程序级别：**

（1）检测针对LSASS的内核函数调用（NtOpenPrecess或ZwOpenProcess）

（2）这层检测最难绕过，因为它监控底层系统调用

**2.StP4 - 部分核心程序：**

（1）检测CreateToolhelp32Snapshot API调用

（2）监控从特定注册表路径向LSASS加载DLL的行为

（3）关注特定的API和系统交互

**3.StP3 - 预置工具：**

（1）检测Rundll32.exe执行comsvcs.dll的行为

（2）监控特定的Sysmon事件（EventID 10，权限值0x1010）

（3）关注系统工具的使用方式

**4.StP2 - 攻击者工具：**

（1）检测特定进程链（父进程windbg.exe/procdump.exe，子进程lsass.exe）

（2）检测Mimikatz工具的特征命令行

（3）关注已知攻击工具的特征

**5.StP1（最低层）- 临时特征：**

（1）检测特定文件名（mimikatz.exe）

（2）检测特定MD5哈希值

（3）这些特征最容易被攻击者更改

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrDpv5pFWicoIA9XvyltYzMLTeLeJuot9QhXXIqeicicPNP94AqPLsgGHwF9Fgm7sibaIT00SE8IcwArA/640?wx_fmt=png&from=appmsg)

图15  T1003.001的攻击技术在攀登金字塔的示例

**ATT&CK在科技领域的应用**

**人工智能领域：**MITRE 人工智能系统对抗威胁格局 (ATLAS)是攻击者的全球可访问的活知识库，基于现实世界攻击的战术和技术，人工观察和真实演示，情报 (AI) 红队和安全小组。人工智能系统中存在越来越多的漏洞，人工智能的结合增加了现有系统的攻击面，超越传统的网络攻击。ATLA...