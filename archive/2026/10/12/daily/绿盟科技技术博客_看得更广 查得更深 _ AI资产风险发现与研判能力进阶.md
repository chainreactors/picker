---
title: 看得更广 查得更深 | AI资产风险发现与研判能力进阶
url: https://blog.nsfocus.net/%e7%9c%8b%e5%be%97%e6%9b%b4%e5%b9%bf-%e6%9f%a5%e5%be%97%e6%9b%b4%e6%b7%b1-ai%e8%b5%84%e4%ba%a7%e9%a3%8e%e9%99%a9%e5%8f%91%e7%8e%b0%e4%b8%8e%e7%a0%94%e5%88%a4%e8%83%bd%e5%8a%9b%e8%bf%9b%e9%98%b6/
source: 绿盟科技技术博客
date: 2026-10-12
fetch_date: 2026-10-13T08:37:54.359667
---

# 看得更广 查得更深 | AI资产风险发现与研判能力进阶

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* 看得更广 查得更深 | AI资产风险发现与研判能力进阶

# 看得更广 查得更深 | AI资产风险发现与研判能力进阶

[0](https://blog.nsfocus.net/%E7%9C%8B%E5%BE%97%E6%9B%B4%E5%B9%BF-%E6%9F%A5%E5%BE%97%E6%9B%B4%E6%B7%B1-ai%E8%B5%84%E4%BA%A7%E9%A3%8E%E9%99%A9%E5%8F%91%E7%8E%B0%E4%B8%8E%E7%A0%94%E5%88%A4%E8%83%BD%E5%8A%9B%E8%BF%9B%E9%98%B6/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-1216:33") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/封面-呢.jpg)

阅读： 16

### 01 AI资产风险发现：从资产识别到风险研判

随着 AI 应用在生产环境中的广泛部署，其安全风险逐渐呈现出资产识别困难、漏洞影响难以判定、依赖风险复杂以及风险状态动态变化等特征。 一个暴露在公网或部署在企业内部的 AI 服务，可能缺少准确的产品和版本信息；公开披露的 CVE 未必影响当前资产；项目自身没有漏洞，也可能因为依赖组件引入新的风险。同时，产品版本、组件依赖和外部安全事件都在持续变化，单次扫描越来越难完整反映一个 AI 资产的实际风险。

因此，在 AI 应用落地之后，安全人员往往需要进一步回答下面这些问题：

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/58f9db18104b4eada83fa42421a477b1~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=Os7Jusy5OqIaLajkxb7P5BORZII%3D)

这些问题共同构成了我们对 AI资产风险发现 的理解：它不只是一次漏洞扫描，而是围绕资产识别、风险关联、影响研判和持续监测建立一套完整的分析过程。

围绕这一目标，我们目前主要建设了以下几类能力：

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/c54c022b85dc4fdcafc45078d1cd831d~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=HI3%2Bfn3lcQRVm3cG4qgtQVlrx54%3D)

在这些能力之上，我们重点关注两个方向：**覆盖范围能否持续扩大，以及风险分析能否持续深入。**

**看得更广：让资产识别持续扩展**

依托绿盟风云卫安全大模型，我们持续拓展 AI 指纹识别的产品类型与覆盖范围，通过综合分析 Title、Footer 等显式特征，以及 JS 变量、CSS 类名、资源路径等隐式特征，提升指纹的识别准确性与泛化能力，增强对二次开发、页面修改及伪装场景的适应能力。

通过持续运营，指纹库可以随着新产品和新特征不断扩展。截至 2026 年 9 月，平台已沉淀 4K+ 通用指纹和 150+ AI 应用专项指纹。

**查得更深：把静态漏洞信息转成具体资产风险**

在完成资产识别之后，分析不会停留在 CVE 列表。我们进一步结合 POC、应用漏洞、供应链关系、漏洞可达性和威胁情报，对风险进行逐层补充和验证，整体链路包含：

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/d0d19e11aebd4b59843f5e0b31df8fa4~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=pNp7sMVTY69yOxdStPrXK2MvD8Q%3D)

也就是说，风险分析会从产品本身逐步延伸到依赖组件、真实影响范围以及外部安全动态，最终回到具体资产和版本上。

后文将重点介绍两项代表性技术——**智能资产识别**与**供应链风险溯源**，并在最后展示这些能力如何汇聚到**AI资产多维风险研判**中。

