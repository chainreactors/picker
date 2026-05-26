---
title: 安全简讯（2026.05.25）
url: https://mp.weixin.qq.com/s/SanKtb1-_vlWNKBRTblkxQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:04.589308
---

# 安全简讯（2026.05.25）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrxPzX7xn3F3vicXUicXFKjGjFqVqa4MFIFkRbeISXVI1K8mUGibAxRicEm12RVAejpGQsnUOZibib7ndEDQJq0iaGHru4TzK1fpnOSz0I/0?wx_fmt=jpeg)

# 安全简讯（2026.05.25）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. 攻击者利用Ghost CMS高危漏洞注入恶意代码**

5月24日，一场大规模网络攻击活动正利用Ghost内容管理系统（CMS）中的一个严重SQL注入漏洞（CVE-2026-26980），向目标网站注入恶意JavaScript代码，进而触发ClickFix攻击流程。该漏洞影响Ghost 3.24.0至6.19.0版本，允许未经身份验证的攻击者从网站数据库中读取任意数据，包括管理员API密钥。一旦获得该密钥，攻击者便可拥有管理员权限，访问用户、文章和主题，并篡改文章页面。尽管Ghost CMS已在6.19.1版本中于2月19日发布修复补丁，但大量网站未能及时更新，导致漏洞被广泛利用。研究人员发现，此次攻击已影响超过700个域名，受害者包括大学门户网站、人工智能与SaaS公司、媒体机构、金融科技公司、安全网站以及个人博客。令人关注的是，攻击者甚至在哈佛大学、牛津大学、奥本大学和DuckDuckGo等知名机构的网站上植入了恶意代码。研究人员至少观察到两个不同的攻击活动集群，它们会反复感染同一域名，甚至在清理后重新注入脚本，或者互相覆盖对方的恶意代码。

https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/

**2. Laravel Lang包遭篡改，供应链攻击窃取开发者凭证**

5月23日，一场针对Laravel Lang本地化包的供应链攻击正在发生，攻击者通过滥用GitHub版本标签功能，利用Composer包管理器分发恶意代码，使开发者面临复杂的凭证窃取恶意软件威胁。安全公司StepSecurity、Aikido Security和Socket于近日发出警告，称攻击者篡改了Laravel Lang组织维护的四个存储库中的GitHub标签，而非发布全新的恶意版本。这些Laravel Lang软件包是第三方本地化包，并非Laravel官方项目的一部分。此次攻击的特殊之处在于，攻击者并没有修改项目的实际源代码来添加恶意代码，而是滥用了GitHub的一项功能，该功能允许标签指向同一存储库中不同分支的提交。攻击者重写了每个存储库中所有现有的git标签，使其指向一个新的恶意提交，而非发布新的恶意版本。重写操作从laravel-lang/lang开始，到laravel-lang/actions结束，所有四个仓库均使用了相同的伪造作者身份、相同的修改文件和相同的有效载荷行为，这几乎可以肯定是由同一攻击者使用一个被盗用的、具有组织级推送权限的凭证所为。据Aikido称，攻击者入侵了三个存储库中的233个版本，而Socket表示大约700个历史版本可能受到了影响。

https://www.bleepingcomputer.com/news/security/laravel-lang-packages-hijacked-to-deploy-credential-stealing-malware/

**3. 意大利摧毁CINEMAGOAL盗版生态，致3亿欧元损失**

5月23日，意大利当局成功摧毁了一个以CINEMAGOAL应用为核心的庞大盗版生态系统。与典型的IPTV服务提供商不同，CINEMAGOAL采取了更为隐蔽的运作方式，它不进行公开营销，而是通过用户自行安装的应用程序来实现盗版访问。在代号为“Tutto Chiaro”的大规模反盗版行动中，意大利金融警察部队在全国范围内执行了100次搜查，查获了大量有助于识别涉案人员及确定非法所得的关键材料。CINEMAGOAL的运作机制极具技术先进性。该应用直接连接到合法的流媒体平台，使用从国外服务器获取的有效解密代码进行身份验证。系统利用位于意大利境内的虚拟机，每三分钟从合法订阅中捕获有效的身份验证和解密代码，然后重新分发给客户。值得注意的是，这些合法订阅均使用虚假身份信息在Sky、DAZN、Netflix、Disney+和Spotify等平台上开通。与传统的盗版流媒体不同，CINEMAGOAL不仅绕过了平台的安全封锁，还提供了更优质的观看体验，用户直接从原服务观看内容而非接收劣质盗版流，同时系统掩盖了用户的真实IP地址，大大降低了被拦截的可能性。据估计，该盗版生态在其运营期间造成的未付订阅收入损失约为3亿欧元。

