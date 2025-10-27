---
title: 如何通过可疑活动检测新威胁？
url: https://www.4hou.com/posts/17gP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:18.097576
---

# 如何通过可疑活动检测新威胁？

如何通过可疑活动检测新威胁？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何通过可疑活动检测新威胁？

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)155938

收藏

导语：本文介绍了如何有效地检测未知威胁的恶意行为。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677237261181723.png "1677237261181723.png")

未知的恶意软件构成了重大的网络安全威胁，可能对组织和个人造成严重损害。如果没有被检测出来，恶意代码就可以访问机密信息、破坏数据，并允许攻击者操控系统。本文介绍了如何避免这些情形，并有效地检测未知的恶意行为。

**检测新威胁面临的挑战**

虽然已知的恶意软件家族更容易预测，也更容易被检测出来，但未知的威胁可能以多种形式呈现，这就给检测它们带来了一系列挑战：

1. 恶意软件开发人员使用多态性，这使他们能够修改恶意代码，以便生成同一种恶意软件的独特变体。

2. 有些恶意软件仍未被识别，也缺少检测它们的任何规则集。

3. 一些威胁可能在一段时间内完全不可检测（FUD），这给边界安全出了难题。

4. 代码常常是经过加密的，因此很难被基于特征的安全解决方案检测出来。

5. 恶意软件的编写者可能使用一种“少量而缓慢”的方法，即在很长一段时间内通过网络发送少量恶意代码，因而加大了检测和拦截的难度。这在企业网络中尤其具有破坏性，因为无法深入了解环境可能导致未被检测出来的恶意活动。

**检测新威胁**

研究人员在分析已知的恶意软件家族时，可以充分利用关于恶意软件的现有信息（比如行为、攻击载荷和已知漏洞），以便检测和响应它。

不过在应对新威胁时，研究人员必须从头开始，使用以下指南：

第1步：使用逆向工程来分析恶意软件的代码，以确定其目的和恶意性质。

第2步：使用静态分析来检查恶意软件的代码，以确定其行为、攻击载荷和漏洞。

第3步：使用动态分析来观察恶意软件在执行期间的行为。

第4步：使用沙盒机制在隔离的环境中运行恶意软件，以观察其行为，又不损害系统。

第5步：使用启发式方法，根据可观察到的模式和行为来识别可能恶意的代码。

第6步：分析逆向工程、静态分析、动态分析、沙盒机制和启发式方法的结果，以确定代码是不是恶意代码。

外头有众多工具可以帮助你完成上面这5个步骤，从Process Monitor、Wireshark到ANY.RUN，不一而足。但如何得出一个准确的结论？在拥有所有这些数据的同时，你又应该注意什么？

答案很简单：关注恶意行为的指标。

**监控可疑活动以实现高效检测**

不同的特征被用来检测威胁。在计算机安全术语中，特征是与计算机网络或系统上的恶意攻击相关联的典型足迹或模式。

这些特征的一部分是行为特征。在操作系统中做了一番手脚而不留下跟踪是不可能做到的。我们可以通过可疑活动来识别是什么软件或脚本。

你可以在沙盒中运行可疑程序，以观察该恶意软件的行为，并识别任何恶意行为，比如：

异常的文件系统活动

可疑的进程创建和终止

异常的网络活动

读取或修改系统文件

访问系统资源

创建新用户

连接到远程服务器

执行其他恶意命令

利用系统中的已知漏洞

微软Office启动了PowerShell，是不是觉得看起来很可疑？一个应用程序将自己添加到计划任务中，一定要注意它。svchost进程在临时注册表中运行，肯定哪里出了岔子。

你总是可以通过行为检测到任何威胁，即使没有特征。

不妨证明一下。

**第一个用例**

这是窃取器的一个样本。它执行什么操作？窃取用户数据、cookie和钱包等。我们如何才能检测它？比如说，当该应用程序打开Chrome浏览器的Login Data（登录数据）文件时，它就会暴露自己。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677237289207794.png "1677237289207794.png")

图1. 窃取器的可疑行为

网络流量中的活动还显露了威胁的恶意意图。合法的应用程序永远不会发送凭据、操作系统特征及本地收集的其他敏感数据。

以流量为例，恶意软件可以通过众所周知的功能检测出来。Agent Tesla在一些情况下并不加密从受感染的系统发送的数据，如该样本所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677237299176776.png "1677237299176776.png")

图2. 网络流量中的可疑活动

**第二个用例**

没有多少合法的程序需要停止Windows Defender或其他应用程序来保护操作系统或者把自己排除在外。每当你遇到这种行为，这是可疑活动的迹象。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677237314129454.png "1677237314129454.png")

图3. 可疑行为

应用程序是否删除影子副本？如果是，看起来像是勒索软件。它是否删除影子副本，并在每个目录中创建带有自述文本的TXT/HTML文件？这是表明它是勒索软件的另一个例子。

如果用户数据在这个过程中被加密，我们基本可以确定它是勒索软件。就像这个恶意例子（https://app.any.run/tasks/39633ba6-7cd7-441a-97f6-9556fc1f0056/?utm\_source=hacker\_news&utm\_medium=article&utm\_campaign=detect\_new\_threats0223&utm\_content=task3）中发生的情况一样，即使我们不知道恶意软件家族，也可以识别出该软件构成什么样的安全威胁，然后见机行事，采取措施来保护工作站和组织的网络。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677237337183417.png "1677237337183417.png")

图4. 勒索软件的可疑行为

根据沙盒中观察到的行为，我们可以对几乎所有类型的恶意软件得出结论。不妨尝试ANY.RUN在线互动服务来监测恶意软件，你可以立即得到初期结果，并实时看到恶意软件的所有活动，这正是我们揪出可疑活动所需要的。

**结语**

网络犯罪分子可以利用未知威胁向企业勒索钱财，并发动大规模网络攻击。即使恶意软件家族没有被检测出来，我们也总是可以通过观察分析其行为来推断威胁的功能。利用这些数据，就可以构建信息安全以防止任何新的威胁。行为分析在不增加成本的情况下增强了应对新型未知威胁的能力，并加强了贵组织的保护。

本文翻译自：https://thehackernews.com/2023/02/how-to-detect-new-threats-via.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?PsyyClsA)

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