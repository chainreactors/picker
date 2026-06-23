---
title: 打不死的网络犯罪品牌ShinyHunters：六年进化，从数据贩子到勒索团伙
url: https://mp.weixin.qq.com/s/3hAmi3xa4dXvSufjQ8Bv-Q
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:02:46.334730
---

# 打不死的网络犯罪品牌ShinyHunters：六年进化，从数据贩子到勒索团伙

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDohJjQmFy9EL2VlZusI5vSuF335g3U2JoHc2Sh648tibTp46SkfAML6lpoWCwwibAPbCM1BoATEQtCfGdEtNqfS6HYiaxQXOM9Grk/0?wx_fmt=jpeg)

# 打不死的网络犯罪品牌ShinyHunters：六年进化，从数据贩子到勒索团伙

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多企业的安全模型依然默认，筑牢边界防线加上 MFA（多因素认证），就能挡住大规模数据窃取。现实是，当下活跃的 ShinyHunters 攻击体系早已轻松绕过这套防御逻辑。

这个名号从 2020 年出现在公众视野，六年时间里经历三次暗网论坛查封，五名核心管理员落网，一名创始人被美国法院定罪，却始终没有消失。2026 年 4 月的七天内，它就在暗网论坛上架了五份全新的企业数据与权限售卖清单，覆盖云开发平台、房地产科技公司、头部科技厂商等多个领域。它早已不是传统意义上的单一黑客团伙，而是一个生命力远超个体成员的网络犯罪品牌。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqUVeDwT1Zzlz8FPtfcx7weRfDfib2JfibLRctAVsCfcd2MRyGGM3p75uzO0QuL50X2PqEibCqhefiaSktVu52CsrjnHVHfSw4utV0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoX0146aBqEjKqrBzKYJIlBW9eIpKz145JfAxF25lUibv7ZGvZMk6hdYoZokDbNQEtKm4mreogNHauPeG4ux5xJB8Y9da6tzXL4/640?wx_fmt=png&from=appmsg)

ShinyHunters 的名字源自宝可梦社区中专门捕捉稀有闪光宝可梦的玩家，刚好契合这个团伙早期专门狩猎高价值数据库的行事风格。

团队在 2020 年初正式公开活动，同年 5 月的两周内，就在多个暗网论坛上架了超过 2 亿条被盗记录，早期攻击目标以消费级平台的大规模 PII（个人身份信息）数据为主，典型案例包括 Mathway 的 2500 万条记录，Tokopedia 的 9100 万条记录，Wattpad 约 2.7 亿条记录，Animal Jam 的 4600 万条记录，以及从微软 / GitHub 获取的约 500GB 代码样本与测试项目。

微软事后评估这批 GitHub 数据多为代码样本、测试项目、电子书籍与通用内容，不涉及核心专有知识产权。数据体量真实存在，但实际影响远低于 ShinyHunters 宣传的程度，这种宣称与实际效果的落差，也成为这个品牌贯穿始终的特征。

2021 年 6 月，美国华盛顿西区联邦法院起诉三名法国公民，认定他们是 ShinyHunters 的初代核心成员。三人分别是负责钓鱼工具与伪造登录页面开发的 Sebastien Raoult，擅长入侵的 Gabriel Kimiaie-Asadi Bildstein，同时也是 GnosticPlayers 成员，以及负责协作与网络运维的 Abdel-Hakim El Ahmadi。

目前仅有 Raoult 被定罪。他在 2022 年 5 月于摩洛哥拉巴特萨累机场被捕，时年 21 岁，日常负责搭建微软、GitHub、Atlassian、AWS 等平台的伪造登录门户，运营钓鱼基础设施收集企业凭证。2023 年 1 月摩洛哥将他引渡至美国，2024 年 1 月 9 日被西雅图地区法院判处三年监禁，并处超过 500 万美元赔偿金。另外两名核心成员据信仍在法国潜逃。

公开报道中常有说法认为 ShinyHunters 创立了 BreachForums，这个结论并不准确。BreachForums 由来自纽约的 19 岁青年 Conor Brian Fitzpatrick，网名为 pompompurin，在 2022 年 3 月 16 日推出，定位是 RaidForums 的继任平台。2023 年 3 月 FBI 在他父母家中将其逮捕时，他刚满 20 岁。

Fitzpatrick 以三丽鸥角色名作为账号，负责论坛的全部运营工作，涵盖账号审核、纠纷处理、封禁管理以及被盗数据交易的担保服务，这个账号同时也出现在他日常使用的合法游戏论坛中。而 RaidForums 在此前几周已经遭遇打击，其创始人 Diogo Santos Coelho 于 2022 年 1 月 31 日在英国被捕，同年 4 月 12 日官方宣布查封站点，行动代号为 Operation TOURNIQUET。

