---
title: 当广告流量分发与效果跟踪系统被用于网络攻击后
url: https://mp.weixin.qq.com/s/jb7IJUPJcbZoCzPzSAvlKw
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:19.467023
---

# 当广告流量分发与效果跟踪系统被用于网络攻击后

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqFl1emnn7JLNfKZ5IUqKicugRx5QICwkT0xysiaFSs1J8gj4YaclQ9xrVujyBiaGMicickNUd0cmth4WRaPRH8WqpqDddMShEs41Vg/0?wx_fmt=jpeg)

# 当广告流量分发与效果跟踪系统被用于网络攻击后

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

Keitaro 是一款自托管的广告流量分发与效果跟踪系统，原生具备的精细化流量路由、受众定向、内容伪装能力，被威胁攻击者改造为网络犯罪的核心基础设施。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoWQ9ZD6WxRAp9Uia5SdKy9mYLOpoQXNTcIibp1WqscVBLfCbNOxV9opiboEVEicVkzOXlqg3V0ttZnfJcXpYW6LeZojpCr2gxUWicM/640?wx_fmt=jpeg)

研究周期内，研究团队监测到约 13500 个与 Keitaro 恶意活动相关的域名、22.6 万次相关 DNS 查询，分析了 2.75 亿次广告曝光数据，识别出 120 余起利用 Keitaro 的垃圾邮件攻击活动，覆盖投资诈骗、加密货币盗窃、恶意软件分发、恶意广告等全品类网络犯罪。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp3JWTTdlicQzBia3qkvZmFmCnMGo0qnDIaO5ib1AAl2k2ACs3Xw9dNHodldjGLO0ibdNFBq7CFYtRyZ09icHFUSxDKpDW8xNBVnibus/640?wx_fmt=png&from=appmsg)

研究发现，AI 技术已成为 Keitaro 相关攻击的核心力量倍增器，超半数主流投资诈骗活动都以 AI 驱动交易、深度伪造内容为核心诱饵。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrhgkRANV3XLQVTCWVGxLY56R71B7f4WSG5lIIkjKIiaFliclsU2QPTREJpRqrwucKKZH8jgf25mqPMPxPcoD8avO93J4kYurCbo/640?wx_fmt=png&from=appmsg)

同时，Keitaro 破解版在地下论坛的广泛传播，大幅降低了网络犯罪的准入门槛，超 20% 被 Confiant 持续跟踪的恶意广告攻击者都在使用该平台。

在治理层面，Keitaro 开发方 Apliteni 对滥用举报表现出积极响应，已建立标准化举报渠道并处置了大量违规账户，但破解版泛滥、攻击者的域名快速轮换、非对称攻防优势等问题，仍给威胁治理带来持续挑战。报告最终也针对防守方、平台方、行业生态提出了分层防御与协同治理的相关方向。

要理解 Keitaro 在网络犯罪生态里的角色，首先要回到这款工具本身的设计初衷和行业背景。

流量分发系统与内容伪装技术，是当前网络犯罪规避检测、精准触达受害者的核心手段。

相较于纯黑产工具，商业级跟踪平台 Keitaro 凭借流量分发、跟踪、伪装一体化的功能特性、低使用门槛、高可扩展性，成为黑灰产从业者的首选工具之一，甚至被 TA2726 等知名恶意软件组织纳入核心攻击链路。

尽管行业内已多次观测到 Keitaro 的恶意滥用行为，但此前缺乏长周期、多维度的系统性研究。本次系列研究通过广告技术层与 DNS 层的双视角互补分析，完整还原了 Keitaro 滥用的全生态图景。

本次研究的核心数据来自 Infoblox 与 Confiant 的能力互补，Infoblox 侧提供了全球客户被动 DNS 遥测、电子邮件日志、HTTP 会话数据和 Web 服务器指纹数据，完整覆盖 DNS 层的全链路威胁观测；Confiant 侧则依托实时广告交易的客户端与服务端数据，以及数千家网站和移动应用的广告曝光验证数据，累计覆盖 2.75 亿次广告曝光，为广告生态的恶意活动提供了全链路视角。

Keitaro 的原生设计目标是为合法广告营销提供流量管理能力，但其核心功能可被攻击者无门槛改造为恶意用途，同时平台的版本迭代与破解版传播，进一步放大了滥用风险。

