---
title: 360发布全球首份《大模型安全漏洞报告》，曝光Intel等知名开源产品漏洞
url: https://www.4hou.com/posts/YZ0O
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-26
fetch_date: 2025-10-06T19:16:49.727025
---

# 360发布全球首份《大模型安全漏洞报告》，曝光Intel等知名开源产品漏洞

360发布全球首份《大模型安全漏洞报告》，曝光Intel等知名开源产品漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 360发布全球首份《大模型安全漏洞报告》，曝光Intel等知名开源产品漏洞

企业资讯
[行业](https://www.4hou.com/category/industry)
2024-11-25 17:07:20

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)53316

收藏

导语：近日，360数字安全集团发布全球首份《大模型安全漏洞报告》。

近年来，全球人工智能浪潮持续升温，大模型作为AI领域中的重要一环，其能力随着平台算力的提升、训练数据量的积累、深度学习算法的突破，得到了进一步提升。然而以大模型为核心涌现的大量技术应用背后，也带来诸多新的风险和挑战。

近日，360数字安全集团发布全球首份《大模型安全漏洞报告》（以下简称“报告”），从模型层安全、框架层安全以及应用层安全三大维度探查安全问题，并借助360安全大模型自动化的代码分析能力，对多个开源项目进行代码梳理和风险评估，最终审计并发现了近40个大模型相关安全漏洞，影响范围覆盖llama.cpp、Dify等知名模型服务框架，以及Intel等国际厂商开发的多款开源产品，全面呈现了全球大模型发展所面对的安全威胁态势，为构建更加安全、健康的AI数字环境贡献力量。

**生成及应用过程隐忧**

**模型层安全或影响训练及推理**

大模型的生成及应用过程通常包含了数据准备、数据清洗、模型训练、模型部署等关键步骤，攻击者可对该流程中相关环节施加影响，使模型无法正常完成推理预测；或者绕过模型安全限制或过滤器，操控模型执行未经授权的行为或生成不当内容，并最终导致服务不可用，甚至对开发者或其他正常用户产生直接安全损害。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241125/1732525409923178.png "1732525409923178.png")

报告指出，大模型的开放性和可扩展性使其在训练和推理过程中面临着**数据投毒、后门植入、对抗攻击、数据泄露**等诸多安全威胁。近年来，各大知名厂商的大语言模型因隐私泄露和输出涉及种族、政治立场、公共安全等不合规信息而引起社会广泛关注的案例屡见不鲜，为了加强模型本身的安全性，越来越多的研究人员开始从模型的可检测性、可验证性、可解释性进行积极探索。

**安全边界模糊**

**框架层安全使攻击面频繁增加**

随着大模型项目需求的不断增长，各类开源框架层出不穷。这些框架极大提升了开发效率，降低了构建AI应用的门槛，同时也打开了新的攻击面。

报告指出，这些框架在各个层级都可能因接触不可信的输入而产生潜在的安全风险。**比如利用非内存安全语言引发内存安全问题，或者通过影响正常业务流程向框架传递恶意数据进行攻击，以及利用物理或虚拟主机集群所暴露的服务接口进行恶意控制等**。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241125/1732525421906074.png "1732525421906074.png")

模型框架通常承载着极其丰厚的计算与存储资源，但又由于其模糊的安全边界，通常难以做到完全运行于隔离的环境之中，因此一旦受到攻击，就可能对整个系统带来不可估量的损失。

**模块协同存在风险**

**应用层安全可致目标系统失控**

AI应用是人工智能技术通过自动化决策和智能分析来解决实际问题的进一步落地，通常集成了前端采集用户输入，后端调用模型分析处理，最终执行用户请求并返回结果的业务流程。

报告发现，除了模型本身，AI应用是多项计算机技术的有机结合，通常还包含了许多其它工程代码实践来落地整套业务逻辑。这些代码涉及输入验证、模型驱动、后向处理等多个方面，而不同分工模块间的业务交互可能会引入额外的安全问题，既包含了传统的Web问题，又涵盖了大模型能力导致的新问题。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241125/1732525432183270.png "1732525432183270.png")

在以往的攻击中，攻击者常通过组合利用业务系统中具有不同“能力原语”的漏洞，进而实现对目标系统的完整控制。而在AI场景下，为了能使大模型能处理各项业务需求，通常会赋予其包括代码执行在内的多项能力，这在带来便捷的同时，也提供了更多攻击系统的可能性。攻击者可以尝试控制并组合AI的“能力原语”，在某些应用场景下达到更为严重的攻击效果。

伴随人工智能的加速发展，以大模型为重要支撑的AI生态拥有巨大的发展潜力，在赋予AI更多能力的同时，也应确保整个系统的可信、可靠、可控。报告认为，大模型所面对的安全威胁应从模型层、框架层、应用层三个层面持续深入探索：

**模型层**是大模型自身在训练和推理过程中，以能直接输入至模型的数据为主要攻击渠道，从而使得大模型背离设计初衷，失去其真实性和可靠性。

框架层则是用于大模型生产的各类开源工具带来的安全威胁，这类框架在掌握有大量数据、算力、存储资源的同时，却缺少基本的安全设计，其安全性很大程度依赖于框架使用者自身经验。

应用层则是集成大模型技术的应用程序，在受传统安全问题影响的同时，又可能在模型能力驱动层面上出现新的攻击场景。

作为国内唯一兼具数字安全和人工智能能力的公司，360数字安全集团基于“以模制模”、“用AI对抗AI”的理念，遵循“安全、向善、可信、可控”原则，打造安全大模型，保障大模型全方位服务的安全运行，防止不法分子利用相关漏洞对系统进行攻击，从而保护用户隐私和服务稳定性，持续助力政府、企业以及科研机构能够高效应对在大模型训练和应用过程中的多重挑战，推动国内大模型生态持续健康发展。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5XyQ5Rrt)

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