---
title: 【重要提醒】东西向流量已成企业数据失窃致命通道！
url: https://mp.weixin.qq.com/s/xxgrEPKUyeP-0RGirHxKPw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:00:27.225474
---

# 【重要提醒】东西向流量已成企业数据失窃致命通道！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0Kn2VsOJzu4NZ1rZ4GlOLWyjLZO5ar3Ay7oV7bRASddQic57mJ6iabFX86mJg3G2TM6ITaOq8N5icCS2v7iahIleBGCS5pbjlPrs7oLUgKuhPiaU/0?wx_fmt=jpeg)

# 【重要提醒】东西向流量已成企业数据失窃致命通道！

原创

深海捕鱼
深海捕鱼

DeepPhish

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

长期以来，国内绝大多数企业做网络安全，都陷入一套固化的防护思维。

把全部预算和防护重心砸在互联网出入口，防火墙、WAF、IPS层层堆叠筑牢外网边界，下意识认定外网才是风险源头，**内网天然可信、无需严加管控。**

但现在的网络攻击往往都是从一个薄弱点撕开一条裂缝，一步步攻陷。近年很多的重大数据泄露事故，起始点甚至只是一条不起眼的钓鱼信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Kn2VsOJzu7cswLib5dyyzkjjMgNvKSB0FnYwISuIGHYVgmLn5KlIrGPopEEFhT6m1h4RPJ0fvialYJlue5K92CW6qxr5uxbibDsdBYJt8jic8w/640?wx_fmt=jpeg&from=appmsg)

**一条钓鱼短信引发的国家级网络攻击**

谁能想到就凭一封短信竟能侵入国家级的安全防护。

2022年3月，美国国家安全局NSA就通过某国外品牌的手机短信的漏洞，秘密监控了10多位国家授时中心的工作人员，在他们毫无察觉的情况下控制了私人手机，非法窃取了通讯录、聊天记录、短信、相册、位置信息等数据，顺利拿到办公主机登录凭证，顺利拿到了进入内网的“钥匙”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0Kn2VsOJzu7ZIw1yBZ49OPeVCQodKJotdwtC0s70b79EzOfVtk2LnLdicyTNdPoq5OfAfvAYlyzePjQc2NBBlGrA7Ihq6sNaQmuxtYHg8VZ8/640?wx_fmt=jpeg&from=appmsg)

后续一年多时间，攻击者摸清了整个单位全部东西向流量传输路径，陆续植入了多次木马，搭建了四层加密传输隧道，而传统边界安全设备却完全无法识别异常外联行为。

**整场攻击最可怕的一环，便是无人管控的内网东西向流量。**

攻击者仅需攻破一台员工终端，就能依托不受管控的东西向流量在内网自由横移，畅通无阻，一路直达核心数据库、高价值业务服务器，窃取关键机密。

无独有偶，据The Hacker News 国际安全媒体《APT28 Targeted European Entities Using Webhook-Based Macro Malware》报道。

被追踪为APT28的组织伪装海关单据发送钓鱼邮件，员工打开带宏附件后，恶意程序24小时内横向移动至货运调度核心服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu4oiau2a9OicuIquJIW8MLtIq7WwN9nHxhaBfrm8icBmxpOfXQL3ToLgjEWj3xgeK5XXfbicjJbhQvlp0HlvLOKTibnMVzh5zeRas28/640?wx_fmt=png&from=appmsg)

长江大学信息中心官方预警通报《网络安全预警通报 - 第 34 期 (2025.11.5)》也通报了一起相似的网络攻击手法。

境外间谍利用邮件渠道发起定向钓鱼攻击，攻陷企业域控服务器，以域控为跳板，依托无管控内网东西向流量扩散，控制了内网50余台核心设备。

梳理以上案例的完整攻击链条不难发现，企业传统的边界防护只拦截进出外网的南北向流量，服务器、终端之间互通的内部东西向流量完全不在管控范围内。

**而攻击者只需利用低成本的钓鱼方式攻破一台终端，就等于在内网打通了一条窃取数据的高速公路。**

**轻视钓鱼防护，会放大所有安全风险**

看完以上真实案例，很多企业管理者可能会疑惑：部署了全套的边界安全设备，为何一封钓鱼信息就能全盘失守？

我们认为核心问题主要有两点，这也是当下大多数企业安全建设的通病。

**1**

**人是所有防护体系中最薄弱的一环。**

利用系统漏洞、软件后门发起的攻击门槛高、成本巨大，而**网络钓鱼依托社会工程学，仅靠短信、邮件、聊天链接就能突破人的防线。**

据Forrester 调研数据显示，每年超八成企业遭遇钓鱼攻击，半数以上造成业务停摆、数据泄露损失。