Keitaro 的核心路由架构以 Campaign、Flow、Filter、Schema 为核心，为攻击者提供了高度灵活的流量控制能力。

每个 Campaign 为独立的路由单元，支持绑定多个域名、生成唯一访问链接，甚至可直接设置为域名根页面，实现单实例多恶意活动的并行管理。Flow 流量流支持强制流、常规流、默认流三级优先级，可按 IP 地理位置、设备指纹、操作系统、浏览器、访问来源等维度设置访问过滤规则，实现目标受害者跳转恶意页面、非目标流量跳转合规诱饵页面的核心伪装逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrcmNFH2iaXHDk6LOS8QlCCD0ZNtm7BDjp8axicse38eDNNK2R1MT5Dd74Xm2BvZw1L2SGVmzu9eicxHIIsl295UL59eEib9vicYM1I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDobCIicIgc7MoJAh1mV10CLlpsWWXBBMxd0nWtIABUogr1W5WIoFZUia2qyibZ6icyMxQzfSicBw5gyVzS7icpjLNGM06I3btyIic10fg/640?wx_fmt=png&from=appmsg)

Schema 动作方案可定义流量匹配后的执行动作，包括多落地页流量分流、直接重定向、嵌套其他路由逻辑等，支持攻击者最大化单流量的变现效率，实现单链路承载多类恶意活动。

典型的应用场景里，针对bc活动的滥用中，攻击者通过 Flow 规则，将德国安卓用户、美国和瑞士 Windows 用户定向至非法bc页面，其余流量则跳转至仿冒手游公司的诱饵页面或 YouTube 等合规站点，完美规避内容审核与安全检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqVGb3DibGOMPZbKjzdkJYY5ALffHkkYfyoGVFAoZ6lFBrh6OllUZEvSgUfp2Q6qAcH73MFwXQibXeRsZZX0o2sKSBqhgsiaK3iaWo/640?wx_fmt=png&from=appmsg)

内容伪装是 Keitaro 被恶意滥用的核心功能，即使平台在新版本中移除了第三方伪装工具的官方集成，攻击者仍可通过多种方式实现伪装能力。平台原生提供反机器人 IP 封禁功能，攻击者可补充 GitHub、地下论坛共享的平台爬虫 IP 库，实现对安全检测流量的精准屏蔽。

平台也支持通过自定义 PHP 过滤器实现与 HideClick、Adspect、IMKLO 等主流伪装工具的深度集成，其中 Adspect 可提供 AI 驱动的流量过滤能力，绕过 Google、Meta、TikTok 等主流平台的检测。除此之外，通过 KClient JS 脚本，攻击者可在不触发页面重定向的前提下，直接替换页面 DOM 内容，受害者始终停留在原域名，大幅降低被重定向检测工具识别的风险。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqwf61NqY34RFjexFQibP6z4Hkr9GE4DA8YzFibL1b9RYZMFjbfCAgZsN7a2icdcTibU0R9OBQnaeCZyJWjD0rzGD8JoB0AEE6dKLY/640?wx_fmt=png&from=appmsg)

该能力可被广泛利用于已被攻陷的 WordPress 站点，实现恶意内容的静默投放。

破解版 Keitaro 是黑产生态滥用的核心载体，也是平台治理的核心难点。7.x 到 9.x 版本的破解版在俄语地下论坛广泛传播，版本内置预激活功能，可绕过官方许可证验证，无成本使用全部核心功能。

研究确认，TA2726、TA576 等知名恶意软件组织，均通过破解版或被盗许可证使用 Keitaro，官方无法直接对这些实例进行管控。

旧版本还存在 Cookie 命名碰撞问题，v11 之前的版本使用 5 位字母数字 Cookie 作为实例标识，该标识并非全局唯一，存在随机碰撞与破解许可证复用导致的碰撞，曾出现恶意软件活动、加密诈骗、广告联盟滥用共用同一 Cookie 标识的情况，给威胁归因带来干扰。

在所有 Keitaro 的恶意滥用场景中，投资诈骗是出现频次最高、覆盖范围最广的威胁类型，而生成式 AI 和深度伪造技术的融入，正在让这类诈骗的杀伤力和隐蔽性持续升级。

攻击者会批量生成同质化的投资网站，以 AI 驱动算法交易、区块链自动化理财为核心噱头，承诺无风险、超高额收益，通过 Web 表单收集受害者联系方式，后续由假冒的客户经理诱导受害者投入资金。

