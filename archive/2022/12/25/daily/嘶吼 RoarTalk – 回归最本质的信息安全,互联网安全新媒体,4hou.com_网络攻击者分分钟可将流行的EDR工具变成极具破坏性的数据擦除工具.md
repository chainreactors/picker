---
title: 网络攻击者分分钟可将流行的EDR工具变成极具破坏性的数据擦除工具
url: https://www.4hou.com/posts/oJ1Y
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-25
fetch_date: 2025-10-04T02:28:46.656145
---

# 网络攻击者分分钟可将流行的EDR工具变成极具破坏性的数据擦除工具

网络攻击者分分钟可将流行的EDR工具变成极具破坏性的数据擦除工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 网络攻击者分分钟可将流行的EDR工具变成极具破坏性的数据擦除工具

布加迪
[新闻](https://www.4hou.com/category/news)
2022-12-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)336231

收藏

导语：微软及另外三家公司近日发布了补丁，以修复各自产品中导致这种安全隐患的一个漏洞。其他EDR产品也可能受到影响。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671779347148559.png "1670557544472415.png")

许多备受信赖的端点检测和响应（EDR）技术可能存在着一个漏洞，使攻击者得以操控产品，从而删除已安装系统上的几乎所有数据。

Or Yair是SafeBreach的一名安全研究人员，他发现了这个问题。他测试了多家供应商提供的11款EDR工具，发现其中6款工具（共涉及四家供应商）易受攻击。这些易受攻击的产品包括：微软Windows Defender、Windows Defender for Endpoint、趋势科技ApexOne、Avast Antivirus、AVG Antivirus和SentinelOne。

**正式的CVE和补丁**

在Yair于12月7日周三在黑帽欧洲大会上披露这个问题之前，三家供应商已经为这个漏洞赋予了正式的CVE编号，并发布了补丁。

Yair在黑帽欧洲大会上发布了名为Aikido（“合气道”）的概念验证代码，他开发该代码是为了演示数据擦除工具如何在仅仅获得非特权用户权限的情况下，操控一款易受攻击的EDR擦除系统上的几乎任何文件，包括系统文件。Yair在描述其在黑帽大会上的演讲时声称：“我们能够在进行测试的一半以上的EDR和AV产品中利用这些漏洞，包括Windows上的默认端点保护产品。很幸运，我们能在真正的攻击者之前发现这一点，因为一旦这些工具和漏洞落入坏人之手，可能会酿成重大破坏。”他表示，面对成千上万个运行易受该漏洞利用代码攻击的EDR版本的端点，数据擦除工具很有效。

Yair在接受IT安全外媒Dark Reading采访时表示，他在7月至8月期间向几家受影响的供应商报告了该漏洞。他说：“我们在随后的几个月与它们密切合作，在发布该漏洞之前创建了一个修复程序。三家供应商发布了新版本的软件或补丁来解决这个漏洞。”他提到这三家供应商是微软、趋势科技以及Gen（Avast和AVG产品的开发商）。他说：“截至今天，我们还没有收到SentinelOne关于是否正式发布了修复程序的确认。”

Yair称该漏洞与一些EDR工具删除恶意文件的方式有关。这个删除过程中有两个关键事件。一个是EDR检测到某个文件是恶意文件的时间，另一个是实际删除文件的时间，这有时需要重新启动系统。在这两个事件的间歇当中，攻击者有机会使用所谓的NTFS连接点（NTFS junction point），指令EDR删除一个与它确定为恶意的文件不同的文件。

NTFS连接点类似所谓的符号链接，符号链接是指向系统上其他位置的文件夹和文件的快捷方式文件，只不过连接点用于链接系统上不同本地卷上的目录。

**触发问题**

为了在易受攻击的系统上触发这个问题，Yair先创建了一个恶意文件——使用非特权用户的权限，这样EDR就会检测到并试图删除该文件。然后他找到了一个法子，通过让恶意文件保持打开的状态，迫使EDR推迟删除，直止重新启动后再删除。他的下一步操作是在系统上创建一个C:\TEMP\目录，使其连接到另一个目录，然后再做一番手脚，以便当EDR产品试图删除恶意文件时（在重新启动后），它遵循一条完全不同的文件路径。Yair发现，他可以使用同样这一招来删除计算机上不同位置的多个文件，只需要创建一个目录快捷方式，并将指向目标文件的精心设计的路径放在其中，以便EDR产品遵循这些路径。

Yair表示，就一些接受测试的EDR产品而言，他无法任意删除文件，而是可以删除整个文件夹。

该漏洞影响推迟删除恶意文件、直止系统重新启动后删除的EDR工具。在这些情况下，EDR产品将恶意文件的路径存储在某个位置（这个位置因供应商而异），并在重新启动后使用该路径来删除该文件。一些EDR产品并不检查恶意文件的路径在重新启动后是否指向相同的位置，这就就给了攻击者可趁之机，在路径中间插入一个突然的快捷方式。他特别指出，这类漏洞属于名为“检查时间至使用时间“（TOCTOU）漏洞的这一类漏洞。

在大多数情况下，组织可以恢复被删除的文件。因此，让EDR自行删除系统上的文件虽然不好，但并不是最坏的情况。删除其实并不是擦除。为此，Yair设计了“合气道”，这样它可以覆盖已删除的文件，使删除的文件也无法恢复。

Yair开发的漏洞利用工具是一个例子，表明了攻击者用其人之道还治其人之身，就像合气道这门武术一样。EDR工具之类的安全产品在系统上拥有超级用户权限，能够滥用它们的攻击者能够以几乎察觉不到的方式来执行攻击。他把这种做法比作攻击者将以色列著名的“铁穹”导弹防御系统改而变成了一条攻击途径。

本文翻译自：https://www.darkreading.com/vulnerabilities-threats/cyberattackers-popular-edr-tools-destructive-data-wipers如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fsgEhFZs)

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