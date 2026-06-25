---
title: 安全419｜一周国际网安资讯：FortiBleed席卷全球 AI安全治理迫在眉睫
url: https://mp.weixin.qq.com/s/VnUPwr8lvcDqUIRNnsczEw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:00:02.808518
---

# 安全419｜一周国际网安资讯：FortiBleed席卷全球 AI安全治理迫在眉睫

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Nf1wzzcfwNgghQEg6j5m7QaQjqPQLUGGPUaA2Nluv7bATueKkqe7hM125K7rXtTOJSbWHibP0hJQZicyHKKDYxVLyPvKZbDwicgpibIqS0y9u4/0?wx_fmt=jpeg)

# 安全419｜一周国际网安资讯：FortiBleed席卷全球 AI安全治理迫在眉睫

原创

安全419
安全419

安全419

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Nf1wzzcfwPc9HrySgwRl3mwY1UHX1ibaR4ZIGyv2R0fXIvWxAcjbNMTHfW3W1cCyogRZO9KwBvLdL0SVVFo9XR8kbfUSPYtQWF2CBndiary4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwOt0I5uL9HnxlhlVezrAIFyJ5NwquW0LMvhIDzOEe0scElG9BaCnL2rzN0pAPkfFbQiag5e54FaZldDS0egUia6jUBNTwWDV1ypQ/640?wx_fmt=gif&from=appmsg)

**一周热点速览**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwNytYGdHzwA4micw9ILchEXI4qeXBBeCKicbtTzoGEyIbxs8bS71GmjjOU52bibhMA6xf3icKazB5WmWAzH3MAfxzKickHx3Rsxpnuk/640?wx_fmt=gif&from=appmsg)

过去一周（6月17日至6月23日）全球网络安全动态呈现多线并发的严峻态势。FortiBleed事件持续发酵， APT组织针对全球超7.5万台Fortinet防火墙发起大规模凭证收割行动，超过1.1亿条凭证被窃取，引发多国网络安全机构紧急预警。供应链攻击事件频发，Klue OAuth令牌被盗导致LastPass等知名企业客户数据泄露，ShapedPlugin和Awesome Motive CDN等WordPress生态供应链相继沦陷。漏洞方面，三星KNOX内核UAF漏洞（已存在8年）、Squid代理29年历史漏洞Squidbleed、DifyTap四个严重漏洞等相继曝光，AI应用安全面临严峻挑战。APT攻击层面，DragonForce组织成功潜伏Microsoft Teams长达两个月未被发现。数据泄露事件持续高发，Xsolis、德州公园与野生动物部门、iRhythm等医疗健康机构成为主要攻击目标。政策法规方面，五眼联盟发布联合警告呼吁全社会响应AI驱动的网络安全威胁，特朗普签署行政令加速后量子密码学部署。本周事件表明，供应链安全、云安全配置、AI治理已成为全球网络安全的核心议题。

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwP03VtfOFGnVGGZjZLIrplNwXLpZ2Q87YTpuT10uD2onjXImb4aWoniaNHa8QicuydjgUAuOJibDQlyXuQ8An1DbZp0QlkHWD8fN8/640?wx_fmt=gif&from=appmsg)

**一、安全事件**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwM5iaice9KoIx5dL2MyMHXYTvooX7CV2AAnM6bN8tlBRYdyDfbRicY0am6nq4Oia22QZAEZXSAp2ibTvI3uQ5LoAwUse84N1vONlSvI/640?wx_fmt=gif&from=appmsg)

**FortiBleed凭证风暴：超7.5万台Fortinet防火墙管理员密码泄露**

代号"FortiBleed"的大规模网络攻击行动正在全球范围内肆虐， APT组织针对Fortinet FortiGate防火墙设备发起持续攻击，成功窃取超过7.5万台设备的管理员密码，并疑似收割了超过1.1亿条各类凭证。

攻击者利用Fortinet设备中的未知漏洞（或组合利用多个已知漏洞），成功绕过身份验证机制，获取设备最高管理权限。一旦获得控制权，攻击者在内存中植入恶意代码，将经过该防火墙的所有流量中的凭证信息进行实时抓取和数据外泄。这种"凭证收割机"式的攻击手法极为隐蔽，设备管理员难以通过常规日志发现异常。

