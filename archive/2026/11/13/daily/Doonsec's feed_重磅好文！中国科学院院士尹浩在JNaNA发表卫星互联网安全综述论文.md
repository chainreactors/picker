---
title: 重磅好文！中国科学院院士尹浩在JNaNA发表卫星互联网安全综述论文
url: https://mp.weixin.qq.com/s/81ym9lFmYAbMv3pbExeoWg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:18:21.189124
---

# 重磅好文！中国科学院院士尹浩在JNaNA发表卫星互联网安全综述论文

# 重磅好文！中国科学院院士尹浩在JNaNA发表卫星互联网安全综述论文

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88VrFt6dibhtTopefOMibK3OYxMSKJLstwicW7kM8QXP7bLmpuvbGlnfn2AJ5BuPDcLwM4UOOIRUj8zYWU5uu6Bwe1qfSQJ3MWsH8k/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/wBNKsKdglKFibVkAPdDCwHnGFRb0VmJTpdq5LoPAbb452TTuVnkPapdk3YZ4koA3iatIW0M9FibM3LPjQ4yleOrLKRYZqyc60h0lkqmibSHg4Ak/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

近日，**中国科学院院士尹浩（Hao Yin）作为第一作者**在《Journal of Networking and Network Applications》（JNaNA）发表题为“A Survey on Satellite Internet Security: Challenges, Principles and Future Trends”的综述论文。

论文聚焦卫星互联网安全领域的重大挑战，提出涵盖物理实体、电磁信号、网络信息和系统服务的四空间安全分析框架，系统揭示跨空间攻击链及威胁传播机制，全面梳理十大关键安全防护技术，为构建体系化、智能化的卫星互联网安全防护体系提供重要参考。

**01**

**论文信息**—— ◆

**论文标题：**A Survey on Satellite Internet Security: Challenges, Principles and Future Trends

**作者：**Hao Yin, Yuanyu Zhang, Shuangrui Zhao, Zhiwei Zhang, Ji He, and Yulong Shen

**单位：**National Key Laboratory for Complex Systems Simulation; School of Computer Science and Technology, Xidian University; Shaanxi Key Laboratory of Network and System Security

**关键词：**Satellite Internet, Electromagnetic Security, RF Fingerprinting, Onboard Trusted Computing, Cross-Space Attack

**引用信息：**Hao Yin, Yuanyu Zhang, Shuangrui Zhao, Zhiwei Zhang, Ji He, and Yulong Shen (2026). A Survey on Satellite Internet Security: Challenges, Principles and Future Trends. Journal of Networking and Network Applications, Volume 6, Issue 3, pp. 144–166.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wBNKsKdglKEPc5eEMR6Rr0f0ys3uawYkrhCLfP9pHT0nC5jo94PibWfeqPfB5iaatQbc3zMYcj42R3teeo1fZej2VqfqoRrMToia7TJEHDCM2c/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

**02**

**导读**—— ◆

卫星互联网是实现全球泛在连接和未来6G通信的重要基础设施，其开放性、动态性及星地深度融合等特点带来了区别于传统地面网络的复杂安全威胁。随着低轨巨型星座、星间链路及星载智能计算技术的发展，卫星互联网安全已从单一通信链路防护演变为涉及物理、电磁、网络与服务的体系化安全问题。

针对现有研究缺乏统一安全分析框架、难以刻画跨空间威胁传播的问题，论文提出卫星互联网四空间安全分类体系，系统分析电磁信号欺骗、网络入侵、非法接入及星载系统攻击等威胁及其跨空间传播机制，揭示不同安全空间之间的相互依赖关系。

在此基础上，论文围绕空间态势感知、卫星信号真实性认证、非法终端检测、安全路由、弹性组网、星载可信计算等十大关键技术，系统总结现有研究进展与技术挑战，并提出星地一体化、跨空间协同与智能驱动的安全设计原则，为未来卫星互联网安全体系建设提供研究方向。

**03**

**背景介绍**—— ◆

近年来，以低轨卫星星座为代表的卫星互联网快速发展，逐步由传统通信中继系统向集通信、计算、存储和智能决策于一体的综合信息网络演进。卫星互联网能够为海洋、航空、偏远地区及应急场景提供广域通信服务，并通过与地面移动通信网络深度融合，成为未来空天地海一体化信息网络的重要组成部分。

