---
title: 黑客欺骗Microsoft ADFS登录页面以窃取凭据
url: https://www.4hou.com/posts/OGGE
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-14
fetch_date: 2025-10-06T20:33:53.558496
---

# 黑客欺骗Microsoft ADFS登录页面以窃取凭据

黑客欺骗Microsoft ADFS登录页面以窃取凭据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客欺骗Microsoft ADFS登录页面以窃取凭据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63559

收藏

导语：这些攻击旨在访问公司电子邮件帐户，以将电子邮件发送给组织内的其他受害者或进行经济动机的攻击（例如商业电子邮件妥协（BEC）），在此付款转移到威胁者的帐户中。

服务台网络钓鱼活动主要针对Microsoft Active Directory Federation Services（ADFS），使用欺骗性的登录页面来窃取凭据和绕过多因素身份验证（MFA）保护措施。据发现该攻击的安全公司称，此次攻击的目标主要是教育、医疗和政府机构，攻击目标至少有150个。

这些攻击旨在访问公司电子邮件帐户，以将电子邮件发送给组织内的其他受害者或进行经济攻击（例如商业电子邮件妥协（BEC）），在此付款转移到威胁者的帐户中。

**欺骗Microsoft Active Directory联合服务**

Microsoft Active Directory Federation Services（ADFS）是一个身份验证系统，允许用户登录一次并访问多个应用程序和服务，而无需重复输入其凭据。它通常在大型组织中用于在基于内部和云的应用程序中提供单登录（SSO）。

攻击者会向冒充其公司IT团队的目标发送电子邮件，要求他们登录以更新其安全设置或接受新策略。

![phish.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250206/1738836516164636.png "1738823819730034.png")

攻击中使用的网络钓鱼电子邮件示例

点击“嵌入式”按钮会将受害者带到一个看起来与他们组织的真实ADFS登录页面一模一样的网络钓鱼网站。网络钓鱼页面要求受害人输入其用户名，密码和MFA代码，或引导他们批准推送通知。

![spoofed-portals.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250206/1738836518585904.png "1738823868149995.png")

欺骗的ADFS门户

网络钓鱼模板还包括基于组织配置的MFA设置来捕获验证目标帐户所需的特定第二因素的表单，针对多种常用MFA机制的异常观察到的模板，包括Microsoft Authenticator，Duo Security和SMS验证。

![mfa-bypass.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250206/1738836520199543.png "1738823913204719.png")

两个可用的MFA旁路屏

一旦受害者提供了所有详细信息，他们就会被重定向到合法的登录页面，以减少怀疑，并使其看起来好像这个过程已经成功完成。

同时，攻击者立即利用窃取的信息登录受害者的帐户，窃取任何有价值的数据，创建新的电子邮件过滤规则，并尝试横向网络钓鱼。

安全公司表示，攻击者在这次活动中使用私人互联网接入VPN来掩盖他们的位置，并分配一个更接近组织的IP地址。

即使这些网络钓鱼攻击并没有直接违反ADF，而是依靠社会工程来工作，但由于许多用户对登录工作流的固有信任，该策略仍然是具有潜在有效性的。

安全工作人员建议相关企业应迁移到现代和更安全的解决方案，如Microsoft Entra，并引入额外的电子邮件过滤器和异常活动检测机制，以尽早阻止网络钓鱼攻击。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-spoof-microsoft-adfs-login-pages-to-steal-credentials/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9H2mAHSm)

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