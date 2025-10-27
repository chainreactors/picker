---
title: 特朗普推翻拜登人工智能行政命令；警惕！勒索软件团伙滥用微软Teams发起攻击 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651134812&idx=2&sn=1644fdd615891c190020e26e48734279&chksm=bd15ab8f8a62229945c2a446ad5f94a740189be7bde929cd002d7b0d2cf230da898fbb608135&scene=58&subscene=0#rd
source: 安全牛
date: 2025-01-23
fetch_date: 2025-10-06T20:10:35.773070
---

# 特朗普推翻拜登人工智能行政命令；警惕！勒索软件团伙滥用微软Teams发起攻击 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkBxZspAhgWwOBgmMQy3dOU4iaMbghic9uIQubSnj9gepKxOXSOeAnqqXb5s1not7jKVV8I9yQTGDBEQ/0?wx_fmt=jpeg)

# 特朗普推翻拜登人工智能行政命令；警惕！勒索软件团伙滥用微软Teams发起攻击 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•工信部提醒：防范开源文件同步工具rsync多个安全漏洞的风险

•特朗普推翻拜登人工智能行政命令

•Cloudflare成功缓解创纪录的5.6Tbps超大规模DDoS攻击

•美国政府承包商Conduent遭网络攻击，多州福利支付系统中断

•Mirai新变种通过物联网漏洞发动DDoS攻击

•英国一所中学因遭遇勒索软件攻击被迫停课

•警惕！勒索软件团伙滥用微软Teams发起攻击

•卡巴斯基披露梅赛德斯-奔驰MBUX娱乐系统十多个漏洞

•Darktrace加码云安全，收购英国网络取证公司Cado

•守内安和ASRC发布《2024年度邮件安全观察报告》，揭示三大趋势

**特别关注**

**工信部提醒：防范开源文件同步工具rsync多个安全漏洞的风险**

1月21日，工业和信息化部网络安全威胁和漏洞信息共享平台发布《关于防范开源文件同步工具rsync多个安全漏洞的风险提示》，指出工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）监测发现，开源文件同步工具rsync存在堆缓冲区溢出等多个漏洞，危害严重。

Rsync是一款开源文件同步与数据传输工具，被广泛用于备份、镜像、数据迁移等场景。由于程序缺陷，存在堆缓冲区溢出、信息泄露、文件泄露、外部目录写入、安全链接绕过和符号链接竞态条件共6个漏洞，可被攻击者组合利用导致远程代码执行等危害，影响3.3.0及以下版本。使用受影响版本rsync的Rclone、DeltaCopy、ChronoSync等备份软件，以及AlmaLinux、Arch、Gentoo、NixOS、Red Hat、SUSE等Linux发行版也受该漏洞影响。目前，rsync官方已修复上述漏洞并发布安全公告。

（公告链接：

https://download.samba.org/pub/rsync/NEWS#3.4.0）

建议相关单位和用户立即开展全面排查，按照官方安全公告升级至3.4.0或更高版本，或采取关闭rsync服务、禁用rsync匿名读取权限等安全防护措施，防范网络攻击风险。

原文链接：

https://mp.weixin.qq.com/s/83njqmciQZzsiup6IONVow

**热点观察**

**特朗普推翻拜登人工智能行政命令**

美国新任总统唐纳德·特朗普在就职首日推翻了前总统乔·拜登于2023年10月30日签署的"关于人工智能安全、可靠和可信赖发展与使用的行政命令"。

该行政命令为联邦机构制定了一系列举措，旨在加强人工智能安全性、避免滥用、偏见和隐私违规等危害，并增强美国人工智能专业人才库。该命令还要求开发"双用基础模型"(包含数十亿参数的最强大模型)的开发者向联邦政府报告其计划、网络安全措施和红队测试结果。

尽管该行政命令为联邦机构制定相关政策、开发框架和发布报告设置了多项已过期的最后期限，但推翻该命令将终止对其目标的持续监测和报告要求，包括与双用基础模型相关的要求。

原文链接：

https://www.scworld.com/news/trump-repeals-2023-biden-administration-executive-order-on-ai

**Cloudflare成功缓解创纪录5.6Tbps超大规模DDoS攻击**

网络安全和连接服务提供商Cloudflare成功缓解了发生在去年10月29日一起创纪录的5.6Tbps分布式拒绝服务(DDoS)攻击。这是迄今为止规模最大的DDoS攻击，峰值达到每秒5.6万亿位。

这是针对东亚地区的一家互联网服务提供商的攻击，试图让其服务离线。攻击持续了80秒，但由于Cloudflare的检测和缓解完全自动化，因此没有对目标造成任何影响或触发警报。攻击来自一个基于Mirai的僵尸网络，包含13，000台受感染设备。Cloudflare此前在2024年10月初报告了一起3.8Tbps的DDoS攻击，持续65秒，曾是最大规模的体量攻击。