此类攻击覆盖英语、德语、日语、西班牙语等多语言受众，通过注册域名生成算法批量注册域名，实现基础设施的快速轮换。也有攻击组织通过 AI 深度伪造技术生成新闻主播、公众人物的虚假视频，仿冒正规媒体的新闻页面，编造虚假投资政策、名人理财故事，诱导受害者进入虚假加密货币投资平台，其中部分组织专门针对美国老年人与低收入群体，以债务减免、社会福利为诱饵，实现精准诈骗。

还有攻击者注册与各大银行、物流、零售品牌高度相似的仿冒域名，搭建虚假登录页、包裹跟踪页、退款通知页，窃取受害者的账户凭证、银行卡信息与身份数据，此类攻击采用低频次、小批量的域名注册模式，规避安全检测系统的识别。

加密货币盗窃是 Keitaro 垃圾邮件攻击的绝对主流，研究显示，96% 的 Keitaro 相关垃圾邮件流量，都指向加密货币钱包窃取攻击。

攻击者以虚假代币空投、NFT 赠送活动为诱饵，仿冒主流加密项目与钱包平台，诱导受害者连接钱包并授权恶意交易，直接清空钱包资产。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrsLdGsr0Bg39ODoQBMzKiapTrJj1BKeibhnscict7VeSj7ludM18pIFh7fsNHEZuJdlACzoUA9P2x8dgpnN0uuOdbxSibu53wxqs4/640?wx_fmt=png&from=appmsg)

此类攻击的基础设施与话术体系高度集中于俄语区网络犯罪生态，同时衍生出仿冒主流加密交易所、虚假区块链工具的诈骗页面，进一步扩大攻击面。

Keitaro 也是当前恶意广告生态的核心基础设施之一，监测数据显示，研究周期内近 30% 的活跃恶意广告组织，都通过 Keitaro 实现流量伪装与分发。

其中技术支持诈骗的典型模式里，攻击者通过 AI 批量生成覆盖海量关键词的诱饵页面，在搜索引擎与广告平台投放，仿冒系统官方警报，编造虚假病毒感染提示，诱导受害者拨打假冒客服电话，进而实现远程控制与资金敲诈，此类攻击主要针对美国本土用户，通过流量过滤规则，屏蔽非美国 IP 与审核流量。

也有组织通过仿冒主流消费品牌的赠品活动，搭建游戏化的落地页，诱导受害者填写身份证、银行卡、地址等敏感信息，还有专门针对巴西用户的攻击，以短视频广告为诱饵，窃取受害者的税号、支付密钥、驾照号等核心身份数据。

除此之外，攻击者还会利用 Keitaro 的地理位置过滤能力，定向分发非法bc内容，同时通过 DNS 失效委托漏洞劫持闲置域名，分发成人内容与约会诈骗页面。

Keitaro 已成为恶意软件分发链路的核心流量网关，最具代表性的是威胁组织 TA2726。该组织作为知名流量中间商，长期利用 Keitaro 搭建流量分发基础设施，分发各类远控木马与加载器。

攻击者通过精细化的流量过滤规则，仅向符合目标环境的受害者分发恶意载荷，其余流量全部跳转至合规诱饵页面，大幅提升了攻击的隐蔽性与溯源难度。除此之外，还有大量攻击者通过垃圾邮件携带 Keitaro 链接，分发各类恶意软件，实现信息窃取与设备控制。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpG6Tsvs5OvOJSWS80F7ouqmpWkejfgu6VrssOpcKiaPc30Q2XjBHkusrBuCHfpAGicTicHvD7osibyTnObovtXmcB44s6RRdGquQA/640?wx_fmt=png&from=appmsg)

除上述核心威胁外，Keitaro 还被广泛滥用于求职诈骗、流媒体订阅钓鱼、电商平台续费诈骗、针对俄语用户的虚假政府社会分红骗局、免费贷款诈骗，以及虚假保健品电商诈骗等全品类黑灰产活动。

