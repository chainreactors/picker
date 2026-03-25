---
title: 微软警告：IRS 钓鱼邮件波及 2.9 万用户，远程管理工具成攻击新载体
url: https://hackernews.cc/archives/63943
source: HackerNews
date: 2026-03-24
fetch_date: 2026-03-25T04:16:18.581411
---

# 微软警告：IRS 钓鱼邮件波及 2.9 万用户，远程管理工具成攻击新载体

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-恶意代码](https://hackernews.cc/wp-content/uploads/2025/08/matrix-5028059_640.jpg)

# 微软警告：IRS 钓鱼邮件波及 2.9 万用户，远程管理工具成攻击新载体

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-03-24](https://hackernews.cc/archives/63943 "10:36")
分类: [网络钓鱼](https://hackernews.cc/archives/category/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)
[暂无评论](https://hackernews.cc/archives/63943#respond)

* 浏览次数 177
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

微软近日发出警告，新型网络攻击正利用美国即将到来的报税季，大肆窃取用户凭证并传播恶意软件。

攻击者抓住报税邮件的紧迫性和时效性特点，发送伪装成退税通知、工资单、报税提醒及税务专业人士请求的钓鱼邮件，诱骗收件人打开恶意附件、扫描二维码或点击可疑链接。

微软威胁情报团队与Defender安全研究团队在上周发布的报告中指出：”多数攻击针对个人用户窃取财务信息，但部分攻击专门瞄准会计师等专业人士——这类人群掌握敏感文件、拥有财务数据访问权限，且习惯在报税季接收税务相关邮件。”

部分攻击将用户导向通过”钓鱼即服务”（PhaaS）平台搭建的虚假页面，另一些则直接部署合法的远程监控管理工具（RMM），如ConnectWise ScreenConnect、Datto和SimpleHelp，使攻击者得以长期控制受害设备。

**主要攻击手法包括：**

* **会计师诱饵**：利用注册会计师（CPA）名义，通过Energy365钓鱼工具包发送钓鱼页面窃取邮箱密码。该工具包日均发送数十万封恶意邮件。
* **二维码与W2表单诱饵**：针对约100家机构，主要为美国制造业、零售业和医疗行业，诱导用户访问仿冒Microsoft 365登录页面的钓鱼网站。该页面使用SneakyLog（又名Kratos）PhaaS平台搭建，专门窃取用户凭证和双因素认证（2FA）码。
* **税务主题域名**：以获取更新版税务表格为幌子，诱骗用户点击虚假链接，实则分发ScreenConnect。
* **IRS加密货币诱饵**：冒充美国国税局（IRS），针对美国高等教育 sector，诱导收件人通过恶意域名（”irs-doc[.]com”或”gov-irs216[.]net”）下载”加密货币税表1099″，进而部署ScreenConnect或SimpleHelp。
* **会计师定向攻击**：以帮助报税为由，发送恶意链接诱导安装Datto。

微软披露，2026年2月10日监测到一场大规模钓鱼攻击，波及超过1万家机构的2.9万名用户。约95%的目标位于美国，涵盖金融服务（19%）、科技与软件（18%）、零售与消费品（15%）等行业。

“邮件冒充IRS，声称收件人的电子报税识别号（EFIN）存在异常报税记录，诱导其下载所谓的’IRS转录查看器’进行核实。”

这些通过亚马逊简单邮件服务（SES）发送的邮件包含”下载IRS转录查看器5.1″按钮，点击后跳转至smartvault[.]im——一个伪装成知名文档管理平台SmartVault的域名。

该钓鱼网站利用Cloudflare拦截机器人和自动扫描工具，确保仅向真实用户投放主要载荷：经过恶意打包的ScreenConnect，使攻击者远程访问系统，实施数据窃取、凭证收集及后续渗透活动。

**防护建议**：组织应强制所有用户启用2FA，实施条件访问策略，监控扫描 incoming 邮件和访问网站，并封禁恶意域名。

与此同时，安全研究人员还发现多起远程访问木马和数据窃取攻击活动：

* **虚假视频会议**：伪造Google Meet和Zoom页面，以软件更新名义推送合法员工监控平台Teramind。
* **Avast退款诈骗**：利用仿冒Avast品牌的欺诈网站，骗取法语用户完整信用卡信息。
* **山寨Telegram**：通过仿冒官网（”telegrgam[.]com”）分发木马安装包，植入DLL启动内存载荷，建立持久化访问。
* **滥用Azure Monitor**：利用微软Azure监控告警通知发送 callback 钓鱼邮件，嵌入虚假账单和攻击者控制的客服电话，从 legitimate 地址azure-noreply@microsoft.com发送钓鱼信息。
* **报价单诱饵**：通过钓鱼邮件投递JavaScript下载器，连接外部服务器下载PowerShell脚本，启动受信任的微软程序”Aspnet\_compiler.exe”并注入XWorm 7.1载荷。类似手法也被用于触发无文件Remcos远控木马感染链。
* **ClickFix伎俩**：结合钓鱼邮件和ClickFix手段投递NetSupport远控木马，窃取数据并部署更多恶意软件。
* **滥用微软应用注册重定向URI**：在钓鱼邮件中利用”login.microsoftonline[.]com”滥用信任关系、绕过垃圾邮件过滤，重定向至窃取凭证和2FA码的钓鱼网站。
* **多厂商链接重写链**：滥用Avanan、Barracuda、Bitdefender、Cisco、INKY、Mimecast、Proofpoint、Sophos和Trend Micro等合法URL重写服务，嵌套多层重写链接隐藏恶意URL，大幅增加安全平台追踪难度。
* **恶意ZIP文件**：伪装成AI图像生成器、变声工具、股票交易软件、游戏模组、VPN和模拟器等，投递Salat窃密木马或MeshAgent，并捆绑加密货币挖矿程序。主要瞄准美国、英国、印度、巴西、法国、加拿大和澳大利亚用户。
* **数字邀请函**：通过钓鱼邮件发送虚假Cloudflare验证码页面，投递VBScript运行PowerShell代码，从Google Drive获取名为SILENTCONNECT的隐蔽.NET加载器，最终部署ScreenConnect。

据Huntress最新报告，攻击者对RMM工具的采用同比增长277%。

Elastic Security Labs研究员Daniel Stepanic和Salim Bitam指出：”由于这些工具被合法IT部门广泛使用，在企业环境中通常被视为’可信’而被忽视。组织必须保持警惕，审计环境中未经授权的RMM使用情况。”

---

**消息来源：[thehackernews.com](https://thehackernews.com/2026/03/microsoft-warns-irs-phishing-hits-29000.html)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[微软](https://hackernews.cc/archives/tag/%E5%BE%AE%E8%BD%AF)[钓鱼邮件](https://hackernews.cc/archives/tag/%E9%92%93%E9%B1%BC%E9%82%AE%E4%BB%B6)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![生成特定网络漏洞图片 (1)_副本](https://hackernews.cc/wp-content/uploads/2026/03/生成特定网络漏洞图片-1_副本-210x140.png)](https://hackernews.cc/archives/63726 "美国联邦调查局称：网络犯罪分子冒充市政官员窃取许可费用")

##### [美国联邦调查局称：网络犯罪分子冒充市政官员窃取许可费用...](https://hackernews.cc/archives/63726 "美国联邦调查局称：网络犯罪分子冒充市政官员窃取许可费用")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-11

[![恶意软件 病毒](https://hackernews.cc/wp-content/uploads/2024/03/恶意软件-病毒-210x140.jpg)](https://hackernews.cc/archives/63592 "微软 Teams 钓鱼攻击以企业员工为目标，投放 A0Backdoor 后门恶意软件")

##### [微软 Teams 钓鱼攻击以企业员工为目标，投放 A0Backdoor 后门恶意...](https://hackernews.cc/archives/63592 "微软 Teams 钓鱼攻击以企业员工为目标，投放 A0Backdoor 后门恶意软件")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-10

[![stocksnap-laptop-2620118_1920](https://hackernews.cc/wp-content/uploads/2026/02/stocksnap-laptop-2620118_1920-210x140.jpg)](https://hackernews.cc/archives/62974 "首个恶意 Outlook 插件被发现 窃取超 4000 条微软用户凭据")

##### [首个恶意 Outlook 插件被发现 窃取超 4000 条微软用户凭据](https://hackernews.cc/archives/62974 "首个恶意 Outlook 插件被发现 窃取超 4000 条微软用户凭据")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-02-12

[![可用 微软](https://hackernews.cc/wp-content/uploads/2026/01/可用-微软-210x140.jpg)](https://hackernews.cc/archives/62411 "微软紧急更新修复在野利用的 Office 零日漏洞")

##### [微软紧急更新修复在野利用的 Office 零日漏洞](https://hackernews.cc/archives/62411 "微软紧急更新修复在野利用的 Office 零日漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-01-27

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team