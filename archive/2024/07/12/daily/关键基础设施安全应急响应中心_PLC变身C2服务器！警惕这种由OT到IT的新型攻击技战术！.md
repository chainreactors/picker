---
title: PLC变身C2服务器！警惕这种由OT到IT的新型攻击技战术！
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544845&idx=1&sn=a85c8ff8642d832819acd1120ab40217&chksm=c1e9bc5cf69e354aa073472937f5409e801919f3dc42680ce19fa8e47d1a434b1a28fc5984b8&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-12
fetch_date: 2025-10-06T17:44:27.165923
---

# PLC变身C2服务器！警惕这种由OT到IT的新型攻击技战术！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguFvapmvBic12Mt3vFN1eOj9eHOgT0X8tWtxv7EuCESh0tibqYyR9AcYYE8pG71X5TmNqJlSiadX2DcQ/0?wx_fmt=jpeg)

# PLC变身C2服务器！警惕这种由OT到IT的新型攻击技战术！

关键基础设施安全应急响应中心

**编者按**

2024年7月8日，俄罗斯网络安全公司Solar旗下的4RAYS网络威胁研究中心发布研究报告，揭露了名为"Lifting Zmiy"的亲乌克兰黑客组织对俄罗斯政府和私营公司的一系列网络攻击。通过对2023年9月至2024年6月间4起典型案例的追踪分析，4RAYS网络威胁研究中心判定该黑客组织入侵了俄罗斯工业自动化企业Tekon-Avtomatika的PLC设备，并在其上部署了控制与通信（C2）服务器，这些控制器不仅用于工业自动化，还控制电梯等关键设备。4RAYS的专家通过特定模式扫描互联网，发现了被Lifting Zmiy黑客入侵的更多控制器。受害者来自IT、电信和公共部门等多个行业，Linux和Windows系统均未能幸免。4RAYS专家以很高置信度认为Lifting Zmiy源自东欧，目前仍然活跃。值得注意的是，攻击者在行动中还使用了SpaceX星链服务的基础设施，这表明他们具有高度的技术能力和资源。4RAYS建议受影响的组织加强网络安全措施，包括审查口令策略、引入双因素认证，并定期进行IT基础设施的安全评估，以防范此类攻击。由于该黑客组织的初始突破与控制针对的是Tekon-Avtomatika的PLC设备，这事实上构成了由OT到IT的攻击链，这种攻击手法的成功应当引起工业网络安全行业的高度警惕。因为传统上大家都认为OT网络攻击都是因IT系统暴露面和弱点而引发，而本次事件中攻击者首先直接突破并控制了PLC并使其变为C2服务器，进而开展更进一步的甚至其它目标的攻击活动，在对抗性、隐蔽性、潜伏性方面均树立了标杆，实属罕见。

