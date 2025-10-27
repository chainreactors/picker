---
title: 新型Secure Boot漏洞允许攻击者安装引导工具包恶意软件
url: https://www.4hou.com/posts/33mx
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-17
fetch_date: 2025-10-06T22:54:03.713690
---

# 新型Secure Boot漏洞允许攻击者安装引导工具包恶意软件

新型Secure Boot漏洞允许攻击者安装引导工具包恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Secure Boot漏洞允许攻击者安装引导工具包恶意软件

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-06-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)49117

收藏

导语：进一步的调查发现，这个易受攻击的模块至少从2022年底就开始在野外传播，后来在2024年被上传到VirusTotal。

安全研究人员披露了一种新的Secure Boot绕过技术，编号为CVE-2025-3052，可用于关闭pc和服务器的安全性，并安装引导工具包恶意软件。

这个漏洞影响了几乎所有的系统，这些系统信任 Microsoft 的 "UEFI CA 2011" 证书，基本上所有支持 Secure Boot 的硬件都受到影响。

Binarly研究人员Alex Matrosov在发现一个带有微软UEFI签名证书的bios闪烁实用程序后发现了CVE-2025-3052漏洞。

该实用程序最初是为坚固耐用的平板电脑设计的，但由于它与微软的UEFI证书签署，它可以在任何启用安全启动的系统上运行。

进一步的调查发现，这个易受攻击的模块至少从2022年底就开始在野外传播，后来在2024年被上传到VirusTotal， Binarly在那里发现了它。

Binarly于2025年2月26日向CERT/CC披露了该漏洞，现在作为微软2025年6月补丁星期二的一部分，CVE-2025-3052得到了缓解。

然而，在此过程中，微软确定该漏洞影响了其他13个模块，这些模块被添加到撤销数据库中。Binarly解释说：“在分类过程中，微软确定问题并不像最初认为的那样只是一个模块，实际上是14个不同的模块。”因此，在2025年6月10日补丁星期二期间发布的更新dbx包含14个新哈希值。

**Secure Boot绕过技术**

这个漏洞是由一个使用微软UEFI CA 2011证书签名的合法BIOS更新工具引起的，大多数现代使用UEFI固件的系统都信任这个证书。

![uefi-tool-signed-with-microsoft-cert.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250611/1749609422323670.jpg "1749608843186473.jpg")

使用Microsoft UEFI CA 2011证书签名的易受攻击模块

此实用程序读取用户可写的 NVRAM 变量（IhisiParamBuffer），但未对其进行验证。如果攻击者拥有操作系统的管理员权限，他们可以修改此变量，从而在 UEFI 启动过程中将任意数据写入内存位置。这一操作发生在操作系统甚至内核加载之前。

利用这一漏洞，Binarly 制作了一个概念验证型漏洞利用程序，将用于强制执行安全启动的“gSecurity2”全局变量清零。

Binarly 的报告解释道：“在我们的概念验证（PoC）中，我们选择覆盖全局变量 gSecurity2。”

此变量保存指向 Security2 架构协议的指针，LoadImage 函数使用该协议来强制执行安全启动。将其设置为零，实际上是禁用了安全启动，从而允许执行任何未签名的 UEFI 模块。

一旦禁用，攻击者就能安装启动恶意软件，这种恶意软件能够躲避操作系统并关闭进一步的安全功能。

为修复 CVE-2025-3052，微软已将受影响模块的哈希值添加到安全启动 dbx 撤销列表中。Binarly 和微软敦促用户通过今日的安全更新立即安装更新后的 dbx 文件，以保护其设备。

今日，Nikolaj Schlej 披露了另一个影响基于 Insyde H2O 的 UEFI 兼容固件的 Secure Boot 旁路漏洞。该漏洞被命名为 Hydroph0bia，并被追踪为 CVE-2025-4275。该漏洞在披露 90 天后被报告给 Insyde 并得到修复。

Binarly 分享了一段视频，展示了他们的概念验证如何能够禁用安全启动，并在操作系统启动前显示一条消息提示。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-secure-boot-flaw-lets-attackers-install-bootkit-malware-patch-now/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?AQXgYrww)

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