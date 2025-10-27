---
title: KeyTrap 攻击：一个 DNS 数据包可中断互联网访问
url: https://www.4hou.com/posts/PK36
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-03-12
fetch_date: 2025-10-04T12:12:01.997169
---

# KeyTrap 攻击：一个 DNS 数据包可中断互联网访问

KeyTrap 攻击：一个 DNS 数据包可中断互联网访问 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# KeyTrap 攻击：一个 DNS 数据包可中断互联网访问

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-03-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)247385

收藏

导语：目前，Google 和 Cloudflare 的 DNS 服务中已经存在修复程序。

域名系统安全扩展 (DNSSEC) 功能中名为 KeyTrap 的严重漏洞，可能会长时间拒绝应用程序的互联网访问。

KeyTrap 的编号为 CVE-2023-50387，影响着所有流行的域名系统 (DNS) 实施或服务。它允许远程攻击者通过发送单个 DNS 数据包，在易受攻击的解析器中长期持续的拒绝服务 (DoS) 。

DNS 允许我们通过输入域名，而不是需要连接服务器的 IP 地址来访问在线位置。

DNSSEC 是 DNS 的一项功能，可为 DNS 记录带来加密签名，从而为响应提供身份验证；此验证可确保 DNS 数据来源。

**攻击请求造成了重大损害**

KeyTrap 已出现在 DNSSEC 标准中二十多年，由国家应用网络安全研究中心 ATHENE 的研究人员以及法兰克福歌德大学、Fraunhofer SIT 和达姆施塔特工业大学的专家发现。

研究人员解释说，该问题源于 DNSSEC 要求发送受支持密码的所有相关加密密钥以及进行验证的相应签名。

即使某些 DNSSEC 密钥配置错误、不正确或属于不受支持的密码，该过程也是相同的。

通过利用此漏洞，研究人员开发了一种新型的基于 DNSSEC 的算法复杂性攻击，该攻击可以使 DNS 解析器中的 CPU 指令数增加 200 万倍，从而延迟其响应。

这种 DoS 状态的持续时间取决于解析器的实现，但研究人员表示，单个攻击请求可以使响应时间从 56 秒到长达 16 小时不等。

![KeyTrapDoS.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240219/1708336822802852.jpg "1708336822802852.jpg")

一次请求的 KeyTrap 攻击中 DNS 解析器延迟

利用这种攻击会对使用互联网的应用程序造成严重后果，包括网络浏览、电子邮件和即时消息等技术。

研究人员表示：“利用 KeyTrap，攻击者可以完全禁用全球互联网的大部分内容。”

自 2023 年 11 月初以来，研究人员已经展示了他们的 KeyTrap 攻击，如何影响 DNS 服务提供商（例如 Google 和 Cloudflare），并与他们合作开发缓解方法。

![vuln-impl.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240219/1708336832115532.jpg "1708336832115532.jpg")

DNS 实施容易受到 KeyTrap 的攻击

ATHENE 表示，KeyTrap 自 1999 年以来就出现在广泛使用的标准中，近 25 年来一直没有引起人们的注意，主要是因为 DNSSEC 验证要求的复杂性。

尽管受影响的供应商已经推出修复程序或正在减轻 KeyTrap 风险，但从根本上解决该问题可能需要重新评估 DNSSEC 设计理念。

为了应对 KeyTrap 威胁，Akamai在 2023 年 12 月至 2024 年 2 月期间开发并部署了针对 DNSi 递归解析器的缓解措施，包括 CacheServe 和 AnswerX，以及云和托管解决方案。

这一安全漏洞允许攻击者对互联网的功能进行破坏，使全球三分之一的 DNS 服务器遭受高效的拒绝服务 (DoS) 攻击，并影响了超过 10 亿用户。

Akamai 指出，根据 APNIC 数据，大约 35% 的美国用户和全球 30% 的互联网用户依赖使用 DNSSEC 验证的 DNS 解析器，极容易受到 KeyTrap 的攻击。

目前，Google 和 Cloudflare 的 DNS 服务中已经存在修复程序。

文章翻译自：https://www.bleepingcomputer.com/news/security/keytrap-attack-internet-access-disrupted-with-one-dns-packet/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?g3k9ZTWz)

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