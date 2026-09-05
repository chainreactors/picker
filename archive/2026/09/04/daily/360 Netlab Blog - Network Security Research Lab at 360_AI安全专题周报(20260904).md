---
title: AI安全专题周报(20260904)
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-20260904-2/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-09-04
fetch_date: 2026-09-05T06:29:06.997911
---

# AI安全专题周报(20260904)

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报(20260904)

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

04 Sep 2026
• 11 min read

[Share](#/share)

**报告编号：**TIC-202609-AI01

**报告周期：**2026年8月29日—9月4日

## 一、报告概述

基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要集中在AI辅助自动化攻击、AI编程与Agent工具链漏洞、模型服务和API密钥滥用、AI辅助恶意软件开发以及AI信任链钓鱼等方向。相关事件显示，AI能力正在加速攻击侦察、攻击规划和漏洞利用适配，同时AI基础设施、代码仓库与云模型资源也成为高价值攻击目标。

**报告重点内容涵盖：**

**· AI辅助攻击与恶意工具开发：**攻击者使用AI和智能体框架在不到10小时内完成多阶段勒索攻击，Aurora团伙使用Cursor AI辅助规划，NodeStealer新增AI辅助编写的间谍功能，Claude还被用于跨设备移植工控漏洞利用。

**· AI应用与Agent工具链风险：**Hermes Agent可因恶意Git配置触发代码执行，LiteLLM漏洞遭在野利用并导致模型配置和API密钥暴露，云端模型资源还面临LLMjacking滥用。

**· AI信任链与开发环境风险：**银狐通过伪造DeepSeek官网并借助用户对AI输出的信任投递木马，AI搜索与推荐结果、第三方代码库和云凭据需要实施更严格的来源验证。

───────────────────────────────────

## 二、本周重点安全事件

### （一）银狐伪造DeepSeek官网利用AI信任链投递木马

**事件名称：**银狐借AI信任链钓鱼 搜索结果暗藏下载陷阱

**发布日期：**2026-09-01

**发布机构：**火绒安全

**威胁概述：**

火绒安全披露，银狐团伙伪造DeepSeek官方网站，并利用用户对AI智能体输出结果的信任诱导下载和运行恶意程序。载荷执行后会检测环境、下载后续文件，利用驱动漏洞关闭安全软件并修改注册表关闭UAC，同时通过计划任务和注册表实现持久化，窃取浏览器数据并针对企业微信环境开展定向攻击。

**IOC指标：**

**· Domain：**lgtnfx.net, lwuoys.net, eeszuu.com

**· IP：**8.218.106.149, 8.218.220.211

**· IP:Port：**92.48.71.103:9000, 92.48.71.103:20032

**· URL：**https://26usdm.oss-cn-beijing.aliyuncs.com/tad, https://2bbaz2.oss-cn-beijing.aliyuncs.com/tad, https://mm2027.oss-cn-hangzhou.aliyuncs.com/f.dat, https://nm25.cn-hangzhou.aliyuncs.com/qd.dat

**STIX详情：**

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzI3NjYzMDM1Mg==&mid=2247536988&idx=1&sn=ec7f000e629139b96b1f3caa956f5958

───────────────────────────────────

### （二）Aurora勒索团伙使用Cursor AI辅助攻击规划

**事件名称：**黑客服务器裸奔泄露内幕：Aurora勒索团伙用Cursor AI做攻击规划

**发布日期：**2026-09-01

**发布机构：**奇安信威胁情报中心

**威胁概述：**

奇安信威胁情报中心披露，Aurora勒索软件攻击者因服务器开放目录配置错误，暴露了攻击工具、AI聊天记录和加密器。素材显示，攻击者使用Cursor AI辅助攻击规划，并结合有效SSL-VPN凭据、内网枚举、ADCS滥用、NTLM中继和数据打包外传等手段，针对多个国家的组织实施勒索活动。

**IOC指标：**

**· CVE：**MS17-010

**· Domain：**ijexszhscln27nl263lmcd7tx3jttkhm4wjhd4e3y6r4csdbfyeprvid.onion, pub-c057b7d0b24944a29e381ce9ea22a2f1.r2.dev, exposedrecords.io

**· IP：**172.86.113.245, 172.86.90.75, 144.172.116.150, 104.194.134.167, 89.106.83.49

**· IP:Port：**167.88.167.37:50167, 45.61.148.166:21056

**· SHA256：**eb0aab1e892d7e09e2c7bcf1d21fd83c1743ed9196b3efac6c78482fb0d99207, a4af136d159a8eb96b54924fa80355ca52874913301300f55af7d67ae97edcfe

**STIX详情：**

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzI2MDc2MDA4OA==&mid=2247520161&idx=1&sn=61ee15f915debc760d7d4ddbd6fb19ad

───────────────────────────────────

### （三）Hermes Agent恶意Git配置可触发远程代码执行

**事件名称：**CVE-2026-71963：Nous Research的Hermes Agent中的远程代码执行漏洞

**发布日期：**2026-09-03

**发布机构：**SecurityVulnerability.io

**威胁概述：**

Hermes Agent 0.18.2至0.21.0版本存在远程代码执行漏洞。攻击者可在伪造的.git/config文件中设置core.fsmonitor命令；当用户与受感染代码库交互并触发Agent刷新Git状态时，恶意命令会在用户进程上下文中执行，可能进一步泄露API密钥等敏感信息。

**IOC指标：**

**· CVE：**CVE-2026-71963

**报告链接：**

https://securityvulnerability.io/vulnerability/CVE-2026-71963

───────────────────────────────────

### （四）LiteLLM漏洞遭在野利用并窃取大模型API密钥

**事件名称：**CISA连夜拉黑7个在野漏洞：黑客正顺着LiteLLM偷你的大模型密钥

**发布日期：**2026-09-04

**发布机构：**安全客

**威胁概述：**

素材显示，攻击者正在利用LiteLLM等组件的漏洞实施攻击，并通过LiteLLM漏洞链绕过认证、实现远程代码执行，进而获取数据库中的模型配置和API密钥材料。后续活动还包括建立反向Shell和部署XMRig挖矿程序。相关漏洞已被纳入CISA已知被利用漏洞目录。

**IOC指标：**

**· CVE：**CVE-2026-83548, CVE-2026-83549, CVE-2026-82329, CVE-2026-9586, CVE-2026-49869

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzA5ODA0NDE2MA==&mid=2649790451&idx=1&sn=8dfae39e2b70514d7beb78ba0e053345

───────────────────────────────────

### （五）泄露AWS凭据被用于LLMjacking盗用模型资源

**事件名称：**其他人正在使用您的AI

**发布日期：**2026-09-03

**发布机构：**FortiGuard Labs

**威胁概述：**

FortiGuard Labs披露，攻击者利用泄露且具有AdministratorAccess权限的长期AWS IAM访问密钥进入云账户，创建新的IAM身份，并通过AWS Marketplace订阅基础AI模型。攻击者随后调用模型产生高额推理费用，或转售模型访问权，形成LLMjacking风险。

**IOC指标：**

**· 暂无公开IOC**

**STIX详情：**

**报告链接：**

https://www.fortinet.com/blog/threat-research/someone-else-is-using-your-ai

───────────────────────────────────

### （六）AI辅助NodeStealer扩展为全功能间谍软件

**事件名称：**Python NodeStealer：AI辅助成为全面间谍软件

**发布日期：**2026-09-02

**发布机构：**Netskope Threat Labs

**威胁概述：**

Netskope发现Python版NodeStealer新变种增加了AI辅助编写的按键记录、剪贴板监控和截图功能，并可查询20多个Facebook Graph API端点收集账户信息。恶意程序通过两个Telegram C2机器人通道分别回传操作数据和Facebook专用数据，主要影响金融服务等行业。

**IOC指标：**

**· 暂无公开IOC**

**STIX详情：**

**报告链接：**

https://www.netskope.com/blog/python-nodestealer-ai-assisted-to-full-spyware

───────────────────────────────────

### （七）研究人员使用Claude跨设备移植工控漏洞利用

**事件名称：**安全专家用Claude将工控漏洞利用跨设备移植

**发布日期：**2026-09-02

**发布机构：**安全圈

**威胁概述：**

素材显示，Forescout实验室研究人员使用Claude大模型，在8小时内将CVE-2021-31886漏洞利用跨设备移植至WAGO控制器。Claude辅助修改协议时序并保留攻击载荷，最终实现ARM Shellcode执行。该实验说明，AI可降低工控漏洞利用适配不同设备和协议实现的技术成本。

**IOC指标：**

**· CVE：**CVE-2021-31886

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzIzMzE4NDU1OQ==&mid=2652078593&idx=3&sn=b27684913ac539add1c5dbc2ff39eb66

───────────────────────────────────

### （八）AI与智能体框架辅助企业网络勒索攻击

**事件名称：**一场AI辅助的网络攻击：深入Unit 42调查

**发布日期：**2026-09-02

**发布机构：**Palo Alto Networks Unit 42

**威胁概述：**

Unit 42调查显示，攻击者利用前沿AI和智能体AI框架对企业网络实施勒索攻击，在不到10小时内完成多阶段行动。攻击者首先破坏公共API端点并部署自动化侦察智能体，随后梳理代码库提取硬编码令牌和密码，利用暴露凭据获取根权限、窃取云访问密钥，并劫持受害者AI基础设施用于后续攻击。

**IOC指标：**

**· 暂无公开IOC**

**STIX详情：**

**报告链接：**

https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/

───────────────────────────────────

## 三、本周AI安全风险观察

**AI辅助攻击已覆盖完整入侵链：**Unit 42案例显示，AI和智能体框架可用于自动化侦察、代码库凭据提取、权限提升和AI基础设施劫持；Aurora事件则表明，Cursor AI已被用于勒索攻击规划，AI能力正嵌入真实攻击流程。

**AI编程工具和Agent执行边界成为新的攻击面：**Hermes Agent漏洞可借助恶意Git配置触发命令执行，说明Agent自动读取代码仓库状态、调用本地工具和继承用户权限时，可能将不可信项目内容转化为主机风险。

**AI基础设施与模型资源面临凭据驱动的直接滥用：**LiteLLM在野利用可导致模型配置和API密钥泄露，LLMjacking则利用长期AWS IAM密钥订阅并调用基础模型，攻击影响同时涉及数据、权限和云成本。

**AI降低恶意代码开发和社会工程门槛：**NodeStealer使用AI辅助扩展间谍功能，Claude可加速工控漏洞利用的跨设备适配，银狐还利用AI输出信任和仿冒DeepSeek网站增强木马投递效果。

───────────────────────────────────

## 四、安全建议

**强化AI Agent和开发工具执行边界：**升级Hermes Agent等受影响组件，禁止AI编程工具自动信任未知仓库配置，对Git状态刷新、Shell执行、文件访问和凭据读取实施最小权限，并对高风险工具调用增加人工确认。

**加强AI基础设施与云凭据安全：**及时修复LiteLLM相关在野漏洞，排查异常日志并轮换可能暴露的API密钥；避免使用长期高权限AWS IAM密钥，启用CloudTrail和Bedrock调用日志，监控异常模型订阅及推理费用。

**提升AI辅助攻击和恶意软件检测能力：**关注代码库批量读取、凭据管理系统访问、云密钥调用及自动化侦察循环；加强Python字节码分析、Telegram C2通信监测，并针对工控环境关闭非必要FTP服务、实施网络隔离和异常流量检测。

**强化AI输出和软件下载来源验证：**限制AI工具直接下载或执行外部文件，不依赖搜索结果、智能体推荐或仿冒品牌页面安装软件；对DeepSeek等AI产品仅使用官方渠道，并结合终端安全工具二次核验文件。

───────────────────────────────────

## 五、报告总结

本周AI安全风险体现出“AI增强攻击能力”与“AI基础设施自身暴露”并行发展的特征。AI和智能体框架已经能够加速侦察、凭据提取、攻击规划和漏洞利用适配，使传统勒索、间谍软件及工控攻击链的执行效率进一步提升。

同时，Hermes Agent、LiteLLM和AWS模型资源相关事件表明，代码仓库配置、Agent工具调用、模型API密钥和云身份凭据正在成为AI应用安全的关键控制点。组织需要将AI平台按照核心基础设施实施资产管理、权限隔离和持续监测。

此外，银狐仿冒DeepSeek官网的活动说明，攻击者正在利用用户对AI输出和品牌的信任实施恶意软件投递。企业在推进AI辅助开发和自动化应用时，应同步强化来源真实性验证、外部内容隔离和高风险操作审批。

───────────────────────────────────

## 报告说明

本报告由360威胁情报中心基于2026年8月29日至9月4日公开威胁情报整理形成，重点分析AI与智能体框架辅助勒索攻击、Cursor AI攻击规划、AI编程Agent恶意Git配置执行、LiteLLM在野漏洞利用、LLMjacking模型资源滥用、AI辅助间谍软件开发、Claude辅助工控漏洞移植及AI信任链钓鱼风险，为企业AI应用、开发环境、云模型服务、工业控制系统及安全运营防护提供参考。

**情报时效性：** 2026年8月29日—9月4日  **威胁评估等级：** 高风险（多源情报验证）

[## AI安全专题周报(20260828)

报告编号：TIC-202608-AI03
报告周期：2026年8月22日—8月28日
一、报告概述
基于360威胁情报中心对本期公开网络安全素材的整理与分析，本周AI安全风险主要集中在AI应用与Agent运行环境漏洞、提示注入和模型配置劫持、AI开发供应链攻击、AI增强型社会工程以及AI驱动自动化攻击等方向。相关事件显示，AI平台的联网接口、插件加载、代码执行、模型模板和第三方依赖正在形成相互关联的攻击面，AI能力也在向语音钓鱼和规模化凭证攻击延伸。
报告重点内容涵盖：
· AI应用与Agent执行环境风险：Langflow遭到在野利用，DeepSeek Harness可因提示注入与插件加载问题发生沙箱逃逸，暴露出AI平台接口、执行权限和隔离边界的现实风险。
· 模型与内容处理链路风险：恶意网页可借助DNS重绑定影响本地Ollama模型配置，隐藏HTML提示注入可静默篡改邮件摘要器输出，模型输入与配置完整性成为新的安全控制重点。
· AI开发供应链与衍生攻击风险：恶意npm包可投递带AI助手能力的远控木马，AI生成的虚假或恶意PoC增加了代码仓库投毒风险；AI语音冒充和](/aian-quan-zhuan-ti-zhou-bao-4/)

28 Aug 2026
13 min read

[## AI安全专题周报(20260821)

报告编号：TIC-202608-AI02
...