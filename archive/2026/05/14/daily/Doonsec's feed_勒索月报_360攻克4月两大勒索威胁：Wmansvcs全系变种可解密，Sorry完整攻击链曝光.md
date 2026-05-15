---
title: 勒索月报|360攻克4月两大勒索威胁：Wmansvcs全系变种可解密，Sorry完整攻击链曝光
url: https://mp.weixin.qq.com/s/A6pONqpunxvP_qkBXaj2AQ
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:51:17.853212
---

# 勒索月报|360攻克4月两大勒索威胁：Wmansvcs全系变种可解密，Sorry完整攻击链曝光

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zfoRGB81MxOPQxO2BVyTibaickPOwltu2qSkDRhf2vtCgvLiacsDR5Nm90zcsm9ZeHwZbWNa3tRLmSF4tEpmhU8F7ibl69jhwTPbepecwQhYTPM/0?wx_fmt=jpeg)

# 勒索月报|360攻克4月两大勒索威胁：Wmansvcs全系变种可解密，Sorry完整攻击链曝光

360数字安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

在AI浪潮席卷全球的背景下，勒索软件的威胁格局正以前所未有的速度裂变与升级。在刚刚过去的4月，全球网络攻击活动依旧强势，各类勒索攻击借助自动化工具与持续扩大的数字攻击面，攻击频率与破坏力同步攀升。如今，勒索攻击所带来的早已不止是技术防线的局部失守，而是正从单点缺口演变为足以击穿生产运营、瘫痪关键服务、动摇政企核心业务的全局性战略威胁。

**近日，360数字安全集团独家发布《2026年4月勒索软件流行态势分析》报告。在360安全智能体的深度赋能下，该报告系统揭示了勒索攻击向产业化、智能化加速演进的现实格局，精准刻画了主要病毒家族的迭代路径及其对能源、金融、制造等关键行业的定向渗透风险。在此基础上，报告还进一步夯实了“事前主动防御、事中快速阻断、事后持续加固”的闭环防护理念，为广大政企机构提供了一套覆盖战略规划、日常运营与应急响应的全流程解决方案。**

报告显示，2026年4月，全球勒索软件威胁版图仍在继续加速扩张。双重勒索方面，HYFLOCK、Audit、TiMc、BlackWater、Aur0ra、M3rx等多支新力量相继入局；而传统勒索软件领域也不断演化出TorBrowserTor、NBLock、JanaWare等多个家族。

在传播量占比方面，Weaxor家族整体传播量仍以25.26%的占比继续领跑榜单。**Wmansvcs家族则完成跃进，以22.68%的占比升至第二位。**该家族自2025年6月首次出现以来，便迅速跻身国内最活跃的勒索软件之列，感染量长期稳居前二。今年2月，它曾成功终结Weaxor长达数月的垄断，登顶传播占比第一，反超关键在于从单一IP升级为多IP远程桌面攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMCxciaiaylE64l1TkaOpwEQueZqgUJHnUL8qxAicfBicHMLcARnCtapHntlLAJRa2ZynGUBrbB5IsCuuC0Go4oQp55yfUPI2t2P9k/640?wx_fmt=png&from=appmsg)

*2026年4月勒索软件家族占比*

近期传播中，该团伙展现出高度明确的攻击意图，持续聚焦国内用户，通过远程桌面协议（RDP）弱口令实施定向投毒与横向渗透。目前，该家族主要演化出“.peng”和“.wman”两个后缀分支。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxNEEyicibTv3An0ooRMxwjqwTLknTgIiagHydp7qmXicU79ia1xUCMqCXMBFPaWeLxSfwVw8nia1OVJLDFmyH14vfiakxaLC6rDHsd7ts/640?wx_fmt=png&from=appmsg)

**值得注意的是，依托360安全智能体的赋能，目前已经能够成功解密该家族现有的全部变种，并为众多受害者提供了免费的技术解密服务。**

榜单第三位被Sorry家族占据，其传播占比为20.62%。该勒索软件自今年3月出现以来，持续利用各类常见企业软件漏洞发起攻击，具备远程加载攻击载荷及跨平台勒索的能力。本月，360数字安全集团对这一新晋高危勒索软件进行了深度分析，全面解析了其在国内的投毒活动，为相关企业快速应对这一新增威胁提供了技术指引与参考。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxOxlicT01DUMgA5qOHgUpscjVEdO2XRPnNpllwBzYibAawbiapRic7iaX8ZDmYibuFqZwHIWaticbe1sDG20P2S3QtstIicDyic6FcnibJ0U/640?wx_fmt=png&from=appmsg)

