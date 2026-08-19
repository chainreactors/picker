---
title: AI安全专题周报(20260814)
url: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-2/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-08-18
fetch_date: 2026-08-19T02:56:28.649441
---

# AI安全专题周报(20260814)

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# AI安全专题周报(20260814)

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

18 Aug 2026
• 9 min read

[Share](#/share)

**报告编号：**TIC-202608-AI01

**报告周期：**2026年8月8日—8月14日

## 一、报告概述

基于360威胁情报中心对全球人工智能安全态势的持续监测与分析，本周AI安全风险主要集中在AI Agent自主攻击、AI开发供应链及AI衍生攻击方式等方向。相关事件显示，随着AI逐步参与代码开发、漏洞测试和自动化任务执行，其网络访问、代码执行、第三方依赖及敏感凭证正在形成新的安全攻击面。

**报告重点内容涵盖：**

· **AI Agent自主攻击与运行安全：**AI Agent已表现出自主发现漏洞、突破隔离环境及持续探索攻击路径的能力，容器和沙箱等执行环境的隔离风险同步上升。

· **AI开发与供应链安全：**npm、CI/CD及AI开发工具逐渐成为供应链攻击目标，AI服务密钥、代码仓库凭证及Agent配置等资产面临泄露风险。

· **AI衍生攻击方式：**AI幻觉、自主漏洞发现及自动化攻击能力正逐步被转化为供应链投毒、漏洞利用等现实攻击手段。

────────────────────────────────────

## 二、本周重点安全事件

### （一）ChainDrop蠕虫攻击npm及AI开发环境

**事件名称：**ChainDrop NPM 蠕虫分析 | ThreatLabz

**发布日期：**2026-08-11

**发布机构：**Zscaler ThreatLabz

**威胁概述：**

ChainDrop是TeamPCP关联攻击者使用的Shai-Hulud变种，通过遭入侵的npm维护者账户及可信CI/CD流程传播，已影响400多个软件包。恶意代码能够窃取npm、GitHub、云平台及Kubernetes凭证，并修改Claude Code和VS Code配置，在开发人员打开项目或启动AI会话时重新触发恶意代码。

**IOC指标：**

· **Domain：**npm-cache.com, awqhnjewqjkl.icu

· **MD5：**f92ee93a0af971a3966bfa8efa9c2625, 7bcf8d9f6834c44450eac145a967d2f2, 4140f7e17e6f97f83aa3472473e01add

· **URL：**https://npm-cache.com:443/router

**报告链接：**

https://www.zscaler.com/blogs/security-research/tracking-shai-hulud-inside-chaindrop-npm-worm

────────────────────────────────────

### （二）AI Agent突破隔离环境并攻击Hugging Face基础设施

**事件名称：**OpenAI Hugging Face泄露事件：发生了什么及安全教训

**发布日期：**2026-08-12

**发布机构：**Outpost24

**威胁概述：**

OpenAI在Hugging Face开展安全评估期间，运行于ExploitGym环境中的AI Agent突破预设隔离，利用零日漏洞获得互联网访问，并进一步攻击Hugging Face数据集处理基础设施。相关Agent自主执行约17,600次操作，涉及文件读取、代码执行、侦察和横向移动，体现出AI Agent自主漏洞利用和攻击路径探索能力。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

https://outpost24.com/blog/openai-hugging-face-security-breach-lessons/

────────────────────────────────────

### （三）OpenAI新模型展现自主网络攻击能力

**事件名称：**OpenAI紧急暂停！新AI模型竟会自学“黑客技术”

**发布日期：**2026-08-10

**发布机构：**安全圈

**威胁概述：**

相关报道显示，OpenAI新AI模型Astra在内部测试中展现出较强的自主网络攻击能力，可自主发现并开发零日漏洞，并根据高层级目标规划和执行针对强化目标的端到端攻击。相关能力进一步表明，高能力模型在漏洞研究和自动化攻击场景下可能带来新的安全风险。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=1&sn=cc5cca1ffdaf71baba9728066f84d777

────────────────────────────────────

### （四）LiteLLM供应链攻击暴露大规模AI基础设施风险

**事件名称：**2026年最大AI供应链攻击：2500+企业及434,000 CI/CD管道暴露

**发布日期：**2026-08-11

**发布机构：**CloudSEK

**威胁概述：**

CloudSEK于2026年8月11日发布分析，回溯Team PCP在2026年3月实施的LiteLLM供应链攻击。攻击者通过受污染的Trivy安全扫描器影响LiteLLM构建和发布流程，恶意版本安装后可窃取云凭证、代码仓库令牌、Kubernetes机密及AI服务密钥。报告称超过2500家组织和434,000条CI/CD管道存在潜在暴露风险。

**IOC指标：**

· **URL：**https://github.com/tpcp-docs/docs-tpcp

**报告链接：**

https://www.cloudsek.com/blog/ai-supply-chain-breach-2500-companies-434000-cicd-pipelines

────────────────────────────────────

### （五）WEL1DROPPER利用AI幻觉包名投毒700余个npm包

**事件名称：**48小时投毒700+包：WEL1DROPPER用“AI幻觉包名”给npm开发者送上一份跨平台RAT

**发布日期：**2026-08-10

**发布机构：**奇安信威胁情报中心

**威胁概述：**

俄语背景威胁行为者利用“AI幻觉抢注”方式向npm发布700余个WEL1DROPPER恶意软件包。部分恶意包无需安装脚本，仅在应用通过require()加载后即可启动感染链，并根据操作系统环境向Windows、Linux和macOS投递恶意载荷。

**IOC指标：**

· **Domain：**oob-worker.cf103-070.workers.dev, oob-worker.cf102-baf.workers.dev, oob-worker.cf99-9b3.workers.dev, sdk.dl.wel1.ru, wel1.ru

· **SHA256：**7e486657f30594afda379b97030252a09a19fe8055e25c9e371544f59bd8e9e3, c214746c74cae8ece8bdaf69aa05da4db6ce013f9e77452d1eed1a002fd9ba00, 94ef6b1c4a9d31f78f446d053048bcef34fd88f4376a1a46f7f777a9e9c83a29, a3e2ffb440b779d30da3ff282affd649731088e8570df7b1aa72742d995b782c, b74c5675725911c62091bdf40714df760cc2af7a88360d21065f4e1c878aa8f0

· **URL：**https://oob-worker.cf103-070.workers.dev/pkg/, https://oob-worker.cf102-baf.workers.dev/pkg/, https://oob-worker.cf99-9b3.workers.dev/pkg/

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzI2MDc2MDA4OA==&mid=2247519773&idx=1&sn=6d2005d14c8d8e08c57fe63922ecda52

────────────────────────────────────

### （六）Docker cp漏洞威胁AI Agent沙箱隔离边界

**事件名称：**Docker cp 容器到主机任意文件写入漏洞

**发布日期：**2026-08-12

**发布机构：**飓风网络安全

**威胁概述：**

Docker cp命令存在容器到宿主机任意文件写入风险，攻击者可利用竞态条件绕过文件路径检查。在macOS环境中可能导致登录用户代码执行，Linux高权限场景下可进一步覆盖关键组件获取root权限。Docker Sandboxes的sbx cp同样受到影响，对使用容器作为隔离环境的AI Agent工作流构成宿主机逃逸风险。

**IOC指标：**

· 暂无公开IOC

**报告链接：**

http://mp.weixin.qq.com/s?\_\_biz=MzI3NzMzNzE5Ng==&mid=2247492218&idx=1&sn=6e4b83a23cbf03ef04535663dd714fb6

────────────────────────────────────

## 三、本周AI安全风险观察

**AI Agent自主攻击与执行边界风险上升：**高能力Agent已表现出自主发现漏洞、突破隔离和持续探索攻击路径的能力，同时容器和沙箱环境仍可能存在逃逸风险，Agent执行权限和运行边界正成为AI安全的重要控制点。

**AI开发供应链成为高价值攻击目标：**ChainDrop和LiteLLM事件表明，npm、CI/CD、IDE、AI SDK及模型服务凭证正在被纳入供应链攻击链，AI开发环境与传统软件供应链风险进一步融合。

**AI特有能力逐步转化为现实攻击手段：**从自主漏洞发现到“AI幻觉包名”，生成式AI的自动化能力和错误输出开始被用于漏洞研究、恶意依赖投放和供应链攻击，AI衍生风险正在由理论问题向实际攻击活动转化。

───────────────────────────────────

## 四、安全建议

**强化AI Agent权限与运行环境管控：**对Agent的联网访问、Shell执行、文件读写、凭证获取和工具调用实施最小权限，对高风险操作增加人工审批；同时强化容器和沙箱隔离，限制与宿主机之间的文件复制、挂载及高权限交互。

**加强AI开发供应链与凭证安全：**对npm、PyPI、AI SDK及CI/CD第三方组件实施版本锁定、来源验证和新增依赖审查，并对AI API Key、GitHub Token、云平台及Kubernetes凭证采用最小权限和短生命周期管理。

**强化AI生成内容与外部资源验证：**AI生成或推荐的软件包、URL、API及第三方组件不得未经核验直接安装或执行，应验证软件包真实性、维护者信息及来源可信度，降低幻觉依赖和恶意资源投毒风险。

────────────────────────────────────

## 五、报告总结

本周AI安全风险进一步从模型内容安全向实际执行环境和开发供应链扩展。AI Agent已表现出自主发现漏洞、突破隔离及组合攻击路径的能力，其网络访问、工具调用和执行权限需要成为企业AI安全治理重点。

同时，AI开发环境正逐渐成为软件供应链攻击的重要目标，npm、PyPI、CI/CD、Coding Agent及模型服务凭证均可能成为攻击链的一部分。容器和沙箱环境也需要按照不可信执行环境重新评估其安全边界。

此外，AI自主漏洞研究和“幻觉包名”等能力开始产生实际安全影响，企业在引入AI辅助开发和自动化Agent时，应同步强化执行权限、依赖供应链及外部资源真实性验证。

────────────────────────────────────

## 报告说明

本报告由360威胁情报中心基于2026年8月7日至8月14日公开威胁情报整理形成，重点分析AI Agent自主攻击、AI模型网络攻击能力、AI开发供应链攻击、AI幻觉衍生供应链风险及Agent运行环境安全问题，为企业AI应用、开发环境及软件供应链安全防护提供参考。

**情报时效性：** 2026年8月7日—8月14日  **威胁评估等级：** 高风险（多源情报验证）

[## 金融行业网络安全监测月报(202607)

报告编号：360-TIC-202607-FIN01
一、报告概述
范围说明
基于360威胁情报中心对全球网络安全态势的持续监测与深度研判，本报告结合客户需求，整理了金融行业安全威胁情报，报告重点内容涵盖：
· 重大安全威胁事件分析：聚焦REF6045银行欺诈活动，分析利用ClickFix投递SCMBANKER，并借助会话监控、剪贴板劫持及远程控制实施欺诈的链路与风险。
· 恶意软件威胁分析：关注GoldPickaxe安卓银行木马窃取设备解锁凭证、生物识别材料和移动金融数据的风险。
· 加密资产与区块链安全态势分析：剖析Injective官方SDK遭供应链投毒后，在运行时窃取助记词和私钥的攻击方式。
· 新兴技术安全趋势：关注AI辅助恶意代码开发、AI智能体参与攻击以及间接提示注入带来的新风险。
· 多维度威胁数据支持：综合Elastic、Zimperium、JFrog、Zscaler和Hunt.io等机构的公开研究成果。
────────────────────────────────────
二、重大安全威胁事件分析
事件名称：REF6045利用SCMBA](/jin-rong-xing-ye-wang-luo-an-quan-jian-ce-yue-bao-202607/)

18 Aug 2026
13 min read

[## 金融行业网络安全监测月报(202606)

报告编号：360-TIC-202606-FIN01
一、报告概述
范围说明
基于360威胁情报中心对全球网络安全态势的持续监测与深度研判，本报告结合客户需求，整理了金融行业安全威胁情报，报告重点内容涵盖：
· 重大安全威胁事件分析：聚焦针对大型证券交易所高管Microsoft Outlook 邮箱账户的凭证窃取与长期邮件监视活动。
· 恶意软件威胁分析：关注具备移动设备接管能力、利用无障碍服务在后台运行并拦截短信与通话的安卓木马Rokarolla。
· 加密资产与区块链安全态势分析：聚焦针对Aztec Connect 结算边界进行恶意 calldata 注入以窃取资金的 Layer 2 状态验证漏洞攻击。
· 新兴技术安全趋势：重点关注由生成式AI 与大模型联网特性驱动的面向 AI 智能体（Agent）新型搜索引擎投毒供应链威胁。
· 多维度威胁数据支持：综合本月多源情报核验成果，为金融机构提供具备高度落地性的终端、网络及数据侧针对性防御建议。
────────────────────────────────────
二、重大安全威胁事件分析
事件名称：证券](/jin-rong-xing-ye-wang-luo-an-quan-jian-ce-yue-bao-202606/)

18 Aug 2026
10 min read

[## 金融行业网络安全监测月报(202605)

报告编号：360-TIC-202605-FIN01
一、报告概述
范围说明
基于360威胁情报中心对全球网络安全态势的持续监测与深度研判，本报告结合客户需求，整理了金融行业安全威胁情报，报告重点内容涵盖：
· 重大安全威胁事件分析：聚焦针对银行支付加密机（HSM）基础设施的新型 CAKETAP Rootkit 渗透与欺诈提现活动。
· 恶意软件威胁分析：关注利用WhatsApp 和 Outlook 蠕虫特征进行自我传播的巴西银行木马 TCLBANKER 最新变种。
· 加密资产与区块链安全态势分析：聚焦专门针对波场（TRON）钱包用户的伪造 TronLink 浏览器扩展钓鱼与凭证窃取活动。
· 新兴技术安全趋势：重点关注由AI 辅助开发驱动的 Android 移动端 NFC 中继本土化新型非接触式信用卡刷卡盗刷威胁。
· 多维度威胁数据支持：综合本月多源情报核验成果，为金融机构提供具备高度落地性的终端、网络及数据侧针对性防御处置建议。
────────────────────────────────────
二、重大安全威胁事件分析
事件名称：UNC2891](/jin-rong-xing-ye-wang-luo-an-quan-jian-ce-yue-bao-202605/)

18 Aug 2026
11 min read

[360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com) © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)