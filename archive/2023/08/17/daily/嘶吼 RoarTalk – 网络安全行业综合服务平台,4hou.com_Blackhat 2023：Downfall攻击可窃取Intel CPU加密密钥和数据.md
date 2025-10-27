---
title: Blackhat 2023：Downfall攻击可窃取Intel CPU加密密钥和数据
url: https://www.4hou.com/posts/GXXL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-17
fetch_date: 2025-10-04T11:59:08.619175
---

# Blackhat 2023：Downfall攻击可窃取Intel CPU加密密钥和数据

Blackhat 2023：Downfall攻击可窃取Intel CPU加密密钥和数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Blackhat 2023：Downfall攻击可窃取Intel CPU加密密钥和数据

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2023-08-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)160232

收藏

导语：​Downfall推测执行攻击可窃取Intel CPU加密密钥和数据。

Downfall推测执行攻击可窃取Intel CPU加密密钥和数据。

谷歌安全研究人员Daniel Moghimi发现了Intel CPU中的一个推测执行漏洞，漏洞CVE编号CVE-2022-40982（Downfall）。漏洞影响所有基于Intel Skylake和Ice Lake微架构的处理器。攻击者利用该漏洞可以从Intel CPU中窃取密码、加密密钥、邮件、短信、银行信息等用户个人数据。

**Downfall攻击**

攻击者利用该漏洞可以提取Software Guard eXtensions (SGX)保护的敏感信息。SGX是Intel基于硬件的内存加密，将系统中的内存代码和软件数据分割开来。目前，SGX只支持服务器中央处理器，为软件提供可信的隔离环境。

Gather是Intel处理器中的内存优化指令，用于加速内存中访问数据。Gather指令使用相邻CPU线程之间共享的临时缓存，可以瞬态转发数据给之后的依赖指令。转发的数据属于不同的进程，gather执行运行在相同内核中。

Moghimi称Downfall攻击利用了gather指令在推测执行过程中泄露内部向量寄存器文件的内容。Moghimi设计了两种Downfall攻击技术：Gather Data Sampling (GDS，gather数据取样)和Gather Value Injection (GVI，gather值注入)。GVI融合了GDS和加载值注入（Load Value Injection）技术。

使用GDS技术，Moghimi成功在隔离的虚拟机中窃取了AES 128位和156位加密密钥。在实验中，对于100个不同的密钥，针对AES-128的攻击成功率为100%，对于AES-256的攻击成功率为86%。除了加密密钥，Moghimi还提供了GDS攻击的变种，可以窃取任意数据。

**漏洞影响与补丁**

Downfall攻击需要攻击者与受害者在同一物理处理器上。本地程序也可能利用来该漏洞来窃取敏感信息，如恶意软件。

Intel 在2022年8月了解到Downfall/GDS漏洞。目前，微软发布了微代码更新来缓解该问题。但该漏洞仍然在1年内时间未公开，以给与OEM厂商和通信服务提供商（CSP）更多的时间来测试和验证解决方案。

Intel称Downfall攻击影响以下Intel 处理器：

Skylake family (Skylake, Cascade Lake, Cooper Lake, Amber Lake, Kaby Lake, Coffee Lake, Whiskey Lake, Comet Lake)

Tiger Lake family

Ice Lake family (Ice Lake, Rocket Lake)

Downfall攻击并不影响Alder Lake, Raptor Lake, and Sapphire Rapids系列CPU。

研究人员公开了Downfall的PoC代码，参见：https://github.com/flowyroll/downfall/blob/main/index.html

相关研究成果已被Usenix security 2023录用，论文下载地址https://www.usenix.org/system/files/usenixsecurity23-moghimi.pdf

成果同时将在Black Hat USA 2023展示，更多参见：https://www.blackhat.com/us-23/briefings/schedule/#single-instruction-multiple-data-leaks-in-cutting-edge-cpus-aka-downfall-31490

本文翻译自：https://www.bleepingcomputer.com/news/security/new-downfall-attacks-on-intel-cpus-steal-encryption-keys-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GQLNkPek)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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