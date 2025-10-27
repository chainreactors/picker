---
title: ​以个人用户为目标的Magniber勒索软件攻击激增；黑客通过窃听HDMI电缆来窃取密码 | 牛­览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651131417&idx=2&sn=42a93b344989eae5a30117599bc28f5b&chksm=bd15beca8a6237dc224e2b5d28ef17c06f6f170c8d60e1f6467cdcd8178f2ef7b655312194e9&scene=58&subscene=0#rd
source: 安全牛
date: 2024-08-08
fetch_date: 2025-10-06T18:05:16.239295
---

# ​以个人用户为目标的Magniber勒索软件攻击激增；黑客通过窃听HDMI电缆来窃取密码 | 牛­览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDm5qGM6lHagDTA7BicY2tOIpFcAcic3B8Ad448DfXMEYGeHd3iaxVicvhZj0lCLvrWu75DdSQiaZ5fgLQ/0?wx_fmt=jpeg)

# ​以个人用户为目标的Magniber勒索软件攻击激增；黑客通过窃听HDMI电缆来窃取密码 | 牛­览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•知名电子制造服务商Keytronic因勒索攻击损失超1.2亿元

•以个人用户为目标的Magniber勒索软件攻击激增

•新发现的LianSpy恶意软件通过阻止Android安全功能来藏身

•黑客组织利用VPN更新漏洞部署恶意软件

•Windows壁纸处理机制缺陷可能让攻击者用来全面控制计算机

•黑客通过窃听HDMI电缆来窃取密码

•Apache OFBiz上发现一个严重的预验证远程代码执行（RCE）安全缺陷

•Google Ads重大报告故障或泄露竞争对手数据

•微软正式将安全工作和员工绩效挂钩

•ISACA发布系列AI学习资源

**热点观察**

**知名电子制造服务商Keytronic因勒索攻击损失超1.2亿元**

近日，知名电子制造服务提供商Keytronic在提交给美国证券会的一份报告显示，由于5月份的勒索软件攻击，该公司遭受了超过1700万美元（约合人民币1.2亿元）的经济损失。

文件显示，他们在5月6日发现了攻击事件，墨西哥和美国的站点发生故障，影响了支持机器人操作和企业功能的业务应用程序；由于这一事件，公司产生了约230万美元的额外费用，并推测在第四季度损失了约1500万美元的收入。此前Keytronic在5月的一份文件中披露，攻击迫使其关闭美国国内和墨西哥的运营两周时间。该公司还确认，在入侵期间，攻击者从其系统中窃取了个人信息。

Black Basta勒索软件团伙在5月下旬声称对此负责，并表示他们通过此次入侵得以窃取大量数据，包括人力资源、财务、工程和公司文件。在其暗网泄露网站上，Black Basta泄露了员工护照和社会保障卡、客户演示文稿和公司文件的截图。

原文链接：

https://www.bleepingcomputer.com/news/security/keytronic-reports-losses-of-over-17-million-after-ransomware-attack/

**网络攻击**

**以个人用户为目标的Magniber勒索软件攻击激增**

日前，研究人员发现，以个人用户的目标的Magniber勒索软件攻击激增，对家庭用户的设备进行加密，并索要数千美元的赎金以换取解密工具。

Magniber于2017年作为Cerber勒索软件的继任者浮出水面，当时它通过Magnitude漏洞利用工具包分发。此后，攻击者利用各种方法分发Magniber和加密设备。这些策略包括利用Windows零日漏洞、虚假的Windows和浏览器更新、植入木马的软件破解和密钥生成器。

与大型勒索软件攻击不同，Magniber主要针对下载恶意软件，并在家庭或小型企业系统上执行的个人用户。2018年，AhnLab发布了Magniber勒索软件的解密工具，但后来威胁行为者进行了修复，该工具不再有效。

一些受害者表示，他们的设备在运行软件破解或密钥生成器后被加密。一旦启动，勒索软件会对设备上的文件进行加密，并在加密文件名后附加一个随机的5-9个字符的扩展名，如.oaxysw或.oymtk。勒索软件还会创建一个名为READ\_ME.htm的勒索信，附有个人文件方面的信息，以及攻击者的Tor勒索网站的唯一URL。

原文链接：

https://www.bleepingcomputer.com/news/security/surge-in-magniber-ransomware-attacks-impact-home-users-worldwide/

**新发现的LianSpy恶意软件通过阻止Android安全功能来藏身**

