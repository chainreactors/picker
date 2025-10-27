---
title: 攻击者针对企业传播macOS恶意软件的7种方式
url: https://www.4hou.com/posts/8YRg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:18.433380
---

# 攻击者针对企业传播macOS恶意软件的7种方式

攻击者针对企业传播macOS恶意软件的7种方式 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者针对企业传播macOS恶意软件的7种方式

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-03-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)178844

收藏

导语：sentinelone的研究人员对macOS恶意软件的2022年审查显示，运行macOS终端的企业和用户面临的攻击包括后门和跨平台攻击框架的增加。

sentinelone的研究人员对macOS恶意软件的2022年审查显示，运行macOS终端的企业和用户面临的攻击包括后门和跨平台攻击框架的增加。像CrateDepression和PyMafka这样的攻击使用对包存储库的错别字攻击来攻击用户，而ChromeLoader和oRAT等其他威胁则利用错别字作为攻击载体。

然而，许多其他macOS攻击所使用的攻击载体仍然未知，比如SysJoker（新型恶意软件正对Windows、Linux 和 macOS 操作系统构成威胁,可利用跨平台后门来从事间谍活动）， OSX.Gimmick，CloudMensis、Alchemist和lazarus的Operation In(ter)ception，研究人员在分析中偶然发现了恶意软件，或者在VirusTotal等恶意软件存储库中发现了样本。

**1. 免费内容的诱惑**

有大量的macOS恶意软件通过免费内容下载网站传播，如torrent网站、共享软件网站、破解的应用程序网站或免费的第三方应用程序分发网站。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741782161946.jpeg "1674741782161946.jpeg")

此torrent文件实用程序下载一个广告软件安装程序

内容诱饵包括：

破解软件；

体育直播网站；

vpn、“隐私”广告和地理围栏规避；

电影、电视、游戏和音乐下载网站，DRM规避；

色情和性服务网站。

免费内容诱饵主要用于驱动广告软件和捆绑包（ bundleware）攻击，但像LoudMiner这样的挖矿软件也以这种方式传播。

最常见的情况是向用户提供免费或破解版本的应用程序，用户开始下载一个据称包含该应用程序的磁盘映像文件，但在安装时发现它被称为“Flash Player”、“AdobeFlashPlayer”之类的文件。这些文件通常是无签名的，用户会得到关于如何重写macOS Gatekeeper以启动它们的说明。

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741797150489.jpeg "1674741797150489.jpeg")

破解版Adobe Photoshop的诱饵会导致用户安装恶意程序

如上图所示，这是Finder中的一个简单技巧，即使是非管理员用户也可以使用它来击败Mac内置的安全机制。

最近发现一些攻击者引导终端用户重写其中的Gatekeeper，可能是为了解决组织管理员可能通过MDM（移动设备管理）部署的任何附加安全控制。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741819245688.jpeg "1674741819245688.jpeg")

一些用户开始寻找合法内容，但却被广告和令人难以置信的交易和优惠拉进了恶意网站。不过，Mac用户普遍认为，浏览此类链接本身并不危险，因为他们认为Mac是安全的、不会被病毒攻击。然而，这些网站的性质，以及坚持使用弹出窗口、误导性图标和重定向链接，会迅速将用户从安全的搜索诱导至危险的下载。

虽然“Flash Player”诱饵主要用于广告软件和捆绑软件活动。其他大量利用这一载体的活动包括 OSX.Shlayer,，Pirrit 和 Bundlore。安全供应商可以很好地检测到这些攻击，但苹果内置的基于签名的检测技术XProtect往往会忽略这些攻击。

缓解措施包括：

通过MDM/安全产品的应用程序允许/拒绝列表控制与软件下载/启动相关的权限；

通过MDM解决方案或安全产品限制对终端的访问；

限制或阻止使用安全产品执行未签名代码；

使用终端保护软件防止和检测已知恶意软件。

**2. 向Mac用户发布恶意广告**

恶意网页广告可以在用户的浏览器中运行隐藏代码，将受害者重定向到显示虚假软件更新或病毒扫描警告的弹出窗口的网站。在过去的12个月中，已知的针对macOS用户的恶意广告活动包括ChromeLoader和oRAT。

ChromeLoader也被称为Choziosi Loader或ChromeBack，采用恶意Chrome扩展的形式，劫持用户的搜索引擎查询，安装侦听器拦截传出的浏览器流量，并向受害者提供广告软件。