![](https://mmbiz.qpic.cn/mmbiz_png/ll2PVky3MmbibjXB0ibFavgNdMQPORxNV4gqGaX5wj085wVOWP0Ub4nVIibSq8w9JPhYaicfsBwicVVmHUYlG2QWX4w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**Lifting Zmiy攻击俄罗斯事件概述**

**攻击事件概述**

Lifting Zmiy黑客组织自2023年10月以来对俄罗斯的政府机构和私营公司发起了一系列网络攻击。该组织利用开源工具，特别是对Linux系统有深入的了解和操作能力，通过入侵Tekon-Avtomatika PLC设备，这些设备是SCADA系统的一部分，也用于控制电梯等设备，进而部署了控制服务器。Solar 4RAYS团队在调查中发现，攻击者使用了开源反向SSH软件，并在互联网上发现了该组织使用的一系列被黑客入侵的控制器。

Lifting Zmiy的攻击不限于特定行业，受害者包括IT、电信和公共部门的组织，Linux和Windows系统均受到波及。特别值得注意的是，攻击者使用了SpaceX的Starlink基础设施来进行攻击。4RAYS团队通过对网络指标的监控，发现了更多的恶意软件样本和攻击者使用Starlink基础设施的痕迹。

尽管Lifting Zmiy使用了公开可用的工具，但他们对Linux操作系统的高级知识使他们能够有效地隐藏恶意软件，并通过暴力破解口令的方式入侵基础设施。从最初的入侵到积极行动，该组织表现出了耐心，有时这一过程会持续数月，暗示他们可能从第三方获取了受损凭证。4RAYS团队通过内部狩猎系统不断发现Lifting Zmiy组织网络攻击基础设施的新元素，包括SpaceX公司星链资源的使用。

![](https://mmbiz.qpic.cn/mmbiz_png/ll2PVky3MmbibjXB0ibFavgNdMQPORxNV4HibOia9XibiaxzKpQHcJzMrnZej5ZOTgvexvFRu9vUUIQPC2xsCWb4dicVg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Lifting Zmiy网络攻击基础设施中典型工具、技术和对象

**主要攻击工具**

Lifting Zmiy组织在攻击过程中使用了多种工具，体现了技术多样性和复杂性，这些工具包括使用开源工具、定制恶意软件、口令破解和各种系统后门。

1.Reverse SSH: 开源恶意软件，用于创建反向shell和命令服务器，是Lifting Zmiy的标志之一。

2.SSH-IT: 软件，用于拦截SSH会话中用户输入的命令。

3.mig-logcleaner: 开源工具，用于清理Linux操作系统日志。

4.ProxyLogon: 漏洞利用，用于攻击Exchange服务器。

5.Shadowpad: 恶意软件，与Blackfly/Grayfly组织相关。

6.SSHD后门: 修改后的sshd文件和libprivatessh.so.5库，用于创建后门sshd服务。

7.gs-netcat: 实用程序，用于创建隧道并绕过防火墙限制。

8.ssh-snake: 蠕虫工具，使用受感染计算机的SSH密钥进一步发展。

9.kerbrute: 实用程序，用于搜索Active Directory中使用Kerberos协议进行身份验证的账户。

10.Responder: 实用程序，用于进行中间人攻击，支持Windows中的多种身份验证方法。

11.proxychains3: 软件，用于代理流量。

12.rackmapexec: 工具集，用于对Windows/AD基础设施进行一系列攻击。

Empire-agent: Empire框架的代理，为后期利用提供了一套广泛的工具。

**主要攻击对象**

Lifting Zmiy黑客组织针对的主要攻击对象是Tekon-Avtomatika公司生产的KUN-IP8控制器（КУН-IP8），这些控制器被广泛应用于自动控制和调度系统，包括电梯设计。研究发现，这些设备运行在Linux内核上的通用固件，并具备编写自定义LUA插件的能力，为攻击者提供了丰富的利用机会。

![](https://mmbiz.qpic.cn/mmbiz_png/ll2PVky3MmbibjXB0ibFavgNdMQPORxNV4U2lUOyJ2uvCryEIreENickH1ibhusS1UR0jC2Hp0IkgxkxpnJ6nZV3Sg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

КУН-IP8

安全专家Jose Bertin在2022年3月的研究表明，存在大量使用默认管理员凭据的设备，这些凭据甚至曾被发布在Tekon-Avtomatika的官方网站上。尽管公司随后删除了这些凭证，但许多设备在初始设置后并未更改默认凭据，留下了安全隐患。LUA插件能够以root权限运行，这可能导致具有超级用户权限的任意bash命令执行，构成严重的安全漏洞。

Lifting Zmiy组织利用了这些公开的安全缺陷信息，通过系统漏洞在KUN-IP8控制器上部署了C2服务器，用于进一步攻击其主要目标。这些攻击不仅展示了攻击者对Linux系统的深入了解，还凸显了设备管理员在数字卫生方面的责任，例如更改默认凭据，以提高安全性，防止未授权访问。

**Lifting Zmiy黑客攻击的威胁是什么？**

Lifting Zmiy黑客并没有对电梯系统本身实施损害，而仅仅是藏身于其控制系统中。这不仅对OT网络安全敲响了警钟，而且警示网络安全工作者，OT安全与IT安全的融合，哪一侧都不能忽视，任何一侧的暴露都可能对另一侧的安危带来巨大风险。

1、试图感染控制器软件

安全专家中心Positive Technologies网络威胁研究部门负责人Denis Kuvshinov指出，该公司还看到了该组织的活动，黑客想要危害SCADA系统软件开发商，试图感染该软件并将其交付给客户。幸运的是，攻击者的尝试失败了——制造商及时发现了问题。

2、多种手段增强攻击活动的隐蔽性

攻击者使用反向SSH工具作为其标志性的恶意软件，创建反向shell连接，实现对受感染系统的隐蔽远程控制。这种工具使得攻击者能够在不引起注意的情况下长期潜伏在受害者的网络中，同时在攻击过程中，一旦建立了控制，攻击者会移除shell，增加了检测的难度。Lifting Zmiy通过侵入合法系统，如Tekon-Avtomatika的SCADA控制器，来隐藏自己的行动。这些控制器是设计用于电梯等自动化过程控制系统的，攻击者利用这些系统的合法性和复杂性作为掩护，使得其恶意活动更难以被追踪和识别。使用星链（Starlink）基础设施：攻击者利用SpaceX的Starlink卫星互联网服务的IP地址进行攻击，这种使用主流且广泛分布的卫星网络服务的做法，为攻击者提供了额外的匿名性和隐蔽性。

3、为电梯控制系统的安全敲响了警钟

尽管Lifting Zmiy黑客组织的主要攻击目标不是电梯本身，但这一事件暴露了电梯控制系统的潜在安全风险。Innostage SOC CyberART的网络威胁中心负责人马克西姆·阿基莫夫强调，电梯控制系统由于连接到互联网或其他数据网络，可能因软件和电子组件的漏洞而容易受到黑客攻击。这种风险不仅局限于新型电梯，因为即使是旧电梯，也可能通过安装额外的控制器来实现远程控制，从而增加了数字风险。Stingray Technologies的总经理尤里·沙巴林提醒，不必要的互联网连接为攻击者提供了攻击媒介，强调了限制设备联网的重要性。因此，加强电梯系统的网络安全监控、定期软件更新和对承包商的审查变得至关重要，以确保电梯运行的安全性和可靠性。

**Lifting Zmiy黑客的攻击手法有何不同？**

Lifting Zmiy黑客颠覆了业界对传统OT网络攻击的典型手法，其“项庄舞剑、意在沛公”的战术得益于其技术、资源、能力的融合，从突破并控制PLC开始，拓展其攻击其它IT目标的意图。

1、暴力破解与购买结合，获取初始访问权限

在Solar公司调查的案例中，基础设施只是通过暴力破解口令而被黑客入侵。但很难说Lifting Zmiy是独立积累了对各个组织的访问权限，还是从通过出售受损凭证进行交易的攻击者那里购买了这些访问权限。但在所有情况下，从最初妥协的那一刻到开始的主动攻击行动都经过了很多时间（有时是几个月）。这可能表明该组织仍然从第三方获得了一些访问凭证。

2、变PLC为C2服务器，规避检测长期潜伏

Tekon-Avtomatika PLC设备运行Linux系统，具有一个模块，允许加载和执行自定义的LUA脚本插件。这种设计提供了极大的灵活性，但也带来了安全风险。由于LUA插件能够以root权限运行，它们能够执行任何bash命令，这为攻击者将PLC变身C2创造了条件。研究人员分析发现反向SSH样本后，他们提取了相应的C2地址，该地址指向受感染的 Tekon-Avtomatika PLC。使用发现的模式，研究者又在受感染的设备上发现了更多命令和控制服务器。此外，通过被动扫描，还发现了一个与反向SSH管理服务器配置类似的基础设施。经验证，它们不再放置在Tekon-Automation设备上 。研究者总共发现了23个C2服务器，其中16个是Tekon-Avtomatika PLC。截至2024年6月，23个C2中仍有14个处于活跃状态，这些活跃的C2中有8台部署在受感染的PLC上。

3、攻击基础设施使用了SpaceX的卫星互联网资源

研究人员检测到的IP地址的Whois记录显示，这些IP属于提供商Starlink Services, LLC，该公司是SpaceX的一个部门，在全球范围内提供宽带卫星互联网服务。Lifting Zmiy黑客组织通过利用SpaceX的Starlink基础设施，实现了在全球范围内的匿名和灵活攻击，受益于其动态IP地址和高速连接，同时规避了传统网络安全措施基于IP地址所归属的物理位置的检测分析，确保了行动的隐蔽性和高效率。这种对先进卫星网络服务的利用，为黑客提供了一个难以追踪和监控的攻击平台，大大增加了网络安全防护的挑战。

**Lifting Zmiy组织初步画像**

综合Solar公司的报告，大致可以对Lift Zmiy黑客组织有一个初步的认识。该组织是一个亲乌克兰的黑客组织，主要针对俄罗斯政府机构和私营公司进行网络攻击。该组织以软件控制SCADA系统的设备，尤其是用于控制电梯的设备。在某些情况下，他们使用Starlink的IP地址与受系统连接，表明这些攻击可能源自乌克兰。

Lifting Zmiy的攻击模式通常通过口令猜测进行初始渗透，然后在系统中扎根，利用反向SSH、SSH后门和GSocket等开源工具管理受感染系统并传递恶意文件。4RAYS网络威胁研究中心的专家在调查过程中发现了十多台受感染的PLC设备，这些设备的在俄罗斯制造的电梯控制和调度设备上使用。

Lifting Zmiy的主要目标窃取数据，并在某些情况下是破坏受害者的资料。专家们在调查过程中还发现，该组织的恶意活动从初始入侵到主动行动占用数月时间，在此期间可能不会有明显的恶意活动痕迹。

**小结及建议**

早在2022年，关于“Tekon-Automatika”控制器的漏洞利用方法已被公开，尽管该公司随后采取了措施移除默认登录信息，但黑客仍成功入侵，表明部分用户未更新安全设置或黑客通过暴力破解获取了新口令。针对这种由OT系统攻击控制，进而实施向更多IT系统的攻击手法，安帝科技建议用户遵循基本的最佳OT安全实践显得更加必要且紧迫。

1、强化口令安全：确保所有系统使用强口令，并实施定期更换口令的政策，避免使用默认或通用口令。

2、启用双因素认证：在关键系统上实施双因素认证，以增加额外的安全层，确保即使口令被破解，攻击者也无法轻易获得访问权限。

3、及时更新与打补丁：定期检查并更新系统软件，及时应用安全补丁，以修复可能被利用的已知漏洞。

4、网络隔离与监控：对关键基础设施实施网络隔离，并部署入侵检测系统，以监控和防范未授权的访问或可疑行为。

5、安全意识教育：对员工进行网络安全培训，提高他们对钓鱼攻击、恶意软件和其他网络威胁的认识，减少人为安全风险。

附：

Tekon-Avtomatika公司简介

Tekon-Avtomatika俄罗斯领先的调度系统产品制造商，自1992年成立以来，已成为该领域市场份额最大的企业。公司专注于生产工程设备控制器、工业远程控制器及相关集线器，以及智慧楼宇的软硬件解决方案。其旗舰产品"工程设备控制器"（Контроллер инженерного оборудования，简称KIO）系列，包括KIO、KIO-1M、KIO-2M，KIR、KUN、KUP等型号以及为满足不同行业需求而衍生的KIO-2MD、KIO-2MS、KIO-2MRS等版本。2022年4月，安全研究人员发现这些控制器存在因默认口令导致的安全缺陷，可能被黑客利用进行远程控制，引发对工业控制系统安全性的广泛关注。

**参考资源：**

1.https://rt-solar.ru/solar-4rays/blog/4506/

2.https://rt-solar.ru/events/news/4509/

3.https://www.rbc.ru/technology\_and\_media/08/07/2024/6687f9af9a7947780a5d1a31

4.http://wiki.tekon.ru/index.php?title=%D0%9A%D0%A3%D0%9D-IP8#.D0.9D.D0.90.D0.97.D0.9D.D0.90.D0.A7.D0.95.D0.9D.D0.98.D0.95

5.https://www.it-world.ru/security/217782.html

原文来源：安帝Andisec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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