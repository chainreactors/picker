---
title: AI安全专题周报
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-3/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-08-21
fetch_date: 2026-08-22T02:51:25.250014
---

# AI安全专题周报

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

21 Aug 2026
• 11 min read

[Share](#/share)

**报告编号：**TIC-202608-AI02

**报告周期：**2026年8月15日—8月21日

## 一、报告概述

基于360威胁情报中心对本期网络安全前沿素材的整理与分析，本周AI安全风险主要集中在AI生成恶意代码与攻击脚本、生成式AI辅助恶意工具开发、AI安全工具自身漏洞、前沿模型网络能力治理、拟人化自动操作对智能行为识别的挑战以及深度伪造驱动的欺诈活动等方向。相关事件显示，AI能力正嵌入后门与远控工具开发、防御规避、工业控制系统攻击准备、网络间谍活动和社会工程链路，同时AI工具、前沿模型与平台行为识别体系也面临新的安全压力。

**报告重点内容涵盖：**

· **AI辅助攻击与恶意工具开发：**UAT-10147使用AI生成的SPECTRE后门致盲EDR；针对西门子S7系列PLC的活动中出现AI生成的Python脚本；Armored Likho继续将生成式AI用于恶意组件开发；UNC7005相关CHERRYPIE样本也存在LLM生成痕迹。

· **AI工具、模型与智能识别风险：**PentestGPT网页爬取组件存在远程代码注入风险；OpenAI强化Astra模型安全机制以应对网络能力风险；自动化硬件拟人操作还对传统设备环境检测形成绕过压力。

· **AI衍生欺诈风险：**投资骗局利用深度伪造广告、WhatsApp群组和虚假投资平台构建连续欺诈链路，提升社会工程欺骗性。

───────────────────────────────────

## 二、本周重点安全事件

### （一）UAT-10147利用AI生成SPECTRE后门实施EDR规避

**事件名称：**网络安全是否错失了致胜标志？

**发布日期：**2026-08-20

**发布机构：**talosintelligence

**威胁概述：**

UAT-10147利用Zimbra、Nacos和Telerik UI等应用的已知1day漏洞获取初始访问，并依赖窃取的ASP.NET MachineKeys实施ViewState反序列化攻击。攻击链进一步使用AI生成的SPECTRE后门及BYOVD能力植入Linux内核rootkit以致盲EDR，并通过跨平台后利用自动化操作维持访问。

**IOC指标：**

· **MD5：**2915b3f8b703eb744fc54c81f4a9c67f, 7bdbd180c081fa63ca94f9c22c457376, 8ef476fa2322d063896830f85bac2e7f, c2efb2dcacba6d3ccc175b6ce1b7ed0a, 9a47c4d379998ade2f8f99e23a630c06

· **SHA256：**9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507, a31f222fc283227f5e7988d1ad9c0aecd66d58bb7b4d8518ae23e110308dbf91, 24fa02c3f6ab460648f2c1274aefffb3e25569b5afdcb0d4a5918c7c742780f1, 90b1456cdbe6bc2779ea0b4736ed9a998a71ae37390331b6ba87e389a49d3d59, c4dd71e347a076ba24bdd2d0ee532ef991c1ef25a2431a19f850942ba2ab16b2

**报告链接：**

https://blog.talosintelligence.com/is-cyber-missing-the-marque/

───────────────────────────────────

### （二）AI生成漏洞利用脚本针对西门子S7系列PLC

**事件名称：**防御针对西门子S7系列PLC的活跃威胁 | CISA

**发布日期：**2026-08-19

**发布机构：**cisa news

**威胁概述：**

威胁攻击者利用互联网扫描服务识别暴露或保护不当的西门子S7系列PLC，并借助AI辅助快速开发漏洞利用代码。素材显示，攻击者部署结合snap7.dll库的AI生成Python脚本，伪装成合法监控工具对PLC数据块执行读写操作，相关活动可能对制造、能源、农业和国防等关键基础设施造成中断或设备损坏风险。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a

───────────────────────────────────

### （三）PentestGPT网页爬取组件存在远程代码注入漏洞

**事件名称：**CVE-2026-76993 : GreyDGL PentestGPT 网页爬取漏洞

**发布日期：**2026-08-20

**发布机构：**securityvulnerability exploits

**威胁概述：**

GreyDGL的PentestGPT网页爬取组件存在代码注入漏洞，攻击者可通过网络向PentestGPT发送恶意Traceback参数，利用组件对该参数处理不当触发远程代码注入。素材显示该漏洞影响最高1.0.0版本，漏洞已公开且存在PoC。

**IOC指标：**

· **CVE：**CVE-2026-76993

**报告链接：**

https://securityvulnerability.io/vulnerability/CVE-2026-76993

───────────────────────────────────

### （四）深度伪造广告与虚假投资平台推动网络化欺诈

**事件名称：**同一个对手：欺诈是一个网络，而不是一次支付| Group-IB 博客

**发布日期：**2026-08-20

**发布机构：**group ib

**威胁概述：**

攻击者通过投资骗局构建连续欺诈链路，利用深度伪造广告、SEO内容或社交广告接触受害者，并进一步引导其进入WhatsApp群组或虚假投资平台。受害者随后被诱导购买指定股票或充值资金，攻击者再通过脚本限制提现或直接抛售股票，造成经济损失。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

https://www.group-ib.com/blog/one-adversary-fraud-network/

───────────────────────────────────

### （五）Armored Likho利用AI扩展BusySnake与Kharon RAT攻击能力

**事件名称：**Armored Likho 军火库中的新木马：BusySnake RAT 和 Kharon RAT

**发布日期：**2026-08-20

**发布机构：**securelist ru

**威胁概述：**

Armored Likho使用新开发的BusySnake RAT和开源工具Kharon RAT开展攻击。素材及其原始报告显示，BusySnake RAT具有Python和Golang版本，利用Telegram和GitLab作为C2基础设施，并通过DLL侧载等方式分发；该组织继续将生成式AI用于初始加载器和恶意组件开发，最终实现远程控制和数据窃取。

**IOC指标：**

· **Domain：**kalkulator.store, wtfdomain.xyz

· **IP：**103.6.169.79

· **MD5：**54e6fb97e5e1e1be431c4b06f2713eca, 1193d0fbe5046ae4b3b757e01a074059, 263bb2f257a8dbb9873366e0493982df, 7a9c9c35588d7734dcb476c93b4fff11, ed8ebe5a7894588a27124e3076e8fa01

**报告链接：**

https://securelist.ru/tr/armored-likho-campaigns-with-busysnake-rat-and-kharon-rat/116658/

───────────────────────────────────

### （六）自动化硬件拟人操作挑战智能行为识别与反作弊

**事件名称：**机器越来越像人，平台还能识别出来吗？我们用8台设备做了一次实验

**发布日期：**2026-08-21

**发布机构：**威胁猎人Threat Hunter

**威胁概述：**

威胁猎人研究团队测试了8台不同类型的自动化设备，分析自动化硬件操作与真人操作的差异。素材显示，机械臂、HID设备等外部硬件可模拟真人触屏操作并尝试绕过设备环境检测；平台需要结合压力、接触面积和操作轨迹等多维行为数据识别自动化作弊。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzI3NDY3NDUxNg==&mid=2247505049&idx=1&sn=834389a1dbd86356daa6852cf548a66c

───────────────────────────────────

### （七）UNC7005使用带有LLM生成痕迹的CHERRYPIE开展攻击

**事件名称：**顺势而为：针对俄罗斯感兴趣的个人的不同集群目标

**发布日期：**2026-08-21

**发布机构：**Google Cloud Blog

**威胁概述：**

Google威胁情报团队追踪的疑似俄罗斯威胁集群UNC7005通过钓鱼、OAuth流程滥用和恶意软件攻击学术、国防、政府及智库人员。原始报告指出，相关CHERRYPIE PowerShell信息窃取器样本存在大量表明由LLM生成的代码痕迹，显示大模型正在缩短恶意工具开发与部署周期，并增加攻击归因和处置难度。

**IOC指标：**

· **Domain：**dosportal.app, foreignrelations.us, fewfwfwfwfwf.info, miov2iaiaoubqosiqoiajwowiwjso.online, mioisiskwowiwjowuwjwolab.club

· **IP：**107.189.18.7, 196.251.107.171, 31.57.243.154, 38.146.28.75, 104.194.159.150

· **SHA256：**5b8d50c2e8cc3038b7c6e6dbf1219f6e814930a1e3c0053143a1191ae67f8ffc, a06a8fd1b6fa1924199a4540cf16d089217ce8f78c617739946f145fd1fc88c1, 1d9299799a7b8da67c44ebec064d64542c27645f8e84de4a22ca3f6cbc843e3c, c5826032207d623a7f6caec8465af7364eccc355f9a48897da2a54f3e4420265, 125752ad7c20d715920a3b2fb0fdde660f07b3f2b053665cf38c2d6d9de86e1e

**报告链接：**

https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia

───────────────────────────────────

### （八）OpenAI强化Astra模型安全机制应对网络能力风险

**事件名称：**OpenAI模型安全机制升级（安全牛资讯汇总）

**发布日期：**2026-08-21

**发布机构：**安全牛

**威胁概述：**

安全牛本期资讯汇总提及OpenAI模型安全机制升级。经原始资讯链路核对，该调整与Astra模型的网络安全能力风险有关，OpenAI因此强化相关安全限制。该事件表明，随着前沿模型网络能力提升，模型安全治理与风险控制机制需要同步升级。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MjM5Njc3NjM4MA==&mid=2651142415&idx=2&sn=d0cae1fe5a9341e4c56a956489484e93

───────────────────────────────────

## 三、本周AI安全风险观察

**AI生成与辅助开发能力已进入真实攻击链：**UAT-10147使用AI生成SPECTRE后门实施防御规避，CISA素材显示威胁方使用AI生成Python脚本对西门子S7系列PLC执行读写操作，Armored Likho继续将生成式AI用于恶意组件开发；UNC7005相关CHERRYPIE样本还存在大量LLM生成痕迹，AI辅助攻击已覆盖通用网络、工业控制系统、跨平台远控工具和网络间谍活动。

**AI工具、前沿模型与行为识别体系面临多重风险：**PentestGPT漏洞表明AI安全工具可能因输入处理和联网组件形成攻击面；OpenAI强化Astra模型安全限制，反映前沿模型网络能力提升带来的治理压力；自动化硬件拟人操作实验则表明，仅依赖设备环境检测难以识别全部作弊行为。

**深度伪造进一步放大网络欺诈效果：**Group-IB素材中的欺诈链路利用深度伪造广告建立初始信任，再通过WhatsApp群组和虚假投资平台完成引流、诱导支付和资金控制，AI生成内容正在增强传统社会工程活动的欺骗性。

───────────────────────────────────

## 四、安全建议

**加强AI辅助攻击相关系统与恶意工具检测：**优先修复Zimbra、Nacos等应用的已知漏洞，锁定ASP.NET MachineKeys，阻止已知易受攻击驱动程序并监控异常HTTP 500错误；同时将BusySnake、Kharon及UNC7005相关域名、IP和样本哈希纳入检测与封禁策略。

**收紧AI工具、前沿模型与工业控制系统暴露面：**避免将受影响的PentestGPT组件暴露于公网并监控应用服务器异常活动；持续跟进前沿模型安全机制升级，限制高风险能力和不必要的外部访问；同时清查西门子S7系列PLC，及时应用关键补丁并监控102端口异常S7comm流量。

**强化拟人化自动操作与深度伪造欺诈识别：**针对自动化作弊，结合压力、接触面积、操作轨迹等多维行为数据进行识别，避免仅依赖设备环境检测；针对投资欺诈，加强对深度伪造广告、WhatsApp引流和虚假投资平台关联关系的识别，及时阻断连续欺诈链路。

───────────────────────────────────

## 五、报告总结

本周AI安全风险进一步体现出攻击能力增强与AI工具自身暴露并行发展的特征。AI生成和AI辅助开发能力已被纳入真实攻击链，用于恶意后门、跨平台远控工具和信息窃取器开发、防御规避、工业控制系统攻击准备及网络间谍活动。

同时，PentestGPT等AI安全工具本身可能因输入处理或联网组件漏洞成为攻击入口，前沿模型网络能力提升也推动模型安全机制持续升级；机械臂、HID设备等自动化硬件可模拟真人操作，平台还需同步评估工具暴露面、模型能力边界和多维行为检测有效性。

此外，深度伪造广告正在与社交引流、虚假投资平台和资金控制手段结合，提升网络欺诈的欺骗性与链路完整度。安全防护需要结合跨渠道风险信号和恶意基础设施模式提升识别与处置能力。

───────────────────────────────────

## 报告说明

本报告由360威胁情报中心基于2026年8月15日至8月21日公开威胁情报整理形成，重点分析AI生成恶意代码与后门、AI辅助工业控制系统攻击、生成式AI与LLM辅助恶意工具开发、AI安全工具漏洞、前沿模型网络能力治理、深度伪造驱动网络欺诈及拟人化自动操作对智能行为识别的挑战，为企业AI应用、工业控制系统、智能风控及安全运营防护提供参考。

**情报时效性：** 2026年8月15日—8月21日  **威胁评估等级：** 高风险（多源情报验证）

[## AI安全专题周报(20260814)

报告编号：TIC-202608-AI01
报告周期：2026年8月8日—8月14日
一、报告概述
基于360威胁情报中心对全球人工智能安全态势的持续监测与分析，本周AI安全风险主要集中在AI Agent自主攻击、AI开发供应链及AI衍生攻击方式等方向。相关事件显示，随着AI逐步参与代码开发、漏洞测试和自动化任务执行，其网络访问、代码执行、第三方依赖及敏感凭证正在形成新的安全攻击面。
报告重点内容涵盖：
· AI Agent自主攻击与运行安全：AI Agent已表现出自主发现漏洞、突破隔离环境及持续探索攻击路径的能力，容器和沙箱等执行环境的隔离风险同步上升。
· AI开发与供应链安全：npm、CI/CD及AI开发工具逐渐...