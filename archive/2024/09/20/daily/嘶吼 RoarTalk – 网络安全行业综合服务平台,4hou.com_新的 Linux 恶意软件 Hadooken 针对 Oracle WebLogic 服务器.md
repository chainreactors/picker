---
title: 新的 Linux 恶意软件 Hadooken 针对 Oracle WebLogic 服务器
url: https://www.4hou.com/posts/Zg0v
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-20
fetch_date: 2025-10-06T18:25:20.472648
---

# 新的 Linux 恶意软件 Hadooken 针对 Oracle WebLogic 服务器

新的 Linux 恶意软件 Hadooken 针对 Oracle WebLogic 服务器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Linux 恶意软件 Hadooken 针对 Oracle WebLogic 服务器

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-09-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102316

收藏

导语：攻击者之所以将 WebLogic 视为目标，是因为它在业务关键型环境中非常受欢迎，这些环境通常拥有丰富的处理资源，是加密货币挖矿和 DDoS 攻击的理想选择。

黑客瞄准 Oracle WebLogic 服务器，用一种名为“Hadooken”的新 Linux 恶意软件感染它们，该恶意软件会启动一个加密矿工和一个分布式拒绝服务 (DDoS) 攻击工具。

获得的访问权限还可能用于对 Windows 系统执行勒索软件攻击。容器安全解决方案公司 Aqua Security 的研究人员在蜜罐上观察到了这种攻击，威胁者由于凭证薄弱而攻破了蜜罐。

Oracle WebLogic Server 是一款企业级 Java EE 应用服务器，用于构建、部署和管理大规模分布式应用程序。该产品常用于银行和金融服务、电子商务、电信、政府组织和公共服务。

攻击者之所以将 WebLogic 视为目标，是因为它在业务关键型环境中非常受欢迎，这些环境通常拥有丰富的处理资源，是加密货币挖矿和 DDoS 攻击的理想选择。

**Hadooken 猛烈攻击**

一旦攻击者破坏环境并获得足够的权限，他们就会下载名为“c”的 shell 脚本和名为“y”的 Python 脚本。

研究人员表示，这两个脚本都会释放 Hadooken，但 shell 代码还会尝试在各个目录中查找 SSH 数据，并利用这些信息攻击已知服务器。此外，“c”还会在网络上横向移动以分发 Hadooken。

![ssh-seek.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240918/1726654041166036.png "1726653902160115.png")

在已知主机上搜索 SSH 密钥

反过来，Hadooken 会投放并执行加密货币挖矿程序和 Tsunami 恶意软件，然后设置多个 cron 作业，这些作业的名称和有效负载执行频率都是随机的。

Tsunami 是一种 Linux DDoS 僵尸网络恶意软件，它通过对弱密码进行暴力攻击来感染易受攻击的 SSH 服务器。

攻击者之前曾使用 Tsunami 对受感染的服务器发起 DDoS 攻击和远程控制，而它再次被发现与 Monero 矿工一起部署。

Aqua Security 研究人员强调，Hadooken 将恶意服务重命名为“-bash”或“-java”，以模仿合法进程并与正常操作混合。

完成此过程后，系统日志将被清除以隐藏恶意活动的迹象，从而使发现和取证分析变得更加困难。

对 Hadooken 二进制文件的静态分析揭示了与 RHOMBUS 和 NoEscape 勒索软件家族的联系，但在观察到的攻击中没有部署勒索软件模块。

研究人员推测，在某些条件下，例如在操作员进行手动检查后，服务器访问权限可能会被用来部署勒索软件。未来版本也有可能引入此功能。

![attack-overview.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240918/1726654043172214.png "1726653984111740.png")

Hadooken 攻击概述

此外，在提供 Hadooken (89.185.85[.]102) 的其中一台服务器上，研究人员发现了一个 PowerShell 脚本，该脚本下载了适用于 Windows 的 Mallox 勒索软件。

有报道称，该 IP 地址用于传播勒索软件，因此我们可以假设威胁者不仅针对 Windows 端点执行勒索软件攻击，还针对 Linux 服务器，以攻击大型组织经常使用的软件来启动后门和加密矿工 - Aqua Security

根据研究人员使用 Shodan 搜索引擎对联网设备进行搜索的结果显示，公共网络上已有超过 230,000 台 Weblogic 服务器。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-linux-malware-hadooken-targets-oracle-weblogic-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Ip2Ntxu8)

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