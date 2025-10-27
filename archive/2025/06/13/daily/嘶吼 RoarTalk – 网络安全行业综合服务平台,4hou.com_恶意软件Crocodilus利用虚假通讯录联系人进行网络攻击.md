---
title: 恶意软件Crocodilus利用虚假通讯录联系人进行网络攻击
url: https://www.4hou.com/posts/wxqM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-13
fetch_date: 2025-10-06T22:50:54.679955
---

# 恶意软件Crocodilus利用虚假通讯录联系人进行网络攻击

恶意软件Crocodilus利用虚假通讯录联系人进行网络攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意软件Crocodilus利用虚假通讯录联系人进行网络攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)101904

收藏

导语：这样做将导致设备在接到来电时显示来电者联系人配置文件中列出的姓名，而不是来电者的ID。这可能使威胁者可以冒充受信任的银行、公司，甚至朋友和家人，使电话看起来更可信。

最新版本的“Crocodilus”安卓恶意软件引入了一种新机制，该机制会在受感染设备的联系人列表中添加一个虚假联系人，以便在收到威胁者的电话时利用虚假联系人欺骗受害者。该功能与其他几个功能一起推出，主要是针对规避的改进，该恶意软件似乎已将其目标范围扩展到全球。

**Crocodilus触角涉及全球**

Threat Fabric研究人员在2025年3月底首次记录了该恶意软件，并强调了其广泛的数据盗窃和远程控制能力。这些早期版本还通过伪造错误信息，要求用户在12小时内“备份”加密货币钱包密钥，否则将无法访问它，从而进行了基本的社交工程尝试。当时，Crocodilus只在土耳其的一些小规模活动中出现过。

根据Threat Fabric的说法，这种情况现在已经改变了，该公司继续监控恶意软件的运行，并观察到Crocodilus已将其目标范围扩大到所有大洲。

同时，最新的发布版本在滴管组件中引入了更好的代码打包以提高逃避检测的能力，并且为有效负载增加了额外的 XOR 加密层。

分析人员还发现，代码复杂化和纠缠现象使得恶意软件的逆向工程更加困难。另一个附加功能是一个系统，可以在受感染设备上本地解析被盗数据，然后将其泄露给威胁者以获得更高质量的数据收集。

**虚假联系人**

最新的Crocodilus恶意软件版本的一个显著特点是能够在受害者的设备上添加虚假联系人。这样做将导致设备在接到来电时显示来电者联系人配置文件中列出的姓名，而不是来电者的ID。这可能使威胁者可以冒充受信任的银行、公司，甚至朋友和家人，使电话看起来更可信。

此操作在发出特定命令时执行，该命令触发以下代码以编程方式（使用ContentProvider API）在Android设备上创建新的本地联系人。

![code.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250612/1749695778107159.png "1749020241245416.png")

JS代码段在设备上创建一个新联系人

“在收到命令“TRU9MMRHBCRO”后，Crocodilus会将指定联系人添加到受害者的联系人列表中，”Threat Fabric在报告中解释道。

这进一步增加了攻击者对设备的控制。威胁分子的意图是在一个令人信服的名字下添加一个电话号码，比如‘银行支持’，这样攻击者就可以在看起来合法的情况下给受害者打电话。恶意联系人不绑定用户的谷歌帐户，因此它不会与用户登录的其他设备同步。

Crocodilus进化得很快，它与社会工程有密切关系，这使它成为一种特别危险的恶意软件。安全研究人员建议Android用户在为他们的设备下载软件时坚持使用谷歌Play或信任的发行商，确保Play Protect始终处于激活状态，并将他们使用的应用数量减少到绝对必要的程度。

文章翻译自：https://www.bleepingcomputer.com/news/security/android-malware-crocodilus-adds-fake-contacts-to-spoof-trusted-callers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OhTtAekO)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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