---
title: XCon2023议题 | Golang安全：探索安全稳定的Hook方法
url: https://www.4hou.com/posts/9ABB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-20
fetch_date: 2025-10-04T11:59:08.243548
---

# XCon2023议题 | Golang安全：探索安全稳定的Hook方法

XCon2023议题 | Golang安全：探索安全稳定的Hook方法 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# XCon2023议题 | Golang安全：探索安全稳定的Hook方法

XCon组委会
[新闻](https://www.4hou.com/category/news)
2023-08-19 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)952226

收藏

导语：自动化，隐私保护，供应链安全，多云安全，深度学习的应用！

![640.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348389115781.jpg "1692348081164323.jpg")

**链链动未来·技术前瞻**

> 自动化，隐私保护，供应链安全，多云安全，深度学习的应用！
>
> **——腾讯云鼎实验室 高级安全研究员**
>
> **蒋浩天、王昊宇**

随着Golang在后端开发中的地位逐渐上升，**其高并发和多协程支持的优质特性让其成为了主流的后端开发语言**。然而，随之而来的是对于安全性的更高要求。为了满足这一需求，安全研究人员开始关注如何对基于Golang的后端服务进行安全加固和漏洞防御。在这个背景下，Hook技术变得不可或缺。

**Hook技术允许开发者通过修改或拦截代码的执行流程，实现对程序行为的监控和控制**。虽然可以对系统库或系统调用进行Hook，但这无法获得Golang内部更为详细的数据信息，尤其是有关程序上下文和执行流的信息。因此，**为了实现更高级别的监控和防御，我们需要深入到Golang内部进行Hook操作**。

在实践中，Hook技术也时刻面临着挑战。这些挑战涉及稳定性、兼容性、性能问题等多个层面，由于Golang的特殊性，Hook技术在其上的应用更为复杂，又因为Golang的并发模型、内存管理等方面与其他语言存在差异，也使得Hook变得更具难度。

为何在Golang中开发一个真正意义上的稳定的Hook框架如此困难？这其中的难点在哪里？现有的Hook框架存在哪些问题？Golang有哪些独特之处？在Hook的过程中又存在哪些不稳定因素？

为了解决这些问题，**本届XCon2023大会上，来自腾讯云鼎实验室的高级安全研究员 蒋浩天、王昊宇将带来议题《Golang安全：探索安全稳定的Hook方法》的分享，带领我们深入剖析Golang语言的特殊性，研究如何在Golang中实现真正意义上的安全稳定Hook，一同来探讨可能的解决方案，涵盖Hook框架的设计、实现和优化等方面**。最终，两位演讲者将分享他们开发的Golang Hook框架，该框架不仅考虑了Golang的特殊性，还解决了已有Hook框架存在的问题。

**议题简介**

**《Golang安全：探索安全稳定的Hook方法》**

Golang语言中，相对于C/C++等语言，存在很多特殊性的机制。这些机制方便了开发者，但是对于我们Hook来讲，还是会增加很多障碍。例如说Golang的协程栈迁移，扩容缩减，runtime变量逃逸分析，gc等机制都会影响我们Hook框架的健壮性。并且这些问题十分隐蔽，很难发现。**因此演讲者将在此次议题中，介绍如何发现各种潜在的问题，以及这些问题在现有Hook框架中存在的风险。**

**演讲人介绍**

**蒋浩天、王昊宇**

**腾讯云鼎实验室的高级安全研究员**

**![640 (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348390396817.jpg "1692348304171409.jpg")**

**蒋浩天，现就职于腾讯云鼎实验室，曾任职360，字节跳动。主要研究方向云安全，二进制安全，虚拟化等相关领域。曾在国内安全峰会多次发表议题。**

![640 (2).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348391252292.jpg "1692348371309874.jpg")

**王昊宇，现就职于腾讯安全云鼎实验室**，毕业于中国科学院大学，主要研究方向**云安全、二进制安全、协议安全**。曾发表论文于DATE、Inscrypt等会议。

**XCon2023**

**会议日程全曝光**

![640 (3).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348425136116.jpg "1692348425136116.jpg")

**☆购票通道同步开启**

**【链动者】¥0，展商互动区+XReward开放路演区可通行，不含闭门演讲、自助午餐及会刊**

**【先锋·造链者】¥2090，全场可通行，含闭门演讲+年度会刊（不含餐）。8月20日晚6点前购买，享此福利**

**【突围·造链者】¥2790，全场可通行，含闭门演讲+自助午餐+年度会刊**

**【全速·造链者】¥4500，仅限会议当日现场购买，不支持票券折扣**

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iPlvPGpv)

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

![](https://img.4hou.com/FgeSuF0KtB-UlpRnM5_Lap8oHIWx)

# [XCon组委会](https://www.4hou.com/member/k2wX)

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

[查看更多](https://www.4hou.com/member/k2wX)

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