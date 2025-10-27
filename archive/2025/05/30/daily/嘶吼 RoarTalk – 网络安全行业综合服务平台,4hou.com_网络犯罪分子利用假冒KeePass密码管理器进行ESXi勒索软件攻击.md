---
title: 网络犯罪分子利用假冒KeePass密码管理器进行ESXi勒索软件攻击
url: https://www.4hou.com/posts/QX80
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-30
fetch_date: 2025-10-06T22:23:20.618125
---

# 网络犯罪分子利用假冒KeePass密码管理器进行ESXi勒索软件攻击

网络犯罪分子利用假冒KeePass密码管理器进行ESXi勒索软件攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 网络犯罪分子利用假冒KeePass密码管理器进行ESXi勒索软件攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)79140

收藏

导语：WithSecure将此活动归因于UNC4696，这是一个之前与Nitrogen Loader活动有关的黑客组织。

至少8个月以来，攻击者一直在分发木马版本的KeePass密码管理器，以安装Cobalt Strike信标、窃取凭证，并最终在被入侵的网络上部署勒索软件。

WithSecure的威胁情报团队在调查一起勒索软件攻击后发现了这一活动。研究人员发现，攻击始于通过必应广告推广的恶意KeePass安装程序，该广告推广了虚假软件网站。

由于KeePass是开源的，攻击者修改了源代码，构建了一个木马化的版本，称为KeeLoader，其中包含所有正常的密码管理功能。然而，它包括安装Cobalt Strike信标并以明文形式导出KeePass密码数据库的修改，然后通过信标窃取密码。

WithSecure表示，此次攻击中使用的Cobalt Strike水印与一个初始访问代理有关，该代理被认为与过去的Black Basta勒索软件攻击有关。

Cobalt Strike水印是嵌入到信标中的唯一标识符，与用于生成有效载荷的许可证绑定。“这个水印通常在与黑巴斯塔勒索软件相关的信标和域的背景下被注意到。它很可能被作为初始访问经纪人与Black Basta密切合作的黑客使用。

研究人员表示，已经发现了多个KeeLoader的变体，这些变体使用合法证书签名，并通过诸如keepaswrd[等拼写错误域名传播。com, keegass[。com和KeePass[.]me。

目前，[。com网站仍然活跃，并继续分发木马化的KeePass安装程序[VirusTotal]。

![keepass-malware-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250520/1747722740172270.png "1747722740172270.png")

假冒的KeePass网站推送木马安装程序

除了释放Cobalt Strike信标之外，木马化的KeePass程序还包含密码窃取功能，允许威胁者窃取输入到程序中的任何凭据。

“KeeLoader不仅被修改到可以作为恶意软件加载器的程度。它的功能被扩展到促进KeePass数据库数据的泄露，”WithSecure报告中写道。

当KeePass数据库数据被打开时；“帐号”、“登录名”、“密码”、“网址”和“评论”信息也以CSV格式导出到“%localappdata%”目录下，格式为“。kp”。这个随机整数值在100-999之间。

![dumping-keepass-credentials.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250520/1747722657616038.png "1747722595106824.png")

转储KeePass凭证

最终，由WithSecure调查的攻击导致该公司的VMware ESXi服务器被勒索软件加密。对该活动的进一步调查发现了一个广泛的基础设施，用于分发伪装成合法工具的恶意程序和旨在窃取凭证的网络钓鱼页面。

aenys[。]com域名被用来托管其他子域名，这些子域名冒充知名公司和服务，如WinSCP、PumpFun、Phantom Wallet、Sallie Mae、Woodforest Bank和DEX Screener。每一个都被用来分发不同的恶意软件变体或窃取凭证。

WithSecure将此活动归因于UNC4696，这是一个之前与Nitrogen Loader活动有关的黑客组织。之前的攻击活动与黑猫/ALPHV勒索软件有关。

建议用户从合法网站下载软件，尤其是像密码管理器这样高度敏感的软件，并避免任何链接到广告中的网站。即使广告显示了软件服务的正确URL，也应该避免，因为威胁者已经多次证明，他们可以绕过广告策略，在链接到冒名顶替的网站时显示合法的URL。

文章翻译自：https://www.bleepingcomputer.com/news/security/fake-keepass-password-manager-leads-to-esxi-ransomware-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wqKNk8Ni)

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