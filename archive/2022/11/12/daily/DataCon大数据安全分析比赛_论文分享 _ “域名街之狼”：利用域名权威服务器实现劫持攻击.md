---
title: 论文分享 | “域名街之狼”：利用域名权威服务器实现劫持攻击
url: https://mp.weixin.qq.com/s?__biz=MzU5Njg1NzMyNw==&mid=2247485299&idx=1&sn=276fe95de0649c3e1ccca134df4da8af&chksm=fe5d1ff3c92a96e5383e593664158630ea3fd6d31f3862ef53a732bd34c59b98f0c1925ae4e1&scene=58&subscene=0#rd
source: DataCon大数据安全分析比赛
date: 2022-11-12
fetch_date: 2025-10-03T22:32:46.489730
---

# 论文分享 | “域名街之狼”：利用域名权威服务器实现劫持攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RicNZQMn3FU7QyAZUvO2rPPSdGTbz75S8XF0ZjS5Uy25Az1b5fEvFW4lqocVSBsVibrt3z2kVvic2icmwV2IFUkBLg/0?wx_fmt=jpeg)

# 论文分享 | “域名街之狼”：利用域名权威服务器实现劫持攻击

DataCon大数据安全分析竞赛

以下文章来源于NISL实验室
，作者张淑涵-NASP

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM766Bv1SQgibFlalH9bqtncibzFunlpyJGeVJiaKNlDOeyfQ/0)

**NISL实验室**
.

网络与信息安全实验室(NISL@THU)，专注于网络、系统、应用、人工智能安全教学与研究，在国际四大安全会议发表三十余篇论文，成果在业界产生了广泛影响力。孕育了蓝莲花、紫荆花等知名战队，发起了网安国际学术论坛InForSec。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU6BGo3eRkbZqNibrl2gtibjgdO1AJowKOibWHFteX0aZRYX0Y0XtBNMUfBgicbfqNmichZnS8Sa4JFL7IQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

“域名体系安全”作为行业热点安全问题备受关注，本次DataCon2022大数据安全分析竞赛也将其作为重点考察内容。赛前，为帮助大家了解最新研究成果，我们将定期分享相关优秀论文，助力各位参赛选手取得更好成绩，欢迎大家关注。**本篇论文分享由清华大学NISL实验室成员整理。**

***【20221111第二期分享】***

**0****0**

****引言****

随着现实世界与网络世界日益融为一体，网络服务已经渗入国民经济的各个领域。几乎所有的互联网上层应用，如在线支付、视频会议、电子邮件等，均需依赖域名系统实现网络资源的寻址与定位。作为互联网的中枢神经，**域名系统在网络安全体系中起到至关重要的作用**，一直都是国际互联网治理领域的热点话题。从普通用户的视角来看，一旦域名系统发生故障，其后果与直接中断网络服务无异。

长期以来的实践证明，域名系统具有灵活的扩展性和优异的解析性能，然而**域名系统的安全性却颇为脆弱**，安全研究人员持续发现域名系统的大量安全缺陷。围绕域名系统的安全研究也成为了国际学术界关注的重点，每年顶级学术会议均有多篇相关论文发表。

本篇论文主题为面向域名权威服务器的域名劫持攻击。本文从域名服务器域名（Nameserver Domain, 以下简称NSDOM）入手，研究域名服务器的“易被劫持性（hijackability）”。针对域名服务器的劫持，本文提出了三种攻击漏洞，分别为存在拼写错误的NS记录、域名服务器内存的比特错误、WHOIS记录中过期的电子邮件；随后，本文分别检测了由这三种漏洞引发的潜在劫持情况，并成功模拟了实际的攻击场景；此外，本文还发现大部分域名服务器运行着过期版本的DNS软件，导致域名服务器易受DDoS等攻击，进而为相应域名的解析带来安全隐患。该论文发表于网络安全领域顶级会议ACM CCS 2017（录取率151/843=17.9%）。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zw3arhxoialSumfBhAtU121tAMb3qAetCx8Rkpkb8iaEPmibwJ4Neaz4JvA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