Forrester 分析师 Allie Mellen 明确提出：**社会工程钓鱼是当前最高效入侵手段，人是整条安全防御链最薄弱环节**；企业即便部署全套边界防火墙、WAF、IPS 硬件防护，只要单一员工点击恶意附件 / 钓鱼链接，外网边界防御会被完全击穿，内网直接暴露在攻击者面前。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu5S9ZibQSFhMWQyEX6BCfibAHh4HU3lwK187mllia2Pw82mn4iau0AzZOmKTOn2JNF5hic5SKpqlfwgkTqKCW6pEveRfKms9ecOUTqI/640?wx_fmt=png&from=appmsg)

**2**

**东西向流量理不清，控不住。**

随着微服务、分布式架构普及，数据中心70%-90%的流量都属于内部东西向流量，流量越大，攻击横向扩散的空间就越大。

而不少运维人员长期存在认知误区，对内网服务器互访、跨业务域调用完全不设限制。内网缺少可视化监测与细粒度权限管控，**黑客攻陷单台终端后，就能顺着东西向流量遍历整个内网，直接拿下存放客户资料、财务数据、核心算法的高价值服务器。**

**分层防护，才能彻底斩断攻击链**

网络安全没有一劳永逸的防护手段，通过对以上案例的攻击链路拆解，我们认为企业需要搭建“事前预防、事中监测、事后处置”的多层闭环防护体系，才能从源头阻断黑客的完整攻击链路。

**1**

**加强员工安全意识培训**

针对运维、财务、系统管理员等高风险岗位开展常态化安全意识培训，定期组织模拟钓鱼演练，推送钓鱼泄密案例科普；对存在点击、下载恶意文件行为的员工开展一对一复盘教育。

同时明确办公设备管理要求，办公终端与私人设备物理隔离，杜绝手机漏洞泄露账号、凭证。

**2**

**精细化管控东西向流量**

落地微隔离完成内网微分段，按业务、资产分区隔离，默认阻断跨域东西向访问，仅放行必要业务通信，遏制攻击横向扩散。

部署 NDR 流量审计平台，采集服务器、虚拟机、容器内网通信，对异常跨库访问、闲置主机异动流量实时告警。

**3**

**完善应急处置机制**

定期组织内网攻防演练，完整模拟“钓鱼入侵终端→内网横向渗透”全流程攻击场景；制定标准化数据泄露应急预案，一旦监测到异常东西向流量，可一键隔离失陷终端、切断跨区域通信链路，快速止损，避免核心数据批量外泄。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Kn2VsOJzu7tljribM38Uleibv7xNqkR9SdaFciaouHnUaZ9XZcKqWkNFULvbbicpYSyWKQuTfAVRkEbDaLOpQibCeDwqia2BWM1L4VwUSAHniacj4/640?wx_fmt=jpeg&from=appmsg)

黑客的攻击手段与时俱进，企业的安全防护意识也要跟上。传统只守外网大门的防护思路早已跟不上时代。

对所有企业而言，网络安全建设必须完成思维转型，防护视线不能只停留在互联网出入口，更要管好内部的“交通要道”。

一方面要持续强化全员反钓鱼安全意识，守住攻击第一道入口；一方面要完成东西向流量的通路管控，搭建起从终端到内网到核心数据的多层纵深防御体系。

双管齐下，才能真正杜绝攻击者靠一条钓鱼信息，就挖空企业核心数据的安全漏洞！

**DeepPhish反钓鱼训练平台**

提供海量逼真的钓鱼邮件模板和定制化场景，可任意模拟发件人地址、钓鱼域名，精准复刻钓鱼邮件，通过沉浸式攻防体验帮助企业将员工从安全“最薄弱环节”转化为“第一道防线”。

以更贴近中小企业实际场景的定制化方案，帮助企业更低成本、更高效率的提升安全意识与防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0Kn2VsOJzu7OOzsWhNDPMpDnQGS0BNicKicYZOfia40xAQKu06ibCtc8Z8yx60MN9vJUax08wd4X2DlBvwHicTjlhib1XmbVVPp8JR3icHe4ia1g9NI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0Kn2VsOJzu4QFkZnRsK6TZxExpibtRWoCNmA0QGcSfB7lTLKmvOxxulFyPD9pfT7e9vPadzjorOWGfK1gBsv5WNLxe7n4M7xFeicXrEqkBW4A/640?wx_fmt=jpeg&from=appmsg)

点赞、爱心、星标支持我们，在钓鱼中招前打一针疫苗！

- 反钓鱼训练平台：deepphish.cn/apt

- EML安全分析平台：deepphish.cn/eml

- 官网选购：deepphish.cn

- 官微：Wh0ami1999，加官微拉粉丝群

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/zsIOptmcnRDqJLJxa8tV10QXefJiaS9ebvvlTZ0FgI58kue6VNtRF1OibkZhAYriawOz70J1KIvEvhlkmDpvepJRw/0?wx_fmt=png)

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