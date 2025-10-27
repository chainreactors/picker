---
title: 全球DDoS攻击观察：最新变化与未来趋势
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534975&idx=2&sn=376cf2dfb88de923fcb8e1e14cccfd8d&chksm=c1e9c52ef69e4c381852dbf8875f67efacf5b7a0094bc56ae6b74efe384bdbaaf7f0fc564dcc&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-28
fetch_date: 2025-10-04T08:15:21.459455
---

# 全球DDoS攻击观察：最新变化与未来趋势

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogspRgbsEyFP3I8P1QgyPuLD11CicFmCbWjnQyAd7fZ28FgK3YIuibCbRWG4trTSZVu1wxIrB18yzsKg/0?wx_fmt=jpeg)

# 全球DDoS攻击观察：最新变化与未来趋势

关键基础设施安全应急响应中心

以下文章来源于虎符智库
，作者虎符智库小编

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6cVdDn2tUw6HoP5Eic3SrLmnxG32EHGBFYEbGjfOFupgQ/0)

**虎符智库**
.

“虎符智库” 专注解读网络安全重大事件与技术趋势，提供高层决策参考。

随着全球各大企业和机构加强网络空间安全防御，并采取更主动保护措施，网络攻击者正在调整其攻击技术，提高其攻击的复杂性。网络犯罪经济的产业化，客观上为网络犯罪分子提供了更多的工具和基础设施，导致全球的网络犯罪率持续上升。

2022年上半年，网空安全威胁集中在俄乌战争，以及世界各地民族国家攻击和黑客活动主义的兴起。2月，乌克兰遭遇该国历史上最大的分布式拒绝服务（DDoS）攻击，严重影响了政府网站和银行的网络服务。随着网络攻击的持续，对包括英国、美国和德国在内的众多国家带来连锁反应。国家攻击组织和黑客活动主义者对英国金融服务企业发起大量攻击，主要表现为DDoS攻击的数量大幅增加，其目的是试图破坏乌克兰的盟友。

黑客主义活动在2022年持续猖獗。除了出于政治动机的攻击外，DDoS攻击影响了广泛的行业，特别是游戏行业继续受到高度关注。2022年3月，一场DDoS攻击导致《我们之中》的游戏服务器瘫痪，数日内玩家无法访问热门的多人游戏。2022年下半年，新版本的RapperBot（深受Mirai僵尸网络的启发）被用于针对运行《侠盗猎车手：圣安德烈亚斯》的游戏服务器。

以下为基于微软Azure安全团队观察的2022年DDoS攻击趋势。

# **大量袭击集中在假日期间**

2022年一天内记录到的最大攻击发生在2022年9月22日，攻击次数达2215次。一天内的攻击次数最低的日期在2022年8月22日，攻击次数为680次。微软宣称，2022年网络安全防护减少了52万起针对全球基础设施的攻击，平均每天减少1435次攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/f0ibSzjpDC6p2UXiaDNw2c0S23rIT4ptcmEVwuI0zbZe2uL5KWt2XhL3QkkOmR9pdnYnwBHjh8Ogll65hn7lKsEw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. 2022年每日DDoS网络攻击数量

2022年的6月至8月，DDoS网络攻击数量较低。在年底假日期间，直到12月的最后一周，DDoS网络攻击数量较高。这与过去几年中看到的袭击趋势保持一致，但2021除外，2021年假日期间DDoS攻击较少。2022年5月发生3.25 TBps攻击，这是2022年最高的攻击。

# **TCP攻击仍是最常见的攻击类型**

TCP攻击是2022年遇到的最常见的DDoS攻击形式，占所有攻击流量的63%，包括所有TCP攻击类型：TCP SYN、TCP ACK、TCP洪水等。由于TCP仍然是最常见的网络协议，预计基于TCP的攻击将继续构成大多数DDoS攻击。

UDP攻击也很重要，占所有攻击的22%（包括UDP洪水和UDP放大攻击），而数据包异常攻击仅占攻击的15%。

