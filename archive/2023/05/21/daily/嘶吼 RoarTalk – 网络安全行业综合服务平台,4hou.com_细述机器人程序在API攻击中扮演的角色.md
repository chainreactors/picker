---
title: 细述机器人程序在API攻击中扮演的角色
url: https://www.4hou.com/posts/wy0m
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-21
fetch_date: 2025-10-04T11:37:03.347035
---

# 细述机器人程序在API攻击中扮演的角色

细述机器人程序在API攻击中扮演的角色 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 细述机器人程序在API攻击中扮演的角色

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)87889

收藏

导语：本文介绍了API机器人程序攻击的性质、威胁分子如何使用机器人程序来攻击API以及用户如何保护API免受机器人程序的攻击。

API 可谓是现代应用程序的构建模块，支撑可组合的企业模型和数字化平台。随着更多的组织意识到 API 集成具有的重要性，API 的使用量随之猛增。

目前，全球使用的公共API和私有API总数估计约为2 亿个。由于API如此重要，它们一开始就让用户可以快速轻松地访问数据、资源和功能，攻击者不可能不注意它们。机器人程序（bot）是攻击者武器库中的一种关键工具，他们利用机器人程序来策划API机器人攻击。

API机器人程序攻击到底是什么？威胁分子如何使用机器人程序来攻击API？你又该如何保护API免受机器人程序的攻击？请耐心读下去。

**API 机器人程序攻击**

在深入研究什么是API机器人程序攻击之前，不妨先了解机器人程序的基础知识。

机器人程序是用于机器对机器通信的自主程序。可以对它们进行编程，以便在无需人工干预的情况下执行功能和执行Web请求。它将HTTP流量从IP地址发送到目标系统。僵尸网络是一堆机器人程序，它们协同工作，可以利用多个IP地址。僵尸网络的规模从几百个IP地址到几千个IP地址不等。

在机器人程序攻击中，恶意分子利用机器人程序来操纵、欺诈或扰乱目标网站、应用程序、最终用户或API。机器人程序攻击最初用于向目标发送垃圾邮件。而今天，它们已变得极其错综复杂，可以执行高度模仿人类行为的复杂攻击。

当这些自动化程序被用来专门攻击API时，或者当攻击者利用机器人程序加大API攻击的规模、影响和复杂度时，这就是API机器人程序攻击。

**为什么机器人程序被用于攻击API？**

**通过编程暴露数据、资源和业务逻辑：**

多年来，机器人程序一直被用于网络攻击。但是当它们用于攻击API时，为什么令人担忧？这是由于API旨在连接不同的应用程序，提供对数据和资源等资产的编程访问，并使多个客户能够轻松集成和共享。就其本质而言，它们暴露了高价值的功能和业务逻辑，并使资源容易被发现。因此，它们加大了暴露敏感信息的风险。

**缺乏可见性：**

API 之所以是机器人程序攻击的诱人目标，是由于组织对整个生命周期内的API缺乏可见性。API在幕后工作，但这没有太大帮助。如果你不知道架构中存在API，又该如何审查、管理和保护它们？这就留下了一些易受攻击的API、影子API、僵尸API、流氓API和配置错误的 API。因此，它们通常不如传统端点来得安全，并急剧加大风险。

再加上机器人程序，灾难就会随时到来。组织可能不知道存在哪些 API、谁在使用它们、它们可以访问哪些资源以及它们暴露了哪些业务逻辑。但威胁分子利用机器人程序来分析组织的IT架构，并四处寻觅API中的薄弱环节。机器人程序实际上为攻击者简化了这个过程。

**今天的机器人程序是隐蔽的：**

如今机器人程序用于API攻击，另一个原因是它们极其隐蔽，可以避免被传统安全工具检测出来。事实上，如今更复杂的机器人程序也可以避免被更高级的安全工具检测出来。

比如说，你可能临时调整了API身份验证规则，以便在三次登录尝试失败后冻结帐户。在凭据填充（撞库）攻击中，尝试两次失败后，机器人程序就会改用另一个IP地址。使用智能自动化，它们可以在没有人工干预的情况下完成这一切工作，根据设定的规则和学习能力做出决定。

