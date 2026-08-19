---
title: 金融行业网络安全监测月报(202511)
url: https://blog.netlab.360.com/jin-rong-xing-ye-wang-luo-an-quan-jian-ce-yue-bao-202511/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-08-18
fetch_date: 2026-08-19T02:56:37.994412
---

# 金融行业网络安全监测月报(202511)

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# 金融行业网络安全监测月报(202511)

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

18 Aug 2026
• 7 min read

[Share](#/share)

**报告编号：**360-TIC-202511-FIN01

## 一、报告概述

### 服务范围说明

基于360威胁情报中心对全球网络安全态势的持续监测与深度研判，本报告结合客户需求，整理了金融行业安全威胁情报，报告重点内容涵盖：

· **重保专项威胁情报服务：** 针对年底高发的资金结算与ATM安全威胁进行专项监测。

· **威胁情报咨询服务：** 深度解析本月移动支付欺诈与APT攻击手段。

· **攻击者溯源定位：** 聚焦朝鲜（BlueNoroff）与网络犯罪团伙的最新TTPs（战术）。

· **多维度威胁数据支持：** 涵盖SOCRadar、Zimperium、Kaspersky等全球Top级情报源。

────────────────────────────────────

## 二、重大安全威胁事件分析

### （一）移动支付与ATM安全威胁：NGate

**事件名称：** NGate（NFC中继）新型ATM盗刷威胁

**发布日期：** 2025-11-03

**发布机构：** CERT Polska / Zimperium

**威胁概述：**NGate是首个被证实的大规模利用NFC中继技术攻击ATM的恶意软件。攻击者无需获得受害者的实体银行卡，只需诱导受害者在感染了恶意App的手机上“贴卡读取”，恶意软件即可通过Android HCE（主机卡模拟）和非加密TCP协议，将卡片数据实时中继到攻击者在ATM前的设备上，实现“隔空取款”

**受影响行业：**金融,个人

**攻击手法（MITRE ATT&CK映射）：**

· 初始访问（T1566）：冒充银行客服发送钓鱼短信，诱导安装伪装成“银行安全工具”的恶意App 。

· 数据收集（T1005）：利用Android HCE（主机卡模拟）捕获受害者贴卡时的NFC流量与PIN码 。

· 命令与控制（T1071）：通过非加密TCP协议将数据实时中继至ATM前的攻击者 。

**IOC指标：**

· **C2 IP:** 91.84.97.13:5653

· **MD5:** 2cee3f603679ed7e5f881588b2e78ddc, 701e6905e1adf78e6c59ceedd93077f3 。

**报告链接：**https://cert.pl/posts/2025/11/analiza-ngate/

────────────────────────────────────

## 三、恶意软件威胁分析

### （一）拟人化银行木马：Herodotus

**事件名称：**Herodotus Android 银行木马

**发布日期：** 2025-10-31

**发布机构：** SOCRadar

**威胁概况：** Herodotus改变了传统木马“瞬间填充”数据的模式，它通过模拟人类的打字延迟、点击节奏和滑动轨迹，成功绕过了许多银行App基于行为生物识别的反欺诈检测。同时，它利用Accessibility（辅助功能）覆盖合法窗口窃取2FA验证码

**受影响行业：**金融

**攻击手法（MITRE ATT&CK映射）：**

· 防御规避（T1562）： 该木马不再瞬间填充数据，而是模拟人类的打字延迟、点击节奏和滑动轨迹，绕过基于行为特征的异常检测 。

· 界面劫持（T1505）： 滥用Accessibility（辅助功能）覆盖合法窗口，诱导输入凭证并截取2FA验证码 。

· 隐蔽通信（T1071）： 使用动态子域（google-firebase.digital）混淆C2流量 。

**IOC指标：**

· **Domain:** google-firebase.digital, gj23j4jg.google-firebase.digital

· **SHA256:**53ee40353e17d069b7b7783529edda968ad9ae25a0777f6a644b99551b412083

**报告链接：**https://socradar.io/herodotus-the-android-trojan-that-types-like-you/

────────────────────────────────────

## 四、APT组织威胁

### （一）针对金融从业者的精准狩猎：BlueNoroff (APT38) "GhostCall" 活动

**威胁主体：** 朝鲜Lazarus 组织关联团伙 BlueNoroff

**目标：**投资机构、Web3开发者、加密货币企业

**发布机构：** Kaspersky Securelist

**受影响行业：**科技,金融

**攻击技战术：**

· 社会工程学（T1566）： 在Telegram上伪装成知名风投机构或招聘人员，建立长期信任 。

· 供应链投毒（T1195）： 邀请受害者参加Zoom/Teams会议，引导访问仿冒会议页面（如 web071zoom.us），诱导下载恶意的AppleScript或ClickFix脚本 。

· 持久化（T1543）： 植入RustBucket变体或ObjCShellz后门窃取资金 。

**IOC指标：**

· **Domain:** web071zoom.us (仿冒Zoom), support.ms-live.us, system.updatecheck.store

· **MD5:** eda0525c078f5a216a977bc64e86160a, 17baae144d383e4dc32f1bf69700e587 。

**报告链接：**https://securelist.ru/bluenoroff-apt-campaigns-ghostcall-and-ghosthire/113883/

────────────────────────────────────

## 五、新兴威胁技术趋势

### （一）AI驱动的威胁升级

**趋势说明：** 攻击者（如朝鲜、伊朗组织）正在利用LLM（如Gemini、Qwen）生成恶意脚本、钓鱼诱饵，甚至实现恶意软件在运行时的即时代码重写以规避检测 。

**报告链接：**

https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools

### （二）“杀猪盘”诈骗产业化

**趋势说明：** 诈骗团伙利用AI生成虚假档案，结合加密货币洗钱网络，实施长周期的情感+投资诈骗（Pig Butchering），并利用虚假交易平台展示虚增收益

**报告链接：**https://www.cyfirma.com/research/pig-butchering-scams-cybercrime-threat-intelligence/

────────────────────────────────────

## 六、防御建议与落地措施

### （一）终端防护建议

· **NFC风控：** 在手机银行App中增加对NFC读取行为的监测，严禁在后台或通话状态下调用NFC功能 。

· **反行为模拟：** 升级反欺诈系统，不再仅依赖点击频率等简单行为特征，应结合设备指纹和环境监测对抗Herodotus类木马 。

### （二）网络防护措施

· **域名阻断：** 将web071zoom.us、google-firebase.digital 等恶意域名加入防火墙黑名单 。

· **供应链隔离：** 严格限制员工通过非官方渠道安装会议软件或运行所谓的“修复脚本”

### （三）情报持续监控

· **资产排查：** 针对Linux内核漏洞（CVE-2024-1086）和Kubernetes Ingress漏洞（CVE-2025-1974）进行资产盘点与补丁修复 。

· **账号安全：** 针对Telegram钓鱼猖獗的情况，建议金融从业者开启强MFA（硬件密钥），避免单纯依赖短信验证码 。

────────────────────────────────────

##

## 七、报告总结与交流

经过对本月多源情报的综合分析，我们对金融行业面临的安全态势总结如下：

**攻击维度的“虚实结合”：** NGate事件标志着网络攻击不再局限于线上数据窃取，而是利用移动端作为跳板，直接突破了**ATM物理设施**的安全防线。这要求银行必须打通移动端风控与ATM机具风控的数据孤岛。

**防御体系的“规则失效”：** Herodotus的出现证明，简单的“非人类行为特征”（如输入速度过快）已不再可靠。未来的反欺诈必须向**意图识别**和**设备底层信誉评估**转型。

**社工攻击的“信任滥用”：** BlueNoroff的案例警示我们，攻击者正利用金融从业者对“业务会议”、“监管合规”的信任进行攻击。**人的因素**依然是防御体系中最薄弱的环节。

**落地建议：** 建议安全团队立即排查本报告IOC清单中的IP与域名，并针对移动应用进行一次针对“辅助功能滥用”的专项渗透测试。

────────────────────────────────────

## 报告说明

本报告基于近期金融行业安全威胁情报表格信息整合，涵盖了ATM新型盗刷、拟人化银行木马、APT定向攻击等主要威胁类型，为客户提供全面的网络安全态势感知和可落地的防御策略建议。

**情报时效性：** 2025年11月  **威胁评估等级：** 高风险（多源情报验证）

[## AI安全专题周报(20260814)

报告编号：TIC-202608-AI01
报告周期：2026年8月8日—8月14日
一、报告概述
基于360威胁情报中心对全球人工智能安全态势的持续监测与分析，本周AI安全风险主要集中在AI Agent自主攻击、AI开发供应链及AI衍生攻击方式等方向。相关事件显示，随着AI逐步参与代码开发、漏洞测试和自动化任务执行，其网络访问、代码执行、第三方依赖及敏感凭证正在形成新的安全攻击面。
报告重点内容涵盖：
· AI Agent自主攻击与运行安全：AI Agent已表现出自主发现漏洞、突破隔离环境及持续探索攻击路径的能力，容器和沙箱等执行环境的隔离风险同步上升。
· AI开发与供应链安全：npm、CI/CD及AI开发工具逐渐成为供应链攻击目标，AI服务密钥、代码仓库凭证及Agent配置等资产面临泄露风险。
· AI衍生攻击方式：AI幻觉、自主漏洞发现及自动化攻击能力正逐步被转化为供应链投毒、漏洞利用等现实攻击手段。
────────────────────────────────────
二、本周重点安全事件
（一）ChainDrop蠕虫攻击npm及AI开发环境](/aian-quan-zhuan-ti-zhou-bao-2/)

18 Aug 2026
9 min read

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

[360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com) © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)