全文共3000字，阅读时间约7分钟。

*作者介绍：张淑涵，网络研究院2022级硕士生，清华大学计算机系NASP实验室成员，师从李丹教授，目前主要研究方向为DNS系统测量与安全分析。*

**0****1**

****背景介绍****

由于域名托管服务的普及，越来越多的域名授权不在自己子域内的域名服务器来提供解析服务，也即违反Bailiwick规则。例如，域名example.com授权ns.example.com为域名服务器是满足Bailiwick规则（in-bailiwick）的；而若其将ns.another.com或ns.example.xyz作为域名服务器，则将违反Bailiwick（out-of-bailiwick）。在out-of-bailiwick的情况下，多个域名服务器之间将产生解析依赖关系。

本文发现，这种因违反Bailiwick规则而产生的域名解析依赖关系是广泛存在的。作者从5个规模较大的通用顶级域（gTLD）：com, net, org, xyz, info的区域文件中选取服务域名数量最多的前10,000个NSDOM（ns.example.com的NSDOM是example.com）作为研究对象。结果显示，有36.4%的NSDOM的解析至少依赖于一个不满足Bailiwick规则的域名服务器；更重要的是，这样的解析依赖关系具有传递性，在域名之间形成了解析依赖链条，前10,000个NSDOM中的依赖链条最长可达8跳；显然，处于依赖链条下游的NSDOM难以察觉更难以控制其解析所依赖的上游NSDOM，而上游的NSDOM被劫持将影响其所有下游NSDOM及其服务域名的解析。因此，若域名服务器被劫持，其危害性和隐蔽性远大于单个域名被劫持。基于域名服务器的劫持可能进一步引发伪造DNS应答、劫持域名证书、伪造MX记录劫持电子邮件等恶意行为。

**0****2**

******攻击漏洞******

针对域名服务器劫持，本文提出了以下三个漏洞，分别对应三种劫持攻击：

**1. 面向NS记录拼写错误的typosquatting劫持攻击**

域名注册者或管理员在手动配置域名的NS记录时，可能出现将域名服务器名称拼写错误的情况。例如，对于图表1中的polishop.com这一域名，其在com顶级域名服务器中的一条NS记录出现了拼写错误，而这个错误的域名服务器被攻击者发现并注册，此时若解析器选择该条NS记录进行polishop.com的查询，将会访问攻击者控制的恶意域名服务器，并得到恶意的解析应答。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zwQsaq685A3Ucvfia2FerPniaaX4uHlupia7hRYWPia6r38GJUn9Vc5uILDw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表1. polishop.com的顶级域名服务器和权威域名服务器各自返回的NS记录集合

**2. 面向域名服务器内存比特错误的bitsquatting劫持攻击**

由于硬件故障、极端环境等原因，域名服务器在返回应答时内存中可能出现比特错误（bit-flip），造成解码后的NS记录出现错误。文章提到，由于域名服务器通常为多个域名提供解析服务，“域名服务器域名”相较于“单个域名”来说会被更频繁地请求，发生这类比特错误的概率也相对越高。然而，不同于typosquatting攻击，由于本文讨论的比特错误发生在域名服务器的内存中，域名服务器二级存储中的NS记录本身是正确的，因而bitsquatting攻击条件成立的概率相对小于typosquatting攻击。图表2简要展示了bitsquatting的攻击流程：

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zwwWUXibALibia8HvWmkJ6TgoSbQc462YVFnxWROC89Qy5y8iapNJ23SzPSA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表2. bitsquatting攻击流程

**3. 面向WHOIS记录中过期电子邮件的劫持攻击**

电子邮件过期分为两种情况：电子邮件本身过期或电子邮件使用的域名过期。由于域名WHOIS记录中的电子邮件信息通常用于在注册商处管理或修改该域名的基本信息，攻击者可通过劫持过期电子邮件的方式假冒域名所有者对域名信息进行篡改；特别地，如果该域名恰好是域名服务器域，攻击者可进一步劫持授权该域名服务器的域名的解析，从而导致更严重的危害。

