---
title: 能信安：病毒和恶意代码通告
url: https://mp.weixin.qq.com/s/GzYUorxIDf4xvnA2Zn3avw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:58.411724
---

# 能信安：病毒和恶意代码通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7EgONBwTicyrGUWzI33RD8e12Jbn7lrUQBa50SDdm4m2e8Le2Fb8v3EVwqxvMjsmKKCzsNndKR913M0Gg8ViaeA/0?wx_fmt=jpeg)

# 能信安：病毒和恶意代码通告

能信安资讯

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7EgONBwTiczUQfWJ4WrTVuo8W1k70LL2J82G8pcFOM0JvqBtb3Vna0emxlIltNWczVzVH0ibWw3TtwKLYXado2A/640?wx_fmt=jpeg&from=appmsg)

网络安全预警通报

  漏洞通告 2025年1月9日

**0****1**

**“DroidLock”勒索软件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTiczUQfWJ4WrTVuo8W1k70LL2cKsm89W6oKTSjcTcI3rzlhUb07eCa9Iujlkp9toricmrouNKgLF1hHw/640?wx_fmt=png&from=appmsg)

**描述：**

该恶意软件由移动安全公司Zimperium 最先发现，目前主要针对西班牙语用户，通过恶意网站分发。攻击者利用伪装成合法应用的“Dropper”（释放器）欺骗用户下载，随后弹窗提示“系统更新”，诱导用户安装包含真正恶意代码的 Payload（有效载荷）。这一多阶段感染策略，让其极易绕过普通用户的警惕防线。

DroidLock 被安装后会立即索取“设备管理器”和“无障碍服务”两项高危权限。获得授权后，该软件能执行多达 15 种恶意指令，包括静音设备、启动摄像头、卸载应用及窃取短信和通话记录。IT之家附上该恶意软件能实现的恶意指令如下：

DroidLock 支持的命令

更为致命的是，它利用VNC（虚拟网络控制台）系统建立远程连接，允许攻击者在设备闲置时完全接管手机。此外，它还能生成一个透明的弹窗，当用户在屏幕上绘制解锁图案后，直接窃取该图案并发送给攻击者。与传统勒索软件不同，DroidLock 并不加密用户文件，而是采用“锁屏勒索”策略。它通过 WebView 加载一个全屏覆盖层，阻断用户对手机的任何操作，并修改设备的 PIN 码或生物识别数据，彻底锁死手机。作为 Google 应用防御联盟（App Defense Alliance）的成员，Zimperium 已将 DroidLock 的特征码同步给 Android 安全团队，目前开启了 Google Play Protect 的设备已能自动检测并拦截此威胁。

安全专家建议，用户应坚决避免从非Google Play 商店“侧载（Side-load）”应用，同时需警惕任何请求“无障碍服务”权限的非必要应用，定期扫描设备以确保安全。

攻击者在勒索界面留下Proton 邮箱地址，威胁受害者若不在 24 小时内支付赎金，将永久删除设备内的所有文件，这种手段利用用户的恐慌心理，达到了与加密勒索相同的敲诈目的。

**安全建议：**

1.安装防病毒软件并及时更新漏洞库，定期实施全盘查杀。

2.避免打开来历不明的邮件、链接和网址附件等，尽量不要在非官方渠道下载非正版的应用软件，发现文件类型与图标不相符时应先使用安全软件对文件进行查杀；

3.定期检测系统漏洞并且及时进行补丁修复。

4.使用强密码，并定期更改密码，以防御黑客进行的暴破攻击。

3.定期检测系统漏洞并且及时进行补丁修复。

4.使用强密码，并定期更改密码，以防御黑客进行的暴破攻击。

**0****2**

**“Glassworm”恶意软件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTiczUQfWJ4WrTVuo8W1k70LL2cKsm89W6oKTSjcTcI3rzlhUb07eCa9Iujlkp9toricmrouNKgLF1hHw/640?wx_fmt=png&from=appmsg)

**描述：**

科技媒体bleepingcomputer 昨日（12 月 1 日）发布博文，Glassworm 恶意软件针对 VS Code 插件生态发起第三波攻击，在 Microsoft Visual Studio Marketplace 和 OpenVSX 两大平台上投放了 24 个新增恶意扩展包。

IT之家曾于 10 月初报道，攻击者利用“隐形 Unicode 字符”逃避代码审查，伪装成 Flutter、Vim 等热门开发工具，并通过人为刷高下载量混淆视听。

在攻击机制上，Glassworm 展现出极高的危险性。一旦开发者误装这些扩展，恶意软件便会立即运行，窃取受害者的 GitHub、npm 和 OpenVSX 账户凭证，并扫描盗取加密货币钱包数据。

更为严重的是，攻击者会在受害者机器上部署SOCKS 代理实现路由恶意流量，并安装 HVNC（隐藏虚拟网络计算）客户端。这让攻击者能够绕过常规监控，隐蔽地远程访问受害者计算机，从而进行更深层次的渗透或破坏。Glassworm恶意软件爆发第三波攻击：24个“李鬼”扩展包投毒

