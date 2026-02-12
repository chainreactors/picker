---
title: 快手：万人组织AI研发范式跃迁之路
url: https://mp.weixin.qq.com/s/I_VpBEktknviXi1kWvt8GA
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:06.398586
---

# 快手：万人组织AI研发范式跃迁之路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNgicopYh8SCtRY0GXMzFugAagQgnzibhwnBocb6VxoibUbs1JdfI2THYfj2w8GtQV96VE8AWVGS6FswUa8TnRRunI0GicpasPyTZdM/0?wx_fmt=jpeg)

# 快手：万人组织AI研发范式跃迁之路

快手技术
快手技术

快手技术

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

从2023年到2025年，快手在研发效能领域持续探索和积累，找到了借助AI平滑通往「研发智能化」的路径。一路走来，积累了大量的洞察和经验，本文系统性地做了深度总结。核心内容：

* 三阶段演进路径：

+ 平台化、数字化、精益化（2023-2024年）：

- 建设一站式研发平台，并标准化需求和工程流程，工具渗透率>95%，流程自动化>94%

- 通过建立效能模型，识别交付瓶颈，需求交付效率、人均需求吞吐量均大幅提升

+ 智能化1.0（2024年6月-2025年6月）：聚焦用AI提升个人开发效率

- 建设并推广AI编码/测试/CR等能力，AI代码生成率超过30%

- 但发现矛盾——个人主观编码效率提升显著，但组织需求交付效率却基本不变

+ 智能化2.0（2025年7月以后）：聚焦用AI提升组织整体效能

- 找到了AI研发范式升级路线：L1 AI 辅助（Copilot）→ L2 AI 协同（Agent）→ L3 AI 自主（Agentic）

- 探索出了支撑路线达成的系统性实践：AI x 效能实践、AI x 研发平台、AI x 效能度量

* 关键洞察与经验：

+ AI研发提效陷阱： 用AI开发工具 ≠ 个人提效 ≠ 组织提效

+ 本质问题：如何将个人提效传导到组织提效

+ 解决方案：研发范式升级，而非单纯推广AI工具

**AI研发提效陷阱：用AI开发工具 ≠ 个人提效 ≠ 组织提效**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

早在2024年，快手就建设了AI编程工具Kwaipilot，并发布给公司内10000+研发人员使用。经过持续的深度优化和推广，快手整体的AI代码生成率，在严格度量口径下（AI生成并入库的代码行/ 新增代码行）从 1% 达到了 30%+，甚至部分业务线达到了40%+。同时，在非编码环节，也衍生出了很多AI提效工具，比如智能CR（CodeReview）、智能测试用例生成、智能单元测试等等，但经过大量的调研和数据分析，我们发现了这个不等式：

“用AI开发工具 ≠ 个人提效 ≠ 组织提效”

如果以企业的研发效能提升为目标，我们发现：

* 对研发工程师而言：深度使用AI开发工具，代码生成率很高，个人主观体感上编码效率提升了20-40%，但并不代表真正的“个人提效”，因为在现实中，大部分工程师并没有接纳更多的需求，个人需求的交付数没有显著提升。
* 对大型组织而言：我们发现部分AI用的好的工程师，确实可以更快更多的完成开发任务，但组织整体的需求吞吐量没有明显提升，需求交付周期也没有明显缩短。

从《2025年DORA报告：人工智能辅助软件开发现状调查报告》中能看到，这也是业界普遍存在的问题。如报告中所述（如下图所示），在对AI提效的结果的预估上，各企业普遍对个人效能的提升有信心，而对团队效能的提升预估非常小。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XpNupYysyMkdMshf6DLuJexKsSQEfnoLsbyLWTBA6suiaXhDJfyKHux5982kOZbsWGQahE1zhEngXM6DDE5ZS1UYicoRAA8fOMI/640?wx_fmt=png&from=appmsg)

在快手，我们发现仅推广研发各阶段的AI提效工具，已经偏离了企业研发效能提升的核心目标，最终必然会导致2个问题：

* 投入很大，但企业整体的研发效率提升不明显：虽然通过调研很容易能收到大量的个人效率提升反馈，但个人提效无法传导到组织提效。

