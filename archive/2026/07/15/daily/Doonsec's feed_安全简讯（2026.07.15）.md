---
title: 安全简讯（2026.07.15）
url: https://mp.weixin.qq.com/s/qnX5Jpld_1igRCEA8Qokng
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:54:26.306090
---

# 安全简讯（2026.07.15）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309Zrw1kHicwH2oeCzERo6FV3HiaRG2jSydt5PJ4biaJxfGTXT1caY8gUykyaibZUtWeDcOy822ha8mNsNnnMiaflicicZibtuq3vibYovbK6uA/0?wx_fmt=jpeg)

# 安全简讯（2026.07.15）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Centers Laboratory数据泄露事件影响54万人**

7月13日，美国医疗诊断公司Centers Laboratory近日向政府通报，一起发生在近一年前的数据泄露事件实际影响超过54万人。根据该公司网站发布的通知，这家总部位于新泽西州的检测和实验室服务提供商于2025年8月发现其IT环境遭到入侵，调查显示威胁行为者在8月9日至14日期间获得了对系统的“有限访问权限”，窃取了包括姓名、出生日期、社会保障号码、驾驶执照或身份证号码、护照号码以及健康保险和医疗信息在内的个人及受保护健康信息。美国卫生与公众服务部的数据泄露追踪器显示，此次事件共影响542,377人。该事件被证实与网络犯罪组织WorldLeaks有关，该组织于2025年10月在其网站上公开了Centers Lab的被盗数据，泄露文件超过160万个，总计720GB。

https://www.securityweek.com/centers-laboratory-data-breach-affects-540000-individuals/

**2. CISA将思科16年前CSRF漏洞列入必修修复目录**

7月13日，美国网络安全和基础设施安全局近日将一枚影响Cisco IOS的跨站请求伪造漏洞（编号CVE-2008-4128）纳入其已知被利用漏洞目录，并要求联邦民事行政部门机构在2026年7月13日前完成修复。该漏洞存在于运行Cisco IOS 12.4版本的Cisco 871集成服务路由器的HTTP管理界面中，远程攻击者可通过构造恶意请求，诱骗已通过身份验证的管理员执行任意命令，包括权限提升命令和配置修改命令，从而完全控制目标设备。安全公告指出，攻击路径主要有两条：一是通过访问特定URI执行“show privilege”命令获取权限信息，二是借助特定URI配合“alias exec”命令执行任意配置指令。尽管该漏洞于2008年便被公开披露，距今已逾16年，但其利用条件相对简单，只需诱使已登录的管理员点击恶意链接即可实现设备接管，因此至今仍具有现实威胁。

https://securityaffairs.com/195262/security/u-s-cisa-adds-a-cisco-ios-flaw-to-its-known-exploited-vulnerabilities-catalog.html

**3. 勒索软件借Synopsys窃博世敏感工程数据**

7月13日，勒索软件组织D1R宣称通过入侵美国科技公司Synopsys，窃取了德国工业巨头博世的大量敏感工程数据，引发业界对专有硬件设计泄露的担忧。D1R在其暗网泄露网站上将博世列为受害者，并设置了11天的谈判倒计时，同时公布了数据样本作为佐证。样本中包含一张控制器局域网（CAN）用户手册首页的截图，CAN协议正是博世于1983年自主研发并已成为汽车、航空及工业控制领域广泛采用的行业标准通信协议。更令人担忧的是，攻击者还展示了被盗文件的目录清单，其中包含大量.vhd文件，这类文件通常承载VHDL硬件描述语言源代码，用于通过代码逻辑设计数字电路和芯片。若文件属实，博世在汽车电子、家用电器及工业设备等领域硬件设计的底层技术细节可能面临泄露风险，对竞争对手及硬件安全研究人员而言均具有极高价值。

https://cybernews.com/security/bosch-synopsys-data-breach-claim/

**4. SonicWall SMA1000零日漏洞遭活跃攻击**

