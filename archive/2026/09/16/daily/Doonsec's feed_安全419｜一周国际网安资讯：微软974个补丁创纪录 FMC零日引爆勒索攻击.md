---
title: 安全419｜一周国际网安资讯：微软974个补丁创纪录 FMC零日引爆勒索攻击
url: https://mp.weixin.qq.com/s/8LPyHbySExj9kcnTu1VLrQ
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:55:15.066326
---

# 安全419｜一周国际网安资讯：微软974个补丁创纪录 FMC零日引爆勒索攻击

# 安全419｜一周国际网安资讯：微软974个补丁创纪录 FMC零日引爆勒索攻击

原创

安全419
安全419

安全419

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Nf1wzzcfwM7skCmo2AsiaOPk5KxJmgyZBKHIYxEqtD1k7YXAXyJOnM7MlqTWYSvwh5oibFHLuR1gTnecAFh4fvHpzpp7CFib4hgQYiaTziabkXU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwNibMMzgialfhfYN40ib5wGRONQVibPbU7pyThia37SibefB4KrOvFKfUbo58rGBjUIgqicpopEe6WMibfiaukzjotalM2gx0ucqcHWIucQ/640?wx_fmt=gif&from=appmsg)

**一周热点速览**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwM0YkpBKvZf4PlXl7mOfUzxRVQ3QfwoKHiblhfCpb1GIZvGpIGAtBqJfCxShKhiahLF0k6e3aYe6MurIhAnpzXAiac1WXqEicKRKEo/640?wx_fmt=gif&from=appmsg)

上周（2026年9月9日至9月15日）全球网络安全领域迎来"补丁超级周"：微软9月Patch Tuesday一次性修复创纪录的974个漏洞，其中两个Windows零日已在野利用；Cisco Secure FMC满分漏洞被确认遭利用，攻击者窃取凭据后直接部署Qilin勒索软件；Chrome V8引擎再曝零日；SAP内核10.0分漏洞可未认证远程接管。与此同时，一个名为BlueMoon的漏洞利用套件一周内被四个间谍组织使用，APT31首发并链式Chrome零日。执法方面，美国捣毁东南亚诈骗园区单日冻结5280万美元加密货币，乌克兰Conti开发者被判4年。政策层面，欧盟《网络弹性法案》（CRA）第14条正式生效，ENISA上线单一报告平台。以下为主要国际网络安全资讯汇总。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwOj08BXicn74rVtK4DeOzPNBQxQl7x9knYEyPr6xuYMuSeFtkJBLvRAGxtuw40UGicn5yH1qtvMNy5DGt5xcAtaCu62nQSwgEskE/640?wx_fmt=gif&from=appmsg)

**一、漏洞预警**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwOSM7ZLszjDShuxAIFT7iaQmDl4GcAaSb80z3nkzup0QT641ibfMPDKicAicFtmRFlSLicC389vUD6XOHJ1ZWWichEh8Icb1qLuSG888/640?wx_fmt=gif&from=appmsg)

**微软9月Patch Tuesday创纪录修复974个漏洞**

微软于9月9日发布9月安全更新，一次性修复了创纪录的974个安全漏洞，远超8月份457个和7月份663个的补丁数量。其中Windows修复723个，Office及Office 2016修复111个，SQL Server修复62个，开发工具修复22个，另有超过110个漏洞被评为严重级别。权限提升、远程代码执行和信息披露三类漏洞占近90%。更引人关注的是，其中两个Windows漏洞已被确认在野外积极利用。此外微软还修复了25个非微软CVE漏洞，总计解决999个漏洞。安全专家指出，在如此大规模的补丁浪潮面前，企业面临的最大挑战不是"打完所有补丁"，而是"确定哪些最需要优先修补"。

**Cisco Secure FMC认证绕过漏洞遭在野利用**

思科于9月9日确认其Secure Firewall Management Center（FMC）软件中的认证绕过漏洞CVE-2026-20079（CVSS满分10.0）正在被积极利用。该漏洞允许未认证的远程攻击者绕过身份验证，在受影响设备上执行脚本并获取操作系统root权限。同时被利用的还有CVE-2026-20316（CVSS 5.3）。思科Talos威胁情报团队报告显示，攻击者利用这些漏洞窃取网络设备凭据，并进一步在受害网络中部署Qilin勒索软件。CISA于9月9日将该漏洞加入已知被利用漏洞目录（KEV），要求联邦机构在9月12日前完成修复，期限仅三天。FMC作为企业防火墙集中管理平台，一旦被攻破可影响整个网络安全基础设施，属于典型的"单点突破、全域沦陷"型漏洞。