从域名服务器的角度出发，除上述三类劫持攻击以外，本文还对域名服务器运行的DNS软件版本进行了扫描。由于部分版本较低的DNS软件安全防护功能较弱，运行过时版本的DNS软件会使得域名服务器易受DDoS等攻击，进而为其服务的所有域名的解析带来安全隐患。

**0****3**

****主要发现****

对于上述三种漏洞，本文分别检测了由其引发的潜在劫持情况，并对实际的攻击场景进行了模拟。

**1. typosquatting劫持攻击**：在本文生成的926,742个存在拼写错误的域名服务器名称中，有5%的域名服务器已被注册，其中有7%正作为活跃域名服务器而被使用（Exploited），其余已被注册的typo域名服务器可能是攻击者提前“占好位”，正在等待拼写错误的发生（Proactive）。对于这些活跃的域名服务器，本文进一步通过HTTP请求检验域名服务器应答的IP地址是否为恶意，发现有16.8%的活跃域名服务器返回了恶意应答。通过注册部分活跃的typo域名服务器，本文成功劫持了共47个受害域名的查询流量，在一个月的观测时段内，平均每天可劫持2000条查询请求。

**2. bitsquatting劫持攻击：**在本文生成的605,965个存在bit-flip的域名服务器名称中，有3.3%的域名服务器已被注册，其中有3%正作为活跃域名服务器而被使用。类似地，通过HTTP请求，本文发现有86%的活跃域名服务器返回了恶意应答。然而，通过注册部分活跃的bit-flip域名服务器模拟实际的攻击场景，本文在一个月的观测时段内平均每天仅能劫持1条受害域名的查询请求，这进一步验证了bitsquatting攻击发生的概率相对小于typosquatting攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zw6150RAVwL9axTGLKUqeBupqYq0vTLNQqqH3zBfukRoLicKgYpZQVFiag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表3. 已被注册的typo/bit-flip域名服务器的应答性质

**3. WHOIS过期电子邮件劫持：**文章发现前10,000个NSDOM中，有11个NSDOM的WHOIS记录电子邮件使用的域名已失效；2个NSDOM的WHOIS记录电子邮件本身已失效。根据电子邮件的所有者信息，本文将这13个NSDOM的被劫持风险划分为三个等级，并分别标注了可能受到劫持影响的域名数量，如图表4所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zwc29NIPib4E2WQnII0SarStW9Sh0oH3rbC40juqSHNxuqSdW6v358v2A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表4. WHOIS电子邮件过期的13个NSDOM及其各自服务的域名数量，按照三个风险等级进行划分

对于域名服务器运行的DNS软件版本，本文通过扫描前10,000个NSDOM域下的312,304个域名服务器，发现有78.33%的域名服务器运行BIND软件，其中6.99%可获取BIND版本信息。以扫描时最新版本BIND软件的发行日期作为基准，图表5展示了这些域名服务器BIND软件的过期天数分布。可以看出，有80%左右的域名服务器BIND软件过期时间长于2015年发行的CVE-2015-5477版本（已证实该版本存在安全漏洞），即运行着存在安全隐患的BIND。值得注意的是，这些域名服务器影响着至少128万个域名的解析，且其中有514个是域名服务器域，也即还会潜在影响更大规模的域名解析。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zwTR8WyYSWhC0z74EK1kaCDK2vE9Z00NCLibSSBX50zniaP4Zseyqsu7LA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表5. 域名服务器BIND软件过期天数的累积分布

**0****4**

****结论****

本文围绕域名服务器的“易被劫持性”，提出了三种攻击漏洞及其对应的劫持攻击，并分别进行了潜在劫持情况的检测以及攻击场景的实现；另外，本文分析了域名服务器运行过时版本DNS软件的规模及其所带来的安全隐患。文章在最后也给出了相应的缓解措施，包括DNSSEC部署、域名注册商增强资源记录确认和检验机制等。

**0****5**

******思考与验证******

阅读完本篇文章，我们产生了如下的一些思考，主要包含三点：

