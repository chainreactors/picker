---
title: 丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息
url: https://buaq.net/go-144626.html
source: unSafe.sh - 不安全
date: 2023-01-09
fetch_date: 2025-10-04T03:20:44.914835
---

# 丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/082d34a7c061462abac831d09460828b.jpg)

丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息

导语：近20家汽车制造商和服务曝出API安
*2023-1-8 12:0:0
Author: [www.4hou.com(查看原文)](/jump-144626.htm)
阅读量:21
收藏*

---

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

![](https://www.4hou.com/captcha/flat?vDMfmd91)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/u=2315571907,182393339&fm=30&app=106&f=JPEG.jpg)

  丰田、奔驰和宝马等众多知名车企的API漏洞泄露车主个人信息](https://www.4hou.com/posts/mXJG)
* [![](https://img.4hou.com/images/253d769bfef5943e46a7a2c621f8d2bb.png)

  PyTorch机器学习框架遭遇恶意依赖供应链攻击](https://www.4hou.com/posts/VZBX)
* [![](https://img.4hou.com/images/微信截图_20230106135651.png)

  勒索软件生态系统在 2023 年将变得更加多样化](https://www.4hou.com/posts/jJDv)
* [![](https://img.4hou.com/images/微信截图_20230106140223.png)

  “伪装广告”：谷歌的Ad-Words被威胁分子大规模滥用，攻击众多组织、GPU和加密货币钱包](https://www.4hou.com/posts/JXmg)
* [![](https://img.4hou.com/images/微信截图_20230106094014.png)

  个人电脑容易因辐射而被盗取数据](https://www.4hou.com/posts/LBED)
* [![](https://img.4hou.com/images/a67d1677128a34f16518ae14b525e793.png)

  加密货币平台3Commas承认：黑客窃取了API密钥](https://www.4hou.com/posts/DE5K)

![]()

文章来源: https://www.4hou.com/posts/mXJG
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)