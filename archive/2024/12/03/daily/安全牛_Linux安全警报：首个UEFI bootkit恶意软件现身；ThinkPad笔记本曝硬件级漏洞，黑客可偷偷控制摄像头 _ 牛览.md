---
title: Linux安全警报：首个UEFI bootkit恶意软件现身；ThinkPad笔记本曝硬件级漏洞，黑客可偷偷控制摄像头 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133722&idx=1&sn=c3ac7d76f7b002486115949f7551d7b0&chksm=bd15a7c98a622edfc0eced4f184a4d959fa1ff4e5354018393a27f00466fffaf7211ee585683&scene=58&subscene=0#rd
source: 安全牛
date: 2024-12-03
fetch_date: 2025-10-06T19:39:17.481779
---

# Linux安全警报：首个UEFI bootkit恶意软件现身；ThinkPad笔记本曝硬件级漏洞，黑客可偷偷控制摄像头 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAGX2kcFynXfjgI9e16X2GiaOVSMfFMdpAgB1191JlzFaYtRtLIg5L2BMtJticCTRkGKZia2OJ3j1XtA/0?wx_fmt=jpeg)

# Linux安全警报：首个UEFI bootkit恶意软件现身；ThinkPad笔记本曝硬件级漏洞，黑客可偷偷控制摄像头 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•隐私监管审查不断加码，Tor项目或启动WebTunnel网桥扩展计划

•澳大利亚新《网络安全法》获通过，强制要求报告勒索赎金支付

•Linux系统警报：首个UEFI bootkit恶意软件现身

•勒索攻击冲击英国医疗体系，威勒尔大学教学医院服务一度中断

•绕过多因素认证，Rockstar  2FA新型钓鱼工具瞄准Microsoft 365用户

•ThinkPad笔记本曝硬件级漏洞，黑客可偷偷控制摄像头

•漏洞利用代码被疯传，开源文件共享应用ProjectSend陷入严重安全危机

•Oracle  Agile PLM框架爆严重安全漏洞，或致企业核心数据泄露

•流行开源监控工具Zabbix曝SQL注入漏洞，普通用户也能完全控制系统

**热点观察**

**隐私监管审查不断加码，Tor项目或启动WebTunnel网桥扩展计划**

来自Tor用户的报告显示，监管机构的在线审查正在升级，目标是阻止访问Tor和其他规避工具。这波新的审查浪潮包括尝试封锁Tor网桥和可插拔传输、从应用商店移除规避应用，以及针对流行的托管提供商，从而缩小了绕过审查的空间。

在此背景下，Tor项目日前向一些隐私社区发出呼吁，希望社区志愿者能在年底前帮助其部署200个新的WebTunnel网桥，以对抗监管机构不断加码的安全审查。目前，Tor项目运营着143个WebTunnel网桥，这些网桥帮助严格审查地区的用户绕过互联网访问限制和网站封锁。

Tor表示，监管部门的审查目前已经影响到浏览器内置的反审查机制，包括obfs4连接和Snowflake。Tor项目认为，设置更多的WebTunnel网桥是应对这种审查升级的最佳方法，因为分析新策略和开发解决方案需要时间，而用户在此期间可能无法访问自由互联网。

WebTunnel是Tor项目于2024年3月推出的一种新型网桥，专门设计用于将Tor流量与常规网络流量混合，使审查者更难检测和封锁。该系统通过在具有有效SSL/TLS证书的Web服务器上运行，将Tor流量伪装成常规HTTPS流量。与使用特定协议（如obfs4）的标准Tor网桥不同，WebTunnel网桥"隐藏在明处"，使其能够抵抗激进的审查。

原文链接：

https://www.bleepingcomputer.com/news/security/tor-needs-200-new-webtunnel-bridges-to-fight-censorship

**澳大利亚新《网络安全法》获通过，强制要求报告勒索赎金支付**

近日，澳大利亚议会通过了新的《网络安全法》，其中最关键的条款之一是要求组织机构在向黑客支付勒索款项后72小时内进行报告。这一变化旨在提高澳大利亚的网络弹性，震慑网络犯罪分子，同时确保企业对其行为负责。

根据新法，除小型企业外，所有公司在支付任何勒索软件赎金后，无论金额大小，都必须向澳大利亚信号局（ASD）报告。这一举措将帮助ASD监控勒索软件趋势，评估潜在的国家安全威胁，并协助执法部门追踪网络犯罪分子。值得注意的是，法律特别指出，虽然不鼓励向网络犯罪分子付款，但在特殊情况下，支付赎金可能是合理的。

除了报告勒索支付外，该法还引入了智能设备新安全标准。物联网设备制造商将被要求满足新的安全标准，包括安全的默认设置、每台设备的唯一密码和敏感数据加密。此外，法案还设立了网络事件审查委员会，负责审查影响国家安全或公共福利的重大网络事件。

《网络安全法》还扩大了《关键基础设施安全法》（2018年）的范围，将与关键基础设施相关的数据系统纳入其中。这一变化赋予了监管机构更多权力，以评估和解决可能影响国家安全或公共安全的漏洞。

