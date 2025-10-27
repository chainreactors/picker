---
title: 勒索软件团伙越来越多地使用Skitnet开发后的恶意软件
url: https://www.4hou.com/posts/MXAO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-06
fetch_date: 2025-10-06T22:52:03.091224
---

# 勒索软件团伙越来越多地使用Skitnet开发后的恶意软件

勒索软件团伙越来越多地使用Skitnet开发后的恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件团伙越来越多地使用Skitnet开发后的恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)60576

收藏

导语：Skitnet感染开始于一个基于rust的加载程序，该加载程序在目标系统上卸载并执行，它解密ChaCha20加密的Nim二进制文件并将其加载到内存中。

勒索软件团伙成员越来越多地使用一种名为Skitnet的新型恶意软件，在被入侵的网络上执行秘密活动。

自2024年4月以来，该恶意软件一直在RAMP等地下论坛上出售，但据安全研究人员称，自2025年初以来，它开始在勒索软件团伙中获得显著成绩。

目前，安全研究人员已经观察到其勒索软件成员在攻击中部署了多个勒索软件操作，包括Microsoft Teams针对企业的网络钓鱼攻击中的BlackBasta和Cactus。

![ad(1).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250519/1747637803119452.png "1747637558105518.png")

该恶意软件在地下论坛上进行推广

**隐蔽而强大的后门**

Skitnet感染开始于一个基于rust的加载程序，该加载程序在目标系统上卸载并执行，它解密ChaCha20加密的Nim二进制文件并将其加载到内存中。

Nim有效负载建立一个基于DNS的反向shell，用于与命令和控制（C2）服务器通信，用随机的DNS查询启动会话。

恶意软件启动三个线程，一个用于发送心跳DNS请求，一个用于监视和泄漏shell输出，另一个用于侦听和解密来自DNS响应的命令。

根据Skitnet C2控制面板发出的命令，通过HTTP或DNS发送要执行的通信和命令。C2面板允许操作员查看目标的IP、位置、状态和发出执行命令。

![panel(1).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250519/1747637805127532.png "1747637629635001.png")

Skitnet的管理面板

支持的命令有：

**·**startup -通过下载三个文件（包括恶意DLL）并在startup文件夹中创建合法华硕可执行文件（ISP.exe）的快捷方式来建立持久性。这会触发一个DLL劫持，该劫持执行一个PowerShell脚本（pass .ps1），用于正在进行的C2通信。

**·**Screen-使用PowerShell捕获受害者桌面的屏幕截图，将其上传到Imgur，并将图像URL发送回C2服务器。

**·**Anydesk -下载并静默安装Anydesk，一个合法的远程访问工具，同时隐藏窗口和通知托盘图标。

**·**Rutserv -下载并静默安装另一个合法的远程访问工具Rutserv。

**·**Shell -启动PowerShell命令循环。发送初始的“Shell started..”消息，然后每5秒重复轮询（?m）服务器，以便使用Invoke-Expression执行新命令，并将结果发送回来。

**·**Av -通过查询WMI （SELECT \* FROM AntiVirusProduct在root\SecurityCenter2命名空间中）枚举已安装的防病毒和安全软件，将结果发送到C2服务器。

除了核心命令集之外，操作人员还可以利用涉及。net加载器的单独功能，该功能允许他们在内存中执行PowerShell脚本，以进行更深入的攻击定制。

![netloader.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250519/1747637806217111.png "1747637767195142.png")

Skitnet's .NET加载器

虽然勒索软件组织经常使用针对特定操作的定制工具，并且反病毒检测能力较低，但这些工具的开发成本很高，而且需要熟练的开发人员，而这些开发人员并不总是可用的，尤其是在较低层次的组织中。

使用像Skitnet这样现成的恶意软件更便宜，部署更快，而且由于许多威胁者使用它，可能会使归因更加困难。

在勒索软件领域，两种方法都有空间，甚至是两种方法的混合，但Skitnet的能力使它对黑客特别有吸引力。

文章翻译自：https://www.bleepingcomputer.com/news/security/ransomware-gangs-increasingly-use-skitnet-post-exploitation-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1bxON9PX)

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