根据不完全统计，全球范围内已有超过7.5万台FortiGate防火墙受到波及，涉及政府机构、金融机构、医疗组织、教育机构等多个关键领域。更令人震惊的是，攻击者构建的凭证数据库中已包含超过1.1亿条各类凭证，这些凭证正在地下市场被出售或用于进一步的攻击行动。

事件曝光后，美国CISA、澳大利亚ACSC等多国网络安全机构相继发布紧急警报，敦促各组织立即检查Fortinet设备是否存在异常，并强制重置所有管理员密码。Fortinet官方已发布情况分析报告，承认部分设备遭到入侵，但强调大部分在运行的设备已通过自动更新获得防护。

安全419建议立即审计所有FortiGate设备的登录日志，重点关注异常IP来源；强制重置所有管理员和用户的密码，并启用多因素认证；部署网络流量监控，检测是否有异常的数据外泄行为；考虑在网络边界部署额外的IDS进行深度包检测。

**DragonForce组织潜伏Microsoft Teams两个月未被发现**

英国威胁情报公司ReliaQuest披露，代号为"DragonForce"的黑客组织成功渗透目标组织的Microsoft Teams环境，并在其中潜伏长达两个月之久，期间持续窃取敏感信息，直至被安全团队发现并驱逐。

攻击者首先通过钓鱼邮件或凭证填充攻击获取了低权限的用户账号，随后利用Microsoft Teams的合法功能和API接口，逐步提升权限并扩大访问范围。由于Teams是企业日常协作的核心工具，其流量通常被安全设备视为"可信流量"，攻击者借此规避了多数安全检测。在潜伏期间，攻击者加入了多个敏感项目团队，访问了包括战略规划、财务数据、产品开发路线图在内的核心机密。

DragonForce展示了高超的"Living off the Land"（就地取材）能力，几乎完全依赖Microsoft 365生态内的合法工具和权限进行操作，避免了引入外部恶意软件带来的暴露风险。他们还利用Teams的第三方应用集成功能，将窃取的数据通过看似正常的"文件共享"操作外传到攻击者控制的外部存储。

传统的安全监控方案多聚焦于端点和服务器的异常行为，对SaaS应用内部的可疑活动缺乏可见性。Microsoft 365的审计日志虽然记录了相关操作，但海量日志中识别APT行为的难度极大，尤其当攻击者的操作模仿了正常用户行为时。

专家建议部署专门的SaaS安全态势管理工具，对Microsoft 365等核心SaaS应用进行持续监控；启用Microsoft 365的高级审计功能，保留至少90天的日志以供溯源分析；建立基于UEBA的异常检测机制，识别账号行为的偏离；定期对员工进行安全意识培训，警惕针对协作工具的社会工程攻击。

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwPOibRlIQecMRNogJrydG03ZwoS0IkPjrLlrFxc7ALNHn3swZ3ADep71SzRxibru6k11WLAfdLiciadXibRKhjlDNCXwqMn5Gk3uQF0/640?wx_fmt=gif&from=appmsg)

**二、漏洞预警**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwMCNeyDpURx6XkbPnV60FKBNvlHDjBgrEp1XicV9WwmJhM9ByILrDe4cV3WjiaNSy9QQo4ibYPh4aw5bfPQ4bh200fvC6XVlwK1ts/640?wx_fmt=gif&from=appmsg)

**三星KNOX内核UAF漏洞暴露数百万Galaxy设备**

安全研究人员在三星KNOX安全框架的核心组件中发现了严重的UAF漏洞，该漏洞已存在长达8年之久，影响几乎所有运行KNOX的Galaxy设备，包括最新的S系列和Note系列旗舰机型。

KNOX是三星为企业用户和政府机构提供的安全平台，用于在设备上创建隔离的安全容器和运行环境。UAF漏洞发生在内核处理特定IOCTL（输入输出控制）请求时，攻击者可以通过精心构造的恶意应用触发内存破坏，从而获得内核级别的代码执行权限。

一旦成功利用该漏洞，攻击者可以绕过KNOX的所有安全隔离机制，访问安全容器内的敏感数据，甚至可以在设备上植入持久化的rootkit，实现长期隐蔽控制。由于漏洞位于内核层，传统的应用层安全防护无法有效检测。

KNOX被广泛用于政府、金融、医疗等高度监管行业，全球有数百万台设备受到影响。更严峻的是，由于漏洞已存在8年，无法确定是否已有APT组织在实际攻击中利用该漏洞。三星已发布安全公告，但部分老旧机型可能无法获得补丁。