7月14日，SonicWall近日发布紧急安全公告，确认威胁行为者正在利用SMA1000系列设备中的两个高危零日漏洞（CVE-2026-15409和CVE-2026-15410）实施主动攻击，并强烈敦促客户立即安装最新热修复版本。其中，CVE-2026-15409为SMA1000设备工作场所接口中的服务器端请求伪造（SSRF）漏洞，CVSS评分达10.0（严重级），允许远程未经身份验证的攻击者强制设备向非预期位置发起请求；CVE-2026-15410则是管理控制台中的身份验证后代码注入漏洞，CVSS评分为7.2（高危级），可令远程经认证的管理员执行任意操作系统命令，尽管该漏洞需要管理员权限，SonicWall仍将其综合风险评为10.0。该公司已调查多起事件并确认两个漏洞均处于被积极利用状态，但尚未透露攻击者是否将二者串联成攻击链。为帮助管理员自查，SonicWall提供了多项入侵指标（IOC）。若发现入侵迹象，公司建议立即重新映像物理设备或重新部署虚拟设备，更换所有用户和管理员密码并重置TOTP令牌。SonicWall明确表示，除安装热修复程序外暂无其他缓解措施可用。

https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-sma1000-flaws-exploited-in-zero-day-attacks-patch-now/

**5. 新型钓鱼工具包Jalisco与OmegaLord强势来袭**

7月14日，近期，网络安全研究人员发现两个分别名为Jalisco和OmegaLord的新型网络钓鱼工具包正被用于针对Microsoft 365账户的大规模攻击，二者均采用了绕过多因素认证（MFA）的先进技术，对企业和个人用户构成严重威胁。其中，Jalisco工具包利用OAuth 2.0设备授权授予流程中的设备代码钓鱼方法，通过社会工程学手段诱骗受害者在合法微软登录页面输入攻击者生成的设备授权码，从而在无需获取用户名和密码的情况下直接授权攻击者控制的设备访问目标账户。该工具包的独特之处在于能够自动实时生成新的Microsoft OAuth设备代码，有效绕过了微软为打击此类攻击而设置的15分钟代码有效期限制，同时为运营者提供管理门户，便于其集中管理捕获的会话和被盗账户。与之相对，OmegaLord则采用更为传统的伪造PDF阅读器登录页面的方式，诱导受害者输入电子邮件地址、密码及关联电话号码，攻击者获取这些信息后可拦截或劫持MFA请求与验证码，从而绕过账户的二次认证保护。

https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/

**6. 虚假GitHub库泛滥，窃密木马借“信任”扩散**

7月14日，近期，网络安全公司Arctic Wolf发现了一场大规模恶意攻击活动：威胁行为者创建了至少292个虚假GitHub代码库，冒充合法的软件和安全项目，利用用户对知名品牌的信任传播信息窃取恶意软件。这些伪造仓库涵盖了安全产品、加密货币服务、金融工具、开发者工具、安全电子邮件提供商、macOS工具及游戏软件等多个热门领域，通过搜索引擎优化和定向引流吸引潜在受害者。每个虚假仓库均包含README文件，内置下载链接将访问者引导至精心设计的恶意着陆页，该页面使用“下载安全内容”等诱人按钮和伪造的信任徽章，所有仿冒品牌共享同一套模板化的HTML/JS代码，客户端脚本通过解析URL路径动态生成看似可信的品牌标识。用户点击下载后，会获得一个约每分钟更改一次名称和载荷的大型ZIP压缩包，内含被植入后门的libcurl.dll文件和一个合法的、已签名的WinGUP更新程序（文件名随冒充产品变化）。当可执行文件运行，gup.exe便会侧载恶意libcurl.dll，后者在内存中解码并反射执行嵌入式信息窃取程序，经分析为BoryptGrab家族的一个变种。

https://www.bleepingcomputer.com/news/security/nearly-300-github-repos-pose-as-legit-software-to-push-malware/

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