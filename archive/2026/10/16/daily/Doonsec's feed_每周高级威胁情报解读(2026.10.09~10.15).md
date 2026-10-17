---
title: 每周高级威胁情报解读(2026.10.09~10.15)
url: https://mp.weixin.qq.com/s/naybdIuxwMSaxO9YPgp4Hg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:33:05.723286
---

# 每周高级威胁情报解读(2026.10.09~10.15)

# 每周高级威胁情报解读(2026.10.09~10.15)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026.10.09~10.15

**攻击团伙情报**

* Kimsuky 的 GitPower 间谍行动针对乌克兰
* 疑似 TraderTraitor 利用植入木马的 Terraform Provider 投放跨平台恶意软件
* 与 UAC-0099 有关的 MATCHBOIL 窃密木马推出新变种
* UAT-6275团伙针对独联体多国政府与关键基础设施开展间谍活动

**攻击行动或事件情报**

* 一连串无认证攻击事件：Ivanti Connect Secure 零日漏洞链式利用
* Ledger证实钱包加密货币盗窃案背后存在间谍芯片植入
* 揭秘 Apex Accelerator 虚假 Web3 加速器，团伙包装合约安全审计服务发布恶意 npm 包
* 月蛾档案深度揭秘：还原 Silent Ransom 勒索团伙运营模式
* GhostAction卷土重来：恶意“安全审计”工作流程现在可以从整个Git历史记录中挖掘凭证

**恶意代码情报**

* ICMacOS 恶意软件演进：从 Mac 信息窃取木马升级为具备远程 Shell 的持久化 RAT
* 用户开机前手机已遭攻陷：Midnight Mimosa 恶意软件兴起
* Warden Stealer：快速崛起的信息窃取木马，专门掠夺 AI 智能体数据
* Unit 42 发现 PEERSTITCH：一款极其隐蔽的 FortiGate 防火墙植入后门

**漏洞情报**

* 微软补丁日通告：2026年10月版

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibTCgeDvH2dlqq8nNmJI2Q6ZFkIaDtLGlfibUwHOWbExSLMOBuRt5js7FdAQakV3AJXwMJTFg7csicCE5x9nRpXIWYOiawnicOUA2Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9gyGpemOib2IrhdYLGHuZXtzKMc5PLmsTpLBqicKvicEMBuiaW0s9dzwpxpwD0hYhibI6q7fwxkMO0mhOyYsPdNVNUiaqEOibEj0zJlc/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibkAGqMBECg08jYNOgkE0altRg3QCLyV24ic4wsWGZVjtjVX0jGMQJa4cribRHgDmYYcQ9ZOdiaaeFV1TTYbibia10zz6QOWKVUAmOA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9e7TWRefeUKclElvtvsWv2Z9xrX5FeA8e8OH6BickKl4NR8NV7kFUqXCd3OSgY0MuwgfjDKMgs0koto6JNvv3ibUTy8BwPiapfvM/640?wx_fmt=gif&from=appmsg)

**01**

**Kimsuky 的 GitPower 间谍行动针对乌克兰**

**披露时间：**2026年10月11日

**情报来源：**https://www.genians.co.kr/en/blog/threat\_intelligence/operation-gitpower

**相关信息：**

Genians安全中心发布报告，披露朝鲜关联组织Kimsuky通过Operation GitPower行动，将目标扩展至乌克兰外交、安全与国际政策专家。攻击采用回复诱饵式鱼叉钓鱼，冒充KCSCON 2026会议邀请或分析合作请求，首封邮件不含附件，待目标回复后才发送恶意压缩包。压缩包内LNK文件伪装成PDF，通过curl从GitLab下载first.ini并保存为VBE执行，再由help.ini收集systeminfo和Downloads目录信息，经硬编码令牌上传至GitHub仓库，并注册伪装成GoogleUpdateTaskMachineUA的计划任务实现持久化。攻击者还使用伪装成Zoom安装程序的可执行文件及GitHub上的PowerShell加载器。基础设施和代码与先前Operation GitPower高度相似，包括wolf字符串混淆、GoogleUpdateTaskMachineUA任务名及GitHub Contents API。研究人员还发现针对日本目标的诱饵文档，表明攻击范围扩大。Kimsuky可能意图收集朝鲜军队损失、战俘处理及韩乌协商情报。

**02**

**疑似 TraderTraitor 利用植入木马的 Terraform Provider 投放跨平台恶意软件**

**披露时间：**2026年10月08日

**情报来源：**https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver

**相关信息：**

