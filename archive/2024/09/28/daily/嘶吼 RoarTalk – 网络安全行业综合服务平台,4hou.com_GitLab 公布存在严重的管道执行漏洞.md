---
title: GitLab 公布存在严重的管道执行漏洞
url: https://www.4hou.com/posts/BvPx
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-28
fetch_date: 2025-10-06T18:24:53.431440
---

# GitLab 公布存在严重的管道执行漏洞

GitLab 公布存在严重的管道执行漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GitLab 公布存在严重的管道执行漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-09-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103489

收藏

导语：该问题影响 CE/EE 版本 8.14 至 17.1.7、17.2 至 17.2.5 之前的版本以及 17.3 至 17.3.2 之前的版本。

GitLab 发布了关键更新以解决多个漏洞，其中最严重的漏洞 (CVE-2024-6678) 允许攻击者在特定条件下以任意用户身份触发管道。

此版本适用于 GitLab 社区版 (CE) 和企业版 (EE) 的 17.3.2、17.2.5 和 17.1.7 版本，并作为每两个月 (计划) 安全更新的一部分修补了总共 18 个安全问题。

CVE-2024-6678 漏洞的严重程度评分为 9.9，该漏洞可能使攻击者能够以停止操作作业的所有者的身份执行环境停止操作。

该漏洞的严重性在于其可能被远程利用、缺乏用户交互以及利用该漏洞所需的权限较低。GitLab 称，该问题影响 CE/EE 版本 8.14 至 17.1.7、17.2 至 17.2.5 之前的版本以及 17.3 至 17.3.2 之前的版本。他们强烈建议所有运行受下述问题影响的版本的安装尽快升级到最新版本。

GitLab 管道是用于构建、测试和部署代码的自动化工作流程，是 GitLab CI/CD（持续集成/持续交付）系统的一部分。它们旨在通过自动执行重复任务并确保对代码库的更改进行一致测试和部署来简化软件开发流程。

GitLab 近几个月多次解决任意管道执行漏洞，包括 2024 年 7 月修复 CVE-2024-6385、2024 年 6 月修复 CVE-2024-5655 以及 2023 年 9 月修补 CVE-2023-5009，均被评为严重。

该公告还列出了四个严重性较高的问题，评分在 6.7 到 8.5 之间，这些问题可能会让攻击者破坏服务、执行未经授权的命令或破坏敏感资源。这些问题总结如下：

**·CVE-2024-8640**：由于输入过滤不当，攻击者可以通过 YAML 配置将命令注入连接的 Cube 服务器，从而可能损害数据完整性。从 16.11 开始影响 GitLab EE。

**·CVE-2024-8635**：攻击者可以通过制作自定义 Maven 依赖代理 URL 来向内部资源发出请求，从而利用服务器端请求伪造 (SSRF) 漏洞，从而危害内部基础设施。从 16.8 开始影响 GitLab EE。

**·CVE-2024-8124**：攻击者可以通过发送较大的“glm\_source”参数触发 DoS 攻击，从而使系统不堪重负并不可用。从 16.4 开始影响 GitLab CE/EE。

**·CVE-2024-8641**：攻击者可以利用 CI\_JOB\_TOKEN 获取受害者 GitLab 会话令牌的访问权限，从而劫持会话。从 13.7 开始影响 GitLab CE/EE。

文章翻译自：https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-pipeline-execution-vulnerability/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?C00fS7l7)

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