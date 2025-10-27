---
title: 新的 DoubleClickjacking 攻击利用双击来劫持帐户
url: https://www.4hou.com/posts/vwJn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-27
fetch_date: 2025-10-06T20:08:03.852149
---

# 新的 DoubleClickjacking 攻击利用双击来劫持帐户

新的 DoubleClickjacking 攻击利用双击来劫持帐户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 DoubleClickjacking 攻击利用双击来劫持帐户

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-01-26 10:39:32

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)95164

收藏

导语：这种攻击几乎影响了所有网站，并分享了利用 DoubleClickjacking 接管 Shopify、Slack 和 Salesforce 帐户的演示视频。

点击劫持攻击的一种新变体称为“DoubleClickjacking”，攻击者可以诱骗用户使用双击授权敏感操作，同时绕过针对此类攻击的现有保护措施。

点击劫持，是指威胁者创建恶意网页，诱骗访问者点击隐藏或伪装的网页元素。这些攻击的工作原理是将隐藏 iframe 中的合法网页覆盖在攻击者创建的网页上。这个攻击者创建的网页旨在将其按钮和链接与隐藏 iframe 上的链接和按钮对齐。

然后，攻击者使用他们的网页来诱使用户单击链接或按钮，例如赢得奖励或查看某些图片。但是，当他们单击页面时，实际上是在单击隐藏 iframe（合法网站）上的链接和按钮，这可能会执行恶意操作，例如授权 OAuth 应用程序连接到其帐户或接受 MFA 请求。

多年来，网络浏览器开发人员引入了新功能来阻止大多数此类攻击，例如不允许跨站点发送 cookie 或引入关于站点是否可以构建 iframe 的安全限制（X-Frame-Options 或框架祖先）。

**新的 DoubleClickjacking 攻击**

网络安全专家 Paulos Yibelo 推出了一种名为 DoubleClickjacking 的新网络攻击，该攻击利用鼠标双击来诱骗用户在网站上执行敏感操作。

在这种攻击场景中，威胁者将创建一个网站，其中显示一个看似无害的带有诱惑的按钮，例如“单击此处”查看奖励或观看电影。当访问者单击该按钮时，将创建一个新窗口，覆盖原始页面并包含另一个诱惑，例如必须解决验证码才能继续。

在后台，原始页面上的 JavaScript 会将该页面更改为攻击者想要诱骗用户执行操作的合法站点。新的重叠窗口上的验证码会提示访问者双击页面上的某些内容来解决验证码问题。但是，此页面会侦听 mousedown 事件，并在检测到时快速关闭验证码覆盖层，从而导致第二次单击落在之前隐藏的合法页面上现在显示的授权按钮或链接上。

这会导致用户错误地单击公开的按钮，从而可能授权安装插件、OAuth 应用程序连接到其帐户或确认多重身份验证提示。

![double-clickjacking-attack-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250106/1736131753968329.png "1736131715642490.png")

DoubleClick劫持攻击流程

之所以如此危险，是因为它绕过了所有当前的点击劫持防御，因为它不使用 iframe，也不会尝试将 cookie 传递到另一个域。相反，这些操作直接发生在不受保护的合法网站上。

Yibelo 表示，这种攻击几乎影响了所有网站，并分享了利用 DoubleClickjacking 接管 Shopify、Slack 和 Salesforce 帐户的演示视频。

研究人员还说，这种攻击不仅限于网页，还可以用于浏览器扩展。“例如，我已经对顶级浏览器加密钱包进行了概念验证，这些钱包使用这种技术来授权 web3 交易和 dApp 或禁用 VPN 来暴露 IP 等，”Yibelo 解释道。

这也可以在手机中通过要求目标‘DoubleTap’来完成。为了防止此类攻击，安全研究员共享了 JavaScript，可以将其添加到网页中以禁用敏感按钮，直到有所反应为止。这将防止双击在删除攻击者的覆盖层时自动点击授权按钮。

除此之外，研究人员还提出了一个潜在的 HTTP 标头，该标头可以限制或阻止双击序列期间窗口之间的快速上下文切换。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-doubleclickjacking-attack-exploits-double-clicks-to-hijack-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?3LUvEugV)

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