---
title: 每周网络安全简讯 ( 2026年 第46周 )
url: https://mp.weixin.qq.com/s/1IMiypkAkwd-vxyTZoSfig
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:44.226239
---

# 每周网络安全简讯 ( 2026年 第46周 )

# 每周网络安全简讯 ( 2026年 第46周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年11月7日至2026年11月13日，国家信息技术安全研究中心在线监测技术研究实验室对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Blind Eagle对拉丁美洲目标用户实施网络钓鱼攻击

近日，安全研究人员披露，APT组织Blind Eagle针对拉丁美洲司法、财政、行政和教育机构发起新一轮钓鱼攻击。此次攻击活动中，该APT组织使用葡萄牙语和西班牙语，仿冒法院通知、检察机关文书及行政文件，向经办案件、合同等事务的人员发送嵌入恶意附件的钓鱼邮件，其中一例附件以哥伦比亚司法为主题，当用户点击附件时，可在浏览器中渲染出仿冒该国总检察长办公室的页面，并利用HTML走私技术在浏览器本地组装ZIP载荷，以规避邮件安全检测。同时，压缩包内的JavaScript投放器伪装成网络配置审计工具，在用户点击时，会自动进行环境侦察，而后启动恶意脚本绕过AMSI与ETW安全机制，清除MotW标记且建立持久化，最终由PowerShell在内存中加载AsyncRAT木马，并实现对用户设备的持久性远控。

**链接：https://thehackernews.com/2026/11/blind-eagle-uses-fake-court-notices-to.html**

02

APT组织Turla利用Cereal恶意工具集对目标用户实施网络攻击

