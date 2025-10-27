---
title: 新的 Linux glibc漏洞可使网络攻击者获得主要发行版 root 权限
url: https://www.4hou.com/posts/qpNk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-02-24
fetch_date: 2025-10-04T12:05:54.568402
---

# 新的 Linux glibc漏洞可使网络攻击者获得主要发行版 root 权限

新的 Linux glibc漏洞可使网络攻击者获得主要发行版 root 权限 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Linux glibc漏洞可使网络攻击者获得主要发行版 root 权限

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-02-23 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)219839

收藏

导语：该安全漏洞被追踪为CVE-2023-6246，是在 glibc 的 \_\_vsyslog\_internal() 函数中发现的。

非特权攻击者可以通过利用 GNU C 库 (glibc) 中新披露的本地权限提升 (LPE) 漏洞，在默认配置下获得多个主要 Linux 发行版的 root 访问权限。

该安全漏洞被追踪为CVE-2023-6246，是在 glibc 的 \_\_vsyslog\_internal() 函数中发现的，广泛使用的 syslog 和 vsyslog 函数调用该函数将消息写入系统消息记录器。

该错误是由于2022 年 8 月在 glibc 2.37 中意外引入的基于堆的缓冲区溢出漏洞造成，后来在解决跟踪为 CVE-2022-39046 的不太严重的漏洞时向后移植到 glibc 2.36。

Qualys 安全研究人员表示：“缓冲区溢出问题构成了重大威胁，因为它可能允许本地权限升级，使非特权用户能够通过对使用这些日志记录功能的应用程序，进行输入来获得完全的 root 访问权限。”

尽管该漏洞需要特定的条件才能被利用（例如异常长的 argv[0] 或 openlog() ident 参数），但由于受影响的库广泛使用，以致于其影响也是巨大的。

**影响 Debian、Ubuntu 和 Fedora 系统**

在测试时，Qualys 确认 Debian 12 和 13、Ubuntu 23.04 和 23.10 以及 Fedora 37 到 39 都容易受到 CVE-2023-6246 漏洞的攻击，允许任何非特权用户在默认安装时，将权限升级到完全 root 访问权限。

尽管他们的测试仅限于少数发行版，但研究人员补充说“其他发行版也可能是可利用的。”

在分析 glibc 的其他潜在安全问题时，研究人员还发现了另外三个漏洞，其中两个较难利用，位于 \_\_vsyslog\_internal() 函数（CVE-2023-6779 和 CVE-2023-6780）中，第三个漏洞（ glibc 的 qsort() 函数中的内存损坏问题仍在等待 CVEID）。

Qualys 威胁研究部门的产品经理表示：“最近发现的这些漏洞不仅是一个技术问题，而且是一个安全问题。”

**Qualys 发现的其他 Linux root 升级缺陷**

在过去的几年里，Qualys 的研究人员发现了其他几个 Linux 安全漏洞，这些漏洞可以让攻击者完全控制未修补的 Linux 系统，即使在默认配置下也是如此。

他们发现的漏洞包括 glibc 的 ld.so 动态加载器（ Looney Tunables ）中的一个缺陷、Polkit 的 pkexec 组件（称为 PwnKit）中的一个缺陷、内核文件系统层（称为 Sequoia）中的另一个缺陷以及 Sudo Unix 程序（又名Baron Samedit）中的一个缺陷。 。

Looney Tunables 漏洞( CVE-2023-4911 ) 披露几天后，概念验证 (PoC) 漏洞在网上发布，威胁分子在一个月后开始利用该漏洞窃取 Kinsing 恶意软件中的云服务提供商 (CSP) 凭据攻击。

Kinsing 组织以在受感染的云系统（包括 Kubernetes、Docker API、Redis 和 Jenkins 服务器）上部署加密货币挖掘恶意软件而闻名。

CISA 随后命令美国联邦机构确保其 Linux 系统免受 CVE-2023-4911 攻击，并将其添加到积极利用的漏洞目录中，将其标记为“对企业构成重大风险”。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-linux-glibc-flaw-lets-attackers-get-root-on-major-distros/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YIgEzXZG)

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