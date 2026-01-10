---
title: 安全简讯（2026.01.09）
url: https://mp.weixin.qq.com/s/gi7gXyhaZSO-R7DIjiQFqg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:17.246919
---

# 安全简讯（2026.01.09）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5NPEia9QicL2uqXPJ7KGM2G0mU6E8d5ZQBibndEpYAJyyF80eba0SFVREbPmobXV0V9ZiaZaXibFDSNlFhjz8SRpGcA/0?wx_fmt=jpeg)

# 安全简讯（2026.01.09）

启明星辰安全简讯

![]()

在小说阅读器中沉浸阅读

**1. CISA要求联邦机构紧急修复HPE OneView漏洞**

1月8日，美国网络安全和基础设施安全局（CISA）近日将HPE OneView的CVE-2025-37164漏洞标记为“正在被积极利用”，该漏洞属最高级别风险。HPE OneView是用于集中管理存储、服务器和网络设备的基础架构管理软件，广泛应用于企业IT环境。漏洞由越南安全研究员Nguyen Quoc Khanh（brocked200）发现并报告，HPE于2025年12月中旬发布安全补丁，但漏洞影响v11.00之前的所有OneView版本。CVE-2025-37164允许未经身份验证的威胁行为者通过低复杂度代码注入攻击实现远程代码执行，攻击者无需本地权限即可完全控制受影响系统。HPE在12月16日的警告中强调，该漏洞可能被远程用户利用执行恶意代码，直接威胁企业核心基础设施安全。CISA已将该漏洞纳入“已知被利用漏洞目录”，并依据2021年发布的BOD 22-01指令，要求联邦民事行政部门（FCEB）机构在2026年1月28日前完成系统修复。

https://www.bleepingcomputer.com/news/security/cisa-tags-max-severity-hpe-oneview-flaw-as-actively-exploited/

**2. GoBruteforcer僵尸网络升级暴力破解攻击**

1月7日，一款名为GoBruteforcer的高复杂度Go语言僵尸网络正对全球Linux服务器发起猛烈攻击，通过暴力破解手段尝试获取FTP、MySQL、PostgreSQL及phpMyAdmin等公网暴露服务的弱密码。Check Point Research记录显示，其2025年变种版本技术水平大幅升级，已攻陷数万台服务器，全球超5万台服务器面临风险，涉及570万FTP、223万MySQL及56万PostgreSQL默认端口暴露设备。该僵尸网络采用模块化架构，包含网页后门、下载器、IRC僵尸程序及暴力破解模块。攻击推手主要源于运维人员复用AI生成的服务器配置模板，以及XAMPP等老旧集成环境缺乏加固。其密码列表与1000万条泄露密码数据库重合率达2.44%，基于375-600个弱密码生成变体，结合庞大暴露服务基数形成高经济效益攻击。2025变种完全重构IRC组件为Go语言，使用Garbler工具深度混淆代码，新增进程伪装技术，躲避安全检测。

https://cybersecuritynews.com/gobruteforcer-botnet/

**3. 恶意npm包传播NodeCordRAT恶意软件**

1月8日，网络安全研究人员近日披露了一起针对npm生态的恶意软件传播事件，发现三个由用户"wenmoonx"上传的恶意npm软件包——bitcoin-main-lib（2,300次下载）、bitcoin-lib-js（193次下载）及bip40（970次下载）。截至2025年11月，这些包已被全部下架，但已对开发者社区造成实质性威胁。据分析，前两个恶意包在安装时会执行postinstall.cjs脚本，自动安装包含恶意负载的bip40包。该最终负载被命名为NodeCordRAT，是一种具有数据窃取能力的远程访问木马。其名称源于双重传播特性：利用npm作为初始传播媒介，通过Discord服务器建立命令与控制（C&C）通道。该木马具备多重危害功能：可窃取谷歌Chrome浏览器凭证、API令牌及MetaMask等加密货币钱包的助记词；通过硬编码的Discord服务器接收指令，支持执行任意shell命令、截取桌面屏幕及上传指定文件等操作。数据通过Discord API的/messages端点以附件形式上传至私密频道，形成隐蔽的窃密链路。

