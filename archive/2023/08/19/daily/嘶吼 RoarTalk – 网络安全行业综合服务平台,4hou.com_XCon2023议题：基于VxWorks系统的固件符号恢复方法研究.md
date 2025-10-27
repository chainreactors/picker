---
title: XCon2023议题：基于VxWorks系统的固件符号恢复方法研究
url: https://www.4hou.com/posts/5wxK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-19
fetch_date: 2025-10-04T11:59:26.929913
---

# XCon2023议题：基于VxWorks系统的固件符号恢复方法研究

XCon2023议题：基于VxWorks系统的固件符号恢复方法研究 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# XCon2023议题：基于VxWorks系统的固件符号恢复方法研究

XCon组委会
[新闻](https://www.4hou.com/category/news)
2023-08-18 10:59:07

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)968324

收藏

导语：本届XCon2023大会中，来自山石网科通信技术股份有限公司安全技术研究院的安全研究员王正涵将带来《基于VxWorks系统的固件符号恢复方法研究》的议题分享。

![640.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692327694213135.png "1692327694213135.png")

**未来5年，物联网领域的技术趋势预测：**

1、物联网设备的数量和多样性的增长，将导致**更多的安全威胁和攻击面；**

2、物联网设备的智能化和自主化，将导致**更多的数据和计算能力分布在边缘和雾层；**

3、物联网设备的跨领域和跨平台的集成，将导致**更多的协作和互操作性的需求；**

4、物联网设备的安全评估和认证，将导致**更多的标准和规范的制定和遵守；**

5、物联网设备的安全防护和恢复，将导致**更多的技术和方法的创新和应用。**

——山石网科通信技术股份有限公司

安全技术研究院安全研究员  王正涵

**VxWorks 操作系统是美国WindRiver公司于1983年设计开发的一种嵌入式实时操作系统（RTOS），**是嵌入式开发环境的关键组成部分。凭借良好的持续发展能力、高性能的内核以及友好的用户开发环境，Vxworks在嵌入式实时操作系统领域占据一席之地。

**“高可靠性”和“强实时性”，使得VxWorks广泛地应用于通信、军事、航空、航天等高精尖技术及实时性要求极高的领域中，**如卫星通讯、军事演习、弹道制导、飞机导航等，也因为应用领域的特殊性与关键性，VxWorks的系统安全一直备受技术人员的关注。

2019年该系统就曾被爆出存在多个高危漏洞，面临严重的RCE攻击风险。研究者称“漏洞会导致内存损坏，并造成远程代码执行”。随后系统方对漏洞进行了更新修复，**但由于VxWorks系统设备的固件通常是无符号的静态编译的二进制文件，缺乏符号信息和调试信息，也导致系统的固件分析和漏洞挖掘持续面临着巨大挑战。**

**本届XCon2023大会中，来自山石网科通信技术股份有限公司安全技术研究院的安全研究员王正涵将带来《基于VxWorks系统的固件符号恢复方法研究》的议题分享，**旨在基于研究VxWorks漏洞挖掘的目的，对无符号静态编译的VxWorks固件系统进行深入研究，**探索通用的固件分析方法和工具。**

**议题简介**

**《基于VxWorks系统的固件符号恢复方法研究》**

本议题**将介绍加载地址分析方法、符号恢复方法具体实现过程和技术细节，以及遇到的问题和解决方案。**希望能够为VxWorks系统设备的安全分析和保护提供一些参考和启示。

**演讲人介绍**

**王正涵——山石网科通信技术股份有限公司 安全技术研究院 安全研究员**

**![640 (2).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692328052399449.jpg "1692328052399449.jpg")**

**王正涵，**就职于山石网科通信技术股份有限公司，在安全技术研究院部门担任安全研究员。**主要从事二进制方向的安全研究、IoT设备漏洞挖掘、Linux内核漏洞挖掘等工作。**

山石安全技术研究院成立于2020年，是公司的信息安全智库与创新部门，旗下包括智能、应用、工控、信创和核心基础等五大实验室，输出原创漏洞、安全专利、原创文章、安全议题等研究成果，不断提供新的漏洞证书、致谢与编号。

**XCon2023**

**会议日程全曝光**

![640 (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692328124165028.jpg "1692328124165028.jpg")

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

![](https://www.4hou.com/captcha/flat?Zkgl6Enj)

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