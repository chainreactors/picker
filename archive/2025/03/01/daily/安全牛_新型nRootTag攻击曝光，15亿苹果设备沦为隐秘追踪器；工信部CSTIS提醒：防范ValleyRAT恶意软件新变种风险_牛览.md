---
title: 新型nRootTag攻击曝光，15亿苹果设备沦为隐秘追踪器；工信部CSTIS提醒：防范ValleyRAT恶意软件新变种风险|牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651135308&idx=1&sn=e03bb682338965dfba6c0673040f2a89&chksm=bd15ad9f8a622489190bd17eea22bf60341b7d554cf755fdab0e1ed52c58d939f28dacc458b0&scene=58&subscene=0#rd
source: 安全牛
date: 2025-03-01
fetch_date: 2025-10-06T21:58:28.410561
---

# 新型nRootTag攻击曝光，15亿苹果设备沦为隐秘追踪器；工信部CSTIS提醒：防范ValleyRAT恶意软件新变种风险|牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB21ulMQ4c9HzJgFPgTONZsRS0D35x5afA0gbzJ67K42fQN6DxiaY152GyicT21sKCibjOEerzBqQia6w/0?wx_fmt=jpeg)

# 新型nRootTag攻击曝光，15亿苹果设备沦为隐秘追踪器；工信部CSTIS提醒：防范ValleyRAT恶意软件新变种风险|牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•工信部CSTIS提醒：防范ValleyRAT恶意软件新变种风险

•新型nRootTag攻击曝光，15亿苹果设备沦为隐秘追踪器

•90多起数据泄露案幕后黑客GHOSTR落网

•Anubis新兴勒索软件服务通过多元化加盟计划加剧威胁

•短暂的暴露GitHub代码库，或永久留存于微软Copilot

•思科Nexus交换机曝高危命令注入漏洞，或使攻击者获得根级访问权限

•西门子Teamcenter存在高危漏洞，攻击者可能窃取会话数据

•虚拟Krpano框架漏洞被利用，黑客在350多个网站植入垃圾广告

•近5万建筑物出入管理系统暴露在网上，或危及隐私和实体安全

**特别关注**

**工信部CSTIS提醒：防范ValleyRAT恶意软件新变种风险**

2月28日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）发布《关于防范ValleyRAT恶意软件新变种的风险提示》。根据风险提示，该恶意软件主要针对政府机构及企业财务、销售等关键岗位人员实施攻击并窃取敏感业务数据。

ValleyRAT是一款基于C++的远程访问木马，具备多阶段攻击能力和虚拟环境逃逸特性。新变种通过伪造Chrome浏览器安装包、钓鱼邮件等进行传播。攻击者利用伪造的.NET可执行文件触发感染链，通过svchost.exe进程注入监控模块，强制终止安全防护进程，并借助Valve游戏组件Tier0.dll实现隐蔽驻留。其攻击链采用多层规避手段，首先禁用AMSI反病毒接口（微软的Windows系统接口，允许反恶意软件扫描内存脚本或代码）与ETW事件追踪功能（微软提供的事件追踪技术，用于收集和分析事件数据），随后通过Donut外壳代码在内存中加载恶意载荷，规避传统磁盘扫描。植入成功后，该恶意软件会通过访问WinSta0窗口站来窃取屏幕信息、键盘输入及系统敏感信息等。

工信部CSTIS建议相关单位及用户立即组织排查，及时更新防病毒软件。启用应用程序白名单限制非授权DLL（动态链接库）加载，针对财务等重点岗位开展钓鱼邮件专项演练。谨慎点击不明来源的链接或下载运行来源不明的应用程序，加强网络安全意识培训，防范网络攻击风险。

原文链接：

https://mp.weixin.qq.com/s/EgnTdpw3HjawfytqmDo-Cw

**网络攻击**

**新型nRootTag攻击曝光，15亿苹果设备沦为隐秘追踪器**

新型攻击nRootTag正在使超过15亿台苹果设备面临被恶意行为者秘密追踪的风险，包括iPhone、iPad、Apple Watch和Mac。这一发现将在即将召开的USENIX Security Symposium 2025上详细披露。

该攻击利用了苹果的"查找我的"网络，能将非苹果设备转变为隐蔽的追踪器，而无需获取根权限。这种利用蓝牙低功耗协议的漏洞，对全球隐私构成了前所未有的威胁。苹果的这一定位系统，依赖于AirTag广播的加密"丢失消息"，由附近的苹果设备转发至云端，从而让用户追踪设备位置。nRootTag通过伪造合法AirTag广播信号，绕过了该系统的安全防护。攻击过程始于在目标设备植入木马代码，收集设备的蓝牙广播地址，并从攻击者服务器获取匹配的公私钥对。一旦配置完成，设备就会广播伪造的"丢失消息"。附近的苹果设备在不知情的情况下充当"查找器"角色，将这些消息转发至苹果服务器，使攻击者能实时追踪目标设备的位置。

