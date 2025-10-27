---
title: 黑客正在利用Wing FTP服务器的关键RCE漏洞
url: https://www.4hou.com/posts/NGg6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-19
fetch_date: 2025-10-06T23:28:10.069606
---

# 黑客正在利用Wing FTP服务器的关键RCE漏洞

黑客正在利用Wing FTP服务器的关键RCE漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客正在利用Wing FTP服务器的关键RCE漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-07-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)111298

收藏

导语：即使Huntress观察到针对其客户的失败攻击，黑客也可能会扫描可访问的Wing FTP实例，并试图利用易受攻击的服务器。因此，强烈建议相关公司尽快升级到该产品的7.4.4版本。

近期，黑客在技术细节曝光后的第一天就利用了Wing FTP Server中的一个严重远程代码执行漏洞。观察到的攻击执行了多个枚举和侦察命令，随后通过创建新用户来建立持久性。

被利用的Wing FTP Server漏洞被追踪为CVE-2025-47812，并获得了最高的严重性评分。它是空字节和Lua代码注入的组合，允许未经身份验证的远程攻击者以系统（root/ system）上的最高权限执行代码。

Wing FTP Server是一个强大的解决方案，用于管理可以执行Lua脚本的安全文件传输，它广泛用于企业和SMB环境。

安全研究员Julien Ahrens近期发表了一篇CVE-2025-47812的技术文章，解释说该漏洞源于C++中对以空结尾的字符串的不安全处理以及Lua中不正确的输入处理。

研究人员演示了用户名字段中的空字节如何绕过身份验证检查并使Lua代码注入到会话文件中。当这些文件随后由服务器执行时，可以实现以根/SYSTEM的身份执行任意代码。

除了CVE-2025-47812之外，研究人员还提出了Wing FTP中的另外三个漏洞：

**·**CVE-2025-27889——如果用户提交登录表单，通过构造的URL可以窃取用户密码，因为在JavaScript变量（位置）中包含不安全的密码。

**·**CVE-2025-47811——Wing FTP默认以root/SYSTEM身份运行，没有沙箱或特权下降，使得rce更加危险。

**·**CVE-2025-47813——提供过长的UID cookie会泄露文件系统路径。

所有的漏洞都影响到7.4.3及更早版本的Wing FTP。供应商在2025年5月14日发布了7.4.4版本修复了这些问题，但 CVE-2025-47811被认为不重要，未做修复。

管理网络安全平台Huntress的威胁研究人员创建了CVE-2025-47812的概念验证漏洞，并展示了黑客如何利用它进行攻击：

Huntress的研究人员发现，在7月1日，也就是CVE-2025-47812的技术细节出现的第二天，至少有一个攻击者利用了他们一个客户的漏洞。

攻击者发送了带有空字节注入的用户名的畸形登录请求，目标是‘ loginok.html ’。这些输入创建了恶意session . Lua文件，将Lua代码注入服务器。

注入的代码被设计成十六进制解码有效载荷并通过cmd.exe执行它，使用certutil从远程位置下载恶意软件并执行它。

同一个Wing FTP实例在短时间内被五个不同的IP地址作为攻击目标，这可能表明有几个威胁者试图进行大规模扫描和利用。

在这些尝试中观察到的命令是用于侦察、获取环境中的持久性以及使用cURL工具和webhook端点进行数据泄露。

Huntress表示，黑客攻击失败“可能是因为他们不熟悉这些软件，或者是因为微软防御者阻止了他们的部分攻击”。尽管如此，研究人员还是发现了对Wing FTP服务器关键漏洞的明显利用。

即使Huntress观察到针对其客户的失败攻击，黑客也可能会扫描可访问的Wing FTP实例，并试图利用易受攻击的服务器。因此，强烈建议相关公司尽快升级到该产品的7.4.4版本。

如果切换到更新的安全版本是不可能的，研究人员的建议是禁用或限制HTTP/HTTPs访问到Wing FTP web门户，禁用匿名登录，并监控会话目录的可疑添加。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-are-exploiting-critical-rce-flaw-in-wing-ftp-server/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1PP08rIm)

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