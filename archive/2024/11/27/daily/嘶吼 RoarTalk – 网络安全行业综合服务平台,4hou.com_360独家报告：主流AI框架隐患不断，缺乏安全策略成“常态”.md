---
title: 360独家报告：主流AI框架隐患不断，缺乏安全策略成“常态”
url: https://www.4hou.com/posts/1MQ0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-27
fetch_date: 2025-10-06T19:12:15.435544
---

# 360独家报告：主流AI框架隐患不断，缺乏安全策略成“常态”

360独家报告：主流AI框架隐患不断，缺乏安全策略成“常态” - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 360独家报告：主流AI框架隐患不断，缺乏安全策略成“常态”

企业资讯
[行业](https://www.4hou.com/category/industry)
2024-11-26 10:30:36

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43447

收藏

导语：漏洞百出！AI主流框架安全性引发业界担忧。

近日，360数字安全集团发布了一份关于大模型安全漏洞的报告，揭示了当前大模型及围绕其构建的框架和应用中存在的严重安全问题。报告显示，360近期研究发现了**近40个大模型相关的安全漏洞，其中既包括二进制内存安全、Web安全等经典漏洞类型，也包含由大模型自身特性引入的综合性问题**。影响范围覆盖多个知名模型服务框架及国际厂商开发的开源产品。**更为严重的是，在对目前流行的框架进行审计后，发现几乎所有的框架都缺乏有效的安全保护策略**。

报告指出，大模型在软件设施和具体应用场景落地中面临诸多安全挑战。这些挑战涵盖了模型层安全、框架层安全和应用层安全。在模型层，攻击者可以通过数据投毒、后门植入、对抗攻击等手段，使得模型无法正常完成推理预测，或绕过安全限制，生成不当内容。而在框架层，问题则更为复杂。目前的大模型项目需求不断增长，各类开源框架层出不穷，这些框架虽然提供了完整的开发周期功能，降低了构建AI应用的门槛，但同时也打开了新的攻击面。

**360对目前流行的框架进行审计后发现，几乎所有的框架都缺乏有效的安全保护策略**。由于框架底层主要使用非内存安全语言进行编程，如C/C++，因此在优化算法的代码实现过程中很可能引入内存安全问题。此外，框架在接受并处理不可信数据时，也缺乏足够的校验和过滤机制，使得攻击者可以通过构造恶意数据来触发漏洞。

例如，在TensorFlow、PyTorch等国内外流行框架中，就存在因内存破坏导致的进程崩溃等问题。这些问题通常可以通过调用特定的接口函数，并传入特殊构造的数据参数来触发。**然而，由于修复这些问题可能会严重影响训练效率，因此一些框架开发者并没有及时对这些问题进行修复**。

更为严重的是，在分布式场景下，框架的安全问题更加突出。由于分布式系统通常包含大量的计算资源和存储资源，一旦被恶意控制，将带来巨大的安全风险。可惜的是，目前几乎所有的框架都没有良好的安全策略来实现分布式场景下的安全防护。一些框架在通信过程中没有对接收的数据进行严格校验，使得攻击者可以通过发送恶意构造的数据包来触发漏洞，进而控制整个集群。

针对这些问题，**360建议框架开发者应加强对安全问题的重视，投入更多精力来解决因框架设计导致的安全敞口问题**。同时，用户在使用这些框架时也应保持警惕，采取必要的安全措施来保护自己的系统免受攻击。

此次发现再次提醒我们，以大模型为重要支撑的AI生态虽然拥有巨大的发展潜力，但同时也面临着复杂而繁多的风险因素。为了确保整个系统的可信、可靠、可控，我们需要将更多的精力投入在AI的安全之上，不断发现和解决潜在的安全问题，为构建更加安全、健康的AI数字环境贡献力量。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?LPPIzS2T)

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