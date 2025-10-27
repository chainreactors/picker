---
title: 勒索软件利用间歇性加密躲避检测算法
url: https://www.4hou.com/posts/xjNJ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-12
fetch_date: 2025-10-04T03:38:19.807573
---

# 勒索软件利用间歇性加密躲避检测算法

勒索软件利用间歇性加密躲避检测算法 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件利用间歇性加密躲避检测算法

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-11 11:11:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)150740

收藏

导语：一些勒索软件组织现正在使用一种新的方法来试图绕过这些检测。

![p1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663546258214319.jpeg "1663546258214319.jpeg")

大多数开展索软件活动的网络犯罪分子都备受关注。他们不仅遭到执法部门和安全公司的调查，就连他们从技术上传播恶意软件的方式以及恶意软件在受感染计算机上运行和工作的方式也受到严密调查。

SentinelOne公司的一份新报告披露了一些勒索软件组织采用的一种新技术，这种最近在外头盛行的技术名为“间歇性加密”（intermittent encryption）。

**什么是间歇性加密？**

这个术语可能令人困惑，因此立即予以澄清似乎很重要：间歇性加密不是旨在加密所选择的完整文件，而是选择性加密文件中的部分字节。

据研究人员声称，间歇性加密让攻击者可以更有效地规避使用统计分析来检测当前勒索软件感染的系统。这种分析基于操作系统文件输入和输出操作的强度，即基于文件的已知版本与可疑修改版本之间的相似性。因此，间歇性加密降低了文件输入/输出操作的强度，在某个特定文件的非加密版本和加密版本之间表现出极高的相似性，因为文件中只有一些字节被更改。

间歇性加密还具有在很短的时间内加密较少内容但仍导致系统无法使用的好处，这使得在感染时间和加密内容时间之间检测勒索软件活动变得更困难了。

针对使用不同文件大小的BlackCat勒索软件的研究表明，间歇性加密为威胁分子在速度方面带来了显著优势。

LockFile勒索软件是2021年年中第一个使用间歇性加密的恶意软件系列，不过现在有几个不同的勒索软件系列也在使用它。

**哪些威胁组织在使用间歇性加密？**

同样重要的是要知道间歇性加密在众多地下论坛中变得越来越流行，地下论坛在大力宣传间歇性加密，以吸引更多的买家或勒索软件组织加盟机构。

**• Qyick勒索软件**

SentinelOne的研究人员报告，他们在暗网的一个流行犯罪论坛上看到了一个名为Qyick的新型商业勒索软件所打的广告。名为lucrostm的广告商此前被发现在兜售其他软件，比如远程访问工具（RAT）和恶意软件加载程序，并出售 Qyick，价格从0.2个比特币到约1.5个比特币不等，具体取决于买家想要的功能选项。Lucrostm作出的保证之一是，如果勒索软件系列的二进制文件在购买后六个月内被安全解决方案检测出来，未检测到的新勒索软件样本将给予60%至80%的大幅折扣。

该勒索软件是用Go语言编写的，据开发人员声称，这有望加快勒索软件的运行，此外使用间歇性加密（图1）。

![p2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220919/1663546283117357.jpeg "1663546283117357.jpeg")

图1. 网络犯罪地下论坛上的Qyick勒索软件广告（来源：SentinelOne）

Qyick仍然是一种正在开发中的勒索软件。虽然它现在没有将数据外泄的功能，但未来版本将让控制者可以执行任意代码，主要用于此目的。

**• PLAY勒索软件**

该勒索软件于2022年6月首次露面。它根据当前文件的大小使用间歇性加密。它以十六进制加密0x100000字节块（十进制为1048576字节），并根据文件大小加密两个、三个或五个块。

**• Agenda勒索软件**

这个勒索软件是另一种用Go语言编写的勒索软件。它支持控制者可以配置的几种不同的间歇性加密方法。

第一种方法名为“skip-step”，让攻击者可以加密文件的每X MB（兆字节），跳过指定MB数量的部分。第二种方法名为“fast”，允许只加密文件的前N MB部分。最后一种方法名为“percent”，允许只加密文件的一部分。

**•Black Basta勒索软件**

这个勒索软件自2022年4月以来一直充当勒索软件即服务（RaaS）。它是用C++语言编写的，其运营团伙一直将它与双重勒索结合使用，如果受害者不支付赎金，就扬言要泄露数据。

Black Basta的间歇性加密方法每加密64个字节，就跳过192个字节，如果文件大小不到4KB。如果文件大于4KB，该勒索软件每加密64个字节，就跳过128个字节，而不是跳过192个字节。

**• BlackCat/ALPHV**

BlackCat又叫ALPHV，是一种用Rust语言开发的勒索软件，被用作RaaS模式。该威胁组织很早就擅长使用勒索手段，比如通过数据泄露或分布式拒绝服务（DDoS）攻击来威胁其受害者。

BlackCat勒索软件为控制者提供了几种不同的加密模式，从完全加密到集成间歇性加密的模式：它提供仅加密文件前N个字节的功能，或者每加密N个字节就跳过X个字节的功能。

它还拥有更高级的加密功能，比如将文件分成不同大小的块，只加密每个块的前P个字节。

除了间歇性加密，BlackCat还包含一些尽可能加快速度的逻辑功能：如果被感染的计算机支持硬件加速，该勒索软件使用AES（高级加密标准）进行加密。要不然，它就使用完全用软件实现的ChaCha20算法。

**如何防范这种威胁？**

建议始终确保操作系统及在其上面运行的所有软件是最新版本，并打上补丁，避免受到常见漏洞的影响。

还建议在勒索软件在一台或多台计算机上被植入之前，部署安全解决方案以尝试检测威胁。

如果有可能，应尽量部署多因素身份验证，以便攻击者无法仅使用凭据就能访问可以运行勒索软件的网络部分。

应该提高每个用户的安全意识，尤其是电子邮件方面的意识，因为电子邮件是勒索软件最常用的感染途径之一。

本文翻译自：https://www.techrepublic.com/article/ransomware-makes-use-of-intermittent-encryption-to-bypass-detection-algorithms/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5TFQ1ezG)

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