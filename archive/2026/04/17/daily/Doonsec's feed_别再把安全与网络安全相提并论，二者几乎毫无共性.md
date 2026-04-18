---
title: 别再把安全与网络安全相提并论，二者几乎毫无共性
url: https://mp.weixin.qq.com/s/LDBmg4finTEmV0ULUso4Ag
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:26:33.962315
---

# 别再把安全与网络安全相提并论，二者几乎毫无共性

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickperkNpETu2MCycB5PuZlrwo0lkhvchqD9SmjkfWcibia7tweicHqLicicVFAuKCjtXwwHn6AzAuFXdhBXbwz68YbmtcdibWy8OJfZBpc/0?wx_fmt=jpeg)

# 别再把安全与网络安全相提并论，二者几乎毫无共性

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**[导读]**

网络安全圈长期流行用 “安全带”“航空安全” 类比网络安全防护，认为可像物理安全一样通过标准化、立法一劳永逸解决问题。但本文认为安全与网络安全本质完全不同。文章从风险属性、危害后果、决策依赖、标准化可行性四个维度，拆解物理安全与网络安全的核心差异，指出安全应对稳定无恶意的物理风险，而网络安全面对的是持续进化、带有恶意的攻击者，新风险永远无法归零。

近一年前，我们在《网络深处》节目中邀请到传奇人物、Duo Security 创始人杜格・宋。

访谈中，他分享的一个精妙类比让我印象深刻。他说，航空领域里，同一种原因导致的飞机失事只会发生一次，最多两次。一旦事故发生，我们会通过分析黑匣子彻查故障根源，随后整个系统与飞机设计都会随之调整，杜绝同类故障再次发生。

但安全领域的情况截然不同。企业总会因同样的方式被入侵，甚至同一家公司会因同一漏洞反复遭袭。杜格将这种状况形容为“最糟糕的土拨鼠日”—— 如同困在痛苦的仓鼠轮中，我们并未真正进步，只是一遍遍重演相同的安全事件。

我想大多数人都能体会杜格的无奈，遗憾的是，这种“循环往复” 几乎每周都在上演。我完全认同他的核心观点，但并不赞同这个类比。我花了许久才想通缘由，因此在本期内容中，**我将阐述为何将安全与网络安全相提并论完全不合理**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcH3Nkic6vtfBS0nia1ibXRkfZsaF8p7EbVbMibUAv3JtONUegeIOZgvWpVN5NcRSicLTloM0Q0uTkeXXuHEdibFLmV9XLjyGOXURmFY/640?wx_fmt=jpeg&from=appmsg)

**备受推崇的安全带类比**

**实则毫无参考意义**

安全领域的从业者总爱拿安全带重塑道路安全的案例说事（若你不了解背景，可参考美国网络安全和基础设施安全局将“安全设计承诺”，与汽车、航空行业的安全举措做对比的案例）。

这个案例的背景是：20 世纪 50 至 60 年代，美国汽车普及率飙升，道路交通事故死亡人数激增。人们很快发现，为汽车加装安全配置能大幅降低死亡率，但落地这一举措困难重重。

首先，通用、福特等汽车制造商强力游说，反对强制安装安全带与出台安全法规，声称这类配置成本高且无必要；而驾驶员也因佩戴不适感，对安全带十分抵触。

最终常识占据上风，1966 至 1968 年，美国出台一系列法律，要求所有新车必须安装安全带。但直到 1984 年，纽约州才颁布首部**强制佩戴安全带**的法律。到 20 世纪 90 年代末，美国几乎所有州都将佩戴安全带列为法定义务。如今，我们早已将安全带视作理所当然，仿佛它从一开始就存在。

人们希望网络安全领域能复制这一模式，由政府立法强制所有人实现“网络安全”，各类行业承诺也秉持着同样的思路。

如果网络安全无需从头摸索，直接借鉴其他领域的成功经验，固然是好事。但遗憾的是，这一思路几乎行不通，核心原因很简单：**安全与网络安全是两类完全不同的问题**。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcrDbFebOmGmibPNyJlK2MiaTYrWqP9BJxlyp1JN4sib6RRJOyEBg23QsLIEQ0N5yCWPmk4GzjQaQhgXOsicpQ1BufNJ6h05jtKTSM/640?wx_fmt=png&from=appmsg)