Zscaler ThreatLabz发现疑似朝鲜背景APT组织TraderTraitor利用木马化的Terraform供应商包发起跨平台恶意软件攻击。该伪装成AWS供应商的二进制文件在Terraform加载时即执行恶意代码，通过仿冒HashiCorp域名下载Bash加载器，该加载器依据操作系统和CPU架构，将加密可执行文件伪装成.woff字体文件，经Base64解码与AES-256-CBC解密后部署Rust编写的FLATROOF后门，其内置Python窃密脚本专门窃取浏览器凭据、Cookie、终端历史及MetaMask等加密货币钱包数据，随后投放ROOFDECK后门实现完全远程控制，后者采用本地配置、带RSA签名的Pastebin死信箱及Nostr元数据的多层方式隐藏C2地址以规避检测。研究显示此类攻击手法与此前KelpDAO事件高度重合，但因缺乏独立代码及基础设施证据，尚无法高置信度归因于TraderTraitor。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq8icTHj2OlZmteytHVzjOdqPKAq9kqnJQ5NNiaubuIDiafaqa57lQOy8K2ibItXqtSbNCbDBvLRmC2jYicbaajUiaoKgYWic7RzicLoNhw/640?wx_fmt=png&from=appmsg)

**03**

**与 UAC-0099 有关的 MATCHBOIL 窃密木马推出新变种**

**披露时间：**2026年10月08日

**情报来源：**https://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/

**相关信息：**

ESET研究人员梳理了俄罗斯支持背景的网络间谍组织UAC-0099所使用的MATCHBOIL下载器从2024年4月至2026年4月近两年间的演变历程。该组织长期针对乌克兰政府、金融机构及媒体，并可为Sandworm组织提供初始访问。MATCHBOIL通过鱼叉式钓鱼邮件中的恶意链接传播，以VBScript下载执行，负责从C&C服务器下载并持久化MATCHWOK后门。研究显示，尽管该恶意软件直至2025年8月才被公开披露，但其开发最早可追溯至2024年4月。各版本迭代持续增强：混淆方式从不可打印Unicode字符与字符串加密升级为Eziriz .NET Reactor混淆器，并新增了通过Windows事件日志系统运行时间判断沙箱环境、调试器检测等反分析手段。此外，其执行逻辑由一次性下载器转变为通过定时器每两分钟轮询C&C以获取最新载荷，持久化机制也在注册表Run键与计划任务之间多次切换。为迷惑受害者，新版本还添加了日程规划器等图形界面伪装。最新变体MATCHBOIL.V2已改为DLL形式并由自定义C#加载器执行，进一步增加了系统安装日期检测等虚拟机识别手段。

**04**

**UAT-6275团伙针对独联体多国政府与关键基础设施开展间谍活动**

**披露时间：**2026年10月14日

**情报来源：**https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations/

**相关信息：**

Cisco Talos联合Recorded Future披露APT组织UAT-6275针对独联体国家政府机构的间谍行动。该组织自2025年6月至2026年8月活跃，目标覆盖哈萨克斯坦、塔吉克斯坦、亚美尼亚、白俄罗斯等九国，重点瞄准外交、经济及水资源与能源管理部门，其活动时间与地区外交会议及俄乌战争引发的能源安全议题高度相关。攻击采用四种感染链，包括宏文档、PS2EXE下载器、GitHub托管的PowerShell脚本以及利用WinRAR漏洞CVE-2025-8088的恶意压缩包，投递Chvost、Laplas、PickleShell等轻量级反弹Shell。该组织三处公开可访问的暂存目录及GitHub仓库的提交历史意外暴露了其载荷构建与基础设施变更。研究人员还发现了针对Linux主机及FortiWeb漏洞的利用工具，显示其能力正在扩展。基于基础设施访问、语言痕迹、样本提交来源及符合UTC+5时区的工作时间分析，Talos以中等置信度评估该组织与哈萨克斯坦存在关联，该活动集群与YoroTrooper等已知行动存在重叠但尚未观察到直接工具共享。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqiciaXZNcf83VL0w2Lg9iaJbiazyFrcrAQiblaJicN057qEunIYQDWjmMvibY2gVPia5iadFgcyzjFSyxWePRU6qYxSlUt2ES9JKF6axiczA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqib2iaEf70LiboLVlYOpRUsWUDCK646AyzJrYPC9LB8XCZaNdKpIT1oF3I3ibtndxDsfqjNZJ9GNBictRl3lkiaQJYiad8w6udYphk3ZU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8FElbtLw06yukd5U2o1701LAgryyq875qPyDe6QlmAAKUBfNeMibnNu1bxm6gc1m8FzxmiaeG8Ih8wLxCNUjej4TqAWWxqSEYoE/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9h3t5a0QfKiaKPCWXMfHo9ppXbvaAyAN5EuqX2VHQmbR8swRibXd3LAnbx5jiaiay7iafuocJg0bQicgk9S1qquKjkeY4Kib5Je0LgVU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8g3BpNZkFUnCpQvBEJDlBN1kvarc58IUTxZk9Me1ujZ6O5XBVlCAQOPibeyucDV9BAb7ibBLRvhkHZxWf8Txt3pVu9QyTFzns4c/640?wx_fmt=gif&from=appmsg)

**01**

**一连串无认证攻击事件：Ivanti Connect Secure 零日漏洞链式利用**

**披露时间：**2026年10月13日

**情报来源：**https://labs.zenity.io/post/rogue-ai-agents-abuse-urlquery-remote-browser-execution-to-extract-russian-government-data

**相关信息：**

