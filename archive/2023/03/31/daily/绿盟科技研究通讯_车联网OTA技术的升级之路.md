---
title: 车联网OTA技术的升级之路
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247494924&idx=1&sn=7a104fb39b5fc60b2bd86585bcc74947&chksm=e84c4bd3df3bc2c5052ae878e593fc44f5c9b15d64b3f0ae58809216d712b7b9d49fae9964d5&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2023-03-31
fetch_date: 2025-10-04T11:15:35.911262
---

# 车联网OTA技术的升级之路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNISGFSiaDQibS4KaEohBnLvvl7IzibxibsdQfY8I7pVTa1oxpKcn4zhePQZnQ/0?wx_fmt=jpeg)

# 车联网OTA技术的升级之路

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNISXrMzF90K9OLsHzjMBrhMMZLpiaOzdve4OqqJxpS52N9OL9yZUppoebw/640?wx_fmt=gif)

一.  简介

OTA（Over-The-Air）空中下载是指通过移动通信的空中接口实现对系统和应用程序的远程管理[1]，它并不是一项全新的技术，在互联网世界早已存在多年，广泛应用于智能手机系统固件升级。而随着近些年车联网逐步发展成熟，汽车行业进入软件定义时代，OTA技术正广泛应用于汽车产业。

汽车厂商通过OTA技术可以将更新的软件、固件、配置等程序文件从云端传输到车辆中心网关，然后再通过汽车内部网络对车辆的电子控制单元（ECU）进行升级、修复和优化，基于OTA的汽车软件更新方式如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNISyH7bdUGOuI7ib4vlicVUzHOpqkM0zUsG74mD1kUm1Q9G45G0VOLGvg7Q/640?wx_fmt=png)

图1 基于OTA的汽车软件更新方式

相比于传统人工升级的方式，OTA技术具有更快速、更方便、更精准的优势，但由于涉及车辆控制系统和用户的隐私信息，若不加强系统安全防护和数据隐私保护，极易引发各类安全事件，给用户造成财产损失和人身威胁。接下来本文首先为大家简要介绍车联网中OTA技术的系统架构，然后探讨汽车在OTA升级过程中面临的安全挑战，最后给出OTA在车联网环境中的典型应用。

二.  OTA系统架构

OTA系统整体架构包含OTA云端、OTA车端、OTA升级对象三部分，如下图2所示。其中OTA云端为OEM(Original Equipment Manufacturer)专属云服务器平台，OTA车端通常指T-box(Telematics Box)，OTA升级对象包括操作系统、车机应用和各类嵌入式ECU(Electronic Control Unit)[2]。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNIStTeMo74k2ic3VqH0AZlxd9XD1UXxLeXoKnia5M16hiciaty5wzIzmvT3Yg/640?wx_fmt=png)

图2 OTA系统架构

2.1

OTA云端

OTA云端作为OTA系统的核心组成部分，主要负责汽车状态数据收集、升级策略制定、升级服务管理以及用户安全认证，包括了OTA管理平台、OTA升级服务、任务管理和文件服务这四部分，功能结构如图3所示。其中，OTA管理平台负责软件版本、升级计划的管理，根据升级策略和设备信息生成相应升级包；OTA升级服务通过网关接入设备，负责车端的更新检查、升级通知并对升级全程监控，同时辅之安全认证、数据加密、数字签名等技术手段，确保OTA数据传输过程的安全性；任务管理负责云端任务的发布、调度、处理等情形；文件服务则负责OTA升级包的存储下载。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNIS7NUca2yOUtHicRnC1fuiaib3ejz0IwZvQ1nXVHQy1amZR5ictkiaaVaDqvA/640?wx_fmt=png)

图3 OTA云端功能结构

2.2

OTA车端

OTA车端采用T-box接收云端通过4G/5G网络传输的更新固件，按功能可分为OTA引擎和升级适配器两部分，结构如图4所示。其中，OTA引擎是连接OTA云端与车端的桥梁，负责云端到车端的安全通信链路，通信SDK组件可以实现固件版本检查、升级包下载、升级包解密、签名验证，对整个升级过程进行监控并提示通知；升级适配器作为硬件设备，可以为车辆OTA升级提供稳定性支持，保证升级过程中数据的安全刷写。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNIStZZ1xh3I7tfdd3pGtzuf7CX5bBWsvKkQq4m4dibe6ibB2p2cUEzvf7NA/640?wx_fmt=png)

图4 OTA车端功能结构

2.3

OTA升级对象

汽车OTA根据升级对象不同，可分为SOTA(Software Over The Air)和FOTA(Firmware Over The Air)两种[3]。SOTA通常是指车载软件的远程升级，包括地图导航、语音识别、智能驾驶等应用软件，主要增强汽车的功能和用户体验；而FOTA是指固件远程升级，或者说系统远程升级，主要针对车辆的硬件进行升级，侧重于提升汽车的性能及安全性，区别如图5所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNISfN4UFrxib2k9PYIJHTrjIIaSibRSIUGk6vXMNI5jJFpEIychiaoPsStmg/640?wx_fmt=png)

图5 SOTA与FOTA区别

从技术角度来说，因为与互联网终端设备中应用软件升级方式较为相似，所以SOTA更容易实现，也已在汽车行业广泛应用，而FOTA则更考验车企在技术上的积累和硬件上的设计，相比于SOTA升级过程更复杂，安全性能要求也更高；从服务角度来说，在软件定义汽车时代，通过OTA升级为用户提供软件服务也将为车企提供新的创收渠道，是大势所趋。

三.  OTA升级面临的安全挑战

