---
title: RSAC：AI驱动的五大攻击技术
url: https://mp.weixin.qq.com/s/LnYF_NYX4aLIbUHGmoHXyQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:48:20.047381
---

# RSAC：AI驱动的五大攻击技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88XOxwGRXdZwxBybfb8spR1eqFOhmYmbUibPzkJFusbasXUuRmqEghaXKp3icrF7icbSTIN0koWXbBjUT3hgUeM37QcggWY1JLBsP8/0?wx_fmt=jpeg)

# RSAC：AI驱动的五大攻击技术

数世咨询
数世咨询

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Ucgehdgtkiaydav1K8EVu2ib3obpn9XZb6rtsZXAcwl0uHCdddA89W8LmdjaMV6fePRYathgCVTTPg3XqEuFLOCdZ73gQggOo4o/640?wx_fmt=gif&from=appmsg)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif#imgIndex=1)

**#****01**

基于token，零日漏洞的成本大大降低。

**#****02**

供应链风险，你的供应商的供应商的供应商……

**#****03**

OT被攻破后的关键证据往往无法获得，因为数据会直接蒸发。而进入OT环境的AI Agent，使情况变得更加恶劣。

**#****04**

在数字取证与事件响应中，人工智能不知道该寻找什么，也无法像人类那样解读证据。

**#****05**

"GTG 1002"利用人工智能工具自动化了高达90%的攻击过程，大部分破坏是在没有人为参与的情况下造成的。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

RSA Conference 2026大会，每年SANS研究人员都会在RSA Conference大会上公布五大攻击技术。但2026年出现了一个明显的转变：这五项技术全部由人工智能驱动。"如果我们在攻击中指出一个与人工智能无关的趋势，那是在欺骗各位，"SANS总裁兼演讲主持人Ed Skoudis在介绍"五大攻击技术"主题演讲时向观众解释道。"这就是我们行业目前的现状。"

攻击技术一：人工智能生成的零日漏洞——从稀缺到过剩

零日漏洞利用曾经只属于那些资金充裕、配备了复杂研究人员的国家级行为者。但SANS Institute研究员兼高级技术总监Joshua Wright表示，人工智能已经打破了进入零日漏洞领域的壁垒。事实上，Wright指出，独立研究人员已经在广泛部署的生产软件中发现了人工智能零日漏洞，攻击者仅需花费116美元的AI token成本即可运行——比起以往复杂攻击者为此投入的数百万美元，这着实是一笔可观的节省。"攻击者已经比我们更快了，"Wright说。"人工智能让这一差距在我们当前的速度下变得无法弥合。"Wright建议，各组织必须加快速度才能跟上，这可以通过加速打补丁、自动化和人工智能驱动的防御工具来实现。

攻击技术二：供应链风险——你的供应商的供应商的供应商

Wright表示，在过去一年中，三分之二的组织受到了软件供应链攻击的影响，第三方参与漏洞的事件也大幅增加，向开源注册表发布的恶意软件包数量也在激增。他指出，Shai-Hulud蠕虫已经感染了超过一千个开源软件包，并在487个组织中暴露了14,000个凭证。

同样，一个团体在六个月的时间里攻破了Notepad++的更新基础设施，有选择地向能源、金融、政府和制造等领域的目标交付后门。"你的攻击面不是你选择的软件，而是其背后整个供应商生态系统，"Wright说。

他建议，在下一次供应链攻击发生之前提前规划是明智之举。他建议，为适应这一点，各组织不应仅仅要求一份材料清单，而应要求提供软件构建方式的可验证证明。此外，各组织应将团队每天依赖的每个更新渠道和开发者工具视为潜在的供应链风险。

攻击技术三：OT复杂性与根本原因危机

SANS Institute研究员、Dragos创始人兼首席执行官Robert Lee解释说，他在OT事件响应方面积累的多年深层经验，帮助他认识到他所称的"日益严重的问责危机"。他警告说，OT被攻陷后的网络活动和其他关键证据往往无法获得——数据会直接蒸发。