**机器人程序被用来掩护其他攻击：**

API 机器人攻击通常被攻击者用作干扰或掩护，以策划其他类型的API滥用。比如说，攻击者可能利用僵尸网络触发数以千计的安全警报，好让安全团队跟进。但他们的目的是在安全团队调查安全警报时枚举 ID。

威胁分子之所以利用机器人程序攻击API，是由于在此过程中提供了无与伦比的速度、灵活性和敏捷性。比如说，无法在不触发安全防御系统的情况下手动发动撞库或蛮力攻击。但机器人程序使蛮力和撞库攻击变得快速、简单且可扩展。

这是表明机器人程序如何帮助攻击者对API下手的另一个例子。攻击者可以在未经身份验证的情况下向端点发送大量API请求，并在短时间内收集大量数据。

**传统工具无力应对现代机器人程序：**

面对常规的机器人程序攻击，传统的安全工具不尽如人意。但它们在阻止API机器人程序攻击方面更加无效，原因是它们不是专门针对API设计的。首先，传统工具无法有效区分机器人程序活动和人类活动，也无法有效区分好的机器人程序活动和坏的机器人程序活动。这严重限制了它们保护API远离基于机器人程序的攻击的能力。

其次，鉴于机器人程序留下的线索较少、API收集的细节较少，传统工具无法有效地判断API调用是恶意的还是合法的。实际上，机器人程序请求的是与浏览器攻击相同的数据。

不同之处在于，API 机器人程序攻击不提供浏览器版本、使用的cookie和设备类型等方面的信息，而传统工具使用这些信息来检测机器人程序活动。由于API攻击是完全虚拟的，机器人程序可以绕过攻击、在不同的云之间移动、轮换IP地址、使用代理网络以及做更多的事情来摆脱传统防御。

**业务逻辑缺陷：**

开发人员往往使用通用规则集，并使用默认配置的API，而不考虑实际业务逻辑。这带来了业务逻辑缺陷，机器人程序可以利用这些缺陷造成严重破坏，同时通过看似合法的API请求逃避检测。

**针对API的机器人程序攻击更容易发起：**

与针对移动和Web应用程序的机器人程序攻击相比，针对API的机器人程序攻击策划起来容易得多，而且极具成本效益。虽然不同的应用程序需要不同的方法和机器人程序功能，但攻击者可以使用相同的基础设施和攻击机制来攻击直接的API和Web API。此外，API 使攻击者能够更接近核心 IT 基础设施和关键资产。

此外，机器人、僵尸网络和攻击工具包很容易租用，而且价格通常很低。因此，攻击者不需要太多资源或深厚的技术知识就能发起API机器人攻击。

**机器人程序用于API 攻击的方式有哪些？**

1. 侦察：攻击者利用机器人程序和僵尸网络来发掘易受攻击的API端点、测试检测阈值和分析攻击面等。

2. 攻击：机器人程序和僵尸网络用于攻击API。一些常见的API机器人程序攻击包括撞库攻击、蛮力攻击、内容抓取攻击和注入攻击等。

3. 规避：在基于API的攻击中，攻击者还利用机器人程序和僵尸网络通过隐蔽行为或制造干扰来规避安全防御系统。

**对付API机器人程序的几种有效方法**

收集情报，并为机器人程序针对API的平常行为建立基准。

监控所有入站API请求，以便在侦察阶段发现并阻止异常行为。

部署的安全工具应该能够根据具体情况智能化地允许、阻止、标记或质询入站流量，无需太多的人为干预。

利用行为和模式分析、工作流验证和指纹识别技术，有效地区分人类活动、好的机器人程序活动和坏的机器人程序活动。

持续扫描、测试和监控API，寻找是否存在错误配置、漏洞和业务逻辑缺陷。

使用零信任策略，加强访问控制和身份验证机制。

始终定制API 规则集。

本文翻译自：https://hackernoon.com/the-role-of-bots-in-api-attacks如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0gO3j8wI)

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