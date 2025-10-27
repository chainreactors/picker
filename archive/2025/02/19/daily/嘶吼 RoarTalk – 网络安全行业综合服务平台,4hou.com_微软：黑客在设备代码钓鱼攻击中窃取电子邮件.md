---
title: 微软：黑客在设备代码钓鱼攻击中窃取电子邮件
url: https://www.4hou.com/posts/wxxX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-19
fetch_date: 2025-10-06T20:36:01.305724
---

# 微软：黑客在设备代码钓鱼攻击中窃取电子邮件

微软：黑客在设备代码钓鱼攻击中窃取电子邮件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微软：黑客在设备代码钓鱼攻击中窃取电子邮件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)75863

收藏

导语：使用相同的刷新令牌和新的设备标识，Storm-2372能够获得主刷新令牌（PRT）并访问其资源。目前已经观察到Storm-2372使用连接的设备收集电子邮件。

据安全研究员观察发现，一个可能与俄罗斯有关联的威胁者发起的活跃攻击活动，正利用设备代码钓鱼手段针对个人微软 365 账户进行攻击。

这些攻击目标涉及欧洲、北美、非洲和中东地区的政府、非政府组织、信息技术服务和科技、国防、电信、医疗以及能源/石油和天然气行业。

微软威胁情报中心将此次设备代码钓鱼活动背后的威胁者追踪为“风暴-237”。基于受害者特征和作案手法，研究人员认为，该活动与符合俄罗斯利益的国家行为有关。

**设备代码钓鱼攻击**

输入受限设备——那些缺少键盘或浏览器支持的设备，比如智能电视和某些物联网设备，依靠代码认证流程让用户通过在另一台设备（如智能手机或电脑）上输入授权码来登录应用程序。

微软研究人员发现，自去年 8 月以来，Storm-2372 通过诱骗用户在合法的登录页面输入攻击者生成的设备代码，滥用这种身份验证流程。

这些特工人员首先通过在 WhatsApp、Signal 和 Microsoft Teams 等消息平台上“冒充与目标有关的知名人士”与目标建立联系，然后才发起攻击。

![messages.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250217/1739761935117731.png "1739761510694932.png")

Storm-2372发送到目标的消息

威胁者会在通过电子邮件或短信发送虚假的在线会议邀请之前，与受害者逐渐建立起一种融洽的关系。根据研究人员的说法，受害者收到一个团队会议邀请，其中包括攻击者生成的设备代码。

微软表示：“这些邀请会引诱用户完成设备代码认证请求，模拟消息传递服务，这为Storm-2372提供了对受害者账户的初始访问权限，并启用了Graph API数据收集活动，如电子邮件收集。”

只要被盗的令牌有效，黑客就可以在不需要密码的情况下访问受害者的微软服务（电子邮件、云存储）。

![flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250217/1739761936922813.png "1739761805567738.png")

设备代码网络钓鱼攻击概述

然而，微软表示，攻击者现在正在设备代码登录流中使用Microsoft Authentication Broker的特定客户端ID，这允许他们生成新的令牌。

这开启了新的攻击和持久化可能性，因为攻击者可以使用客户端ID将设备注册到微软基于云的身份和访问管理解决方案Entra ID。

使用相同的刷新令牌和新的设备标识，Storm-2372能够获得主刷新令牌（PRT）并访问其资源。目前已经观察到Storm-2372使用连接的设备收集电子邮件。

**防御风暴2372**

为了对抗Storm-2372使用的设备代码钓鱼攻击，微软建议在可能的情况下阻止设备代码流，并在微软Entra ID中执行条件访问策略，以限制其对可信设备或网络的使用。

如果怀疑设备代码网络钓鱼，立即使用‘revokeSignInSessions’撤销用户的刷新令牌，并设置条件访问策略来强制受影响的用户重新认证。

最后，使用Microsoft Entra ID的登录日志来监视并快速识别短时间内大量的身份验证尝试、来自无法识别的ip的设备代码登录，以及发送给多个用户的设备代码身份验证的意外提示。

文章翻译自：https://www.bleepingcomputer.com/news/security/microsoft-hackers-steal-emails-in-device-code-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?aU8kP5ht)

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