建议立即检查设备是否收到三星2026年6月安全更新，并尽快安装；在企业移动设备管理策略中，暂时禁止存在漏洞的设备访问企业资源；考虑在企业环境中部署移动威胁防御（MTD）解决方案，对设备内核行为进行实时监控。

**Squidbleed：29年历史的Squid代理漏洞泄露用户凭证**

代号"Squidbleed"的安全漏洞在广泛使用的Squid代理服务器中被发现，该漏洞自1997年Squid项目启动以来就已存在，已有29年历史，堪称"化石级"漏洞。该漏洞可导致经过代理服务器的HTTP请求以明文形式泄露，包括用户认证凭证。

Squid是全球使用最广泛的代理服务器之一，特别是在企业网络、ISP、CDN等场景中。估计有数十万台服务器受到影响，其中不少仍在运行多年未更新的旧版本。由于漏洞涉及明文凭证泄露，其危害程度极高。

目前，Squid开发团队已发布修复版本，建议所有用户立即升级。对于无法立即升级的系统，可以临时禁用详细日志记录，并配置严格的访问控制列表（ACL）限制对代理服务器的访问。

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwNY53pzQKibGic7I9542VgRxWicvVicsZev1jGuWfgfHKZFyjv2DTfYKrakJib75HqjGXD5BfvWZSml4r6ZZt594gerSNRbF9Moy7UQ/640?wx_fmt=gif&from=appmsg)

**三、供应链攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwPc0CwOaawSHruoll942bm8AvmB7vv3n3pLK1GIBfric3otibBj97Z00ibaNctXZbxqysWniboGGafp8ibm95tDJfNgEO1lNZgtyVcs/640?wx_fmt=gif&from=appmsg)

**Klue OAuth令牌被盗导致LastPass等客户数据泄露**

客户情报平台Klue遭遇供应链攻击，攻击者通过未知手段窃取了Klue用于访问Salesforce集成的OAuth令牌，随后利用该令牌访问了Klue的Salesforce实例，导致包括LastPass在内的多个Klue企业客户的敏感数据被窃取。

LastPass已确认其部分客户数据在事件中泄露，包括客户姓名、电子邮件地址、电话号码、账单信息等。虽然LastPass强调密码库的主密钥未受影响，但此次泄露的数据仍可用于发起针对性的社会工程攻击或钓鱼攻击。其他Klue客户也可能受到影响。

在获知事件后，Salesforce迅速禁用了Klue的集成权限，并配合执法部门展开调查。但此事件暴露了SaaS应用生态中OAuth令牌管理的脆弱性：多数企业在授予第三方应用权限时缺乏足够的审查和监控，且很少定期审计已授权的OAuth令牌。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwP89o8BzFr1trcYsicS7PbHkG8n7sWxXSPjNE629GBMfyryVOL2aqqicFyO31zUjS3icOSXPQS8hhc1lYsA2sZLcEcmbNNnlIODe8/640?wx_fmt=gif&from=appmsg)

**四、恶意软件**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwOBd2Z41as0vJzxr6vJRyzrus0zJfHtRmt3oia54s394NPIjXYiaQHiautj3AY2anM88lUPCiaEaakFqIKOZaic8HSVrIMmf4QkZBbQ/640?wx_fmt=gif&from=appmsg)

**WhatsApp恶意软件攻击活动劫持信任安装合法管理工具**

安全研究人员发现了一场针对WhatsApp用户的全球性恶意软件攻击活动，攻击者通过WhatsApp消息发送看似合法的文档，诱导用户点击后下载并执行VBScript脚本，最终在受害者的设备上安装合法的远程管理工具（如ManageEngine RMM）。

攻击主要通过WhatsApp的消息功能进行传播。攻击者伪装成同事、朋友或业务伙伴，发送带有社会工程学诱导的消息。由于WhatsApp的端到端加密特性，安全网关和邮件过滤器无法对这类消息进行检测。

该攻击活动已在全球范围内蔓延，尤其针对企业高管和IT管理员。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwMBk2AxVLZkaYXbfSJ83IJUOyvq0VTfLac8xiaw05HpicfTDcH1k0aSVyFDiawHbPPOXP8yzjDvDRgo8mldLGHtsLIOaoJ0CDDHy0/640?wx_fmt=gif&from=appmsg)

