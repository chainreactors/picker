---
title: Kimsuky Hackers使用新的自定义RDP包装器进行远程访问
url: https://www.4hou.com/posts/RXXw
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-13
fetch_date: 2025-10-06T20:34:22.064060
---

# Kimsuky Hackers使用新的自定义RDP包装器进行远程访问

Kimsuky Hackers使用新的自定义RDP包装器进行远程访问 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Kimsuky Hackers使用新的自定义RDP包装器进行远程访问

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)60422

收藏

导语：使用自定义RDP包装器的主要优点是规避检测，因为RDP连接通常被视为合法的，允许Kimsuky在雷达下停留更长时间。

被称为Kimsuky的朝鲜黑客组织在最近的攻击中被发现使用定制的RDP包装器和代理工具直接访问受感染的机器。

发现该活动的AhnLab安全情报中心（ASEC）表示，朝鲜黑客现在正使用一套多样化的定制远程访问工具，而不再仅仅依赖于PebbleDash等嘈杂的后门，但PebbleDash目前仍在使用中，此举也是Kimsuky改变策略的手段之一。

**Kimsuky最新的攻击链**

最新的感染链始于一封鱼叉式网络钓鱼电子邮件，其中包含伪装成PDF或Word文档的恶意快捷方式（. lnk）文件附件。这些电子邮件包含收件人的姓名和正确的公司名称，表明Kimsuky在攻击前进行了侦察。

打开.LNK文件会触发PowerShell或Mshta从外部服务器检索额外的负载，包括：

**·**PebbleDash，一个已知的Kimsuky后门，提供初始系统控制。

**·**一个修改版本的开源RDP包装工具，支持持久的RDP访问和安全措施绕过。

**·**代理工具绕过私有网络的限制，允许攻击者访问系统，即使直接RDP连接被阻止。

**自定义RDP包装器**

RDP Wrapper是一个合法的开源工具，用于在Windows版本（如Windows Home）上启用本地不支持的远程桌面协议（RDP）功能。

它充当中间层，允许用户在不修改系统文件的情况下启用远程桌面连接。Kimsuky的版本改变了导出功能，以绕过反病毒检测，并可能区分其行为，足以逃避基于签名的检测。

![export-functions.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250208/1739002994188091.png "1739001991529385.png")

自定义RDP包装器导出功能

使用自定义RDP包装器的主要优点是规避检测，因为RDP连接通常被视为合法的，允许Kimsuky在雷达下停留更长时间。

此外，与通过恶意软件进行shell访问相比，它提供了更舒适的基于gui的远程控制，并且可以通过中继绕过防火墙或NAT限制，允许从外部进行RDP访问。

ASEC报告说，一旦Kimsuky在网络上站稳脚跟，他们就会放弃二次有效载荷。其中包括一个键盘记录器，它捕获击键并将其存储在系统目录中的文本文件中，一个infostealer（强制复制）提取保存在web浏览器上的凭据，以及一个基于powershell的ReflectiveLoader，它允许在内存中执行有效负载。

整体来看，Kimsuky作为一个持续不断的威胁，也是朝鲜致力于收集情报最多产的网络间谍威胁组织之一。根据ASEC的最新发现表明，其威胁组织正转向更隐蔽的远程访问方法，以延长在受损网络中的停留时间。

文章翻译自：https://www.bleepingcomputer.com/news/security/kimsuky-hackers-use-new-custom-rdp-wrapper-for-remote-access/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Lrji6Fev)

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