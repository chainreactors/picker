---
title: 网络安全早报·11月14日
url: https://mp.weixin.qq.com/s/hQktcHU3bixNT6LtXUEQgw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:28.195203
---

# 网络安全早报·11月14日

# 网络安全早报·11月14日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 12 日至 14 日 · 共 8 条。11 月 14 日首次披露的事件不足 8 条，本期按近 3 日要闻回顾收录。

01在野利用UnrealIRCd 标签注入漏洞被用于服务器级命令执行，CISA 列入 KEV

CISA 11 月 13 日将 CVE-2026-114713 列入已知被利用漏洞目录，The Hacker News 11 月 14 日报道时称已观察到实际利用。漏洞位于 labeled-response 模块：6.0.0 至 6.2.7.1 之前的版本在回显 IRCv3 label 标签时未做转义，在两个以上服务器互联的网络中，任意普通用户可注入以服务器权限执行的命令，可执行 KILL、GLINE 等操作。

维护者 Bram Matthys 称这是 15 年来 UnrealIRCd 最严重的漏洞。项目方 11 月 7 日发布 6.2.7.1 与热补丁，同时修复 9 个安全问题；利用尝试在 11 月 8 日出现。

**受影响：**UnrealIRCd 6.0.0 至 6.2.7.1 之前的版本，且所在网络存在两个以上互联服务器。

**官方处置：**升级到 6.2.7.1 或应用官方热补丁；CISA 依据 BOD 22-01 要求联邦民事机构在 11 月 16 日前完成修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeUibvtXhXiaQPMM5nYeTa0PgNpWQ1ebcSqeG1sibXWxV1icAr39aZ1FSx0giawPrpQBR4sr35JcQe0PCGIspLaibu1L0wbwhwBOQvwWk/640?from=appmsg)

图：NVD CVE-2026-114713 记录页，2026-11-14 截图

02n0n 声称窃取 Expedia 近 10 亿条旅客记录，Expedia 确认经第三方数据平台被入侵

SecurityAffairs 11 月 14 日报道，勒索组织 n0n 声称通过入侵第三方数据平台供应商取得 Expedia 数据，规模接近 10 亿条旅客记录。该组织称其中包括 35 个忠诚度计划的逾 8.3 亿条记录、5800 万份旅客档案、逾 3.33 亿条消费者账户与凭据记录，以及约 250 万条信用卡消费记录。

Expedia 向 Skift 确认，攻击者通过一家第三方数据平台供应商的受信访问进入其系统，同一供应链攻击还影响多家公司。Expedia 未确认 n0n 公布的数字，调查仍在进行，并称其平台对旅客与合作伙伴仍可使用。Wiz 与 Sentra 称，攻击使用了一个从 Qubole 窃取的供应商密钥。

**受影响：**Expedia Group 及其 Hotels.com、Vrbo 等品牌的相关数据平台；具体受影响记录数与用户数未公布。

**官方处置：**Expedia 称发现后已控制影响并引入外部安全专家调查，未确认 n0n 声称的数据规模。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeW10zE4ibtDgEgiaEYL68JNM1N0D7XOUo1b0FvsLDRkxIxpaMHTcvtQph1oicvYYc6k13dY9ZxU8aqwHxybSw517IUNKv3ql7veus/640?from=appmsg)

图：SecurityAffairs 2026-11-14 报道配图（Expedia）

03Cursor 披露入侵源头：Fireworks AI 泄露访问密钥，恶意 Claude Code 扩展最多触及 5000 名用户

Cursor 11 月 13 日发布事件更新，BleepingComputer 11 月 14 日报道。攻击者取得 Cursor 签发给 Fireworks AI 的访问密钥，该密钥由 Fireworks 泄露；攻击者用它从 Cursor 共享给 Fireworks 的只读存储桶复制数据，内容主要是 2025 年未开启 Privacy Mode 的编码智能体会话轨迹。Cursor 称少量轨迹含未脱敏凭据，不到 0.01% 的客户 API 凭据暴露。

10 月 29 日，攻击者用从内部系统窃取的凭据，把 Anthropic.claude-code 2.1.312 与 2.1.313 的恶意副本放入 Cursor VS Code 扩展市场缓存，存续约 11 小时，最多 5000 名请求特定缓存版本的用户可能收到。Anthropic 未发布该副本，Open VSX 未受影响。Cursor 称最后一次攻击者活动在 11 月 1 日，已被阻断。

**受影响：**10 月 29 日从 Cursor 扩展市场安装或更新至 Anthropic.claude-code 2.1.312、2.1.313 的用户；少于 0.05% 的未开启 Privacy Mode 用户的历史编码智能体轨迹被暴露。

**官方处置：**Cursor 已停用签发给 Fireworks 的密钥、迁走全部推理流量、轮换凭据、重建扩展市场并通知受影响客户；安装过上述版本的用户需按 10 月 30 日安全公告处置，仅卸载扩展可能不够。

04Uber 通报司机驾照信息泄露，三州已确认 7870 人受影响

Uber 开始通知美国司机，其个人与驾照信息在 10 月第三方 AI 供应商 Fireworks AI 的数据泄露中被窃取。已提交的州通报显示，马萨诸塞州 2567 人、南卡罗来纳州 3430 人、罗德岛州 1873 人受影响，三州合计 7870 人。

TechCrunch 11 月 13 日报道涉事供应商为 Fireworks AI。Uber 未公布全国受影响人数，也没有说明是否已有资金损失。

**受影响：**收到 Uber 通报的美国司机，已披露的三个州合计 7870 人；泄露字段包括姓名与驾照信息。

**官方处置：**Uber 已向受影响司机发出通知，未公布全国总数。

05在野利用Check Point Gaia OS 提权漏洞 CVE-2026-123039 列入 KEV

