---
title: 每周高级威胁情报解读(2026.10.23~10.29)
url: https://mp.weixin.qq.com/s/WJ72urVlkQDElPI45PkSeg
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:18.732409
---

# 每周高级威胁情报解读(2026.10.23~10.29)

# 每周高级威胁情报解读(2026.10.23~10.29)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026.10.23~10.29

**攻击团伙情报**

* MythicRatatoskr 新型后门：滥用 Yggdrasil 去中心化网状网络搭建隐蔽 C2
* APT-C-36组织使用新型RAT开展攻击活动
* 奇安信发布《网络安全威胁2026年中报告》
* APT28（Swallowtail）入侵北约海军造船厂潜伏两个月
* 未知 APT 团伙利用 NetamLoader 攻击亚洲政府专用定制版 Win10

**攻击行动或事件情报**

* 遗忘的 Popcorn Time 更新程序，让数百万设备面临劫持风险
* 深度解析 LiteLLM 1.107.0 供应链攻陷事件：借助 Python 启动钩子窃取凭据
* 灰色 AI 中转劫持 Codex/Claude Code
* 追踪朝鲜威胁团伙在攻击手法中对 AI 的应用

**恶意代码情报**

* 揭秘 Sirius 后门：伪装成联邦快递（FedEx）发票的多阶段无文件攻击行动
* 窃取木马搭上 AI 快车：Aokigahara 信息窃取器专项分析
* NIK C2：新型搭载 AI 能力的命令控制框架
* Doorway 僵尸网络：大规模 IoT 与网络设备入侵活动深度解析

**漏洞情报**

* 高危 “HTTP2Shell” Brotli 漏洞，厂商紧急发布补丁

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8Evgo5ZeZTzgQTQiapkAwalGxYLMnpDQjmhkDzX3iaDhaeCic1oabt6GxR8Zs10bTHPrhmFHzibHoge5MKRSwicic1iaGPMwh1may2w8/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq99FzzkU3hD64lnp6ZBjK64HcLDt0YpeyQI0NuGhF7ZA3uP3VKEtEANYSTQpiaiaSCo9zd2SXDXkM8pbvfJ16DvYGEkZ94AE4ibL8/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqib4SuXu2ibh1CrHkDPEzib6xSmxmsp5517ib0koO7FWVp0OVibx01iapMnT0obDOETzib5FAFGb467paicMibx4VtRIsIaIvsxbLcpUGIk/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9GeXz9BNAYHU6LnrqtdNHHHfbgO13YqRqtsoHdrxLH9rgiag3P5bq7ibsxhyyP7cQq31zQUlQA96hrCYFYLpXUWDoRbR16uXCibI/640?wx_fmt=gif&from=appmsg)

**01**

**MythicRatatoskr 新型后门：滥用 Yggdrasil 去中心化网状网络搭建隐蔽 C2**

**披露时间：**2026年10月22日

**情报来源：**https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/

**相关信息：**

ESET披露一起俄罗斯支持背景威胁组织间的协作事件：UAC-0099于2025年7月16日通过钓鱼邮件及恶意附件获取乌克兰一家粮食物流公司初始访问权限，部署已知工具链MATCHBOIL与MATCHWOK，次日投放此前未记录的Go语言后门MythicRatatoskr。该后门创新性地利用Yggdrasil去中心化网状网络隐藏其命令控制服务器，随机选择三个公共节点接入网络，通过端到端加密IPv6通信，可执行文件传输、截屏、命令执行及反向SOCKS5代理等操作，配置还暗示存在Linux版本。约两个月后，Sandworm通过Active Directory组策略部署SDelete工具实施数据擦除攻击。研究人员以中等置信度评估UAC-0099充当初始访问中介，此为首次记录国家级威胁行为者滥用Yggdrasil网络的案例，或预示对手采用实验性点对点网络以增强基础设施韧性与隐蔽性的趋势。

**02**

**APT-C-36组织使用新型RAT开展攻击活动**

**披露时间：**2026年10月27日

**情报来源：**https://mp.weixin.qq.com/s/Wmw5\_LMYXv3ROxecNAh-gg

**相关信息：**

360披露APT-C-36盲眼鹰于2026年8月针对哥伦比亚等南美目标发起攻击，以伪装哥伦比亚国家总检察院的SVG钓鱼文件诱导点击，打开伪造下载页并投放加密ZIP，内含多层混淆的JS加载器，继而释放VBS和PowerShell，利用AES、Base85和Gzip还原.NET程序集，通过系统调用和进程镂空注入RegSvcs.exe，最终加载新型远控Evolution RAT。该RAT具备HVNC隐藏桌面、注入浏览器DLL并挂钩文件API、克隆并窃取Chrome等浏览器登录与Cookie、键盘记录、远程Shell、文件管理、麦克风监听和反向代理等能力。360依据司法主题SVG诱饵和多脚本混淆手法将其归因于盲眼鹰，并指出其攻击复杂度提升。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicgORhql59FUK5bicd8cGwJXicGX7cSCkeiaME1kREWcuAXr50uJeEsJoDPwfTJCBUPw33iawGLSL2jDVdrCYFppeusCw9xFIV8dNo/640?wx_fmt=png&from=appmsg)