原文链接：

https://thecyberexpress.com/australia-cyber-security-act/

**网络攻击**

**Linux系统警报：首个UEFI bootkit恶意软件现身**

近日，安全公司ESET披露了一个重大发现：首个针对Linux系统设计的UEFI bootkit恶意软件Bootkitty。这一发现打破了长期以来Linux系统比Windows更安全的观念，同时也引发了对操作系统用户数量是否影响其成为恶意软件目标的讨论。

UEFI bootkit是近期的重要安全隐患，它们既难以检测又难以删除，而且在操作系统加载之前就已经激活，允许攻击者从最基本的层面控制系统。但此前，UEFI bootkit仅影响基于Windows的系统。Bootkitty的出现标志着这类威胁已经扩展到Linux平台。

ESET是在VirusTotal上发现了一个此前未知的bootkit.efi UEFI应用程序后，揭示了这个针对Linux的UEFI bootkit恶意软件。尽管针对Linux的这类恶意软件的出现令人担忧，但ESET认为目前不必过度恐慌。

据ESET分析，Bootkitty的主要目标是禁用内核的签名验证功能，并通过Linux init进程（Linux内核在系统启动期间执行的第一个进程）预加载两个尚未知的ELF二进制文件。研究人员还发现了一个可能相关的未签名内核模块，该模块部署了一个ELF二进制文件，负责加载另一个在分析期间未知的内核模块。

原文链接：

https://betanews.com/2024/11/29/proving-linux-is-not-a-safe-sanctuary-eset-finds-first-linux-targeting-uefi-bootkit-malware/

**勒索攻击冲击英国医疗体系，威勒尔大学教学医院服务一度中断**

近日，隶属于英国国民保健服务（NHS）基金会信托的威勒尔大学教学医院（WUTH）遭遇重大网络勒索攻击，导致医疗服务中断，多项预约和手术被迫推迟。

WUTH运营着多家医疗机构，包括Arrowe Park医院、Clatterbridge医院和Wirral妇女儿童医院。本次攻击事件始于上周早些时候，直到周末仍在持续影响医院的IT系统。医院在检测到网络中的可疑活动后宣布进入重大事件状态。作为预防措施，WUTH隔离了其系统以防止问题扩散，导致部分IT系统离线。

为了应对攻击，部分受影响区域已转为手动操作模式，使用纸质流程代替数字系统。WUTH发言人表示，他们正在努力解决由有针对性的网络安全问题引发的故障，并与国家网络安全服务部门密切合作，以尽快恢复正常运营。

虽然紧急服务仍然可用，但这次勒索攻击已经对计划内服务造成了严重干扰。一些预约和手术程序被推迟，需要重新安排。医院继续优先处理紧急治疗，但患者在急诊科和评估区等待计划外医疗可能会经历比平常更长的等待时间。

原文链接：

https://cybersecuritynews.com/uk-healthcare-provider-suffered-cyberattack/

**绕过多因素认证，Rockstar 2FA新型钓鱼工具瞄准Microsoft 365用户**

近日，Trustwave安全研究人员发布报告，重点关注了一款名为Rockstar 2FA的钓鱼工具包。该工具包主要针对Microsoft 365账户，通过中间人攻击（AitM）绕过多因素认证（MFA）。

自2024年8月以来，研究人员观察到针对Microsoft 365用户的钓鱼活动激增。这些攻击活动的一个独特特征是使用汽车主题的网页，自2024年5月以来已识别出超过5000个相关域名。

Rockstar 2FA是DadSec/Phoenix钓鱼工具包的升级版本，采用钓鱼即服务（PaaS）模式运营。攻击者通过ICQ、Telegram和Mail.ru等平台进行营销和沟通，使得其他网络犯罪分子可以轻松获取这些易于设置的钓鱼工具。Rockstar 2FA钓鱼活动使用多种主题，包括文件共享、人力资源通知、MFA诱饵和账户警报等。该工具包通过FUD链接、混淆和二维码等方式逃避检测。此外，它还使用合法的链接重定向器绕过反垃圾邮件检测，并使用Cloudflare Turnstile反机器人检查来防止自动页面分析。

原文链接：

https://securityaffairs.com/171532/cyber-crime/rockstar-2fa-phaas.html

**安全漏洞**

**ThinkPad笔记本曝硬件级漏洞，黑客可偷偷控制摄像头**

近日，安全研究员Andrey Konovalov发现了一个影响ThinkPad X230型号笔记本电脑摄像头的严重安全漏洞。该漏洞允许攻击者在不触发LED指示灯的情况下秘密访问设备摄像头，引发了用户隐私安全的重大担忧。

Konovalov的研究始于对ThinkPad X230笔记本电脑进行USB模糊测试。通过深入分析和逆向工程，他发现了几个关键问题：摄像头固件可通过USB供应商请求被覆盖；LED指示灯由独立于摄像头传感器电源的GPIO引脚控制；内存映射的GPIO允许软件控制LED。

