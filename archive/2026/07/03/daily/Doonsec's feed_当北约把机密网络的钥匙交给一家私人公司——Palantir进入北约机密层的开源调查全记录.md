---
title: 当北约把机密网络的钥匙交给一家私人公司——Palantir进入北约机密层的开源调查全记录
url: https://mp.weixin.qq.com/s/gtNMWBnRP1vmPiUYJH7xVw
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:54.897825
---

# 当北约把机密网络的钥匙交给一家私人公司——Palantir进入北约机密层的开源调查全记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pBCQrIFuT7fav0wn1qiciaeGmkrLAWhgk0ogJqevyoCF4GKEIUciaJvjdy8zicMZOqpLoX8ibLrJZwAfmMzNDbTtcFpLOddee1sfYpwSTqBlb8w4/0?wx_fmt=jpeg)

# 当北约把机密网络的钥匙交给一家私人公司——Palantir进入北约机密层的开源调查全记录

原创

FF
FF

情报分析师Pro

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

北约安全认证委员会正式授权一家名叫Palantir的美国私营公司，让其开发的Maven智能系统（Maven Smart System，以下简称MSS）在北约机密网络上全面运行。

不是演习，不是试验，是完整作战能力。

对于不熟悉北约安全体系的人，小编先解释一下这意味着什么。

北约的网络安全分级和各国军队类似，分为公开、限制、机密等层级。能在机密网络上运行，意味着这个系统可以接触到盟国最敏感的情报数据、作战计划和指挥通讯。

这不是随便什么公司拿一纸合同就能做到的事，背后要通过极其繁琐的安全认证流程。

而现在，一家2003年由硅谷风险资本家彼得·蒂尔在CIA风险投资部门In-Q-Tel支持下创立的私人公司，拿到了这把钥匙。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7eInyCBxiaYyo8EBAKBYRNM4iccH7vBstEdS4sbt3LIIYwAQsdUJD1k8icNoqZhg0pEets7Rxl5OILRTSibxRtuic63ianeI4Tg0YibibE/640?wx_fmt=png&from=appmsg)

然后，北约各国领导人就要在7月7日到8日聚集土耳其安卡拉，举行年度峰会——人工智能采购和网络安全列为核心议题。 这两件事放在一起，时间节点太微妙，不可能是巧合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7d4RHxod4rmnmd0GibsLxA0OcGBkYs3U1xuiaFrpe38cNODawjJnZwwlwria7ibt6icWLdlVFJEIUuHF8nVkbfeBrer4AdKMygCbA50/640?wx_fmt=png&from=appmsg)

今天写这篇文章，不是来给Palantir站台的，也不是来喷它的。要做的，是像一个情报分析师应该做的——用开源情报的方法，把这件事从头剥开，让你看清楚里面到底有什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7c8EgkoAKfrFBmB5yfrt20sIchFcSyMKOMSf7oDd3s7qo2OtXMzraY9gYecRTbwHn4OExibAHmIqgLmBJLrQ9LlLXuCvhmKScJ8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

先说清楚：MSS到底是什么东西？

很多分析文章在描述Maven智能系统时，要么把它说得像科幻小说，要么避重就轻。

这里来直接说。

MSS的根源是美国国防部2017年4月启动的Project Maven，最初叫"算法战跨职能团队"。

最早的任务很具体：用机器学习处理无人机监控视频，帮分析师从海量视频中自动识别目标——车辆、建筑、武装人员。

Google最开始拿了这个项目，但2018年因为内部员工抗议退出了。Palantir在2024年以4.8亿美元的五年固定价格合同接手，后来合同上限追加到2029年为止的近13亿美元。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7cicpdIxrz3fXhVBiaHPzOcCiaUaxEpOwcLlStKSUjyQ1WBnyefYUVV4SkCTrrbwXZVshk6dKiaLbXlADicSDVOhX4snFVCsU4skBz4/640?wx_fmt=png&from=appmsg)

从无人机视频分析起家，现在的MSS已经进化成一个完全不同的东西——一套"活的战场同步视图"平台，能实时整合卫星影像、雷达数据、信号情报、各类传感器读数和情报报告，把它们统一整理成一个可搜索的数据库，然后配合大型语言模型生成目标清单、武器建议和行动方案。

用军队里一句话来说，Palantir的Task Force Maven主任、美国陆军上校阿内尔·大卫说得直白："我们正在数据里淹死，但我们饥渴的是智慧和战略洞察。"（原文："We're drowning with data, but we're starving for wisdom and strategic insight."）

然后他也说了，MSS现在支持的不是单一模型——它是模型无关的（LLM agnostic）平台，可以同时接入Anthropic的Claude、Meta的开源模型、法国的Mistral AI，以及任何通过安全认证的第三方模型。

这一点很关键，后面我们要回来讲。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

这套系统在真实战争里表现如何？

在把MSS推进北约机密网络之前，这套系统已经在真实战场上经过了最血腥的检验。

2026年2月28日凌晨1时15分，美以联合行动"史诗狂怒"（Operation Epic Fury）对伊朗发起了先发制人的打击。

