---
title: 软件供应链风险犹在，平台工程的安全危机如何解决？
url: https://www.4hou.com/posts/poVV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:37.480218
---

# 软件供应链风险犹在，平台工程的安全危机如何解决？

软件供应链风险犹在，平台工程的安全危机如何解决？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 软件供应链风险犹在，平台工程的安全危机如何解决？

企业资讯
[行业](https://www.4hou.com/category/industry)
2023-07-31 16:23:31

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)95819

收藏

导语：9月2日，国内首届平台工程技术峰会将在北京召开

国际权威知名调研机构 Gartner 在《2023年最重要的10个技术趋势》报告中将平台工程（Platform Engineering）列为高速发展的技术趋势之一，并预测到2026年80%的软件企业都将搭建平台团队以为内部的工程师提供可复用的服务、组件以及工具来帮助应用交付。

![1280X1280.PNG](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690791737184580.png "1690791737184580.png")

平台工程是一门新兴技术，专注于通过减少现代软件交付的复杂性和不确定性来提高开发人员的生产力。它解决了规模化DevOps的一些最大挑战，包括减少在整个应用生命周期内管理复杂工具和基础设施网络的负担。无论是基础设施配置、流水线、监控还是容器管理等，自助服务平台将所有这些复杂的问题放入黑盒中，进而为开发人员提供开箱即用的所有必要工具。

平台团队将基础设施管理自动化，并使开发人员能够从一个集中管理的技术平台上自助获取可靠的工具和工作流程，进而减轻开发团队的认知负担。可以说，平台工程是云原生软件交付的一个重要转向。

尽管平台工程已经受到诸多知名企业的青睐，但针对平台工程的质疑却从未停止，其中最为值得注意的是安全方面的指控。

Gartner 调查报告表明，平台团队认为在不破坏开发者体验的情况下满足应用的安全要求是十分困难的，同时碎片化的开发流程和繁杂的工具也很难保持安全策略的一致性。在软件供应链安全风险激增的当下，这显然成为悬在每个人头上的“达摩克利斯之剑”。

针对当前云原生软件供应链安全，由于应用成分更为复杂的现状，传统解决方案具有很大的局限性，因此我们不妨将目光投向 SBOM （软件物料清单）。

SBOM 是一种正式且可查询的记录信息，其中包含用于构建软件的各种组件的详细信息和关系，包括开源软件和所有引入的第三方软件。SBOM 提供的清单是安全软件开发框架（secure software development framework）的关键要素，有助于在软件开发过程中检测漏洞，协助开发团队管理依赖项、识别安全问题以减少其重复的工作，并在软件生命周期中持续发挥作用。

去年，开源软件基金会（OpenSSF）发布的一项安全动员计划中就包括了推动 SBOM 无处不在的目标。旨在帮助推动 SBOM 作为基础构建块的应用，以改善整个开源生态系统的安全状况。该计划的核心思想是让 OSS 生态系统能够为其软件的每个版本提供准确的 SBOM。对于 OSS 厂商、用户和维护者，SBOM 提供的软件产品中所有组件的最终列表，可用于在软件开发生命周期的每个阶段识别现有漏洞和新漏洞。

在 Gartner 的报告中为平台工程的内部开发者平台的默认安全能力提供了一个推荐模型，其中明确列出在保障代码安全方面需要验证 SBOM。

![1280X1280 (1).PNG](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690791762650101.png "1690791762650101.png")

**9月2日，国内首届平台工程技术峰会将在北京召开，本次峰会以“AIGC时代下的平台工程”为主题，安易科技创始人兼CEO韩春雷先生将在峰会现场以《基于软件物料清单的平台工程安全思考》为主题，分享如何基于SBOM软件物料清单优化目前的平台工程体系，探索软件供应链成分透明度与全链路建设，降低软件供应链风险。届时，还有来自小米、滴滴、蚂蚁集团的技术负责人分享平台工程的落地实践。点击此处查看峰会完整议程并报名：[https://hdxu.cn/CNCed](https://hdxu.cn/CNCed "https://hdxu.cn/CNCed")**

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?a61wwsX6)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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