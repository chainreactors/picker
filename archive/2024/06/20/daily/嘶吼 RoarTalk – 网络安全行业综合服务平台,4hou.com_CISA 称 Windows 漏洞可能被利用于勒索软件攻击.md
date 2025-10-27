---
title: CISA 称 Windows 漏洞可能被利用于勒索软件攻击
url: https://www.4hou.com/posts/kj9N
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-20
fetch_date: 2025-10-06T16:55:04.082728
---

# CISA 称 Windows 漏洞可能被利用于勒索软件攻击

CISA 称 Windows 漏洞可能被利用于勒索软件攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CISA 称 Windows 漏洞可能被利用于勒索软件攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-06-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)163274

收藏

导语：截至 2024 年 5 月，Black Basta 勒索软件的附属机构已入侵了 500 多个组织。

美国网络安全和基础设施安全局 (CISA) 将勒索软件攻击中滥用的高严重性 Windows 漏洞作为零日漏洞，添加到其主动利用的安全漏洞目录中。

此安全漏洞编号为 CVE-2024-26169，是由 Windows 错误报告服务中不当的权限管理漏洞引起的，利用此漏洞可让本地攻击者在无需用户交互的低复杂度攻击中获得系统权限。

微软在 2024 年 3 月 12 日的每月补丁星期二更新中解决了该漏洞。

本周发布的一份报告显示，安全研究人员发现有证据表明，Black Basta 勒索软件团伙（Cardinal 网络犯罪集团，也被追踪为 UNC4394 和 Storm-1811）的运营者很可能是利用该漏洞作为零日漏洞进行攻击的幕后黑手。

他们发现，在这些攻击中部署的 CVE-2024-26169 漏洞利用工具的一个变体的编译时间戳为 2 月 27 日，而第二个样本的构建时间甚至更早，为 2023 年 12 月 18 日。

正如安全研究机构在其报告中承认的那样，这些时间很容易被修改，这使得他们的零日漏洞利用结果不确定。然而，攻击者这样做的动机很少甚至没有，因此这种情况不太可能发生。

种种迹象表明，勒索软件组织在微软发布安全更新来修补本地特权提升漏洞之前的 14 到 85 天内就已存在漏洞。

![CVE-2024-26169-exploit.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240617/1718613754311562.png "1718613668854841.png")

BLACK BASTA CVE-2024-26169 漏洞演示

**尽快保护易受攻击的系统**

根据 2021 年 11 月的具有约束力的运营指令 (BOD 22-01)，联邦民事行政部门机构 (FCEB) 必须保护其系统免受 CISA 已知利用漏洞目录中添加的所有漏洞的攻击。

CISA 要求 FCEB 机构在 7 月 4 日前修补 CVE-2024-26169 安全漏洞，并阻止可能针对其网络的勒索软件攻击。

尽管该指令仅适用于联邦机构，但网络安全机构也强烈敦促要优先修复该漏洞，并警告称“此类漏洞是恶意分子的常见攻击媒介，对企业构成重大风险。”

早在 2022 年 4 月，Conti 网络犯罪团伙在发生一系列令人尴尬的数据泄露事件后分裂为多个派系，随后 Black Basta 作为一家勒索软件即服务 (RaaS) 组织出现。

自那时起，该团伙已入侵了许多受害者，包括德国国防承包商莱茵金属、英国技术外包公司 Capita、多伦多公共图书馆、美国牙科协会、政府承包商 ABB、现代欧洲分部、加拿大黄页和美国医疗保健巨头 Ascension等等。

据CISA 和 FBI 透露，截至 2024 年 5 月，Black Basta 勒索软件的附属机构已入侵了 500 多个组织，加密了系统并窃取了至少 12 个美国关键基础设施部门的数据。

根据网络安全公司研究数据，截至 2023 年 11 月，Black Basta 从 90 多名受害者那里收取了至少 1 亿美元的赎金。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisa-warns-of-windows-bug-exploited-in-ransomware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KKmGMECd)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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