从攻击目标的分布来看，4月基本延续了3月的态势。在所有操作系统中，Windows 10依然最受勒索软件“青睐”，其次分别为Windows Server 2012与Windows Server 2019。若按系统类型划分，桌面PC仍然是主要受害对象，与此同时，针对NAS平台的攻击活动也日趋频繁。

值得关注的是，随着双重及多重勒索模式的持续升温，数据泄露威胁同步攀升。360安全智能体监测数据显示，本月全球范围内共有789家政企机构新近沦陷。从主要勒索家族的赎金收益结构来看，Qilin、Thegentlemen与Dragonforce位居前三，占比分别为14.07%、10.52%和8.24%。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxMYXPvCSnFicRCSxJnsY0KUl345ruJuQUNk8en7UtpibS3ZOtmE1icjfeJib7cvJ8mrKBLdwH2zSBMtIGkxicw68Vdm4XQ95XOgFGOw/640?wx_fmt=png&from=appmsg)

*2026年4月通过数据泄露获利的勒索软件家族占比*

**作为数字安全的领导者，360数字安全集团多年来一直致力于勒索病毒的防范。基于过去20年积累的安全大数据、实战对抗经验，以及全球顶级安全专家团队等优势能力，360创新构建出依托安全大模型赋能的“安全智能体蜂群”体系。**

该体系将安全专家能力和经验进行固化，集成终端防勒索、钓鱼邮件检测、终端病毒查杀等数十类垂直安全智能体。通过安全智能体的协同调度，该体系不仅可以完成自动化、毫秒级的威胁识别与处置，并能够针对勒索病毒从攻击前、攻击中到攻击后的每一个主要节点进行定向查杀，助力广大政企机构构建AI时代下面向勒索病毒的全生命周期防护能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2MhjMzIW1B3IDC6MVuSFcEOWhSaibfutibsDunLsunQ3uV0GiaxW2HKWx0dzia3U6EEP0ccEY26EzduA/640?wx_fmt=png&from=appmsg)

**让病毒进不来：**在终端与流量侧部署360安全探针，通过互联网入口检测等主动防御能力实时监测威胁。一旦触发病毒告警，终端安全智能体将自动获取样本，快速完成病毒家族鉴定，并联动威胁情报进行深度分析，最终实时同步威胁级别与处置结果，实现在病毒落地阶段的精准查杀与拦截；

**让病毒散不开：**终端勒索防御智能体能够对勒索病毒的异常加密行为和横向渗透攻击行为，进行智能化分析拦截和检测阻断，实现“一点发现，全网阻断”；

**让病毒难加密：**通过终端安全探针结合云端情报赋能，利用终端安全智能体的自动溯源分析能力，能够精准判断勒索病毒身份，并进行反向查杀；同时内置文档备份机制，可无感知备份日常办公文档和敏感业务数据，对备份区文件进行全面保护，不允许第三方程序对备份区进行非授权操作，从而阻断勒索病毒对备份区的加密行为；

**加密后易恢复：**内置大量360独家文档解密工具及云端解密平台，云端支持1000+类勒索文件解密、本地支持100+类勒索文件解密，并通过终端安全智能体实现加密后的全方位恢复工作。

目前，360安全智能体蜂群体系针对不同类别的勒索病毒，不同客户体量与需求，推出了多元产品及服务套餐，已累计为超万例勒索病毒救援求助提供帮助。

**欢迎点击【阅读原文】**

**获取完整报告**

**如需咨询相关服务**

**请联系电话**

**400-0309-360**

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 2026两会观察 | 周鸿祎为智能体人才培养献策，360先行落地 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585196&idx=1&sn=411d31527985da5cfb73f1beb83c429b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ●  覆盖亿级用户！360发现全球高危漏洞 漏洞挖掘智能体首次披露 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585736&idx=1&sn=3f8646fdec13122c42f50da17a326780&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● 国内首个！360推出Wmansvcs勒索软件专用解密服务 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585720&idx=1&sn=a9d6a2bbb8dc837f46267354353f25a7&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 360亮相2026世界互联网大会亚太峰会 智能体成果引行业关注 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585693&idx=1&sn=55047066b073b716f9b19dca0a73bccf&scene=21#wechat_redirect) | |

预览时标签不可点

阅读原文

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