与地面互联网相比，卫星互联网具有全球开放接入、无线信道暴露、卫星高速运动、网络拓扑动态变化及在轨维护困难等特点。一方面，开放的电磁环境使卫星通信链路易受到干扰、欺骗、重放及窃听攻击；另一方面，星地网络互联和星载软件定义能力的增强，进一步扩大了非法接入、路由劫持、控制系统入侵及恶意软件攻击的影响范围。

更为重要的是，卫星互联网的物理实体、电磁信号、网络协议和业务服务之间存在紧密耦合。攻击者可通过伪造卫星信号诱导终端错误接入，进而实施网络层攻击；也可通过入侵测控系统注入恶意指令，影响卫星姿态与轨道安全。因此，传统面向单一网络层次或特定攻击类型的安全防护方法，难以全面应对卫星互联网跨空间、多层次的复杂安全威胁。

论文从卫星互联网体系架构出发，构建统一的安全威胁分类体系，分析典型跨空间攻击链，并系统梳理关键防护技术，为卫星互联网安全研究提供综合性参考。

**04**

**主要内容**—— ◆

**1）卫星互联网四空间安全体系**

论文将卫星互联网安全划分为物理实体空间、电磁信号空间、网络信息空间和系统服务空间四个维度。

物理实体空间主要涉及卫星、地面站、用户终端及轨道资源，重点关注空间碎片碰撞、恶意机动和物理破坏等威胁；电磁信号空间涉及卫星通信、导航与测控信号，重点关注干扰、欺骗、重放及非法信号接入；网络信息空间涉及卫星接入协议、星间链路及网络路由，重点关注非法接入、网络入侵和路由攻击；系统服务空间涉及星载操作系统、数据存储、智能计算及业务应用，重点关注数据篡改、计算结果伪造和人工智能模型攻击。

四个空间在逻辑上具有不同的安全目标，但在实际运行中相互关联。论文通过统一的威胁对象、攻击类型和防护目标分类，为卫星互联网安全风险分析及防护技术设计建立系统化框架。

