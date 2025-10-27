---
title: 伊朗黑客盯上核安全专家，短短一周内将Windows感染链移植到了Mac
url: https://www.4hou.com/posts/PKrA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-20
fetch_date: 2025-10-04T11:53:20.411406
---

# 伊朗黑客盯上核安全专家，短短一周内将Windows感染链移植到了Mac

伊朗黑客盯上核安全专家，短短一周内将Windows感染链移植到了Mac - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 伊朗黑客盯上核安全专家，短短一周内将Windows感染链移植到了Mac

布加迪
[新闻](https://www.4hou.com/category/news)
2023-07-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)354987

收藏

导语：最新研究表明，政府撑腰的威胁分子具有的水平和能力足以攻击不同目标。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689730524147221.png "1689108348192261.png")

新的研究表明，威胁分子可以灵活地快速迭代攻击模式，以绕过安全控制措施。

安全公司Proofpoint对最近一起针对美国一家智库的核安全专家的攻击进行了调查，揭示了资源丰富的攻击者如何迅速改变花招以攻击不同的机器。

在意识到最初的攻击载荷无法在Mac上奏效后，威胁分子迅速转而采用已知攻击使用苹果硬件的目标奏效的新技术。

在这起复杂的行动中，技术娴熟的威胁分子针对一个重要目标设计了一条看似无害的电子邮件链，并在数周内保持联络，以建立信任和融洽关系，然后趁机发动进一步的攻击。

**攻击是如何发生的？**

2023年5月中旬的攻击来自TA453，这是一伙与伊朗政府有关联的威胁分子，被称为Charming Kitten（迷人小猫）、APT42、Mint Sandstorm和Yellow Garuda，他们冒充皇家联合军种研究所（RUSI）的成员。

这伙以从事间谍活动出名的攻击者利用多角色手法，向目标发送了一条电子邮件链，似乎要求收件人就一个名为“全球安全背景下的伊朗”项目给予反馈。

攻击者从不同的账户发送了多封邮件，所有邮件都相互引用参照，以营造一种真实感——这是在以前的电子邮件劫持活动中看到的一种技术。

在一次看似无害的交互之后，恶意的Google Script宏被投递，旨在将目标引到Dropbox URL。这个URL托管了一个由密码加密的.rar文件，该文件含有一个伪装成PDF但实际上是Windows LNK文件的释放器（dropper）。

自去年微软默认屏蔽VBA宏以来，使用LNK文件一直是网络攻击的标志。多年来，利用VBA宏一直是使用恶意制作的Microsoft 365文件安装恶意软件的首选方法。

Proofpoint表示：“使用.rar和LNK文件部署恶意软件有别于TA453使用VBA宏或远程模板注入的典型感染链。”

“RAR中含有的LNK使用PowerShell从云托管提供商那里下载额外阶段的载荷。”

然而，目标使用的是苹果电脑，这意味着投递的文件无法运行。它试图投递的文件是一个刚被识别出来的基于PowerShell的后门，名为GorjolEcho。

一旦意识到GorjolEcho无法在macOS上运行，TA453随即转向在稍后的日期重新启动攻击，使用可以在苹果硬件上运行的移植版后门。

攻击者继续与目标进行看似正常的电子邮件对话，大约在最初企图基于Windows进行攻击一周后，他们用移植到苹果系统的后门重新发起了攻击。

在这种情况下，恶意软件通过一个由密码保护的ZIP文件来投递，该文件伪装成RUSI VPN解决方案和共享驱动器。

在与威胁分子进行一番交互之后，用户会被说服打开该文件。然后，一系列bash脚本将安装名为NokNok的后门。

Proofpoint判断，这是为了充当进一步指令的立足点，几乎可以肯定是PowerShell后门的移植版。

这起事件提醒人们，威胁分子的适应能力很强。在这个例子中，被发送的是LNK文件，而不是带有宏的Microsoft Word文档，并在机会出现时迅速移植到了macOS。

**Mac恶意软件现状**

随着苹果硬件在企业中越来越受欢迎，它也相应成为了更多威胁分子的目标。

尽管如此，据苹果管理专业公司Jamf声称，2022年新的恶意软件感染数量有所下降。

Malwarebytes在其2023年恶意软件现状报告中特别指出，虽然Mac恶意软件很少见，但确实存在。检测事件的机器中有11%被恶意软件感染。

然而，Jamf的组合策略副总裁Michael Covington表示，2023年是苹果安全界非常活跃的时期。

他说：“今年上半年，我们看到威胁领域出现了一些值得注意的动向，表明针对苹果设备的攻击在强度和目的方面都在发生变化。”

“在此期间，我们看到了第一起专门针对macOS构建的勒索软件的真实例子。我们还看到了新的恶意软件在传播，它们可以追溯到政府撑腰的攻击者。它们使用了新颖的规避技术来避免检测，并绕过内置的平台保护措施潜伏下来。”

Covington还注意到针对苹果处理器的加密货币劫持威胁在增加，而且针对高风险个人（主要是政府和媒体业的那些人）的间谍软件持续演变，但他也赞扬了苹果解决活跃漏洞所做的行动。

他还提醒了易受骗或分心的用户带来的风险，尤其是在网络钓鱼攻击方面。

Proofpoint的研究证明了威胁分子的适应能力、他们响应环境变化的能力以及不断发展的威胁领域。

Proofpoint的Joshua Miller说：“TA453能够并且愿意将资源投入到攻击目标的新工具，体现了与政府有关联的网络威胁持续存在。”

“威胁分子不断努力迭代其感染链以绕过安全控制措施，表明基于强大社区的防御对于挫败最先进的对手有多么重要。”

本文翻译自：https://www.itpro.com/security/cyber-attacks/iranian-hackers-targeted-nuclear-expert-ported-windows-infection-chain-to-mac-in-a-week如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fmNehtlo)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)