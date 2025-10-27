---
title: 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露
url: https://www.4hou.com/posts/nlJp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-25
fetch_date: 2025-10-06T20:04:49.117472
---

# 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露

针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-01-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)88583

收藏

导语：如果开发人员点击嵌入的“转到策略”按钮来了解他们违反了哪些规则，他们就会被带到 Google 域上的恶意 OAuth 应用程序的合法登录页面。

有关针对 Chrome 浏览器扩展程序开发人员的网络钓鱼活动的新细节近期被披露，该活动导致至少 35 个扩展程序被入侵，以注入数据窃取代码，其中包括来自网络安全公司 Cyberhaven 的扩展程序。

尽管最初的报告主要集中在 Cyberhaven 的安全扩展上，但随后的调查显示，相同的代码已被注入到至少 35 个扩展中，总共约有 2,600,000 人使用。从目标开发者对 LinkedIn 和 Google Groups 的报告来看，最新的攻击活动于 2024 年 12 月 5 日左右开始。然而，有安全研究人员发现早期命令和控制子域早在 2024 年 3 月就已存在。

**欺骗性的 OAuth 攻击链**

攻击首先会直接或通过与其域名关联的支持电子邮件发送给 Chrome 扩展程序开发人员的网络钓鱼电子邮件。从看到的电子邮件来看，该活动使用了以下域名来发送网络钓鱼电子邮件：

```
supportchromestore.com
forextensions.com
chromeforextension.com
```

这封网络钓鱼电子邮件看起来像是来自 Google，声称该扩展程序违反了 Chrome Web Store 政策，有被删除的风险。  “我们不允许扩展程序具有误导性、格式不良、非描述性、不相关、过多或不适当的元数据，包括但不限于扩展程序描述、开发者名称、标题、图标、屏幕截图和宣传图片，”钓鱼邮件中写道。

具体来说，该扩展程序的开发人员会相信其软件的描述包含误导性信息，并且必须同意 Chrome 网上应用店政策。

![chrome-phishing-email.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250102/1735802872355920.png "1735802653144850.png")

攻击中使用的网络钓鱼电子邮件

如果开发人员点击嵌入的“转到策略”按钮来了解他们违反了哪些规则，他们就会被带到 Google 域上的恶意 OAuth 应用程序的合法登录页面。该页面是 Google 标准授权流程的一部分，旨在安全向第三方应用授予访问特定 Google 帐户资源的权限。

![page.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250102/1735802873104803.png "1735802695380977.png")

恶意认证请求

在该平台上，攻击者托管了一个名为“隐私策略扩展”的恶意 OAuth 应用程序，该应用程序要求受害者授予通过其帐户管理 Chrome Web Store 扩展程序的权限。 OAuth 授权页面上写道：“当您允许此访问时，隐私政策扩展程序将能够：查看、编辑、更新或发布您有权访问的 Chrome Web Store 扩展程序、主题、应用程序和许可证。”

![approval.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250102/1735802875112120.png "1735802732309856.png")

权限审批提示

多重身份验证无助于保护帐户，因为不需要 OAuth 授权流程中的直接批准，并且该过程假设用户完全了解他们授予的权限范围。

Cyberhaven 在事后分析报告中解释说：“该员工遵循标准流程，无意中授权了这个恶意第三方应用程序。”

据了解，该员工启用了 Google 高级保护，并对其帐户进行了 MFA，但没有收到 MFA 提示。该员工的 Google 凭据没有受到损害。

一旦威胁者获得了扩展程序开发人员帐户的访问权限，他们就会修改扩展程序以包含两个恶意文件，即“worker.js”和“content.js”，其中包含从 Facebook 帐户窃取数据的代码。

被劫持的扩展程序随后作为“新”版本发布在 Chrome 网上应用店上。虽然 Extension Total 正在跟踪受此网络钓鱼活动影响的 35 个扩展程序，但攻击中的 IOC 表明，目标数量要多得多。

据 VirusTotal 称，威胁者预先注册了目标扩展的域名，即使他们没有遭受攻击。虽然大多数域名是在 11 月和 12 月创建的，但威胁者在 2024 年 3 月就测试了此攻击。

![attack-subdomains.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250102/1735802876647569.png "1735802793443441.png")

网络钓鱼活动中早期使用的子域

**针对 Facebook 企业帐户**

对受感染机器的分析表明，攻击者的目标是中毒扩展程序用户的 Facebook 帐户。具体来说，数据窃取代码试图获取用户的 Facebook ID、访问令牌、帐户信息、广告帐户信息和企业帐户。

![facebook-data-stolen-by-extensions.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250102/1735802877213683.png "1735802854651429.png")

Facebook 数据被劫持的扩展程序窃取

此外，恶意代码还专门针对受害者在 Facebook.com 上的交互添加了鼠标点击事件监听器，寻找与平台的双因素身份验证或验证码机制相关的二维码图像。此举旨在绕过 Facebook 帐户的 2FA 保护，并允许威胁者劫持该帐户。

被盗信息将与 Facebook cookie、用户代理字符串、Facebook ID 和鼠标单击事件打包在一起，并渗透到攻击者的命令和控制 (C2) 服务器。威胁者一直通过各种攻击途径瞄准 Facebook 企业帐户，从受害者的信用直接付款到他们的帐户，在社交媒体平台上运行虚假信息或网络钓鱼活动，或者通过将其访问权限出售给其他人来货币化。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-details-reveal-how-hackers-hijacked-35-google-chrome-extensions/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tUHDWhs4)

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