**Chrome V8引擎零日漏洞在野利用**

谷歌于9月9日发布Chrome安全更新，共修复230个安全漏洞，其中V8引擎的越界写入漏洞CVE-2026-87491已被确认在野外积极利用。攻击者可通过精心构造的HTML页面，在Chrome沙箱内执行任意代码。修复版本为Chrome 153.0.8010.36。这是继上月CVE-2026-85046之后Chrome V8引擎曝出的又一个在野零日漏洞，短短一个月内连续两个V8零日，显示浏览器引擎仍是网络攻击的核心目标。

**SAP内核CVSS 10.0漏洞未认证远程RCE**

SAP于9月9日发布月度安全更新，修复其Extended Passport（EPP）处理组件中的严重漏洞CVE-2026-44756（CVSS满分10.0），代号OVERPASS。该漏洞由SAP安全公司Onapsis发现，存在于SAP内核处理EPP数据时的反序列化过程中，由于缺少边界验证导致内存安全违规。攻击者无需任何认证即可远程利用，在SAP主机上以SAP管理员权限执行任意操作系统命令，完全危及SAP业务数据和流程的保密性、完整性和可用性。SAP系统广泛应用于全球大型企业的核心ERP、供应链和财务流程，该漏洞的潜在影响面极大。企业应尽快评估受影响系统，优先修补暴露在网络中的SAP实例，并加强对SAP管理端口的访问控制。

**N-able N-central预认证RCE漏洞入KEV**

CISA于9月9日将N-able N-central远程监控管理平台中的严重漏洞CVE-2026-86218加入已知被利用漏洞目录（KEV），要求联邦机构在9月11日前完成修复。该漏洞为静态代码注入，可导致预认证远程代码执行，CVSS评分满分10.0。N-able于9月5日在2026.3 Hotfix 4中发布了补丁。N-central是广泛使用的MSSP和企业IT管理平台，一旦被攻破可影响大量客户系统。这是本周继Cisco FMC之后又一个管理平台类满分漏洞，再次凸显网络管理工具已成为攻击者的首要目标。

**研究员公开Microsoft Defender ShieldCrash补丁绕过PoC**

安全研究员Chaotic Eclipse于9月9日发布Microsoft Defender另一个零日漏洞的概念验证（PoC），代号ShieldCrash，被评估为对CVE-2026-69414（又称ShieldBreak，CVSS 7.8）的补丁绕过。研究员表示微软未能正确修补ShieldBreak，在特定条件下仍可触发完全相同的问题。安全产品自身的漏洞一直是攻击者关注的高价值目标，Defender作为Windows默认安全产品，其漏洞影响面极为广泛。这也提醒安全团队，不能盲目信任安全产品的完整性，需要对安全工具本身进行独立验证。

**Alby Hub比特币钱包关键漏洞可接管互联网暴露钱包并转走资金**

比特币钱包公司Alby于9月9日警告，其自托管闪电网络钱包Alby Hub存在一个严重漏洞，可能让攻击者接管互联网暴露的钱包并转走资金。漏洞影响v1.7.0至v1.18.5版本（均为2025年8月之前发布），目前已知有一名用户受影响。v1.19.0及之后版本已修复此问题。Alby建议仍在旧版本的用户首先停止外部访问Hub管理界面，然后升级到v1.24.0当前版本。该公司暂未公开漏洞详情，计划稍后发布完整信息。自托管加密货币钱包一直是攻击者的高价值目标，任何暴露在互联网上的钱包服务都应谨慎，建议通过VPN或本地访问方式管理。

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwO3nD7lCquWOhyj4tL5asU5onadphlJKj45bnszUAneibAqGfcqmcMEBBuibdQnurmbzDgs2ib4vK1X5BsrWjGmae33JiaESExYtp0/640?wx_fmt=gif&from=appmsg)

**二、安全事件与攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwO0agU6ATrkVib12RiaqtBsFMhUobERGiaH6uthC1OXROmSOQBGJnalOAPAcWdOF4vR0yy119fUSibOgWITAqLbbOibtddzlybqOXgg/640?wx_fmt=gif&from=appmsg)