Lee举了一个2025年12月针对波兰分布式能源资源的攻击作为例子，这是Dragos参与处理的案例。调查人员能够确认破坏已经发生，但由于缺乏OT监控覆盖，他们无法看到威胁行为者在系统内部做了什么。在另一个案例中，一个具有摧毁设备意图的国家级威胁行为者盯上了一个对其基础设施毫无可见性的设施。一个月后，设施发生了爆炸。

令人不寒而栗的是，调查人员至今仍不知道破坏是来自攻击还是单纯的事故。"各国政府不会对无法了解关键基础设施发生了什么以及为何有人死亡感到安心，"Lee说。"这种情况是不可接受的，而且已经在发生。"他补充说，更糟糕的是，代理型人工智能已经进入了OT环境，各组织需要迎头赶上并获得对这些系统的更多可见性。他警告说，对OT系统可见性增加的投资，不能等到下一次灾难发生时才被迫应对。

攻击技术四：人工智能的阴暗面——数字取证与事件响应中的不负责任使用

作为全球领先的数字取证与事件响应（DFIR）专家之一、SANS Institute教师负责人兼高级取证专家Heather Barnhart表示，各组织在部署人工智能时，如果没有培训、验证框架和调查规范，就是在自寻失败。她补充说，人工智能不知道该寻找什么，也无法像人类那样解读证据。

人工智能给出一个有把握的错误结论并没有帮助，而且在响应过程中也肯定不能节省任何时间或资源。"大多数漏洞的失败不是因为工具，"Barnhart说。"它们失败在决策点上。人工智能不能成为决策点。"她提醒各组织，人工智能也正被用于无人监控的媒介，比如人工智能笔记工具。攻击面已经远远扩展到网络之外，在每一步都需要授权具有决策权的人类来主导。

攻击技术五：发现邪恶——自主防御的竞赛

Rob Lee还表示，安全研究人员估计，由人工智能驱动的攻击比老式的人工攻击快47倍。这意味着威胁行为者可以用一个被盗登录凭证，在不到10分钟内在AWS等环境中从完全管理员控制权。

以2025年11月Anthropic记录的一次活动为例。这个被称为"GTG 1002"、被归因于某国家级支持团体的行动，以30多个政府和金融机构为目标，并使用人工智能工具将攻击过程的最多90%自动化，包括网络内部侦察、漏洞利用和横向移动。大部分破坏是在没有任何人类帮助下完成的。防御者如何应对？"他们有人工智能，"Lee说。"现在我们也要建立我们的（人工智能）。"他指向了SANS Institute的开源计划Protocol SIFT，该计划旨在帮助防御者赶上使用人工智能的攻击者。它使用人工智能来组织工作流程、提炼洞察并协调工具。

同时，由人类负责验证结果和做出决策。"目标是加速分析师，而不是取代他们，早期结果表明，该模型可以显著压缩响应时间，"Lee说。在一次涉及复杂双周攻击场景的响应演练中，一名分析师使用Protocol SIFT在不到15分钟内完成了整个调查，包括识别恶意软件、绘制攻击者移动轨迹、将战术、技术和程序（TTP）活动与已知框架对齐，以及确定后续步骤。

Lee补充说，正是防御者能够快速行动并与全球安全社区协调的能力，将给防御者带来真正对抗攻击者的优势。

原文地址：https://www.darkreading.com/threat-intelligence/sans-most-dangerous-attack-techniques