* 效能平台开始割裂：传统DevOps平台仍承担研发主流程，每天被高频的使用，却无法演进到下一代AI研发平台（顶多扩展一些单点的AI功能）。新生的AI编程工具，只取代了传统IDE，又无法与老平台协同演进。

为了解决上述2个问题，我们从2025年开始进行了更激进的探索和变革，我们称之为“AI研发范式升级”，最终，通过一系列的实践，找到了一条能借助AI能力平滑通往研发智能化的路径。

正逢2025年年末，我们把镜头拉远，将时间回溯到3年前，对快手研发效能的演进做一个系统性总结，有踩过的坑，也有做出的突破，希望为更多企业提供经验和参考。

**总览：快手研发效能演进路线**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1U6995DHKG8yGu1KBfFnqEJN22cUGdPpweZyx22L3u8zWZ5OC58znGjLjRTxeopIqrsZyeGiaAzbcUTYeX6cjp2PhibUdKDgkX7o/640?wx_fmt=png&from=appmsg)

如图所示：快手有10000+研发、8+业务线，研发效能的演进可以分为3个大阶段。

阶段1：平台化、数字化、精益化（2023-2024年）：通过建设三端一站式研发平台、需求流&工程流标准化，解决了研发交付流程散乱，既无标准也无数据的问题。再通过建立效能模型，识别交付瓶颈，提升需求交付效率。

阶段2：智能化1.0（2024年6月-2025年6月）：在研发全流程中开始建设AI能力，包括AI编码、AI单元测试、AI CR、AI手工用例生成、AI OnCall等等，并进行全员推广。经过1年多的实践，基本上完成了全员普及，在主观调研中，开发人员主观体感上效率提升20-40%，在客观数据上，AI代码生成率也在持续增长。但同时也发现了矛盾点：需求交付效率基本不变，即个人效率提升未能有效传导到组织效率提升。

阶段3：智能化2.0（2025年7月至今）：从“推广AI工具，让开发者使用”回归到了更本质的元问题：如何用AI提升需求端到端交付效率？经过半年多的探索，终于找到了新的路径，并得到了充分的数据验证。我们称这套解决方案为“AI研发范式”，主要解决了3个问题：

AI x 效能实践：如何用AI提升工程师的生产力，并将个人提效传导到组织提效。

AI x 研发平台：支撑需求交付全流程（从分析到编码再到发布）的研发工具链，如何整体演进到智能化？即下一代的智能研发平台，应该是什么样的？而不仅仅是只推广AI编程工具或在原有工具链上增加一些散点的AI提效功能。

AI x 效能度量：如何在效能度量指标的基础上，构建AI提效的指标体系，能清晰的量化过程和结果，为组织级的AI研发范式升级提供有效指引。

**阶段1：平台化、数字化、精益化（2023-2024年）**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25)

这个阶段的解决方案，业界相关的分享已经非常多了，但从实际情况看，在千人规模的技术团队中，能做好、做深、做透的实践非常稀有。

因此，我们直接分享1个具体的案例，以便能更好的看清快手的研发效能从基础建设到效能提升的全过程，这也是我们之所以能更快跃迁到AI研发范式的重要基石。案例来源是快手最核心的技术团队之一——主站技术部，是快手APP的研发团队，开发人员规模千人以上。

***背景：了解快手的研发效能基建***

首先，主站技术部的实践依托一套公司级的研发效能基建，由横向团队「研发效能中心」提供，如下图所示，这是在2023年快手当时的研效基建，主要分为：

* 效能平台：项目管理平台（Team）、三端一站式研发平台（KDev（服务端）、KFC（前端）、Keep（客户端））、琅琊阁（效能度量）、质量平台（KTest等）
* 效能实施：效能BP专家（Business Partner），负责深入各业务线，提供专业支持。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1V5x1fGDDaqlicQALYSTMP0fD2ZdSaaoF4HIUNCv2hr1phIZ5e9qjv8sdvnwO3yDKSkLRNqgNaSicQ3rnibsoKX79bXnxkZqPYvK0/640?wx_fmt=png&from=appmsg)

