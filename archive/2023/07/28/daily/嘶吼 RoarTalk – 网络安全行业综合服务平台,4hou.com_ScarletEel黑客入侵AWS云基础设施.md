---
title: ScarletEel黑客入侵AWS云基础设施
url: https://www.4hou.com/posts/kjDJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-28
fetch_date: 2025-10-04T11:51:39.588710
---

# ScarletEel黑客入侵AWS云基础设施

ScarletEel黑客入侵AWS云基础设施 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ScarletEel黑客入侵AWS云基础设施

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-07-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128691

收藏

导语：该攻击团伙非常精通使用AWS工具，可将本地网络连接到云环境中，并利用AWS的本地功能轻松地进行横向移动。

研究人员发现，一个名为ScarletEel的有经济动机的威胁攻击者一直在渗透亚马逊网络服务（AWS）进行各种恶意活动。这些攻击活动包括窃取凭证和知识产权、部署加密挖矿软件以及进行分布式拒绝服务（DDoS）攻击。

ScarletEel最初是由云安全公司Sysdig在今年2月的一篇博文中进行披露的。研究人员发现该组织能够对AWS工具进行灵活的运用，并利用原生的AWS功能在云环境中进行有效的操作。并且通过获得适当的访问权限，ScarletEel然后会执行双重攻击策略，即植入加密挖矿软件，同时窃取知识产权。

针对Sysdig最近进行的分析显示，ScarletEel在不断完善它的战术并躲避云安全检测机制。该威胁行为体已将其能力扩展到针对AWS Fargate（一种相对未开发的计算引擎）。此外，ScarletEel还将DDoS即服务（DDoS-as-a-service）纳入到了其利用技术的范围。

Sysdig的威胁研究工程师Alessandro Brucato解释说，ScarletEel更善于针对受害者的环境，提高了利用漏洞的能力，同时很好的规避了客户实施的防御安全措施。

为了发起更多的网络攻击，ScarletEel利用了Kubernetes集群中的Jupyter notebook容器。攻击者利用脚本搜索AWS凭据，并将其发送回指挥控制（C2）服务器内。不过有趣的是，这些脚本使用了内置的shell命令，而不是使用命令行工具来隐蔽地窃取数据，从而避免了curl和wget等监控工具的检测。

ScarletEel也使用了Pacu（一种针对AWS的开源渗透测试工具）来识别受害者账户中的权限提升的漏洞。同时，该威胁行为者还使用了Peirates，这是一款专为探索和利用Kubernetes环境而定制的工具。

攻击者为了掩盖他们真实的活动痕迹，设计了一种巧妙的防御机制。他们没有直接与AWS进行交互，而是使用了支持AWS协议的俄罗斯服务器。通过使用本地的AWS命令，那么他们的恶意行为就会被掩盖。此外，由于这些活动是在俄罗斯服务器上进行的，因此在受害者的AWS CloudTrail日志中并没有被发现。

ScarletEel对云环境的攻击给传统的云安全措施带来了很大的挑战。例如，该威胁攻击者成功入侵了AWS Fargate，由于其有限的访问权限以及该工具主要在内部网络进行使用，AWS Fargate通常不被视为目标。Sysdig的威胁研究主管Michael Clark强调，我们需要采取积极的防御措施来对抗ScarletEel这样的设施。

他补充说，就像我们在这次攻击中看到的那样，他们最终还是进入了Fargate系统，并获得了它的凭证。因此，他们肯定意识到了这其中存在的问题，而且他们进行攻击可能只是时间问题。

Brucato解释说，要防范像ScarletEel这样的实体被攻击，必须首先要采取一些措施防止攻击者进入到你的环境。但如果他们已经进入到了你的内部网络环境中，因为现在他们已经变得越来越复杂，你还必须要实施有效的安全措施。这里，Clark强调了有效的云安全态势管理（CSPM）和云基础设施权限管理（CIEM）的价值。

Brucato总结道，现在仅仅通过一种方式进行网络保护还是不够的，因为现在的攻击者已经意识到了这一点。现在他们可以利用任何漏洞细节进行攻击。

本文翻译自：https://www.cysecurity.news/2023/07/scarleteel-hackers-breach-aws-cloud.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?urceVIOl)

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

![](https://img.4hou.com/portraits/f1cf9065382964bd9f4a9cd061a16d17.jpg)

# [~阳光~](https://www.4hou.com/member/lPjj)

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

[查看更多](https://www.4hou.com/member/lPjj)

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