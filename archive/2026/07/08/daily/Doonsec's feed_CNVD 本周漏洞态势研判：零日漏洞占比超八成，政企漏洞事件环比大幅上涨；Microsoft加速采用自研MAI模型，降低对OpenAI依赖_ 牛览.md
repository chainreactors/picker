---
title: CNVD 本周漏洞态势研判：零日漏洞占比超八成，政企漏洞事件环比大幅上涨；Microsoft加速采用自研MAI模型，降低对OpenAI依赖| 牛览
url: https://mp.weixin.qq.com/s/yudRSd2hjmEd9TxIoLHKmg
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:56:23.864719
---

# CNVD 本周漏洞态势研判：零日漏洞占比超八成，政企漏洞事件环比大幅上涨；Microsoft加速采用自研MAI模型，降低对OpenAI依赖| 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wKeDC5RjIzFXicrPNJdJFmo7XH0iaSA5SVd4QUj0EfgajibSmqF7XYOzyEIrkCzYTxQnJWdv1ZNkZS760N2XDccUTuLtrXSw7SKjicJX7Sjh3mM/0?wx_fmt=jpeg)

# CNVD 本周漏洞态势研判：零日漏洞占比超八成，政企漏洞事件环比大幅上涨；Microsoft加速采用自研MAI模型，降低对OpenAI依赖| 牛览

安全牛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzGlLibGz6mXricUYYHaGe2NK5WneIFfNJicryibYnW0Lib5HvGuV7pBryAmTibibBepvdogiaNicc2Tallak5v2bZPy6eWOIX2m4K8Vv7Lc/640?wx_fmt=png&from=appmsg)

新闻速览

* CNVD 发布上周关注度较高的产品安全漏洞
* Microsoft加速采用自研MAI模型，降低对OpenAI依赖
* CNVD 本周漏洞态势研判：零日漏洞占比超八成，政企漏洞事件环比大幅上涨
* 英国推出自主智能体 AI 国家级网络防御盾 Cyber Shield，应对机器速度 AI 网络攻击
* 美军多个网站遭404Hijacking篡改，404错误页被植入亲库尔德政治信息
* 日本电信巨头 KDDI 遭供应链攻击，超 1200 万邮箱数据外泄
* 法庭文件显示Windows设备ID助力FBI追踪Scattered Spider黑客嫌犯
* Google Dialogflow CX“Rogue Agent”漏洞可导致聊天机器人被劫持
* Microsoft推出MXC，为AI代理加上运行边界
* Censys 监测：超七成 WordPress 站点运行过期 PHP，老旧组件催生 MR.GREEN 攻击
* 守内安 x ASRC 2026第二季度电子邮件安全观察报告

特别关注

**CNVD 本周漏洞态势研判：零日漏洞占比超八成，政企漏洞事件环比大幅上涨**

本期 CNVD 漏洞威胁综合评级为中，平台累计收录漏洞 523 个，高危 289 个、中危 180 个、低危 54 个，漏洞平均分值 6.65。其中 0day 漏洞 422 个，占总量 81%，含 D-Link DIR-513 缓冲区溢出等可直接发起攻击的零日漏洞。

本周政企单位上报事件型漏洞 5130 条，较上周环比上升 45%。漏洞类型集中于 WEB 应用，共 282 条，占比 54%；网络设备、操作系统漏洞次之，路由器、物联网终端风险突出。三六零、启明星辰、新华三等安全厂商为主要漏洞报送方。

海外厂商风险集中，Google Chrome、Android、Apple 全系终端、Fortinet 安全设备、Mozilla 浏览器批量爆出高危漏洞，多数可远程执行代码、沙箱逃逸、越权操作，厂商均已推送补丁。国产设备方面，D-Link DIR-513 存在栈溢出漏洞，暂未发布修复程序，攻击者可远程控机或断网；华为 HarmonyOS、腾达路由器亦有多条可用性破坏漏洞。

CNVD 已向金融、电信、教育、能源等关键行业通报风险，建议运维人员尽快完成设备补丁更新，收紧外网访问权限。

原文链接：

https://www.cnvd.org.cn/webinfo/show/12541

**CNVD 发布上周关注度较高的产品安全漏洞**

2026 年 7 月 6 日，CNVD 发布上周关注度较高的软硬件安全漏洞，覆盖境外主流软件、Linux 内核与华为、D-Link、Tenda 等境内厂商终端、路由产品，多漏洞可执行任意代码、逃逸沙箱或造成设备瘫痪。

