---
title: Sysdig报告解读：配置不当和漏洞是云安全的两大风险
url: https://www.4hou.com/posts/q8KG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-08
fetch_date: 2025-10-04T08:54:21.445396
---

# Sysdig报告解读：配置不当和漏洞是云安全的两大风险

Sysdig报告解读：配置不当和漏洞是云安全的两大风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Sysdig报告解读：配置不当和漏洞是云安全的两大风险

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)155439

收藏

导语：据网络安全公司Sysdig声称，大约87%的容器镜像含有高危漏洞或严重漏洞，而90%的已授权限并未被使用。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230307/1678157733107757.png "1675978402316715.png")

据Sysdig的报告显示，两个最大的云安全风险依然是配置不当和漏洞，漏洞日益通过软件供应链被引入。

虽然零信任是当务之急，但数据显示，零信任架构的基础：最小特权访问权限并未得到妥善执行。报告特别指出，几乎90%的已授权限并未被使用，这就给窃取凭据的攻击者留下了很多机会。

以上数据来自分析Sysdig客户日常运行的700多万个容器的报告。该报告还考虑了从GitHub、Docker Hub和CNCF等公共数据源获取的数据。报告分析了南美/北美、澳大利亚、欧盟、英国和日本等国家的客户的数据。

**87%的容器镜像存在高危漏洞或严重漏洞**

几乎87%的容器镜像被发现含有高危漏洞或严重漏洞，比去年报告的75%%有所上升。一些镜像还存在不止一个漏洞。Sysdig特别指出，许多组织意识到了这种危险，但难以在保持软件发布快节奏的同时修复漏洞。

尽管有补丁，但漏洞依然存在的原因在于处理能力和优先级问题。当生产环境中运行的容器镜像中87%存在高危漏洞或严重漏洞时，DevOps或安全工程师就要登录并查看成百上千个存在漏洞的镜像。

Sysdig的威胁研究工程师Crystal Morin表示，彻查一遍并修复漏洞需要花时间。对大多数开发人员而言，为新应用程序编写代码才是其工作重心，所以他们在打补丁上每花1分钟，开发能卖钱的新应用程序的时间就少了1分钟。

有相应补丁的高危漏洞或严重漏洞中只有15%存在于运行时加载的软件包中。如果筛选出这些实际使用的危险软件包，企业就能把精力集中在带来真正风险的一小撮可以修复的漏洞上。

**Java软件包风险最高**

Sysdig按软件包类型估算运行时加载的软件包中所含漏洞的百分比，以评估哪些编程语言、库或文件类型带来的漏洞风险最高。结果发现，Java软件包在运行时加载的软件包中所含的320000多个漏洞中占到了61%。Java软件包占运行时加载的所有软件包的24%。

运行时暴露的软件包漏洞更多，导致泄密或攻击的风险更高。Java在运行时暴露的漏洞数量最多。虽然Java不是所有容器镜像当中最流行的软件包类型，却是运行时最常用的软件包。

Morin说：“因此，我们认为好人和坏人都关注Java软件包以获得最大回报。由于Java大受欢迎，漏洞赏金猎手更侧重于寻找Java语言漏洞。”

Morin表示，虽然更新颖或不太常见的软件包类型似乎更安全，但这可能是由于漏洞尚未被发现，或者更为糟糕的是，漏洞已被发现，但还没有没披露。

**采用安全左移、防护右移的概念**

安全左移指这种实践：将测试、质量和性能评估放到开发生命周期的早期阶段。然而，即使采用了完美的左移安全实践，威胁仍可能出现在生产环境中。

Sysdig建议，组织应奉行安全左移、防护右移的策略。防护右移安全强调保护和监测运行中服务的机制。Morin表示，光有借助防火墙和入侵防御系统（IPS）等工具的传统安全实践还不够到位。这留下了安全缺口，因为它们通常无法深入了解容器化的工作负载和周围的云原生环境。

运行时可见性可以帮助组织改善安全左移实践。一旦容器进入到生产环境中，将运行时发现的问题与底层代码关联起来的反馈回路可以帮助开发人员了解该关注哪个方面。运行时可见性还可以帮助静态安全测试工具精准地确定哪些软件包在运行应用程序的容器内部执行。

Morin补充道，这使开发人员可以不用太关注未使用软件包的漏洞，转而专注于修复可利用的运行时漏洞。每项网络安全计划都应该旨在实现全面生命周期安全。

**配置不当是导致云安全事件的最大元凶**

虽然漏洞是个问题，但配置不当仍是导致云安全事件的首要原因，因此应该引起组织重视。据Gartner声称，到2023年，75%的安全问题是由身份、访问和权限管理不到位造成的，而2020年这个比例是50%。

Sysdig的数据显示，在为期90天的分析期间，授予非管理员用户的权限仅10%被使用。

Sysdig的同比分析显示，组织将访问权授予更多的员工，或者完善身份和访问管理（IAM）实践。这家网络安全公司特别指出，人员用户数量增加可能是更多业务转移到云环境或者因业务发展而增加人员配置的结果。

今年，Sysdig客户的云环境中58%的身份归属非人员角色，去年这个比例是88%。

非人员角色常常临时使用；如果不再使用却没删除，恶意分子就很容易趁虚而入。Morin说：“角色类型的转变可能是由于组织使用云的力度加大，随之而来的是将云访问权授予更多的员工，从而改变了人员角色和非人员角色的比重。”

授予非人员身份的权限中超过98%至少90天没有被使用。Sysdig特别指出：“这些未被使用的权限常常被授予了孤立身份，比如到期失效的测试帐户或第三方帐户。”

**对非人员身份实施最小权限原则**

安全团队应像管理人员身份一样对非人员身份实施最小权限原则，还应该尽可能删除未被使用的测试帐户，以防止访问风险。Sysdig特别指出，虽然人工排查很繁琐，但所使用权限筛选器和自动生成的建议可以提高这个过程的效率。

与对待人员角色一样，也应该对非人员角色实施最小权限原则。组织需要授予人员完成工作所需的最小权限。这个原则同样适用于非人员，比如需要访问权才能完成任务的应用程序、云服务或商业工具。这就好比手机上的应用程序请求权限，以访问联系人、相册、摄像头和麦克风等更多功能或内容。

Morin说：“除此之外，我们还必须考虑针对这些非人员实体的访问管理。授予过大的权限、未定期管理所授权限，为恶意分子在初始访问、横向移动和权限提升等方面提供了更多机会。”

本文翻译自：https://www.csoonline.com/article/3686579/misconfiguration-and-vulnerabilities-biggest-risks-in-cloud-security-report.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?679E6Ajn)

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