研究人员指出，nRootTag的低成本和可扩展性使其难免会被网络犯罪分子采用。苹果已在iOS 18.2、macOS Sequoia 15.2等更新中修复了nRootTag漏洞，但只能阻止更新后的苹果设备转发恶意信号。随着支持蓝牙的设备不断增多，研究呼吁重新评估离线查找系统的密码学设计，以防止恶意追踪成为常态。

原文链接：

https://cybersecuritynews.com/new-attack-nroottag-iphones/

**90多起数据泄露案幕后黑客GHOSTR落网**

近日，在泰国、新加坡执法部门和网络安全公司Group-IB的联合行动中，一名使用"GHOSTR"等多个化名活动、被指与90多起数据泄露事件有关的黑客被捕。

据报道，这名被控黑客曾使用GHOSTR、ALTDOS、DESORDEN和0mid16B等多个在线身份，窃取并在暗网市场出售超过13TB的敏感信息，包括政府机构记录。这名至少自2020年就已活跃的黑客，起初针对泰国、新加坡、马来西亚、巴基斯坦和印度等亚太国家的组织，后扩展至欧洲、北美和中东地区。他最初通过威胁公开被盗数据，向公司施压勒索，如果被无视则常常通知媒体或监管机构；后来转而在暗网论坛出售数据库，因高质量泄露而臭名昭著，能够索取高价。在某些情况下，他甚至直接给公司客户发邮件施压。

该黑客利用常见漏洞渗透系统，使用sqlmap等工具执行SQL注入攻击。这种方法可利用网站访问后端数据库，并入侵安全性差的远程桌面协议(RDP)服务器。一旦进入，他们就会部署经过修改的渗透测试工具CobaltStrike，以控制被入侵网络。被窃取的数据随后被复制到云服务器用于勒索。

原文链接：

https://hackread.com/ghostr-hacker-linked-to-90-data-breaches-arrested/

**Anubis新兴勒索软件服务通过多元化加盟计划加剧威胁**

最新调查发现，去年底首次被发现的新兴勒索软件服务(Ransomware-as-a-Service，RaaS)运营团伙Anubis，凭借其广泛的加盟计划，可能会成为今年对企业构成严重威胁的一股新力量。

威胁情报公司Kela发现，Anubis幕后黑客superSonic推出了三种新的加盟计划，包括经典的勒索软件选项、盗取数据货币化服务，以及向访问代理支付后续收益。尽管Anubis入侵了澳大利亚医疗服务提供商Pound Road Medical Centre并窃取了其数据，但并未被发现使用勒索软件，这表明其更侧重于数据勒索。Anubis专注于数据勒索，但superSonic的帖子却详细介绍了其恶意载荷的文件加密能力，表明传统的RaaS加密仍在其攻击范围之内。

该新兴RaaS运作团伙凭借其多元化的加盟计划，对企业网络安全构成了日益严峻的威胁，企业需提高警惕，加强防护。

原文链接：

https://www.securityweek.com/new-ransomware-anubis-could-pose-major-threat-to-organizations/

**安全漏洞**

**短暂的暴露GitHub代码库，或永久留存于微软Copilot**

安全研究人员近日警告称，即使是短暂暴露在互联网上的数据，也可能长期滞留在微软Copilot等在线生成式AI聊天机器人中，即使该数据后来已被设为私有。根据网络安全公司Lasso的发现，属于亚马逊网络服务、谷歌、IBM、PayPal、腾讯和微软等1.6万多个组织的超过2万个已私有的GitHub代码库的数据仍可通过Copilot访问。

Lasso公司的发现源自察觉到其GitHub代码库的内容出现在Copilot中，因为这些内容之前曾被微软的必应搜索引擎索引和缓存。该代码库曾一度被误设为公开，后来已重新设为私有，在GitHub上访问会显示"页面未找到"的错误。在意识到 GitHub 上的任何数据（即使是短暂的数据）都可能被 Copilot 等工具泄露后，Lasso 进一步展开了调查。

研究人员表示，这一漏洞可能被利用来暴露包含敏感公司信息、访问密钥和令牌，以及知识产权的GitHub存档，即使微软在停用必应缓存功能后，Copilot仍可持续访问这些数据。

原文链接：

https://techcrunch.com/2025/02/26/thousands-of-exposed-github-repositories-now-private-can-still-be-accessed-through-copilot/

**思科Nexus交换机曝高危命令注入漏洞，或使攻击者获得根级访问权限**

思科系统公司近日发布了一则严重安全公告，披露了其Nexus 3000和9000系列交换机在独立NX-OS模式下存在一个命令注入漏洞（CVE-2025-20161）。该漏洞允许拥有管理员权限的经过身份验证的本地攻击者，在底层操作系统上执行任意命令，获取根级访问权限。

CVE-2025-20161源于软件升级过程中的不当输入验证。具体而言，交换机未能对软件镜像中的元素进行适当净化，使攻击者能够制作恶意镜像，将命令注入操作系统。该漏洞利用了CWE-78(OS命令注入)这一常见漏洞，即未经信任的数据被传递到系统命令中。

