---
title: 警惕！全球超190,000台Android设备感染后门程序，包括国内知名品牌的手机设备
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492482&idx=1&sn=5659f4a8b3130b6eb9ecc4905ec2fb89&chksm=e90dc9a8de7a40be03e68362534d51ef1552c8d39fee60f1da8179773cf4f9a2fa4a4b0021b3&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-24
fetch_date: 2025-10-06T19:41:06.627710
---

# 警惕！全球超190,000台Android设备感染后门程序，包括国内知名品牌的手机设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 警惕！全球超190,000台Android设备感染后门程序，包括国内知名品牌的手机设备

BaizeSec

白泽安全实验室

近期，全球网络安全领域遭遇了一起大规模的恶意软件攻击事件，名为BadBox的恶意软件感染了超过190,000台Android设备。此次事件涉及的设备包括Yandex智能电视和Hisense智能手机，主要分布在俄罗斯、中国、印度、白俄罗斯、巴西和乌克兰。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN0kbwjqhJEUjJ3nuF18pZzLO7G0ThAWjsqVcxgU0nJicyzws54vLF3XiaRtKJia8ypp3PKqAPQBRtbA/640?wx_fmt=png&from=appmsg)

**1.BadBox恶意软件**

BadBox恶意软件是一种安卓平台上的恶意僵尸网络，源自Triada恶意软件家族，近年来在全球范围内迅速扩散，感染了超过19.2万台设备，包括知名品牌如Yandex电视和海信智能手机等，尤其是Yandex 4K QLED智能电视和T963海信智能手机。BadBox的首次出现可以追溯到2023年初，当时它被发现隐藏在亚马逊销售的T95 Android电视盒中。此后，恶意软件通过多种方式悄然入侵用户设备，主要包括供应链攻击、内部人员的恶意操作以及在产品分销阶段的恶意代码注入。

一旦设备感染BadBox恶意软件，它们会被转变为住宅IP代理（residential proxy），进而被用于广告欺诈或出租给网络犯罪分子，以实施各种非法活动。这种行为不仅威胁到用户的隐私和安全，也对整个网络安全环境构成了严重的威胁。BadBox的恶意功能包括窃取用户的身份验证信息、安装其他恶意软件，并通过模拟虚假流量进行广告欺诈，帮助网络犯罪分子获取经济利益。

德国联邦信息安全办公室（BSI）已采取措施，成功切断了约3万台设备与BadBox僵尸网络的连接，但尽管如此，感染规模仍在持续扩大。根据最新的研究，BadBox的命令与控制服务器每天有超过16万个独立IP地址试图连接，显示出其强大的传播性和隐蔽性。这一事件不仅引发了公众对智能设备安全的关注，也促使用户在购买设备时更加重视安全性能，以降低被感染的风险。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN0kbwjqhJEUjJ3nuF18pZzVwGmVBhyZTPgEYxMOxnhsSibk494CBXf60Emhdr2JjUdQCTtTfIib9UQ/640?wx_fmt=png&from=appmsg)

**2.攻击流量及攻击技术详细分析**

BadBox恶意软件的核心与Triada恶意软件家族相似，似乎是Triada的变种，具有在用户不知情的情况下下载和执行额外代码或模块的能力。其攻击原理和过程涉及多个技术层面和供应链环节，以下是详细的攻击流程和技术分析：

**（1）攻击流程如下**

* 受感染的设备在启动时会尝试连接到恶意基础设施，以加载后门。
* 后门能够下载次级有效载荷，允许进一步远程模块安装而无需用户许可。
* BadBox利用受感染的设备进行住宅IP代理、远程代码安装、账户滥用和广告欺诈等活动。

**（2）攻击过程技术详细介绍**

* 供应链入侵：

BadBox恶意软件主要通过供应链攻击进入设备。黑客组织利用供应链环节的薄弱之处，将恶意软件预装到低成本、非品牌的Android设备中。这些设备大多运行过时的Android版本，存在严重的安全漏洞，使得攻击者能够更容易植入恶意软件。

* 固件级别的感染：

攻击者在固件级别嵌入恶意软件，使得设备在到达消费者手中之前就已经被感染。这种预装的恶意软件使得设备在启动时立即连接到命令和控制（C2）服务器，授予攻击者访问本地网络的权限。

* 广告欺诈与住宅IP代理：

受感染的设备被转换为住宅IP代理（residential proxy），用于广告欺诈或出租给网络犯罪分子进行攻击等非法活动。BadBox恶意软件利用设备固件进行恶意活动，包括住宅IP代理、远程代码安装和广告欺诈等。

* 拦截双因素身份验证详细信息：

BadBox恶意软件可以拦截双因素身份验证详细信息并安装更多恶意软件，这使得攻击者能够进一步扩大攻击范围并窃取敏感信息。

* 远程控制与数据窃取：

当受感染的设备首次连接到互联网时，恶意软件将尝试联系威胁者运行的远程命令和控制服务器。该远程服务器将告诉BadBox恶意软件应在设备上运行哪些恶意服务，并且还将接收从网络窃取的数据。

* 加密与隐蔽性：

BadBox使用不同的自定义加密方案，这增加了对其行为分析的难度。返回结果中包含下载地址、md5、版本号等内容，显示了其后台刷广告牟利的功能。

* 广告欺诈网络PEACHPIT：

BadBox攻击活动背后还隐藏着一个名为PEACHPIT的广告欺诈僵尸网络。该僵尸网络利用受感染设备模拟虚假流量，伪造流行App的广告点击量，并通过程序化广告平台出售这些虚假impressions，从而实现“吸金”目的。

* 沦为“肉鸡”：

受BadBox感染的设备还可能被用作住宅IP代理服务器，为其他黑客提供网络攻击的跳板，或用于创建Gmail、WhatsApp等在线账户，实施网络犯罪。

**3.事件总结**

本次BadBox事件清晰地揭示了BadBox恶意软件的复杂攻击链，这一攻击链是多阶段和多手段的，覆盖了从供应链的初始入侵到最终的恶意行为执行。这不仅对全球网络安全构成了严重威胁，还暴露了智能设备在安全防护方面的脆弱性。网络犯罪分子通过全球供应链传播恶意软件，这一点在BadBox事件中得到了明显的体现。无论是低成本的电子产品还是如Yandex和海信这样的高端品牌设备，影响范围都极为广泛，显示出不同类别设备中存在的安全漏洞。这一事件也强调了网络安全问题的紧迫性，同时，它也提醒用户在购买智能设备时，必须更加关注产品安全性能，包括软件更新的频率、生产商的责任以及软件版本的合规性等因素，这些都是减少设备被恶意软件感染风险的关键点。

参考链接：

https://www.bitsight.com/blog/badbox-botnet-back

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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