![](https://mmbiz.qpic.cn/mmbiz_png/f0ibSzjpDC6p2UXiaDNw2c0S23rIT4ptcm8Zo71eezvwTnpW03kSeFEIzUSoDQp1MAYtMvWo7tIsIa8qKcQcNmRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2.DDoS攻击类型

在UDP洪水攻击中，“欺骗洪水”攻击占攻击总量的53%。其余的攻击是“反射放大攻击”，主要类型为CLDAP、NTP和DNS。

研究人员发现 “TCP反射放大攻击”越来越普遍，对Azure资源的攻击使用不同类型的反射器和攻击向量。这种新的攻击向量利用了中间盒（如防火墙和深度数据包检测设备）中不正确的TCK堆栈实现，以引发放大的响应，在某些情况下可以达到无限放大。例如，在2022年4月，研究人员监测到对亚洲Azure资源的反射放大SYN+ACK攻击。攻击达到每秒3000万包（pps），持续15秒。攻击吞吐量不是很高，但涉及900个反射器，每个反射器都有重传，导致pps率很高，可能会降低主机和其他网络基础设施。

# **短时攻击继续流行**

![](https://mmbiz.qpic.cn/mmbiz_png/f0ibSzjpDC6p2UXiaDNw2c0S23rIT4ptcmQGs2RDZWYPuLqL7eM8jicu7tMBBS25lDnpaeia7aWLg3fXmyZoZTs7Yw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3.DDoS攻击持续时间

在过去的一年中，持续时间较短的DDoS攻击更为常见，89%的攻击持续时间不到一小时。一到两分钟的攻击占全年攻击的26%。这并不是一个新趋势，因为短时攻击需要更少的资源，并且对于传统DDoS防御来说，更具挑战性。攻击者通常在数小时内使用多次短时攻击，以在使用最少资源的同时发挥最大影响。

短时攻击利用了系统检测攻击和缓解所需的时间。缓解时间可能只需要一两分钟，但这些短时攻击的信息可能会进入服务后端，影响合法使用。如果短时时间的攻击会导致系统重新启动，那么当每个合法用户同时尝试重新连接时，这可能会触发多个内部攻击。

# **美国、印度和东亚是主要攻击目标**

![](https://mmbiz.qpic.cn/mmbiz_png/f0ibSzjpDC6p2UXiaDNw2c0S23rIT4ptcmaEPF3wTBpAOlxUFiadiawlpDIyP5z7pKjjHh6gAa8JMeqydUItclMdgQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图4. 攻击目的地

与前几年一样，大多数DDoS攻击都是针对美国，印度、东亚和欧洲占了剩余攻击的很大一部分。智能手机的日益普及，以及在线游戏在亚洲的普及，可能会增加DDoS攻击的风险。这也适用于加快数字化转型和云应用的国家。

# **黑客主义卷土重来**

2022年，出于政治动机的DDoS攻击大规模增加。特别是名为Killnet的黑客组织，针对西方政府、医疗保健、教育和金融公司持续进行攻击。俄乌战争中，Killnet一直是俄罗斯的坚定支持者，将DDoS攻击作为其在西方国家制造混乱的主要武器。

美国网络安全与基础设施安全局（CISA）、联邦调查局（FBI）和多州信息共享和分析中心(MS-ISAC)专门发布指南，帮助政府和组织有效应对DDoS攻击，尤其是Killnet等黑客组织发起的攻击。

# **更多物联网设备用于DDoS攻击**

2022年，物联网设备持续被用于DDoS攻击，并扩展到俄乌网络战中。越来越多的攻击重新利用现有恶意软件或利用僵尸网络的模块化特性来实施这些攻击。攻击者还在日益增长的犯罪黑市购买恶意软件和解决方案，以发展其恶意工具包。

Mirai等众所周知的僵尸网络，也被国家攻击组织和不断增长的犯罪组织所使用。此类恶意软件的长期持续存在，突显了其适应性，以及其感染各种物联网设备和危害新攻击媒介的潜力。目前Mirai仍然是主要的僵尸网络，但物联网恶意软件领域的威胁格局正在演变，已经出现了新的僵尸网络，如Zerobot和MCCrash。

# **2023年预测**

2023年，随着新威胁和攻击技术的出现，网络犯罪可能会继续上升。预计可以看到越来越多的DDoS攻击被用作干扰，以隐藏同时发生的更复杂攻击，例如勒索攻击和数据盗窃。

新的物联网DDoS僵尸网络将会出现，由其发起的攻击将继续流行，造成严重破坏。随着全球地缘政治局势日趋紧张，将会看到DDoS被黑客活动者用作网络攻击的主要工具。

未来，DDoS攻击将越来越频繁、复杂且成本低廉，各种规模的组织都必须保持主动，全年都加强防护并制定DDoS攻击响应策略。

**参考资料：**

https://www.microsoft.com/en-us/security/blog/2023/02/21/2022-in-review-DDoS-attack-trends-and-insights/

https://venturebeat.com/security/DDoS-attack-was-largest-ever-in-ukraine-russia-suspected/

https://www.finextra.com/newsarticle/40955/uk-finance-suffers-surge-in-DDoS-attacks

https://www.nbcnews.com/tech/security/taiwanese-websites-hit-DDoS-attacks-pelosi-begins-visit-rcna41144

https://www.pcmag.com/news/DDoS-attack-takes-among-us-servers-offline-for-entire-weekend

https://thehackernews.com/2022/11/warning-new-rapperbot-campaign-aims-to.html

原文来源：虎符智库

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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