**02**

**奇安信发布《网络安全威胁2026年中报告》**

**披露时间：**2026年10月29日

**情报来源：**https://mp.weixin.qq.com/s/XGUSwR2LeUpeDVJdVyRQgw

**相关信息：**

《网络安全威胁2026年中报告》基于奇安信威胁雷达测绘数据、红雨滴团队真实攻击处置线索、威胁情报全线产品告警数据以及全球公开威胁情报，对上半年的高级持续性威胁、勒索攻击、互联网黑产、漏洞利用和新型安全风险进行了系统梳理。报告共收录199篇高级威胁类公开报告，涉及84个已命名的攻击组织或攻击行动，至少63个国家和地区遭遇过APT攻击，为读者还原了一幅完整的全球网络威胁地图。

**04**

**APT28（Swallowtail）入侵北约海军造船厂潜伏两个月**

**披露时间**：2026年10月28日

**情报来源：**https://www.anomali.com/blog/apt28-spent-2-months-inside-a-nato-naval-shipbuilder-and-left-behind-a-loader-nobody-had-seen-before

**相关信息：**

Anomali披露APT28即俄军第26165单位入侵北约海军造船厂并潜伏至少两个月，属Swallowtail行动，另针对执法机构和军机发动机厂商。攻击者7月24日经Outlook附件缓存打开混淆宏文档，投递Hookedge后门，借隐藏离屏Edge连接webhook.site后改用专用C2，7月27日人工连发7项任务。其以SSH反向隧道和PowerShell回环假HTTP监听经SMB-over-HTTP捕获NTLMv2双路径窃取凭证，再部署未见公开记录的反射加载器Id.exe，在内存解密加密载荷并调用ExecuteLoader，但Events.dat未回收，基础设施活跃至9月24日。建议检测隐藏Edge外联、webhook.site、回环NTLM和SSH -R，发现Hookedge迹象应视为攻击仍在进行。

**05**

**未知 APT 团伙利用 NetamLoader 攻击亚洲政府专用定制版 Win10**

**披露时间：**2026年10月29日

**情报来源：**https://securelist.com/netamloader/121676/

**相关信息：**

卡巴斯基披露未知APT利用NetamLoader攻击亚洲政府专用定制Windows 10，样本于2026年上半年发现，CAB包置于系统更新目录，内含微软签名的Patch My PC组件和恶意配置，借AppDomainManager注入加载签名程序集，再经fabric.config触发ResXResourceSet解析，利用BinaryFormatter反序列化和TypeConfuseDelegate执行XAML，通过多层压缩加密载荷绕过AMSI并清理更新与预取日志，随后用RPC创建dllhost.exe远程COM对象执行XAML-3和.NET插件，通信采用AES-CBC与HMAC-SHA256并长时间轮询Cloudflare承载的openaiqpt4v.com。目前仅确认亚洲一个受害者，无法归因已知APT，文章强调自主操作系统供应链面临暴露风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicD0y4wt8vuwQNXl0Enib7iaBKeEPEuMEibpnkv3ob4yicIOasnUqmW71Jc8kaStgeA0RdKo6M3U8ACWWLHj3F4JV784MibHmZFZoho/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9ZvUicIQNts4LQcYQgCn26t3N1Q39pqPCnehBUrR4GS9tfyqX9qFg9hb7Dlzm8dCicehBFu2LxkXibypN60LVIy6icFtFQ4fLyljg/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8ZmESkiaoZiaMVdr12ic58JWcufQPPyrk8jkjRr9hPtxbJtCJzK8XqupEZ41XeugUdBtxDVoLDVWlByBibW8LISOB6h35VnUAA4icY/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibYIkCRhFNn05nygyAhncDOd4NWQ7LbeMaQH6UhicbibGk9r6k7nzEI64HJh1XBibFRakF1tSzLxtYsZLVTH1jkpHQLRm7AnCYgZI/640?wx_fmt=gif&from=appmsg)

**01**

**遗忘的 Popcorn Time 更新程序，让数百万设备面临劫持风险**

**披露时间：**2026年10月26日

**情报来源：**https://www.malwarebytes.com/blog/news/2026/10/popcorn-times-forgotten-updater-left-millions-of-devices-exposed-to-hijacking

**相关信息：**