数据显示：**在行动开始后的第一个24小时内，美军打击了超过1,000个目标**。 这是什么概念？2003年入侵伊拉克整个初始阶段出动量的两倍，在二十四小时内完成。

而后来五角大楼首席数字与人工智能官卡梅伦·斯坦利（Cameron Stanley）在2026年5月的SCSP AI+Expo大会上公开说：**"史诗狂怒行动中，MSS在38天内打击了13,000个目标。"**

同期，MSS的非机密使用量月同比激增38%，机密使用量激增89%，峰值单日令牌（token）使用量暴涨4,425%，有一天达到了大约200亿个令牌。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7fBTpH7uLOUvrZ24pp2cxatqOgcYRmTrsibhfGvuq1icChDJjJhCH9ljhkribTicUP9PqzSYjFtR2nXjUXPU0TnlqI4gSuLajC1VNg/640?wx_fmt=png&from=appmsg)

这是人类历史上迄今为止最密集的AI辅助军事行动。

当然，这个成绩单里也有一页让所有人都沉默的数字——在伊朗米纳布，一所女子小学遭到打击，根据伊朗方面报告有超过165名平民死亡，大多数是孩子。

五角大楼承认是"过时情报"导致的，正在调查是否出现在AI辅助生成的目标清单上。

这个悲剧不在今天文章的核心讨论范围，但它是必须放在这里的背景。因为正是这一切——战场上的成功，以及这些无法回避的问题——构成了欧洲盟国对MSS进入北约机密体系感到如此不安的原因。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

北约采购MSS的时间线，这次历史上最快的一次

这里做了一条时间线梳理，完全基于可核查的公开来源：

**2024年**：美国陆军与Palantir签署5年4.8亿美元MSS合同，后来增加到2029年约13亿美元上限。

**2024年9月至2025年3月**：北约NCIA完成从需求定义到合同授予的全部流程，只用了6个月——官方描述这是"北约历史上最快的采购程序之一"。

**2025年3月25日**：NCIA与Palantir正式签署MSS NATO合同。

**2025年4月**：北约Allied Command Operations（ACO）开始使用MSS。

**2025年8月**：北约军事人员开始正式使用MSS进行训练。

**2025年11月**：Task Force Maven工业日，来自法国、德国、芬兰、英国的多家企业整合进入MSS平台。

**2026年6月22日**：MSS NATO宣布达到完整技术作战能力。

**2026年6月26日**：NCIA代理首席运营官巴特·范·米尔特（Bart van Miert）致信北约SHAPE副参谋长确认达标。NATO安全认证委员会同日授予MSS完整安全认证，准许在机密网络上的演习、任务和一切活动中使用。

从需求到机密级全面运营，不到18个月。这在北约的传统采购时间表里简直是光速。

北约自己也拿"六个月完成采购"这件事当成功故事在讲，但这件事在情报圈引发的担忧，恰恰在于"太快了"。速度本身就是一个信号。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7cibibesxiaDKJjfia36pLj13VX7b0Q9cFKngcHBW5LrDCN9tekIG7jmMEQHGCuCs44oXtbtAgsYPqvoUsMDcgcvyS0xsib1venjLGs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

欧洲盟国的集体焦虑：他们在怕什么？

如果只看北约官方的新闻稿，这是个皆大欢喜的数字化转型成功案例。但只要打开欧洲的媒体，你会看到完全不同的画面。

**西班牙**

2026年7月1日，西班牙政府指示国家工业参股公司SEPI（Spain's State Society for Industrial Participations）旗下企业将Palantir列入黑名单，禁止签署新合同。

多家大型国有企业的董事会成员向《机密报》（El Confidencial）证实，他们收到了指令，任何可能"危及国家主权或战略信息"的Palantir合同均须回避。受影响的企业包括电信巨头Telefónica、国防科技集团Indra和军舰建造商Navantia。

讽刺的是，西班牙国防部与Palantir签订的2023年1,650万欧元情报融合合同仍在执行，到今年11月才到期。

**法国**

前总理塞巴斯蒂安·勒科尔努2026年6月10日宣布，法国将停止与Palantir合作。 但与此同时，法国军队自己在研发名为"Arcadia"的AI作战指挥系统，集成了Mistral AI、Safran.AI、Thales和空客的技术，并已在北约演习中测试。法国陆军副参谋长帕特里克·朱斯特尔（Patrick Justel）将军直接说："Arcadia是我们对Maven的回应。"

**德国**

德国网络防御负责人托马斯·达乌姆明确表示，德方不打算向Palantir授予合同。联邦国防军已将德国本土的Almato、Orcrist和法国ChapsVision列为三家备选方案，计划今年夏天测试。理由同样是数据主权：**"不能允许外国工业公司人员访问我们的国家数据库。"**

**荷兰**

荷兰国防国务秘书德克·博斯韦克（Derk Boswijk）在议会宣布，要在两年内建立"完全成熟的替代方案"，摆脱对Palantir的依赖。

**英国**

