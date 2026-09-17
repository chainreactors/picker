---
title: 安全简讯（2026.09.16）
url: https://mp.weixin.qq.com/s/jAyxGfGkgRXR6YSeeMvWtg
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:56:28.136245
---

# 安全简讯（2026.09.16）

# 安全简讯（2026.09.16）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**1. 思科安全邮件网关零日漏洞遭实际利用**

9月15日，思科周一警告客户，影响安全电子邮件网关设备的零日漏洞已被实际利用。该漏洞被识别为CVE-2026-76461，CVSS评分为9.8。思科将其描述为AsyncOS软件中的一个电子邮件解析问题，攻击者可以远程利用该漏洞，无需身份验证即可在底层操作系统上以root权限执行任意命令。这家科技巨头解释说，攻击者可以利用这个严重漏洞，通过在精心构造的电子邮件中向目标用户发送恶意SQL语句来执行这些语句。思科表示，其产品安全应急响应小组（PSIRT）于2026年9月发现了CVE-2026-76461漏洞，但并未透露有关该零日漏洞攻击的细节，目前尚不清楚幕后黑手是谁。该公司已发布入侵指标（IoC），但指出由于威胁行为者可以获得设备上的root权限，因此他们可以删除或隐藏IoC来掩盖其踪迹。该安全漏洞会影响任何配置下的安全电子邮件网关的物理版本和虚拟版本，安全电子邮件和Web管理器以及安全Web设备不受影响。

https://www.securityweek.com/root-rce-zero-day-in-cisco-secure-email-gateway-under-active-exploitation/

**2. Telegram桌面版HTML导出功能曝存储型XSS漏洞**

9月15日，Telegram Desktop的HTML导出功能存在存储型跨站脚本漏洞。攻击者可通过机器人内联键盘按钮，在聊天记录中植入不可见JavaScript代码，潜伏数月，待用户导出记录并用浏览器打开HTML文件时执行。攻击者无需加入目标聊天，转发消息即可传播。问题根源在于导出时键盘按钮文本未经清理直接写入HTML，导致标签被当作真实标记执行。触发后，注入代码可读取消息、发件人、时间戳等元数据并发送至攻击者服务器，还可获取文件本地路径、篡改页面内容。该漏洞已存在两年多，2024年2月引入，3月进入稳定版4.15.1。研究人员6月3日报告后，Telegram于2026年6月修复，首个稳定修复版为7.0.1，7月14日发布。但更新客户端无法修复旧版导出的HTML文件，恶意代码仍可执行，对留存记录用于合规或调查的组织构成风险。建议更新后重新生成导出文件，将旧HTML文件视为不可信。

https://securityaffairs.com/199076/security/telegram-desktop-flaw-could-turn-old-chat-exports-into-data-theft-traps.html

**3. CenterPoint Energy 749万客户信息被窃**

9月15日，休斯顿公用事业公司CenterPoint Energy近日披露了一起数据泄露事件，部分客户的个人信息遭到泄露。事件起因于一名使用别名“4d722e4d656f77”的网络威胁者在网上发帖，声称从该公司窃取了749万条客户记录，内容包括姓名、电话号码、服务和账单地址、账号、账单金额以及部分社会保障号码。该威胁者表示，因公司无视其信息、将其当作笑话，遂决定泄露数据。据其称，攻击方式是通过遍历CenterPoint公共API上的数百万个ID来窃取数据，而该API缺乏速率限制、Web应用程序防火墙保护及其他防止自动访问的安全措施。CenterPoint Energy在提交给美国证券交易委员会的文件中证实数据被盗，但未透露威胁行为者身份、受影响客户数量及被泄露数据的具体类型。公司表示，调查仍在进行中，已确定未经授权的第三方通过公司面向外部的系统获取了部分客户的个人信息，正继续与第三方专家合作以确定事件影响范围，并打算按照适用法律要求通知受影响的客户和监管机构。

https://www.bleepingcomputer.com/news/security/centerpoint-energy-confirms-customer-data-stolen-in-cyberattack/

**4. BambooToken利用MQTT协议攻击多国系统**