Malwarebytes报道，已废弃的Time4Popcorn更新器通过未加密HTTP且不验证签名接受可执行更新，弃用域名可被注册，构成CVE-2026-30612远程代码执行漏洞，攻击者无需用户打开应用即可静默控制Windows和macOS设备，估计影响250万至350万台Windows和25万至35万台Mac。Android安装APK需用户批准。Eye Security注册域名并下发禁用更新器的更新，下载逾200万次，请求降98%，后将15个域名移交Shadowserver。桌面应用另有2014年旧Chrome引擎和禁用沙箱等弱点。建议检查卸载旧版Popcorn Time或Time4Popcorn，Windows检查Updater.exe与Update Service，macOS检查PT.updd及启动守护进程，Android直接卸载，并使用实时反恶意软件防护。

**02**

**深度解析 LiteLLM 1.107.0 供应链攻陷事件：借助 Python 启动钩子窃取凭据**

**披露时间：**2026年10月23日

**情报来源：**https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/

**相关信息：**

微软分析LiteLLM 1.107.0供应链事件，恶意wheel和镜像含cook.pth、cook.py、sitecustomize.py，安装后普通Python启动即经站点初始化执行，无需导入LiteLLM。载荷收集开发者与AI工具凭证、Git和包管理器配置、云与Kubernetes凭证、浏览器数据、SSH/GPG/TLS私钥、进程环境及LiteLLM代理数据库记录，经AES-256-CBC和RSA-OAEP封装后上传litellm.dev/healthcheck；Unix加载器还可从GitHub读取域名指针并下载执行远程Python代码，但未确认。微软建议不要用可疑环境的Python或pip排查，应隔离主机和容器，清除启动文件并重建，轮换所有可达凭证，限制出站，结合文件哈希、进程链、加密暂存和网络目的关联研判，并使用Defender检测与狩猎查询。

**03**

**灰色 AI 中转劫持 Codex/Claude Code**

**披露时间：**2026年10月29日

**情报来源：**https://www.security.com/threat-intelligence/openai-claude-unauthorized-relays

**相关信息：**

Symantec 披露灰色非授权 AI 中转服务，面向国内及东亚跨国企业研发人员，在用户安装正版 OpenAI Codex、Anthropic Claude Code CLI 之后，通过无文件脚本篡改配置，将沙箱设置为 `danger-full-access` 放开执行与网络权限，并把所有 AI 流量劫持到第三方中转服务器；虽然目前暂无运营方主动作恶证据，但中转节点可全量窃取对话、源码和密钥，也可篡改 AI 返回内容下发恶意命令，风险极高。

**04**

**追踪朝鲜威胁团伙在攻击手法中对 AI 的应用**

**披露时间：**2026年10月29日

**情报来源：**https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/

**相关信息：**

微软追踪朝鲜威胁行为者的AI采用情况，评估总体采用度高，并划分为新兴、扩展、加速和运营化四阶段。Jade、Coral、Jasper已运营化，Diamond、Onyx、Pearl、Sapphire处于加速阶段，Emerald处于扩展阶段。AI被用于目标侦察、生成定制钓鱼诱饵和虚假身份、制作简历与面试回答、辅助代码及恶意工具开发、总结受害信息并加速决策。Jade一周内通过三家前台公司开展活动，Onyx数分钟生成数十份诱饵，Coral快速开发私有代码仓库木马化能力，Diamond借AI增强定向与虚假公司建设，Onyx和Pearl使用ARTEX。微软评估相关活动仍由人类主导，尚未完全自主，目的仍是创收、情报收集及政治破坏，重点针对加密货币金融、IT供应链、政府和教育。建议加强漏洞与暴露管理、钓鱼防护、员工背景审查及恶意软件防御。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq8bS7zseJWoxFYwIrqaOJzBlk2MKzrGXCKXP45djybEx94R3rmtJDEBpMggFDNuiauP7IpfZMdVYJBCR92GoXjj7oCdAV55kQww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibHL5WlptZPRMWONXNd7GsvwwPpgAKia3d2hlhGTyODeibsViamwTH1FE1DxUiaS5wQnb7GEbLhszoAVEBMQ9fvFIJxib3JuQv42l90/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8yRG80wS3OtOhw4rzr2GxDbLQZbrxmHFibEcFV9ibo9vQuXbHpnVasp5kNsDkceZ3v0rgAPHjZNPnec9r9tWzjtxQ9Y1R9ic7sLc/640?wx_fmt=gif&from=appmsg)

**恶意代码情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicE58W5DVX7rt4VoJrhmjrcbjIuHG4PnJWozGicPzVYQvSjkLoaCcIEFhK9qKvqXRYSq7u0RvBLJy16TeroGGKS3P36N5xN7I9k/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8v83uiaASCaVJlibjaLlpYWjHnnAYGIYDBjv0wEXaCqv4glRTZxgsibxJRic0IiaicXwmK41MiaFwHSW7nsH0JFBqCaibvRolCeClBgBM/640?wx_fmt=gif&from=appmsg)

**01**

**揭秘 Sirius 后门：伪装成联邦快递（FedEx）发票的多阶段无文件攻击行动**

**披露时间：**20...