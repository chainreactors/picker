---
title: 一周回顾：从港口到AI工具，关键基础设施接连遭受攻击
url: https://mp.weixin.qq.com/s/kIUuOeok4s2a3iMiUYobhQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:09.099249
---

# 一周回顾：从港口到AI工具，关键基础设施接连遭受攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mSqhDgeKrPDibuPyOLfQdibM30P5WaXsRvb1NbPdt3vPfibscYxN87rxzdKk05yUZkEleYpKTibnXv8cjvNH3tNn1bLPXIHvlqv2AN9ibo22N3t8/0?wx_fmt=jpeg)

# 一周回顾：从港口到AI工具，关键基础设施接连遭受攻击

奇安信集团

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarbeibXRgFiaLhJj1QdgPcxzLh3OFl0EicBlXUMStdia9vxEro6xT4wLKAYU4rUOOX1ibfaUpT6ZRibL4gw/640?wx_fmt=jpeg&from=appmsg)

本周网络安全延续紧张态势：西班牙维戈港遭勒索软件攻击，部分数字系统中断，被迫启用人工流程维持货运；美国酒驾检测系统遭DDoS攻击，导致全国数千车辆无法启动；开源大模型网关LiteLLM和国产开发工具Apifox均遭供应链投毒，大量用户凭据被窃；加拿大外包巨头Telus Digital疑似泄露约1PB敏感数据。

## [欧洲最大渔港遭勒索攻击运营中断，被迫转入人工作业](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515737&idx=2&sn=991c4b4fe68294e72d7dbc302fb2bac1&scene=21#wechat_redirect)

3月26日安全内参消息，西班牙维戈港3月24日遭勒索软件攻击，导致部分港口数字系统中断运行，港口启用人工流程维持运营。作为欧洲最大的渔港之一，此次事件对港口物流调度产生了明显影响。

据港口方面披露，受影响系统主要包括用于管理货物流量及相关数字服务的服务器。部分设备已被攻击者锁定，并提出赎金要求。为防止影响进一步扩大，港口技术团队迅速采取隔离措施，切断受影响系统与外部网络连接。

尽管数字系统受阻，港口实体运营仍在继续，包括船舶调度与货物装卸。但由于原有物流协调高度依赖数字平台，部分业务已转为人工处理，并使用纸质文件进行替代，整体效率受到一定影响。

港口方面已将此次事件定性为以勒索为目的的网络攻击，但尚无组织公开宣称对此负责。近年来，随着港口在全球供应链中的枢纽作用不断增强，已逐渐成为勒索软件攻击的重点目标。

## [知名大模型网关LiteLLM遭供应链投毒，大量用户凭据和认证令牌被窃取](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247518101&idx=1&sn=b2d0d3b55c7cca6f53a1583fbc3cb5e1&scene=21#wechat_redirect)

3月24日，Bleeping Computer报道，知名开源大模型网关项目LiteLLM遭遇供应链投毒。LiteLLM月下载量接近1亿，并被DSPy等主流AI框架广泛依赖，导致此次事件波及范围极广。

受影响的版本为1.82.7和1.82.8，这些版本被植入恶意代码，能够窃取用户系统上的各类凭据和认证令牌。

据悉，此次攻击由威胁组织TeamPCP发起，是其针对全球关键开发生态系统连续多日渗透行动的一部分。此前，TeamPCP已渗透Trivy、Checkmarx、OpenVSX等知名开源项目，最终窃取了LiteLLM PyPi官方仓库账号权限（LiteLLM使用Trivy进行安全扫描），并在约4小时的窗口期内发布了两个高危版本。

此次事件的影响范围已从基础软件开发延伸至AI应用安全等核心领域，开发者和企业立即检查依赖版本并采取安全防护措施。

## [加拿大外包巨头遭攻击，1PB数据疑似泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515717&idx=1&sn=94640f2c622895f4e0194affd6312d6a&scene=21#wechat_redirect)

安全内参3月24日消息，加拿大电信Telus旗下数字服务与BPO部门Telus Digital确认发生安全事件。威胁组织ShinyHunters声称，通过持续数月攻击，窃取了约1PB数据，涉及Telus及其众多客户。

Telus Digital为全球企业提供客户支持、内容审核、AI数据服务等外包运营，BPO业务集中处理多公司数据，使其成为理想攻击目标。ShinyHunters利用此前Salesloft Drift数据泄露中获取的谷歌云平台凭证，访问Telus系统并横向扩展，下载包括客户支持记录、呼叫录音、源代码及财务信息在内的敏感数据。

Telus Digital表示所有业务运营保持正常，并已采取措施加固系统、聘请网络取证专家并配合执法机构调查。公司未与攻击者接触，并将在适当时通知受影响客户。ShinyHunters称自今年2月起对Telus实施勒索，要求支付6500万美元。

此次事件凸显BPO及外包服务提供商的安全风险，影响范围涵盖客户支持、AI工具、财务和通话数据等多个核心业务领域。

## [美国酒驾检测系统遭网络攻击，大规模车辆无法启动](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515709&idx=1&sn=2adbb96b2e4e5875f6f498b1bb022a27&scene=21#wechat_redirect)

安全内参3月20日消息，美国酒精检测设备供应商 Intoxalock 近日遭遇DDoS攻击，导致全国46州酒驾检测系统瘫痪，数千司机无法启动。

Intoxalock主要提供车载酒精检测锁服务，受法院要求使用该设备的酒驾司机必须先通过检测，才能启动车辆。该事件导致整个系统关闭，所有安装该设备的车辆均无法启动。受影响司机表示，有些人只有一辆车，因而完全无法出行。CBS13报道，Intoxalock确认遭遇DDoS攻击，黑客向其服务器发起大量流量，影响安装、拆除、校准及账户访问，但用户数据未受损害。公司未透露是否有赎金要求。

Intoxalock已于3月19日宣布设备全面恢复运行，并提供最长10天的服务延期。公司声明称，将承担系统暂停造成的直接费用，但不包括常规校准费用，并对受影响客户表示歉意，承诺持续提供支持。缅因州州务卿办公室表示，已与公司保持联系，并可通过车辆管理局网站查阅供应商和安装点名单。

## [国产开发工具 Apifox 遭遇供应链投毒攻击](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247518109&idx=1&sn=b9d326d632994618da5d45bf84923834&scene=21#wechat_redirect)

3月26日，国产开发工具 Apifox 被曝遭遇供应链投毒攻击。攻击者通过篡改其官方CDN上的动态JavaScript文件，在大量开发者电脑中植入隐蔽后门程序，进而实现凭证窃取、远程命令执行等恶意操作。

此次攻击主要影响Apifox公网SaaS版桌面客户端（基于Electron框架），Web版及私有化部署版本未受到波及。分析显示，攻击者利用Electron应用未开启沙盒机制及依赖动态加载远程资源的特性，对CDN托管文件进行恶意篡改，从而在用户无感知的情况下完成后门植入，并持续开展近20天的数据窃取活动。

安全业内人士指出，此类攻击本质属于典型的软件供应链攻击，通过污染分发环节实现大规模传播，隐蔽性强、影响面广。近期多起类似事件表明，开发者工具及其生态正成为攻击者重点攻击的高价值入口，一旦失陷，可渗透企业内部系统，放大安全风险”。

目前，建议相关用户尽快停止使用受影响版本，检查本地环境异常行为，并重置关键凭证。同时，企业侧需加强对开发工具的安全评估与访问控制，避免将高权限凭证直接暴露于开发环境中，以降低类似事件带来的连锁风险。

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