oRAT是一个用Go编写的后门植入程序，以未签名的磁盘映像（.dmg）的形式下载到受害者的计算机上，伪装成Bitget应用程序的集合。磁盘映像包含一个含有名为Bitget Apps.pkg 的包以及com.adobe.pkg.Bitget传播标识符。

![6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741868164585.jpeg "1674741868164585.jpeg")

加密的数据块被附加到包含配置数据（如C2 IP地址）的恶意二进制文件中。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741886128822.png "1674741886128822.png")

oRAT的加密blob和解密的纯文本

缓解措施包括：

使用防火墙控制和web过滤器阻止对已知恶意网站的访问，在极端敏感的情况下，防火墙只能限制对有限的授权IP的访问；

使用广告拦截软件，广告拦截程序可以阻止大多数广告的显示，但这可能会影响性能和对某些资源的访问；

部署终端保护软件以防止和检测通过恶意广告传播的恶意代码。

**3.对开发者的攻击**

开发者是大规模攻击、供应链攻击、间谍活动和政治操纵等攻击行为的高价值目标。毫无疑问，迄今为止对苹果开发者最成功的攻击是XcodeGhost，这是2015年在中国服务器上托管的苹果Xcode IDE的恶意版本。许多中国开发者选择下载他们认为是Xcode的本地镜像，因为从苹果在美国的服务器下载合法版本非常慢。

XcodeGhost将恶意代码插入到任何使用它构建的iOS应用程序中，许多受攻击的应用程序随后在苹果应用商店发布。受攻击的应用程序能够窃取敏感信息，如设备的唯一标识符和用户的Apple ID，并在受攻击的iOS设备上执行任意代码。

更常见的是，攻击者试图通过共享代码来攻击开发人员。因为开发人员希望通过借助已有成果来提高工作效率，他们通常会寻找共享代码，而不是尝试自己编写复杂或不熟悉的API调用。

在Github等网站上托管的公共存储库中可以找到有用的代码，但这些代码也可能带有恶意软件或代码，从而为攻击者打开攻击后门。XCSSET恶意软件和XcodeSpy都利用共享的Xcode项目危害macOS和iOS软件的开发人员。

在XCSSET中，项目的.xcodeproj/project.xcworkspace/contents.xcworkspace数据被修改为包含对隐藏在项目xcuserdata文件夹中的恶意文件的文件引用。构建该项目导致恶意软件被执行，然后在开发人员的设备上进行多阶段感染，包括后门。

在XcodeSpy中，攻击者在GitHub上发布了一个合法开源项目的篡改版本。项目的构建阶段包括一个模糊的运行脚本，它将在开发人员的构建目标启动时执行。

![8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741910439734.jpeg "1674741910439734.jpeg")

在XcodeSpy示例中发现的模糊脚本

脚本在/private/tmp/.tag 目录下创建了一个隐藏文件，其中包含一个命令：mdbcmd。这反过来又通过反向shell传输到攻击者C2。文件路径链接到VirusTotal上的两个自定义EggShell后门。

在执行时，自定义的EggShell二进制文件会在~/Library/LaunchAgents/com.apple.usgestatistics.plist或~/Liblery/LaunchAgents.com.appstore.checkupdate.plist处放置LaunchAgent。此plist检查原始可执行文件是否正在运行；如果没有，它将从~/Library/Application Support.com/apple.AppStore/.update的‘master’ 版本创建可执行文件的副本，然后执行它。

![9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741926130505.jpeg "1674741926130505.jpeg")

链接到XcodeSpy的EggShell后门使用的持久性代理

缓解措施包括：

将开发环境与运行环境隔离；

要求所有共享开发人员项目在下载或在公司设备上构建之前都要经过审查和授权；

实施安全开发，如安全编码指南、代码审查和代码加密；

教育开发人员使用外部代码的危险；

使用终端保护软件监控可疑和恶意代码的执行。

**4. 开源包存储库**

当攻击者以开放源代码包存储库为目标时，情况开始变得更加严重。通过这些共享的代码在企业中的许多项目中广泛使用，安全审查既薄弱又困难。在不同的平台和语言中有许多应用，包括：