![](https://mmbiz.qpic.cn/mmbiz_png/wBNKsKdglKFJfnzv7Sdvp2nZZke2m1TcJL7TDT840n4UTV44iaK90jPDmrbeUa8TNoNtlruFtM8vLQgAh8bjB1aq15YETuicjhDica5aPOVMug/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

表1 卫星互联网四空间安全威胁分类

**2）跨空间攻击链与威胁传播**

针对卫星互联网中不同安全空间紧密耦合的特点，论文分析了攻击行为从一个空间向其他空间传播的典型机制，包括电磁信号到网络、网络到物理、网络到服务以及物理到网络等多种攻击路径。

例如，在电磁信号到网络的攻击链中，攻击者首先伪造卫星接入信号，诱导终端连接虚假卫星，随后通过丢弃、篡改或重定向接入请求，造成网络接入失败或信息泄露。在网络到物理的攻击链中，攻击者通过入侵卫星控制网络，注入恶意测控指令，进而干扰卫星姿态和轨道控制，产生物理安全风险。

论文进一步结合KA-SAT网络攻击、Starlink终端安全分析及GNSS欺骗等典型案例，说明卫星互联网攻击的初始入口与最终影响可能分属不同安全空间。由此，卫星互联网安全防护不仅需要识别单一攻击行为，还需要分析威胁在不同空间之间的传播路径及其级联影响。

![](https://mmbiz.qpic.cn/mmbiz_png/wBNKsKdglKG76uMMTYFIwzowA0ZyhMYEsJia8q91hCibf7YuubRb2nU6PLnn1WqgLkg7qDGVDGTyF8piayMyX6v12J9vxGKvh1IicFOCHdFLJ9o/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

表2 卫星互联网典型跨空间攻击链

**3）卫星互联网十大关键安全技术**

围绕卫星互联网安全防护需求，论文系统总结了十大关键技术，分别为：空间态势感知、基于射频指纹的卫星信号真实性认证、非法终端检测与定位、空间安全路由、大规模弹性网络构建、星载系统安全、星载可信存储与计算、卫星量子密钥分发、卫星互联网人工智能安全以及跨空间协同威胁感知与防御。

其中，空间态势感知通过目标检测、轨道预测和风险评估保障卫星物理安全；射频指纹认证利用卫星发射机硬件特征验证信号来源真实性，辅助识别卫星信号欺骗；非法终端检测与定位通过频谱感知、信号识别和多源定位技术发现未授权接入行为；安全路由与弹性组网通过可信路径选择、冗余拓扑及动态恢复机制保障网络连续运行。

同时，星载系统安全与可信计算重点保障卫星软硬件、数据存储及计算过程的安全性；卫星量子密钥分发为关键链路提供密钥建立手段；人工智能安全关注模型投毒、模型篡改及智能决策可靠性；跨空间协同威胁感知与防御则融合物理、电磁、网络与服务等多源安全信息，实现攻击链推理和协同响应。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wBNKsKdglKHr8mlA7nmpvoCFR2B2icWqSnQ7YqFXrVicGbG3rgE7P8PicZr2bmjqpnYF06mibELAG1v2DsAuSypXxXpticFkGp99ZjSFzgDeuDI8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

图1 卫星互联网十大关键安全技术

**4）安全设计原则与未来研究方向**

论文提出，未来卫星互联网安全体系应遵循星地一体化、跨空间协同和智能驱动三项设计原则。

星地一体化安全强调卫星、地面网关、用户终端及网络服务之间的端到端安全协同；跨空间协同安全强调物理态势、电磁异常、网络流量和系统运行信息的联合分析；智能驱动安全则利用人工智能提升威胁预测、自适应防御及安全决策能力，同时保障智能模型自身的可信性。

围绕十大关键防护技术，论文进一步讨论了从空间目标跟踪向任务影响预测、从传统密码身份认证向物理层信号真实性认证、从静态网络防护向动态拓扑感知安全路由，以及从分散安全告警向跨空间攻击链推理等未来研究方向，为卫星互联网体系化安全防护提供技术参考。

**05**

**评价与展望**—— ◆

该论文围绕卫星互联网面临的复杂安全挑战，从威胁分类、攻击机理、关键防护技术和安全体系设计等方面开展了系统性综述，主要工作集中在三个方面。

首先，论文提出覆盖物理实体、电磁信号、网络信息和系统服务的四空间安全分类体系，突破了传统安全研究侧重单一通信层次或攻击类型的局限，为卫星互联网安全威胁分析提供了更加完整的系统视角。

其次，论文系统分析跨空间攻击链及威胁传播机制，揭示电磁、网络、物理和服务安全之间的关联关系，为理解卫星互联网复杂攻击行为及设计协同防御机制提供了参考。

最后，论文梳理十大关键安全防护技术，并提出星地一体化、跨空间协同和智能驱动的安全设计原则，为未来卫星互联网安全技术研究与体系建设提供了方向。

论文同时指出，现有卫星互联网安全研究仍面临跨空间安全数据融合困难、真实攻击数据集和测试平台不足、星载资源受限以及智能安全决策可信性不足等挑战。未来需进一步加强跨空间威胁关联分析、轻量化可信认证、动态网络弹性防护及星载可信智能等方面的研究，推动卫星互联网安全由分散式防护向一体化协同防御发展。

转载自：NSSLab-Xidian

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88WycdWO1wNrGTfzXg2mJucs29pJ0CoZUNcGgO3196QCztkhiaSDH1ic7jyb6aem5iarRyoKKsUSzMC6VoqSK5A2pg5pQgd0da4POQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540726&idx=1&sn=b9402b72bbf0adc75cef49f7bbd0bd49&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540726&idx=1&sn=b9402b72bbf0adc75cef49f7bbd0bd49&scene=21#wechat_redirect)

****| 推荐阅读****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[重磅发布 | 行业首部《智能网联汽车内生安全白皮书》，智己LS9 Hyper全球首搭中国原创内生安全系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540505&idx=1&sn=db8e714a57b8bf3dad9268b996fb5a44&scene=21#wechat_redirect)

[邬江兴院士：构建内生安全质量检测体系，筑牢人类可控可信 AI 根基](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539044&idx=1&sn=1791fd1aad5f130fe5d87c46cc4b8687&scene=21#wechat_redirect)

[人工智能内生安全让“千里马”跑得快又跑得稳——邬江兴院士解读AI安全应对新思路](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540081&idx=1&sn=7abcebf943fbb1723bc747b626f90087&scene=21#wechat_redirect)

[中国工程院院士邬江兴：从“概率性”中构建“确定性”，以内生安全范式破解大模型安全困局](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540750&idx=1&sn=412b1fca972cda7fe628429d14ea6a7a&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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