2023 年 6 月，也就是 Fitzpatrick 被捕三个月后，ShinyHunters 接管了 BreachForums 的运营权，联合管理员 Baphomet 重启论坛推出 BreachForums v2。这是该组织的关键战略转折点，他们不再只是被盗数据市场的交易者，转而成为平台的运营者，掌握交易规则、数据拍卖机制、会员纠纷仲裁权，还能看到所有买家的采购偏好。

此后该论坛又经历两次关停。2024 年 5 月 15 日，FBI 查封 BreachForums v2，有消息称管理员 Baphomet 同期被捕，但美国司法部从未正式确认该信息。2025 年 4 月 28 日，论坛管理员发布 PGP 签名的关停公告，称原因是存在 MyBB 零日漏洞，也有报道认为关停源于 Dark Storm Team 的 DDoS 攻击或是执法部门渗透，具体原因至今存在争议。

每一次关停之后，这个品牌都会在几天内更换新域名重新上线。截至 2026 年 4 月，相关交易信息主要发布在 breachforums.rs 站点。这种持续存活的能力并非源于技术层面的抗打击能力，而是组织模式的特殊性，品牌本身就是核心资产，单一管理员落网不会摧毁整个生态。

## 战术全面迭代：转向身份驱动的业务逻辑滥用

##

到 2024 年年中，ShinyHunters 已经完全脱离了早期批量拖库的粗犷模式，2025 年之后的攻击链路呈现出高耐心、强身份感知、精准打击的特征。谷歌威胁情报团队 GTIG 将不同战术的攻击划分为多个集群，完整呈现了战术的演进路径。

### 2024 Snowflake 浪潮：凭证重放的降维打击

Mandiant 将该集群追踪为 UNC5537，攻击手法简单但破坏力极强。攻击者直接将信息窃取器收集到的账号凭证，重放到未强制开启 MFA 的 Snowflake 实例中。

Mandiant 的分析显示，攻击涉及六种信息窃取器恶意程序，分别是 VIDAR、RISEPRO、REDLINE、RACOON STEALER、LUMMA 与 METASTEALER，参与攻击的账号中 79.7% 存在历史凭证泄露记录，最早的信息窃取器感染时间可以追溯到 2020 年 11 月。

已确认的受害者包括 AT&T、Ticketmaster、Santander、Lending Tree 与 Advance Auto Parts，其中 AT&T 被报道支付了 37 万美元赎金以阻止通话详单泄露，这是该浪潮中唯一有公开记录的赎金支付。攻击者使用定制的 Snowflake 侦察工具 FROSTBITE，存在.NET 与 Java 两个版本，可以枚举用户、角色、IP 与会话 ID，再通过原生 Snowflake SQL 语句完成数据外渗，最终数据流向 MEGA 网盘以及摩尔多瓦的 ALEXHOST SRL 等 VPS 服务商。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDq1TZxTmhIvic68BfAcFYrmHTIbpXcAXwxH2nAuqvohPxgK62DoNDuBnPcMPsKmABHBhSLdzbMQ7TO4nrnCrIz9IUFrvib6lXkWs/640?wx_fmt=jpeg&from=appmsg)

### 2025 Salesforce 语音钓鱼：合法授权绕过 MFA

Mandiant 将该集群追踪为 UNC6040，美国 FBI 也发布了 IC3 预警，编号 CSA-2025-0912，同时覆盖 UNC6040 与后续的 UNC6395 集群。

这套攻击链并没有从技术层面破解 MFA，而是利用业务流程直接获得合法权限，完整步骤分为五步。第一步攻击者致电企业帮助台，冒充内部 IT 支持人员。第二步以排查连接故障为由，引导员工访问 Salesforce 的 setup/connect 页面。第三步诱导员工授权一款恶意连接应用，通常是经过篡改的 Salesforce Data Loader。第四步系统生成 OAuth（开放授权协议）访问令牌，继承该员工的全部账号权限。第五步攻击者通过批量 API 查询，从云环境中拉取数千万条数据记录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqFFBTp1qQvZ0efzVjPKWkRbk9PDBaD0QVhSy5qHE6J4vXkITMyeYCCM0iajyr1ib6gl0Ngvb2S60l9U9btRTRSCsXVCsP3ibt6cQ/640?wx_fmt=jpeg&from=appmsg)

