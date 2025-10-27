---
title: Fortinet 发现零日攻击中使用了新的严重 FortiManager 漏洞
url: https://www.4hou.com/posts/rpgk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-30
fetch_date: 2025-10-06T18:51:23.641119
---

# Fortinet 发现零日攻击中使用了新的严重 FortiManager 漏洞

Fortinet 发现零日攻击中使用了新的严重 FortiManager 漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Fortinet 发现零日攻击中使用了新的严重 FortiManager 漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-10-29 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)83515

收藏

导语：只要攻击者获得了有效证书，将 FortiGate 设备连接到暴露的 FortiManager 服务器并不困难。

Fortinet 近期公开披露了一个严重的 FortiManager API 漏洞（编号为 CVE-2024-47575），该漏洞在零日攻击中被利用，用于窃取包含托管设备配置、IP 地址和凭据的敏感文件。

该公司从 10 月 13 日开始在高级通知电子邮件中私下通知 FortiManager 客户有关该漏洞的信息，并包含在发布安全更新之前缓解该漏洞的步骤。

然而，有关该漏洞的消息已经由 Reddit 上的客户和 Mastodon 上的网络安全研究员 Kevin Beaumont 泄露，他将此漏洞称为“FortiJump”。

Fortinet 设备管理员还表示，该漏洞已被利用一段时间，有客户报告在通知发送给客户几周前就遭到了攻击。

**FortiManager 零日漏洞披露**

目前，Fortinet 公开披露了被主动利用的关键 FortiManager 漏洞，编号为 CVE-2024-47575，严重程度为 9.8。Fortinet 的 FG-IR-24-423 在安全公告中写道：未经身份验证的攻击者通过特制请求可执行任意代码或命令。

“报告显示该漏洞可被广泛利用。”一位熟悉攻击的消息人士告诉记者。该通报缺少一些利用该漏洞的关键信息：威胁者必须首先从任何拥有或受损的 Fortinet 设备（包括 FortiManager VM）中提取有效证书。该漏洞影响以下 FortiManager 版本：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241029/1730167782153539.png "1729738372190427.png")

目前，仅发布了 FortiManager 7.2.8 和 7.4.5 版本，其余版本将在未来几天内发布。 Fortinet 创建了“FortiGate 到 FortiManager 协议”(FGFM)，允许公司轻松部署 FortiGate 防火墙设备，并让它们注册到远程 FortiManager 服务器，以便可以从中央位置进行管理。

这些场景包括 FortiManager 位于公共互联网上，而 FortiGate 设备位于 NAT 后面，FortiGate 设备位于公共互联网上，而 FortiManager 位于 NAT 后面，或者 FortiManager 和 FortiGate 设备都具有可路由的 IP 地址。

正如网络安全研究员 Kevin Beaumont 指出的那样，只要攻击者获得了有效证书，将 FortiGate 设备连接到暴露的 FortiManager 服务器并不困难。

该证书用于在 FortiGate 和 FortiManager 服务器之间建立 SSL 隧道，以对两个设备进行身份验证。然而，这不是漏洞所在。相反，通过 FortiManager FGFM API 执行命令需要额外的授权级别，可以使用 CVE-2024-47575 漏洞绕过该 API。

API 中的身份验证绕过已在最新版本的 FortiManager 中修复。该 API 允许攻击者执行命令、检索信息并完全控制托管设备和 FortiManager，以进一步访问企业网络。

由于 MSP（托管服务提供商）经常使用 FortiManager，因此用户可以使用它进入下游内部网络。

由于 FGFM 的设计方式（NAT 穿越情况），这也意味着如果获得对托管 FortiGate 防火墙的访问权限，就可以向上遍历到管理 FortiManager 设备，然后返回到其他防火墙和网络。如果此时无法安装最新的固件更新，Fortinet 提供了不同的方法来缓解这种攻击：

**·**使用 set fgfm-deny-unknown enable 命令阻止序列号未知的设备注册到 FortiManager。

**·**创建自定义证书，以在创建 SSL 隧道并使用 FortiManager 验证 FortiGate 设备时使用。

然而，Fortinet 表示，如果威胁者能够获得此证书，那么它仍然可以用于连接 FortiGate 设备并利用该漏洞。

**·**为允许连接的 FortiGate 设备创建 IP 地址的允许列表。