近日，安全研究人员披露，APT组织Turla使用名为Cereal的新型恶意工具集，将已失陷的Microsoft Exchange服务器转变为邮件收集系统和控制节点，针对哈萨克斯坦和罗马尼亚政府机构目标实施网络攻击。经分析，Cereal恶意工具集包含CerealNeuron和CerealBox等组件，其中CerealNeuron不主动外联，而是在形似Exchange正常服务的路径上等待传入请求，研究人员未发现专用外部控制基础设施；CerealBox为邮件收集组件，运行于EdgeTransport.exe进程内，按发件人、收件人、主题及附件等规则筛选并加密暂存邮件，且不影响正常投递。安全研究人员建议称，相关组织应对Exchange基础设施通信流量与用户设备进程等联动监测，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/turla-hackers-attacking-exchange-servers/**

02

网络动态

01

日本政府出台紧急网络安全方案，应对大规模数据泄露事件

日本政府当日宣布推出一项总额100亿日元（约6300万美元）的紧急网络安全方案，以应对近期数十家企业和政府机构接连遭遇未经授权访问及客户数据泄露的情况。该方案旨在推动公私部门信息共享、快速援助受害方并恢复受损业务。具体举措包括：强化已于10月合法化的“主动网络防御”能力；在可能危及国家安全的情况下，派遣由防卫省、警察厅和国家网络安全办公室官员组成的支援团队；经济产业省将于11月底前组建“顶尖”网络安全专家团队，利用人工智能对抗黑客、检测网络系统弱点，并与友好国家的科技企业和先进人工智能开发者合作；另设由公私部门专家组成的“网络救援队”，为受攻击企业提供初期响应，并由专门团队协助防护薄弱的企业加强防御。日本首相高市早苗在阁僚会议上表示，在人工智能生成攻击的时代，需要政府机构和企业加强准备，以快速应对潜在攻击威胁。

**链接：https://www.securityweek.com/japan-announces-emergency-cybersecurity-package-following-a-wave-of-attacks/**

02

美国CISA更新网络事件报告表

美国网络安全与基础设施安全局(CISA)近日更新网络事件报告表，旨在收集更详细的攻击信息，并帮助关联看似无关的事件。修订后的问卷就恶意软件、攻击技术、内部威胁及诱骗人员交出系统访问权限的手法设置了更具体的问题，删除了重复问题并采纳事件响应合作伙伴的反馈，同时纳入MITRE ATT&CK框架，便于分析人员比对不同机构的事件并研判可能的责任方。CISA相关负责人表示，此类报告有助于识别新出现的网络攻击活动、预警潜在目标并加强国家集体防御。

**链接：https://www.nextgov.com/cybersecurity/2026/11/cisa-updates-cyber-reporting-form-broader-incident-mandate-awaits-approval/417130/**

03

美太空军启动“太空数据网络”任务运营中心建设，支撑“金穹”等现代化项目

美国太空军太空系统司令部宣布，将为“太空数据网络骨干”项目设立任务运营中心（MOC），以支撑“金穹”导弹防御架构等依赖数字连接的现代化重点项目。Viasat公司获得一份最高价值4.5亿美元的IDIQ合同，用于支持网络与任务系统集成，其中首份任务订单价值1.15亿美元，用于设计、部署和扩展该中心。太空军新闻稿称MOC将在不断扩大的多供应商架构下整合任务集成、网络运营和数据传输管理，并作为协调多星座、多供应商任务系统的中央集成枢纽，为陆、海、空、天各域作战人员提供安全、韧性、高容量的连接支持。

**链接：https://defensescoop.com/2026/11/06/pentagon-mission-operations-center-space-data-network/**

04

印度CERT-In发布《人工智能安全审计指南》

印度计算机应急响应小组(CERT-In)发布《人工智能安全审计指南》1.0版，为印度机构开发、采购、部署或运营的AI系统，以及处理印度数据或服务印度用户的系统建立基于风险的审计框架。该框架将AI系统划分为低、中、高、关键四个风险等级，据此确定审计的深度、频率、独立性及人工监督要求，并设定覆盖AI全生命周期的九个核心审计领域，涵盖治理、数据质量、对抗韧性、人工监督和第三方供应链保障等。指南还针对生成式AI、检索增强生成、智能体AI、多模态及多智能体AI等提出专门要求，以应对提示注入、数据与模型投毒、过度代理等风险，并引入五级成熟度模型供机构评估AI治理能力。

**链接****：https://industrialcyber.co/ai/indias-cert-in-issues-ai-security-auditing-guidelines-targeting-model-poisoning-prompt-injection-agentic-ai-threats/**

05

英法主导的“帕尔马尔进程”通过首份商业网络入侵企业行为准则

由英国和法国主导、旨在约束全球间谍软件行业的“帕尔马尔进程”（Pall Mall Process）在“帕尔马尔倡议第三次会议”（Pall Mall initiative’s third conference）上通过首份面向商业网络入侵企业的行为准则。会议有43国代表出席，其中英国、法国、美国、德国、意大利、日本等14国政府表示支持。该准则针对商业网络入侵能力（CCICs）扩散带来的滥用问题，呼吁开发、销售此类能力或为其提供资金的企业审查客户、建立防滥用技术保障措施并维持滥用监测与报告机制，在存在严重滥用的可信风险时停止销售与支持。准则属自愿性质，不具约束力，不设违规处罚，预计主要由采购相关工具并审批其出口的政府施加压力。法国外交部称，该准则确立了“首个全球性负责任行为标准”。

**链接****：https://therecord.media/britain-france-set-out-guidelines-for-commercial-hacking-firms**

06

美国NIST发布对抗性机器学习分类与术语草案，聚焦智能体超级智能系统攻击与缓解

美国国家标准与技术研究院（NIST）发布《对抗性机器学习：攻击与缓解措施的分类和术语》初始公开草案（NIST SP 2400-102e2026），重点关注针对智能体超级智能（SI）系统的攻击及相应缓解措施，公开征求意见至12月18日。该草案区分预测型、生成型和智能体型SI系统，按系统类型、攻击所处生命周期阶段以及攻击者的目标、能力与知识等维度对攻击分类，涵盖规避、投毒、隐私攻击，以及直接提示、信息提取、间接提示注入和模型篡改等类型，并新增智能体SI攻击分类索引。草案同时梳理了缓解方法及其局限，指出现有缓解措施多属经验性手段，理论研究表明完美的防护无法实现，建议相关组织在部署前对抗性测试之外，优先加强韧性与应急准备，按“假定已失陷”的思路管理剩余风险。

**链接****：https://industrialcyber.co/nist/nist-lays-out-adversarial-machine-learning-taxonomy-to-address-attacks-targeting-agentic-superintelligence-systems/**

07

美国“流域250计划”试点聚焦水务设施网络安全

美国于8月31日在得克萨斯州启动为期6个月的“流域250计划”(Project Watershed 250)试点，由白宫国家网络总监办公室、得克萨斯州网络司令部、州长办公室及私营部门联合开展，环境保护署和CISA参与，向水务机构免费提供红队评估、人工智能工具、威胁情报、培训及漏洞修复支持。此前，FBI与环境保护署于7月30日发出警报称，至少7个州的水务机构遭到攻击，暴露于互联网的罗克韦尔自动化可编程逻辑控制器成为目标，部分事件干扰了供水运行。报道指出，漏洞修复需要专业人员、设备更换和持续投入，但试点结束后的费用来源尚不明确，受访专家认为，若缺乏可持续的联邦和州资金支持，多数机构的修复工作可能随试点结束而停止。

**链接****：https://industrialcyber.co/features/project-watershed-250-puts-water-utility-cybersecurity-under-scrutiny-though-long-term-funding-remains-unresolved/**

03

漏洞资讯

01

Apache OFBiz存在远程代码执行漏洞

近日，安全研究人员发现Apache OFBiz存在远程代码执行漏洞（CVE-2026-83542），攻击者可通过访问相关路径，以及公开且无需认证的/sfa/control/editPortalPageColumnWidth路由触发上述安全漏洞，无需登录即可在服务器上执行任意代码。目前，用户可通过将版本升级至OFBiz 24.09.08或更高版本的方式进行漏洞修复。

**链接：https://www.tuskira.ai/advisories/cve-2026-83542**

02

微软公司发布11月份安全漏洞更新公告

近日，微软公司发布2026年11月份安全漏洞更新公告，共修复1235个漏洞，其中约639个涉及Windows或其组件，66个为“严重”级别漏洞，分别为48个远程代码执行、15个权限提升，以及3个Microsoft Edge释放后使用缺陷。同时，微软公司还修复了已遭在野利用的Outlook欺骗漏洞（CVE-2026-124194），未经身份验证的攻击者可发送特制消息文件，诱使受害者用受影响版本Outlook打开后，在未充分提示外部内容风险的情况下连接至攻击者控制的网络位置，进而泄露可用于冒充用户的身份认证信息。目前，用户可通过补丁更新修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/**

03

React服务器组件存在远程代码执行漏洞

近日，安全研究人员发现React服务器组件（React Server Components）存在远程代码执行漏洞，影响react-server-dom-webpack、react-server-dom-parcel和react-server-dom-turbopack三个软件包，攻击者无需身份认证和用户交互，即可通过特制载荷实现远程代码执行。漏洞影响19.0.0至19.0.8、19.1.0至19.1.9、19.2.0至19.2.8及19.3.0等版本，目前用户可通过软件包更新修复上述安全漏洞。

**链接：https://cybersecuritynews.com/react-server-components-vulnerability-patch/**

04

Fortinet FortiClient存在远程代码执行漏洞

近日，安全研究人员发现Fortinet终端产品FortiClient存在远程代码执行漏洞(CVE-2026-121529)，是由其跨源资源共享(CORS)配置存在缺陷所导致，攻击者无需身份认证，仅需诱使用户访问恶意网站，即可借助网页向受害者主机上的本地服务发送请求并执行恶意代码。漏洞影响FortiClient Mac 7.4.0至7.4.7等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/fortinet2shell-vulnerability/**

05

谷歌Chrome浏览器存在9个安全漏洞，其中1个零日漏洞已遭在野利用

谷歌发布Chrome稳定版更新，修复9个安全漏洞，涉及7个高危漏洞、2个中危漏洞。其中，XML组件释放后使用漏洞（CVE-2026-125350）已遭在野利用，可使远程攻击者在浏览器中执行恶意代码。其余6个高危漏洞（CVE-2026-125343至CVE-2026-125348）涉及XML组件释放后使用、V8类型混淆、GPU越界写入、FileSystem授权错误、Compositing缓冲区溢出和WebGL未初始化资源；2个中危漏洞（CVE-2026-125342、CVE-2026-125349）均为GPU未初始化资源问题。目前，用户可通过将Chrome升级至Windows和Mac版157.0.8103.50/.51、Linux版157.0.8103.50并重启浏览器的方式修复上述漏洞。

**链接：https://cybersecuritynews.com/google-chrome-0-day-exploited/**

06

Windows CLFS驱动疑似存在本地提权漏洞

近日，安全研究人员在GitHub公开名为SignDrop的概念验证代码（PoC），声称本地普通用户可借助Windows通用日志文件系统（CLFS）驱动获取SYSTEM权限。该利用针对微软2025年10月为CLFS引入的日志认证功能，滥用Defender服务特权进程打开预置日志时会创建伴随文件的机制，在特定路径下创建任意文件。据称该PoC已在Windows 11 26H2等版本上测试，未关闭该认证功能的系统均在所称影响范围内，韩国安全公司78researchlab测试确认该利用有效，但认为其稳定性尚不足以用于实战。目前，微软尚未确认该问题，也未分配CVE编号或发布修复，且暂无在野利用报告。

**链接：https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html**

07

红帽容器镜像仓库Red Hat Quay存在2个安全漏洞

近日，安全研究人员披露容器镜像仓库Red Hat Quay存在2个安全漏洞。其中，第一个安全漏洞（CVE-2026-123710）允许可访问Quay仓库的用户将自有密钥加入Quay信任密钥且不设有效期，进而读取并覆盖所有仓库中的私有容器镜像；第二个安全漏洞（CVE-2026-110697）允许可创建命名空间的用户窃取其他租户的机器人账户令牌，并读取、推送或覆盖其镜像。目前，用户可通过版本升级修复上述安全漏洞。

**链接：https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html**

08

MongoDB存在安全漏洞

近日，安全研究人员发现MongoDB存在安全漏洞（CVE-2026-118383），允许未经身份认证的远程攻击者借助两个ping请求致使数据库服务器崩溃，特定条件下还可能在服务器进程内执行任意代码。该漏洞仅影响副本集成员，独立部署的mongod实例不受影响。目前，用户可通过将版本升级至9.0.7、8.3.16、8.0.37、7.0.48、6.0.30、5.0.35或4.4.32的方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/mongodb-database-crash-vulnerability/**

09

7-Zip存在远程代码执行漏洞

近日，安全研究人员发现开源文件压缩/解压缩工具7-Zip存在远程代码执行漏洞（CVE-2026-125742），是由LZX解码器的边界检查机制存在缺陷所导致，攻击者可构造特制的多卷CAB归档，诱导用户使用受影响版本的7-Zip解压，通过精确控制越界写入内容覆盖堆上的对象虚表进而劫持控制流实现任意代码执行。漏洞影响0≤version≤26.06等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：[【查看原文】](https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247509041&idx=1&sn=d6e387eacb4bd1900b1f3c36100a3b3f&scene=21#wechat_redirect)**

04

木马病毒

01

新型类蠕虫恶意工具包SCKit被披露

近日，安全研究人员披露一款名为SCKit的新型类蠕虫恶意工具包，被用于针对托管服务提供商（MSP）的ScreenConnect攻击。SCKit含16个脚本和组件，先在受害终端部署连接攻击者服务器的远程访问客户端以维持访问，再以RelayTrap组件替换合法Guest进程，待技术人员连入时尝试利用已修复的文件传输漏洞（C...