---
title: Leaky Vessels 缺陷允许黑客逃离 Docker、runc 容器
url: https://www.4hou.com/posts/EX3l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-02-28
fetch_date: 2025-10-04T12:06:16.409362
---

# Leaky Vessels 缺陷允许黑客逃离 Docker、runc 容器

Leaky Vessels 缺陷允许黑客逃离 Docker、runc 容器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Leaky Vessels 缺陷允许黑客逃离 Docker、runc 容器

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-02-27 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)204729

收藏

导语：Snyk安全研究员发现了这些缺陷 ，并建议所有受影响的系统管理员尽快应用可用的安全更新。

**逃逸容器**

容器是打包到文件中的应用程序，其中包含运行应用程序所需的所有运行时依赖项、可执行文件和代码。这些容器由 Docker 和 Kubernetes 等平台执行，这些平台在与操作系统隔离的虚拟化环境中运行应用程序。

当攻击者或恶意应用程序突破隔离的容器环境，并获得对主机系统或其他容器未经授权的访问时，就会发生容器逃逸。

Snyk 团队发现了四个缺陷，统称为“Leaky Vessels”，这些缺陷影响 runc 和 Buildkit 容器基础设施和构建工具，可能允许攻击者在各种软件产品上执行容器逃逸。

![blog-cve-2024-21626-docker-run[1].gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240206/1707201194210793.gif "1707201174118779.gif")

演示利用 Leaky Vessels 访问主机上的数据

由于 runc 或 Buildkit 被广泛流行的容器管理软件（例如 Docker 和 Kubernetes）使用，因此遭受攻击的风险更加严重。

**泄漏容器缺陷总结如下：**

**·**CVE-2024-21626：由于 runc 中 WORKDIR 命令的操作顺序缺陷而产生的错误。它允许攻击者逃离容器的隔离环境，授予对主机操作系统的未经授权的访问权限，并可能危及整个系统。

**·**CVE-2024-23651：Buildkit 的挂载缓存处理中的竞争条件导致不可预测的行为，可能允许攻击者操纵进程进行未经授权的访问或中断正常的容器操作。

**·**CVE-2024-23652：允许在 Buildkit 的容器拆卸阶段任意删除文件或目录的缺陷。它可能导致拒绝服务、数据损坏或未经授权的数据操纵。

**·**CVE-2024-23653：此缺陷是由于 Buildkit 的 GRPC 接口中的权限检查不足而引起的。它可能允许攻击者执行超出其权限的操作，从而导致权限升级或未经授权访问敏感数据。

**影响和补救**

Buildkit 和 runc 被 Docker 和多个 Linux 发行版等流行项目广泛使用。

因此，“Leaky Vessels”缺陷的修补需要 Snyk 的安全研究团队、受影响组件（runc 和 BuildKit）的维护者以及更广泛的容器基础设施社区之间协调行动。

2024 年 1 月 31 日，Buildkit 在 0.12.5 版本中修复了该缺陷，runc 在1.1.12 版本中解决了影响其的安全问题 。

Docker  同日发布了 4.27.0 版本，将组件的安全版本合并到其 Moby 引擎中，版本为 25.0.1 和 24.0.8。

Amazon Web Services、  Google Cloud和 Ubuntu 也发布了相关安全公告，指导用户通过适当的步骤来解决其软件和服务中的缺陷。

  CISA 也发布了一份警报， 敦促云系统管理员可以采取适当的措施，以保护其系统免受潜在利用。

文章翻译自：https://www.bleepingcomputer.com/news/security/leaky-vessels-flaws-allow-hackers-to-escape-docker-runc-containers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SC8YTHsH)

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