有关如何执行这些缓解措施和恢复受感染服务器的说明，可参阅 Fortinet 的公告。

**被利用窃取数据**

Fortinet 表示，观察到的攻击被用来从 FortiManager 服务器窃取各种文件，这些文件“包含受管设备的 IP、凭据和配置”。

这些被盗信息可用于了解和定位 FortiGate 设备，以获得对企业网络或 MSP 下游客户端的初始访问权限。

该公司还确认，没有证据表明受感染的 FortiManager 服务上安装了恶意软件，也没有证据表明托管 FortiGate 设备的配置发生了变化。 Fortinet 在安全公告中表示：“现阶段尚未收到有关在这些受感染的 FortiManager 系统上安装任何低级恶意软件或后门的报告。”

Fortinet 并未将这些攻击归因于任何特定的威胁者，也没有分享有关因正在进行的调查而受到影响的客户数量和类型的任何信息。然而，Fortinet 共享了以下 IOC，以帮助安全专业人员和网络管理员检测其 FortiManager 服务器是否因该漏洞而遭到破坏。

观察到的攻击表明，威胁参与者以“localhost”名称连接了攻击者控制的 FortiGate 设备，该名称将出现在 Fortimanager 的“未注册设备”部分中。日志条目将显示威胁参与者发出 API 命令来添加这些未注册的“localhost”设备。

Fortinet 共享的另一个日志条目用于编辑设备设置：

类型=事件，子类型= dvm，pri =通知，desc =“设备，管理器，dvm，日志，at，通知，级别”，user =“系统”，userfrom =“”，msg =“” adom =“根” session\_id=0 opera,on=“修改设备” Performed\_on=“localhost”changes=“已编辑的设备设置 (SN FMG-VMTM23017412)”

Fortinet 表示，恶意 FortiGate 设备使用序列号 FMG-VMTM23017412，这似乎是 FortiGate-VM 虚拟机使用的格式。其他 IOC 包括创建 /tmp/.tm 和 /var/tmp/.tm 文件。在攻击中观察到以下 IP 地址，全部位于云托管公司 Vultr：

**·**45.32.41.202

**·**104.238.141.143 （最近看到托管 SuperShell C2 基础设施）

**·**158.247.199.37

**·**45.32.63.2

Fortinet 警告称，并非所有 IOC 都可能出现在被利用的设备上。 Shodan 搜索显示有 59,534 个 FortiManager 设备的 FGFM 端口（TCP 端口 531）在线暴露，其中大多数位于美国。

**客户对漏洞披露方式感到失望**

Fortinet 分享了有关 CVE-2024-47575 漏洞以及如何向客户披露该漏洞的声明，表示“识别此漏洞 (CVE-2024-47575) 后，Fortinet 立即向客户传达了关键信息和资源。”

然而，Fortinet 客户对漏洞的披露方式表示失望，一些 FortiManager 客户没有收到提前通知，不得不依靠泄露的信息来查找零日漏洞。

所有 FortiManager 客户的“主”帐户都应该收到此通知。如果没有，他们应该联系 Fortinet 或其经销商，以确认他们拥有正确的联系信息。其他人感到沮丧的是，私人咨询并未将 FortiManager Cloud 列为受零日影响的产品，但当他们致电 Fortinet TAC 时，却被告知它受到了影响。这个漏洞并不是 Fortinet 第一次决定悄悄修补关键漏洞或私下向客户披露。

2022 年 12 月，Fortinet 悄悄修补了一个被主动利用的 FortiOS SSL-VPN 漏洞（编号为 CVE-2022-42475），但没有公开声明该漏洞已用于攻击。

与这个 FortiManager 漏洞一样，Fortinet 于 12 月 7 日向客户发布了私人 TLP:Amber 公告，提醒客户注意该漏洞。

2023 年 6 月，Fortinet 于 6 月 8 日再次悄悄修补了一个关键的 FortiGate SSL-VPN 远程代码执行漏洞，编号为 CVE-2023-27997。

四天后，即 6 月 11 日，该公司披露该漏洞已被用于零日攻击针对政府、制造业和关键基础设施的攻击。为此有很多人批评 Fortinet 缺乏透明度。

文章翻译自：https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-critical-fortimanager-flaw-used-in-zero-day-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fr1ozaxK)

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
[RSS](https...