境外产品漏洞方面，Google Chrome 蓝牙组件内存错误引用漏洞可借恶意外设执行任意代码；Oracle WebCenter Sites 权限校验缺陷允许攻击者完整接管系统；Fortinet FortiSandbox 存在命令注入漏洞，恶意 HTTP 请求可越权执行系统指令。Mozilla 全系浏览器、邮件客户端存在逻辑漏洞，存在沙箱逃逸风险；Linux kernel btrfs 模块释放逻辑缺陷会引发内核内存破坏，本地触发文件操作即可破坏系统内存。

国内设备系统漏洞集中在移动终端与家用路由器。Huawei HarmonyOS 短信应用存在路径遍历漏洞，EMUI 与 HarmonyOS 日志服务输入校验缺失，两类漏洞均会破坏系统可用性。D-Link DIR-513 两款接口存在栈溢出，可远程执行代码或触发拒绝服务；Tenda W15E 路由器白名单配置接口参数溢出，特制网络请求可直接断网。

上述漏洞均有对应 CNVD 编号备案，企业运维、安全运维人员需尽快对照设备版本完成补丁更新与访问权限收紧。

原文链接：

https://www.cnvd.org.cn/webinfo/show/12546

热点观察

**英国推出自主智能体 AI 国家级网络防御盾 Cyber Shield，应对机器速度 AI 网络攻击**

外媒 therecord.media 披露，英国国家网络安全中心 NCSC 联合政府通信总部 GCHQ 公布国家级自主 AI 防御项目 Cyber Shield，旨在打造主权可控、全自主运行的网络防护能力，覆盖政府内网与能源、交通、金融等关键国家基础设施。

项目核心驱动力是 AI 对手带来的防御危机：攻击者依托前沿 AI，可将数周的情报侦察、漏洞挖掘压缩至数分钟，传统人工防御完全跟不上机器运算速度，同时行业出现 “漏洞补丁潮”，新漏洞爆发速度远超企业修复能力，重大勒索攻击持续造成巨额经济损失，捷豹路虎曾遭攻击损失 15 亿英镑。

系统核心技术采用成对 Agentic AI 智能体架构，红方 AI 模拟攻击探测漏洞，蓝方 AI 实时执行防御处置，资产所属机构保留系统控制权。规划六大核心功能，自动化全网扫描已局部落地，全自主漏洞修复仍处于技术攻关阶段。

GCHQ 负责人 Anne Keast-Butler 警示，攻防 AI 能力将在数月内完成迭代，英国窗口期十分有限。项目定为跨代级工程，计划五年内全面落地，采用迭代测试、分阶段推广模式，无固定上线节点。政府无法独立完成建设，将联合前沿 AI 实验室、网络安全厂商、高校与关键基础设施运营商协同开发，并邀请行业参与方案设计。

英国同步推出网络弹性承诺，号召 60 余家企业落实安全规范，另投入 9000 万英镑强化中小企业网络防护，通过政企协同补齐全国自主 AI 防御短板GOV.UK。

原文链接：

https://therecord.media/britain-plans-autonomous-ai-cyber-shield

**法庭文件显示Windows设备ID助力FBI追踪Scattered Spider黑客嫌犯**

外媒 The Hacker News7 月 7 日披露美国联邦法院公开卷宗，FBI 依靠 Windows 全局设备标识符 Global Device Identifier（GDID）锁定 Scattered Spider 团伙 19 岁嫌疑人 Peter Stokes（代号 Bouquet），这名美爱双重公民已从芬兰引渡至美国受审。

2025 年 5 月 12 至 15 日，攻击者以 Google Voice 号码致电珠宝商 IT 客服，伪装员工骗取账号重置权限，拿下两名管理员账号；部署 ngrok、Teleport 隧道工具，窃取 77GB 数据上传至亚马逊云，并索要 800 万美元加密货币赎金。企业拦截勒索程序未支付赎金，仍产生 200 万美元处置损失。

GDID 为 Windows 安装专属持久标识，系统更新不会变更，仅重装系统才重置。涉案设备标识 g:6755467234350028 的访问记录，与 ngrok 注册、企业入侵时间完全吻合，同时匹配嫌疑人多地 IP、社交账号与出入境记录，成为完整证据链核心。嫌疑人虽使用 VPN、匿名账号，却未更换设备，最终暴露身份。

安全团队指出，本次入侵突破口为人为流程漏洞，仅靠 FIDO2 抗钓鱼 MFA 不足以防护，需增加账号重置回电核验、管理员审批等流程管控。

威胁情报机构 Group-IB 提示，Scattered Spider 并非单一团伙，而是由 5 人以内小型单元构成的松散社群，共享攻击工具与手法。该组织已发起超百起入侵，勒索金额超 1 亿美元，即便抓获个别成员，分散式架构仍会持续制造网络攻击风险。近年多国已有多名团伙成员相继落网，但整体威胁未得到根本遏制。