9月15日，网络安全研究人员披露，代号BambooToken的恶意软件利用MQTT协议控制Windows和Linux系统，至少自2023年2月起活跃，攻击亚洲和南美洲组织机构，最近一次检测在2026年7月。Lumen Black Lotus Labs于2026年初在VirusTotal上发现该恶意软件，认为出自技术高超且此前未被发现的攻击者，初始访问途径尚未确定。攻击者使用Tendyron公司的“OnKey”软件将恶意软件侧载到目标机器。Tendyron生产用于高安全环境验证身份的硬件令牌，其PKI USB令牌流通量达1.9亿枚。尽管其代码签名证书和构建环境未遭破坏，但攻击者疑似利用易受DLL侧加载攻击的二进制文件触发攻击。早期BambooToken通过.DAT文件提取C2地址，失败则回退到硬编码地址。后续版本侧载恶意DLL文件“OnKeyToken\_KEB.dll”，由Tendyron OnKeySrv程序进入MQTT通信循环。截至2025年12月，攻击范围已扩大至Linux主机。该恶意软件能收集广泛主机信息，并提供Windows防病毒插件，使用WMI框架收集已安装防病毒产品详情并泄露至C2服务器，相关域名使用Cloudflare代理。

https://thehackernews.com/2026/09/bambootoken-malware-uses-mqtt-to.html

**5. HBO Max官方账号遭黑客入侵用于恶意广告攻击**

9月15日，黑客入侵Reddit上的HBO Max官方账号，利用其发起恶意广告活动，跳转至ClickFix着陆页。48小时内，攻击者通过五个诱饵组推送108个恶意广告，作为PasteSwitch活动的一部分。攻击者利用已验证的u/hbomax账户，针对macOS和Windows用户推广并不存在的HBO Max原生macOS应用。点击广告引导用户至模仿HBO Max官网的hbomaxx[.]us，其下载按钮打开ClickFix提示框，诱导用户复制命令并在终端运行，从而将执行权限转移至可信系统实用程序。在macOS上，攻击依靠curl | zsh传播MacSync、AMOS Helper、虚假钱包应用等恶意软件，窃取凭据、消息、浏览器及加密货币钱包信息并获得持久访问权限。在Windows上，则利用MSHTA和PowerShell传播Amatera Stealer并实现持久化，该恶意软件通过伪造Facebook连接绕过网络遥测，隐藏C&C通信。PasteSwitch还使用AnimateClipper和ZigClipper作为剪贴板替换工具，在用户交易时交换加密货币地址。剪贴板窃取者使用托管在区块链上的C&C服务器，该基础设施可能一年多前已搭建。

https://www.securityweek.com/hacked-hbo-reddit-account-used-for-malware-delivery-via-clickfix-attack/

**6. CISA警告勒索团伙利用VMware vCenter漏洞**

9月15日，美国网络安全和基础设施安全局（CISA）警告安全团队，勒索软件团伙现已加入正在进行的攻击，利用VMware vCenter的一个关键漏洞，该漏洞已于7月份得到修复。博通公司于7月29日解决了该安全漏洞（编号CVE-2026-59310），并将其描述为vCenter Syslog服务器中的一个严重目录遍历漏洞，未经身份验证的攻击者可以利用该漏洞执行任意代码。该公司当时在补充常见问题解答中警告客户，将修复该漏洞视为紧急情况并尽快安装补丁。两周后，数字取证和事件响应公司QUIRSO报告称，在疑似高级持续性威胁攻击者开始利用该漏洞部署反向SSH工具以实现持久性和远程访问后，发现47个国家/地区的361个IP地址遭到入侵。几天后，CISA将CVE-2026-59310添加到其已知利用漏洞目录中，并命令政府机构在三天内保护其vCenter系统。周末期间，CISA再次更新KEV目录，将该安全漏洞标记为勒索软件团伙正在积极利用的漏洞。

https://www.bleepingcomputer.com/news/security/cisa-critical-vmware-vcenter-rce-flaw-now-exploited-by-ransomware-gangs/

预览时标签不可点

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