日前，研究人员发现新发现了一个名为 “LianSpy”的安卓恶意软件，攻击者通过该恶意软件获取设备的root权限来开展一系列恶意活动，如抓取屏幕截图、窃取文件和收集通话记录。自2021年7月以来，LianSpy一直在觊觎安卓用户，在手机上冒充支付宝应用或系统服务以逃避检测，强大的隐身能力使其在三年多的时间里未被察觉。

卡巴斯基的研究人员认为，攻击者利用零日漏洞或使用物理访问权让设备感染上恶意软件。LianSpy使用经过修改后的su二进制文件来获取Root访问权限。恶意软件样本试图在默认的su目录中找到mu二进制文件，旨在逃避Root检测。研究人员认为，通过对修改后的二进制文件的强烈依赖来获取超级用户权限，表明这种间谍软件很可能是通过先前未知的漏洞或物理设备访问途径来分发。其一系列的规避功能包括绕过安卓12及更高版本的“隐私指示器”安全功能，该功能在应用程序录制屏幕，或启用摄像头或麦克风时在状态栏上显示指示器。

一旦启动，LianSpy会请求屏幕叠加、通知、联系人、通话记录和后台活动等权限。如果LianSpy以系统应用的身份运行，它会自动获得这些权限，而无需用户的明确许可。

原文链接：

https://www.bleepingcomputer.com/news/security/new-lianspy-malware-hides-by-blocking-android-security-feature/

**黑客组织利用VPN更新漏洞部署恶意软件**

日前，韩国国家网络安全中心（NCSC）警告称，黑客组织通过VPN软件更新中的漏洞部署恶意软件，并侵入网络企图窃取商业机密。

在一起攻击活动中，黑客组织Andariel利用了VPN软件通信协议中的漏洞，推送了伪装成软件更新的DoraRAT恶意软件。也就是说，他们把更新文件换成恶意软件，向建筑和机械公司分发DoraRAT远程控制恶意软件。韩国国家网络安全中心解释，这个漏洞允许威胁行动者伪装数据包发送到用户的个人电脑，被误认为是合法的服务器更新，从而允许安装恶意版本。

据悉，DoraRAT是一种轻量级远程访问木马（RAT），具有最小的功能，使其能够更隐秘地运行。在这次特定攻击中观察到的变种被配置用于窃取大文件，例如机械和设备设计文件，并将它们传输到攻击者的命令和控制服务器。

原文链接：

https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-vpn-update-flaw-to-install-malware/

**漏洞预警**

**Windows壁纸处理机制缺陷可能让攻击者用来全面控制计算机**

日前，研究人员发现Windows壁纸处理机制存在一个严重的安全漏洞。该安全缺陷可能让攻击者在受影响的机器上获得系统级权限。安全研究员Andrea Pierini披露的这个缺陷编号为CVE-2024-38100，并被命名为“FakePotato”。

FakePotato利用了Windows处理壁纸文件方面的一个缺陷。如果攻击者对系统拥有有限的访问权，就可以通过操纵特制壁纸图像的某些属性，将权限提升到系统账户的级别，从而完全控制该计算机，未经授权访问用户的敏感信息，并使用获得的凭据在网络中横向移动。

这个安全漏洞影响了多个Windows Server版本，包括：Windows Server 2016、Windows Server 2019、Windows Server 2022、Windows Server 2022 23H2。据悉，微软已在安全更新KB5040434中修复了此漏洞，安全研究人员建议用户和系统管理员尽快应用此补丁以减轻利用风险。

原文链接：

https://cybersecuritynews.com/leaked-wallpaper-exploit/

**黑客通过窃听HDMI电缆来窃取密码**

日前，安全研究人员发现了黑客通过窃听HDMI电缆来窃取密码等敏感信息。乌拉圭共和国大学的研究人员介绍，这种技术利用人工智能来解码HDMI连接的电磁辐射，并在计算机屏幕上重建显示的内容。

研究人员可以使用现成的软件定义无线电设备捕获HDMI电缆发出的电磁辐射信号。如果运用深度学习算法分析这些捕获的信号，他们可以从计算机显示器上重建文本和图像，准确率高达70%。

虽然老式的CRT显示器也存在类似的缺陷，但现代HDMI连接使用的复杂数字信号使得此类攻击变得不再可行。这项新研究表明，人工智能可以克服这些障碍，可能将数百万计算机用户置于险境。研究人员认为，执行此类攻击需要大量的技术专长和专门的设备，普通家庭用户不太可能成为攻击目标，但是政府机构或企业用户可能面临此类风险。

原文链接：

https://cybersecuritynews.com/hdmi-cables-steal-passwords/

**Apache OFBiz上发现一个严重的预验证远程代码执行（RCE）安全缺陷**

