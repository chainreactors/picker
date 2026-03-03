---
title: 从 BeijingCrypt攻击看天珣EDR防护实践，构筑代码漏洞之外的终端安全屏障
url: https://mp.weixin.qq.com/s/eYxaAbPXLxV6OXyDMfn0sg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:30.279289
---

# 从 BeijingCrypt攻击看天珣EDR防护实践，构筑代码漏洞之外的终端安全屏障

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/j1hpA7GJeRApfibSM0fLcd551nvB66bSaEu6BREP3lypGg1dygwngODoaMAxFXyeVcWeI7G0lBwQMV2dq23CfO2icCyHXN4NEr1RaoQEWsUibg/0?wx_fmt=jpeg)

# 从 BeijingCrypt攻击看天珣EDR防护实践，构筑代码漏洞之外的终端安全屏障

启明星辰集团

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j1hpA7GJeRCNRdrEz7f88nn0ROWQHUfAKdSMcZNNzW8Vfj6DydLB9MRl6z8ricsLbUradLuAW1ibZmywZ0es12sctsjKSIybjmjz2g978eN5E/640?wx_fmt=gif&from=appmsg)

近期，Anthropic推出的Claude Code Security作为一款集成于Claude Code的AI安全工具，备受关注。区别于依赖规则匹配的传统静态分析工具，它能模拟安全研究员的分析逻辑，深度理解代码结构，通过组件交互与数据流转分析，精准识别传统手段易遗漏的复杂漏洞。然而，Claude Code Security的能力边界在于静态代码分析，无法触及动态运行时的安全防护。

在实际攻击场景中，大量攻击方式并非利用代码漏洞，而是通过远程桌面爆破、数据库端口攻击、钓鱼邮件等方式，直接对终端、端口或权限进行突破，进而植入恶意程序或窃取数据。这类动态、实时终端入侵行为，需依赖终端侧的全流程行为监测与即时拦截，这正是EDR产品的核心能力所在，也是静态AI工具的防护盲区。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/M82cWMKlQSXz5P09XRtyYmNEmvBJcq3HLzuXeFYiaOBtg5yZq2hDYicXF4BQCElKGib89uic278TU4br0XxyfO9pekXWfgkqjVx51RjY9go7Gso/640?wx_fmt=gif&from=appmsg)

**BeijingCrypt**

**变种勒索病毒攻击手法剖析**

以近期某企业遭遇的BeijingCrypt变种勒索病毒攻击为例，该事件即属于典型的无代码漏洞利用型动态攻击。攻击链路完全脱离代码层面，从技术上让Claude Code Security等AI代码工具失去防护作用。

* 入侵链路隐蔽专业：攻击者通过暴力破解攻破SQL Server数据库密码，完成初始突破后立即执行PowerShell恶意命令，植入CobaltStrike后门，进而下载网络扫描工具与勒索程序的恶意文件。整个过程依托终端进程逐层推进，行为隐蔽且直指核心数据库。

* 加密破坏具有毁灭性：病毒成功植入后，随即对数据库备份、安装程序、办公文件等核心资产进行高强度加密，文件后缀统一改为.bixi，并留下勒索信。若企业无有效备份，核心数据将面临永久性丢失，业务运行遭受严重打击。
* 攻击行为具备普适性：该攻击无需利用企业自研或开源代码的漏洞，仅针对终端设备、数据库的基础权限与端口防护短板，任何存在弱密码、端口暴露、行为监测缺失的企业都可能成为目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j1hpA7GJeRCuia2Y9Zjdk3lgkFrjRFECHVVic25Pw0xap9hoYzr4Pz0NdibbQgNpKleS112A3cox5E8al0ZlsxfF6PtIJxFRpG4gh5lbuoaibWo/640?wx_fmt=jpeg)

文件被加密后，后缀均变为.bixi

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAUCE48mqEfxk5tflHEFRFLzaicicIRhkpSfBGf01tB1eSufd945kDpFp7jiaOXsAluNfSAMuKy356Bjn9sOZich1Fh5YCdP6Xz32U/640?wx_fmt=png&from=appmsg)

BeijingCrypt变种勒索病毒的勒索信

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/M82cWMKlQSXz5P09XRtyYmNEmvBJcq3HLzuXeFYiaOBtg5yZq2hDYicXF4BQCElKGib89uic278TU4br0XxyfO9pekXWfgkqjVx51RjY9go7Gso/640?wx_fmt=gif&from=appmsg)

**EDR运行时防护**

**动态监测 精准阻击**

面对此次高难度动态攻击，启明星辰天珣EDR凭借终端行为实时监测、攻击进程树溯源、恶意程序精准识别等核心技术，实现了对攻击的全流程拦截。