**五、数据泄露**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwNNVyNhwQJcRNEZf5IDeLp4JiaTtybDuSibnrmMfLDuY27TrsibfA29pONCeG6cdjeU212AeMyeycN5fia4MY4wgCD65HAKgYSTEv8/640?wx_fmt=gif&from=appmsg)

**Xsolis数据泄露影响140万人**

医疗技术公司Xsolis通报一起重大数据泄露事件，攻击者非法访问了其系统中存储的约140万人的个人和医疗信息。受影响的数据可能包括姓名、社会保险号、医疗记录、账单信息等高度敏感数据。

Xsolis已通知美国卫生与公众服务部（HHS）民权办公室，并正在向受影响个人发送书面通知。公司提供了为期两年的免费信用监控和身份盗用保护服务。但此类事后补救措施无法消除数据已被泄露的事实，患者仍需长期警惕可能出现的身份盗用和诈骗。

医疗数据的泄露不仅会导致身份盗窃和保险欺诈，还可能对患者的心理健康造成损害。此外，医疗行业一直是数据泄露的重灾区，医疗数据在地下市场的价格远高于普通身份信息，单个医疗记录的售价可达数十至数百美元。医疗机构掌握的海量敏感数据、相对薄弱的网络安全防护、以及业务对可用性的极高要求，使其成为攻击者的理想目标。监管机构应加大对医疗行业网络安全的审计和执法力度。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwMHyiaV82JH68uZSemLuTnTt6SuVYOT8uibb3j0yO5febZbnjnL9YI39GXcRia8LhS5Wup6M8zl8MuPeV25sicLhfBV07iafZoWNOU0/640?wx_fmt=gif&from=appmsg)

**六、勒索软件**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwNpKV4uN1v1vxeK3wqDHHI0SbRpkWBOUyCNpCtSOGYNxQuEcgYX2c1gOn5omR9ZwMSnruN2ka7o9m3S1iawIHI7QZaVgao2rUOE/640?wx_fmt=gif&from=appmsg)

**巴贾吉汽车遭遇勒索软件攻击，内部系统受影响**

印度最大的摩托车制造商巴贾吉汽车（Bajaj Auto）通报遭遇勒索软件攻击，部分内部IT系统受到影响。公司已紧急启动应急响应机制，隔离受影响系统，并配合执法部门展开调查。

制造业一直是勒索软件组织的高频攻击目标。与金融、医疗等行业不同，制造企业的生产线高度依赖IT/OT的融合，一旦系统被加密，生产将直接中断，造成的经济损失每小时可能高达数百万美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/9Nf1wzzcfwMBAefkftwicUqDiaTZM1Vm2VLzhoIlnTWlhTl2O6iaoZtFMr5YoyOBevuHfutHdiaNPObhH9Pn6N3gaicgKw0ArTc7EeiaWPlb3UbT4/640?wx_fmt=gif&from=appmsg)

**七、政策法规**

![](https://mmbiz.qpic.cn/mmbiz_gif/9Nf1wzzcfwOfwDxWnJfW98XOHxqWuTxXzZwsYiaicEOWV2AgUyGURHSw1PibcNMGNSicNiawmYOlOtP1ROK6s4WwZxNsnUXvMpo03Q1WzzMzQhD0/640?wx_fmt=gif&from=appmsg)

**五眼联盟呼吁全组织全社会响应应对AI驱动的网络威胁**

美国、英国、加拿大、澳大利亚和新西兰的网络安全机构（统称"五眼联盟"）发布联合警报，警告AI技术正在"快速改变"网络安全风险格局，呼吁各组织和社会各界采取紧急行动应对AI驱动的威胁。

五眼联盟在警报中特别强调了以下几点：1）AI大模型可被用于规模化生成高度逼真的钓鱼邮件和社会工程攻击，大幅降低了攻击门槛；2）AI代理（Agentic AI）具备自主规划和执行复杂攻击的能力，传统的基于规则的防御体系难以应对；3）AI系统的训练数据和模型本身成为新的攻击面，数据投毒、模型提取、对抗样本等攻击手法层出不穷。

五眼联盟向各组织提出了一系列建议，包括：建立AI安全治理框架，对AI系统的开发、部署、使用进行全生命周期管理；加强对AI生成内容的检测和标记能力；提升安全团队的AI素养，使其能够理解和应对AI驱动的攻击；在政府层面推动AI安全国际标准的制定。

**免责声明**

本周...