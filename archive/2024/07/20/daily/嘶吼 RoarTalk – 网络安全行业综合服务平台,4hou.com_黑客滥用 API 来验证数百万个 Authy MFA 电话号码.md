---
title: 黑客滥用 API 来验证数百万个 Authy MFA 电话号码
url: https://www.4hou.com/posts/QXWL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-20
fetch_date: 2025-10-06T17:41:28.420048
---

# 黑客滥用 API 来验证数百万个 Authy MFA 电话号码

黑客滥用 API 来验证数百万个 Authy MFA 电话号码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客滥用 API 来验证数百万个 Authy MFA 电话号码

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-19 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)99388

收藏

导语：Authy 用户还应确保其移动帐户配置为在未提供密码或关闭安全保护的情况下阻止号码转移。

Authy 是一款移动应用程序，可在启用 MFA 的网站上生成多因素身份验证码。

6 月底，一个名为 ShinyHunters 的威胁分子泄露了一个 CSV 文本文件，其中包含他们声称的在 Authy 服务上注册的 3300 万个电话号码。

Twilio 已确认，不安全的 API 端点允许威胁分子验证数百万 Authy 多因素身份验证用户的电话号码，而这使他们很容易就受到短信网络钓鱼和 SIM 卡交换攻击。

![shinyhunters-twilio.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720427308177748.png "1720425695177703.png")

ShinyHunters 在黑客论坛上分享 Twilio Authy 数据

该 CSV 文件包含 33,420,546 行，每行包含一个帐户 ID、电话号码、一个“over\_the\_top”列、帐户状态和设备数量。

Twilio 现已证实，威胁分子使用未经身份验证的 API 端点编制了电话号码列表。Twilio 检测到威胁分子能够通过未经身份验证的端点识别，与 Authy 帐户相关的数据，包括电话号码。目前，Twilio 已采取措施保护此端点，不再允许未经身份验证的请求。

Twilio 接受媒体采访时表示“没有看到任何证据表明威胁分子获得了 Twilio 系统或其他敏感数据的访问权限。作为预防措施，我们要求所有 Authy 用户更新到最新的 Android 和 iOS 应用程序以获取最新的安全更新，并鼓励所有 Authy 用户保持警惕并提高对网络钓鱼和短信钓鱼攻击的认识。”

早在2022 年，Twilio 就披露其在 6 月和 8 月遭受了入侵，威胁分子得以入侵其基础设施并访问 Authy 客户信息。

**滥用不安全的 API**

据获悉，这些数据是通过将大量电话号码列表输入不安全的 API 端点汇编而成的。如果号码有效，端点将返回有关在 Authy 注册的关联帐户的信息。

现在该 API 已经得到保护，它不再被滥用来验证电话号码是否与 Authy 一起使用。

这种技术类似于威胁分子滥用不安全的 Twitter API 和 Facebook API 来编译包含公开和非公开信息的数千万用户的个人资料。

虽然 Authy 抓取的数据仅包含电话号码，但对于想要通过短信网络钓鱼和 SIM 卡交换攻击来窃取账户的用户来说，它们仍然是有利的。

ShinyHunters 在他们的帖子中提到了这一点，并表示“你们可以在 gemini 或 Nexo db 上加入”，建议威胁分子将电话号码列表与所谓的 Gemini 和 Nexo 数据泄露中泄露的电话号码列表进行比较。

如果发现匹配，威胁分子可能会尝试执行 SIM 卡交换攻击或网络钓鱼攻击来破坏加密货币交易账户并窃取所有资产。

Twilio 现已发布新的安全更新，并建议用户升级到包含安全更新的 Authy Android (v25.1.0) 和 iOS App (v26.1.0)。目前尚不清楚此安全更新如何帮助保护用户免受威胁者利用抓取的数据进行攻击。

Authy 用户还应确保其移动帐户配置为在未提供密码或关闭安全保护的情况下阻止号码转移。此外，Authy 用户应警惕潜在的短信网络钓鱼攻击，这些攻击试图窃取更敏感的数据，例如密码。

在一次看似无关的泄露事件中，Twilio 也开始发送数据泄露通知，因为第三方供应商不安全的 AWS S3 存储桶暴露了通过该公司发送短信的相关数据。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-abused-api-to-verify-millions-of-authy-mfa-phone-numbers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iChl2v04)

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