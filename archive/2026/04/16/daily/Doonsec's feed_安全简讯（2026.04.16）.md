---
title: 安全简讯（2026.04.16）
url: https://mp.weixin.qq.com/s/yeZ69s8DqIVcBDF82rysig
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:47:50.709096
---

# 安全简讯（2026.04.16）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrzR7iamDia6TVrMul2iaSZfDvnricNCkahWv2shr9icpGs6jibxM4Er2uhrwfwrqJySCa2q7korC9ia8EruvMOeVC4sNwNQJErXmGbdpg/0?wx_fmt=jpeg)

# 安全简讯（2026.04.16）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Nginx UI身份验证绕过漏洞已被恶意利用**

4月15日，Nginx UI 中一个支持模型上下文协议（MCP）的严重安全漏洞（编号CVE-2026-33032）目前正遭到恶意利用，攻击者无需任何身份验证即可完全控制目标服务器。该漏洞的根本原因在于nginx-ui未能对/mcp\_message端点实施有效保护，使得远程攻击者能够在无凭据的情况下调用特权MCP操作。由于这些操作涉及写入、修改及重新加载nginx配置文件，一个简单的未认证请求即可改变服务器行为，实现Web服务器的全面接管。美国国家标准与技术研究院（NIST）在国家漏洞数据库（NVD）中明确指出，任何网络攻击者均可未经认证调用所有MCP工具，包括重启nginx、创建或修改配置文件以及触发自动重载。Nginx UI官方于3月15日发布2.3.4版本修复该漏洞，此前一天由Pluto Security AI的研究人员报告。然而，漏洞标识符、技术细节及概念验证（PoC）代码直至月底才公开披露。本周早些时候，Recorded Future在CVE概览报告中确认该漏洞正被积极利用。Pluto Security通过Shodan扫描发现，目前约有2600个公开暴露的实例可能存在漏洞，主要分布在中国、美国、印度尼西亚、德国和香港。

https://www.bleepingcomputer.com/news/security/critical-nginx-ui-auth-bypass-flaw-now-actively-exploited-in-the-wild/

**2. 新型恶意软件AgingFly正攻击政府与医院**

4月15日，一种名为“AgingFly”的新型恶意软件家族正被用于攻击地方政府、医院乃至国防部队成员，该软件专门从基于Chromium的浏览器和Windows版WhatsApp中窃取身份验证数据。CERT-UA已将攻击行动归因于其追踪的网络威胁集群UAC-0247。攻击链始于目标收到伪装成人道主义援助的电子邮件，诱导点击嵌入链接，该链接会重定向到因跨站脚本（XSS）漏洞遭入侵的合法网站，或使用AI工具生成的虚假网站。随后，受害者收到包含快捷方式文件（LNK）的归档文件，该文件启动内置的HTA处理程序，连接远程资源检索并执行HTA文件。HTA显示诱饵表单以分散注意力，同时创建计划任务下载并运行EXE有效载荷，将shellcode注入合法进程。接着攻击者部署两阶段加载器，最终有效载荷经压缩和加密后释放。典型的TCP反向shell或类似RAVENSHELL的工具被用作跳板，建立与管理服务器的TCP连接，使用XOR密码加密的TCP通道与C2服务器通信，通过Windows命令提示符执行命令。之后AgingFly被交付部署，同时利用PowerShell脚本（SILENTLOOP）执行命令、更新配置并从Telegram频道获取C2地址。

https://www.bleepingcomputer.com/news/security/new-agingfly-malware-used-in-attacks-on-ukraine-govt-hospitals/

**3. EssentialPlugin三十余款插件遭后门入侵**

4月15日，EssentialPlugin软件包中的30多款WordPress插件已被恶意代码入侵，攻击者可在未经授权的情况下访问并控制运行这些插件的网站。该事件由托管WordPress主机提供商Anchor Hosting的创始人Austin Ginder发现，他在收到某插件包含允许第三方访问代码的线索后展开调查，结果显示：自2025年8月该项目被新东家以六位数价格收购以来，EssentialPlugin软件包中的所有插件均存在后门。后门最初处于不活动状态，直到近期才被激活，它静默连接外部基础设施获取一个名为“wp-comments-posts.php”的文件，进而将恶意软件注入核心配置文件“wp-config.php”。该恶意软件对网站所有者不可见，并利用基于以太坊的C2地址解析进行规避，可根据指令获取垃圾链接、重定向和虚假页面。WordPress.org迅速响应，关闭了相关插件并强制网站更新，以切断后门通信并禁用其执行路径。建议使用受影响插件的网站管理员立即检查并手动清理配置文件中的恶意代码。

