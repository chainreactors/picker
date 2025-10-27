---
title: 假冒 CrowdStrike 使用恶意软件和数据擦除程序修复目标公司
url: https://www.4hou.com/posts/Zg4J
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-30
fetch_date: 2025-10-06T17:41:02.114834
---

# 假冒 CrowdStrike 使用恶意软件和数据擦除程序修复目标公司

假冒 CrowdStrike 使用恶意软件和数据擦除程序修复目标公司 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 假冒 CrowdStrike 使用恶意软件和数据擦除程序修复目标公司

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-29 10:01:45

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)100892

收藏

导语：此次中断的原因是 Windows 主机（7.11 及以上版本）的通道文件（传感器配置）更新触发了逻辑错误，从而导致系统崩溃。

威胁者利用 CrowdStrike 故障更新造成大规模业务中断，利用数据擦除器和远程访问工具攻击公司。随着越来越多企业寻求帮助，要求修复受影响的 Windows 主机，研究人员和政府机构发现试图利用这种情况的网络钓鱼电子邮件有所增加。

**官方渠道沟通**

CrowdStrike 在最新的更新中表示，它“正在积极协助受到近期内容更新影响的客户”，该更新导致全球数百万台 Windows 主机崩溃。

该公司建议客户通过官方渠道验证他们是否与合法代表进行沟通，因为“对手和不良行为者会试图利用此类事件”。

英国国家网络安全中心 (NCSC) 警告称，他们发现旨在利用此次中断的网络钓鱼邮件数量有所增加。自动恶意软件分析平台 AnyRun 也注意到“冒充 CrowdStrike 的尝试有所增加，这可能会导致网络钓鱼”。

**伪装成修复程序和更新的恶意软件**

网络安全研究员 g0njxa 首次报告了针对 BBVA 银行客户的恶意软件活动，该活动提供了安装 Remcos RAT 的虚假 CrowdStrike Hotfix 更新。

该虚假修补程序通过钓鱼网站 portalintranetgrupobbva[.]com 进行推广，该网站伪装成 BBVA 内部网门户。恶意存档中附有说明，告知员工和合作伙伴安装更新，以避免在连接到公司内部网络时出现错误。

“强制更新以避免公司内部网络的连接和同步错误”，西班牙语的“instrucciones.txt”文件写道。AnyRun 也在社交媒体上发布了有关同一活动的推文，他表示，假冒的热修复程序会提供 HijackLoader，然后将 Remcos 远程访问工具投放到受感染的系统上。

![HiJackLoader_CrowdStrike-hotfix.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721635355899409.png "1721635165928445.png")

恶意软件加载程序伪装成 CrowdStrike 的修补程序

在另一个警告中，AnyRun 宣布攻击者正在以提供 CrowdStrike 更新为幌子分发数据擦除器。它通过用零字节覆盖文件来破坏系统，然后通过 #Telegram 报告此内容。

亲伊朗的黑客组织 Handala 声称发动了这次攻击，该组织在 Twitter 上表示，他们冒充 CrowdStrike 向以色列公司发送电子邮件，分发数据擦除器。威胁者冒充 CrowdStrike，通过域名“crowdstrike.com.vc”发送电子邮件，告诉客户他们创建了一个工具来让 Windows 系统恢复在线。

![phishing-email.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721635357111511.png "1721635223176892.png")

Handala 威胁者发送的网络钓鱼电子邮件

这些电子邮件包括一份 PDF，其中包含有关运行虚假更新的进一步说明，以及从文件托管服务下载恶意 ZIP 存档的链接。此 zip 文件包含一个名为“Crowdstrike.exe”的可执行文件。

![malicious-pdf.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240722/1721635359228513.png "1721635268132382.png")

恶意附件推送数据擦除器

一旦执行虚假的 CrowdStrike 更新，数据擦除器就会被提取到 %Temp% 下的文件夹并启动以销毁存储在设备上的数据。

**数百万台 Windows 主机崩溃**

 CrowdStrike 软件更新中的缺陷对众多 Windows 系统产生了巨大影响，这对网络犯罪分子来说是一个不容错过的好机会。

据微软称，此次错误更新“影响了 850 万台 Windows 设备，占所有 Windows 设备的不到 1%”。此次损害发生在 78 分钟内，即 UTC 时间 04:09 至 UTC 时间 05:27 之间。

尽管受影响的系统比例很低，而且 CrowdStrike 也努力迅速解决问题，但影响却十分巨大。计算机崩溃导致数千架航班被取消，金融公司业务中断，医院、媒体组织、铁路瘫痪，甚至影响了紧急服务。

CrowdStrike 在上周六发布的事故分析文章中解释称，此次中断的原因是 Windows 主机（7.11 及以上版本）的通道文件（传感器配置）更新触发了逻辑错误，从而导致系统崩溃。

虽然导致崩溃的通道文件已被确定并且不再导致问题，但仍在努力恢复系统正常运行的公司可以按照 CrowdStrike 的指示来恢复单个主机、BitLocker 密钥和基于云的环境。

文章翻译自：https://www.bleepingcomputer.com/news/security/fake-crowdstrike-fixes-target-companies-with-malware-data-wipers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qarmy0Q8)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

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