日前，研究人员发现Apache OFBiz上存在一个严重的预验证远程代码执行（RCE）安全缺陷。该缺陷可能被攻击者用来窃取组织数据，并通过横向移动到其他应用程序和网络带来更多威胁。该缺陷编号为CVE-2024-38856，CVSS得分高达9.8分。

Apache OFBiz是一个开源ERP系统，用户实现组织的集中式管理和自动胡，享有访问各种业务流程的高度权限，这些业务流程包括会计、人力资源、客户关系管理、订单管理、生产制造和电子商务。OFBiz拥有约170家客户，其中包括Atlassian JIRA、家得宝、美国联合航空公司和Upwork Global等大牌企业。

据发现该漏洞的SonicWall Capture Labs威胁研究团队声称，CVE-2024-38856漏洞存在于Apache OFBiz的“覆盖视图”功能中，攻击者可以利用这个缺陷，通过精心构造的请求来访问关键的终端。

原文链接：

https://www.darkreading.com/application-security/critical-apache-ofbiz-vulnerability-allows-preauth-rce

**Google Ads重大报告故障或泄露竞争对手数据**

近日，谷歌广告的重大报告故障导致一些广告商无法获得关键的广告效果数据，而且泄露了敏感的竞争对手信息，引发了对数据安全和不公平商业行为的严重担忧。

该问题始于7月30日，导致谷歌广告的某些功能，如报告编辑器、仪表盘和保存的报告在Web界面中无法使用，而产品、产品组和列表组页面在Web界面、API和谷歌广告编辑器中都无法访问。由此导致广告商无法访问关键的性能数据，包括有关竞争对手产品和广告策略的信息

在7月30日至31日，一小部分广告商还能看到其他账户中的无关商品ID、产品名称和商家中心信息。这起安全事件使广告商可以通过搜索泄露的产品名称来识别直接竞争对手，引发了严重的隐私问题。

目前谷歌已确认该问题，并表示正积极解决问题。

原文链接：

https://thecyberexpress.com/google-ads-suffers-glitch-exposing-competitors/

**行业动态**

**微软正式将安全工作和员工绩效挂钩**

据theverge网站报道，在经历了一系列安全事件和外界批评后，微软决定将安全问题提升到前所未有的高度。从8月6日开始，微软将其安全工作与员工绩效评估联系起来。微软首席人力官Kathleen Hogan在一份内部备忘录中表示，微软的每个人都应该将安全作为核心优先事项。在面临抉择时，明确安全高于一切。

报道称，微软现在已将安全性与多样性和包容性并列作为其关键优先事项之一，这两者都成为每位员工绩效对话（内部称为“Connect”）的一部分，以及员工与其经理之间商定的优先事项。所有微软员工都需要使用该公司的Connect工具进行绩效评估，包括高管人员。

微软员工如果对安全缺少关注，可能会影响晋升、绩效加薪和奖金。对于技术员工来说，这意味着在项目开始时就应该将安全性纳入产品设计流程，遵循既定的安全实践，并确保产品对微软客户来说默认是安全的。作为安全未来计划（SFI）的一部分，微软彻底改革了其安全工作，以更好地保护微软的网络、生产系统、工程系统等。

原文链接：

https://www.theverge.com/2024/8/5/24213774/microsoft-security-performance-reviews-employees-top-priority

**ISACA发布系列AI学习资源**

为了帮助专业人士应对AI带来的挑战和机遇，专业技术组织ISACA日前推出了一系列AI培训课程，旨在培养审计师、网络安全经理、风险分析师和隐私专家等数字信任专业人士在AI领域的技能和知识。这些新课程不仅有助于专业人士掌握AI的基本原理和技术应用，还能加深他们对AI伦理的理解，从而更好地支持企业的AI采纳与使用。

新课程包括面向审计人员人工智能入门课程，主要介绍与审计相关的AI基本概念，深入探讨特定的AI技术、AI驱动的工具和系统，以及与审计相关的伦理考量；人工智能中的伦理视角课程，探讨AI使用的伦理后果、应考虑的伦理原则，以及AI对社会可能产生的影响；业务赋能导向的机器学习课程，探索如何有效地评估机器学习解决方案，更好地评估风险，并促进负责任的采用。

ISACA最新研究揭示，23%的受访者表示他们的组织正在考虑增加AI相关的工作岗位，60%的受访者认为AI将在未来一年内对审计/保证领域产生积极影响，这一比例超过了风险、合规性、安全、IT战略/治理和隐私等其他领域。

原文链接：

https://mp.weixin.qq.com/s/s3iRxLebxp6qlwR9WizeeA

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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