### 02 智能资产识别

**资产识别是风险分析的入口，识别范围与准确性直接影响后续的漏洞关联和风险研判。** 传统识别方式各有局限：人工提取成本较高，开源指纹规则覆盖有限，而单纯依赖 LLM 则难以保证识别结果的稳定性与准确性。

针对这些问题，我们引入绿盟风云卫安全大模型，对页面特征进行细粒度提取与分析，识别效果达到与主流网络空间测绘平台相当的水平。

**不止看表面：显式与隐式特征一起识别**

在指纹生成过程中，我们借助绿盟风云卫安全大模型的特征分析能力，不仅关注页面中直观可见的信息，还深入挖掘隐藏在页面结构与代码中的识别线索。除了 Title、Footer、Copyright 等显式信息外，还会进一步关注 JS 变量、CSS 类名、相对路径等隐式特征。相比只依赖明显页面元素，这种方式能够保留更多具有区分度的细节，对二次开发、页面修改和一定程度的伪装场景更友好。下表列举了部分常见的指纹特征。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/8728bd5a9e1243cf864377252df97e6c~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=nDf5lXniBMW4GIBwaBrX1TOFoT0%3D)

**指纹好不好，用真实资产说话**

指纹质量最终需要通过实际识别效果来衡量。为此，我们建立了量化评估体系，通过对比不同识别方式下的资产特征分布，综合评估指纹的识别准确性与覆盖能力，并引入 F1 指标进行统一衡量。具体计算公式如下：

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/7de86c879d104b66ba397dcae2308ebe~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=jPzWRBlyiCVbbLOU9vO2oer5598%3D)

其中，f 表示用于对比的特征标签，t\_f 和 o\_f 分别表示两组识别结果中对应标签的资产数量。通过比较各标签及其资产数量分布，计算综合匹配得分，从而量化评估生成指纹与参考结果的一致程度。

在实际资产识别场景中，生成指纹展现出良好的识别表现。部分指纹及效果对比如下。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/22ea449d903748a5a5cd4655d7366279~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=cSg3X5MUOI2Md0KkVruHk7nru1w%3D)

**指纹是如何运营的？**

为此，我们搭建了一套自动化指纹运营平台，实现从资产特征分析、指纹生成的完整闭环。

以下图中的 drawDB 为例，平台基于绿盟风云卫安全大模型生成候选指纹，并通过量化指标评估其识别效果。红框部分展示了指纹 **“drawDB | Online database diagram editor and SQL generator”** 的验证结果：准确率达到 **100%**，召回率达到 **93.3%**，F1 值达到 **0.96**，展现出较高的识别精度与覆盖能力，为大规模指纹生成和持续运营提供有力支撑。

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/1c0a2a73e0484de6b6eba19b0b932cad~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=7yfNiho57IePS1t9y8eHG2xjG7c%3D)

依托这套运营平台，我们在三个月内累计沉淀了 4K+ 条指纹。下一步，我们将重点研究无监督场景下的指纹质量评价方法，希望对不同来源、不同生成方式的指纹建立更统一的有效性评价标准。

### 03 供应链风险溯源

**传统开源组件平台已经能查组件、版本和漏洞，为什么 AI 项目的供应链还需要单独研究？**

一个重要背景是，AI 项目迭代速度快、版本分支多、依赖复杂，而且正在被越来越多企业以不同版本、不同部署形态广泛使用。对于企业侧的大规模资产管理来说，不可能对每个项目、每个版本都逐一开展源码审计，也很难依靠人工把项目依赖逐项映射到开源组件平台中完成风险核对。

因此，更现实的需求是：**自动识别项目依赖、理解版本关系，并将具体项目版本持续关联到组件、漏洞和风险传播路径中。** 这也是我们开展供应链风险溯源技术的出发点。

**首先，我们使用的开源组件数据底座本身就不是简单的组件集合。** 相比 OSI、libraries 等以组件收录和基础关联查询为主的平台，我们采用知识图谱组织组件、版本、依赖和漏洞之间的关系，更关注复杂的上下游依赖链路。下图展示了绿盟开源组件供应链知识图谱。以 PyPI 生态中的 tensorflow-gpu 2.7.4 为例，可以沿图谱继续追踪其上下游组件、关联漏洞及风险传播路径，从而为后续的风险溯源、影响范围分析和传播面管理提供基础。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/e121348fc9254800a8b99ff693271968~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=e0ZOqBxyRSbzjfgV%2Bxw%2B23Mh2m0%3D)

