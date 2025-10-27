---
title: SOAR+HIDS，增强主机安全防护
url: https://www.4hou.com/posts/ZX5J
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-17
fetch_date: 2025-10-04T09:49:20.566214
---

# SOAR+HIDS，增强主机安全防护

SOAR+HIDS，增强主机安全防护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SOAR+HIDS，增强主机安全防护

雾帜智能
[行业](https://www.4hou.com/category/industry)
2023-03-16 17:13:06

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125453

收藏

导语：2019年8月国内首发的AI+SOAR产品——雾帜智能HoneyGuide，通过虚拟作战室、AI机器人和可视化剧本编排和青藤云HIDS进行联动，当发生主机安全事件时，帮助安全团队快速开展日志信息丰富及获取实现自动化、智能化的安全应急响应。

**背景介绍**

随着网络安全攻防对抗的日趋激烈，主机当前企业和组织的安全运营工作面临的挑战越来越突出，外网防护的同时，内网主机安全防护也越来越重要。

HIDS(Host-based Intrusion Detection System)，是基于主机型入侵检测系统的简称。作为计算机系统的监视器和分析器，它并不作用于外部接口，而是专注于系统内部，监视系统全部或部分的动态的行为以及整个计算机系统的状态。作为传统攻防视角的重要一环有着不可替代的作用，可以有效的检测到从网络层面难以发现的安全问题，如：后门，反弹shell，恶意操作，主机组件安全漏洞，系统用户管理安全问题，主机基线安全风险等。代表厂商：青藤云、长亭、安全狗、深信服、启明星辰等。

企业和组织要在主机已经遭受攻击的假定前提下构建集阻止、检测、响应和预防于一体的全新安全防护体系。正是在这样的背景下，SOAR应运而生。SOAR 的全称是Security Orchestration, Automation and Response，意即安全编排自动化与响应。该技术聚焦安全运维领域，重点解决安全响应的问题。它以安全编排和自动化为核心对既有安全产品、网络设备、IT系统和SaaS服务等基础能力进行统筹调度；基于可视化剧本编排和调度执行引擎，开展有逻辑、有顺序的自动化流程操作，实现日常安全事件运营和突发事件处置的过程自动化，辅助安全运营人员日常工作，提升安全运营效率。代表厂商：雾帜智能。

本文将讨论在主机安全防护过程中如何通过SOAR和HIDS的结合，开展更高效、更稳定和更智能的安全保障。

**应用场景**

在主机遭受外部攻击需要开展快速响应时，一线安全事件响应工程师肯定有过这样期望：

1）不在岗时发生安全事件可以被自动处置，并且能够高效、准确；

2）在应急响应期间，只需登录一台设备即可得到所需日志信息，开展快速事件处置。

**解决方案**

2019年8月国内首发的AI+SOAR产品——雾帜智能HoneyGuide，通过虚拟作战室、AI机器人和可视化剧本编排和青藤云HIDS进行联动，当发生主机安全事件时，帮助安全团队快速开展日志信息丰富及获取实现自动化、智能化的安全应急响应。

青藤云产品功能丰富，并且提供非常规范的接口对接方式，便于实现功能调度。联动示例（如下图）

![1678441913132930.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678441913132930.png "1678441913132930.png")

典型客户案例：某金融科技集团公司、某汽车制造集团公司、某能源集团公司、某互联网公司、某交通企业单位。

场景举例：例如终端发现感染病毒，雾帜智能HoneyGuide SOAR通过结合HIDS，通过编排剧本开展快速调用HIDS实现主机日志获取及上下文的信息丰富，极大帮助安全人员开展自动化、快速化的安全事件响应。

**关键步骤**

雾帜智能HoneyGuide SOAR + HIDS，可实现主机进程等日志查询及处置，主要流程：

1. 安全剧本启动后，获取告警日志（来源态势感知或HIDS）；

2. 查询HIDS服务器，并判断事件涉及的主机是否安装HIDS客户端或杀毒客户端；

3. 查询CMDB获取资产负责人/所有者，及资产所在资产组管理员的信息（邮箱等信息）；

4. 根据HIDS返回的客户端安装情况，执行相应操作：

（1）有杀毒客户端，更新并启动杀毒；

（2）有HIDS客户端，启动后门扫描查杀；

（3）未装任何客户端，邮件通知资产负责人/所有者/资产组管理员。

5.  将异常结果通知资产负责人/所有者，如果没有查询到资产负责人/所有者，则通知资产组管理员：终端未装任何客户端，杀毒软件更新失败或杀毒或后门查杀发现了异常。根据不同判断进行对应通知。

![1678441862140087.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230310/1678441862140087.png "1678441862140087.png")

**方案成效**

通过落地雾帜智能HoneyGuide SOAR+ HIDS的组合，大幅节约响应时间，降低人员依赖，保障应急处置质量。主要体现在以下方面：

1）防护全：7\*24小时安全事件响应，做到全时段防护，避免人员不在岗风险；

2）速度快：自动化剧本响应做到秒级、分钟级事件处置，大幅提高响应效率；

3）流程稳：安全事件处理流程剧本化，做到安全事件处置流程化、标准化，避免因人员变动导致无法进行安全响应。

**总结**

通过SOAR+HIDS可以使主机安全防护响应更加全面和高效，无需安全人员登录平台手工查询日志，自动和上下游能力协作，开展自动化、快速化、高效化的应急响应，提升MTTR水平。目前雾帜智能HoneyGuide SOAR产品已经实现支持联动国内外主流终端防护系统：青藤云主机安全、深信服终端响应、赛门铁克SEP、奇安信天擎终端安全等，并且还在持续扩充中。

**雾帜智能**

雾帜智能自2019年成立以来始终坚持在SOAR领域持续创新，专注于网络安全技术和产品的自主研发为核心，秉承“充分运用人工智能和自动化技术，为智能安全运营提供创新的技术和产品”的企业使命，为客户提供高质量的产品和服务。

雾帜智能以先发产品的优势、点纵横的市场打法和持续创新的自我突破，使得公司在SOAR市场始终保持遥遥领先的位置。目前公司已形成了以上海为总部，覆盖北京、广州、深圳、济南、合肥、杭州、武汉、成都等地的全国性服务支撑体系，并构建了强大的合作伙伴与渠道营销体系；客户已覆盖政府、教育、互联网、金融、运营商、能源、烟草、汽车制造等行业。

**青藤云安全**

青藤云安全运用云计算、大数据、AI等技术，采用自适应安全架构，构建基于主机端的安全态势感知平台，为用户提供持续的安全监控、分析和快速响应能力。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ygQkYmHL)

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

![](https://img.4hou.com/portraits/b0fab1927d88da9f7da8efe2f1bb29c4.jpg)

# [雾帜智能](https://www.4hou.com/member/lgY1)

专注SOAR,全面加速应急响应！

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/lgY1)

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