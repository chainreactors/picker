---
title: Ghostscript 库中存在 RCE 漏洞，现已被积极利用
url: https://www.4hou.com/posts/6M8l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-27
fetch_date: 2025-10-06T17:41:29.776076
---

# Ghostscript 库中存在 RCE 漏洞，现已被积极利用

Ghostscript 库中存在 RCE 漏洞，现已被积极利用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Ghostscript 库中存在 RCE 漏洞，现已被积极利用

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-26 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)109745

收藏

导语：Linux 系统上广泛使用的 Ghostscript 文档转换工具包中存在一个远程代码执行漏洞，目前正在遭受攻击。

Linux 系统上广泛使用的 Ghostscript 文档转换工具包中存在一个远程代码执行漏洞，目前正在遭受攻击。

Ghostscript 预装在许多 Linux 发行版上，并被各种文档转换软件使用，包括 ImageMagick、LibreOffice、GIMP、Inkscape、Scribus 和 CUPS 打印系统。

此格式字符串漏洞的编号为 CVE-2024-29510，影响所有 Ghostscript 10.03.0 及更早版本。它使攻击者能够逃离 -dSAFER 沙盒（默认启用），因为未修补的 Ghostscript 版本无法在激活沙盒后阻止对 uniprint 设备参数字符串的更改。

这种安全绕过尤其危险，因为它允许他们使用沙箱通常会阻止的 Ghostscript Postscript 解释器执行高风险操作，例如命令执行和文件 I/O。

发现并报告此安全漏洞的 Codean Labs 安全研究人员警告称：“此漏洞对提供文档转换和预览功能的 Web 应用程序和其他服务有重大影响，因为这些服务通常在后台使用 Ghostscript。”

安全研究人员建议用户验证解决方案是否（间接）使用了 Ghostscript，如果是，请将其更新到最新版本。

Codean Labs 还分享了 Postscript 文件，可以通过以下命令运行它来帮助防御者检测他们的系统是否容易受到 CVE-2023-36664 攻击：

```
ghostscript -q -dNODISPLAY -dBATCH CVE-2024-29510_testkit.ps
```

**在攻击中被积极利用**

Ghostscript 开发团队在 5 月份修补了该安全漏洞，而 Codean Labs 则在两个月后发布了包含技术细节和概念验证漏洞代码的说明。攻击者已经在利用 CVE-2024-29510 Ghostscript 漏洞，使用伪装成 JPG（图像）文件的 EPS（PostScript）文件获取易受攻击系统的 shell 访问权限。

开发人员警告称，如果生产服务中的任何地方有 ghostscript，则会受到令人震惊的远程 shell 执行攻击，应该升级它或将其从生产系统中删除。

Codean Labs 补充道：“针对此漏洞的最佳缓解措施是将 Ghostscript 安装更新至 v10.03.1。如果用户的发行版未提供最新的 Ghostscript 版本，则可能仍发布了包含此漏洞修复程序的补丁版本（例如，Debian、Ubuntu、Fedora）。”

一年前，Ghostscript 开发人员修补了另一个严重的 RCE 漏洞 (CVE-2023-36664)，该漏洞也是由未修补的系统上打开恶意制作的文件引发的。

文章翻译自：https://www.bleepingcomputer.com/news/security/rce-bug-in-widely-used-ghostscript-library-now-exploited-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?d8ueUq56)

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