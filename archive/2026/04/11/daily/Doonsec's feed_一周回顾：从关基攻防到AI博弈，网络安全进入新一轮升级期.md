---
title: 一周回顾：从关基攻防到AI博弈，网络安全进入新一轮升级期
url: https://mp.weixin.qq.com/s/uroAJt3MWYnYAIoK-Qud5A
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:47:20.009671
---

# 一周回顾：从关基攻防到AI博弈，网络安全进入新一轮升级期

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mSqhDgeKrPD1jRZbFcrDtFoMAVXppdF1hrZEibc9ibDQLh2717lib8c1Xbz7dibyj2AMCTNsNdVe4Yt83hxr0DoZ1zRib3ywxjQV362CM0dK9ib3o/0?wx_fmt=jpeg)

# 一周回顾：从关基攻防到AI博弈，网络安全进入新一轮升级期

奇安信集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![安全态势头图](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarbeibXRgFiaLhJj1QdgPcxzLh3OFl0EicBlXUMStdia9vxEro6xT4wLKAYU4rUOOX1ibfaUpT6ZRibL4gw/640?wx_fmt=jpeg&from=appmsg)![]()

本周全球网络安全态势加速向“高烈度、实战化、智能化”演进。伊朗相关组织对美国能源、水务等关键基础设施发动具备物理破坏能力的攻击，表明网络攻击正持续向关键基础设施领域深化；与此同时，俄罗斯电信级DDoS事件、金融内部违规及终端漏洞被利用等事件集中暴露出基础设施与管理体系的系统性脆弱；更值得警惕的是，以 Anthropic Mythos为代表的前沿AI已具备规模化挖掘0day能力，正在重塑攻防力量对比，推动网络安全进入“AI主导攻防博弈”的新阶段。

## [美政府紧急发布警报：能源水务等关基设施遭破坏性网络攻击](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515788&idx=1&sn=81d72b88950c341fe7c4b76824a88c77&scene=21#wechat_redirect)

安全内参4月9日消息，美国多家联邦机构近日联合发布紧急警告，称伊朗相关黑客正在对美国关键基础设施发起大规模网络攻击，目标涵盖能源、水务及政府设施，重点针对工业控制系统中的PLC设备。攻击者通过入侵控制器并篡改操作界面，试图干扰甚至破坏物理系统运行，部分事件已导致业务中断和经济损失。

分析认为，此类行动与伊朗背景组织“CyberAv3ngers”高度相关。该组织自2023年以来频繁针对水务系统发动攻击，曾入侵全球多地工控设备，并具备从“信息破坏”向“实质性破坏”升级的能力。与此同时，其使用的IOControl恶意软件已被用于渗透工业及物联网设备，增强长期潜伏与控制能力。

安全专家指出，伊朗攻击组织正通过攻击工业控制系统实施非对称打击，未来此类针对关键基础设施的破坏性网络行动或将持续增加。

## [银行员工违规访问客户数据超两年，意大利开出超2.5亿元罚单](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515763&idx=1&sn=313b34af1fe1654de2abbcc963179a3d&scene=21#wechat_redirect)

安全内参4月3日消息，意大利数据保护监管机构对该国最大银行之一——联合圣保罗银行（Intesa Sanpaolo）处以3180万欧元（约合人民币2.52亿元）罚款。调查显示，2022年2月至2024年4月期间，一名员工在未获授权情况下，违规访问3573名客户的银行账户信息，持续时间超过两年。

监管指出，该事件暴露出了在数据安全技术防护与内部管理机制方面存在严重缺陷，尤其是未能及时识别异常访问行为，内部控制与异常监测机制存在重大弱点。同时，银行系统允许员工批量查询客户数据，但缺乏有效的权限约束与审计机制。

此外，受影响客户多为高风险群体，包括知名公众人物，但银行未实施更严格的保护措施。在事件处置过程中，还存在客户通知不及时、信息披露不完整等合规问题。

监管机构表示，罚款综合考虑违规持续时间、影响范围及整改情况等因素作出。该事件再次凸显金融机构在内部权限管理与数据访问监控方面的重大风险隐患。

## [俄电信巨头遭大规模DDoS攻击，全国多城互联网服务中断](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515780&idx=2&sn=fb20336df2077d273311bd1982c24e1f&scene=21#wechat_redirect)

安全内参4月8日消息，俄罗斯国有电信巨头 Rostelecom 周一晚间遭遇大规模分布式拒绝服务（DDoS）攻击，导致全国约30个城市互联网服务异常。网上银行、政府平台及娱乐平台一度无法访问，包括 Steam、Gosuslugi、Rutube 等核心服务受影响。

运营方表示攻击已被遏制，服务中断主要源于紧急流量过滤措施。期间，部分用户仅能访问政府“白名单”网站。事件发生后，仍有用户反映部分政务服务未完全恢复。

此次事件叠加此前一周银行与支付系统中断，暴露出俄罗斯“Runet”主权互联网体系在极端流量冲击与管控措施下的脆弱性。当前具体原因尚未明确，可能涉及网络攻击、流量管控策略或金融机构内部系统故障等多重因素。

## [AI攻防拐点显现：Anthropic前沿模型可规模化挖掘0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515780&idx=1&sn=bd0f5e0150a0f2ee41c12e2e737092ff&scene=21#wechat_redirect)

安全内参4月8日消息，Anthropic 发布前沿模型Mythos预览版，并通过“Glasswing”安全计划向少数机构开放，用于防御性网络安全研究。该模型具备强大的智能体编程与推理能力，可自动扫描第一方软件及开源系统漏洞，在测试中已识别出数千个零日漏洞（0day），部分漏洞存在时间长达10至20年，成功挖掘率超过70%，对传统“打补丁”防御模式形成冲击。

目前，包括 Amazon、Apple、Microsoft、Cisco、CrowdStrike、Linux Foundation 等在内的十余家机构已参与测试，另有约40家组织获得预览权限。Anthropic同时组建“核心安全联盟”，以防范模型能力外泄带来的潜在风险。

值得关注的是，Mythos此前曾因数据管理失误被曝光（代号“Capybara”），叠加近期代码泄露事件，凸显前沿AI在提升漏洞发现能力的同时，也带来新的安全治理挑战。业内观点认为，随着AI具备规模化挖掘与利用漏洞的能力，网络安全正加速进入“AI主导攻防”的新阶段。

## [工信部预警：iOS多版本漏洞遭利用，或致设备被控与信息泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515770&idx=2&sn=3177f777e9ed09388a73f2dec02e6329&scene=21#wechat_redirect)

近日，工信部网络安全威胁和漏洞信息共享平台（NVDB）发布风险提示称，近期发现有攻击者利用针对 Apple 终端产品的漏洞实施网络攻击，可能导致用户信息被窃取、设备被远程控制等严重后果。

通报显示，受影响范围包括运行 iOS 13.0 至 17.2.1 的 iPhone、iPad 等设备。攻击者主要通过短信、邮件或恶意网页投毒等方式，诱导用户使用Safari浏览器访问含恶意代码页面，进而利用系统漏洞植入远控木马，获取设备最高权限。

工信部建议用户尽快升级系统补丁，关注官方安全更新公告，避免点击不明链接，提高安全防护意识，及时开展风险排查，降低被攻击风险。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

奇安信集团

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

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