Cloudflare警告，DDoS攻击持续时间越来越短，以至于人工响应、分析流量和应用缓解措施已经无法实现，这些短暂的超大流量通常发生在高峰使用期，如节假日和促销活动，以期产生最大影响，为勒索DDoS攻击创造条件。Cloudflare认为，攻击持续时间的缩短强调了内置、始终在线、自动化DDoS保护服务的必要性。

原文链接：

https://www.bleepingcomputer.com/news/security/cloudflare-mitigated-a-record-breaking-56-tbps-ddos-attack/

**网络攻击**

**美国政府承包商Conduent遭网络攻击，多州福利支付系统中断**

美国政府承包商巨头Conduent公司正遭遇一起"服务中断"事件，导致美国多个州的居民无法获取部分福利和支付款项。

美国威斯康星州儿童及家庭部门在1月17日的社交媒体帖子中告知居民，该州当周大部分时间无法处理儿童抚养费支付。该部门称，包括威斯康星在内的四个州都受到了Conduent公司中断事件的影响。此前俄克拉荷马人力资源部门在1月9日的社交媒体帖子中告知居民，Conduent的客户服务热线受到了"技术中断"的影响。

一位知情人士告诉媒体，此次中断是由于一起网络攻击所致。Conduent发言人Sean Collins承认公司确实发生了服务中断，部分服务已经恢复，但拒绝回答相关问题或排除网络事件的可能性。

原文链接：

https://techcrunch.com/2025/01/21/govtech-giant-conduent-wont-rule-out-cyberattack-as-outage-drags-on/

**Mirai新变种通过物联网漏洞发动DDoS攻击**

Qualys威胁研究团队近期发现了一场针对AVTECH摄像头和华为HG532路由器的大规模活动。攻击者利用ELF和shell脚本执行的方式，通过利用现有漏洞(CVE-2024-7029、CVE-2017-17215)下载下一阶段的恶意载荷，部署名为 Murdoc\_Botnet 的新 Mirai 变种僵尸网络，发动DDoS攻击。

研究人员发现，攻击者利用约 1300 多个活跃 IP 和100 多个服务器进行指挥控制和分发恶意软件。Murdoc\_Botnet主要针对\*nix系统，尤其是存在漏洞的AVTECH和华为设备。该恶意软件主要使用bash脚本，利用GTFOBins获取恶意载荷、使用chmod授予执行权限，然后执行并删除它们。此外，它还利用现有漏洞获取下一阶段的恶意载荷。感染过程包括利用漏洞下载shell脚本，这些脚本在被入侵的设备上执行，从而下载Mirai僵尸网络的新变种。

为了防御 Murdoc\_Botnet 攻击，安全专家建议组织监控可疑进程，避免从不可信来源执行 shell 脚本，并及时更新系统和固件的最新补丁。

原文链接：

https://hackread.com/mirai-variant-murdoc-botnet-ddos-attacks-iot-exploits/

**英国一所中学因遭遇勒索软件攻击被迫停课**

位于英国切斯特的布莱肯高中在1月17日遭遇勒索软件攻击后，不得不于1月20日和21日停课两天。学校的许多IT系统目前已瘫痪，老师不得不通过谷歌教室平台布置了作业，供学生在家完成。

该校校长表示，尽管采取了最新的安全措施，但这种网络攻击发生的频率越来越高，英国国家医疗服务体系、国家铁路、其他公共部门和学校都遭受过类似攻击。就在两天前的1月15日，Medusa勒索软件团伙曾攻击了盖茨黑德市政府，在数据泄露网站上公布了31页被盗取的文件和截图，包括居民和员工的个人身份信息，并索要60万美元赎金以"删除"被盗数据。去年，英国国家医疗服务体系遭受了多次勒索软件袭击，其中包括夏季对病理服务提供商Synnovis的攻击，导致数千个预约和手术程序在伦敦主要医院受到影响。11月下旬，INC Ransom勒索团伙还攻击了英格兰北部最大的儿童医院阿尔德黑儿童医院。

当前，英国政府正在考虑全面禁止公共部门和关键国家基础设施组织支付赎金，，同时要求大型私营企业向政府申请支付赎金许可。

原文链接：

https://www.theregister.com/2025/01/20/blacon\_high\_school\_ransomware/

**警惕!勒索软件团伙滥用微软Teams发起攻击**

网络安全公司Sophos发现，威胁组织STAC5143和STAC5777滥用包括Teams和Outlook在内的微软Office 365服务，伪装成IT支持人员以获取受害组织系统的初始访问权限，企图窃取数据和部署勒索软件。Sophos透露，在过去三个月内观察到超过15起此类事件。