https://thehackernews.com/2026/01/whatsapp-worm-spreads-astaroth-banking.html

**4. 巴西WhatsApp用户遭Astaroth木马定向攻击**

1月8日，安克诺斯威胁研究团队近日披露代号"粉红河豚"的新型攻击活动，攻击者以巴西WhatsApp用户为目标，通过该平台传播具有多模块化特性的Astaroth（又名"吉尔达马"）Windows银行木马。该木马自2015年起持续活跃于拉美地区，尤以巴西为重灾区，核心目标为窃取用户数据及银行凭证。攻击链以ZIP压缩包为初始载体，内含伪装成正常文件的VB脚本及MSI安装程序。当受害者解压并执行脚本后，会触发PowerShell/Python脚本下载，启动设备入侵流程。此次攻击的显著特征在于新增的Python语言开发WhatsApp蠕虫模块，该模块可自动收集受害者通讯录，并向全部联系人转发含恶意ZIP的传播消息，形成几何级扩散效应。Astaroth采用模块化架构设计：其核心程序由德尔福语言编写，安装程序依托VB脚本运行，而传播模块则使用Python开发，体现威胁行为者对多语言编程的灵活运用。银行木马模块在后台持续监控用户浏览器活动，当检测到访问银行相关网址时，立即激活并窃取登录凭证，实现经济犯罪目的。

https://thehackernews.com/2026/01/whatsapp-worm-spreads-astaroth-banking.html

**5. 朝鲜Kimsuki利用恶意二维码攻击美国组织**

1月8日，美国联邦调查局近日发布紧急警报，揭露朝鲜官方支持的黑客组织Kimsuki（APT43）正通过恶意二维码发起针对美国组织的鱼叉式网络钓鱼攻击。此次攻击主要瞄准参与朝鲜相关政策、研究和分析的美国机构，包括非政府组织、智库、学术机构、战略咨询公司及政府实体。攻击者通过发送包含恶意二维码的钓鱼邮件，诱使受害者扫描二维码后重定向至伪装成问卷调查、安全驱动器或虚假登录页面的恶意网站。扫描后，受害者设备会被路由至攻击者控制的基础设施，进行设备指纹识别，收集用户代理信息、操作系统、IP地址、屏幕尺寸及本地语言等数据。随后，受害者会看到模仿Microsoft 365、Okta、VPN或Google登录页面的钓鱼页面，最终目的为窃取访问凭证或会话令牌。此类攻击通过移动设备扫描二维码的特性，有效绕过传统电子邮件安全解决方案及多因素身份验证（MFA）。由于攻击源自未受管理的移动设备，处于标准端点检测与响应（EDR）和网络监控之外，被描述为“不受MFA保护的身份入侵向量”。

https://www.bleepingcomputer.com/news/security/fbi-warns-about-kimsuky-hackers-using-qr-codes-to-phish-us-orgs/

**6. 恶意软件加载器pkr\_mtsi可传递多种有效载荷**

1月8日，ReversingLabs（RL）近日披露，一种名为pkr\_mtsi的恶意Windows打包程序自2025年4月24日发现以来持续活跃，成为大规模恶意广告和SEO投毒活动的核心加载器。该工具通过虚假下载网站诱骗用户下载伪装成PuTTY、Rufus、Microsoft Teams等合法软件的木马安装程序，利用付费搜索广告和搜索排名操纵提升曝光率，而非依赖供应商入侵。pkr\_mtsi具备高度灵活性，可部署Oyster、Vidar、Vanguard Stealer、Supper等多种恶意软件家族。其进化轨迹显著：过去八个月内引入更强大的混淆技术、哈希API解析及反分析机制，同时保持“内存分配-小规模写入重建载荷”的稳定执行模型。关键技术特征包括改进的UPX中间级填充、混淆的ZwAllocateVirtualMemory调用、干扰分析的垃圾GDI API调用，以及触发进程终止或无限循环的反调试检查。尽管结构多变，但其重复调用带有无效保护标志的NtProtectVirtualMemory函数产生的可预测错误，为端点遥测监控提供了可靠检测机会。

https://www.infosecurity-magazine.com/news/malware-loader-pkrmtsi-payloads/

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