---
title: NGINX 模块堆缓冲区溢出漏洞，特定条件下可 RCE
url: https://mp.weixin.qq.com/s/GugzE78-TsFkLO7_YbO_ig
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:42.062259
---

# NGINX 模块堆缓冲区溢出漏洞，特定条件下可 RCE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzzicdjGa81YQSDZBTo5XFSTDs8p5mak0lPm45eUJ0UyficlovOwZibxgdKPOdhuhCxgXN7FCNibZDRaV14HTCicCFQpehAIp9ic74hibkM/0?wx_fmt=jpeg)

# NGINX 模块堆缓冲区溢出漏洞，特定条件下可 RCE

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

NGINX 曝出严重的堆缓冲区溢出漏洞（CVE-2026-42945，CVSS 8.1），未认证的远程攻击者通过向配置了 rewrite 等特定指令的目标服务器发送特制的 HTTP 请求，即可触发堆缓冲区溢出，导致 worker 进程崩溃重启。目前在关闭 ASLR 的环境下可实现远程代码执行，不排除未来绕过的可能性。

**利用前置条件：**

* 攻击者能够网络访问目标平台/服务器
* 该 rewrite 自身的替换字符串中包含问号 ?
* rewrite 指令后紧跟着 rewrite、if 或 set 指令
* 该 rewrite 自身使用了未命名捕获组（如 $1、$2）

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | NGINX ngx\_http\_rewrite\_module 模块堆缓冲区溢出漏洞 | | |
| **漏洞编号** | CVE-2026-42945 | | |
| **公开时间** | 2026-05-13 | **POC状态** | **已公开** |
| **漏洞类型** | 堆缓冲区溢出 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 8.1 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

受影响的软件版本：

NGINX Open Source 1.0.0 <= 受影响版本 <= 1.30.0
NGINX Open Source 0.6.27 <= 受影响版本 <= 0.9.7

NGINX Plus R32 <= 受影响版本 < R32 P6

NGINX Plus R36 <= 受影响版本 < R36 P4

**02**

**修复建议**

**正式防护方案**

NGINX Plus 升级至 37.0.0、R36 P4、R32 P6 版本。

NGINX Open Source 升级至 1.31.0、1.30.1 版本。

**03**

**漏洞描述**

近日，F5 官方披露了 NGINX 核心组件 ngx\_http\_rewrite\_module 中存在的一处高危堆缓冲区溢出漏洞（CVE-2026-42945）。该漏洞源于 NGINX 脚本引擎在处理重写指令和变量赋值时，其内部状态在“长度计算”与“数据复制”这两个阶段中产生了不一致。当配置文件中同时使用了 rewrite 和 set 指令，且重写目标中包含问号时，系统会错误地在计算大小时使用未标记的子引擎，而在执行复制时使用已标记的全局引擎。这种逻辑不一致导致原本用于存储未转义字符的缓冲区被塞入了转义后的超长数据，最终引发严重的堆缓冲区溢出，可致使服务器进程崩溃或远程代码执行。

**04**

**漏洞复现**

360漏洞研究院已成功复现 NGINX ngx\_http\_rewrite\_module 模块堆缓冲区溢出漏洞（CVE-2026-42945），在关闭 ASLR（地址随机化）的环境下，通过漏洞利用反弹 Shell，成功验证了该漏洞具备远程代码执行的能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzzicg1BmckEicwdictk1uYCgJXmfYRJdxX1w6849M0YIQia0yzBtAqu0GliakpLLpywpc4eW3Zib3xw3KoAwLEfgfC5ickFoQyCledmofM/640?wx_fmt=png&from=appmsg)

CVE-2026-42945

NGINX ngx\_http\_rewrite\_module 模块堆缓冲区溢出漏洞复现

**05**

**产品侧支持情况**

**360安全智能体：**支持该漏洞攻击的智能分析**。**

**360测绘云 Quake**：默认支持该产品的指纹识别。

**360高级持续性威胁预警系统**：预计 2026年05月15日发布规则更新包，支持该漏洞利用行为的检测。

**360资产与漏洞检测管理系统**：预计 2026年05月15日发布规则更新包，支持该漏洞利用行为的检测。
**本地安全大脑**：默认支持该漏洞的PoC检测。

**06**

**时间线**

2026年05月14日，360漏洞研究院发布本安全风险通告。

**07**

**参考链接**

https://my.f5.com/manage/s/article/K000161019

**08**

**更多漏洞情报**

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg)

建议您订阅360数字安全-漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。

邮箱：360VRI@360.cn

网址：https://vi.loudongyun.360.net

**“洞”悉网络威胁，守护数字安全**

**关于我们**

360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

360漏洞研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

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