2025 年 4 月，开云集团旗下的 Gucci、Balenciaga、Brioni 与 Alexander McQueen 均遭遇该手法攻击，事件直到 2025 年 6 月才被发现。ShinyHunters 宣称仅 Gucci 就有 4300 万条记录被盗，另外三个品牌合计约 1300 万条，去重后包含 740 万个唯一客户邮箱，同时泄露姓名、地址、电话号码与消费总额等信息。开云集团事后确认了入侵事件，但未证实数据规模，同时否认曾进行赎金谈判。

### 2025 第三方 OAuth 供应链：无需钓鱼的合法入口

UNC6395 是并行的攻击集群，甚至不需要致电目标企业。攻击者利用 Salesloft Drift 聊天机器人与 Salesforce 集成的 OAuth 令牌完成入侵，Mandiant 追溯令牌泄露根源，是 2025 年 3 月至 6 月期间 Salesloft 的 GitHub 账号遭遇入侵。

来自可信 SaaS 集成的被盗 OAuth 令牌，是最隐蔽的入侵入口。整个过程不需要投放恶意软件，不会触发凭证校验拦截，也不需要突破边界防护，因为这个集成本身就在企业的信任列表当中。

两条攻击链路同时运行的现实，给防御带来了新的挑战。多数企业针对 UNC6040 的语音钓鱼加固了帮助台流程，却依然暴露在 UNC6395 的集成令牌失窃风险中。只关注用户账号的抗钓鱼 MFA 建设，未必会监控新增的连接应用授权，或是第三方 SaaS 集成的安全状态。

### 2026 攻击集群扩张

2026 年 1 月，谷歌威胁情报集团 GTIG，也就是原 Mandiant，更新了集群分类，新增三个集群追踪最新的战术演进。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoDnGHmx9ovDyY8pQPnIuLTlHWRo9ePcK3N0zTTWWGpAFX092ENHQh419DU7IRoZ84Hvo8jkHcS3tnQfn8hsgTiaDtwIfOia7h2M/640?wx_fmt=jpeg&from=appmsg)

UNC6661 在 2026 年 1 月上中旬开展语音钓鱼行动，冒充 IT 人员谎称公司正在更新 MFA 设置，引导员工访问仿冒的企业凭证收集页面，获取 SSO（单点登录）凭证与 MFA 验证码。随后攻击者会在受害者的身份提供商中注册自己的设备作为 MFA 验证端，即便后续企业修改密码，攻击者依然保有访问权限。

UNC6671 在同一时间段针对不同目标运行了完全相同的攻击链路，GTIG 将其单独追踪以排除仿冒可能。UNC6240 则负责勒索变现环节，GTIG 根据共用的 Tox 谈判账号、带有 ShinyHunters 标识的勒索邮件，以及使用 Limewire 作为样本托管服务的特征，确认该集群承接 UNC6661 入侵后的勒索工作。2026 年 1 月底，带有 ShinyHunters 标识的全新数据泄露站点上线，公示该批次攻击的受害者名单。

这次技术升级的影响范围显著扩大。2025 年的 UNC6040 仅针对 Salesforce 平台，滥用连接应用授权流程。2026 年的三个集群直接攻击通用的 SSO 加 MFA 体系，意味着企业身份提供商对接的所有 SaaS 应用都会暴露在风险中，不再局限于单一平台。抗钓鱼 MFA 的安全建议依然有效，但需要覆盖的攻击面已经大幅拓宽。

## 三强联合：联邦式犯罪联盟 SLH 成型

2025 年 8 月，三个知名度最高的英语系网络犯罪品牌宣布合并，组成联合实体 SLH。三个品牌各有擅长领域，Scattered Spider 也就是 UNC3944，擅长社会工程与帮助台仿冒，LAPSUS$ 擅长高强度入侵、MFA 疲劳攻击与内鬼招募，ShinyHunters 则负责数据外渗、变现与论坛运营。

2025 年 8 月 8 日，首个经过验证的 Telegram 频道上线。到 2025 年底，SLH 旗下运营的 Telegram 频道至少有 16 个，频道内发布的 PGP 签名消息，可以通过此前已知的 ShinyHunters 公钥完成验证。2025 年 10 月的澳洲航空与越南航空数据泄露事件中，发帖内容直接标注了 SLH 相关频道名称，这是 SLH 品牌首次与高可信度的真实数据泄露事件绑定。

