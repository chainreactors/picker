---
title: Dev 无视 CVE 严重性，将其 GitHub 存储库设为只读
url: https://www.4hou.com/posts/W16v
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-23
fetch_date: 2025-10-06T17:40:59.203009
---

# Dev 无视 CVE 严重性，将其 GitHub 存储库设为只读

Dev 无视 CVE 严重性，将其 GitHub 存储库设为只读 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Dev 无视 CVE 严重性，将其 GitHub 存储库设为只读

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-22 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106401

收藏

导语：近年来，开源开发者收到的有争议的 CVE 报告数量不断增加，有些甚至是未经确认的伪造 CVE 报告。

流行的开源项目“ip”的 GitHub 存储库最近被其开发人员存档或设为“只读”，由于 Fedor Indutny 的项目收到了 CVE 报告，因此网上有人开始向他报告这个漏洞。

不幸的是，Indutny 的案例并非孤例。近年来，开源开发者收到的有争议的 CVE 报告数量不断增加，有些甚至是未经确认的伪造 CVE 报告。

这可能会导致这些项目的用户产生不必要的恐慌，并且安全扫描程序会生成警报，而所有这些都会成为开发人员的头痛之源。

**“node-ip” GitHub 存储库已存档**

本月初，“node-ip”项目的作者 Fedor Indutny 将该项目的 GitHub 存储库存档，实际上使其成为只读的，并限制了人们打开新问题（讨论）、拉取请求或向项目提交评论的能力。

![github-archived.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720431368163063.png "1720430882833641.png")

node-ip GitHub repo 已存档并设为“只读”

“node-ip”项目作为“ip”包存在于 npmjs.com 注册表中，每周下载量达 1700 万次，是 JavaScript 开发人员使用的最受欢迎的 IP 地址解析实用程序之一。

6 月底，Indutny 在社交媒体上表达了存档“node-ip”背后的理由与 CVE-2023-42282 有关，这是该项目今年早些时候披露的一个漏洞。

使用其他开放项目（例如应用程序中的 npm 包和依赖项）的 Node.js 开发人员可以运行“npm audit”命令来检查其应用程序所使用的这些项目中是否有针对它们的漏洞报告。

![dev-mast-thread.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720431369172518.jpg "1720430981788136.jpg")

Bothered dev 的开发人员在社交媒体上表达了他的担忧

该 CVE 与实用程序无法正确识别以非标准格式（例如十六进制）提供给它的私有 IP 地址有关。这会导致“node-ip”实用程序将私有 IP 地址（十六进制格式）如“0x7F.1...”（代表 127.1...）视为公共 IP 地址。

如果应用程序仅依赖 node-ip 来检查提供的 IP 地址是否公开，则非标准输入可能会导致受影响的实用程序版本返回不一致的结果。

**“可疑”的安全影响**

公开消息称，CVE-2023-42282 最初的评分为 9.8，即“严重”。尽管 Indutny 在其项目的后续版本中修复了该问题，但他否认该漏洞构成了实际威胁，以及严重程度较高。

该开发人员早些时候写道：“我认为该漏洞的安全影响相当可疑”，并要求 GitHub 撤销 CVE。

正如 GitHub 安全团队成员所解释的那样，对 CVE 提出异议不是一件容易的事，它要求项目维护者追踪最初发布 CVE 的 CVE 编号机构 (CNA)。

CNA 通常包括 NIST 的 NVD 和 MITRE。过去几年，科技公司和安全供应商也加入了这一名单，并能够随意发布 CVE。这些 CVE 以及漏洞描述和报告的严重性评级随后被其他安全数据库（如 GitHub 公告）联合发布。

在 Indutny 在社交媒体上发布帖子后，GitHub 降低了其数据库中 CVE 的严重性，并建议开发人员开启私人漏洞报告，以便更好地管理传入的报告并减少噪音。

在撰写本文时，该漏洞在 NVD 上的严重程度仍然为“严重”。

**日益严重的滋扰**

CVE 系统最初旨在帮助安全研究人员以合乎道德的方式报告项目中的漏洞，并在负责任的披露后对其进行分类，但最近吸引了一部分社区成员提交未经核实的报告。

虽然许多 CVE 都是由负责任的研究人员善意提交的，并且代表了可信的安全漏洞，但最近出现了一种新模式，新手安全爱好者和漏洞赏金猎人表面上“收集”CVE 来丰富他们的简历，而不是报告构成现实世界、实际利用影响的安全漏洞。

因此，开发人员和项目维护人员进行了反击。

2023 年 9 月，著名软件项目“curl”的创建者 Daniel Stenberg 斥责了“虚假 curl 问题 CVE-2020-19909”，这是针对该项目报告的一个拒绝服务漏洞。

根据 NVD 的历史数据，这个现在备受争议的 CVE 的严重程度最初被评为 9.8 级或严重程度，但在随后的讨论中，该漏洞对安全造成的实际影响引发质疑，随后其评级被降至“低”3.3 级。

“这不是一个独特的例子，也不是第一次发生。这种情况已经持续多年了，”斯滕伯格在批评 CVE 条目时写道。

另一个 npm 项目 micromatch 每周下载量达 6400 万次，但报告称存在“高”严重程度的 ReDoS 漏洞，社区成员正在追查其创建者，询问这些问题。

针对未经验证的漏洞报告发布 CVE 的行为类似于针对项目、其创建者及其更广泛的消费者群体发起拒绝服务 (DoS)。

开发人员安全解决方案（例如 npm audit）旨在防止易受攻击的组件进入用户的应用程序，如果检测到任何已知漏洞，可能会触发警报，并且根据用户的设置，可能会破坏用户构建。

“几个月前 有人报告了针对该项目的一个关键 CVE，并认为其破坏了全球的构建，”一位评论员在 2023 年针对虚假的 curl CVE 做出反应时写道。

正如其他开发人员所说，这个问题并不是项目的安全问题，而是 Java 递归数据结构的固有性质。

**平衡点在哪里**

此类事件频发引发了人们的疑问：如何才能取得平衡？不断报告理论上的漏洞可能会让开源开发者（其中许多是志愿者）因筛选而精疲力竭。

另一方面，如果安全从业人员（包括新手）对他们认为的安全漏洞置之不理，不免给项目维护人员带来不便，这是否合乎道德？

第三个问题出现在没有活跃维护者的项目上。多年无人触及的废弃软件项目包含漏洞，即使被披露，也永远不会被修复，而且没有办法联系其原始维护者。

在这种情况下，包括 CNA 和漏洞赏金平台在内的中介机构就陷入了困境。

在收到研究人员的漏洞报告后，这些组织可能并不总是能够独立地充分审查每一份此类报告。在没有得到（现已缺席的）项目维护者的意见的情况下，他们可能会被迫在“负责任的披露”窗口期过后分配和发布 CVE。

目前，这些问题均没有答案。

在安全研究人员、开发人员和供应商社区齐心协力找到有效的解决方案之前，开发人员必然会对虚假报告感到沮丧，而 CVE 系统也将充斥着夸大的“漏洞”，这些漏洞在纸面上看起来可信，但实际上毫无意义。

文章翻译自：https://www.bleepingcomputer.com/news/security/dev-rejects-cve-severity-makes-his-github-repo-read-only/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vlFRa0zu)

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