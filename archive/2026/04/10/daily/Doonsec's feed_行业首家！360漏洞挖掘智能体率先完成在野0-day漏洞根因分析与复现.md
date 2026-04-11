---
title: 行业首家！360漏洞挖掘智能体率先完成在野0-day漏洞根因分析与复现
url: https://mp.weixin.qq.com/s/PjNXBFe8Eona3ep1vAqm9Q
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:15:49.675577
---

# 行业首家！360漏洞挖掘智能体率先完成在野0-day漏洞根因分析与复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zfoRGB81MxM0WITLcy6sUat0b13F3ic2vibiaCkmvWeVGkYeAgt2LjM4jWkyWSNf5j7kjXf2uwayOWw4dH7dB4E3ebwrqtGKDWMob3OWwictG2E/0?wx_fmt=jpeg)

# 行业首家！360漏洞挖掘智能体率先完成在野0-day漏洞根因分析与复现

360数字安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

news

**近日，360数字安全集团依托自主研发的漏洞挖掘智能体体系，对Adobe Acrobat Reader一款在野0-day高危漏洞的自动化复现与验证，实现了行业首次由AI智能体独立完成0-day漏洞根因分析与自动化复现的突破。**该漏洞可直接突破软件内置安全防护机制，实现远程代码执行与主机控制，威胁覆盖全球海量政企及个人用户。目前，360漏洞复现智能体已完成漏洞全流程验证，并对外发布安全通告与防护建议，为广大用户筑牢安全防线。

Adobe Acrobat Reader是全球使用范围最广、应用场景最丰富的PDF阅读与编辑工具，广泛覆盖办公、政务、金融、教育等关键领域。因其用户基数庞大、使用频次高，一旦出现高危漏洞，极易被黑产团伙利用，引发大规模数据泄露、定向攻击乃至系统性安全事件。

据360安全专家介绍，此次发现的特权API权限绕过及远程代码执行漏洞，核心隐患源于Adobe Reader底层JavaScript引擎在权限校验环节存在安全缺陷。攻击者可通过构造特制PDF文档，嵌入精心设计的恶意代码，绕过软件安全策略限制，突破防护边界获取系统高级操作权限。攻击一旦触发，攻击者可在用户完全无感知的状态下，读取本地敏感文件、获取系统核心信息，并建立隐蔽的远程控制通道，最终实现对受害设备的持久化控制与数据窃取。整个攻击过程隐蔽性强、危害等级高，不仅可能造成隐私泄露与核心数据失窃，还可被用于定向攻击、勒索病毒投放等恶意活动，安全风险极高。

经360安全团队验证，Adobe官方截至目前尚未发布针对该漏洞的补丁，Adobe Reader 2026.001.21367（最新版）及以下版本均受波及。更为严峻的是，即便用户开启保护模式、AppContainer隔离、受保护视图等软件默认推荐的安全机制，也无法有效抵御该漏洞的利用。目前，该漏洞相关利用信息已在互联网公开传播，黑产团伙与恶意攻击者极易获取并滥用，全球用户均面临紧迫的安全威胁。

**本次漏洞的快速发现、深度分析与全链路验证，全程由360漏洞复现智能体独立完成，自动化完成核心验证流程。**作为漏洞挖掘智能体体系的重要组成，漏洞复现智能体深度融合360二十余年攻防实战经验与大模型能力，可自动化实现威胁线索捕捉、漏洞原理分析、攻击环境构建、漏洞利用验证等全流程工作。在本次Adobe Reader漏洞研判中，智能体精准定位风险根源，高效完成沙箱穿透、权限绕过、文件读取等关键验证环节，快速输出可复现POC与完整攻击链，将传统人工数天的分析周期压缩至小时级，大幅提升高危漏洞响应与处置效率，成为应对智能时代网络威胁的核心安全能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxOTkKADpnick5YnibDHs9Ep2ic25j3LaFicwLGU9sRUysmlemoWdotnze58T8hDkd55Ispd6MQm6fprmsmxwR31DaL7XGrthjkyHrk/640?wx_fmt=png&from=appmsg)

截至目前，360漏洞挖掘智能体体系已连续发现并披露一系列高价值安全漏洞，尤其在AI智能体、大模型应用等新兴领域持续产出重要漏洞成果，已成为应对智能时代网络威胁的核心安全能力。

针对此次高危漏洞，360已第一时间发布临时安全防范建议，帮助用户快速降低风险：

**1**

用户进入Adobe Reader首选项，在JavaScript设置中关闭“启用 Acrobat JavaScript”功能；

**2**

临时办公可使用浏览器内置PDF阅读器替代；

**3**

待Adobe官方补丁发布后，第一时间完成最新版本升级。

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 2026两会观察 | 周鸿祎为智能体人才培养献策，360先行落地 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585196&idx=1&sn=411d31527985da5cfb73f1beb83c429b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ●  360龙虾卫士重磅上线：九大能力专治OpenClaw“裸奔” | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585414&idx=1&sn=eda1a5e0a9282e83255dfe33c7de4ab7&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● IDC双报告首推：360以绝对实力护航每只“龙虾”安全 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585375&idx=1&sn=e70a863eb3baac335080bdc9c4d0143a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 360安全龙虾「养虾速成课」正式上线ISC.AI学苑！ | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585434&idx=2&sn=9e145e933928722c36df13f6cdbd53dd&scene=21#wechat_redirect) | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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