```
Python Package Index (PyPI)Crates.io (Rust)Node Package Manager (NPM)Go Module Index (Go)NuGet Gallery (.NET)RubyGems (Ruby)Packagist (PHP)Chocolatey (Windows)Scoop (Windows)Homebrew (macOS)CocoaPods (Swift, iOS)Carthage (Swift, macOS)Fedora Package Database (Linux)CentOS Package Repository (Linux)Arch Linux User Repository (Linux)Ubuntu Package Repositories (Linux)Alpine Package Repository (Linux)Maven Central (Java)
```

包存储库可能容易受到拼写错误攻击和依赖混淆攻击。在某些情况下，合法软件包的所有权被劫持或转移给开发者。

在2022年5月，一个流行的PyPI包“PyKafka”成为了一个名为“PyMafka”的包的拼写攻击的目标。PyMafka包包含一个Python脚本，用于检查主机并确定操作系统。

![11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741946133787.jpeg "1674741946133787.jpeg")

如果设备运行的是macOS，它会连接到C2，下载一个名为“macOS”的Mach-O二进制文件，并将其写入名为“zad”的/private/var/tmp。二进制文件是upx封装的，且进行了模糊处理，还释放了一个Cobalt Strike信标。

就在不久前，Rust储存库Crates.io也被攻击者盯上了，他们用恶意的“rustdecimal”包来拼写合法的“rust\_decimal”包。后者使用GitLab Continuous Integration（CI）管道环境，并释放了一个Go编写的macOS编译的Poseidon负载。

2022年末，一名自称为“研究员”的攻击者对PyPI上的PyTorch包进行了依赖混淆攻击。

依赖混淆攻击利用了某些包具有托管在私有服务器上的依赖项这一事实。默认情况下，包管理器首先通过搜索公共存储库来处理客户端对依赖项的请求。如果依赖包的名称在公共回收中不存在，攻击者可以将自己的恶意包上传到公共回收中，并拦截来自客户端的请求。

恶意软件在攻击PyTorch时收集并窃取了攻击设备上的各种敏感数据，以传输到远程URL，包括~/.gitconfig/ 和~/.ssh/的内容。

PyTorch是一个流行的Python开源机器学习库，估计已经有大约1.8亿次下载。在圣诞节到元旦期间的5天里，恶意软件包托管在PyPI上，下载量达到了2300次。

缓解措施包括：

针对通过此载体分发的攻击的缓解措施包括许多与防范恶意共享开发人员项目相同的建议。此外，安全团队还可以采纳以下建议:

使用私有存储库并将包管理器配置为不默认为公共存储库；

通过代码签名验证包的真实性；

外部源代码的定期审计和验证；

**5. 木马程序**

对包存储库的攻击可能具有毁灭性和深远的影响，它们将不可避免地被发现并引起大量关注。相比之下，那些希望更隐蔽地向特定目标发送恶意软件的攻击者可能更倾向于对流行应用程序进行木马攻击。

2021年，百度搜索引擎中的赞助链接被用来通过流行的终端应用程序iTerm2的木马版传播恶意软件。进一步调查OSX.Zuru,，该活动还使用了微软Mac远程桌面、Navicat和SecureCRT的木马版本。

这些应用程序在共同设计时使用了不同于合法签名的开发者签名，主要是为了确保它们不会被Gatekeeper屏蔽。除了替换原来的代码签名外，攻击者还在.app/Contents/Frameworks/文件夹中使用名为libcrypt .2.dylib的恶意dylib修改了应用程序包。对该文件的分析揭示了监视本地环境、连接到C2服务器和通过后门执行远程命令的功能。

对木马应用程序的选择很有意思，这表明攻击者针对的是用于远程连接和业务数据库管理的工具的后端用户。

最近，有关的攻击者被发现传播木马化的EAAClient和SecureLink，这些版本提供了一个silver有效载荷。这些木马在没有代码签名的情况下传播，攻击者使用上述技术方法诱导受害者通过终端重置本地安全设置。

![12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230126/1674741969733766.jpeg "1674741969733766.jpeg")

研究人员最近还发现了一种恶意版本的开源工具，旨在窃取受害者的密码和钥匙链，这样攻击者就可以完全访问macOS中所有用户的密码。在此示例中，攻击者使用Resign tool并将其打包到ipa文件中，以便在iOS设备上安装，这表明攻击者显然有意发起攻击。

缓解措施包括：

验证所有代码是否已签名，以及代码签名是否与适当的已知开发人员签名相对应；

限制或阻止使用安全产品执行未签名代码；

使用终端保...