SecurityAffairs 与 GBHackers 11 月 14 日报道，CISA 已将 CVE-2026-123039 列入已知被利用漏洞目录。该漏洞位于 Gaia OS 的 DynamicCLI 组件，CVSS 7.8：已取得设备代码执行权限的本地攻击者可借此提升到 root。

Check Point 在 11 月 12 日的调查中称，该漏洞被用于攻击未修补的 Security Gateway，攻击者随后部署 TSGA 后门，并在部分受害机构的 VMware ESXi 主机上执行擦除操作。

**受影响：**R81、R81.10、R81.20、R82、R82.10、R82.20 的 Security Gateway、管理服务器与日志服务器、多域安全管理（MDSM）、多域日志服务器（MDLS）与 Maestro Orchestrator。

**官方处置：**Check Point 发布公告 sk1000362 要求安装修复程序；CISA 要求联邦民事机构在 11 月 16 日前完成修复。

06BlackNevas 用合法管理接口清除 4 台 ESXi 主机、全部虚拟机与备份

卡巴斯基 GERT 11 月 13 日发布分析，GBHackers 11 月 14 日报道。一起入侵持续 10 天，攻击者清除 4 台 VMware ESXi 主机上的全部虚拟机、2 台 vCenter Server Appliance 及全部备份基础设施，勒索信息指向 2024 年 11 月首次出现的 BlackNevas 组织。

攻击者未利用虚拟机逃逸漏洞，而是通过暴露的 VMware 管理接口、窃取的管理员凭据，以及一套监控系统中可复用的 root 凭据进入虚拟化层。受害方运行的是已停止支持的 vSphere 版本。同一篇分析还记录了另一起针对 Proxmox 环境的勒索案例。

**受影响：**VMware ESXi 与 vCenter，受害环境为已停止支持的 vSphere 版本。

**官方处置：**卡巴斯基建议修补虚拟化平台、限制管理接口暴露、隔离管理网络、轮换特权凭据并保留离线备份。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5LNgXJargeXPeMmg49XuxRlicVTsqrjpibiawNzOU2nib72busFECKMBibNicib1cfKOWys5FTcJF8dTmyqymuCJ7ia5KbusAL5uiacvFqu3cpIDZ6Ek/640?from=appmsg)

图：卡巴斯基 Securelist 2026-11-13 分析配图

07昆士兰国家公园预订系统因第三方 Bookeasy 数据泄露下线

昆士兰州环境、旅游、科学与创新部 11 月 14 日更新公告：正在调查第三方供应商 Bookeasy 的数据泄露，Bookeasy 负责运营该州国家公园预订系统。部门已联系客户告知泄露与可能的诈骗风险，称尚不确定哪些客户信息被访问。

公告称支付通过独立的安全系统处理，目前不认为客户财务信息被访问。预订系统暂时不可用，公园正常开放，已有预订仍然有效。

**受影响：**使用昆士兰国家公园预订服务的客户；受影响人数与字段未公布。

**官方处置：**预订系统已暂时停用；收到可疑邮件、短信、WhatsApp 或电话的客户应先报告至 QPWS@detsi.qld.gov.au，不要点击链接或提供支付信息；如已提供支付信息，联系银行。

08FBI 预警：ARTEX 自动化渗透框架被用于攻击，部分入侵 3 小时内取得特权访问

FBI 11 月 13 日发布 FLASH-20261113-001，GBHackers 11 月 14 日报道。预警称 ARTEX 这一开源、由大语言模型驱动的智能体平台已被用于自动化侦察、利用、提权与数据外传；至少自 2026 年 8 月起，多个攻击者用它针对金融、政府、科技、国防、半导体、能源、医疗、制造与电信等行业。

FBI 称部分入侵在不到 3 小时内取得特权访问，攻击者组合使用窃取凭据、暴露应用与云权限。

**受影响：**暴露在公网的应用、使用云身份与第三方联邦信任的组织；预警未列出具体产品版本。

**官方处置：**FBI 在预警中列出检测指标与缓解措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeXXUrMXibeqU40MDHRbtoUKUm7j4SxUyJ1LoiafDtxfzjypaKxbp2L0ibOd7ictbWoXGD1syJnN4PdUF8ExGicXUKZnBvibwRH2w1xZk/640?from=appmsg)

图：FBI FLASH-20261113-001 首页

The Hacker News　https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html

NVD　https://nvd.nist.gov/vuln/detail/CVE-2026-114713

SecurityAffairs（Expedia）　https://securityaffairs.com/203062/cyber-crime/extortion-group-claims-theft-of-nearly-one-billion-expedia-traveler-records.html

Cursor　https://cursor.com/blog/security-incident-update

BleepingComputer　https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/

GBHackers（Uber）　https://gbhackers.com/uber-hacked-hackers-steal-drivers-license-personal-data/

SecurityAffairs（CISA KEV）　https://securityaffairs.com/203040/hacking/u-s-cisa-adds-check-point-and-unrealircd-flaws-to-its-known-exploited-vulnerabilities-catalog.html

Check Point　https://support.checkpoint.com/results/sk/sk1000362

GBHackers（BlackNevas）　https://gbhackers.com/blacknevas-ransomware-attacks-vmware-esxi-servers/

卡巴斯基 Securelist　https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/

昆士兰国家公园　https://parks.qld.gov.au/contactus/important-security-update

GBHackers（ARTEX）　https://gbhackers.com/fbi-warns-artex-ai-framework/

FBI IC3　https://www.ic3.gov/CSA/2026/261113.pdf

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GtFR6uY3nh6MJdyIdsWXrDem00Mia2eSiae1MMcoX2HUKRsPnx0EenFmcMdQwn0qAz5TJfRlOYVF4zsSibLicTlPtA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过