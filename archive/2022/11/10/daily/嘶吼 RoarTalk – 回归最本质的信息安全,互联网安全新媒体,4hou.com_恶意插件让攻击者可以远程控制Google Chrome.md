---
title: 恶意插件让攻击者可以远程控制Google Chrome
url: https://www.4hou.com/posts/ZXx8
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-10
fetch_date: 2025-10-03T22:13:20.410771
---

# 恶意插件让攻击者可以远程控制Google Chrome

恶意插件让攻击者可以远程控制Google Chrome - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意插件让攻击者可以远程控制Google Chrome

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)175041

收藏

导语：一个名为“Cloud9”的Chrome浏览器僵尸网络近日被发现在外头肆虐，它利用恶意插件来窃取在线账户、记录击键内容、注入广告和恶意JavaScript代码，并利用受害者的浏览器来发动DDoS攻击。

一个名为“Cloud9”的Chrome浏览器僵尸网络近日被发现在外头肆虐，它利用恶意插件来窃取在线账户、记录击键内容、注入广告和恶意JavaScript代码，并利用受害者的浏览器来发动DDoS攻击。

Cloud9浏览器僵尸网络实际上是一种针对Chromium浏览器（包括谷歌Chrome和微软Edge）的远程访问木马（RAT），让威胁分子可以远程执行命令。

这个恶意的Chrome插件未出现在官方的Chrome网站商店中，而是通过其他渠道来传播，比如推送虚假的Adobe Flash Player更新的网站。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221109/1667951359788429.png "1667951359788429.png")

图1. Chrome上的恶意浏览器插件（来源：Zimperium）

这种方法似乎屡试不爽，Zimperium的研究人员近日报告称，他们已经在全球各地的系统上看到了Cloud9感染。

**感染浏览器**

Cloud9是一个恶意的浏览器插件，它给Chromium浏览器植入后门，以执行大量的恶意函数和功能。

该插件由三个JavaScript文件组成，这几个文件用于收集系统信息、使用主机的资源来挖掘加密货币、执行DDoS攻击，以及注入运行浏览器漏洞利用代码的脚本。

Zimperium注意到加载的漏洞利用代码针对Firefox中的CVE-2019-11708和CVE-2019-9810漏洞、IE中的CVE-2014-6332和CVE-2016-0189以及Edge的CVE-2016-7200漏洞。

这些漏洞被用来在主机上自动安装和执行Windows恶意软件，使攻击者能够对系统进行更严重的破坏。

然而，即使没有Windows恶意软件组件，Cloud9插件也可以从被攻击的浏览器窃取cookie，威胁分子进而可以利用这些cookie劫持有效的用户会话、接管帐户。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221109/1667951330144822.png "1667951330144822.png")

图2. 浏览器cookie窃取器（来源：Zimperium）

此外，该恶意软件有一个击键记录器，可以窥视按键内容，以窃取密码及其他敏感信息。

该插件中还有一个“clipper”模块，不断监测系统剪贴板，以窃取复制的密码或信用卡信息。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221109/1667951317395208.png "1667951317395208.png")

图3. Cloud9的clipper组件（来源：Zimperium）

Cloud9还可以通过悄然加载网页来注入广告，以提升广告点击率，从而为其运营团伙带来收入。

最后，恶意软件可以征集主机的计算能力，通过向目标域发送HTTP POST请求来执行第7层DDoS攻击。

Zimperium表示，第7层攻击通常很难被检测到，因为TCP连接看起来与合法请求非常相似。开发者很可能利用这个僵尸网络来提供执行DDOS的服务。

**运营团伙和攻击目标**

据信Cloud9背后的黑客与Keksec恶意软件团伙有关联，因为最近这次活动中所用的指挥和控制（C2）域曾出现在Keksec过去的攻击中。

Keksec负责开发和运营多个僵尸网络项目，包括EnemyBot、Tsunamy、Gafgyt、DarkHTTP、DarkIRC和Necro。

Cloud9的受害者遍布全球各地，而威胁分子在论坛上发布的截图表明，他们的目标是各种浏览器。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221109/1667951309434919.png "1667951309434919.png")

图4. Cloud9面板的截图（来源：Zimperium）

此外，在网络犯罪论坛上大肆推广宣传Cloud9的做法让Zimperium认为Keksec可能将Cloud9出售/出租给其他运营团伙。

本文翻译自：https://www.bleepingcomputer.com/news/security/malicious-extension-lets-attackers-control-google-chrome-remotely/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?NSqKU0VY)

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