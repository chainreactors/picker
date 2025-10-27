---
title: 新的 Migo 恶意软件禁用 Redis 服务器上的保护功能
url: https://www.4hou.com/posts/YY3Y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-03-15
fetch_date: 2025-10-04T12:07:59.093462
---

# 新的 Migo 恶意软件禁用 Redis 服务器上的保护功能

新的 Migo 恶意软件禁用 Redis 服务器上的保护功能 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Migo 恶意软件禁用 Redis 服务器上的保护功能

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-03-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)187207

收藏

导语：Migo 活动由云取证提供商 Cado Security的分析师所发现。

安全研究人员最新发现一起针对 Linux 主机上的 Redis 服务器的安全活动——威胁组织正使用名为“Migo”的恶意软件来挖掘加密货币。

Redis（远程字典服务器）是一种内存数据结构存储，用作数据库、缓存和消息代理，以其高性能而闻名，每秒为游戏、技术、金融服务等行业的实时应用程序提供数千个请求。

威胁组织通常利用暴露的和可能易受攻击的 Redis 服务器来劫持资源、窃取数据和实施其他恶意目的。

新的恶意软件的不同之处在于使用系统削弱命令来关闭 Redis 安全功能，从而允许加密劫持活动较长时间持续。

Migo 活动由云取证提供商 Cado Security的分析师所发现，他们在蜜罐中观察到攻击者使用 CLI 命令关闭保护配置并利用服务器。

**关闭 Redis 防护罩**

在暴露的 Redis 服务器受到攻击后，攻击者会禁用关键的安全功能，以允许接收后续命令并使副本可写。

Cado 表示，他们注意到攻击者通过 Redis CLI 禁用了以下配置选项：

**·**set protected-mode：禁用此选项将允许外部访问 Redis 服务器，从而使攻击者更容易远程执行恶意命令。

**·**replica-read-only：关闭此功能使攻击者能够直接写入副本并在分布式 Redis 设置中传播恶意负载或数据修改。

**·**aof-rewrite-incremental-fsync：禁用它可能会导致在仅追加文件 (AOF) 重写期间产生更重的 IO 负载，来帮助攻击者不被检测到。

**·**rdb-save-incremental-fsync：关闭它可能会导致 RDB 快照保存期间性能下降，从而可能允许攻击者造成拒绝服务 (DoS) 或操纵持久性行为以获取优势。

![command.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240221/1708506274161505.jpg "1708506244810339.jpg")

观察命令执行

攻击者设置一个 cron 作业，从 Pastebin 下载脚本，该脚本从 Transfer.sh 检索 Migo 的主要负载 (/tmp/.migo) 以作为后台任务执行。

这是一个用 Go 编译的 UPX 打包的 ELD 二进制文件，具有编译时混淆功能以阻碍分析。

Migo 的主要功能是直接从 GitHub 的 CDN 在受感染的端点上获取、安装和启动修改后的 XMRig (Monero) 挖矿程序。

该恶意软件通过创建 systemd 服务和关联的计时器来为矿工建立持久性，确保其连续运行，以攻击者的帐户挖掘加密货币。

![code.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240221/1708506275117396.jpg "1708506270145551.jpg")

Migo 的 Linux 系统调用序列

Cado 报告称，Migo 使用用户模式 rootkit 来隐藏其进程和文件，从而使检测和删除变得复杂。

该恶意软件修改“/etc/ld.so.preload”以拦截和更改列出进程和文件的系统工具的行为，从而有效地隐藏其存在。

攻击结束时，Migo 设置防火墙规则来阻止某些 IP 的出站流量，并执行命令来禁用 SELinux、搜索并可能禁用云提供商监控代理，并删除竞争的矿工或有效负载。

它还操纵 /etc/hosts 以阻止与云服务提供商的通信，从而进一步隐藏其活动。

Migo 的攻击链表明，其背后的威胁组织对 Redis 环境和操作已有了深入了解。尽管加密劫持威胁并不太严重，但威胁组织却可以利用该访问权限来传递更危险的有效负载。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-migo-malware-disables-protection-features-on-redis-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hHzI4Ps9)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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