**BlueMoon漏洞利用套件一周内被四个间谍组织使用**

Proofpoint于9月9日发布报告，披露一个此前未公开的漏洞利用套件BlueMoon，在短短一周内被四个不同的间谍组织使用。该套件链式利用多个Windows和Chrome漏洞，首次在野使用被归因于APT31组织，时间为8月28日。数日内，其他几个间谍组织也开始使用BlueMoon。利用链包括Chrome V8类型混淆漏洞CVE-2026-85046及一个V8沙箱逃逸漏洞。这一事件表明漏洞利用套件正在成为高级持续性威胁组织间共享的标准化武器，一旦某组织开发出高质量利用链，很快就会在地下市场扩散。

**DeepSeek Harness漏洞致AI代理可关闭自身沙箱**

安全公司OX Research于9月8日披露DeepSeek开源工具Harness中的漏洞CVE-2026-82533（CVSS 9.4）。Harness是用于在开发者机器上运行AI编码代理的工具，默认将代理命令运行在操作系统沙箱中，防止代理在处理不可信文件时写入工作区外。但该漏洞允许沙箱内的代理通过调用工具自身的Web界面，用一条命令关闭沙箱限制，且无需用户批准。漏洞在默认安装中即可利用，需要攻击者提供代理会读取的文本内容来触发。DeepSeek已于8月27日修复了该漏洞。

**美国捣毁Xinbi Guarantee骗局市场**

美国司法部于9月9日宣布采取协调行动，打击名为Xinbi Guarantee的非法在线骗局市场，查封了用于运营该服务的Telegram频道，没收两个加密货币钱包，并部署"骗局中心打击特遣队"前往马达加斯加，协助捣毁13个诈骗园区。司法部表示，单日内约5200万美元涉及诈骗洗钱的加密货币被冻结。这些东南亚诈骗园区每年从美国受害者手中窃取数十亿美元，采用"杀猪盘"、虚假投资、假冒客服等多种骗局手法。此次行动是美国打击海外电信网络诈骗的重要升级。

**乌克兰Conti勒索软件开发者在美国被判4年监禁**

曾参与Conti勒索软件团伙的乌克兰公民Oleksii Oleksiyovych Lytvynenko于9月11日在美国被判处4年监禁。他于2023年在爱尔兰被捕，后被引渡至美国。Conti是2020至2022年间最臭名昭著的勒索软件团伙之一，攻击了全球数百家企业和医疗机构，造成数亿美元损失。Lytvynenko作为开发者参与了Conti勒索软件的开发和维护。

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwPiadHsyCxnEyPXICVj9Qlicic4ZdtLvWKwkWz4HphjDCwmoHKRDob9VMwKylNkB460B8pIgGUDVbn84pML9zrwwVO2Wdm5RdnQibM/640?wx_fmt=gif&from=appmsg)

**三、政策法规**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwOzvuUUrjPsoYyvzGyH2gCxENHicdyIULlD5kbSebOwtOHIrkNZfzhB5EbeCUayXqibHXFeqI2LVlicVs8hNOWlDlUsOBzhHBWEOQ/640?wx_fmt=gif&from=appmsg)

**欧盟网络弹性法案（CRA）正式生效，ENISA上线单一报告平台**

欧盟《网络弹性法案》（CRA）第14条报告义务于9月11日正式生效，欧洲网络安全局（ENISA）同日上线单一报告平台（SRP），制造商和开源软件维护者可通过该平台一次性提交主动披露的漏洞和严重事件报告。报告将发送给制造商主要营业地所在国的CSIRT，同时共享给ENISA。制造商需在发现被积极利用的漏洞后24小时内提交预警报告，72小时内提交详细报告。ENISA还发布了漏洞披露延迟机制（PEC）指引，协调CSIRT可决定是否延迟公开披露。CRA是欧盟近年来最重要的网络安全立法之一，对所有向欧盟市场销售数字元素产品的企业具有约束力。中国出海企业需特别关注CRA合规要求，建立内部漏洞报告和应急响应流程，避免违规风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwOzlIpZFB1dcaibdbvwYUxPeEY0peiceGk3uuLt82CESKiaJl4G6icFhWzzHdKQF0fiauOQpchRxotia5fXf52SgaickBQfoo3oVkicE5Y/640?wx_fmt=gif&from=appmsg)

