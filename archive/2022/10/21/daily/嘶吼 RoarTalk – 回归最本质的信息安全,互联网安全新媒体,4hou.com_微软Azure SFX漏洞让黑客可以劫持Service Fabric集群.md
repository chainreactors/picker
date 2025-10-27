---
title: 微软Azure SFX漏洞让黑客可以劫持Service Fabric集群
url: https://www.4hou.com/posts/q8kD
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-21
fetch_date: 2025-10-03T20:28:38.721983
---

# 微软Azure SFX漏洞让黑客可以劫持Service Fabric集群

微软Azure SFX漏洞让黑客可以劫持Service Fabric集群 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微软Azure SFX漏洞让黑客可以劫持Service Fabric集群

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)169850

收藏

导语：Orca Security披露了漏洞，旧版本Azure Fabric Explorer仍然岌岌可危。

![1666220384172647.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221020/1666233313133753.png "1666233313133753.png")

Service Fabric是一个面向业务关键型应用系统的平台，它托管着100多万个应用程序，并为微软的许多产品提供底层支持，包括但不限于Microsoft Intune、Dynamics 365、Skype for Business、Cortana、Microsoft Power BI以及Azure的多项核心服务。Service Fabri是微软用来构建、部署和管理基于微服务的分布式云应用程序的平台。它可以在Windows和Linux上运行，还可以跨任何云或本地环境来运行。

Service Fabric Explorer（SFX）是一种可用作托管式解决方案或桌面应用程序的开源工具，还是一种分布式系统平台，让Azure管理员可以管理和检查Azure Service Fabric集群中的节点和云应用程序。

Orca Security安全公司的研究人员Lidor Ben Shitrit近日发现了一个名为FabriXss的SFX欺骗漏洞（编号为CVE-2022-35829，CVSS的严重程度评分为6.4），这个漏洞可能使潜在的攻击者能够获得全面的管理员权限，并接管Service Fabric集群。

Orca Security解释道：“我们发现，如果Deployer（部署者）类型的用户只要拥有通过仪表板‘创建新应用程序’的权限，就可以利用仅仅这一权限来创建恶意应用程序名称，并滥用管理员权限，以执行各种调用和操作。”

这种操作包括执行集群节点重置，集群节点重置会删除所有的自定义设置，比如密码和安全配置，让攻击者可以创建新密码，并获得全面的管理员权限。

**外头没有被利用的案例**

Orca Security在8月11日向微软安全响应中心（MSRC）报告了这个漏洞，微软在10月11日的当月补丁星期二期间发布了修复该漏洞的安全更新。该漏洞影响Azure Fabric Explorer版本8.1.316及之前的版本。

Orca Security的博文介绍了属于概念验证的FabriXss漏洞利用代码，还附有其他技术细节。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221020/1666220399175006.png "1666220399175006.png")

图1

Orca团队解释道，利用这个漏洞始于通过客户端模板注入（CSTI）执行表达式。

接下来，攻击者需要跳出CSTI，进入到存储的XSS：

为了跳出CSTI进入到XSS，我们需要准确了解应用程序名称到底是如何创建和格式化的。仔细观察我们当前的有效应用程序（nginx），我们就可以看到“fabric:/”果然被添加到了该应用程序的后面。

最后，攻击者可以使用存储的XSS创建拥有管理员级别权限的自定义角色，然后重置其中一个节点并执行攻击载荷。

Service Fabric Explorer是共享的；默认情况下，有两种权限级别：只读取和管理员级。然而，正如Orca的研究人员解释，有一个选项可以修改只读取客户端权限，从而创建不是管理员、但仍能够执行特定操作的自定义用户。

研究人员能够滥用存储的XSS，只需创建自定义的客户端用户：deployer用户，然后创建发送攻击载荷的恶意应用程序即可。

微软表示，FabriXss漏洞只适用于针对不受支持的旧版本Service Fabric Explorer（SFXv1）的攻击，而当前默认的SFX Web 客户软件（SFXv2）不易受到攻击。

微软表示，然而，客户可以从默认Web客户软件（SFXv2）手动切换到易受攻击的旧版SFX Web 客户软件版本（SFXv1）。

这个问题要求攻击者已经在Service Fabric集群中拥有代码部署和执行权限，并且攻击目标使用易受攻击的Web客户软件（SFXv1）。

虽然微软并没有发现证明FabriXss已在攻击中被滥用的证据，但它还是建议所有Service Fabric客户升级到最新的SFX版本，而不是切换到易受攻击的SFXv1 Web客户软件版本。

据微软声称，即将发布的Service Fabric版本也将删除SFXv1以及切换到它的选项。

6月份，微软还修复了一个名为FabricScape的Service Fabric容器逃逸漏洞，该漏洞让威胁分子可以将权限提升到root级，并获得对主机节点的控制权，从而危及整个SF Linux集群。

参考及来源：https://www.bleepingcomputer.com/news/security/microsoft-azure-sfx-bug-let-hackers-hijack-service-fabric-clusters/
https://www.theregister.com/2022/10/19/azure\_service\_fabric\_vulnerability/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GA51PJrO)

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