1. 我们注意到，仅在请求域名的NS记录时未返回相应glue记录的条件下，typosquatting和bitsquatting两种攻击才成立，其原因为：typosquatting和bitsquatting两种攻击的核心是解析器对某个错误的域名服务器域（分别由拼写错误和比特错误导致）进行显式查询，而如果解析器在得到NS记录的同时也得到了相应的glue记录，即可直接向域名服务器IP地址发起下一步的查询；此时即使解析器得到的NS记录指向错误的域名服务器域，也不会对其进行显式地解析。当然，利用解析器的缓存机制，这两种攻击也可以成功将错误的NS记录注入解析器的缓存中，实现缓存污染攻击。

进一步，文章在描述bitsquatting攻击时提到，仅当受害域名授权的域名服务器所在顶级域与该域名不同时，bitsquatting攻击才成立，原因是如果域名与其授权的域名服务器在相同的顶级域，通常向顶级域名服务器请求该域名的NS记录时会附带返回域名服务器的glue记录，因而解析器可以直接得到域名服务器的IP地址而非对NS记录中错误的域名服务器域进行显式查询。为了验证这一点，我们对Tranco Top 1M（https://tranco-list.eu）中的所有二级域名相应的顶级域名服务器发起了对域名NS记录的查询，并观察应答中是否有附带的glue记录，结果如图表6所示。在总计2,507,896条NS记录中，共有1,394,604条（55.6%）没有对应的glue记录；进一步，按照域名与域名服务器顶级域和二级域是否相同进行划分，我们发现，即使域名和域名服务器在相同的顶级域，仍有56,401条（5.9%）的NS记录没有相应的glue记录，因而这部分NS记录也是易受bitsquatting攻击的。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibDOf2lCAWJbmgwJFozz9zwiaibZsaeO8kTFPtwaZAZiayKpFV0MnIIvFUMDkSFibPRaIIXCG5sVDzXSw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表6. Tranco Top 1M二级域名的NS记录有/无对应glue记录的数量

2. 对于typosquatting攻击，当DNS注册商同时也是域名托管服务商时（例如GoDaddy），通常会自动地为所注册的域名随机分配域名服务器，此时便不需要域名注册者手动输入配置NS记录，因而typosquatting攻击的条件也就不成立。然而，文章并未对域名注册者需要手动配置NS记录这一情况是否普遍进行详细论述。

3. 本文提出的缓解措施之一为加强DNSSEC部署，然而对于本文提出的攻击漏洞而言，DNSSEC仅能在域名与域名服务器顶级域相同的情况下起到防御作用。

### *原文链接*

*https://doi.org/10.1145/3133956.3133988*

---

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU404mXGBJyHLlibG1NK555Q9O0gshBicsAUGLEfxH8SIRickqZI5MbKnB8bM2h2cg47eEf717ltsyB8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

报名时间：11月1日-11月29日

竞赛时间：12月1日-12月10日

****DataCon2022大数据安全分析竞赛******报名地址：**

https://datacon.qianxin.com/datacon2022

QQ交流群：962067583

**欢迎大家进群交流**👇
![](https://mmbiz.qpic.cn/mmbiz_jpg/RicNZQMn3FU404mXGBJyHLlibG1NK555Q9tO9Zq9TEuBqicxT5fK5ib4xtPLibGpGOIaSQI6Q6Jx03fa63Hv8HAxA1A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)
注册报名、赛题答疑等问题可咨询管理员

**关注公众号****更多DataCon赛事信息和惊喜好礼等你拿👇**

**转发本文至朋友圈**

**喊你的小伙伴一起来抽奖**👇

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4RERTvR4nx6ppbJNtw8CaLibFcS0Yz0N67rpejhWXImHbQGicuyKJx6EPajBGLnmmEZLzT3ovq1dVA/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4hm1Q9ribADDO7RNGuhGoaK6TGiacLYicPyX2PZw0dic30n8cWY2cWJed3agEib9Re36dmOJhWvoCVvDw/0?wx_fmt=png)

DataCon大数据安全分析竞赛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4hm1Q9ribADDO7RNGuhGoaK6TGi...