**四、产业动态**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwNZGcD4UmO43gQ8siaAHy6U6kICNJyic1BdC9YGfEsdHXcGrXMA4biaHxF2Yw35kicjDxW44CFKmPRVcrdoDI57yuxq8a4VNfDalPM/640?wx_fmt=gif&from=appmsg)

**CrowdStrike收购XM Cyber知识产权**

CrowdStrike于9月10日宣布与Schwarz Digits扩大战略合作伙伴关系，签署最终协议收购XM Cyber的知识产权。XM Cyber是一家以先进攻击路径可视化和攻击模拟技术闻名的公司，拥有45多项专利和源代码。CrowdStrike表示，随着前沿AI加速发现、链式利用漏洞的速度，企业正在用Falcon平台替代零散的单点工具，将持续安全监控统一在单一平台上。此次收购是CrowdStrike近期一系列AI安全和身份安全收购的延续，此前已收购SGNL（连续身份安全）和Seraphic（浏览器运行时安全）。安全行业的平台化整合趋势持续加速。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwMlFNDKNfSs2SEzBpZt89T8vnu4avSFwQgrecDs2GKibalN4sKRVibVhwPDoMpHibR6xgzh1Sic7ia6fYUzQM71WWTsycOhJib36SjiaE/640?wx_fmt=gif&from=appmsg)

**四、本周安全建议**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwPua1DYKRvlwibUIhC7AEtuJQhakfPZtUlZpq1Mc0ua4gd36zzj4XbWyMticxJDzYHibx6TWmc0LBoT54DTdWOXn31KmA2AsicYVLc/640?wx_fmt=gif&from=appmsg)

**紧急修补：**立即部署微软9月累积更新，优先处理两个在野利用的Windows零日；修补Cisco Secure FMC CVE-2026-20079（CVSS 10.0）、Chrome 153.0.8010.36、SAP内核CVE-2026-44756、ConnectWise ScreenConnect 26.6.5、N-able N-central 2026.3 Hotfix 4及cPanel最新版本，全部为本周新确认在野利用或满分级漏洞。

**管理平台加固：**本周FMC、N-central、ScreenConnect等管理平台漏洞密集，应立即审查所有暴露在互联网上的远程管理和监控平台，限制管理端口访问IP范围，启用强认证和MFA，监控异常登录和配置变更。

**AI安全治理：**针对信息窃取者窃取AI令牌、DeepSeek Harness沙箱绕过等事件，企业应审查内部AI服务使用情况，实施API密钥轮换机制，监控异常AI API调用，对AI代理的沙箱隔离机制进行独立验证，防止AI代理越权操作。

**欧盟CRA合规：**向欧盟市场销售数字产品的企业需立即启动CRA合规准备，建立内部漏洞报告和应急响应流程，确保能在24/72小时内通过ENISA SRP平台完成报告，避免面临最高达全球营业额7.5%的罚款。

**免责声明**

本周报内容由安全419编辑部基于公开资讯整理汇总，旨在为网络安全从业者提供参考信息，不代表安全419的立场和观点，我们已尽力确保信息的准确性和完整性，但不对信息的及时性、准确性、完整性做出保证，同时也不构成任何安全建议、法律意见或投资推荐。依据以上内容做出任何决策前，都应独立进行进一步核实和研究，对于因使用以上内容而导致的任何损失或损害，安全419概不负责。

END

✦

**推荐活动**

✦

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Nf1wzzcfwM2xzoTCvqLIFdmprru9pVXDMCzzicIibKjwiccyYc1l6jQfDPOxLw5C95fLwxbwZ7TAFuwVxJIDicDczZdjd6ux1rSTxLAPLicGlb4/640?wx_fmt=jpeg&from=appmsg)

✦

**推荐阅读**

✦

[![](https://mmbiz.qpic.cn/mmbiz_png/9Nf1wzzcfwOec7KM5M0H6P1X32IVxY8DcicLFmajHqRH1d6j5Kf4WN8b0wItacI0k8hdicmq0ibpT0LBhx6Zq59PJvKb3oQznqPvbFuN7ibvPyU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzUyMDQ4OTkyMg==&mid=2247555004&idx=1&sn=df8849c9cbe3ed3659747a8...