英国国防部在2025年12月30日签署了3年2.406亿英镑的Palantir企业协议——继续用，但议会委员会报告已经说这家公司形成了"不可接受的弱点"。

核心担忧是什么？用一个词来概括：**"断开开关"**。

欧洲国家担心的是，如果他们所有最敏感的军事指挥系统都运行在一家美国私营公司的平台上，那么理论上，华盛顿可以命令Palantir切断访问权限。无论这个概率有多低，它的存在本身就是一种战略脆弱性。

Palantir的回应是，其北约系统中"不存在此类机制"。然而，**"我们没有断开开关"这句话——永远无法被第三方独立核实**。

这就是问题所在。

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7c5ldurwhjJuyeZ5Q0VTgG9C6BeNic47dyelQgeOmq4cQDagc15eCHIXUv6ZOTiaJP1IrOjk9awicG9PbhkDAtx2dR6tZtGqzJUXU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

北约盟军转型司令的那句话

北约盟军转型最高司令、法国海军上将皮埃尔·万迪耶（Pierre Vandier）2026年5月接受《政客》（Politico）采访时说："据我所知，目前Palantir并没有真正意义上的竞争对手。"

他是法国人。他是最了解Arcadia项目的人之一。他是北约体系里最高的技术转型官员。他说的是"没有真正的竞争对手"。

然后他补充说，欧洲国家如果想要替代方案，需要"在数月或数年内，而非十年之后"拿出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7cyTNu89gcfpE0kbNrMlu86ssoEYE01JLsh6qschmibHtZv9UAgyd4mF79uickKGKOeEz8dU3clN2bBcCKF54s2bp6IzKIyajYVQ/640?wx_fmt=png&from=appmsg)

这句话同时是对欧洲现实的清醒判断，也是对Palantir的最高级别背书。

这就是所谓的"Palantir悖论"——你越抵制它，你就越面对一个残酷的现实：没有它，你的战场AI能力将是一片空白。而现代战场已经证明，AI处理速度的差距就是战场存活率的差距。

万迪耶将军其实还说了另一件很重要的事：欧洲的"数字主权"讨论把几个不同的问题混在一起了——对单一供应商的依赖、对非欧洲基础设施的依赖，以及对数据控制权的缺失。这三个问题的解法是完全不同的。

对他来说，当前最现实的目标不是完全技术自主，而是**控制数据**——确保欧洲国家拥有并控制经过处理的数据，包括附着其上的知识产权，以及决定与谁分享什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yvwyny73qKnOHokoj8fcalNmApGeV4e5o4y9CAiaB3nbc1h2AnXk1ZEiaGZtj0aic02EHbCAj2N2NEPnXpUpUNhmn3yHQh3gian9Mug9wibHMeek/640?from=appmsg)

如何用OSINT调查这类事件？

好，以上是背景和分析。下面换个模式，面对这样一个事件——一家私营公司获得北约机密级使用授权——一个合格的开源分析师应该怎么做调查。

这是这篇文章实操性最强的部分，下面会一步一步告诉你工具、步骤和逻辑。

第一层：锁定事实核心，找一手来源

任何分析的第一步，都是先找最原始的一手来源，而不是从媒体报道开始。

**具体操作：**

直接去NATO官方网站（https://www.nato.int）和NCIA官网（https://www.ncia.nato.int），用"Maven Smart System"作为搜索词，找所有官方新闻稿。

NCIA在2025年4月13日发布了合同签署公告，这是最权威的一手来源。同时检索Palantir的官方博客（https://blog.palantir.com）——他们在上面发布了关于MSS和北约合作的多篇技术文章，这些内容是公司自己说的，可以与官方声明交叉验证。

用Google高级搜索缩小范围：`site:nato.int "Maven Smart System"`、`site:ncia.nato.int "Palantir"`、`"Security Accreditation Board" "Maven"` ——逐层确认核心事实。

官方来源和公司官方来源永远是分析的锚点，但它们都有立场。它们告诉你的是"他们希望你知道什么"，不是全部真相。

第二层：挖采购合同，看真金白银

媒体报道可以有色彩，但合同数字很难撒谎。

**对于美国联邦合同：** 访问 https://www.usaspending.gov，搜索"Palantir Technologies"，按"Award Date"筛选2023年至2026年的合同记录，找与美国陆军合同指挥部相关的MSS合同条目，可以看到合同编号、金额、执行机构等细节。 同时在 https://sam.gov（整合了原FPDS功能）做交叉验证。

**对于英国合同：** 英国政府有"Find a Tender"系统（https://www.find-tender.service.gov.uk），我们搜索到的那份2025年12月30日签署、价值2.406亿英镑的MOD-Palantir企业协议，就是在这里找到的。这是100%可核查的公开记录。

**对于欧洲NATO合同：** NATO的采购相对不透明，但可以通过欧盟采购数据库TED（Tenders Electronic Daily，https://ted.europa.eu）搜索NCIA相关采购信息。此外，Politico Europe和DefenseNews通常会第一时间报道北约采购动向，是可靠的二手来源。

**关键提示**：永远要分清"合同总上限"和"已拨款金额"。Palantir...