该漏洞影响所有运行独立NX-OS软件的思科Nexus 3000和9000系列交换机。思科已发布修补程序版本。尽管CVE-2025-20161尚未被发现在活跃攻击中利用，但其潜在影响值得高度重视。网络管理员应:通过官方软件检查门户应用思科的安全更新；严格控制管理员账户访问；对所有软件镜像实施哈希值验证。

原文链接：

https://cybersecuritynews.com/cisco-nexus-vulnerability-malicious-commands/

**西门子Teamcenter存在高危漏洞，攻击者可能窃取会话数据**

研究人员近日发现，西门子Teamcenter产品生命周期管理(PLM)软件存在一个高危安全漏洞(CVE-2025-23363)。该漏洞可能允许攻击者窃取用户的有效会话数据，并获得对易受攻击应用程序的未经授权访问。

西门子Teamcenter是一套应用程序，被企业用于管理产品的整个生命周期，广泛应用于航空航天、国防、汽车、工业机械制造等行业。CVE-2025-23363是Teamcenter单点登录(SSO)服务中的一个开放重定向漏洞。在受影响的应用程序中，该服务接受用户控制的输入，可能指定到外部站点的链接。这可能允许攻击者制作一个链接，将合法用户重定向到攻击者选择的URL，以窃取有效的会话数据。

尽管西门子公司本月早些时候私下修复了由Nicolo Vinci报告的CVE-2025-23363漏洞，但由于实施的修复程序被撤回(因为"不充分")，该漏洞目前仍可被利用。当前该公司正在为CVE-2025-23363漏洞制定新的修复方案。与此同时，建议用户避免点击来自不受信任来源的链接。

原文链接：

https://www.helpnetsecurity.com/2025/02/27/siemens-teamcenter-vulnerability-could-allow-account-takeover-cve-2025-23363/

**虚拟Krpano框架漏洞被利用，黑客在350多个网站植入垃圾广告**

安全研究员近日在一份报告中指出，虚拟旅游框架Krpano的跨站脚本(XSS)漏洞被恶意分子利用，在数百个网站注入恶意脚本，用于操纵搜索结果并大规模推广垃圾广告。这一被称为"360XSS"的活动影响了超过350个网站，包括政府门户网站、美国大学、酒店连锁、新闻媒体等，以及多家财富500强公司。

这一活动利用了Krpano的一个配置设置"passQueryParameters"，该设置旨在将HTTP参数从URL传递到查看器。如果启用该选项，攻击者就可以使用特制的URL在访问易受攻击网站时在受害者浏览器中执行恶意脚本。Krpano早在2020底披露了这一行为导致的反射型XSS漏洞(CVE-2020-24901)。Krpano在1.20.10版本中引入了更新，试图通过限制"passQueryParameters"到允许列表来防止此类XSS攻击发生，但将XML参数明确添加到允许列表中会重新引入XSS风险。

在负责任的披露后，Krpano的最新版本1.22.4通过消除对XML参数的外部配置支持，从而消除了即使使用该设置时也存在XSS攻击的风险。Krpano用户建议升级到最新版本，并将"passQueryParameters"设置为false。受影响的网站所有者建议通过Google搜索控制台查找并删除感染页面。

原文链接：

https://thehackernews.com/2025/02/hackers-exploited-krpano-framework-flaw.html

**近5万建筑物出入管理系统暴露在网上，或危及隐私和实体安全**

Modat研究人员发现，全球4.9万多个错误配置且暴露在互联网上的出入管理系统(AMS)，可能会危及关键行业的隐私和实体安全。

出入管理系统是通过生物识别、ID卡或车牌等方式控制员工进出建筑物、设施和禁区的安全系统。研究人员全面调查发现，数以万计的互联网暴露的AMS系统未正确配置安全身份验证，任何人都可以访问。这些暴露的AMS包含未加密的敏感员工数据，如个人身份信息、生物特征数据、照片、工作时间表和出入记录等。在某些情况下，黑客甚至可以编辑员工记录、添加虚假员工、更改访问凭证或操纵出入系统，限制合法员工进出或允许未经授权的人员进入。对于政府建筑和关键基础设施的暴露AMS系统，其实体安全风险尤其令人担忧。除实体安全外，暴露的信息还可能被利用实施精准的网络钓鱼和社会工程学攻击。

Modat为AMS用户提供了多项安全建议，包括将系统暂时离线防止未经授权的远程访问，或将其放置在防火墙和VPN后仅允许授权人员访问。Modat还建议更改默认管理员凭证，并实施多因素身份验证。AMS管理员应安装供应商的最新软件和固件更新，减少不必要的网络服务以降低攻击面。

原文链接：

https://www.bleepingcomputer.com/news/security/over-49-000-misconfigured-building-access-systems-exposed-online/

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAibeib6HUSIXJ4IhpazTYic3uwicySgIEk8ZeMC7X5evYXoNPHxoUlibqgo6Ilq0dRkGrMKibWtfcibYwsg/640?wx_fmt=jpeg)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

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