Volexity披露未知威胁者UTA0576利用Ivanti Connect Secure VPN三个零日漏洞链，实现未认证root级远程代码执行。漏洞包括welcome.cgi认证绕过、wu.cgi文件写入竞态条件RCE，以及通过篡改DSCache配置让dsinvoked以root执行Perl的提权。攻击者未部署后门或webshell，所有命令和结果均通过漏洞利用的HTTPS请求传递。利用后窃取域凭据、AD元数据、LAPS密码和BitLocker恢复密钥，部署Kerberos和LDAP工具，进行密码喷洒和LDAP流量抓包，并清除调试与审计日志、恢复内存补丁。受影响版本至22.8R2.4。Ivanti已修复认证绕过和RCE，编号CVE-2026-104935，提权修复稍后发布。建议打补丁、监控welcome.cgi和X-DSCGI-PATH异常、内存取证。Volexity中置信度认为UTA0576可能使用LLM辅助开发。

**02**

**Ledger证实钱包加密货币盗窃案背后存在间谍芯片植入**

**披露时间：**2026年10月12日

**情报来源：**https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/

**相关信息：**

Ledger确认，部分通过东南亚经销商CryptoBilis销售的硬件钱包被植入恶意硬件，导致用户加密货币被盗。至少一台设备含未授权硬件植入物，公司已要求CryptoBilis暂停销售和发货，并建议近90天购买者未初始化则不要设置，已设置则转移资产至新助记词钱包。研究人员在Ledger Nano X中发现植入物隐藏于屏幕后方，通过采集显示输出和按键获取助记词，再经带eSIM的LTE模块外传。植入物使用STM32G431KBU6微控制器和微型eSIM，通过更换更小电池或利用屏幕下泡沫垫空间容纳。第二个变体更先进，使用原装电池，天线沿顶部边缘走线成为明显破绽。部分元件标识被刮除，PCB为工厂定制而非手工焊接。Ledger的正品检查无法检测此类植入物，因为原安全元件仍完好。公司正与执法部门合作调查，并警告用户避免从非授权经销商购买。

**03**

**揭秘 Apex Accelerator 虚假 Web3 加速器，团伙包装合约安全审计服务发布恶意 npm 包**

**披露时间：**2026年10月12日

**情报来源：**https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages

**相关信息：**

Elastic Security Labs 揭露 REF8801 行动，攻击者伪装成 Web3 加速器 Apex Accelerator，通过恶意 npm 包 @apexacc/cli 和 @apexacc/audit 针对加密货币初创公司创始人。这些包以 AI 编码助手和安全审计工具为名，安装时从 GitHub 下载平台特定可执行文件，并通过 vrf.apexaccs[.]org 获取命令执行。macOS 端投递 CloudSyncD 后门，Windows 端投递信息窃取器，经 Telegram 外泄数据。攻击者还重新打包合法编码代理 Oh My Pi，将 OpenRouter 流量重定向至其服务器，注册恶意 MCP 服务器，可窃取提示、代码和工具输出并影响代理行为。所有 18 个审计工具返回硬编码伪造结果，远程评分服务对虚构项目返回 51/100。该行动通过虚假网站、会议活动、伪造评论和 AI 生成内容制造可信度。

**04**

**月蛾档案深度揭秘：还原 Silent Ransom 勒索团伙运营模式**

**披露时间：**2026年10月09日

**情报来源：**https://blog.checkpoint.com/security/how-luna-moth-runs-data-extortion-like-a-business/

**相关信息：**

Check Point 基于暗网流出的 “Luna Moth Files（月蛾档案）” 泄露材料，还原 Silent Ransom Group（SRG，Luna Moth/UNC3753）的犯罪运营模式；该团伙 2022 年从 Conti 集团分裂，属于封闭独立团队，不使用文件加密，仅依靠窃取敏感数据实施勒索；以语音钓鱼冒充 IT 运维为主要入侵手段，甚至物理上门获取访问，优先攻击美国律所，内部台账记录累计勒索金额 2.07 亿美元；团伙全程滥用合法远程工具，无自定义恶意载荷，传统勒索病毒检测很难发现。

**05**

**GhostAction卷土重来：恶意“安全审计”工作流程现在可以从整个Git历史记录中挖掘凭证**

**披露时间：**2026年10月09日

**情报来源：**https://www.stepsecurity.io/blog/ghostaction-returns

**相关信息：**

StepSecurity报告GhostAction供应链攻击回归。2026年10月8日，攻击者利用两个被入侵的维护者账户，向345个仓库推送伪装成安全审计的恶意GitHub Actions工作流。新变种除窃取仓库命名密钥外，还以fetch-depth 0检出全部历史，用git log -p --all扫荡工作树和整个git历史，搜索AWS、Anthropic、OpenAI、GitHub、GitLab、Slack、SendGrid等13类凭据，捕获AWS密钥上下文配对，并将全部数据明文POST到硬编码IP 193.32.204.199。uber/athenadriver确认外泄成功，pyxel被手动重跑五次，typecho-fans因工作流需审批而未执行。截至10月9日仍有378个仓库带活跃恶意工作流。修复须轮换所有Actio...