原文链接：

https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html

**Censys 监测：超七成 WordPress 站点运行过期 PHP，老旧组件催生 MR.GREEN 攻击**

2026 年 7 月 7 日，网络测绘厂商 Censys 发布监测数据，2026 年 6 月全网可探测 WordPress 站点超 5900 万个，分布于超 100 万个独立 IP，平台普及率极高，但整体安全状况堪忧。

监测显示，披露 PHP 版本信息的站点中，超 70% 搭载已停止官方维护的 PHP 版本；PHP7.4 使用占比超 20%，该版本 2022 年 11 月便终止支持。仅 14% 站点搭载最新版 WordPress，包含已停服的 6.9 版本在内，主流更新站点占比仅 31%。

站点插件同样存在大面积滞后问题，约 750 万个站点对外暴露插件信息，主流插件 YoastSEO 仅不足 22% 站点升级至 2026 年 5 月发布的 27.7 最新版。插件审核标准低于 WordPress 内核，老旧版本存在数据泄露、权限绕过、恶意代码上传等漏洞，攻击者还会篡改、收购废弃插件植入后门。

团伙 MR.GREEN 长期针对 WordPress 实施网页篡改攻击，截至 6 月已有 900 余站点遭入侵，该攻击活动自 2020 年延续至今。受害站点普遍存在多重短板：过期 PHP 与插件、未关闭安装页面、开放 xmlrpc.php、SSH 无访问限制。GreyNoise 近 90 天数据显示，已有 70 个 IP 持续扫描 xmlrpc.php 接口暴力破解。

Censys 给出防护建议：每 1 至 3 个月巡检 PHP、程序、插件、服务器配置，紧急漏洞补丁立即部署；不盲目全开自动更新，但切勿长期搁置升级，多类老旧组件叠加会形成完整入侵链路。

原文链接：

https://www.securitylab.ru/news/574529.php

安全事件

**美军多个网站遭404Hijacking篡改，404错误页被植入亲库尔德政治信息**

美国陆军多个互联网子域名近日遭遇疑似404Hijacking攻击，攻击者篡改网站404错误页面，植入支持库尔德（Kurdistan）的政治信息及针对美国总统Donald Trump、美国驻Türkiye大使Tom Barrack的攻击性内容。目前已确认受影响的网站包括oil.army.mil和ai2c.army.mil，美军在接到安全研究人员通报后已将相关页面下线并启动事件调查。

其中，oil.army.mil属于美国陆军Open Innovation Lab，主要用于软件及网络安全能力测试；ai2c.army.mil则属于Artificial Intelligence Integration Center，负责推进AI技术在陆军中的应用与人员培训。攻击仅影响404错误页面，暂无证据表明网站核心内容或后台系统遭到篡改。

研究人员Ronald Lovelace分析认为，此次事件具有典型404Hijacking特征，即攻击者利用网站404错误处理机制，在用户访问不存在页面时展示恶意内容，而非直接篡改网站主页。受影响站点运行于WordPress，并部署在Microsoft云基础设施上，攻击入口可能涉及第三方插件或服务器配置缺陷，但具体入侵路径尚未得到官方确认。

美国陆军表示，涉事页面托管于遗留第三方平台，与Army企业网络并未直接连接。目前相关页面已被移除，事件响应和取证工作仍在持续，官方尚未确认是否存在更大范围的系统受影响情况。

原文链接：

https://cyberscoop.com/us-army-websites-defaced-404-hijacking-kurdistan/

**日本电信巨头 KDDI 遭供应链攻击，超 1200 万邮箱数据外泄**

专业媒体 therecord.media 披露日本电信运营商 KDDI 发生大规模网络数据泄露事件，攻击者依托第三方软件漏洞入侵其面向多 ISP 共享的邮件底层平台，造成超 1233 万条用户电子邮件地址、近 762 万组账号密码泄露，覆盖六家日本互联网服务商 STNet、J:COM、Chubu、NIFTY、BIGLOBE 及自有业务用户。

攻击窗口期为 2026 年 5 月 16 日至 6 月 17 日，KDDI 在 6 月 17 日监测到异常未授权访问行为，第一时间修补第三方软件高危漏洞并隔离风险系统，完成取证后于 7 月 7 日正式对外公布泄露规模，并上报日本总务省与个人信息保护监管机构。

本次事故属于典型供应链安全风险，KDDI 为中小 ISP 统一提供邮件托管、网页邮箱、邮件存储服务，单一第三方组件漏洞形成跨服务商连锁泄露。部分用户密码采用哈希加密存储，一定程度降低账号劫持风险，但仍存在暴力破解、钓鱼复用等次生威胁。

