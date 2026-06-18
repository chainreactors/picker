---
title: 揭秘Agent Tesla的隐蔽感染链
url: https://mp.weixin.qq.com/s/RH5wtaXorP8XN_P-i1zAjg
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:00.451011
---

# 揭秘Agent Tesla的隐蔽感染链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0XsXqJttQhuIEybqiaRgVfl3z6PVasj72PBQLYhJvGKnbMU874khpXLTCPgKmpicKAJbUuuy7lSIcbu16UEVpic9rCMrO53UMDG4/0?wx_fmt=jpeg)

# 揭秘Agent Tesla的隐蔽感染链

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3VL38wK6kBP3S451ALR8p3Ows9CxfeB6CicMJfm9JiakaagHRRge3rysbtAGyHlAXGibguiaIaR84tzhU7nobmCZmRH42Uico91ibfI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX28nGM2TicfEdKpgl8Q5X0bjBcOWbia7zFapA9zOuQO9lDtS3H5YrLib2ib90C4OLAslyA0b3rtEicuCwslUMXHSWIMpibnuPGzpaxzQ/640?wx_fmt=jpeg&from=appmsg)

看似普通的付款回执附件，有时可能引发严重后果。近期观测到的一起攻击中，表面寻常的网络钓鱼邮件悄然触发了完整的恶意软件入侵，展示了Agent Tesla的高级感染链。这套精密攻击从用户点击到系统完全沦陷一气呵成，受害者全程难以察觉异常。

Part01

攻击手段升级

从文档漏洞到脚本加载器

不同于以往主要利用未修补文档软件漏洞(如CVE-2017-11882、CVE-2017-0199和CVE-2018-0802等微软Office漏洞)的攻击方式，现代攻击者转而采用极具迷惑性的脚本加载器。虽然旧漏洞仅需诱骗用户打开特制文档即可触发远程代码执行，但如今这些漏洞大多已被修复。为此，威胁分子调整策略，转而使用高度混淆的脚本实现初始入侵，通过受害者机器已有的原生管理工具绕过现代安全防护。

Part02

分阶段感染流程

根据详细记录Agent Tesla多阶段感染链(从钓鱼邮件到进程注入)的完整报告，该恶意软件运营商已掌握静默执行的完美技巧。Point Wild报告明确指出："看似普通的附件背后，隐藏着精心设计的攻击链，包括隐蔽脚本执行、基于PowerShell的有效载荷投递、内存加载恶意软件、进程注入以及旨在长期潜伏的数据窃取技术。"

初始诱饵是精心构造的钓鱼邮件，能够规避基础垃圾邮件过滤器。当受害者解压并打开附件时，高度混淆的批处理脚本随即激活。该脚本专门设计用于禁用本地安全警告，随后静默启动PowerShell。通过直接在内存中运行，恶意软件避免了在硬盘留下可识别痕迹——这正是传统基于磁盘的杀毒软件常见检测点。研究人员解释称："简言之，受害者打开看似无害的文件时，背后高度混淆的批处理脚本已悄然启动PowerShell，进而直接在内存中拉取并执行额外恶意代码。"这种无文件技术极大缩短了防御者的检测响应时间。

Part03

进程注入与规避技术

攻击随后升级为分阶段执行链。PowerShell脚本负责解码shellcode，并在受感染机器上建立持久据点。进程注入是该行动的关键阶段——通过强制charmap.exe等可信应用程序运行恶意代码，攻击者可绕过应用程序白名单和防火墙规则(这些防护本会阻止未知程序联网)。这种被称为"进程镂空"的技术会创建处于挂起状态的合法进程实例，卸载其原始代码后注入恶意载荷再恢复进程线程，使得Agent Tesla感染链极难被标准安全软件察觉。

Part04

强大的反分析能力

该现代恶意软件的另一特点是内置强大的反分析能力。嵌入的VB.NET有效载荷配备了多种防御规避技术，专门干扰逆向工程。分析人员发现其包含特定反调试功能，用于检测是否在受控调试环境中执行。此外，有效载荷会主动执行反沙箱DLL检查，并枚举系统硬件识别虚拟机(反VM检测)。若代码发现自动化恶意软件分析系统的常见特征(如特定虚拟机驱动或沙箱配置)，将立即终止执行以防安全人员分析其行为。这些反调试、反沙箱和反VM检测的组合，使其远超普通凭据窃取程序。

Part05

隐蔽数据外传

Agent Tesla的外传模块高度可配置且功能全面。确认运行在真实受害者机器后，该恶意软件便在后台静默运作，大肆窃取浏览器凭据、会话cookie、自动填充数据等敏感信息。其内置持久键盘记录功能可捕获所有击键，确保连新输入密码也不遗漏。该软件还频繁截取活动桌面屏幕，为攻击者提供受害者操作的实时视觉上下文。窃取数据随后通过SMTP、FTP甚至Telegram机器人等合法协议，伪装成正常网络流量外传至攻击者的命令控制服务器。

此次攻击生命周期的详细分析揭示了现代网络安全的关键现实：用户交互往往是最薄弱环节，但由此触发的自动化攻击链却极为先进。为防御此类隐蔽入侵，企业需部署能监控进程镂空和内存执行的高级端点检测与响应(EDR)方案，并配合全面的员工反钓鱼意识培训。

参考来源：

Inside the Stealthy Agent Tesla Infection Chain

https://securityonline.info/agent-tesla-infection-chain/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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