---
title: 丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息
url: https://www.4hou.com/posts/mXJG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-09
fetch_date: 2025-10-04T03:21:21.274611
---

# 丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息

丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)233312

收藏

导语：近20家汽车制造商和服务曝出API安全漏洞，可能会让黑客进行各种恶意活动，包括解锁、启动和跟踪汽车以及泄露客户的个人信息等。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985006713378.png "1672894515119507.png")

近20家汽车制造商和服务曝出API安全漏洞，可能会让黑客进行各种恶意活动，包括解锁、启动和跟踪汽车以及泄露客户的个人信息等。

安全漏洞影响了全球众多知名品牌，包括宝马、劳斯莱斯、梅赛德斯-奔驰、法拉利、保时捷、捷豹、路虎、福特、起亚、本田、英菲尼迪、日产、讴歌、现代、丰田和捷尼赛思。

这些漏洞还影响了汽车技术品牌Spireon和Reviver以及流媒体服务SiriusXM。

这些API漏洞是由Sam Curry领导的研究团队发现的，他此前已在2022年11月披露了现代、捷尼赛思、本田、讴歌、日产、Infinity和SiriusXM的安全问题。

虽然Curry之前的披露解释了黑客如何利用这些漏洞来解锁和启动汽车，但鉴于自报告这些问题以来已经过了90天的漏洞披露期，该团队近日发布了一篇披露API漏洞的更详细的博文。

受影响的厂商已经修复了该报告中提出的所有问题，因此现在无法利用这些漏洞。

**访问内部门户网站**

最严重的API缺陷出现在宝马和梅赛德斯-奔驰，它们受到面向整个公司的单点登录（SSO）漏洞的影响，攻击者可以趁机访问内部系统。

就梅赛德斯-奔驰而言，分析师可以访问多个私有GitHub实例、Mattermost上的内部聊天频道、服务器、Jenkins和AWS实例、连接到客户汽车的XENTRY系统等内容。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985007713576.png "1672894528176069.png")

图1. 梅赛德斯-奔驰内部门户网站（来源：Sam Curry）

就宝马而言，研究人员可以访问内部经销商门户网站，查询任何汽车的车辆识别码（VIN），并检索含有敏感车主详细信息的销售文件。

此外，他们还可以利用SSO漏洞以任何员工或经销商的身份登录，并访问保留给内部使用的应用程序。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985008559593.png "1672894545789324.png")

图2. 访问宝马门户网站上的车辆详细信息（来源：Sam Curry）

**泄露车主详细信息**

利用其他API漏洞让研究人员得以访问起亚、本田、英菲尼迪、日产、讴歌、梅赛德斯-奔驰、现代、捷尼赛思、宝马、劳斯莱斯、法拉利、福特、保时捷和丰田等汽车车主的个人身份信息（PII）。

以超级昂贵的汽车为例，披露车主信息来得尤其危险，因为在一些情况下，这些数据包括销售信息、实际位置和客户地址。

法拉利存在内容管理系统（CMS）上实施的SSO很糟糕这一问题，泄露了后端API路由，并使攻击者可以从JavaScript代码片段中提取凭据。

攻击者可以利用这些漏洞来访问、修改或删除任何法拉利客户帐户，管理他们的车辆配置文件，或将自己设置为车主。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985010126724.png "1672894559202153.png")

图3. 披露法拉利用户数据细节（来源：Sam Curry）

**跟踪车辆GPS**

这些漏洞还可能让黑客可以实时跟踪汽车，带来潜在的物理风险，并影响数百万车主的隐私。

保时捷是受影响的品牌之一，其车载通讯系统存在的漏洞使攻击者能够检索车辆位置并发送命令。

GPS跟踪解决方案Spireon也曝出了汽车位置泄露的问题，1550万辆使用其服务的车辆受到影响，甚至让攻击者可以获得全面的权限以访问远程管理面板，使攻击者能够解锁汽车、启动发动机或禁用启动器。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985012151938.png "1672894577159086.png")

图4. Spireon管理面板上的历史GPS数据（来源：Sam Curry）

第三家受影响的实体是数字车牌制造商Reviver，该公司的管理面板容易受到未经身份验证的远程访问，任何人都可以访问GPS数据和用户记录，还能够更改车牌信息等。

Curry解释了这些漏洞如何让他们可以在Reviver面板上将车辆标记为“被盗”，这将自动向警方通知事件，从而将车主/司机置于不必要的风险中。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230106/1672985013188417.png "1672894595191514.png")

图5. 远程修改Reviver车牌（来源：Sam Curry）

**尽量减少泄露**

车主们可以限制存储在车辆或移动配套应用程序中的个人信息数量，从而保护自己远离这些类型的漏洞。

另外有必要将车载通讯设置为最私密的模式，并阅读隐私政策以了解数据的使用方式。

Sam Curry还向IT安全外媒BleepingComputer分享了以下建议，车主们在购车时应遵循。

Curry在发给BleepingComputer的一份声明中警告：“在购买二手车时，确保原车主的账户已被删除。如果可能的话，对与车辆关联的应用程序和服务使用强密码，并设置双因素身份验证（2FA）。”

Spireon发言人向BleepingComputer发来了以下声明：

我们的网络安全专业人员已与安全研究人员会面，讨论和评估所谓的系统漏洞，并立即在必要的范围内实施补救措施。

我们还采取了积极的措施，进一步加强我们产品组合的安全性，这是我们作为一家售后配件车载通讯解决方案领先提供商对客户持续承诺的一部分。

Spireon认真对待所有安全问题，并利用广泛的行业领先工具集来监测和扫描其产品和服务，以发现已知和新颖的潜在安全风险。

本文翻译自：https://www.bleepingcomputer.com/news/security/toyota-mercedes-bmw-api-flaws-exposed-owners-personal-info/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?QFTtB8tK)

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