---
title: 2023年十大开源安全和运营风险
url: https://www.4hou.com/posts/GKP0
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-03
fetch_date: 2025-10-04T11:30:25.171250
---

# 2023年十大开源安全和运营风险

2023年十大开源安全和运营风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 2023年十大开源安全和运营风险

小二郎
[趋势](https://www.4hou.com/category/observation)
2023-04-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161013

收藏

导语：开源软件的“金矿”还需合理“开采”！

近日，促进开源软件安全和维护的软件公司Endor Labs发布了一份报告，揭示了许多软件公司依赖于开源代码，但在如何衡量和处理与开源代码软件相关的风险和漏洞方面却缺乏一致性。同时，该报告还确定了2023年开源软件的十大安全和运营风险。

根据Endor Labs的说法，对开源软件的过度依赖已经涉及一些已知的漏洞，被捕获为常见漏洞和暴露（CVE）；这些漏洞经常被忽视，如果不修复，可能会被攻击者利用。

Endor Labs的首席安全研究员Henrik Plate表示，“开源软件对应用程序开发者来说是一座‘金矿’，但它需要同样有效的安全能力。数据显示，一个新应用程序中超过80%的代码可能来自现有存储库，这种环境显然存在严重的风险。”

**2023年顶级开源风险**

**1. 已知的漏洞**

报告显示，开源组件版本可能包含由开发人员意外引入的易受攻击的代码。该漏洞可以在下游软件中被利用，可能会危及系统及其数据的机密性、完整性或可用性。

**2. 受损的合法包**

根据Endor的报告，攻击者可以针对现有项目或分发基础设施中的合法资源，将恶意代码注入组件。例如，他们可以劫持合法项目维护者的帐户或利用包存储库中的漏洞。这种类型的攻击可能是危险的，因为恶意代码可以作为合法包的一部分分发，并且很难检测到。

**3. 名称混淆攻击**

攻击者可以创建具有类似合法开源或系统组件名称的组件。Endor Labs的报告显示，这可以通过以下方式实现：

拼写错误（Typo-squatting）：攻击者创建的名称是原始组件名称的错误拼写；

品牌劫持（Brand-jacking）：攻击者滥用品牌或软件组件的知名度或声誉；

组合抢注（Combo-squatting）：攻击者利用不同语言或生态系统中的通用命名模式。

这些攻击都滥用了已知合作伙伴生态系统内的信任，并利用了品牌或软件组件的知名度或声誉，旨在将恶意代码向上游推送到与品牌相关联的受信任代码库，然后将其下游分发到最终目标：该品牌的合作伙伴、客户或用户等。

**4. 缺乏维护的软件**

根据Endor Labs的报告，未维护的软件属于运营问题。组件或组件的版本可能不再被积极开发，这意味着针对功能性和非功能性错误的补丁可能不会被原始开源项目及时提供或根本不提供。这可能使软件容易受到针对已知漏洞的攻击者的利用。

**5. 过时的软件**

为了方便起见，有些开发人员会在有更新版本时使用某个代码库的过时版本。这可能导致项目错过重要的错误修复和安全补丁，使其容易被攻击者利用。

**6. 无路径的依赖项**

项目开发人员可能没有意识到组件的依赖项，原因如下：

它不是上游组件的软件材料清单（SBOM）的一部分；

软件组成分析工具没有运行或没有检测到它；

依赖项不是使用包管理器建立的，这可能会导致安全问题，因为未跟踪依赖项中的漏洞可能不会被注意到。

**7. 许可证和监管风险**

组件或项目可能没有许可证，或可能有与预期用途不兼容的许可证，或其需求没有或不能满足的许可证。

按照许可条款使用组件是至关重要的。如果不这样做，例如使用没有许可证或不遵守其条款的组件，可能会导致版权或许可证侵权。在这种情况下，版权方有权采取法律行动。

此外，违反法律和监管要求可能会限制或阻碍针对特定行业或市场的能力。

**8. 不成熟的软件**

开源项目可能并非遵循开发最佳实践，例如使用标准版本控制方案，拥有回归测试套件，或拥有评审指南或文档。这可能导致开源组件不可靠或不安全地运行，使其容易被攻击者利用。

依赖于不成熟的组件或项目可能会带来重大的运营风险。例如，依赖于它的软件可能无法正常运行，从而导致运行时可靠性问题。

**9. 未经批准的更改（可变的）**

当使用在不同时间下载且不能保证相同的组件时，会存在重大的安全风险。Codecov Bash Uploader等攻击就证明了这一点，在这种攻击中，下载的脚本直接通过管道传输到Bash，而无需事先验证其完整性。可变组件的使用也会对软件构建的稳定性和可重复性造成威胁。

**10. 过度/不足的依赖性**

Endor报告指出，对组件的过度依赖或不足依赖可能也是一种运营风险。例如，较小的组件，例如那些只包含几行代码的组件，与较大的组件一样容易遭受相同的风险。这些风险包括帐户接管、恶意拉取请求以及持续集成和持续开发管道漏洞。

另一方面，大型组件可能积累了许多标准用例不需要的特性。这些特性增加了组件的攻击面，并可能引入未使用的依赖项，导致组件膨胀。

**风险缓解建议**

以下是Endor Labs关于软件开发人员和IT管理者如何降低这些开源风险的建议。

**1. 定期扫描代码以发现受损包**

防止合法包被破坏是一个复杂的问题，因为没有万能的解决方案。为了解决这个问题，组织可以参考新兴的标准和框架，如OpenSSF安全供应链消费框架（S2C2F）。组织可以根据自己特定的安全需求和风险承受能力，选择最适合自己需求的安全措施并确定优先级。

**2. 检查项目是否遵循开发最佳实践**

为了评估一个项目的质量，有必要检查它的文档和发布说明的完整性和及时性。寻找指示测试覆盖率或可以检测回归的CI/CD管道存在的标识。

此外，组织可以通过检查活跃维护者和贡献者的数量、发布新版本的频率、以及打开和关闭的问题和拉取请求的数量来评估项目。查找关于项目维护或支持策略的信息也是至关重要的——例如，长期支持版本的存在和日期。

**3. 保持依赖项处于最新状态**

为了确保代码的安全性，检查代码和项目的特征是很重要的。要检查的代码特征示例包括安装前和安装后hook和编码的有效负载。对于项目特征，要考虑源代码存储库、维护者帐户、发布频率和下游用户的数量。

保持依赖项更新的一种方法是使用带有更新建议的工具来生成合并或拉取请求。同样重要的是，要优先考虑依赖项更新和重复的待办事项。

**4. 评估和比较软件组成分析工具**

安全团队应该确保软件组成分析（SCA）工具能够在粗粒度级别（如借助Maven或npm等包管理工具声明的依赖关系）和细粒度级别（如不使用包管理器而包含“带外”的单个文件等工件）上生成准确的材料清单。

**5. 使用符合开源许可条款的组件**

IT领导者应该确保他们的软件开发人员避免在没有许可证的情况下使用开源组件，因为这可能会带来法律风险。为了确保遵从性并避免潜在的法律问题，为软件开发中使用的组件确定可接受的许可是很重要的。

需要考虑的因素包括组件的链接方式、部署模型和预期的分发方案。一旦确定了可接受的许可证，就要遵守这些开源许可证中规定的要求。

本文翻译自：https://www.techrepublic.com/article/top-open-source-security-risks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Nnfv9E07)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
* [![]()

  随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
* [![]()

  关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)
* [![]()

  2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

![](https://img.4hou.com/wp-content/uploads/2017/06/9381c342641778c32b6b.jpeg)

# [小二郎](https://www.4hou.com/member/enxl)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
  2025-09-30 12:00:00
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
  2025-09-02 12:00:00
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
  2025-06-06 16:28:40
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
  2025-05-09 12:00:00

[查看更多](https://www.4hou.com/member/enxl)

# 相关热文

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)

  胡金鱼
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)

  胡金鱼
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)

  梆梆安全
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)

  胡金鱼
* [关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)

  胡金鱼
* [2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

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