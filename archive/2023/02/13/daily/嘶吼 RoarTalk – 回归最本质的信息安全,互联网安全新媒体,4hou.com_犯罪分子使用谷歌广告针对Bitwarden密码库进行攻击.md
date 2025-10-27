---
title: 犯罪分子使用谷歌广告针对Bitwarden密码库进行攻击
url: https://www.4hou.com/posts/oJwB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-13
fetch_date: 2025-10-04T06:27:38.726285
---

# 犯罪分子使用谷歌广告针对Bitwarden密码库进行攻击

犯罪分子使用谷歌广告针对Bitwarden密码库进行攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 犯罪分子使用谷歌广告针对Bitwarden密码库进行攻击

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-02-12 11:44:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)177103

收藏

导语：Bitwarden和其他密码管理器正在成为谷歌广告钓鱼攻击活动的目标，其目的在于窃取用户的密码库凭证。

随着企业和消费者开始在每个网站使用独特的密码，使用密码管理器来跟踪所有的密码已经变得非常有必要。

然而，除非你使用像KeePass这样的本地密码管理器，否则大多数密码管理器是基于云的，管理器允许用户通过网站和移动应用程序访问他们的密码。

这些密码被储存在云端的 "密码库" 中，并且以加密的形式保存数据，通常会使用用户的主密码进行加密。

最近LastPass的安全漏洞和Norton的凭证填充攻击说明，主密码是密码库的一个薄弱点。

由于这个原因，人们发现威胁者创建了针对密码库登录凭证进行攻击的钓鱼网页，一旦他们获得了这些凭证，他们就可以完全访问你的密码库。

**Bitwarden用户成为谷歌广告钓鱼的目标**

本周二，Bitwarden的用户在"bitwarden密码管理器"的搜索结果中看到了一个题为"Bitward密码管理器" 的谷歌广告。

虽然无法直接复制这个广告，但Bitwarden用户可以在Reddit和Bitwarden论坛上可以看到这个广告。

广告中所使用的域名是'appbitwarden.com'，点击后会将用户重定向到'bitwardenlogin.com'网站。

![图片1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675079675100024.jpeg "1675079466167654.jpeg")

bitwardenlogin.com网站的页面是通过完全复制合法的Bitwarden Web Vault登录页面得到的，如下图所示。

![图片2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675079675431318.jpeg "1675079491384495.jpeg")

在我们的测试中，该钓鱼页面可以接受用户提交的凭证，用户一旦提交后，系统会将用户重定向到合法的Bitwarden登录页面。

然而，我们最初使用的是假凭证进行的测试，当我们使用真实的Bitwarden测试登录凭证进行测试时，发现该页面已经关闭。

因此，我们无法看到该钓鱼页面是否也会像很多其他高级钓鱼页面一样试图窃取MFA支持的会话cookie（认证令牌）。虽然许多人觉得这个URL很明显是不正常的，表明这是一个钓鱼网页，但很多人无法分辨它是否是假的。

Reddit上一个关于钓鱼网页的话题的发帖人说，在这样的情况下，我怎么可能发现这是假的呢？这真是太可怕了。另一位用户在同一个Reddit帖子上评论道，别人都说要看网址，但我真的无法分辨哪个是真的。

更糟糕的是，不仅仅是Bitwarden被谷歌广告中的恶意钓鱼页面盯上了。安全研究人员MalwareHunterTeam最近也发现谷歌广告针对1Password密码管理器的凭证进行攻击的迹象。

![图片3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675079676131114.jpeg "1675079516208002.jpeg")

我们目前还没能找到针对其他密码管理器进行攻击的广告，但谷歌搜索结果中的广告最近已经成为了一个巨大的网络安全隐患。

最近的研究表明，威胁者正在利用谷歌广告为他们的恶意软件投放活动推波助澜，为初步进入企业网络，窃取凭证，并进行网络钓鱼攻击做准备。

**保护你的密码库**

由于密码库中包含了一些很敏感的私人数据，适当地保护它们是很重要的。

当谈到保护你的密码库免受网络钓鱼攻击时，第一道防线就是确认你在正确的网站上输入了你的凭证。

然而，如果你错误地在一个钓鱼网站上输入了你的凭证，那么你应该及时在你的密码管理器中配置多因素验证功能。在使用的各种MFA验证方法中，其效果从最好到最差，是硬件安全钥匙（安全性最好但最麻烦），认证应用程序（更容易使用），以及短信验证（可以在SIM卡交换攻击中被劫持）。

不幸的是，即使有MFA保护，你的账户仍然容易受到高级中间人（AiTM）网络钓鱼攻击。

AiTM钓鱼攻击是指威胁者利用专门的工具包，如Evilginx2、Modlishka和Muraena，创建钓鱼登陆页面，代理目标服务的合法登录表格进行攻击。

使用这种方法，网络钓鱼页面的访问者会看到一个合法服务的登录表，如微软365。当他们输入他们的凭证和MFA验证码时，这些信息也会被转发到真实的网站内。

然而，一旦用户登录，合法网站会发送MFA支持的会话cookie，网络钓鱼工具箱就可以窃取这些令牌供以后使用。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675079677551717.png "1675079542736045.png")

由于这些令牌已经通过MFA验证，它们允许威胁者登录你的账户而无需再次验证MFA。微软在7月警告说，这种类型的攻击被用来绕过了10,000多个组织的多因素认证。

所以，最好的方法是回到第一道防线，确保你只在合法的网站或移动应用程序上输入你的凭证。

本文翻译自：https://www.bleepingcomputer.com/news/security/bitwarden-password-vaults-targeted-in-google-ads-phishing-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iwA1LtNe)

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

![](https://img.4hou.com/portraits/f1cf9065382964bd9f4a9cd061a16d17.jpg)

# [~阳光~](https://www.4hou.com/member/lPjj)

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

[查看更多](https://www.4hou.com/member/lPjj)

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