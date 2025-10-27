---
title: TP-Link确认路由器存在未修复零日漏洞
url: https://www.4hou.com/posts/YZ8p
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-11
fetch_date: 2025-10-02T19:57:11.103572
---

# TP-Link确认路由器存在未修复零日漏洞

TP-Link确认路由器存在未修复零日漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# TP-Link确认路由器存在未修复零日漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-09-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)48854

收藏

导语：在TP-Link明确受影响设备清单并发布修复程序前，用户应采取以下措施。

目前，TP-Link已确认多款路由器型号存在未修复的零日漏洞，该公司路由器的其他漏洞已被用于实际攻击。

**零日漏洞详情与厂商响应**

该零日漏洞由独立威胁研究员Mehrun发现。他表示，已于2024年5月11日首次向TP-Link报告此问题。

TP-Link证实，目前正在调查该漏洞的可利用性及影响范围。据悉，针对欧洲地区型号的补丁已开发完成，但针对美国及全球其他地区固件版本的修复程序仍在开发中，尚未给出具体发布时间。TP-Link强烈建议所有用户通过官方支持渠道及时为设备安装最新固件更新。

该漏洞目前尚未分配CVE编号，其本质是TP-Link多款路由器（具体数量未知）的CWMP（客户终端设备广域网管理协议）实现中存在的栈溢出漏洞。

研究员Mehrun通过对路由器二进制文件进行自动化污点分析发现了该漏洞，他解释称，漏洞存在于处理SOAP协议SetParameterValues消息的函数中。问题根源在于“strncpy”调用时缺乏边界检查，当栈缓冲区大小超过3072字节时，攻击者可通过缓冲区溢出实现远程代码执行（RCE）。

Mehrun表示，实际攻击场景可能是：将易受攻击的设备重定向至恶意CWMP服务器，然后发送超大SOAP有效载荷以触发缓冲区溢出。要实现这一点，攻击者可利用过时固件中的漏洞，或使用用户未更改的默认凭据访问设备。

一旦通过远程代码执行攻陷路由器，攻击者可指令其将DNS查询重定向至恶意服务器、暗中拦截或篡改未加密流量，以及在网页会话中注入恶意有效载荷。

研究员通过测试确认，TP-Link Archer AX10和Archer AX1500两款路由器使用了存在漏洞的CWMP二进制文件。这两款均为热门型号。

Mehrun还指出，EX141、Archer VR400、TD-W9970以及其他多款TP-Link路由器型号也可能受到影响。

在TP-Link明确受影响设备清单并发布修复程序前，用户应采取以下措施：更改默认管理员密码；如无需使用CWMP，应将其禁用；为设备安装最新固件；如有可能，将路由器与核心网络进行隔离。

**TP-Link已被利用漏洞**

上周，CISA将TP-Link的另外两个漏洞（编号CVE-2023-50224和CVE-2025-9377）添加至“已知被利用漏洞目录”。这两个漏洞已被Quad7僵尸网络利用以攻陷路由器。

其中，CVE-2023-50224为身份验证绕过漏洞，CVE-2025-9377为命令注入漏洞。攻击者将两个漏洞结合利用，可在易受攻击的TP-Link设备上实现远程代码执行。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-tp-link-zero-day-surfaces-as-cisa-warns-other-flaws-are-exploited/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MPjHozIv)

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