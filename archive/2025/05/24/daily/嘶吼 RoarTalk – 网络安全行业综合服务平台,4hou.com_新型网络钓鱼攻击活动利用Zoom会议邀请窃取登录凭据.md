---
title: 新型网络钓鱼攻击活动利用Zoom会议邀请窃取登录凭据
url: https://www.4hou.com/posts/RXVO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-24
fetch_date: 2025-10-06T22:27:37.729798
---

# 新型网络钓鱼攻击活动利用Zoom会议邀请窃取登录凭据

新型网络钓鱼攻击活动利用Zoom会议邀请窃取登录凭据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型网络钓鱼攻击活动利用Zoom会议邀请窃取登录凭据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-23 11:59:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61529

收藏

导语：鼓励各组织在所有平台上采用多因素身份验证（MFA），以增加额外的安全层，即使凭证被泄露也应该及时采取此类措施。

一个新发现的网络钓鱼活动通过伪装成Zoom紧急会议邀请来瞄准用户。这种欺骗策略利用对工作场所通信相关的熟悉和信任来诱骗受害者进入旨在窃取其登录凭证的陷阱当中。

网络安全研究人员对这种攻击进行了标记。在一个假的会议页面，上面有一段所谓“参与者”的视频，恶意分子以此来制造一种虚假的合法性。邮件主题和内容中隐含的紧迫性会迫使收件人不假思索地点击恶意链接。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250520/1747724336156642.png "1747724249166979.png")

— SpiderLabs (@SpiderLabs)

**精心设计的诈骗邮件仿冒**

这些网络钓鱼邮件制作精良，模仿了 Zoom 正式通知的品牌标识和格式，以降低用户的警惕性。

一旦用户点击嵌入的链接，他们就会被重定向到一个假冒的会议页面，该页面会提示他们输入 Zoom 凭证或其他敏感信息。

此页面托管在乍一看合法但实际上经过细微篡改以逃避粗略审查的域名上。

在幕后，被盗的数据很可能会通过被攻破的应用程序编程接口（API）或消息服务被传送给攻击者，从而实现凭证的迅速外泄，以便进一步加以利用。

专家警告称，此类攻击往往会导致更广泛的网络入侵，因为被盗的凭证可被用于访问企业系统，从而形成一个不断被攻破的恶性循环。

**攻击机制的技术剖析**

网址中使用个性化参数，例如目标 ID 和用户名，表明攻击者可能利用了先前泄露的数据或侦察信息来定制其网络钓鱼尝试，从而使其更具说服力。

这种高度定制化的程度表明与普通的网络钓鱼活动相比，它更加复杂，因为它利用了特定的用户信息来提高电子邮件的可信度。

安全研究人员强烈建议用户应避免点击可疑链接，并通过已知的通信渠道直接联系发件人或手动导航到Zoom平台来验证任何意外的会议邀请的真伪。

攻击者的策略也依赖于心理操纵，利用人们害怕错过重要会议或未及时回复同事时的不安。这种社会工程学手段在快节奏的工作环境中特别有效，因为员工可能没有时间仔细检查每封电子邮件。

此外，网络安全意识培训仍然是一个重要的防御措施，实施像MailMarshal这样的电子邮件过滤解决方案也是如此，以在威胁到达收件箱之前检测和阻止这些威胁。

鼓励各组织在所有平台上采用多因素身份验证（MFA），以增加额外的安全层，即使凭证被泄露也应该及时采取此类措施。

文章翻译自：https://gbhackers.com/new-phishing-attack-poses-as-zoom-meeting/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?CDeQ4rvE)

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