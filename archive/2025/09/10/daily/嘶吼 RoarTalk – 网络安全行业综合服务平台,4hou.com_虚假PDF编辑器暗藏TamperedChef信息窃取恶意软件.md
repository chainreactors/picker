---
title: 虚假PDF编辑器暗藏TamperedChef信息窃取恶意软件
url: https://www.4hou.com/posts/GAm0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-10
fetch_date: 2025-10-02T19:53:38.761822
---

# 虚假PDF编辑器暗藏TamperedChef信息窃取恶意软件

虚假PDF编辑器暗藏TamperedChef信息窃取恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 虚假PDF编辑器暗藏TamperedChef信息窃取恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)39834

收藏

导语：Truesec发现，该活动的操作人员至少从2024年8月起就开始活跃，并推广了其他工具，包括OneStart和Epibrowser浏览器。

威胁者一直在利用多个通过谷歌广告推广的网站，分发一款看似可信的PDF编辑应用，而该应用实则会植入名为TamperedChef的信息窃取恶意软件。

此次活动是一项大规模网络行动的一部分，该行动涉及多款可相互下载的应用程序，其中部分应用会诱骗用户将其系统注册为住宅代理。

研究人员表示，目前已识别出50多个域名用于托管这些欺诈性应用，这些应用由至少四家不同公司签发的虚假证书进行签名。该活动范围广泛且组织严密——操作人员会先让广告正常投放，待时机成熟后再激活应用中的恶意组件。

**全面更新触发信息窃取功能**

网络安全服务公司Truesec的技术分析详细阐述了TamperedChef信息窃取恶意软件植入用户系统的过程。研究人员发现，该恶意软件通过多个推广“AppSuite PDF Editor”免费工具的网站进行分发。

根据网络记录，调查人员确定该活动始于6月26日，当时相关的多个网站要么刚完成注册，要么已开始为AppSuite PDF Editor投放广告。但研究人员同时发现，这款恶意应用早在5月15日就已通过VirusTotal恶意软件扫描服务的检测。

该程序在8月21日前一直表现正常，直到当天接收了一次更新后，其内置的恶意功能才被激活——这些功能专门用于收集凭证、网络Cookie等敏感数据。

Truesec指出，TamperedChef信息窃取恶意软件是通过向PDF编辑器的可执行文件传递“-fullupdate”参数来实现植入的。

该恶意软件会检查主机上的各类安全代理，还会利用DPAPI（数据保护应用程序接口，Windows系统中用于加密敏感数据的组件）查询已安装网页浏览器的数据库。

![TamperedChf_security-agents.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250902/1756802660144443.png "1756801798134123.png")

tamperedChef 信息窃取器检查已安装的安全代理

深入调查分发方式后，Truesec的研究人员发现证据表明，在AppSuites PDF Editor中传播TamperedChef的网络犯罪分子，主要依靠谷歌广告推广这款恶意程序。

威胁者可能有一个策略，在激活AppSuites PDF Editor中的恶意组件之前，最大限度地提高下载量，因为他们比典型的60天Google广告活动到期时间提前四天交付了信息窃取器。

深入研究AppSuites PDF Editor，研究人员发现该程序的不同版本是由至少四家公司颁发的证书签名的，其中包括ECHO Infini SDN BHD、GLINT By J SDN. BHD和SUMMIT NEXUS Holdings LLC、BHD。

**诱导用户加入住宅代理网络**

Truesec发现，该活动的操作人员至少从2024年8月起就开始活跃，并推广了其他工具，包括OneStart和Epibrowser浏览器。值得注意的是，OneStart通常被标记为潜在有害程序（PUP，此类程序通常指广告软件）。

但托管检测与响应公司Expel的研究人员在调查涉及AppSuites PDF Editor、ManualFinder和OneStart的事件时发现，这些程序均会“植入高度可疑的文件、执行未预期的命令，并将主机转变为住宅代理”，其行为已更接近恶意软件。

研究人员发现，OneStart可下载由ECHO INFINI SDN. BHD公司签发证书的AppSuite-PDF，而AppSuite-PDF又能进一步获取PDF Editor。

Expel指出：“OneStart、AppSuite-PDF和PDF Editor的初始下载渠道，是一系列推广PDF及PDF编辑器的大型广告活动。这些广告会将用户引导至众多提供上述三款程序下载的网站之一。”

尽管该活动中使用的代码签名证书已被吊销，但当前已安装这些程序的设备仍面临风险。在部分PDF Editor的使用场景中，应用会向用户弹出提示，以“免费使用工具”为交换，请求获得将其设备用作住宅代理的权限。

研究人员指出，提供代理网络服务的供应商可能是合法实体，并未参与此次恶意活动，而PDF Editor的操作人员实则是作为附属机构从中牟利。显然，PDF Editor的幕后操纵者正以全球用户的利益为代价，试图实现利润最大化。

即便该活动中的这些程序被归为潜在有害程序（PUP），但其具备的功能与恶意软件并无差别，应同等视作恶意软件处理。

研究人员警告称，他们发现的这一网络行动还涉及更多应用程序，其中部分尚未被武器化，但这些应用均具备分发恶意软件或可疑文件、秘密在系统上执行命令的能力。

文章翻译自：https://www.bleepingcomputer.com/news/security/tamperedchef-infostealer-delivered-through-fraudulent-pdf-editor/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?E70FPkrA)

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