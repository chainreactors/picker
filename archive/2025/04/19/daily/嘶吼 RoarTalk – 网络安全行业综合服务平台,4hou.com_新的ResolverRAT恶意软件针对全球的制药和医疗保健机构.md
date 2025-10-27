---
title: 新的ResolverRAT恶意软件针对全球的制药和医疗保健机构
url: https://www.4hou.com/posts/QXR9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-19
fetch_date: 2025-10-06T22:04:06.534371
---

# 新的ResolverRAT恶意软件针对全球的制药和医疗保健机构

新的ResolverRAT恶意软件针对全球的制药和医疗保健机构 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的ResolverRAT恶意软件针对全球的制药和医疗保健机构

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-18 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)73209

收藏

导语：ResolverRAT是一个完全在内存中运行的隐形威胁，同时它还滥用 net ‘ resourcerresolve ’事件来加载恶意程序集，而不执行可能被标记为可疑的API调用。

一种名为“ResolverRAT”的新型远程访问木马（RAT）正被用于攻击全球的组织，发现该恶意软件最近被用于针对医疗保健和制药行业的攻击。

ResolverRAT通过网络钓鱼邮件传播，违反法律或版权，根据目标国家的语言量身定制。电子邮件包含下载合法可执行文件（'hpreader.exe'）的链接，该链接利用反射DLL加载将ResolverRAT注入内存。

Morphisec发现了之前未记录的恶意软件，他们指出，Check Point和Cisco Talos最近的报告中也记录了相同的网络钓鱼基础设施。

然而，这些报告强调了Rhadamanthys和Lumma窃取者的分布，未能捕获独特的ResolverRAT有效载荷。

**ResolverRAT功能**

ResolverRAT是一个完全在内存中运行的隐形威胁，同时它还滥用 net ‘ resourcerresolve ’事件来加载恶意程序集，而不执行可能被标记为可疑的API调用。

“这种资源解析器劫持代表了恶意软件的最佳进化——利用一个被忽视的。net机制完全在托管内存中运行，绕过了传统的安全监控，重点是Win32 API和文件系统操作，”Morphisec描述道。

研究人员报告说，ResolverRAT使用复杂的状态机来混淆控制流，使静态分析变得极其困难，通过识别资源请求来检测沙箱和分析工具。

即使它在调试工具的存在下执行，它对误导和冗余代码/操作的使用也会使分析复杂化。

该恶意软件通过在Windows注册表中最多20个位置添加xor混淆键来确保持久性。同时，它还将自己添加到文件系统位置，如“Startup”、“Program Files”和“LocalAppData”。

![registry.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744790109664150.png "1744790015182352.png")

基于注册的持久性

ResolverRAT尝试以随机间隔在计划回调时进行连接，以逃避基于不规则信标模式的检测。

操作员发送的每个命令都在专用线程中处理，在确保失败的命令不会使恶意软件崩溃的同时，启用并行任务执行。

虽然Morphisec没有深入研究ResolverRAT支持的命令，但它提到了数据泄露功能，该功能具有用于大数据传输的分块机制。

具体来说，大于1MB的文件被分成16KB的块，这样可以通过将恶意流量与正常流量混合来逃避检测。

![chunks.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744790110103317.png "1744790074196188.png")

将较大的文件分成小块

在发送每个块之前，ResolverRAT检查套接字是否好写，防止拥塞或网络不稳定导致的错误。该机制具有最佳的错误处理和数据恢复功能，从最后一个成功的块恢复传输。

Morphisec在意大利、捷克、印度、土耳其、葡萄牙和印度尼西亚观察到网络钓鱼攻击，因此该恶意软件具有全球操作范围，可以扩展到更多国家。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-resolverrat-malware-targets-pharma-and-healthcare-orgs-worldwide/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SSDkqzPM)

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