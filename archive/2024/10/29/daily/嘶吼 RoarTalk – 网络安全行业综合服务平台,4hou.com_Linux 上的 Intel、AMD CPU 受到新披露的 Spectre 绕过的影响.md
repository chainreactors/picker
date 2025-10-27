---
title: Linux 上的 Intel、AMD CPU 受到新披露的 Spectre 绕过的影响
url: https://www.4hou.com/posts/1MYo
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-29
fetch_date: 2025-10-06T18:47:45.025020
---

# Linux 上的 Intel、AMD CPU 受到新披露的 Spectre 绕过的影响

Linux 上的 Intel、AMD CPU 受到新披露的 Spectre 绕过的影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Linux 上的 Intel、AMD CPU 受到新披露的 Spectre 绕过的影响

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-10-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)80054

收藏

导语：受影响的旧架构以及 AMD 很久以前就了解了该错误的事实可能解释了该公司决定不发布纠正微代码的原因。

据了解，最新一代的 Intel 处理器（包括 Xeon 芯片）和 AMD 在 Linux 上的旧微架构很容易受到绕过现有“Spectre”缓解措施的新推测执行攻击。

这些漏洞影响英特尔第 12、第 13 和第 14 代芯片以及面向服务器的第 5 和第 6 代 Xeon 处理器，以及 AMD 的 Zen 1、Zen 1+ 和 Zen 2 处理器。

这些攻击破坏了 x86 处理器上的间接分支预测器屏障 (IBPB)，这是针对推测执行攻击的核心防御机制。

推测执行是现代 CPU 上的一项性能优化功能，它在知道未来任务是否需要指令之前执行指令，从而在预测正确时加快进程。

基于错误预测执行的指令称为瞬态指令并被压缩。这种机制一直是侧通道风险（例如 Spectre）的来源，因为推测过程调用可以从 CPU 缓存检索的敏感数据。

**新的类似幽灵的攻击**

安全研究人员表示，尽管为遏制类似 Spectre 的攻击进行了多年的缓解努力，但仍有许多变体绕过了现有的防御措施。

他们的贡献是跨进程攻击（针对 Intel）和 PB-inception 攻击（针对 AMD），即使在应用 IBPB 后也允许劫持投机返回目标，从而绕过当前的保护并泄露敏感信息。

在第一种情况下，攻击利用了英特尔微代码中的一个漏洞，即 IBPB 不会在上下文切换后完全使返回预测无效。攻击者操纵返回指令的推测执行，允许过时的预测从 suid 进程中泄漏敏感信息，例如 root 密码的哈希值。

在 AMD 处理器上，Linux 内核中的 IBPB-on-entry 应用不当，导致返回预测器即使在 IBPB 之后仍保留过时的预测。攻击者在 IBPB 触发之前错误训练返回预测器，劫持它以在屏障之后泄漏特权内核内存。

![8.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241021/1729493251399671.png "1729493188121104.png")

IBPB 后英特尔和 AMD 仍然脆弱的回报预测

**应对措施和缓解措施**

研究人员于 2024 年 6 月向英特尔和 AMD 通报了这些问题。英特尔回应称，他们已经在内部发现了该问题，并为其分配了 CVE-2023-38575 标识符。

该公司于 3 月份发布了可通过固件更新进行的微代码修复，但研究人员指出，该代码尚未到达所有操作系统，Ubuntu 就是其中之一。

AMD 也确认了该漏洞，并表示该漏洞已被记录并追踪为 CVE-2022-23824。值得注意的是，AMD 的公告将 Zen 3 产品列为受影响的产品。但是，AMD 将该问题归类为软件错误，而不是硬件缺陷。

受影响的旧架构以及 AMD 很久以前就了解了该错误的事实可能解释了该公司决定不发布纠正微代码的原因。尽管这两家 CPU 供应商知道 Spectre 绕过，但这些公司在公告中将其标记为具有潜在影响。

通过他们的工作，安全研究人员能够证明这种攻击甚至在 Linux 6.5 上也能发挥作用，Linux 6.5 附带了 IBPB-on-entry 防御，被认为是针对 Spctre 利用的最强防御。目前，有关高校正在与 Linux 内核维护人员合作开发适用于 AMD 处理器的补丁。

文章翻译自：https://www.bleepingcomputer.com/news/security/intel-amd-cpus-on-linux-impacted-by-newly-disclosed-spectre-bypass/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?47Qyy8Hv)

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