研究人员开发了一个多阶段的漏洞利用方法，包括固件分析、代码注入、内存操作和LED控制。他创建了一个强大的基于USB的植入程序，可以在不干扰正常摄像头操作的情况下执行任意代码，读写任何内存位置，并完全控制LED指示灯。

虽然这项研究集中在ThinkPad X230上，但Konovalov表示类似的漏洞可能存在于其他笔记本电脑型号中，特别是同一时期的产品。潜在的漏洞指标包括：通过UVC或供应商USB请求控制LED、可通过USB覆盖的固件、存在可利用漏洞的固件等。

原文链接：

https://cybersecuritynews.com/hackers-can-access-laptop-webcams/

**漏洞利用代码被疯传，开源文件共享应用ProjectSend陷入严重安全危机**

安全研究机构VulnCheck近日发出警告称，广受欢迎的开源文件共享Web应用ProjectSend中的一个严重安全漏洞（CVE-2024-11680）可能已被黑客积极利用。

这是一个身份验证不当的漏洞，影响ProjectSend r1720之前的版本。远程未经身份验证的攻击者可以通过向options.php发送精心构造的HTTP请求来利用此漏洞，从而未经授权修改应用程序的配置。成功利用后，攻击者可以创建账户、上传网页后门（webshell）并嵌入恶意JavaScript代码。虽然该漏洞的补丁早在2023年5月16日就已发布，但直到今年11月26日才被正式公开。

自补丁发布以来，包括Synactiv、Project Discovery（Nuclei）和Rapid7（Metasploit）在内的多个研究团队已发布了相关的漏洞利用代码。据介绍，自2024年9月以来，威胁行为者开始使用这些漏洞利用代码。攻击者还启用了用户注册功能（这是一个非默认设置），以获得身份验证后的访问权限，并修改登录页面以提示创建账户。

研究人员指出，考虑到这种设置被广泛启用，问题可能比"研究人员侵入性地检查易受攻击的版本"更为严重。他们认为，当前情况可能已经进入了"攻击者安装网页后门"的阶段。此外，该漏洞还允许攻击者嵌入恶意JavaScript，这可能导致一些有趣且不同的攻击场景。

原文链接：

https://securityaffairs.com/171494/hacking/projectsend-critical-flaw-actively-exploited.html

**Oracle Agile PLM框架爆严重安全漏洞，或致企业核心数据泄露**

印度计算机应急响应小组（CERT-In）近日发布警告，指出Oracle Agile产品生命周期管理（PLM）软件存在一个高风险安全漏洞（CVE-2024-21287）。该漏洞于2024年11月26日被发现，影响Oracle Agile PLM框架9.3.6版本。

该漏洞与PLM框架内的身份验证不当有关，允许攻击者通过HTTP连接远程利用系统。CERT-In的公告强调，数据泄露是该漏洞最令人担忧的后果之一。因为该漏洞可能允许经过身份验证的远程攻击者未经授权访问存储在Oracle Agile PLM系统中的敏感数据。如果成功利用，该漏洞可能导致关键系统信息泄露，使组织面临数据泄露、知识产权盗窃或PLM数据未经授权操作的高风险。

Oracle公司已发布安全警报，强烈建议客户将系统更新到最新安全补丁的Oracle Agile PLM框架9.3.6版本。这些补丁对于解决框架中发现的信息泄露漏洞和防止未经授权的访问或数据泄露至关重要。

原文链接：

https://thecyberexpress.com/cert-in-flags-cve-2024-21287/

**流行开源监控工具Zabbix曝SQL注入漏洞，普通用户也能完全控制系统**

近日，广受欢迎的开源监控解决方案Zabbix被发现存在一个严重的安全漏洞，可能允许攻击者完全控制受影响的实例。该漏洞被标识为CVE-2024-42327，影响多个Zabbix应用版本。

这个SQL注入漏洞存在于Zabbix前端的CUser类中，具体位于addRelatedObjects函数。该函数由CUser.get函数调用，而后者可被任何具有API访问权限的用户访问。尤为令人担忧的是，该漏洞可被具有默认User角色或任何提供API访问权限的角色的非管理员用户账户利用。

安全研究员Mark Rakoczi通过HackerOne漏洞赏金平台发现并报告了这一漏洞。受影响的Zabbix版本包括6.0.0至6.0.31、6.4.0至6.4.16和7.0.0。鉴于此漏洞的严重性，使用Zabbix的组织应优先关注此问题，安全专家建议实施以下缓解策略：

1. 审查并限制API访问权限

2. 为Zabbix前端实施额外的访问控制和监控

3. 使用Web应用防火墙（WAF）规则检测和阻止潜在的SQL注入尝试

4. 定期审核用户角色和权限

5. 实施网络分段以限制Zabbix服务器的暴露

6. 监控数据库和应用程序日志以发现可疑活动

原文链接：

https://cybersecuritynews.com/zabbix-sql-injection-vulnerability/

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