https://www.bleepingcomputer.com/news/security/wordpress-plugin-suite-hacked-to-push-malware-to-thousands-of-sites/

**4. Mirax恶意软件攻击活动波及22万账户**

4月15日，一种名为Mirax的新型安卓远程访问木马（RAT）正通过Meta平台（Facebook和Instagram）上的广告大规模传播，主要针对西班牙语用户，目前已有超过22万个账户被感染。该恶意软件不仅允许攻击者实时完全控制受感染设备，还能将设备转化为SOCKS5代理节点，通过受害者的IP地址路由恶意流量。Mirax以恶意软件即服务（MaaS）形式出售，但采用高度管控的独家分发模式，仅限少数联盟成员访问，这标志着移动威胁正从广泛的MaaS向更隐蔽的“私有MaaS”演变。自2025年12月19日起，Mirax开始在地下论坛公开推广，Cleafy威胁情报团队自2026年3月起对其进行积极监控。攻击通过多阶段营销活动实施，利用Meta广告诱骗用户下载恶意应用程序。受害者被重定向到提供虚假服务（如非法体育直播应用）的钓鱼网站，利用用户侧载APK文件的习惯进行攻击。恶意软件通过托管在GitHub Releases上的投放器传播，这些投放器频繁更新和重新打包以绕过安全检查。安装后，投放器解压有效载荷并应用强混淆技术，通过WebSocket建立连接。

https://securityaffairs.com/190842/uncategorized/mirax-malware-campaign-hits-220k-accounts-enables-full-remote-control.html

**5. CISA更新KEV目录：新增SharePoint及Excel漏洞**

4月15日，美国网络安全和基础设施安全局（CISA）近日将影响Microsoft SharePoint Server和Microsoft Office Excel的漏洞添加到其已知可利用漏洞（KEV）目录中，要求联邦机构在2026年4月28日前完成修复。其中，编号为CVE-2009-0238（CVSS评分9.3）的漏洞影响多个版本的Microsoft Excel及相关查看器。当用户打开特制的Excel文件时，该漏洞会导致应用程序访问内存中的无效对象，造成内存损坏，从而使远程攻击者能够以当前用户权限在受影响系统上执行任意代码。该漏洞早在2009年2月就被积极利用，特别是通过Trojan.Mdropper.AC恶意软件传播，是当时重大现实威胁之一。第二个被加入目录的漏洞编号为CVE-2026-32201（CVSS评分6.5），涉及Microsoft SharePoint Server中的欺骗漏洞，可能与跨站脚本攻击（XSS）相关。微软报告称该零日漏洞已被积极用于实际攻击中。安全公告指出，SharePoint中不正确的输入验证允许未经授权的攻击者通过网络执行欺骗操作，成功利用后可查看部分敏感信息，或更改已披露信息。

https://securityaffairs.com/190852/hacking/u-s-cisa-adds-microsoft-sharepoint-server-and-microsoft-office-excel-flaws-to-its-known-exploited-vulnerabilities-catalog.html

**6. CISA警告Windows任务主机权限提升漏洞正被利用**

4月15日，美国网络安全和基础设施安全局（CISA）近日发出警告，要求美国政府机构尽快保护其系统免受Windows任务主机权限提升漏洞（CVE-2025-60710）的侵害。该漏洞允许本地攻击者在仅具备基本用户权限的情况下，通过低复杂度的攻击方式获得SYSTEM权限，从而完全控制受感染的设备。任务主机是Windows系统的核心组件，作为基于DLL的进程的容器，允许它们在后台运行，并确保在关机期间正确关闭以防止数据损坏。该漏洞源于影响Windows 11和Windows Server 2025设备的链接跟踪弱点，具体表现为Windows任务主机进程在文件访问之前的链接解析不当，导致授权攻击者能够在本地提升权限。微软已于2025年11月发布了针对该漏洞的安全更新。本周一，CISA将CVE-2025-60710正式列入其“已知可利用漏洞”（KEV）目录。根据2021年11月发布的具有约束力的操作指令（BOD）22-01，联邦民事行政部门（FCEB）机构被给予两周时间来完成漏洞修复，以保护其网络免受攻击。

https://www.bleepingcomputer.com/news/security/cisa-flags-windows-task-host-vulnerability-as-exploited-in-attacks/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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