https://www.bleepingcomputer.com/news/legal/italy-disrupts-cinemagoal-piracy-app-that-stole-streaming-auth-codes/

**4. 加男子运营200万台设备僵尸网络，遭美加联合逮捕**

5月22日，美国和加拿大当局近日逮捕并指控一名23岁的加拿大男子雅各布·巴特勒（网名“多特”），罪名是运营名为KimWolf的分布式拒绝服务（DDoS）僵尸网络。该僵尸网络规模惊人，感染了全球近200万台设备。巴特勒于周三在渥太华被加拿大当局根据引渡令逮捕，目前正等待被引渡至美国。他面临一项协助和教唆计算机入侵的指控，最高可判处10年监禁。根据阿拉斯加地区公布的刑事诉状，执法部门通过IP地址、在线账户信息、交易记录和在线消息记录，成功将巴特勒与KimWolf僵尸网络联系起来。KimWolf实际上是一个DDoS攻击出租服务平台，被网络犯罪分子用来发起规模空前的攻击，最高攻击流量接近每秒30太比特，是当时公开披露的最大规模DDoS攻击之一。巴特勒采用网络犯罪即服务模式，向客户出售对庞大受控设备网络的访问权限。这些被感染的设备种类繁多，包括数码相框、网络摄像头、基于安卓系统的电视盒和流媒体设备等物联网终端。该僵尸网络被用于对全球计算机和服务器发起超过25,000次攻击，攻击目标甚至包括美国国防部信息网络的IP地址，给部分受害者造成了超过100万美元的经济损失。

https://www.bleepingcomputer.com/news/security/us-and-canada-arrest-and-charge-suspected-kimwolf-botnet-admin/

**5. 趋势科技修复已遭利用的Apex One零日漏洞**

5月22日，日本网络安全软件公司趋势科技已修复了一个针对其Windows版Apex One终端安全平台的零日漏洞，该漏洞已被发现在实际环境中遭到攻击利用。Apex One是趋势科技的企业级终端安全平台，用于保护企业网络免受恶意软件、勒索软件、无文件攻击和基于Web的威胁等多种安全威胁。该漏洞编号为CVE-2026-34926，是一个存在于Apex One本地部署服务器中的目录遍历漏洞，允许具有管理员权限的本地攻击者注入恶意代码。据趋势科技周四披露，该目录遍历漏洞可能允许预先经过身份验证的本地攻击者修改服务器上的密钥表，从而注入恶意代码并将其部署到受影响安装中的代理上。需要说明的是，此漏洞仅可在Apex One的本地部署版本上利用，潜在攻击者必须拥有对Apex One服务器的访问权限，并且已经通过其他方式获得了服务器的管理凭据。尽管成功利用该漏洞的条件相当严格，但趋势科技警告称，其威胁情报系统“TrendAI”已经观察到至少一起在实际环境中利用该漏洞的尝试。鉴于该漏洞已被活跃利用，美国网络安全和基础设施安全局（CISA）于昨日将CVE-2026-34926纳入其正在被利用的漏洞列表，并命令联邦机构在6月4日之前完成设备修补。

https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/

**6. Drupal SQL注入漏洞(CVE-2026-9082)遭大规模利用**

5月24日，美国网络安全和基础设施安全局（CISA）已将Microsoft Exchange Server中的一个漏洞（编号CVE-2026-9082，CVSS评分9.8）添加到其已知利用漏洞（KEV）目录中。该漏洞实际上是Drupal于5月20日发布高度关键安全补丁所针对的SQL注入漏洞，允许未经身份验证的攻击者入侵运行PostgreSQL数据库的网站。漏洞利用几乎在补丁发布后立即开始，48小时内安全公司就追踪到了数千起实际攻击。该漏洞存在于一个旨在清理数据库查询并防止SQL注入的API中。该API的缺陷意味着攻击者可以发送特制请求，向使用PostgreSQL的网站注入任意SQL命令。根据Drupal发布的安全公告，此漏洞允许攻击者导致使用PostgreSQL数据库的网站遭受任意SQL注入攻击，可能导致信息泄露，在某些情况下还会引发权限提升、远程代码执行或其他攻击。更令人担忧的是，匿名用户也可以利用此漏洞。5月22日更新的安全公告确认，风险评分已更新以反映目前已在实际环境中检测到攻击尝试。安全公司Imperva在漏洞披露后的两天内，监测到针对65个国家近6000个Drupal网站的超过15000次攻击尝试。近一半的攻击目标集中在游戏和金融服务机构，这可能是因为这些机构的凭证和财务数据价值较高。

https://securityaffairs.com/192566/uncategorized/u-s-cisa-adds-a-flaw-in-drupal-core-to-its-known-exploited-vulnerabilities-catalog.html

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