---
title: 360发布全球首份智能体安全报告，剖析Google、Intel等知名开源产品风险
url: https://www.4hou.com/posts/XPvW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-19
fetch_date: 2025-10-06T23:28:11.057332
---

# 360发布全球首份智能体安全报告，剖析Google、Intel等知名开源产品风险

360发布全球首份智能体安全报告，剖析Google、Intel等知名开源产品风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 360发布全球首份智能体安全报告，剖析Google、Intel等知名开源产品风险

企业资讯
[行业](https://www.4hou.com/category/industry)
2025-07-18 10:13:34

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)70238

收藏

导语：“以模制模”实践成果+1！360联合清华大学发布智能体安全实践报告。

当前，人工智能正迈入规模化应用落地阶段，智能体（AI Agent）作为具备环境感知、自主决策、任务执行等核心能力的智能化实体，呈现出多样化发展趋势。与此同时，智能体带来的安全风险也与日俱增。

近日，**360联合清华大学发布全球首份漏洞视角的《智能体安全实践报告》**，通过典型攻击面梳理和漏洞挖掘研究，深入分析智能体全生命周期链路各个场景的安全风险。**结合360安全智能体的高效代码分析能力以及特有的特征库，分析报告了智能体相关开源项目漏洞20余个，其中不乏被广泛使用的Github高星项目**，旨在提供智能体安全的综合性视角，为智能体安全生态的持续、积极发展贡献力量。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250718/1752804585208170.png "1752804585208170.png")

**框架层藏开发隐患，易成攻击突破口**

智能体架构通常由模型、工具、编排三个主要组件构成，开发框架则以模块化、可扩展性和快速编排能力为核心，提供一系列预设工具和基础功能，进而简化了智能体的构建与部署流程，提升了整体开发效率。但框架中的潜在安全问题也提供了额外的攻击向量，使其变为恶意攻击者通过网络发起攻击的“帮凶”。

**报告指出，智能体开发框架无论是仅建立在本地服务，或是部署在云端的接口，都存在着从远程被攻破的可能**。一方面，启动本地服务的开发框架通常默认所有的请求都是可信任的，缺少对请求发起方的身份验证以及对请求中包含数据的二次验证，极易成为攻击者横向渗透的目标，且存在经由浏览器转发请求从而进行远程攻击的可能；另一方面，部署在云端的接口中一旦存在漏洞，攻击者就能利用它来影响整个业务系统的安全。

**生态层现协同风险，安全边界模糊**

随着业务复杂度的提升，参与到智能体系统运作中的成员日益复杂，智能体系统对多角色、多工具的整合能力使其安全边界愈发模糊。而智能体通过自然语言形式来驱动的特性，使其天然易受外界的干扰和影响。

报告指出，在智能体系统中，**大模型通常作为核心感知与决策模块，大模型的输出结果在很大程度上决定了智能体的行为走向**，智能体的正确推理和响应很大程度上也依赖于可靠的输入信息。因此，攻击者可以通过操纵大模型生成包含恶意内容或错误流程的响应，从而间接影响智能体的行为。

此外，随着MCP（Model Context Protocol）规范提出了大模型与工具之间的通用通信框架，极大拓展了智能体的能力边界，智能体接入的工具愈发复杂多样，调用链条越来越长，MCP Server投毒、MCP Server远程风险、MCP Client恶意请求等一系列安全风险也随之显现。

**沙箱层存配置盲区，亟需多层级防护**

为了避免智能体在应用过程中的操作风险，通常会使用沙箱隔离方案，即将智能体调用工具的执行环境与真实系统分离，在沙箱内完成操作指令后，将执行结果返回大模型，从而保障工具调用的安全性。

然而，当前主流沙箱虽能快速构建文件系统与代码执行的隔离环境，却普遍缺乏对智能体应用场景的精细化配置，无法完全保障隔离效果的可靠性。此外，沙箱自身存在的安全漏洞也可能成为新的攻击入口，进一步影响智能体整体安全。

**以模制模，360安全智能体守护智能体安全**

报告指出，智能体的全生命周期安全风险呈现多维性、隐蔽性和系统性特征，其安全威胁渗透在开发、测试、部署和运营等一系列的流程中，**只有将安全性作为智能体技术演进的核心指标，而非事后补救的附加功能，才能推动智能体真正成为人类社会的可靠伙伴**。

作为国内唯一兼具数字安全和人工智能双重能力的企业，360不仅较早开始关注大模型安全风险，同时打造了首个实现实战应用的安全智能体——360安全智能体。**基于“以模制模”理念，360以安全智能体为核心构建大模型安全解决方案，涵盖智鉴、智盾、智搜、智控等多款产品**，利用AI来检测和防范大模型可能出现的安全风险，全流程守护AI落地应用的全生命周期安全可控。既解决了传统网络安全问题，又为攻克AI安全新挑战提供了可行性方案。

随着人工智能发展进入“下半场”，智能体成为推动产业变革的核心力量。站在技术与产业融合的关键节点，唯有以创新思维重塑安全体系，将“以模制模”理念融入智能体发展全生命周期，才能真正保障智能体安全运行，推动其发挥核心作用，加速产业在智能化浪潮中行稳致远。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mAXRT8pP)

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