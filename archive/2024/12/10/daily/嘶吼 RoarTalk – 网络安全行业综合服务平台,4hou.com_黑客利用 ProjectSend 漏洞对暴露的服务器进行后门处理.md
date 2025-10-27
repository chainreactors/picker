---
title: 黑客利用 ProjectSend 漏洞对暴露的服务器进行后门处理
url: https://www.4hou.com/posts/pnBX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-10
fetch_date: 2025-10-06T19:35:10.038228
---

# 黑客利用 ProjectSend 漏洞对暴露的服务器进行后门处理

黑客利用 ProjectSend 漏洞对暴露的服务器进行后门处理 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 ProjectSend 漏洞对暴露的服务器进行后门处理

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-12-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103121

收藏

导语：尽管该漏洞已于 2023 年 5 月 16 日得到修复，但直到近期才为其分配了 CVE，导致用户没有意识到其严重性以及应用安全更新的紧迫性。

恶意分子正在利用 ProjectSend 中的一个关键身份验证绕过漏洞的公共漏洞来上传 Webshell 并获得对服务器的远程访问。

该漏洞被追踪为 CVE-2024-11680，是一个严重的身份验证错误，影响 r1720 之前的 ProjectSend 版本，允许攻击者向“options.php”发送特制的 HTTP 请求以更改应用程序的配置。

成功利用该漏洞可以创建流氓帐户、植入 Webshell 以及嵌入恶意 JavaScript 代码。

尽管该漏洞已于 2023 年 5 月 16 日得到修复，但直到近期才为其分配了 CVE，导致用户没有意识到其严重性以及应用安全更新的紧迫性。

根据已检测到活跃利用的 VulnCheck 的说法，到目前为止，修补速度非常糟糕，99% 的 ProjectSend 实例仍在运行易受攻击的版本。

**数千个实例被曝光**

ProjectSend 是一款开源文件共享 Web 应用程序，旨在促进服务器管理员和客户端之间安全、私密的文件传输。它是一款颇受欢迎的应用程序，被那些更喜欢自托管解决方案而不是 Google Drive 和 Dropbox 等第三方服务的组织所使用。

VulnCheck 表示，在线大约有 4,000 个面向公众的 ProjectSend 实例，其中大多数都容易受到攻击。具体来说，根据 Shodan 数据，55% 的暴露实例运行 2022 年 10 月发布的 r1605，44% 使用 2023 年 4 月的未命名版本，只有 1% 运行修补版本 r1750。

VulnCheck 报告称，发现 CVE-2024-11680 的主动利用不仅限于测试，还包括更改系统设置以允许用户注册、获得未经授权的访问以及部署 Webshell 以保持对受感染服务器的控制。

![registration.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733125343941224.png "1733123442100089.png")

启用新用户注册

自 2024 年 9 月 Metasploit 和 Nuclei 发布 CVE-2024-11680 的公共漏洞以来，此活动有所增加。

报告中写道：“VulnCheck 注意到面向公众的 ProjectSend 服务器已开始将其登陆页面标题更改为长的、随机的字符串。这些又长又随机的名称符合 Nuclei 和 Metasploit 实施漏洞测试逻辑的方式。”

这两种漏洞利用工具都会修改受害者的配置文件，以使用随机值更改站点名称（以及 HTTP 标题）。GreyNoise 列出了与此活动相关的 121 个 IP，表明存在广泛的尝试，而不是孤立的来源。

![shodan-victims(1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733125343185823.jpg "1733123494192259.jpg")

Shodan 上出现的攻击受害者

VulnCheck 警告称，Webshell 存储在“upload/files”目录中，名称由 POSIX 时间戳、用户名的 SHA1 哈希值以及原始文件名/扩展名生成。

通过 Web 服务器直接访问这些文件表明存在积极的利用行为。基于攻击可能已经很普遍存在，研究人员建议用户尽快升级到 ProjectSend r1750 版本。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-exploit-projectsend-flaw-to-backdoor-exposed-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?VSiDDIHP)

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