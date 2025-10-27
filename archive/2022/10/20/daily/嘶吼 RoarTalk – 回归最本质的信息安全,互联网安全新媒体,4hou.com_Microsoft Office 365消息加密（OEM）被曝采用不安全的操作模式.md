---
title: Microsoft Office 365消息加密（OEM）被曝采用不安全的操作模式
url: https://www.4hou.com/posts/17No
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:53.310397
---

# Microsoft Office 365消息加密（OEM）被曝采用不安全的操作模式

Microsoft Office 365消息加密（OEM）被曝采用不安全的操作模式 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Microsoft Office 365消息加密（OEM）被曝采用不安全的操作模式

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)159628

收藏

导语：Microsoft Office的云版本中所用的默认电子邮件加密可泄露信息，该公司承认了这个问题，但表示不会修复。

**概述**

Microsoft Office 365消息加密（OME）采用电子密码本（ECB）操作模式。这种模式通常是不安全的，可能会泄露所发送消息的结构方面的信息，这可能导致部分或全部消息泄露。正如美国国家标准与技术研究所（NIST）发布的《提议修订特别出版物800-38A 的公告》所述：“在NIST全国漏洞数据库（NVD）中，使用ECB加密机密信息构成了严重的安全漏洞；比如，参阅CVE-2020 -11500：https://nvd.nist.gov/vuln/detail/CVE-2020-11500。”

**描述**

Microsoft Office 365提供了一种发送加密消息的方法。微软声称该功能让组织可以以一种安全的方式在组织内外的人员之间发送和接收加密的电子邮件。遗憾的是，OME消息是在不安全的电子密码本（ECB）操作模式下被加密的。

**影响**

由于ECB泄露了消息的某些结构信息，如果第三方可以访问加密电子邮件消息，也许就能够识别消息内容。这会导致机密性可能丧失。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221015/1665800256645946.png "1665800256645946.png")

图1. 从Office 365邮件加密保护的电子邮件中提取的图像

由于加密消息是作为常规电子邮件附件发送的，因此发送的消息可能会存储在各种电子邮件系统中，可能已被发送者和接收者之间的任何有关方截获。

如果攻击者拥有庞大的消息数据库，可以通过分析截获消息的重复部分的相对位置，推断其内容（或部分内容）。

大多数OME加密消息都受到影响，攻击者可以对任何之前发送、接收或截获的加密消息离线执行攻击。组织无法阻止已经发送的消息被人分析，也无法使用权限管理功能来解决这个问题。

视通过加密消息发送的内容而定，一些组织可能需要考虑该漏洞的法律影响。正如欧盟《通用数据保护条例》（GDPR）、《加利福尼亚州消费者隐私法》（CCPA）或其他类似法规所述，漏洞可能会导致隐私受到影响。

**细节**

电子密码本（ECB）操作模式意味着每个密码块都单独加密。明文消息的重复块总是映射到相同的密文块。实际上，这意味着虽然实际的明文并不直接显示，但消息结构方面的信息却直接显示。这是在ECB操作模式下经过AES加密的RAW图像：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221015/1665800329184554.png "1665800329184554.png")

虽然不知道实际的单个像素值，但可以轻松识别图像的实际内容。

即使特定消息不会以这种方式直接泄露信息，拥有大量消息的攻击者仍可以分析文件中重复模式的关系来识别特定文件。这可能导致加密消息的（部分）明文能够推断出来。

不需要知道加密密钥就可以利用该漏洞，因此自带密钥（BYOK）或类似的加密密钥保护措施没有任何补救方面的影响。

用于Microsoft Office 365消息加密的密码似乎是高级加密标准（AES）。然而面对这个漏洞，实际的密码无关紧要，因为无论使用何种密码，ECB操作模式都具有相同的属性。

**CWE-327：使用损坏或有风险的加密算法**

Outlook 365消息加密在将邮件加密成RPMSG blob时使用电子密码本（ECB）操作模式。

这个漏洞的根本原因似乎是事先决定使用具有消息加密功能的电子密码本（ECB）操作模式，然后一直采用这个糟糕的决定。

Microsoft信息保护（MIP）ProtectionHandler::PublishingSettings类有一个 SetIsDeprecatedAlgorithmPreferred方法，文档对该方法描述如下：

“设置是否优先使用被废弃的加密算法（ECB）以实现向后兼容性。”

OME很可能使用这种方法来启用RPMSG的ECB加密。如果未设置该标志，则使用密码块链接（CBC）操作模式。

Microsoft信息保护FIPS 140-2 合规文档提到：

“旧版Office（2010）需要AES 128 ECB，而Office文档仍以这种方式受到Office应用程序的保护。”

**缓解措施**

在多次询问漏洞状态后，微软最终回复如下：

“我们认为漏洞报告不符合安全服务标准，也不被认为是泄密事件。没有更改代码，因此没有为此报告发布CVE。”

电子邮件系统的最终用户或管理员无法强制执行更安全的操作模式。由于微软没有计划修复该漏洞，唯一的缓解措施是避免使用Microsoft Office 365消息加密。

**资料卡**

类型：使用损坏或有风险的加密算法

严重程度：很高

受影响的产品：Microsoft Office 365

缓解措施：由于微软没有计划修复这个漏洞，唯一的缓解措施就是避免使用Microsoft Office 365 消息加密。

感谢：感谢WithSecure Consulting公司的Harry Sintonen发现漏洞。

参考：MSRC VULN-060517

时间线

2022-01-11 发现漏洞。通过MSRC报告该漏洞，编号为VULN-060517。

2022-01-19 微软发放赏金5000美元。

2022-05-19 就问题的状态与微软取得联系，没有收到回复。

2022-08-29 向微软告知计划公开披露。

2022-09-21 微软对此问题进行了跟进，声称“我们认为漏洞报告不符合安全服务标准，也不被认为是泄密事件。没有更改代码，因此没有为此报告发布CVE。”

2022-10-14 WithSecure发布公告。

本文翻译自：https://labs.withsecure.com/advisories/microsoft-office-365-message-encryption-insecure-mode-of-operation如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TVhTZs6P)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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