---
title: E-ZPass收费系统在大规模网络钓鱼活动中频繁遭遇攻击
url: https://www.4hou.com/posts/0MBL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-09
fetch_date: 2025-10-06T22:04:30.062145
---

# E-ZPass收费系统在大规模网络钓鱼活动中频繁遭遇攻击

E-ZPass收费系统在大规模网络钓鱼活动中频繁遭遇攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# E-ZPass收费系统在大规模网络钓鱼活动中频繁遭遇攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-08 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)65530

收藏

导语：如果用户收到其中一条消息，应该阻止并报告该号码，以便将电子邮件地址或电话号码报告给Apple。

近期，冒充 E-ZPass 及其他收费机构的网络钓鱼活动愈演愈烈，收件人会收到多条 iMessage 和短信，企图窃取个人及信用卡信息。

这些信息中嵌入了链接，一旦点击，就会将受害者带到冒充 E-ZPass、The Toll Roads、FasTrak 或其他收费机构的钓鱼网站，试图窃取他们的个人信息，包括姓名、电子邮件地址、实际地址和信用卡信息。

这种诈骗手段并非新出现的，联邦调查局早在 2024 年 4 月就已发出过相关警告。这些短信绕过了反垃圾邮件措施，且来自看似随机的电子邮件地址，再加上攻击的规模，表明这仍是一次自动化攻击。

此次发现的诈骗短信冒充 E-ZPass 或机动车管理局直接发送。这些短信使用的语言带有紧迫感，比如称通行费需在一天或两天内支付，否则将产生额外费用，或者驾照将被吊销。

![ezpass-phish.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250407/1744013410158249.png "1744013314103479.png")

该活动中的网络钓鱼短信样本

苹果 iMessage 自动关闭来自未知发件人的信息链接，以保护用户免受短信钓鱼诈骗。为了绕过这一点，骗子会让用户回复文本，这样链接就可以点击了。

点击提供的链接将受害者带到一个E-ZPass网络钓鱼网站，除了URL，它看起来像一个合法的网站。安全研究人员测试表明，该钓鱼网站仅在手机上加载，因此桌面用户不会看到它。

![ezpass-page.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250407/1744013411424792.png "1744013385125568.png")

受害者登录的钓鱼页面

在这种骗局中发送的短信数量如此之大，以至于用户对特定骗局发生频率表示沮丧，据统计，这种信息有时一天多达7条短信。

虽然这些信息的来源尚未确定，但最近发现了一个名为Lucid的新兴网络钓鱼即服务平台，该平台与这些类型的骗局有关。

Lucid和Darcula等平台使用加密的iMessage和RCS消息绕过传统的反垃圾邮件过滤器，发送大量文本，而不会产生与标准短信发送相关的成本。

如果用户收到其中一条消息，应该阻止并报告该号码，以便将电子邮件地址或电话号码报告给Apple。然而，作为一般规则，用户应尽量避免回应这些骗局。

对于那些担心他们有合法的未付款项的人，应该直接登录收费当局的网站来检查任何余额。邦调查局此前曾建议收件人在IC3门户网站上提出投诉。

文章翻译自：https://www.bleepingcomputer.com/news/security/toll-payment-text-scam-returns-in-massive-phishing-wave/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ISzvY42d)

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