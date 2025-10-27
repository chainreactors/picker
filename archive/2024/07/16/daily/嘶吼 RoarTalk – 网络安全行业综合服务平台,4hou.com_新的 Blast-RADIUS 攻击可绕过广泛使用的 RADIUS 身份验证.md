---
title: 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证
url: https://www.4hou.com/posts/gyJ3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-16
fetch_date: 2025-10-06T17:42:46.493063
---

# 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证

新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)133373

收藏

导语：由于此攻击不会危及最终用户凭证，因此用户最终无法采取任何措施来防范此攻击。

Blast-RADIUS 是广泛使用的 RADIUS/UDP 协议中的一种身份验证绕过方法，它使威胁分子能够通过中间人 MD5 碰撞攻击侵入网络和设备。

企业和电信网络上的许多联网设备（包括交换机、路由器和其他路由基础设施）都使用身份验证和授权 RADIUS（远程身份验证拨入用户服务）协议，有时单个网络上有数万台设备。

该协议具有广泛的应用范围，可用于 DSL 和 FTTH（光纤到户）、802.1X 和 Wi-Fi、2G 和 3G 蜂窝漫游、5G DNN（数据网络名称）、私有 APN 和 VPN 以及关键基础设施网络中的身份验证。

Blast-RADIUS 利用了新的协议漏洞 (CVE-2024-3596) 和 MD5 碰撞攻击，允许有权访问 RADIUS 流量的攻击者操纵服务器响应并添加任意协议属性，从而使他们无需暴力破解或窃取凭据即可获得 RADIUS 设备的管理员权限。

Blast-RADIUS 攻击允许 RADIUS 客户端和服务器之间的中间人攻击者伪造有效的协议接受消息来响应失败的身份验证请求。而这种伪造可以让攻击者访问网络设备和服务，而无需攻击者猜测或暴力破解密码或共享机密。攻击者无法获知用户凭证。

攻击者可以将权限从部分网络访问提升到能够登录任何使用 RADIUS 进行身份验证的设备，或者为自己分配任意网络权限。

在设备上执行身份验证时，RADIUS 协议使用 MD5 哈希请求和响应。研究人员的概念验证漏洞（尚未共享）计算出伪造有效“Access-Accept”响应所需的 MD5 选择前缀哈希碰撞，以表示身份验证请求成功。然后使用中间人攻击将伪造的 MD5 哈希注入网络通信，允许攻击者登录。

该漏洞需要 3 到 6 分钟才能伪造此 MD5 哈希值，比 RADIUS 实际中通常使用的 30 到 60 秒的超时时间要长。

然而，攻击中使用的碰撞算法的每个步骤都可以有效地并行化，并且适合硬件优化，这将使资源充足的攻击者能够使用 GPU、FPGA 或其他更现代、更快的硬件实施攻击，以实现更快的运行时间，可能快几十倍或几百倍。

![Blast-RADIUS-attack.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240710/1720594165129824.png "1720593038163666.png")

攻击流

安全研究小组表示：“虽然 MD5 哈希碰撞在 2004 年首次被证明，但人们认为不可能在 RADIUS 协议环境中利用这一点。”“我们的攻击确定了 RADIUS 使用 MD5 的方式中的协议漏洞，该漏洞允许攻击者注入恶意协议属性，从而在服务器生成的响应认证器和攻击者想要的伪造响应数据包之间产生哈希碰撞。

此外，由于攻击是在线的，攻击者需要能够在几分钟或几秒钟内计算出所谓的选择前缀 MD5 碰撞攻击。之前报道的最佳选择前缀碰撞攻击时间需要数小时，并且产生的碰撞与 RADIUS 协议不兼容。

由于此攻击不会危及最终用户凭证，因此用户最终无法采取任何措施来防范此攻击。但是，安全研究人员建议制造和管理 RADIUS 设备的供应商和系统管理员遵循这些最佳实践和指导。

为了防御这种攻击，网络运营商可以升级到 TLS 上的 RADIUS（RADSEC），切换到“多跳” RADIUS 部署，并使用受限访问管理 VLAN 或 TLS/IPsec 隧道将 RADIUS 流量与互联网访问隔离。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-blast-radius-attack-bypasses-widely-used-radius-authentication/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?cDQz6x3E)

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