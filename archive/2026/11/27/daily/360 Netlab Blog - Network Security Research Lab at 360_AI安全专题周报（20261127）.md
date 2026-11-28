---
title: AI安全专题周报（20261127）
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-20261127/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-11-27
fetch_date: 2026-11-28T09:42:10.608374
---

# AI安全专题周报（20261127）

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报（20261127）

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

27 Nov 2026
• 阅读时间 13 分钟

[分享](#/share)

**报告编号：**TIC-202611-AI04

**报告日期：**2026年11月21日—11月27日

## **一、报告概览**

本期关注8项AI安全事件与研究。智能体被用于加速Web服务器和云环境入侵，模型托管平台出现利用加载流程窃取凭据的恶意仓库，仿冒AI工具的安装程序则借助脆弱驱动攻击终端防护。现有案例表明，企业需要同时管控模型加载权限、云身份信任关系和软件下载来源，并以行为关联检测补充静态IOC拦截。 本期还纳入DIVD入侵取证、OpenRouter推理供应商数据处理事件，以及Gradio和Kubernetes MCP服务的漏洞通告。

**报告重点内容涵盖：**

智能体辅助入侵：Unit 42披露多平台攻击中的高速命令执行与自适应横向移动。

模型供应链：JFrog发现恶意Hugging Face仓库通过远程代码、Pickle和模板路径尝试窃取凭据。

云与终端防护：Wiz分析ARTEX相关云攻击；ASEC披露仿冒Ollama安装包加载恶意驱动。

服务与身份边界：复核第三方推理路由的数据处理承诺，升级受影响的Gradio及Kubernetes MCP部署。

## **二、本周重点安全事件**

### **（一）智能体加速Web服务器与云环境入侵**

**事件名称：**Unit 42披露自主AI智能体参与多平台攻击

**发布日期：**2026-11-24

**发布机构：**Palo Alto Networks Unit 42

**威胁概述：**

Unit 42披露，2026年7月至9月观察到十余起使用自主AI智能体的攻击活动，初始立足点均来自脆弱Web应用上的Web shell。智能体随后接手侦察、凭据搜寻和横向移动，部分样本中的命令间隔中位数从人工阶段的23.9秒降至1.4秒。研究还记录了从Linux向Windows IIS迁移、针对云实例元数据接口调整访问方式等行为。这些结果体现的是既有技术被更快组合和执行，不能据此认定所有尝试均成功或无需人工介入。防守方应关联Web服务子进程、短时密集脚本运行及异常云API调用，对凭据使用与横向移动及时阻断。

**IOC指标：**

**· IP：**150.242.254.199, 204.194.54.240, 206.123.152.217, 38.253.224.12

**报告链接：**

[https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/?ref=blog.netlab.360.com)

### **（二）恶意Hugging Face模型借加载流程窃取凭据**

**事件名称：**ARTEX驱动的恶意模型活动在自测中泄露操作者环境

**发布日期：**2026-11-26

**发布机构：**JFrog Security Research

**威胁概述：**

JFrog发现，一个Hugging Face账号发布的所谓Llama微调模型实际携带凭据收集代码，随后继续调整仓库包装。攻击涉及远程Python模块、恶意Pickle及模板注入尝试，并利用Hugging Face提交接口回传环境信息。不同路径受加载配置约束：远程模块需要允许相应代码执行，较新的PyTorch权重加载保护及Transformers模板沙箱能够阻断部分路径。最初公开的外传数据来自操作者自身测试环境，不能据此推定存在同等规模的下游受害者。平台已依研究报告停用相关仓库；企业仍应固定可信revision，隔离模型检查任务，并避免向模型加载容器注入生产凭据。

**IOC指标：**

**· SHA256（节选）：**ceb5816fac7cbd886b096c7f0c0402913488ca0f967b617d3a7e25508032e6a8, b068b5a2ec3a6a13deef686173935330fb2f7fd2b3fb1f34aa2b6e359624de19, ed89685e8c16d0cb6dc218d0972e7a0a9e292f9b98f6b0ef0b2ab340d06d34e3, 79b47fe688932507fa013de36c057846916f586b3893f2fae3fc364cbd5d7c9e, 2bf25c4c3aa1e2efdff4ae9ee7e1434e279115608eb7a176e4e50e874c07c50d

哈希为原始研究列出的恶意模型组件节选；Hugging Face公共域名本身不作为恶意IOC。

**报告链接：**

[https://research.jfrog.com/post/the-agent-that-robbed-itself-an-ai-driven-hugging-face-malware-campaign-leaks-its-own-operator/](https://research.jfrog.com/post/the-agent-that-robbed-itself-an-ai-driven-hugging-face-malware-campaign-leaks-its-own-operator/?ref=blog.netlab.360.com)

### **（三）ARTEX相关攻击沿CI与云身份信任链扩散**

**事件名称：**Wiz披露智能体攻击框架参与的真实云入侵案例

**发布日期：**2026-11-23

**发布机构：**Wiz Research

**威胁概述：**

Wiz披露多起使用ARTEX及相似框架的云攻击，入口包括被盗凭据、暴露服务和租户隔离缺陷。在具体案例中，攻击者从代码仓库与CI信任关系进入云环境，搜集工作流可访问的机密和Terraform状态；另有攻击利用服务账号权限创建特权Pod，继续获取节点及集群凭据。研究强调，ARTEX存在大量分支与改名版本，相关活动来自多个无关操作者，不能因工具相同便统一归因。攻击中住宅代理轮换频繁，单纯依赖IP封禁效果有限。企业应收紧CI工作负载身份、服务账号与特权容器权限，关联异常机密批量读取和跨环境凭据使用。

**IOC指标：**

**· IP（节选）：**192.236.187.90, 104.223.50.72, 107.172.5.167, 107.173.104.66, 130.94.102.111

地址为研究列出的历史观测节选，部分属于代理或托管基础设施；应结合观测时间与行为研判，不能据此认定其所有流量均恶意。

**报告链接：**

[https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks?ref=blog.netlab.360.com)

### **（四）仿冒Ollama安装程序借脆弱驱动攻击安全产品**

**事件名称：**伪装AI工具的恶意软件通过BYOVD加载WinWyvern

**发布日期：**2026-11-23

**发布机构：**AhnLab SEcurity intelligence Center（ASEC）

**威胁概述：**

ASEC发现，攻击者使用韩语仿冒Ollama下载页分发恶意安装包，目标指向韩国用户。安装流程运行正常AI组件以降低怀疑，同时释放恶意程序，将后续DLL隐藏在NTFS备用数据流中，并安装存在漏洞的NeacSafe64.sys驱动。攻击者借助该驱动的内核读写能力加载WinWyvern，尝试修改安全产品内存、削弱检测与清除功能。这里的AI关联主要是品牌和安装诱饵，不能认定载荷本身由AI生成。研究同时说明，最新版AhnLab V3已不受该内存补丁手法影响。组织应统一AI工具下载渠道，结合驱动加载、备用数据流与安全产品异常行为排查此类攻击。

**IOC指标：**

**· Domain：**ollama-ko.com

**· URL：**http://ollama-ko.com/

原文所列4条MD5均存在长度异常，未擅自补齐或作为有效哈希展示；原始值完整保留在核验归档。

**报告链接：**

[https://asec.ahnlab.com/ko/96707/](https://asec.ahnlab.com/ko/96707/?ref=blog.netlab.360.com)

### **（五）DIVD公布智能体参与入侵的取证报告**

**事件名称：**荷兰漏洞披露机构复盘工单系统入侵及数据外泄

**发布日期：**2026-11-27

**发布机构：**DIVD、Merlon

**威胁概述：**

DIVD与Merlon于11月25日公布9月入侵事件的完整取证报告。DIVD确认，攻击者借助两处当时未知的Zammad漏洞突破工单系统，并在后续活动中使用AI智能体，部分数据被外传。机构随后关闭并重建机房系统，向受影响方发出通知，继续公开披露调查结果。两处漏洞分别在Zammad 7.2和7.2.2得到修复，部署方应核查是否已覆盖两项修复，并复盘高权限会话、工单数据访问及异常流量。工单系统常含漏洞线索和联系方式，建议将它与扫描及管理基础设施分段隔离，并在审计中关联身份、主机和网络信号。公开取证报告的日期与最早发现攻击的日期相隔两个月。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

[https://www.divd.nl/hacked/](https://www.divd.nl/hacked/?ref=blog.netlab.360.com)

[https://csirt.divd.nl/cases/DIVD-2026-00014/](https://csirt.divd.nl/cases/DIVD-2026-00014/?ref=blog.netlab.360.com)

### **（六）OpenRouter披露第三方推理数据处理事件**

**事件名称：**推理供应商的数据处理风险触发下架和零保留资格复核

**发布日期：**2026-11-24

**发布机构：**OpenRouter

**威胁概述：**

OpenRouter于11月22日发布供应商数据处理通报。研究人员发现部分推理供应商出现数据受损或未遵守已公布政策的迹象，平台随后移除三家供应商，并撤销125个端点的零数据保留资格，其中包括预防性移除的端点。平台表示已通知可能受影响的客户，并继续验证请求是否被转发至第三方。企业应查看受影响路由、供应商通知、请求留存以及凭据暴露范围，对可能提交到受影响端点的密钥进行轮换，同时明确零保留承诺适用到哪一层。该事件说明，推理代理的合同条款应与实际路由、分包方清单和持续验证结合使用。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

[https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/?ref=blog.netlab.360.com)

### **（七）Gradio运行历史接口存在身份验证绕过风险**

**事件名称：**CVE-2026-134825可能暴露使用本地令牌访问的运行历史数据

**发布日期：**2026-11-22

**发布机构：**VulnCheck、Gradio

**威胁概述：**

VulnCheck披露Gradio 6.27.0至6.32.0之前版本的身份验证绕过风险。在启用服务端渲染的受影响部署中，运行历史接口对本地请求来源的认定存在缺陷。未经身份验证的远程请求可能借用部署者已保存的Hugging Face令牌，读取运行记录和相关资源，或以该令牌的权限进行写入。企业应将受影响部署升级至6.32.0或后续已修复版本，限制后台和运行历史接口的网络可达范围，审查服务端令牌权限，并检查异常的历史记录或资源访问。当前收录依据为公开漏洞通告，通告本身未证明相关部署已遭入侵。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

[https://osv.dev/vulnerability/CVE-2026-134825](https://osv.dev/vulnerability/CVE-2026-134825?ref=blog.netlab.360.com)

[https://github.com/gradio-app/gradio/releases/tag/gradio%406.32.0](https://github.com/gradio-app/gradio/releases/tag/gradio%406.32.0?ref=blog.netlab.360.com)

### **（八）Kubernetes MCP服务存在非预期文件读取风险**

**事件名称：**CVE-2026-134817影响对远程客户端开放的部分部署

**发布日期：**2026-11-22

**发布机构：**VulnCheck、Flux159

**威胁概述：**

公开通告指出，Flux159的mcp-server-kubernetes在4.2.0之前存在输入校验缺陷。远程客户端能够调用受影响工具时，服务进程可能访问原本不应向该客户端公开的本地文件，暴露范围取决于进程账号可读取的内容。运维团队应盘点开放HTTP或SSE的部署，优先升级至4.2.0或后续修复版本，关闭不需要的远程入口，并用独立、最小权限的账号运行服务。建议检查历史工具调用与可疑文件访问，必要时轮换服务在本机可读取的集群凭据。该通告描述的是文件读取风险，实际影响需结合网络可达性、客户端权限及服务部署方式判断。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

[https://github.com/advisories/GHSA-8v48-c263-r637](https://github.com/advisories/GHSA-8v48-c263-r637?ref=blog.netlab.360.com)

[https://github.com/Flux159/mcp-server-kubernetes/releases/tag/v4.2.0](https://github.com/Flux159/mcp-server-kubernetes/releases/tag/v4.2.0?ref=blog.netlab.360.com)

## **三、本周AI安全风险观察**

攻击提速使暴露资产、遗留密钥和过宽权限更容易被连续利用。应把Web访问、终端进程、CI执行和云审计日志串联起来，以异常行为触发自动隔离与凭据撤销。

模型仓库中的配置、Python模块、序列化文件和聊天模板都可能影响执行边界。安全检查任务与正式推理环境应分别隔离，不能把仓库可下载等同于制品可信。

同一框架名称不代表同一攻击组织，公共服务或代理IP也不等同于永久恶意基础设施。IOC匹配应结合时间、路径、账号和上下文复核。

## **四、安全建议**

修复对外Web应用与云管理服务的高风险暴露，监测Web服务启动Shell、批量脚本及跨系统远程写入；发现入侵后同步撤销关联凭据。

对CI工作流、云角色和Kubernetes服务账号执行最小权限，限制创建特权Pod和读取集群机密，检查生产审批是否能被分支或工作流修改绕过。

模型下载与预加载在隔离环境完成，固定来源、revision和可信摘要；谨慎启用远程代码及不安全反序列化，移除环境中的生产密钥并限制外传。

AI工具统一从核实后的官方渠道分发，排查仿冒安装包、异常驱动与NTFS备用数据流；保持终端安全产品和脆弱驱动拦截策略更新。

## **五、报告总结**

本期事件反映出AI安全风险已贯穿模型制品、开发与云身份以及终端软件分发环节。防护重点应落在执行权限、凭据隔离和可快速响应的行为检测上，并保留证据区分成功入侵、攻击尝试与研究推断。

## **报告说明**

本报告由360威胁情报中心基于2026年11月21日至11月27日公开威胁情报整理形成，重点分析智能体参与的多平台入侵、Hugging Face恶意模型、ARTEX相关云攻击及仿冒Ollama安装包，为企业模型供应链、云身份、开发环境和终端安全防护提供参考。

**情报时效性：**2026年11月21日—11月27日

[## AI安全专题周报（20261120）

报告编号：TIC-202611-AI03
报告日期：2026年11月14日—11月20日
一、报告概览
本期整理7项AI安全事件与研究。微软agent-framework遭供应链投毒，恶意GitHub仓库将项目说明和启动钩子变成编码助手的执行入口；Kokoro发布者账号接管研究则暴露了模型更新链的身份恢复风险。攻击侧，非洲证券交易所调查发现...