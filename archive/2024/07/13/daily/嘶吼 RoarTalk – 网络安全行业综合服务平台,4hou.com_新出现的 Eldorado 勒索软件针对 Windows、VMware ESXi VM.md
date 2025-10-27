---
title: 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM
url: https://www.4hou.com/posts/OGYL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-13
fetch_date: 2025-10-06T17:38:41.588340
---

# 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM

新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新出现的 Eldorado 勒索软件针对 Windows、VMware ESXi VM

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114725

收藏

导语：研究人员建议采取以下防御措施，这将在一定程度上有助于用户防范所有勒索软件攻击。

今年最新出现了一种名为 Eldorado 的新型勒索软件即服务 (RaaS)，它带有适用于 VMware ESXi 和 Windows 的锁版变种。该团伙目前已危害 16 名受害者，其中大部分在美国，涉及房地产、教育、医疗保健和制造业。

网络安全公司的研究人员监控了 Eldorado 的活动，并注意到其运营商在 RAMP 论坛上推广恶意服务，并寻求熟练的附属机构加入该计划。

Eldorado 还运营着一个列出受害者名单的数据泄露网站，但在撰写本文时该网站已处于瘫痪状态。

![targets.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720423962561064.png "1720421720529414.png")

Eldorado 勒索软件目标

**加密 Windows 和 Linux**

Eldorado 是一款基于 Go 的勒索软件，可通过两个不同的变体加密 Windows 和 Linux 平台，且这两个变体的操作非常相似。

研究人员从开发人员那里获得了一个加密器，该加密器附带一份用户手册，其中说明有适用于 VMware ESXi 虚拟机管理程序和 Windows 的 32/64 位变体。

Group-IB 表示，Eldorado 是一个独特的开发项目。该恶意软件使用 ChaCha20 算法进行加密，并为每个锁定的文件生成唯一的 32 字节密钥和 12 字节随机数。然后使用 RSA 和最佳非对称加密填充 (OAEP) 方案对密钥和随机数进行加密。

加密阶段结束后，文件将被附加“.00000001”扩展名，名为“HOW\_RETURN\_YOUR\_DATA.TXT”的勒索信将被放置在 Documents 和 Desktop 文件夹中。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720423963789976.png "1720421807199184.png")

Eldorado 的赎金条

Eldorado 还利用 SMB 通信协议加密网络共享，以最大限度地发挥其影响，并删除受感染 Windows 计算机上的卷影副本，以防止恢复。

勒索软件会跳过 DLL、LNK、SYS 和 EXE 文件，以及与系统启动和基本功能相关的文件和目录，以防止导致系统无法启动/无法使用。最后，它默认设置为自我删除，以逃避响应团队的检测和分析。

据渗透到该行动中的安全研究人员称，联盟成员可以定制他们的攻击。例如，在 Windows 上，他们可以指定要加密的目录、跳过本地文件、针对特定子网上的网络共享，并防止恶意软件自我删除。

但是，在 Linux 上，自定义参数止步于设置要加密的目录。

**防御建议**

安全研究人员强调，Eldorado 勒索软件威胁是一个新的、独立的行动，并不是以另一个组织的名义重新出现的。而尽管 Eldorado 相对较新，且并非知名勒索软件组织的改头换面，但它已在短时间内迅速证明了其能够对受害者的数据、声誉和业务连续性造成重大损害的能力。

研究人员建议采取以下防御措施，这将在一定程度上有助于用户防范所有勒索软件攻击：

**·**实施多因素身份验证 (MFA) 和基于凭证的访问解决方案。

**·**使用端点检测和响应 (EDR) 快速识别和响应勒索软件指标。

**·**定期备份数据以最大限度地减少损害和数据丢失。

**·**利用基于人工智能的分析和高级恶意软件引爆进行实时入侵检测和响应。

**·**确定优先级并定期应用安全补丁来修复漏洞。

**·**培训员工能够识别网络安全威胁。

**·**进行年度技术审计或安全评估并保持数字安全。

**·**不要支付赎金，因为它很少能确保数据恢复，而且可能导致更多攻击。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-eldorado-ransomware-targets-windows-vmware-esxi-vms/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?F4hsFrVS)

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