---
title: 研究人员绕过了微软更新的&quot;ProxyNotShell &quot;漏洞修复指导方案
url: https://www.4hou.com/posts/q8nR
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-14
fetch_date: 2025-10-03T19:49:07.944991
---

# 研究人员绕过了微软更新的&quot;ProxyNotShell &quot;漏洞修复指导方案

研究人员绕过了微软更新的"ProxyNotShell "漏洞修复指导方案 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 研究人员绕过了微软更新的"ProxyNotShell "漏洞修复指导方案

星辰大海
[新闻](https://www.4hou.com/category/news)
2022-10-13 11:44:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)184178

收藏

导语：微软已经更新了它为上周所发现的影响Exchange服务器软件的两个零日漏洞所提供修复指导方案。

据其中几位花了几周时间研究漏洞的安全研究人员说，发现目前为这些漏洞（俗称 "ProxyNotShell"）所提供的修复建议并不足以完全解决这些问题。

网络安全公司Huntress的高级threatOps分析师团队负责人Dray Agha解释说，微软提供的原始修复措施是很容易被恶意利用的。

他说，由于这种缓解措施很容易被绕过，所以那些使用了原始修复措施的服务器现在仍然是很脆弱的。截至周二，微软已经重新更新了缓解措施的脚本，并考虑到了这种被绕过的情况。

但是不幸的是，我们很可能会看到这将会成为一场猫捉老鼠的游戏，因为攻击者和安全研究人员都在寻找新的方法来绕过微软的缓解措施。

上周，在越南网络安全公司GTSC的报告中，微软确认它目前正在调查这些问题，这些漏洞也正在野外被利用。GTSC向 趋势科技的零日计划报告了这个问题，该计划也确认了这些漏洞的存在。

微软表示，它观察到目前在全球有不到10个组织被这些漏洞攻击。

该公司的安全团队解释说，黑客组织很可能是一个国家支持的组织，他们主要利用两个漏洞。

第一个是服务器端请求伪造漏洞，该漏洞被指定为CVE-2022-41040，它可以让拥有邮件服务器上用户账户凭证的攻击者获得未经授权的访问级别。第二个漏洞被定为CVE-2022-41082，该漏洞允许攻击者远程代码执行，这类似于2021年给许多公司造成混乱的ProxyShell漏洞。GTSC表示，它目前还不方便公布这些漏洞的技术细节。

远程代码执行漏洞被认为是特别危险的，因为它们使攻击者可以对受害者的系统进行修改。电子邮件也是许多企业日常办公的重要软件，并且内部可能会包含很多敏感信息，这也使得它们成为了攻击者的首要目标。

网络安全和基础设施安全局（CISA）在发现这两个漏洞数小时后，已将其添加到已知被利用的漏洞列表中，而微软在周四也证实，这些漏洞目前也正在被攻击者利用，并已经影响到那些运行的微软Exchange Server 2013、2016和2019。

Huntress高级安全研究员约翰-哈蒙德证实，微软最初的缓解措施可以很容易地被绕过，但他指出，微软目前已经提供了更新的自动化工具，可以使那些打了官方补丁的服务器获得更好的保护。

Sophos公司首席研究科学家Chester Wisniewski说，目前已知只有极少数的服务器由于这一漏洞受到了攻击，这也为我们大家争取了一点时间来实施缓解措施。

Wisniewski说，我们都还在等待官方补丁的发布，IT团队应该迅速做好准备，在官方补丁发布后尽快对漏洞进行修复，因为我们预计攻击者会在补丁发布后极短的时间内进行逆向工程，研究如何去利用这个漏洞。

Tenable的Claire Tills解释说，这些漏洞似乎是ProxyShell的变种，Proxyshell漏洞是2021年底被披露的一连串漏洞。

Tills说，最明显的区别是，这两个最新的漏洞都需要身份认证，而ProxyShell并不需要。

她补充说，ProxyShell是2021年发布的被利用最多的攻击链之一。

**网络犯罪获得的利益**

一些研究人员说，他们看到GitHub上有人出售虚假的漏洞利用工具，Flashpoint研究人员说，他们在俄语黑客和恶意软件论坛Exploit上看到一个漏洞被以25万美元出售。但是他们无法核实该漏洞是真的还是假的。

Flashpoint和其他几位专家一样，也对微软所认为的Exchange Online客户不需要采取任何措施提出了异议。Flashpoint研究人员说，这可能会使客户陷入一种错误的安全感中，客户即使迁移到了Exchange Online，但同时也在内部保留了一台混合的服务器。

他们说，在这种情况下，客户仍然需要对混合服务器进行处置。

根据微软发布的关于Exchange服务器更新的一般指导，即使你只在企业内部使用Exchange服务器来管理Exchange相关对象，你也需要保持服务器处于最新版本。

不幸的是，一些研究人员已经找到了绕过微软最近发布的最新缓解措施的方法。

Vulcan Cyber的高级技术工程师Mike Parkin指出，希望微软能够尽快发布补丁，以解决众多有潜在风险的企业内部Exchange服务器的问题。

本文翻译自：https://therecord.media/microsoft-updates-guidance-for-proxynotshell-bugs-after-researchers-get-around-mitigations/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?18JdmoES)

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

![](https://img.4hou.com/portraits/d79ce62858b2af535a202a0195e229e4.jpg)

# [星辰大海](https://www.4hou.com/member/Ny06)

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

[查看更多](https://www.4hou.com/member/Ny06)

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