Trustwave SpiderLabs 将 SLH 定义为联邦式品牌，而非中心化组织。这个定性至关重要，意味着整个体系不存在可以被一网打尽的核心头目。成员主要来自名为 The Com 的松散英语系网络犯罪生态，参与者多为年轻群体甚至青少年，通过 Discord 与 Telegram 共享攻击手册、招募新成员。

### 向勒索软件即服务转型

2025 年 11 月 19 日，BleepingComputer 报道 SLH 正在开发自有 RaaS（勒索软件即服务）项目，命名为 ShinySp1d3r。根据早期版本的技术分析，该勒索软件具备多项技术特征。加密算法采用 ChaCha20，对称密钥通过 RSA-2048 保护。当前仅支持 Windows 系统，Linux 与 VMware ESXi 版本据称即将发布。反取证能力通过挂钩 EtwEventWrite 函数实现，压制 Windows 事件跟踪的遥测数据，从 API 层面干扰事件查看器而非直接禁用服务。程序会清除卷影副本以阻止数据恢复，内置硬编码的服务与进程终止列表，还支持多种横向传播方式，包括通过 SCM 部署、WMI 部署以及组策略部署。

目前 ShinySp1d3r 仍处于开发阶段，尚未有公开确认的真实攻击案例。其技术来源也存在争议，多数分析认为这是从零开发的加密器，不基于 LookBit、Qilin 或 DragonForce 等已知家族，也有安全厂商评估其早期版本是基于泄露的 Hellcat 勒索软件源码，经过人工智能辅助修改而成。

无论技术来源如何，这个开发信号本身具备战略意义。ShinyHunters 在过去六年始终回避文件加密路线，全部变现模式都建立在数据窃取与勒索之上。开发 RaaS 意味着该品牌的战略方向出现调整，将在现有数据勒索的基础上，拓展 affiliate 模式的加密勒索业务。

## 典型事件与 2026 年最新动态

2024 到 2026 年期间，高影响力的攻击事件持续出现，完整呈现了战术演进的轨迹。

2024 年除了 Snowflake 浪潮的多个受害者，还有 6 月的 Cylance 也就是 BlackBerry 数据泄露事件，账号为 Spid3r 的卖家上架 3400 万条 2015 到 2018 年的营销数据，开价 75 万美元。BlackBerry 否认当前客户数据受到影响，该账号与 SLH 生态关联紧密，但不等同于官方的 ShinyHunters 身份。

2025 年除了开云集团与 Salesloft 供应链事件，典型案例还包括 9 月的越南信贷机构数据泄露，据称泄露 1.6 亿条以上记录。10 月的澳洲航空事件涉及 570 万唯一客户，企业拒绝赎金后数据被公开。同月份的越南航空事件宣称泄露 2300 万条记录，Have I Been Pwned 验证其中包含 730 万个唯一邮箱。

2025 年 11 月上架的 Millicom 也就是 Tigo 数据集，宣称包含 3.8 亿条记录，容量 1.3TB，攻击者声称利用 CVE-2024-2577 窃取 AWS 凭证并下载 S3 数据库备份。但这个 CVE 编号对应的是 SourceCodester 员工任务管理系统的 IDOR 漏洞，属于完全不相关的开源 PHP 应用，与描述的攻击向量完全不符，不能作为防御参考。更多分析认为这批数据来自 2024 年 1 月 Tigo 巴拉圭业务的勒索软件事件，是早期入侵的长尾勒索阶段。

2026 年 4 月出现了集中上架潮，七天内新增五份售卖清单，包括 Cisco 的源码与云密钥，Santander 的银行卡数据，Vercel 的访问权限与源码，Compass 的全套管理员权限包，以及 Anthropic 的 Claude 模型相关数据。其中 Anthropic 的宣称内容，包括十万亿参数规模、20TB 模型体积、可用零日漏洞等，与公开的大模型架构常识不符，业内普遍评估可信度极低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqp8QfXfNCT2HcaQmSQbwXu4fNEdtGSHGLHfQSMo8KzKaufOVDtOgnOMOmvFlWYTLYrBDuIR64P1Zfe6YmZruzr05aGYZvMsF4/640?wx_fmt=png&from=appmsg)

值得注意的是 Vercel 与 Compass 的售卖内容打破了该品牌的历史模式，不再单纯售卖导出的数据，转而售卖实时的系统访问权限。Compass 的权限包同时包含身份提供商 Okta、支付处理商 Stripe 与代码托管平台 GitHub 的访问权限，标志着该品牌从数据中间商，转向活跃的访问权限服务商。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoJjIrJ5E42W53L2G3EYQHcEh2bPBcFM76X3tu9gib15DzbKBN4fX3UOoV...