**有了开源组件知识图谱，下一步的问题是：怎样把一个具体的 AI 项目真正接进来？**

为此，我们进一步解析 AI 应用自身的组件依赖，并将这些依赖关系接入现有的千万级开源组件知识图谱。整个过程被封装成一套自动化流水线：**① 拉取项目仓库中的依赖声明文件；② 解析项目、组件与版本之间的依赖关系，并转换为图数据；③ 将依赖组件关联到千万级开源组件知识图谱；④ 最终汇入 AI 资产风险子图谱。**

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/2f4663c5ee924dc68244fb8ecf6d5480~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=jTeYMtVU%2FcxOumpMJ4Jz1%2Bshzgc%3D)

**不止供应链：把应用自身漏洞也纳入图谱**

除了供应链漏洞，应用自身漏洞也需要纳入图谱。问题在于，漏洞公告给出的是“0.3.14 及以下”“fixed in 0.3.15”这类自然语言版本范围，而代码仓库提供的是实际 Tags 列表，两者往往无法直接对齐，甚至边界版本并不存在于 Tags 中。

为此，我们引入步骤**⑤：结合漏洞公告中的版本描述与仓库 Tags，确定实际受影响的版本区间**，例如 [“v0.0.1”, “v0.3.14”]，从而实现漏洞与产品版本的准确关联。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/7234c74c774c4b0fa4d2814b251285f1~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=%2Bu5Pm6sjvdGuZj4snr%2FA9YtE6LA%3D)

**不止漏洞：把威胁情报也接进来**

我们还在步骤⑥中加入了 NTI （绿盟威胁情报），除了漏洞本身，用户可以进一步查看AI 应用相关的安全事件、热点新闻等信息，对产品风险补充背景理解。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/dcf935ad964447ab9c8e5583a67af8bc~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=DJWKDq67pBjpwdekfBgtAdIiFVc%3D)

报告对威胁情报的新闻、事件等内容进行展示

**发现了吗？项目和组件可能是同一个产品**

步骤⑦解决的是**同一产品以不同形态发布时的重复识别问题。**例如 OpenClaw 既有源码仓库，也以 NPM 包形式发布，如果两者分别进入图谱，就容易被当成两个独立对象。为此，我们引入 Derive 关系，将项目仓库中的 Git Tag 与对应的组件版本进行映射，把“项目”和“组件”重新关联到同一个产品及版本体系中。

**九个步骤很复杂？平台替你持续跑**

前面的九个步骤涉及依赖解析、版本映射、漏洞关联、情报融合和图谱更新，如果依靠人工处理，运营成本较高。为此，我们将整套流程统一封装到运营平台中，由平台持续跟踪项目变化并自动完成更新。目前已覆盖 **MaxKB、XInference、FastGPT、Ollama 等 94 个 AI开源项目，累计持续运营 18,557 个版本。**

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/520b7ef30f744169b3836e5382cd9b1c~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=buDSJW6bbEZ9jQnxP4lsd2QPWBE%3D)

**风险报告：供应链风险**

下面展示 AI 资产风险发现报告中的**供应链风险模块**，该模块将前述供应链图谱能力落到具体资产和版本上，集中呈现应用漏洞、供应链漏洞及其关联关系。以 OpenClaw v2026.3.28.beta.1 为例，该版本共关联 35 个应用漏洞。这里的“应用漏洞”是指项目自身在该版本上直接受影响的 CVE，在图谱中通过 Repo → Project → CVE 的关系路径进行展示。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/399163c2d2b340aebaa0bd126cbb0434~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261012163056E8BC8956AB336A5AC0FD&x-expires=2147483647&x-signature=p%2BULd8heAYUucjb8345UFEzKjgM%3D)

另一部分是**供应链漏洞**。同样以 OpenClaw v2026.3.28.beta.1 为例，该版本共关联 13 个供应链漏洞，这些风险并非来自项目自身，而是由其依赖组件传递而来，在图谱中通过 Repo → Project → Component → CVE 的路径进行展示。

![](https://p11-sign.toutiaoimg.co...