了解快手的研效基建后，下面开始重点介绍主站技术部的实践过程。

******Step1：依托工具推广，实现流程标准化******

***![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UibbQFWELjUlmtrAvrLh6NLIDAlkeaNJuk1ayHzgy2ZxDgJtB5MvlLKshjKxhEicef4d0KHjJPz0gvv1xgpMQu0Kjbr4YtPf87A/640?wx_fmt=png&from=appmsg)***

解决的问题

需求流和工程流均不标准，开发人员的工作分散在各处，日常开发体验差、学习成本高，又无法实施有效的质量防护措施，还不能沉淀准确的研发过程数据持续度量与改进。

达成的效果

通过推广三端一站式研发平台，定义需求、研发的标准流程，将研发全流程标准化。核心度量指标与结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XZiafkThOQcWNMf9ibQ8QuoEoPsgJ6acQzdFpLq6AiaMTJiaicicyFEzCWjt0DQtWQGEvkr3w679xib7PsRyuCpcLia0PjjyIuNjgum54/640?wx_fmt=png&from=appmsg)

***实践过程***

主要难点

* 用一套产品设计尽量满足多样化的研发场景：工具一边建设一边落地，且需兼容之前散乱各种不同的研发模式和习惯。

+ 服务端（KDev平台）：需要支持一些特殊的研发模式（比如Master模式、窗口模式）。

+ 客户端（Keep平台）：移动端研发场景多样化，包括APP、动态化、SDK。

+ 前端（KFC平台）：前端应用类型多（Web、Node、低码、KRN（动态化）、小程序），研发流程和习惯散乱。

+ 研发流程规范差异大：不同团队间，不同的技术栈的研发流程上存在一定差异，包括研发流程配置、流程各阶段信息字段、单点环节所需的工具能力不同等。

* 用户迁移成本大：迁移过程中，需持续关注和解决用户问题，包括用户体验变化、用户学习成本、用户情绪。
* 落地时间紧迫：一般互联网大厂类似的工作基本会持续6个月以上，快手主站只用了1个多月。

实施要点

1. 精准的解决方案设计：

* 服务端（KDev平台）：精准的打造了4套标准研发模式，适配了主站实际研发情况。
* 客户端（Keep平台）：一套平台底层能力，支撑3种移动研发场景；通过可配置与定制化能力，满足不同团队流程规范与管理诉求（自动翻转配置、流程与质量卡点配置、团队定制化模板）。
* 前端（KFC平台）：支持80%以上前端应用类型，并通过8个流程模板、适配5个内部自建的插件，兼顾了前端差异化研发流程和用户习惯。

2. 以用户满意为导向：提供完整的迁移配套服务，降低用户迁移成本。主要包括：

* 产品质量专项：用户BUG日结。
* 用户体验专项：持续深度用户访谈，识别体验问题，并优化。5周内，交付了73个功能&体验需求。
* 用户培训与激励：通过12次培训，50+线下访谈，7x24小时OnCall、200+人次的用户激励，提升用户对产品的接受度。

3. 数据驱动团队级推广：每周度量进度，驱动各部门接口人推广。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1WibzUY2XSltOyqj4NkolUKmC2oOoQXanxXclC87N7ns4tnZKIUtlsbNicCYRavyg2rlGoLb3u41VoibVTUgINEG5IPcK4PApQWyU/640?wx_fmt=png&from=appmsg)

经验总结

可能大家会有疑惑，为什么三端分别是3个平台，而不是一套平台。因为从实际情况看，服务端、前端、客户端的底层模式、流程都有比较大的差异，强行整合，不仅对产品用户收益不大，反而牺牲了要兼容不同端的流程、习惯差异化的灵活性，给标准化的推进增加难度。因此，我们在用户层面上，还是三套平台，分别解决各自领域的问题，但在底层的基础能力用的是一套，比如流水线、权限等。

***Step2：建设效能度量体系***

主站的研发效能早在2022年就开始启动了，当时在探索北极星指标阶段，缺少度量体系，更多是根据一线开发者的开发痛点反馈，进行偏工具流程等的优化，没有核心指标的牵引，项目都无法推进，更谈不上论证给业务带来的价值。在2023年3月再次重启效能项目时，北极星指标初步定义为 “有效需求吞吐量”，但是当时需求有效性的衡量难度太大，内部无法达成共识，项目推进困难，而且也无法看清业务堆积和开发人效情况。