事件处置层面，KDDI 已联动所有受影响 ISP 推送安全提醒，强制引导用户重置邮箱密码。长期整改方案包含两点，一是引入 AI 安全检测工具常态化审计第三方组件漏洞，二是联合合作服务商逐步迁移至加密强度更高的新一代邮件通信标准，消除共享平台集中暴露隐患。

该案例凸显电信行业共享基础设施的单点突破风险，为运营商供应链安全、多租户平台权限隔离提供典型警示样本。

原文链接：

https://therecord.media/major-japanese-telco-cyberattack-12-million-emails

安全攻防

**Google Dialogflow CX“Rogue Agent”漏洞可导致聊天机器人被劫持**

Varonis Threat Labs于2026年7月7日披露了一个名为Rogue Agent的严重安全漏洞，该漏洞影响Google的Dialogflow CX平台。攻击者若拥有对某个启用了Code Block功能的agent的编辑权限，便可利用此漏洞入侵同一Google Cloud项目中的其他启用Code Block的agent。

该漏洞仅影响使用Dialogflow Playbooks和自定义Code Blocks构建agent的组织。Code Blocks允许开发者添加自定义Python代码以扩展聊天机器人功能。攻击场景要求攻击者必须拥有dialogflow.playbooks.update权限，这意味着攻击并非远程无认证攻击，而是需要内部权限的横向移动攻击。

成功利用该漏洞后，攻击者可在受影响的Google Cloud容器环境中持久化恶意代码，从而劫持其他聊天机器人agent的运行逻辑，可能导致敏感数据泄露、业务流程被篡改或进一步的权限提升。由于Dialogflow CX广泛应用于企业客户服务、智能助手等场景，该漏洞的潜在影响范围较大。

Google已收到漏洞报告并采取相应修复措施。建议使用Dialogflow CX且启用Code Block功能的组织立即审查项目权限配置，限制dialogflow.playbooks.update权限的分配范围，并监控agent行为异常，以防范潜在的跨agent攻击风险。

原文链接：

https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html

产业动态

**守内安 x ASRC 2026第二季度电子邮件安全观察报告**

2026年第二季度，电子邮件安全环境面临典型的威胁平移。攻击者正加速从依赖传统的已知病毒特征，转向以规避防毒软件静态检测为核心的高级威胁形式（对应 MITRE ATT&CK: Defense Evasion）。数据显示，本季度带有恶意内容的邮件量较上一季暴增约 8 倍，并于今年5月达到峰值。

值得警惕的是，5月，恰逢多数企业开展内部演练，备战HW时期。极易被黑客利用此时间点发动真实攻击，从而衍生出严重的管理与通报风险：

**防范预期落差：**部分员工在预知有演练的心理状态下，面对异常邮件失去应有的警惕，认为只是模拟演练，不会产生实际损失。

**警报疲劳与通报拥堵：**当演练邮件与真实攻击同时涌入，it运维（Helpdesk）与安全部门（SOC）的资源会迅速被海量反馈的钓鱼邮件信息占用，真真假假的信息可能直接影响到应急预案的响应，导致实际响应滞后。

**“计中计”效应：**当安全团队拦截到真实攻击并发布给全公司紧急通知（如：【请注意！目前有真实钓鱼攻击，主题为 XXX】）时，员工容易将该通知信误认为是演练环节而置之不理，导致“人防”在最关键的时刻失效。

原文链接：https://mp.weixin.qq.com/s/b0E30fQ7\_6zFAHNlyZ3FZQ?click\_id=1287846159

**Microsoft加速采用自研MAI模型，降低对OpenAI依赖**

随着生成式AI推理成本持续攀升，Microsoft正通过扩大自研模型应用降低AI服务成本。据TechCrunch援引Bloomberg消息，Microsoft已开始在Excel、Word等Office应用中，将部分用户请求交由内部研发的MAI模型处理，而非完全依赖OpenAI和Anthropic的模型。这意味着Microsoft正在调整其AI模型部署策略，以优化推理成本和资源利用率。

报道指出，目前Microsoft仍会同时使用OpenAI和Anthropic模型，但自研MAI模型承担的任务比例正在提高。此前，在Build大会上，Microsoft已发布7款MAI模型，覆盖AgenticCoder、文生图等能力，进一步完善自有AI技术栈。

这一调整也反映出AI行业的新趋势。随着大模型训练和推理成本不断上升，越来越多科技企业开始优化模型使用策略，通过采用自研模型、混合模型架构或针对不同任务选择不同模型，以降低Token成本并提升运营效率。报道称，Amazon、Uber、Meta和Accenture等企业近期也陆续采取类似的成本控制措施。与此同时，部分企业还开始评估成本更低的中国大模型，但...