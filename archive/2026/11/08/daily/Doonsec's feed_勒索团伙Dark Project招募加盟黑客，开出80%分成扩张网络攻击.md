---
title: 勒索团伙Dark Project招募加盟黑客，开出80%分成扩张网络攻击
url: https://mp.weixin.qq.com/s/Xw8yrTYBH2jISQg1GbI1yg
source: Doonsec's feed
date: 2026-11-08
fetch_date: 2026-11-09T08:52:50.714209
---

# 勒索团伙Dark Project招募加盟黑客，开出80%分成扩张网络攻击

# 勒索团伙Dark Project招募加盟黑客，开出80%分成扩张网络攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3qH8AApFUqjszW69ePibZwDfiac2ZILlxldpHm5U0gwxUDibxHqicpg5vvBKZHCoft1EFMMB8ufSZOjLOYq45VO3QFViaYMia4vAazM/640?wx_fmt=gif)

![Dark Project招募加盟黑客](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX133ggBvtiahibvAq5yGDzSsYsBpedSibLwibrrJVgMUUaD54kKNOZicaDQHTQOYiagUoQ7obVO7WicNFHWyFrQnYnMT2V1S2sK5iakRib8/640?wx_fmt=png)

名为Dark Project的勒索软件团伙正在招募犯罪合作者，承诺攻击成功后合作者可获得80%的收益分成，同时还提供全套勒索管理平台支持。安全行业2026年6月首次监测到该团伙活动，其以牟利为核心目的，结合数据窃取、文件加密、公开泄露威胁三种手段胁迫企业支付赎金。

目前该团伙公开的受害者记录覆盖8个国家的38家机构，其中美国的机构占30家。制造业、医疗健康、建筑行业是受攻击最多的领域。值得注意的是，这些数据仅来自威胁情报平台和泄露站点公示的名单，既未经过独立核实确认入侵事实，也不能完整反映该团伙的全部活动规模。

Gurucul的研究人员在威胁行为者画像报告中披露了Dark Project的勒索活动，梳理了其招募流程、基础设施布局及公开宣称的攻击手法。报告显示，这一新兴犯罪团伙甚至套用合法安全服务的话术，宣传其面向勒索活动的工具与合作伙伴支持体系。

Part01

Dark Project推出80%高分成计划

Dark Project对外宣传的合作计划规定，加盟黑客可获得攻击收益的80%，剩余20%归团伙运营方所有，用于平台服务与运营报表相关工作。这种分成模式与其他成熟勒索团伙的RaaS联盟分成机制类似，但目前仅为团伙单方面宣传，无法证实其确实会按承诺向合作者支付分成。

其招募流程分为四个阶段：申请、审核入职、攻击部署、佣金结算。申请者需通过Tox联系该团伙。通过审核的合作者会获得专属身份标识、平台访问权限与操作指引，随后即可向目标机构投放攻击载荷。Dark Project称会全权负责与受害者的沟通、赎金谈判全流程，承诺在一笔勒索交易完成后24小时内结清对应佣金。

该团伙宣传的配套基础设施包括部署在Tor上的运营管理面板、EXE和BIN格式的代理程序，以及一套社工模拟工具套件。据称这些代理程序内置合作者专属标识，可将具体攻击活动关联到对应的加盟黑客。以上能力均为Gurucul记录的团伙单方面宣传内容，尚未有公开的恶意软件分析报告独立验证这些功能确实存在。

![比特币支付说明与加密货币结算流程（来源：Gurucul）](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1THob1H8lHUQHpgSROSiaIAOnXiciclsSgSeA1zYnQZemNIR1tHiactSrmM7Mh63nYWTZUO1dGxHYT2BSC8wtlTLn6eqtiaHdmTsgc/640?wx_fmt=png)

这种将载荷投放与赎金谈判拆分的模式，大幅降低了加盟黑客需要负责的运营工作。类似的联盟管理平台功能此前曾出现在Lynx勒索软件的运营模式中，其合作者可直接在平台管理受害者档案、数据泄露排期。Dark Project还宣传支持比特币支付，但现有报告并未提供相关钱包地址或交易记录，无法证实其确实完成过佣金结算。

该团伙的受害者公示数量在2026年8月达到峰值，当月共公示20家机构；6月公示4家，7月无新增公示；9月、10月各新增5家，截至报告数据统计时11月已新增4家。这些时间点仅对应团伙公示受害者信息的操作时间，不能等同于实际入侵发生的时间。

Part02

采用双重勒索作案模式

Gurucul梳理的信息显示，该团伙的初始接入途径包括钓鱼攻击、暴露在公网的远程桌面协议（RDP）服务、失陷凭证，以及从信息窃取木马日志或初始访问经纪人处购买的VPN访问权限。该团伙主要针对Windows环境作案，采用双重勒索模式：先窃取目标的敏感数据，再加密文件，若谈判失败就公开泄露窃取的数据。这种模式会带来业务中断、数据泄露两类独立风险。

区分这两类风险很关键，因为即使企业恢复了被加密的文件，也无法消除被盗数据被公开的威胁。此前关于数据窃取勒索手法的相关报告也指出，仅靠数据恢复无法应对所有勒索要求。Dark Project部署在Tor上的数据泄露站点就是公开施压的渠道，当团伙需要额外谈判筹码时，就会在站点上公布所谓的受害者信息。

报告将该团伙的活动映射到多种攻击技术，包括滥用合法账号、利用Windows管理规范（WMI）、RDP、SMB协议、数据外渗、文件加密，以及尝试破坏系统恢复流程。报告同时列出了相关漏洞，但并未提供足够的事件证据，无法证实所有列出的漏洞都是Dark Project实际利用的入侵入口。防御方需要注意区分"报告提及的关联漏洞"和"已被证实利用的漏洞"。

目前公示的受害者中，制造业有12家，医疗健康行业7家，建筑行业4家。这种行业集中分布的特征，意味着相关行业的机构需要将访问监控、恢复能力建设作为重点防御工作。Gurucul建议企业及时修补漏洞、强化访问控制、监控可疑活动、做好安全备份。安全团队在落地这些措施时，不需要默认所有加盟黑客都会遵循完全相同的入侵流程。

Part03

失陷指标（IoCs）

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX04CCDBvIh8LHV0qtNbMLgRrPwNvMH0YLfQf9roTlqmq0Eqia9v1IubI5lgdOO3y70Jl3oF6LKfxSfDBibb27PrZ6O6JXh00dVko/640?wx_fmt=png&from=appmsg)

注：报告中的IP地址与域名均已做无害化处理（例如将.替换为[.]），防止意外解析或点击跳转。请仅在MISP、VirusTotal或内部SIEM等受控威胁情报平台中恢复原始地址。

参考来源：

New Dark Project Ransomware Group Offers Hackers 80% Commission to Expand Cyberattacks

https://cybersecuritynews.com/new-dark-project-ransomware-group/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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