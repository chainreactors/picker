---
title: MOVEit Transfer 中的严重漏洞可使黑客获得文件访问权限
url: https://www.4hou.com/posts/DxNq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-11
fetch_date: 2025-10-06T17:38:50.571975
---

# MOVEit Transfer 中的严重漏洞可使黑客获得文件访问权限

MOVEit Transfer 中的严重漏洞可使黑客获得文件访问权限 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# MOVEit Transfer 中的严重漏洞可使黑客获得文件访问权限

山卡拉
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-10 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107462

收藏

导语：Progress 已经认识到 CVE-2024-5806 的严重性，并与客户展开密切合作，以确保迅速解决这一问题。

![Vulnerability in MOVEit Transfer.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719386658373499.jpg "1719386435168428.jpg")

MOVEit Transfer 是一个广泛使用的托管文件传输软件，安全研究人员最近发现了一个严重的安全漏洞，标识为CVE-2024-5806。该漏洞存在于身份验证过程中未正确验证用户输入，导致攻击者能够发送特制请求并绕过身份验证，进而获取管理访问权限。

受影响的软件版本包括 MOVEit Transfer 2023.0.0 至 2023.0.10、2023.1.0 至 2023.1.5 和 2024.0.0 至 2024.0.1。为了修复这一漏洞，Progress 强烈建议所有使用受影响版本的客户立即升级到以下修补版本：

**·**MOVEit Transfer 2023.0.11

**·**MOVEit Transfer 2023.1.6

**·**MOVEit Transfer 2024.0.2

Rapid7 的研究人员已确认可以利用这一漏洞绕过未修补版本的身份验证，包括 MOVEit Transfer 和 MOVEit Gateway。

**影响与缓解**

此漏洞可能导致攻击者绕过身份验证机制并未经授权地访问系统，进而可能造成数据泄露和敏感信息泄露等恶意活动。

为了减少风险，建议客户使用完整安装程序升级到最新的 MOVEit Transfer 修补版本。请注意，升级过程可能会导致系统中断。

不过，此漏洞不会影响 MOVEit Cloud 客户，因为补丁已经在云基础设施中部署。此外，MOVEit Cloud 通过严格的访问控制来防范第三方漏洞。

Progress 建议人们可以采取以下步骤以进一步降低风险：

1. 验证 MOVEit Transfer 服务器的公共入站 RDP 访问是否被阻止。

2. 将 MOVEit Transfer 服务器的出站访问限制到仅已知的可信端点。

一旦发布，Progress 将向 MOVEit Transfer 客户提供第三方供应商的修复程序。

Progress 已经认识到 CVE-2024-5806 的严重性，并与客户展开密切合作，以确保迅速解决这一问题。此外，他们还提供了详细的应用程序补丁和保护系统的指导。

本文翻译自：https://gbhackers.com/authentication-bypass-vulnerability-in-moveit-transfer/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?X7SeMXbV)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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