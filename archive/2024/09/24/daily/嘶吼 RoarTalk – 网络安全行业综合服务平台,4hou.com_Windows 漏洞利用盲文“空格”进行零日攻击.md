---
title: Windows 漏洞利用盲文“空格”进行零日攻击
url: https://www.4hou.com/posts/YZ50
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-24
fetch_date: 2025-10-06T18:24:48.048290
---

# Windows 漏洞利用盲文“空格”进行零日攻击

Windows 漏洞利用盲文“空格”进行零日攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows 漏洞利用盲文“空格”进行零日攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-09-23 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)101659

收藏

导语：微软在 9 月补丁星期二修复了其他三个被积极利用的零日漏洞，其中包括 CVE-2024-38217，该漏洞被利用于 LNK 踩踏攻击中以绕过 Web 安全功能的标记。

最近修复的“Windows MSHTML 欺骗漏洞”被追踪为 CVE-2024-43461，现在被标记为之前已被利用，因为它曾被 Void Banshee APT 黑客组织用于攻击。在 2024 年 9 月补丁星期二首次披露时，微软并未将该漏洞标记为之前被利用。然而，微软在最新更新的 CVE-2024-43461 公告中，表明它在修复之前曾被利用用于攻击。

该漏洞的发现归功于零日高级威胁研究员 Peter Girnus，他发现 Void Banshee 在零日攻击中利用 CVE-2024-43461 漏洞来安装窃取信息的恶意软件。

Void Banshee 是其首次追踪的一个 APT 黑客组织，其目标是北美、欧洲和东南亚的组织，以窃取数据和获取经济利益为主要目的。

**CVE-2024-43461 零日漏洞**

7 月份，Check Point Research 和 Trend Micro 均报告了同样的攻击，这些攻击利用 Windows 零日漏洞感染设备，并安装 Atlantida 信息窃取程序，用于从受感染设备窃取密码、身份验证 cookie 和加密货币钱包。

此次攻击利用了被追踪为 CVE-2024-38112（7 月修复）和 CVE-2024-43461（本月修复）的零日漏洞作为攻击链的一部分。

CVE-2024-38112 零日漏洞的发现归功于 Check Point 研究员 Haifei Li，他表示，该漏洞被用来强制 Windows 在启动特制的快捷方式文件时在 Internet Explorer 中打开恶意网站，而不是在 Microsoft Edge 中打开。

研究员在 7 月份的 Check Point Research 报告中解释道：“攻击者使用特殊的 Windows Internet 快捷方式文件（.url 扩展名），单击该文件时，会调用已退役的 Internet Explorer（IE）来访问攻击者控制的 URL。”

这些 URL 用于下载恶意 HTA 文件并提示用户打开它。打开后，将运行脚本来安装 Atlantida 信息窃取程序。HTA 文件利用另一个零日漏洞（跟踪为 CVE-2024-43461）来隐藏 HTA 文件扩展名，并在 Windows 提示用户是否应打开时使文件显示为 PDF，如下所示。

ZDI 研究员 Peter Girnus 表示，CVE-2024-43461 漏洞也被用于 Void Banshee 攻击，通过包含 26 个编码盲文空白字符 (%E2%A0%80) 的 HTA 文件名创建 CWE-451 条件以隐藏 .hta 扩展名。

如下所示，文件名以 PDF 文件开头，但包含 26 个重复编码盲文空白字符 (%E2%A0%80)，后跟最后的“.hta”扩展名。

```
Books_A0UJKO.pdf%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80%E2%A0%80.ht
```

当 Windows 打开此文件时，盲文空白字符会将 HTA 扩展推到用户界面之外，仅在 Windows 提示中用“...”字符串划定界限，如下所示。这导致 HTA 文件显示为 PDF 文件，使其更有可能被打开。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240923/1727055617140614.png "1727055617140614.png")

盲文空白字符将 HTA 扩展推离了视线

安装 CVE-2024-43461 的安全更新后，Girnus 表示空格未被删除，但 Windows 现在在提示中显示文件的实际 .hta 扩展名。

![security-update-shows-extension.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240923/1727055584211171.png "1726648452119685.png")

但这个修复并不完美，因为包含的空格可能仍然会让人们误以为该文件是 PDF 而不是 HTA 文件。

微软在 9 月补丁星期二修复了其他三个被积极利用的零日漏洞，其中包括 CVE-2024-38217，该漏洞被利用于 LNK 踩踏攻击中以绕过 Web 安全功能的标记。

文章翻译自：https://www.bleepingcomputer.com/news/security/windows-vulnerability-abused-braille-spaces-in-zero-day-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?weWa5U10)

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