从监测到的全量数据来看，Keitaro 的滥用行为呈现出清晰的趋势与固定的行为模式。在基础设施运营层面，攻击者的域名注册行为与注册商促销高度绑定，会集中在域名注册商的促销窗口期批量注册域名，研究周期内，超 8000 个恶意域名注册集中在五大主流注册商，两次大规模的恶意域名注册爆发，都恰好对应注册商的大型促销活动。攻击者普遍采用低价顶级域，配合域名生成算法批量生成域名，实现单日上百个域名的快速轮换，形成封禁一个、新增五个的非对称攻防优势，让单纯的域名封禁失去长期效果。同时，超半数恶意实例通过 CDN 隐藏真实源站，同时大量使用抗投诉主机服务商，阻碍安全团队的溯源与封禁操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDohSR1iajK4B4pjoXCJnjjGzawIMczic0EUo2piaYkkLKVLx9ricbNRbicrawDjtSkQC3wyjebIbtFqh02W4nFoem5ploiaDAV91NOG8/640?wx_fmt=png&from=appmsg)

在攻击技术与产业化演进层面，AI 已成为攻击规模化的核心驱动力，攻击者已实现从 AI 生成诱饵内容到 AI 作为诈骗核心噱头的全链路应用，通过生成式 AI 批量生产多语言文案、图片、落地页，通过深度伪造技术提升诈骗可信度，大幅降低了攻击的边际成本，同时提升了转化率。Keitaro 整合了流量分发、跟踪、伪装三大核心能力，替代了原本需要单独付费的多款黑产工具，配合破解版的零成本传播，让无深厚技术能力的攻击者也可快速搭建规模化的恶意攻击链路，网络犯罪的准入门槛持续降低。同时，攻击者普遍采用多维度流量过滤规则，仅向高价值目标展示恶意内容，非目标流量全部跳转至合规页面，让传统的基于 URL 的安全检测工具大量失效，同时实现了攻击资源的最大化利用，攻击的定向精准化与隐蔽性持续提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr9CamNsNm2R06f710YFbVX70DWj4qkNSKxulUjh61pAqMwGT5uDQIiaicBSbToEpQPaubOxB3OQ3I57VDSnlsJCzYWM0WYvibicO8/640?wx_fmt=png&from=appmsg)

研究团队与 Keitaro 开发方 Apliteni 进行了长达 6 个月的持续沟通与协同，验证了厂商在滥用治理上的积极动作与实际成效。

2025 年 9 月，Keitaro 更新了信任与安全准则，将原本仅支持即时通讯工具的举报渠道，升级为标准化的邮件举报系统，建立了规范化的滥用处置流程。研究周期内，团队累计向厂商上报了上百个恶意实例域名，Keitaro 累计取消了十几个违规账户，且被处置的攻击者中，仅 1 个在监测期内重新使用平台，处置具备长期威慑效果。在产品层面，平台也在新版本中移除了第三方伪装工具的官方集成，同时持续打击破解版的传播与使用，通过许可证绑定 IP 的机制，限制被盗许可证的滥用。

但当前的治理工作仍面临着难以突破的核心挑战。绝大多数恶意软件分发、大规模诈骗活动，都使用旧版本破解版 Keitaro，此类实例不接入官方许可证系统，厂商无法直接进行管控与处置。

同时，滥用举报与域名封禁本质上是对防守方的资源耗尽攻击，攻击者可低成本批量注册域名，而安全厂商与平台方需要投入大量资源完成证据收集、验证、处置全流程，难以覆盖全部恶意实例。再加上 Keitaro 的流量伪装与条件跳转特性，导致平台方难以复现、验证恶意行为，给快速处置带来了技术门槛。

整体来看，Keitaro 作为一款合法的商业广告跟踪工具，其本身并非恶意产品，但其强大的流量管理、内容伪装、受众定向能力，被网络犯罪生态深度改造与滥用，成为当前各类诈骗、恶意软件分发、恶意广告活动的核心基础设施。生成式 AI 技术的融合，进一步放大了 Keitaro 相关威胁的危害，让攻击实现了规模化、低成本、高可信度的升级。

尽管 Keitaro 开发方已积极响应滥用治理需求，建立了标准化的处置流程，但破解版泛滥、攻击者的非对称攻防优势等核心问题，无法通过单一厂商的努力解决。

原分析报告链接：

https://www.infoblox.com/blog/threat-intelligence/patterns-pirates-and-provider-action-what-we-learned-working-with-keitaro/

https://www.infoblox.com/blog/threat-intelligence/inside-keitaro-abuse-a-persistent-stream-of-ai-driven-investment-scams/

https://www.infoblox.com/blog/threat-intelligence/no-reach-no-risk-the-keitaro-abuse-in-modern-cybercrime-distribution/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0i...