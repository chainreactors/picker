---
title: PlugX恶意软件隐藏在USB设备上，以感染新的Windows主机
url: https://www.4hou.com/posts/jJoP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-09
fetch_date: 2025-10-04T06:05:21.574925
---

# PlugX恶意软件隐藏在USB设备上，以感染新的Windows主机

PlugX恶意软件隐藏在USB设备上，以感染新的Windows主机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PlugX恶意软件隐藏在USB设备上，以感染新的Windows主机

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)146183

收藏

导语：安全研究人员近日分析了PlugX恶意软件的一个变种，这个变种可以将恶意文件隐藏在可移动USB设备上，然后伺机感染USB设备所连接的Windows主机。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230208/1675819344532784.png "1674954326169347.png")

安全研究人员近日分析了PlugX恶意软件的一个变种，这个变种可以将恶意文件隐藏在可移动USB设备上，然后伺机感染USB设备所连接的Windows主机。

这种恶意软件使用了研究人员所说的“一种新颖技术”，可以让它在较长时间内不被发现，并且有可能传播到严加保护的系统。

派拓网络公司（Palo Alto Network）的Unit 42团队在响应Black Basta勒索软件攻击时发现了这个PlugX变种的样本，而Black Basta勒索软件攻击依赖GootLoader和Brute Ratel后利用（post-exploitation）工具包用于红队攻击活动。

Unit 42团队在寻找类似的样本时还在Virus Total扫描平台上发现了PlugX的一个变种，它可以找到受攻击系统上的敏感文件，并将它们复制到USB驱动器上的一个隐藏文件夹中。

**将PluxX隐藏在USB驱动器中**

PlugX是一种颇有些年头的恶意软件，至少从2008年开始使用，最初只被亚洲的黑客组织使用。如今其中一些黑客组织将其与数字签名软件结合使用，以便侧加载加密的攻击载荷。

然而随着时间的推移，PlugX变得极其广泛，多个威胁组织在攻击中采用了它，因而对其的使用进行追根溯源显得困难重重。

在Unix 42团队观察到的近期攻击中，威胁分子使用了“x64dbg.exe”这个Windows调试工具的32位版本和“x32bridge.dll”被投毒的版本，后者加载PlugX攻击载荷（x32bridge.dat）。![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230208/1675819345943658.png "1674954340190758.png")

图1. 感染链示意图（图片来源：Unit 42团队）

撰写本文时，Virus Total扫描平台上的大多数防病毒引擎都并未将该文件标记为恶意文件，61个产品中只有9个检测出了它。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230208/1675819346654830.png "1674954352107437.png")

图2. VirusTotal扫描结果（图片来源：BleepingComputer.com）

PlugX恶意软件的最近样本被Virus Total上数量更少的防病毒引擎检测出来。其中一个样本（去年8月份添加）目前仅被该平台上的三个产品标记为是威胁。很显然，实时安全代理依赖多种检测技术，这些技术查找由系统上的文件生成的恶意活动。

研究人员解释道，他们遇到的PlugX版本使用Unicode字符在被检测的USB驱动器中创建一个新目录，这使得它们在Windows资源管理器和命令shell中不可见。这些目录在Linux上是可见的，但在Windows系统上隐藏起来。

Unit 42团队称：“恶意软件为了实现从隐藏的目录执行代码，在USB设备的根文件夹上创建了一个Windows快捷方式（.lnk）文件。”

“恶意软件的这个快捷路径含有Unicode空白字符，这是一个不会导致断行，但在通过Windows资源管理器查看时不可见的空格。”

恶意软件在隐藏目录上创建一个“desktop.ini”文件，以指定根文件夹上的LNK文件图标，使其看起来像一个USB驱动器，以欺骗受害者。与此同时，“RECYCLER.BIN”子目录起到了伪装作用，在USB设备上存放恶意软件的副本。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230208/1675819347176951.png "1674954366188127.png")

图3. 快捷方式文件属性（图片来源：Unit 42团队）

Sophos研究人员在2020年底分析PlugX的旧版本时已经目睹了这种技术，不过当时研究的重点是作为执行恶意代码的一种方式的DLL侧加载。

受害者点击USB设备根文件夹上的快捷方式文件，该文件通过cmd.exe执行x32.exe，从而导致主机感染上PlugX恶意软件。

同时，一个新的资源管理器窗口将打开，显示用户在USB设备上的文件，使一切看起来很正常。

在PlugX潜入设备后，它会持续监测新的USB设备，一旦发现它们，就企图感染。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230208/1675819348208883.png "1674954392155972.png")

图4. 干净的USB驱动器与被感染的USB驱动器比较（图片来源：Unit 42团队）

Unit 42团队在研究过程中还发现了PlugX恶意软件同样针对USB驱动器的的窃取文档的变种，但这个变种多了一项本领：可以将PDF和微软Word文档复制到隐藏目录中一个名为da520e5的文件夹。

目前还不清楚这伙威胁分子如何从USB驱动器中获取这些“从本地向外泄露”的文件，但物理访问可能是其中一种手段。

虽然PlugX通常与政府撑腰的威胁分子有关联，但这种恶意软件可以在地下市场上买到，网络犯罪分子也使用过它。

Unit 42团队的研究人员表示，鉴于新的发展动向使PlugX更难被发现，因而得以通过可移动驱动器传播开来，它有可能进入到严加保护的网络。

本文翻译自：https://www.bleepingcomputer.com/news/security/plugx-malware-hides-on-usb-devices-to-infect-new-windows-hosts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?assiuwnc)

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