一、毫秒级异常行为检测

通过对终端进程的实时监控，精准捕捉到SQLServer进程执行的高危powershell恶意命令，第一时间识别出异常进程行为，实现对攻击行为的早期预警，从时间维度压缩攻击实施空间。

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRD3jOibNU7uXEMFASUmWGfuq6AlN1mJ3Ch4mQrf3LATtPV6sxwOnf1osTH7YO0CLGr5wYK4bRXkcWJXG2ibABRkkTDEmNiaPWYOqs/640?wx_fmt=png&from=appmsg)

SQLServer进程执行powershell命令进程树

二、全链路攻击溯源

通过构建攻击进程树，清晰还原了从wininit.exe到services.exe，再到sqlservr.exe，最终触发cmd.exe与powershell.exe执行恶意命令的完整进程树，为安全处置提供精准的技术依据。

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRAx9ewAibCLEiaHrh6meicjnFk9yVzon7eTW4TbljUkQ0DfEZLPvar5GiaJIqf3NJ0MnKPtx3MTz6wFzeZPtZPibt1PD04icuPn08vzs/640?wx_fmt=png&from=appmsg)

植入CobaltStrike后门命令

三、多维度恶意程序识别

基于特征库匹配与行为分析相结合的技术手段，成功识别并标记了CobaltStrike后门、网络扫描工具、勒索程序等各类恶意程序，明确各类风险的技术类型与处置建议，实现对恶意程序的精准阻断。

![](https://mmbiz.qpic.cn/mmbiz_png/j1hpA7GJeRBDX4OYhT7nNkJ01au60UEQpffXwCB9MSHxerTGsFO2LKwGRVYxtPBLFekiaA76W52xPOZ9MrRiam05bt1Vhdg91CajCJqkpwF6A/640?wx_fmt=png&from=appmsg)

天珣EDR病毒查杀检测出此勒索病毒相关进程

四、终端层面全流程拦截

从恶意命令执行、后门植入到恶意文件下载，在终端层面有效拦截攻击各环节，避免病毒传播与文件的大规模加密，为企业设备和数据安全筑牢了终端技术防线。

此次BeijingCrypt勒索攻击事件表明，AI技术虽为代码漏洞防护提供了有效手段，但依赖无代码漏洞的动态攻击并未消失，反而以更隐蔽的手段、更普适的路径，成为企业当前面临的主要安全威胁。从技术属性看，EDR等动态运行时防护产品聚焦行为监测与实时拦截，受静态AI工具影响最小，是应对此类攻击的核心手段，也是网络安全体系中具备高技术壁垒的关键环节。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j1hpA7GJeRDib5M2dGxcjsZrP2D8Hib9Jf36l0ZxQvmba7hMp4MfkEvgfg4SUp3rSAs9dsh7g3Vu5EHQiaXkz3zibibsYCkMaxxvibwCAcdWvibe8c/640?wx_fmt=gif&from=appmsg)

完美的代码并不等同于运行时的安全，当代码可由AI生成，防御能力也必须向智能体进化。启明星辰持续深耕EDR终端安全领域，将AI智能分析与EDR实时防护深度融合，通过持续技术创新打造全方位的终端安全解决方案，为用户筑牢“运行时”与“AI对抗”双重防线。

•

END

•

![](https://mmbiz.qpic.cn/mmbiz_gif/j1hpA7GJeRAyvzibhTfcqcC6e5ibxGickQ3Rgrp2XIrN8jwxwIgovicB1hCt5Tv5bEwxaWbLCa8VHvl5zlzXBNLkjERLjPD2SxxuokUDibrIattk/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/BwR7Xg3aXhZeib4948EIKnKMjz0waPZd0Ugx2ERldiaylnDUPODL5gst1RcjwtHWbOlQbFR1wIYMe2LR1AcMPiaNg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651696952&idx=1&sn=f2bb1c66eca7a93bc760079e7ed36523&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/BwR7Xg3aXha9IicKLXriatsDKmgOhWibfq3oIsltPzLBHCIrGM6jHTheaGNxcZkeePtG7kIL3C5GaNZZwUC7uht1A/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BwR7Xg3aXhbViaj0gQhCzVicIDc9gtBzytuEmgsDS4EqCtgpyMohatb3ZicDSDtcJJtvuhV9xpiczTpicJjcXkhVPpA/0?wx_fmt=png)

启明星辰集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwR7Xg3aXhbViaj0gQhCzVicIDc9gtBzytuEmgsDS4EqCtgpyMohatb3ZicDSDtcJJtvuhV9xpiczTpicJjcXkhVPpA/0?wx_fmt=png)

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