汽车OTA凭借其快速迭代的特性缩短汽车上市周期，提升用户产品体验，降低售后运维成本，带来了全新的商业模式，但在实际升级过程中，仍面临着很多的安全挑战，许多安全问题需要被关注和解决，特别是从汽车隐私保护、安全认证、稳定可靠三个角度来看[4]。

3.1

隐私保护

智能汽车上通常配备了大量传感器，采集到的数据在OTA升级过程中存在泄露风险，因此，对于OTA升级过程中可能存在的隐私安全问题，汽车制造商需要从多个方面采取措施保护隐私数据的安全性。一方面，可以采用加密技术对敏感数据进行加密，以防止黑客通过攻击直接获取隐私数据；另一方面，建立完善的权限控制机制，只有经过授权的人员或设备才能访问和处理相应隐私数据；此外，还可使用脱敏、匿名化等技术手段保护用户个人隐私，确保传输和存储数据的安全。

3.2

安全认证

认证作为OTA升级过程中不可或缺的一部分，涉及到许多敏感操作，如身份信息的验证和授权，重要数据的传输和存储等，为确保远程升级过程的安全性，需要采取相应的安全策略，如访问控制、权限管理、双向认证等，除此之外，在升级过程中，还要验证数据的完整性和真实性，避免中间人攻击所带来的风险。因此，制定完善的身份认证方案，加强操作权限的管理，平衡安全和性能间的关系，是保障OTA升级过程安全的关键。

3.3

稳定可靠

通过前文OTA架构描述可知，车端OTA的实现是从TBox经网关，再通过总线通讯（CAN或以太网）将固件刷写到车内嵌入式设备ECU，涉及网络环境和众多零部件，所以在进行OTA升级时，必须要考虑整车的稳定性，否则一旦升级失败，汽车秒“变砖”。因此，为保障远程升级过程的稳定可靠，事先需要进行充分测试以保证固件兼容性，采取双备份保护机制以确保系统连续性，制定应急方案以针对升级过程中出现的紧急情况。

四.  OTA应用场景

随着汽车产业的数字化转型和智能化升级，汽车电子成本占整车成本比重不断上升，汽车软件复杂度也随之提升，软件故障修复及个性化定制需求促使越来越多的车企和互联网公司开始重视OTA技术的研发和应用。特斯拉作为最早大规模应用OTA技术的车企之一，通过该技术让车辆更高效地管理新增功能、修复缺陷以及提升性能，成功拓宽了“服务”和“运营”范畴，增加车辆的附加价值。本小节将结合实际案例，从漏洞修复、更新升级两个方面说明汽车OTA的典型应用场景。

4.1

漏洞修复

漏洞和安全隐患的存在，极易导致车辆遭遇黑客攻击或远程控制，从而为用户带来严重的安全风险，通过OTA及时检测、排查、并推送漏洞补丁到所有需要修复的车辆上，不仅方便用户，还大幅节省了车企的召回成本。2021年Pwn2Own比赛中，攻击者凭借特别构建的Wi-Fi网络来欺骗特斯拉Web浏览器，然后通过执行恶意代码成功获取了汽车控制权，不久后，特斯拉就通过OTA技术，向受该漏洞影响的车辆推送了修复程序，消除汽车潜在的安全风险。根据美国国家公路交通安全管理局（NHTSA）的数据显示，仅2022年，特斯拉在美国就通过OTA开展了19次召回活动，覆盖超过377万辆汽车[5]，详细事件如图6所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZbpGRZUHCS8zSkwRGuPNISeksfjWQyORePVFmxOYuV1DzMznEo8pHpXklbBAsQpDicTbkJpLfebRA/640?wx_fmt=png)

图6 2022年特斯拉汽车召回事件

4.2

更新升级

除漏洞修复外，汽车通过OTA技术还可以实现固件远程升级、在线更新、集中管理等功能，显著提升汽车的智能化程度，实现车辆与驾驶者之间的无缝互动。特斯拉最早将OTA升级应用到固件更新上，通过硬件预埋交付，每当一项新功能或性能增强推出，车主不需要到店升级换新，只需通过OTA即可将车辆升级为最新版本，体验汽车的全新特性。此外，OTA技术还支持汽车像手机一样进行数据更新，实时获取卫星导航数据，并根据当前交通信息自主规划最优路径，提供更加精准、高效的导航服务，提升用户出行体验。

五.  小结

在本篇文章中，我们详细介绍了远程升级(OTA)技术的系统架构、安全挑战及应用场景。作为智能网联汽车的重要标识，OTA赋予了汽车全新的生命力，使得软件定义汽车成为行业共识，为智能汽车产业的发展注入新的机遇和活力。

据市场研究机构预测，未来几年，全球汽车OTA市场规模将持续快速增长，而这也将对汽车企业和IT企业提出更高的技术挑战和安全防护要求，因此需要不断增强技术研究和安全管理，以确保OTA技术的健康发展和应用。

参考文献

1. https://zh.wikipedia.org/wiki/OTA

2. 智能网联汽车的OTA升级方案，https://xueshu.baidu.com/user-center/paper/show?paperid=1f2108h0ac460xj086630r70dk172775

3. https://baike.pcauto.com.cn/58561.html

4. 智能网联汽车OTA升级安全设计，https://xueshu.baidu.com/user-center/paper/show?paperid=154h0g30x96h0tw0f55r0ag0ek048308

5. https://baijiahao.baidu.com/s?id=1752069238401796790&wfr=spider&for=pc

内容编辑：创新研究院 李智科

责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUbrbTJxY0Qv9BtgtXZsYVvaVUtlPicCUV6qDBGgZnrxicAMwvibG73JUu0w1UweTicfkuTRIyJyt77C5Q/640.jpeg?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2)

**长按上方二维码，即可关注我**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

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