来源：数世咨询    编译：泽钧

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88UR6icztiaMDcvGBs077WN4FIDNT7bJkZ4NKH5o7uRIGIzibFZa2mq1qXCzmtBEz8ICcicPia9n64FMynVib4bjvbnZCppHQ1Z5TpIkQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[安测促发展，积聚创未来——2026网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88WjwEF932bqbsMPq0DTA9D2YkakBfmTLKazcj1TV2FCpaSMerCv4bCfffibN5lN92u3woYmLXauY5iazscibMiaXvuVD6xxNSGszGM/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

[征集标准参编单位！关于征集《消费级无人机检验检测通用要求》认证认可行业标准参编单位的通知](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

****热点聚焦****

****HOT！！****

**[邬江兴院士：AI内生安全问题及可信应用系统研究](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524079&idx=1&sn=f4e4c0da54b241108c7940047ee1be77&scene=21#wechat_redirect)**

**[征稿启事 | 16个热点问题，欢迎来稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247521812&idx=1&sn=df8ac4f4f7071445227e454703cf3eac&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[新书出版 | 邬江兴院士发布最新英文著作](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247525711&idx=1&sn=7c47de2a92853e19af33b0c0ff76063e&scene=21#wechat_redirect)**

**[可信内生安全、变结构拟态计算技术等入选“新一代信息工程科技新质生产力技术备选清单（2024）”](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524134&idx=1&sn=e8f83445d7ea448a8ea38a06e228f77c&scene=21#wechat_redirect)**

**[持续赋能内生安全！第五届网络空间内生安全学术大会暨第八届“强网”拟态防御国际精英挑战赛完美收官](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534994&idx=1&sn=a35dc208810295861b94d6af88c2c7e8&scene=21#wechat_redirect)**

[蓝皮书下载 | 第五届网络空间内生安全学术大会，四本蓝皮书重磅发布](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535240&idx=2&sn=da33dc8d3ad64e3c161538e0d3a14494&scene=21#wechat_redirect)

**[正式发布！网络空间内生安全理论和标准体系入选信息通信领域十大科技进展（附手册）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247527344&idx=1&sn=b9f70ff5f052f6866645a8bc506f43bd&scene=21#wechat_redirect)**

**[递交2025网信生态高质量发展“开年答卷”  网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247528656&idx=1&sn=28c73aa522cb86038989efae1f2c8ee2&scene=21#wechat_redirect)**

**[邬江兴院士为五色石先导班学生授课](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247530005&idx=1&sn=ae066476dfc29be0b0d528a64e6b6679&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[邬江兴院士——AI时代内生安全自主知识体系建设的思考](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534787&idx=1&sn=3e2e3df01300637de00f028894fd6493&scene=21#wechat_redirect)**

**[出版啦！南京市网络空间内生安全协会5项团体标准在中国标准出版社正式出版](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534684&idx=1&sn=1814c0aed65128d0e345064e5b7b83d1&scene=21#wechat_redirect)**

**[邬江兴院士 | 破击美欧网络弹性铁幕——基于自主知识技术体系的数字生态系统底层驱动范式变革](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247533711&idx=1&sn=7a843b5f85bfce11554c51cb97c5e1f0&scene=21#wechat_redirect)**

**[喜报！南京市网络空间内生安全协会获评为AAAA等级社会组织！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535467&idx=1&sn=343185d42eca10a491337f0111035b24&scene=21#wechat_redirect)**

**[邬江兴院士提出“时空协同复杂度”理论——揭秘介观尺度智能涌现机理引领AI架构革新](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535842&idx=1&sn=bf905ee97eb951d993e28c518e8adf67&scene=21#wechat_redirect)**

**[南京市网络空间内生安全协会第二届会员大会暨换届选举大会圆满举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536554&idx=1&sn=e7d5d716f55a62c9f64360c2a527d45d&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[邬江兴院士：人工智能内生安全质量检测中试平台](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536446&idx=1&sn=0ede0c81fb0d67df45be75a62e84b87b&scene=21#wechat_redirect)**

[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)

[国家数据局局长刘烈宏：中国人工智能发展现状、趋势与未来产业机遇](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537347&idx=1&sn=82902010c542ccc131383e73188601fa&scene=21#wechat_redirect)

[欧洲科学院院...