随着流程标准化的落地，研发数据的置信度大幅提升，为效能度量提供了土壤。因此，我们定义了以“人均交付产品需求数” 为北极星目标来看清业务开发交付能力，同时观测需求颗粒度（避免单一指标跑偏：度量什么得到什么，种瓜得瓜种豆得豆）来保障交付提升的良性发展，逐步建立了一套更全面的指标体系（多指标互相佐证约束，hack成本极高）来体现业务交付产能和交付效率，以及组织和个人效率情况。

快手的效能度量体系如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UM2QgxYp9q2FatbMfCewREDjPUXCoiccmWdcEYFQXeNiaHHia9YjPbzf310BnvXk3HDkHFUvDSGYQEsS7AgicWV6HcWv5ricqGrjvI/640?wx_fmt=png&from=appmsg)

注明：SP：Story Point，快手用于度量需求工作量的单位。

借助这套全面完备的指标体系，我们不仅避免了依赖单一指标可能导致的偏差，还有效防范了效能数据被hack的风险，确保了效能数据的准确性和可靠性。

***Step3：效能问题分析与改进***

有效能度量体系，首先我们可以为任何一个业务线做系统性的体检，如下图所示，依托数据和经验，可以逐一拆解出核心的优化专项，并以效能项目的形式实施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UuibHbgMTWwUoc9bsQ7uuAVGZxogictVIBARy5BgFt7nVexV0ba9eLgbLqDz8XYUcePjy0rwQgu2v2XNBCE6v4QuujvCJmHDA5w/640?wx_fmt=png&from=appmsg)

其次，在研发流程和管理上，也能洞察出更多平时看不见的Case，深入改进，下面是2个具体的洞察与改进案例：

Case1:通过「研发活动在线化率」分析，深挖出架构不合理问题

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Xkic10eD2aNjG7xp4TVlBXYbjgWHtGvnK41oqcQocOxIlYEmib2DedvRHWHhbQIHHyMStsbl3LHhodcUem2bJmqDGSM8HqPda0Y/640?wx_fmt=png&from=appmsg)

上图是主站技术部下级各团队的研发活动在线化率，其中有一个团队出现了数据异常，分析之后可以发现存在不少问题：

* 横向来看，这个团队的研发活动在线化率处于中上水平，但产品需求投入占比只有59%，处于末尾水平。而且产品需求中体验优化占比11.44%，又是各团队中最高的。那么问题来了，“时间都去哪儿了？”
* 再下钻一层，这个团队的缺陷占比14%，也是各团队中最高的，且Oncall&排障占比6%也不低。

因此，数据表明，此团队可能存在的问题：在缺陷问题、体验问题、Oncall&排障消耗了团队大量的投入，以至于无法消化更多产品需求。所以，通过对团队核心成员的调研和访谈，基本可以找到根因：和客户端的架构劣化有关，比如：

* 反馈1：新需求开发时，上手门槛特别高，很多需求会涉及到多个模块开发，这会涉及到自己不熟悉的模块，因为架构分层结构不合理，模块耦合度太高，往往需要花大量的时间去熟悉其他模块的代码，最近做了一个新需求，评估是3天的工作量，2天都在看代码，实际的开发联调只有1天。
* 反馈2：模块边界不清晰，代码杂糅一起，新需求的代码，可能会影响到已有功能，导致旧功能的BUG，而且这些BUG在回测时，不容易被发现，导致问题漏测逃逸到线上。

通过效能的客观数据再结合主观调研，就可以看清“架构劣化”这种深层次问题，也可以对症下药了。解法是这个团队实施了2个技术专项：

1. 客户端的架构升级：从根本上解决因为架构问题带来的交付效率低和交付质量差的问题。

2. 体验优化：集中优化重点场景的体验问题。

随着这两个专项的落地上线，这个团队的效能数据已经有所改善，产品需求投入占比已经提升到64%，体验优化占比下降到6%。

Case2：...