**安全与网络安全，本质截然不同**

一、安全应对的是稳定不变的问题，网络安全并非如此

首先，安全防护针对的是**稳定、固定**的风险。以最典型的安全带为例，它的设计目标明确且单一：防范车祸中的人员伤亡。需要考量和测试的变量有限（车速、撞击角度、乘客位置、车身高度等）。

我并非说统筹这些变量很容易，但关键在于：**重力不会“学习”，也不会改变作用方式**。物理规则是恒定的，我们清楚事物的运行规律，只要复刻相同环境（变量有限，很容易实现），就能得到相同结果。

但网络安全完全是另一回事。攻击者会不断尝试新手段，直到找到突破口，还会主动调整战术、刻意寻找防护漏洞。

我的朋友、BforeAI 创始人路易吉・伦圭托在领英的评论中说得一针见血：**“很多人总把安全和网络安全混为一谈，实则二者天差地别。安全是找到根源、修复问题，逐步打造零事故的安全环境；而网络安全即便部署防护、完成修复，新风险也会不断涌现，永远无法趋近于零 —— 因为攻击者会主动加大破坏力度与影响范围。这是一个不可控的环境。”**

简单来说，系安全带不会引发新型车祸，但一项网络安全防护措施，往往会催生新的攻击路径。

几周前我曾发布深度分析，探讨我们的安全防护能力其实在提升，只是攻击者的手段也在同步进化，导致进步难以被察觉。这正是核心矛盾：攻击者会持续适配我们部署的防护措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpdfnsibjHeKviaSe5dS352v7OdDjT7Sefv9jkSaAo1jib4U4btAsCMSvxlQlTl4temZjLMDOmE5Otwa0AcMcaBQ9xmwGPzeEhHWV8/640?wx_fmt=png&from=appmsg)

二、安全关乎生命安危，多数网络安全防护并非如此

安全与网络安全的另一核心区别，在于**风险代价不同**。

安全领域的核心关切，始终是人的生命与健康。我们不惜代价彻查飞机失事原因，是因为这类事故后果极其惨重。我们重视汽车安全、食品安全、建筑规范，也是同理—— 这些领域直接关系到人身伤害，而生命是社会公认最珍贵的财富。

值得庆幸的是，网络安全通常**无关生死**。尽管有诸多悲观预测，尽管攻击者理论上可能造成大规模人员伤亡，但绝大多数网络攻击的动机都是牟利。

诚然，医院遭遇勒索软件攻击曾导致患者受害的悲剧，但所幸这类事件并未像部分预测那样大范围蔓延。

大多数人从未听说过重大安全入侵事件，即便自身数据泄露，绝大多数普通人也感受不到实质影响。普通个体面临的网络安全与隐私风险，通常只是这些：

•邮箱被盗，被用来发送垃圾邮件，仅造成不便，通常无不可逆伤害；

•点击恶意链接，电脑安装广告软件，仅偶尔弹出烦人的弹窗，无致命风险；

•信用卡信息泄露，账户产生盗刷，但银行通常会补发新卡、退还损失。

我并非低估网络安全事件对生活的影响。确实有家庭因数据泄露耗尽毕生积蓄，个人隐私曝光造成不可逆伤害，甚至引发死亡。但大多数人将这类事件视作**极端个例**，认为不会发生在自己身上。

我们很难指责大众缺乏认知—— 即便个人数据在暗网被低价贩卖，多数人遭遇优步、艾奎法克斯等数据泄露事件后，仅收到一封入侵通知邮件，以及一套看不懂价值的免费身份监控服务，除此之外毫无感知。

简言之，对大多数普通人而言，网络安全入侵只是**麻烦事**；对大多数企业而言，只是**经营成本**。这与动辄酿成悲剧、夺走生命的飞机失事、车祸完全没有可比性。

三、安全防护旨在减少人为决策，网络安全防护做不到

安全带的使用极其简单：人们只需系上，就能获得保护。它无需配置、不依赖场景，每次作用效果都完全一致。安全气囊、护栏、儿童安全锁等防护配置也大体如此。

这类设计的核心特点是**被动、可预测、无需用户持续耗费心力**。一旦安装，就能在数百万次相同场景中稳定发挥作用。