在这些攻击中，威胁组织采用了共同的策略，包括"电子邮件轰炸"、语音钓鱼以及使用微软远程控制工具。这两个威胁组织在攻击中都运营自己的微软Office 365服务租户，并利用了微软Teams的默认配置，允许外部域的用户与内部用户发起聊天或会议。他们用大量垃圾邮件淹没受害组织某些员工的Outlook收件箱，以"制造紧迫感"；他们滥用Teams，通过语音或视频通话伪装成组织的技术支持人员，接触目标员工。他们使用微软远程控制工具(Quick Assist或直接通过Teams屏幕共享)控制目标个人的计算机并安装恶意软件。

安全专家强调，任何可能被跨组织消息传递或凭据和访问令牌盗窃利用的通信平台都可能成为此类网络犯罪的目标。Sophos敦促组织确保其微软Office 365服务配置限制了来自外部的Teams通话，并为远程访问应用程序(如Quick Assist)设置了限制性策略。此外，还要加强员工的社会工程学意识培训。

原文链接：

https://www.techtarget.com/searchsecurity/news/366618294/Threat-actors-abusing-Microsoft-Teams-in-ransomware-attacks

**安全漏洞**

**卡巴斯基披露梅赛德斯-奔驰MBUX娱乐系统十多个漏洞**

网络安全公司卡巴斯基披露了其在梅赛德斯-奔驰MBUX车载信息娱乐系统中发现的十多个漏洞的细节。

卡巴斯基基于一个中国团队2021年公布的研究结果发现，第一代MBUX的一些漏洞可被利用进行拒绝服务攻击，另一些可用于获取数据、命令注入和权限提升。卡巴斯基表示，他们证实了攻击者在物理接触目标车辆的情况下，可以利用部分漏洞禁用车载主机的防盗保护、对车辆进行调优以及解锁付费服务。这些攻击是通过USB或自定义UPC连接进行的。

这些漏洞被分配了2023年和2024年的CVE编号，但梅赛德斯-奔驰向媒体透露，他们早在2022年就已经知晓卡巴斯基的研究发现。此外，研究人员描述的主题需要现场物理接触车辆，并进入车内，还需要拆卸并打开车载主机。新版本的信息娱乐系统不受影响。"

原文链接：

https://www.securityweek.com/details-disclosed-for-mercedes-benz-infotainment-vulnerabilities/

**产业动态**

**Darktrace加码云安全，收购英国网络取证公司Cado**

网络安全公司Darktrace宣布将收购英国网络取证和响应解决方案提供商Cado Security，以增强其云安全能力。此次收购旨在将Cado的取证调查技术与Darktrace的ActiveAI安全平台相结合，提升跨多云环境的数据收集能力。该交易预计将于下月完成。

Cado Security在多云、容器、无服务器、SaaS和本地环境中提供服务，能捕获设备上存储的数据快照，并进行取证调查以发现入侵痕迹或威胁。Darktrace计划投资加速Cado现有产品的增长，同时将其取证技术与自身的ActiveAI安全平台相融合，增强跨多云环境的数据收集能力。凭借此次收购带来的更丰富数据集，Darktrace还预计将为其Cyber AI Analyst解决方案带来益处，该解决方案可调查警报、简化调查并优先处理事件。

Darktrace将此次收购视为加强其云安全能力的一个举措。该公司近年来在这一领域进行了大量投资。该公司指出，最近的一项研究显示，安全领导者认为云安全是防御性AI能产生最大影响的领域之一。去年10月，该公司推出了面向AWS的Darktrace/CLOUD服务，后来又扩展到覆盖微软Azure。

原文链接：

https://www.itpro.com/cloud/cloud-security/darktrace-targets-cloud-security-gains-with-cado-security-acquisition

**守内安和ASRC发布《2024年度邮件安全观察报告》，揭示三大趋势**

近日，守内安和ASRC共同发布《2024年度邮件安全观察报告》。报告显示，2024年被用于攻击或携带垃圾信息的Word文件，以及通过新注册或不存在的假冒域名发送的垃圾邮件数量，相较于2023年增长了约50%。相反，通过同一IP连续发送、退信攻击，或利用动态IP发送的垃圾邮件数量则呈现明显下降趋势，这可能是攻击者有意减少使用无效或易被检测的攻击手段。

针对2024年的邮件攻击手法与模式，报告总结了邮件安全的三个主要趋势：浏览器成为重要的攻击目标；手机成为新的攻击突破口；以假乱真的社交工程手段。

原文链接：

https://mp.weixin.qq.com/s/\_1\_PoOV8zcVJSExeM\_-C9w

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAibeib6HUSIXJ4IhpazTYic3uwicySgIEk8ZeMC7X5evYXoNPHxoUlibqgo6Ilq0dRkGrMKibWtfcibYwsg/640?wx_fmt=jpeg)

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