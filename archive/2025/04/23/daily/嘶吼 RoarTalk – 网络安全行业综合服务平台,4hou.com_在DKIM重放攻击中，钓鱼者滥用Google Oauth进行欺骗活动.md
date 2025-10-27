---
title: 在DKIM重放攻击中，钓鱼者滥用Google Oauth进行欺骗活动
url: https://www.4hou.com/posts/gyNk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-23
fetch_date: 2025-10-06T22:05:32.377146
---

# 在DKIM重放攻击中，钓鱼者滥用Google Oauth进行欺骗活动

在DKIM重放攻击中，钓鱼者滥用Google Oauth进行欺骗活动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 在DKIM重放攻击中，钓鱼者滥用Google Oauth进行欺骗活动

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)68352

收藏

导语：PayPal会自动向攻击者的地址发送确认信息，该地址会将其转发到一个邮件列表，该邮件列表会将其转发给群组中所有潜在的受害者。

在一次相当巧妙的攻击中，黑客利用了一个漏洞，得以发送一封看似来自谷歌系统的虚假电子邮件，通过了所有验证，但指向了一个用于收集登录信息的欺诈页面。

攻击者利用谷歌的基础设施诱骗收件人访问一个看似合法的“支持门户”，该门户要求提供谷歌账户凭证。

这条欺诈信息看似来自“no-reply@google.com”，并且通过了域名密钥识别邮件（DKIM）验证方法，但实际发件人却并非如此。

**带有谷歌“域密钥识别邮件”印章的虚假电子邮件**

以太坊域名服务（ENS）的首席开发者尼克·约翰逊收到了一封看似来自谷歌的安全警报，称执法部门已向谷歌发出传票，要求获取他的谷歌账户内容。

谷歌甚至将其与其他合法的安全提醒放在一起，以至于几乎所有东西看起来都合情合理，这很可能会欺骗那些不太懂技术、不知道从何处寻找欺诈迹象的用户。

![NickJohnson_fake_email.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745206183439493.png "1745205184665647.png")

通过谷歌系统转发的网络钓鱼邮件

然而，约翰逊敏锐发现，电子邮件中的虚假支持门户网站托管在sites.google.com——谷歌的免费网站建设平台上，这引起了人们的怀疑。

在谷歌域名上，收件人意识到他们被瞄准的机会更低。约翰逊说，这个虚假的支持门户网站“和真实的完全一样”，唯一的迹象是它托管在sites.google.com上，而不是accounts.google.com上。

![NickJohnson_fake_support.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745206184175597.png "1745205251570465.png")

假冒谷歌支持门户

开发人员认为，欺诈性网站的目的是收集凭据，以破坏收件人的帐户。

假门户在骗局中很容易解释，但聪明的部分是传递一条似乎已经通过谷歌的DKIM验证的消息，即所谓的DKIM重放网络钓鱼攻击。

仔细观察电子邮件的详细信息就会发现，mailed-by头显示的地址与谷歌的no-reply不同，收件人是一个me@地址，位于一个看起来像是由谷歌管理的域。然而，这条消息是由谷歌签署和传递的。

![Johnson_header.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745206185142214.png "1745205317112434.png")

邮件标头显示真实的收件人和投递地址

约翰逊将线索拼凑起来，识破了骗子的伎俩。首先，他们会注册一个域名，并为“me@域名”创建一个谷歌账号。域名不是特别重要，但看起来像某种基础设施会有所帮助。选择“me”作为用户名很聪明，这位开发者解释道。

随后，攻击者创建了一个谷歌 OAuth 应用程序，并将其名称设为整个钓鱼信息。在某个时候，该信息包含大量空白，以使其看起来已经结束，并与谷歌关于攻击者 me@domain 电子邮件地址的访问权限通知区分开来。

当攻击者授权他们的OAuth应用程序访问谷歌工作区中的电子邮件地址时，谷歌会自动向该收件箱发送安全警报。

由于谷歌生成了这封电子邮件，它用一个有效的DKIM密钥签名，并通过了所有的检查。最后一步是将安全警报转发给受害者。

谷歌系统的弱点是DKIM只检查消息和头，而不检查信封。因此，假电子邮件通过了签名验证，并在收件人的收件箱中看起来是合法的。

此外，通过将欺诈地址命名为me@， Gmail将显示消息，就好像它是发送到受害者的电子邮件地址一样。

电子邮件认证公司EasyDMARC也详细介绍了约翰逊描述的DKIM重放式网络钓鱼攻击，并对每一步进行了技术解释。

**PayPal选项以同样的方式被滥用**

谷歌以外的其他平台也尝试过类似的技巧。今年3月，一场针对PayPal用户的攻击活动采用了同样的方法，即欺诈性信息来自这家金融公司的邮件服务器，并通过了DKIM的安全检查。

测试显示，攻击者使用“礼物地址”选项将新电子邮件链接到他们的PayPal账户。

添加新地址时有两个字段，攻击者用电子邮件填充其中一个字段，并将网络钓鱼信息粘贴到第二个字段中。

PayPal会自动向攻击者的地址发送确认信息，该地址会将其转发到一个邮件列表，该邮件列表会将其转发给群组中所有潜在的受害者。

![paypal-scam-attack-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745206186926136.png "1745205415405976.png")

PayPal骗局使用类似的伎俩

事后有媒体就此事联系了PayPal，但从未收到回复。Johnson还向谷歌提交了一份bug报告，而谷歌最初的回复是“这个过程是按计划进行的”。但不久后，谷歌认识到它对用户来说存在一定风险，目前正在努力修复OAuth的弱点。

文章翻译自：https://www.bleepingcomputer.com/news/security/phishers-abuse-google-oauth-to-spoof-google-in-dkim-replay-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Y15FpqHt)

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