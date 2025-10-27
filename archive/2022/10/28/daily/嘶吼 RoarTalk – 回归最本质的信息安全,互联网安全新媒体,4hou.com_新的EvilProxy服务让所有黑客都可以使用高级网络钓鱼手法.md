---
title: 新的EvilProxy服务让所有黑客都可以使用高级网络钓鱼手法
url: https://www.4hou.com/posts/17qj
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-28
fetch_date: 2025-10-03T21:06:15.684074
---

# 新的EvilProxy服务让所有黑客都可以使用高级网络钓鱼手法

新的EvilProxy服务让所有黑客都可以使用高级网络钓鱼手法 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的EvilProxy服务让所有黑客都可以使用高级网络钓鱼手法

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)163107

收藏

导语：反向代理网络钓鱼即服务（PaaS）平台EvilProxy承诺可以窃取身份验证令牌，从而绕过苹果、谷歌和Facebook等IT大公司的多因素身份验证（MFA）机制。

一个名为EvilProxy的反向代理网络钓鱼即服务（PaaS）平台近日兴风作浪，承诺可以窃取身份验证令牌，从而绕过苹果、谷歌、Facebook、微软、Twitter、GitHub、GoDaddy甚至PyPI上的多因素身份验证（MFA）机制。

该服务使不知道如何设置反向代理的技能低下的威胁分子也能够窃取原本受到有力保护的在线帐户。

反向代理是位于目标受害者和合法身份验证端点（比如公司的登录表单）之间的服务器。当受害者连接到网络钓鱼页面时，反向代理会显示合法的登录表单，转发请求，并返回来自该公司网站的响应。

当受害者将他们的凭据（即登录信息）和MFA输入到网络钓鱼页面后，他们被转发到实际平台的服务器（用户登录到该服务器上），并返回会话cookie。

然而，由于威胁分子的代理位于中间，它也可以窃取含有身份验证令牌的会话cookie。然后，威胁分子就可以使用该身份验证cookie以用户身份登录网站，从而绕过已配置好的多因素身份验证保护。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424348161900.png "1662424348161900.png")

图1. 反向代理的工作原理（来源：Resecurity）

一段时间以来，狡猾的高级持续性威胁（APT）组织一直在使用反向代理来绕过目标帐户上的MFA保护，一些组织使用自己的自定义工具，而另一些组织使用更易于部署的工具包，比如Modlishka、Necrobrowser和Evilginx2。

这些网络钓鱼框架与EvilProxy之间的区别在于，后者部署起来容易得多，并提供详细的教学视频和教程、对用户友好的图形界面，以及针对流行互联网服务的一大堆可供选择的克隆网络钓鱼页面。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424360115536.png "1662424360115536.png")

图2.平台上的使用说明（来源：Resecurity）

**更深入地了解EvilProxy**

网络安全公司Resecurity报告称，EvilProxy提供了一种易于使用的图形用户界面（GUI），威胁分子可以在GUI上设置和管理网络钓鱼活动以及支持它们的所有细节。

![p3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424379623108.png "1662424379623108.png")

图3. 选择网络钓鱼服务上的钓鱼活动选项（来源：Resucurity）

该服务承诺可以窃取用户名、密码和会话cookie，收费标准为150美元（10 天）、250美元（20 天）或400美元（为期一个月的网络钓鱼活动）。针对谷歌帐户的攻击收费更高，分别为250美元、450美元和600美元。

在以下视频中，Resecurity演示了针对谷歌帐户的攻击将如何通过EvilProxy开展。

![p4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424392204196.png "1662424392204196.png")

图4

虽然该服务在各种明网（clearnet）和暗网黑客论坛上大肆推广，但服务运营商会对客户进行审查，因此一些潜在买家可能会遭到拒绝。

据Resecurity声称，该服务的支付事项是在Telegram上单独安排的。一旦预付了费用，客户可以访问托管在洋葱网络（TOR）中的门户。

Resecurity测试该平台后证实，EvilProxy还提供虚拟机、反分析和反机器人程序防护，以过滤掉平台托管的网络钓鱼网站上无效或不受欢迎的访客。

![p5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424409100758.jpeg "1662424409100758.jpeg")

图5. EvilProxy上的反分析功能（来源：Resecurity）

Resecurity在报告中解释道：“不法分子正在使用多种技术和方法来识别受害者，并保护网络钓鱼工具包代码不被检测到。”

“与欺诈预防和网络威胁情报（CTI）等解决方案一样，它们汇总了有关已知VPN服务、代理、TOR出口节点及其他主机的数据，这些数据可用于（对潜在受害者进行）IP声誉分析。”

**值得留意的服务**

随着MFA的采用率不断提高，越来越多的威胁分子纷纷采用反向代理工具，而出现为骗子自动化一切操作的平台对于安全专业人员和网络管理员来说可不是好消息。

![p6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662424427812111.png "1662424427812111.png")

图6. EvilProxy在Breached论坛上大肆推广

目前，这个问题仍然可以通过实施客户端TLS指纹识别机制以识别和过滤掉中间人请求来解决。然而，行业内实施这种机制的步伐却落后于其迅猛发展的动向。

因此，像EvilProxy这样的平台实际上弥补了技能方面的不足或差距，为低水平的威胁分子提供了一种经济高效的方式来窃取有价值的帐户。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-evilproxy-service-lets-all-hackers-use-advanced-phishing-tactics/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iI0yTh4S)

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