IT之家 12 月 2 日消息，科技媒体 bleepingcomputer 昨日（12 月 1 日）发布博文，Glassworm 恶意软件针对 VS Code 插件生态发起第三波攻击，在 Microsoft Visual Studio Marketplace 和 OpenVSX 两大平台上投放了 24 个新增恶意扩展包。

IT之家曾于 10 月初报道，攻击者利用“隐形 Unicode 字符”逃避代码审查，伪装成 Flutter、Vim 等热门开发工具，并通过人为刷高下载量混淆视听。

在攻击机制上，Glassworm 展现出极高的危险性。一旦开发者误装这些扩展，恶意软件便会立即运行，窃取受害者的 GitHub、npm 和 OpenVSX 账户凭证，并扫描盗取加密货币钱包数据。

更为严重的是，攻击者会在受害者机器上部署 SOCKS 代理实现路由恶意流量，并安装 HVNC（隐藏虚拟网络计算）客户端。这让攻击者能够绕过常规监控，隐蔽地远程访问受害者计算机，从而进行更深层次的渗透或破坏。

为了躲避安全审查与用户警觉，Glassworm 采用了多重伪装战术。在技术层面，它继续使用“隐形 Unicode 字符”将恶意代码隐藏在看似正常的源码中，同时在第三波攻击中引入了 Rust 语言编写的植入程序，进一步增加了分析难度。

在运营层面，攻击者通常在扩展包上架并通过审核后，才推送包含恶意代码的更新。随后，他们会人为刷高下载量，让恶意扩展在搜索结果中排位靠前，甚至紧邻其模仿的正规项目，极具欺骗性。

第三波攻击由安全机构 Secure Annex 的研究员 John Tuckner 发现，他分析指出攻击者的目标范围非常广泛，涵盖了 Flutter、Vim、Yaml、Tailwind、Svelte、React Native 和 Vue 等主流开发框架与工具。

被曝光的恶意包名称极具迷惑性，如icon-theme-materiall（模仿材质图标主题）、prettier-vsc（模仿代码格式化工具）等，这种“李鬼”式的命名策略，利用了开发者在搜索安装时的惯性，极易导致误下载。

**安全建议：**

1.安装防病毒软件并及时更新漏洞库，定期实施全盘查杀。

2.避免打开来历不明的邮件、链接和网址附件等，尽量不要在非官方渠道下载非正版的应用软件，发现文件类型与图标不相符时应先使用安全软件对文件进行查杀；

3.定期检测系统漏洞并且及时进行补丁修复。

4.使用强密码，并定期更改密码，以防御黑客进行的暴破攻击。

▼

**能信安——新一代网络安全领先企业！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7EgONBwTicyukySMu6FXUXWDAkWwribspgqezQeNT68WySw9CozfOicqxGnISiaB0GFYXp3qXHmpmHzays0SBTSibQ/640?wx_fmt=jpeg "bde0f1f294be1789aa279651ce5123d5.jpg")

**公司简介**

深圳市能信安科技股份有限公司，是以安全、移动、泛在和大数据为主要方向的专业技术公司，致力于移动互联安全、车联网安全、物联网安全、大数据安全和人工智能安全技术。

公司是公安部、工信部网络安全技术支撑单位，国家网络安全威胁和漏洞信息共享平台技术支撑单位，是深圳大运会、党的十八大、2020年全国两会、2021年联合国生物多样性大会网络安全技术支撑单位。公司是国家级专精特新“小巨人”企业，中国移动安全十强企业，全国网络安全百强企业，具有良好的品牌影响力。

公司为中国新一代网络安全领先企业。在移动安全领域，公司可提供业界最先进、完整的技术、产品与解决方案，引领移动互联安全的技术潮流。主要产品及服务包括移动应用安全防火墙、无线安全检测及防御系统、移动应用安全检测及加固技术等。在数据安全领域，提供业界领先的数据安全治理、数据安全合格产品与服务。

公司依托于多年网络安全领域的技术经验及专业资质，向各类政府机关及企事业单位提供等级（分级）保护顾问咨询、关基保护顾问咨询、数据安全治理、密码改造顾问咨询、信息系统风险评估、安全体系建设咨询、修复加固服务、渗透测试服务、应急响应服务、安全运维保障服务。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTicwJbtXPMDMSMHxOK5ibqcf4XC5icFVAVsNF8fiaHuTFeRINsEs3tESvq6aNNTywQlVga3LibzRqNXoPiaA/0?wx_fmt=png)

能信安资讯

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTicwJbtXPMDMSMHxOK5ibqcf4XC5icFVAVsNF8fiaHuTFeRINsEs3tESvq6aNNTywQlVga3LibzRqNXoPiaA/0?wx_fmt=png)

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