---
title: 黑客在PoisonSeed网络钓鱼攻击中降低FIDO2多因素认证强度
url: https://www.4hou.com/posts/42j1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-25
fetch_date: 2025-10-06T23:27:12.620860
---

# 黑客在PoisonSeed网络钓鱼攻击中降低FIDO2多因素认证强度

黑客在PoisonSeed网络钓鱼攻击中降低FIDO2多因素认证强度 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客在PoisonSeed网络钓鱼攻击中降低FIDO2多因素认证强度

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)90012

收藏

导语：这种攻击突出了威胁者如何通过欺骗用户完成登录流程来绕过使用安全密钥进行物理交互的需要，从而找到绕过抗网络钓鱼认证的方法。

PoisonSeed网络钓鱼活动通过滥用WebAuthn中的跨设备登录功能来绕过FIDO2安全密钥保护，诱骗用户同意来自虚假公司门户的登录认证请求。

众所周知，PoisonSeed攻击者利用大规模网络钓鱼攻击来进行金融欺诈。在过去，分发包含加密种子短语的电子邮件用于耗尽加密货币钱包。

在Expel最近观察到的网络钓鱼攻击中，PoisonSeed攻击者并没有利用FIDO2的安全漏洞，而是滥用了合法的跨设备身份验证功能。

跨设备认证是一种WebAuthn功能，允许用户使用另一台设备上的安全密钥或认证应用程序在一台设备上登录。身份验证请求不需要物理连接，比如插入安全密钥，而是通过蓝牙或二维码扫描在设备之间传输。

这种攻击首先将用户引导到一个仿冒企业登录门户的网络钓鱼网站，比如Okta或Microsoft 365。当用户向门户输入凭据时，该活动使用中间对手（AiTM）后端，使用提交的凭据在合法登录门户上实时静默登录。

攻击中的目标用户通常会使用他们的FIDO2安全密钥来验证多因素身份验证请求。但是，网络钓鱼后端会告诉合法登录门户使用跨设备身份验证进行身份验证。

这将导致合法门户生成QR码，该QR码被传输回网络钓鱼页面并显示给用户。当用户使用智能手机或身份验证应用扫描这个二维码时，它就会批准攻击者发起的登录尝试。

![poisonseed-attack-flow.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250722/1753168927643631.jpg "1753168581611154.jpg")

PoisonSeed攻击流绕过FIDO2保护

这种方法允许攻击者发起依赖于跨设备身份验证而不是用户的物理FIDO2密钥的登录流，从而有效地绕过了FIDO2安全密钥保护。

Expel说，这种攻击并没有利用FIDO2实现中的漏洞，而是滥用了降低FIDO密钥身份验证过程的合法功能。为了降低风险，Expel建议采取以下防御措施：

**·**限制允许用户登录的地理位置，并为个人旅行建立注册流程。

**·**定期检查来自未知地点的未知FIDO密钥和不常见的安全密钥品牌的注册。

**·**考虑强制基于蓝牙的身份验证作为跨设备身份验证的要求，这将大大降低远程网络钓鱼攻击的有效性。

Expel还观察到一个单独的事件，一个威胁者在通过被认为是网络钓鱼的方式破坏了一个账户并重置了密码后，注册了自己的FIDO密钥。然而，这种攻击不需要任何欺骗用户的方法，比如QR码。

这种攻击突出了威胁者如何通过欺骗用户完成登录流程来绕过使用安全密钥进行物理交互的需要，从而找到绕过抗网络钓鱼认证的方法。

文章翻译自：https://www.bleepingcomputer.com/news/security/threat-actors-downgrade-fido2-mfa-auth-in-poisonseed-phishing-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hCm9oWcV)

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