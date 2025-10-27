---
title: RVTools在供应链攻击中被迫分发Bumblebee恶意软件
url: https://www.4hou.com/posts/Zg9w
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-28
fetch_date: 2025-10-06T22:25:36.377917
---

# RVTools在供应链攻击中被迫分发Bumblebee恶意软件

RVTools在供应链攻击中被迫分发Bumblebee恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# RVTools在供应链攻击中被迫分发Bumblebee恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61103

收藏

导语：除非验证其哈希值，否则不要从非官方来源下载并执行声称提供安全/干净版本的RVTools安装程序。

近期，RVTools VMware管理工具遭遇供应链攻击，官方网站被关闭，攻击中分发了一个被木马化的安装程序，以在用户的机器上放置Bumblebee恶意软件加载程序。

随后，官方RVTools网站“rvtools.com”和“robware.net”现在显示了一条通知，表示Robware.net和RVTools.com目前处于离线状态，提醒用户请勿从任何其他网站或来源搜索或下载所谓的RVTools软件。但消息中没有给出下载门户何时会重新上线的估计时间。

![notice.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250521/1747813763791702.png "1747811774146009.png")

robware.net和rvtools.com上的公告

**RVTool供应链攻击**

RVTools最初由Robware开发，现在归Dell所有，是一个Windows实用程序，为VMware vSphere环境提供全面的库存和运行状况报告。

RVTools被广泛认为是VMware管理员的必备工具，VMware自己的Virtual Blocks Blog也将其视为vSphere管理的顶级实用工具。

零日实验室的研究员Aidan Leon首先发现了供应链攻击，他警告说，官方的RVTools安装程序[VirusTotal]试图执行一个恶意版本。dll [VirusTotal]，该版本被检测为Bumblebee恶意软件加载程序。

进一步调查发现，RVTools网站上列出的文件哈希值与实际下载的文件不匹配。下载的版本明显更大，包含version.dll；旧版本的RVTools不包含此文件，并且正确匹配其发布的散列。

在VirusTotal提交后大约一个小时，公众提交的数量从4个上升到16个。大约在同一时间，RVTools网站暂时下线。当它重新上线时，下载的文件发生了变化：文件大小变小了，哈希值现在与网站上列出的干净版本相匹配。

Bumblebee是一种恶意软件加载器，通常通过SEO中毒，恶意广告和网络钓鱼攻击来推广。安装后，恶意软件会下载并在受感染的设备上执行额外的有效载荷，例如Cobalt Strike信标、信息窃取器和勒索软件。

该恶意软件与Conti勒索软件行动有关，Conti利用该恶意软件获得了企业网络的初始访问权限。虽然Conti勒索软件行动于2022年关闭，但其许多成员分裂成其他勒索软件行动，包括Black Basta， Royal， Silent Ransom等，他们可能仍然可以访问这些工具。

网络安全公司Arctic Wolf也报告称，通过恶意输入域名传播木马RVTools安装程序，可能通过SEO中毒或恶意广告进行推广。

Arctic Wolf最近观察到一个木马化的RVTools安装程序通过一个恶意输入的域名进行分发。该域名与合法域名匹配，但顶级域名（TLD）从.com更改为.org。RVTools是一款广泛使用的VMware工具，由Robware开发，用于库存和配置报告。

最近，还有其他关于搜索引擎优化中毒和针对RVTools品牌的恶意广告活动的报道，以诱骗人们下载恶意的木马安装程序。

如果从这些域名下载了软件，其设备很有可能感染了Bumblebee恶意软件，并可能感染了额外的有效载荷。

由于恶意软件被威胁者用于在企业网络中获得 foothold，如果检测到恶意软件，人们应进行彻底调查以确定其他设备是否被攻破是至关重要的。除非验证其哈希值，否则不要从非官方来源下载并执行声称提供安全、干净版本的RVTools安装程序。

文章翻译自：https://www.bleepingcomputer.com/news/security/rvtools-hit-in-supply-chain-attack-to-deliver-bumblebee-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?425og3tr)

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