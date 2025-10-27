---
title: 黑客滥用iCloud日历邀请发送钓鱼邮件 借苹果服务器绕过垃圾邮件过滤
url: https://www.4hou.com/posts/5MPR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-16
fetch_date: 2025-10-02T20:11:24.053046
---

# 黑客滥用iCloud日历邀请发送钓鱼邮件 借苹果服务器绕过垃圾邮件过滤

黑客滥用iCloud日历邀请发送钓鱼邮件 借苹果服务器绕过垃圾邮件过滤 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客滥用iCloud日历邀请发送钓鱼邮件 借苹果服务器绕过垃圾邮件过滤

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-15 16:43:05

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)37733

收藏

导语：尽管这封钓鱼邮件的诱饵内容并无特别之处，但攻击者通过滥用iCloud日历邀请这一合法功能，并借助苹果邮件服务器及官方邮箱地址，为邮件增添了可信度，且因其发自可信来源，有可能绕过垃圾邮件过滤器。

黑客正滥用iCloud日历邀请功能，以苹果邮件服务器名义发送伪装成购买通知的回电钓鱼邮件。由于这类邮件直接发自苹果官方服务器，因此更有可能绕过垃圾邮件过滤器，直接进入目标用户的收件箱。

**钓鱼邮件伪装成PayPal支付通知**

本月初，一苹果用户在社交媒体上分享了一封可疑邮件：该邮件声称收件人的PayPal账户被扣除599美元，并提供了一个电话号码，称若需讨论付款事宜或进行修改可拨打联系。

邮件内容写道：“您好，客户。您的PayPal账户已被扣费599.00美元。我们特此确认已收到您最近的付款。” 后续补充道：“如您希望讨论或修改此笔付款，请拨打+1 (786) 902-8579联系我们的支持团队。如需取消，请拨打+1 (786) 902-8579。”

![icloud-calendar-phishing.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250909/1757387531676243.jpg "1757387524190736.jpg")

iCloud日历邀请用于网络钓鱼邮件

这类邮件的目的是欺骗收件人，使其误以为自己的PayPal账户遭盗用并被恶意扣费，进而恐吓收件人拨打骗子的“支持”电话。一旦拨通，骗子会进一步谎称收件人账户已被盗，或声称需要远程连接电脑协助办理退款，诱骗用户下载并运行恶意软件。

而在以往的类似骗局中，这种远程访问权限常被用于窃取银行账户资金、植入恶意软件或盗取电脑中的数据。

**滥用iCloud日历邀请的技术细节**

该邮件的诱饵内容虽属典型的回电钓鱼骗局，但异常之处在于其发件地址为“noreply@email.apple.com”，且通过了SPF、DMARC和DKIM三项邮件安全验证——这意味着邮件确实发自苹果的官方服务器。

邮件验证结果显示：

Authentication-Results: spf=pass (sender IP is 17.23.6.69)

smtp.mailfrom=email.apple.com; dkim=pass (signature was verified)

header.d=email.apple.com;dmarc=pass action=none header.from=email.apple.com;

从这封钓鱼邮件来看，它本质上是一封iCloud日历邀请：攻击者将钓鱼文本写入“备注”字段，然后向自己控制的一个Microsoft 365邮箱地址发送邀请。

当用户创建iCloud日历活动并邀请外部人员时，苹果服务器会以“noreply@email.apple.com”为发件地址，以iCloud日历所有者的名义从email.apple.com发送邮件邀请。

文章举例获取的这封邮件中，邀请对象是一个Microsoft 365账户“Billing3@WilliamerDickinsonerLTD.onmicrosoft.com”。与此前利用PayPal“新地址”功能的钓鱼活动类似，这个被邀请的Microsoft 365邮箱实际是一个邮件列表——它会自动将收到的所有邮件转发给列表中的所有成员，而这些成员正是钓鱼骗局的目标。

通常情况下，若邮件最初发自苹果服务器，经Microsoft 365转发后会无法通过SPF验证。为避免这一问题，Microsoft 365会使用“发件人重写方案（SRS）”将“回复路径”重写为微软关联地址，从而使其通过SPF验证。例如：

原始回复路径：noreply@email.apple.com

重写后回复路径：bounces+SRS=8a6ka=3I@williamerdickinsonerltd.onmicrosoft.com

**风险提示与平台回应**

尽管这封钓鱼邮件的诱饵内容并无特别之处，但攻击者通过滥用iCloud日历邀请这一合法功能，并借助苹果邮件服务器及官方邮箱地址，为邮件增添了可信度，且因其发自可信来源，有可能绕过垃圾邮件过滤器。

若用户收到意外的日历邀请，且其中包含可疑信息，请务必保持警惕。截至目前苹果公司尚未就此事进行回复。

文章翻译自：https://www.bleepingcomputer.com/news/security/icloud-calendar-abused-to-send-phishing-emails-from-apples-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?242UGOoL)

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