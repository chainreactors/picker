---
title: 顶级iPhone黑客工具“DarkSword”曝光：六连环漏洞，多国用户数据遭窃
url: https://mp.weixin.qq.com/s/O6TD0nHPnSQyyArWV5kaQA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:59.675053
---

# 顶级iPhone黑客工具“DarkSword”曝光：六连环漏洞，多国用户数据遭窃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3EdkYYTB7v5FW8urI0ksicbOYXAJ4T94ZGM8SekjBvyytPCO1e5oQ9bib38AsmMKpyNePZC5zp7Afo5cfekibc0TDtONz6JFfcUY/0?wx_fmt=jpeg)

# 顶级iPhone黑客工具“DarkSword”曝光：六连环漏洞，多国用户数据遭窃

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

一个名为“DarkSword”的高级漏洞利用套件，自2025年11月起被多个商业监控软件厂商及国家级黑客组织使用，已导致沙特阿拉伯、土耳其、马来西亚和乌克兰等地的用户成为目标，其个人数据面临严重泄露风险。

不同于一般的恶意软件，“DarkSword”是一套完整的“全链式”攻击武器。它巧妙地串联了六个不同的安全漏洞，其中四个在被利用时属于“零日漏洞”（即苹果公司尚未发现并修复的漏洞）。这套攻击链能够覆盖从iOS 18.4到18.7的多个系统版本，对尚未更新的iPhone构成巨大威胁。

整个攻击流程完全通过JavaScript代码执行，无需用户点击任何可疑链接或安装应用，仅需访问一个被植入恶意代码的网页即可触发，隐蔽性极高。

其攻击步骤环环相扣：

1. 初始突破（远程代码执行）：攻击首先利用JavaScriptCore引擎（负责Safari浏览器的核心解析）中的两个漏洞（CVE-2025-31277, CVE-2025-43529），在目标手机上获得初步的代码执行能力。

2. 安全机制绕过（PAC绕过）：紧接着，利用一个在动态链接器（dyld）中的漏洞（CVE-2026-20700），绕过苹果引以为傲的指针认证（PAC）防护机制，为后续攻击扫清障碍。

3. 沙盒逃逸（突破限制）：为了获得更高权限，攻击者分别利用WebGL组件（CVE-2025-14174）和XNU内核中的内存管理漏洞（CVE-2025-43510），连续突破了两层沙盒限制，将控制范围从Web内容扩展至系统核心。

4. 权限提升与载荷投放：最后，利用内核文件系统中的竞争条件漏洞（CVE-2025-43520）提升至最高权限（Root权限），并将最终的恶意载荷植入系统，实现对设备的完全控制。

安全研究人员将“DarkSword”的使用与三个不同的威胁组织关联起来，每个组织都部署了功能各异的定制化后门：

UNC6748 & “GHOSTKNIFE”：该组织通过一个伪造的Snapchat登录页面（snapshare[.]chat）传播恶意程序。其部署的后门“GHOSTKNIFE”是一个轻量级的JavaScript后门，能窃取账户信息、消息记录、浏览器数据，甚至能够秘密录制音频。为了躲避检测，它会在窃取数据后主动删除设备上的崩溃日志。

PARS Defense & “GHOSTSABER”：土耳其商业监控厂商PARS Defense使用该漏洞套件，针对土耳其和马来西亚的用户。其部署的“GHOSTSABER”功能强大，支持超过15种指令，包括文件窃取、数据库查询等。更令人担忧的是，部分高级功能（如录音、实时定位）尚未在后门本体中完成，暗示攻击者可能会在后续阶段动态下载更完整的恶意模块。

UNC6353 & “GHOSTBLADE”：这个被怀疑与俄罗斯有关的间谍组织，主要通过入侵乌克兰的合法网站，在其中植入恶意代码来实现攻击。其部署的“GHOSTBLADE”更像一个“数据挖掘机”，不提供交互式控制，而是专注于全面收集信息，其目标包括iMessage、Telegram、WhatsApp消息、加密货币钱包、Safari浏览记录、健康数据、钥匙串以及保存的Wi-Fi密码。

值得庆幸的是，GTIG安全研究团队已将相关漏洞报告给苹果公司。截至目前，所有六个漏洞均已在新版系统中得到修复，其中大部分在iOS 18.7.2和26.1版本中已修复，而关键的PAC绕过漏洞（CVE-2026-20700）也在随后的iOS 26.3版本中被封堵。

对于广大iPhone用户而言，立即将设备更新至最新的iOS版本防御此类攻击的最有效手段。如果设备因型号较老无法更新至最新系统，建议开启“锁定模式”，这能大幅增加攻击的难度，为设备提供一道额外的安全屏障。

资讯来源：综合自GTIG、iVerify及Lookout安全研究机构的公开报告与分析。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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