正是这种简单与可预测性，让安全带、喷淋装置、阳台栏杆等物理安全防护发挥了巨大作用—— 它们无需人们费心思考，就能自动生效。

但网络安全**高度依赖场景**。每一项防护措施，都受客户环境、配置、业务流程、数据流等细节影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpep1ic9ZWj4G5ZzObYibCicVJf6iclMxbEktBn4KFMgXteibPxKicArnZ8vgeLYwm4OBw3icIAYlIKwuyvvAGu81VXnKJV7yvQjjFHObw/640?wx_fmt=jpeg&from=appmsg)

不仅如此，安全防护措施之间还会相互作用，且往往以不可预见的方式发生，一个微小的漏洞就可能引发连锁失效。

错误部署安全工具，本身就会导致入侵，反而为攻击者大开方便之门（想象一下，系安全带反而增加车祸概率）。

正因为网络安全防护的场景依赖性极强，其效果完全取决于人：需要做决策、抽时间、精细调试上千个相互关联的参数。

做好网络安全，远不止遵守安全协议那么简单。人们需要权衡利弊、结合场景判断、跟进落实、说服他人、保持持续的运营规范—— 这比系安全带难得多。

四、安全可通过标准化解决，网络安全不行

安全防护之所以高效，核心原因之一是**可标准化落地**。安全带之所以有效，是因为应用环境高度统一：同款车型的十万辆汽车设计一致、道路标准统一、物理规则在加州与佛罗里达、中国都完全相同。

在标准化环境中，统一推行安全措施就能取得良好效果；一旦验证有效，即可强制所有同类场景执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpceWlfc5G2TJDqrttbON4ErRQz63YZ7tsut6WVCGDYMrqFiboJsBl3rswcS81aWR4uz6xhuOhwDXMnaH5Csubf9niayFdey77fKQ/640?wx_fmt=jpeg&from=appmsg)

但网络安全完全不具备这一条件。首先，企业环境**高度异构、持续变化**，每家企业、每个应用、每项工作流程都高度定制化，因此标准化根本行不通。

更糟的是，**标准化本身可能成为漏洞源头**。最典型的案例就是 VPN 等网络设备：成千上万家用同款工具实现标准化部署的企业，一旦该工具被发现漏洞，会同时遭遇入侵。

因防火墙存在严重漏洞被入侵，就像一万辆汽车因安全带设计缺陷同一天失事—— 由此可见，安全带类比再次失效。

**结语**

我还能列举出更多安全与网络安全不可类比的理由，业内也有越来越多人认同这一观点。

在上述领英评论区中，伊万诺・邦焦万尼也提出精辟观点：“**我最喜欢的安全与网络安全的区别，在于负面事件是否存在人为恶意。安全：无恶意；网络安全：有恶意。因此，一个系统可能安全但不稳固，也可能稳固但不安全。**”

无数案例都指向同一个结论：将安全与网络安全相提并论毫无道理，是时候抛弃安全带这个类比了。

这既是坏消息，也是好消息。坏消息是，我们无法简单套用安全领域的成功模式解决网络安全问题；好消息是，我们可以避免陷入误区—— 不再把节奏缓慢的汽车制造、飞机生产范式，生搬硬套到迭代快速的科技领域。

我认为，我们理应接受一个事实：**网络安全没有捷径，唯有持续完善防御体系，不断提高攻击者的作案难度**。除此之外，别无魔法解法。

最后，强烈推荐大家观看《网络深处》对杜格・宋的专访，内容十分精彩！

原文链接：https://ventureinsecurity.net/p/stop-comparing-safety-and-cybersecurity

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

**安在安全意识团购服务**

安在新媒体面向企业用户，推出“网络安全意识团购服务”，涵盖宣传素材、培训课程、威胁体验、游戏互动等，采用线上线下融合的方式，帮助员工掌握安全要点，并提供定制化安全策略咨询。

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38ItohfRTzvpcE07AIbkJ25dha55ibNRFTkSiaLooM0IVnFWxIAAsKcotGXxaib6xoxGOWXUflQgAc1w/640?wx_fmt=png&from=appmsg#imgIndex=10)

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibNFRaXRrrAqFhwTopSZARuA1k9KjC2qjwVP...