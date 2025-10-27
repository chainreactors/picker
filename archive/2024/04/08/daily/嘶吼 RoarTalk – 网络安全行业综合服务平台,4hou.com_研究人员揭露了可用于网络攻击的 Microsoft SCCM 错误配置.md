---
title: 研究人员揭露了可用于网络攻击的 Microsoft SCCM 错误配置
url: https://www.4hou.com/posts/wyGX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-04-08
fetch_date: 2025-10-04T12:14:42.212086
---

# 研究人员揭露了可用于网络攻击的 Microsoft SCCM 错误配置

研究人员揭露了可用于网络攻击的 Microsoft SCCM 错误配置 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 研究人员揭露了可用于网络攻击的 Microsoft SCCM 错误配置

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-04-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)202464

收藏

导语：对于各种攻击方式，研究人员给出了保护环境免受攻击技术侵害的办法。

安全研究人员基于 Microsoft 配置管理器的不当设置，创建了攻击和防御技术的知识库存储库，这将允许攻击者执行有效负载或成为域控制器。

配置管理器 (MCM) 称为系统中心配置管理器（SCCM、ConfigMgr），自 1994 年以来一直存在，并存在于许多 Active Directory 环境中，帮助管理员管理 Windows 网络上的服务器和工作站。

十多年来，它一直是安全研究的对象，作为可以帮助对手获得 Windows 域管理权限的攻击面。

在SO-CON 安全会议上 ，SpectreOps 研究人员宣布发布 Misconfiguration Manager，这是一个基于错误 MCM 配置进行攻击的存储库，还为防御者提供资源以强化其安全立场。

SpectreOps 解释说：“我们的方法不仅限于对已知对手的策略进行分类，还包括渗透测试、红队行动和安全研究领域的贡献。”MCM/SCCM 的设置并不容易，而且许多默认配置都为攻击者留下了可乘之机。

**获取域控制**

SpectreOps 研究人员指出，研究人员在其工作中看到的最常见且最具破坏性的错误配置是具有过多特权的网络访问帐户 (NAA)。

谈到 MCM/SCCM，研究人员表示，“配置起来非常困难，新手或不知情的管理员可能会选择使用相同的特权帐户来完成所有操作。”

在工作期间，他们遇到了一种场景，该场景从损害标准用户的 SharePoint 帐户到成为域控制器，这一切都是由于 MCM 的 MCM 部署配置错误以及特权过高的 NAA 造成的。

在另一个示例中，研究人员表示配置管理器站点可以将域控制器注册为客户端，如果站点层次结构设置不正确，这会带来远程代码执行的风险。

为了进一步证明 MCM/SCCM 部署配置错误的风险，研究人员概述了相关经验，团队能够进入 MCM/SCCM 的中央管理站点 (CAS) 数据库并授予自己完整的管理员角色。

从那里他们可以通过使用配置管理器，在先前植入域客户端网络共享上的有效负载上执行来进一步破坏环境。

**攻击与防御方法**

由 Chris Thompson、Garrett Foster和 Duane Michael创建的Misconfiguration  Manager存储库旨在帮助管理员更好地了解 Microsoft 的工具，并“为防御者简化 SCCM 攻击路径管理，同时对攻击性专业人员进行有关这一模糊攻击面的培训”。

目前，该存储库描述了 22 种可用于直接攻击 MCM/SCCM 或在后利用阶段利用它的技术。

![MisconfigurationManager.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240312/1710232050495399.jpg "1710231626179506.jpg")

错误配置管理器技术的攻击矩阵

根据环境的不同，所描述的技术可能允许访问凭证 (CRED)、提升权限 (ELEVATE)、执行侦察和发现 (RECON) 或获得对 MCM/SCCM 层次结构的控制 (TAKEOVER)。

对于每种攻击方法，研究人员还提供了保护环境免受每种攻击技术侵害的信息。

**三类防御行动：**

**预防：**直接减轻或影响攻击技术的配置更改

**检测：**检测各种攻击技术的指南和策略

**CANARY：**基于欺骗的检测策略，使用攻击者经常滥用的功能

考虑到它被广泛采用并且必须安装在 Active Directory 域中，如果配置不当，MCM/SCCM 可能会降低公司的安全状况，这项任务适合经验丰富的管理员。

尽管错误配置管理器的创建者已经进行了测试，但建议管理员在生产环境实施之前尽量再测试一遍存储库中提供的防御方法。

文章翻译自：https://www.bleepingcomputer.com/news/security/researchers-expose-microsoft-sccm-misconfigs-usable-in-cyberattacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?g2FtIFaX)

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