---
title: 揭露路由协议的隐藏风险
url: https://www.4hou.com/posts/kjKN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-27
fetch_date: 2025-10-04T11:58:44.434501
---

# 揭露路由协议的隐藏风险

揭露路由协议的隐藏风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 揭露路由协议的隐藏风险

布加迪
[新闻](https://www.4hou.com/category/news)
2023-08-26 11:50:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)116609

收藏

导语：忽视边界网关协议（BGP）及其他路由协议的安全性已造成了诸多漏洞，必须予以解决。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230820/1692496413734772.png "1692496413734772.png")

路由协议对于互联网及建立在其之上的众多服务的正常运作起到了关键作用。然而，许多这些协议是在没有考虑安全问题的情况下开发的。

比如说，边界网关协议（BGP）起初并没有考虑对等节点之间可能发生的攻击。在过去的几十年里，人们在BGP的起源和路径验证方面投入了大量的研究。然而，忽略BGP实施的安全性、尤其是消息解析的安全性已导致了多个漏洞，结果被用来实现拒绝服务攻击（DoS）。

安全行业有一种普遍的态度：“如果它没有坏，就别去修它”。人们往往忽视安全审计，错误地认为这些类型的漏洞不如起源和路径验证问题来得严重。

传统的风险评估常常无法彻底检查网络上的所有软件和设备及其影响，因而形成盲区。当组织甚至没有意识到这些路由协议在使用时，安全缺口会变得更加刺眼。路由协议可能出现在人们意想不到的更多地方，比如数据中心、跨组织站点的VPN以及嵌入到定制设备中。

**不为人知的风险**

在过去的一年里，威胁分子越来越多地瞄准网络设备，包括路由器。美国网络安全和基础设施安全局（CISA）已发布了一项具有约束力的操作指令，要求联邦机构减小这些设备的风险。

这种对路由器的高度关注引起了业界对底层路由协议安全性的关注。比如说，已出现了威胁分子利用路由器进行侦察、恶意软件部署以及指挥和控制通信的情况。CISA已知的被利用漏洞目录中还有三个BGP DoS问题，以及影响另一种路由协议实施的另外两个DoS漏洞。

此外，BGP劫持和泄漏也引起了人们的关注，导致这类事件频发：流量被重定向到意想不到的目的地，有可能暴露敏感信息。数据中心攻击带来了另一大风险，因为路由协议中的漏洞可以被利用来将数据中心与互联网隔离，从而使其服务无法访问。

**风险评估方面的盲区**

要堵住风险评估方面的盲区，需要采取多管齐下的做法。

组织应该尽可能频繁地给网络基础设施打上补丁，但你无法修复你不知道坏掉的东西。实际上，应该为连接到网络的所有设备及在网络上运行的软件（包括路由协议）列一份资产清单。

这种安全意识使组织能够识别漏洞，并采取必要的措施来确定补救工作的优先级。组织还可以通过实施分段策略来降低这些风险，从而保护未打补丁的设备不暴露在互联网上。

理想情况下，安全应该从软件开发人员开始做起，他们可以通过使用增强的静态和动态分析技术以及保护软件开发生命周期，降低路由协议实施中出现漏洞的可能性。此外，应该建立有效的沟通机制，以便及时地处理和解决任何已确定的漏洞。

同样，将这些协议整合到其设备中的供应商成为了供应链中第三方风险的来源。实施软件物料清单（SBOM）可以更深入地了解设备和网络中存在的漏洞，从而使组织能够更好地管理风险。然而，当供应商不提供这种透明度（或者供应商不知道其设备受到影响）时，责任最终就落在组织的身上，需要积极主动地评估攻击面。

最后，安全研究社区在发现和负责任地披露这些安全漏洞方面发挥着重要的作用。在某些情况下，安全研究社区提供了比安全公告更及时、更有效的补救和缓解建议，补救和缓解建议本该是由软件开发人员和供应商发布的。比如在最近的BGP漏洞中，安全研究人员发布了一个开源的BGP模糊测试工具，可以快速测试协议实施以发现漏洞。

**暴露风险**

影响软件的漏洞还会影响连接的设备，因此增强安全性需要两者共同努力。安全研究人员可以提高公众对路由协议的潜在风险及其对更广泛生态系统造成的影响的认识，但最终还是由组织负责倡导加强安全性。

组织必须重视全面了解自己的网络设备，而不仅仅是传统的端点和服务器，还要了解所有的软件和设备。它们必须实施严格的脆弱性评估，并建立有效的威胁检测和响应机制。

软件开发人员和供应商需要改进其安全实践，加强沟通，并提高透明度。通过共同努力，我们才能加强路由协议的安全性，并保护我们这个高度互联的世界。

本文翻译自：https://www.darkreading.com/vulnerabilities-threats/unveiling-the-hidden-risks-of-routing-protocols如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?nLrv5hrP)

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