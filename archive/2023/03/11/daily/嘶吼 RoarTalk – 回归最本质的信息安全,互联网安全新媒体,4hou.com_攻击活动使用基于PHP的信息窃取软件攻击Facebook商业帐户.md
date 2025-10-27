---
title: 攻击活动使用基于PHP的信息窃取软件攻击Facebook商业帐户
url: https://www.4hou.com/posts/506B
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-11
fetch_date: 2025-10-04T09:12:42.651966
---

# 攻击活动使用基于PHP的信息窃取软件攻击Facebook商业帐户

攻击活动使用基于PHP的信息窃取软件攻击Facebook商业帐户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击活动使用基于PHP的信息窃取软件攻击Facebook商业帐户

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)154324

收藏

导语：这伙威胁分子使用恶意软件攻击关键政府基础设施员工、制造公司及其他行业。

![微信截图_20230310105052.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678416617174592.png "1678416617174592.png")

在过去的一年里，一伙攻击者通过恶意谷歌广告或虚假的Facebook个人简档传播窃取信息的恶意软件，从而攻击 Facebook 商业帐户。感染链通过合法应用程序使用 DLL 侧加载手段，还使用用各种编程语言（比如Rust、Python和PHP）编写的独立可执行文件。

安全公司Morphisec的研究人员在一份新报告中称：“我们已经看到SYS01stealer攻击关键政府基础设施员工、制造公司及其他行业。这起活动背后的威胁分子使用谷歌广告和虚假的Facebook个人简档来攻击Facebook商业帐户，这些广告或虚假简档大力宣传游戏、成人内容和破解版软件之类的内容，以引诱受害者下载恶意文件。攻击旨在窃取敏感信息，包括登录数据、cookie以及Facebook广告和商业帐户信息。”

Zscaler的研究人员过去也报告过这起活动，他们将其归因于DUCKTAIL，这个总部位于越南的黑客组织同样专门从事渗入Facebook商业帐户的活动。然而，Morphisec 研究人员认为这起活动并不归因于DUCKTAIL。自2021年以来一直很活跃的DUCKTAIL攻击似乎更具针对性和复杂性，最终目的是滥用与被劫持帐户相关的支付方法，从而在平台上投放广告。

**DLL侧加载变体**

Morphisec研究人员跟踪并分析了可以追溯到2022年5月的几起SYS01stealer攻击，发现逐渐出现了不同的变体。无论是通过Facebook个人简档来分发还是通过恶意广告来分发，几乎所有攻击都离不开一个以游戏、电影、破解版应用程序甚至裸照为幌子的ZIP文件。该文件通常含有作为合法应用程序一部分的可执行文件以及将在该可执行文件运行后加载的恶意DLL。

这种技术名为DLL侧加载或DLL劫持，会影响配置成使用相对路径加载特定DLL的合法应用程序。这意味着应用程序将让Windows API可以搜索DLL，而不是使用绝对路径指定DLL所在的确切位置，而搜索的位置之一将是当前工作目录，即打开可执行文件所在的目录。

这意味着攻击者可以将这种可执行文件与一个DLL一起放置在一个文件夹中——该DLL的名称与应用程序要查找的DLL相似，它们的流氓DLL将被加载到内存中。由于加载由可能经过数字签名、已知不是恶意的合法可执行文件完成，一些安全解决方案可能不会标记DLL。

如果用户起疑心，他们可能会使用VirusTotal之类的服务扫描干净的.exe文件，而不是扫描随附的DLL，尤其是由于它具有隐藏属性，甚至可能不会出现在文件资源管理器中。

在一个攻击变体中，研究人员发现了攻击者滥用WDSyncService.exe，这个可执行文件是存储设备制造商西部数据开发的应用程序WD Sync的一部分。在另一个变体中，攻击者使用了ElevatedInstaller.exe，这是技术公司佳明（Garmin）开发的应用程序。这两个应用程序都存在DLL侧加载漏洞，企图分别加载名为WDSync.dll和vcruntime140.dll的DLL。

**感染链导致SYS01stealer**

恶意DLL是一种恶意软件加载器，可以执行其他隐藏的可执行文件，或从隐藏在同一ZIP压缩包中的.dat或.txt文件提取它们。这些文件使用不同的编程语言（比如Rust或Python）创建，用于设置计划任务、下载诱饵文件，并将它们显示给受害者或提示诱饵错误。

最终的攻击载荷也从指挥和控制（C&C）服务器下载，它始终是使用Inno-Setup创建的安装程序，部署研究人员称为SYS01stealer的木马程序。这个恶意程序用PHP编写，而PHP 通常是一种Web脚本语言，因此它需要执行PHP运行时环境（php.exe）。PHP运行时环境包含在安装程序中，执行的命令是php.exe include.php。

include.php是负责部署计划任务以实现持久隐藏的脚本，加载index.php，里面含有窃取帐户的逻辑代码。该软件包还含有一个名为rhc.exe的文件，用于隐藏已启动程序的窗口和一个Rust可执行文件（有时名为rss.txt），后者的目的是解密基于Chromium的浏览器用于保护会话cookie等敏感网站数据的加密密钥。

SYS01stealer脚本联系指挥和控制服务器，并发送有关受害者的身份识别信息。C&C服务器响应脚本任务。一项名为get\_ck\_all的任务用于从系统上安装的所有基于Chromium的浏览器中提取所有的cookie和登录数据。

研究人员表示，攻击还检查用户是否登录了Facebook帐户。为此，它采取的手段是检查cookie主机名是否含有facebook.com，并收集分别存储用户ID和会话秘密的会话特定cookie：xs和c\_user。

提取的信息然后用于查询Facebook的图形API，并提取有关受害者帐户的所有可用信息，然后将信息上传回C&C服务器。

另一个实现的任务是dlAR，它代表下载和运行。顾名思义，该脚本将从特定的URL下载文件，并使用指定的参数在系统上执行。攻击者似乎通过下载同样使用DLL侧加载的更新版加载器来使用该任务以更新窃取程序，这回是通过滥用西部数据WD Discovery应用程序以及恶意WDLocal.dll。

其他实现的任务名为upload和r，前者用于将指定的本地文件上传回C&C，后者用于通过Windows命令行提示符执行指定的命令，并将结果发布到服务器。

Morphisec的研究人员表示，有助于防止SYS01stealer的基本措施包括实施零信任政策，并限制用户下载和安装程序的权限。而SYS01stealer在本质上依赖采用社会工程伎俩的活动，因此培训用户了解攻击者使用的技巧以便知道如何识破技巧就显得很重要。

本文翻译自：https://www.csoonline.com/article/3689891/attack-campaign-uses-php-based-infostealer-to-target-facebook-business-accounts.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7JJoZpvC)

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