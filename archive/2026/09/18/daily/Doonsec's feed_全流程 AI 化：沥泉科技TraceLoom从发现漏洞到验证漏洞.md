---
title: 全流程 AI 化：沥泉科技TraceLoom从发现漏洞到验证漏洞
url: https://mp.weixin.qq.com/s/RpB5-hwLT-0-q7ClbQ-x5w
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:51:22.590281
---

# 全流程 AI 化：沥泉科技TraceLoom从发现漏洞到验证漏洞

# 全流程 AI 化：沥泉科技TraceLoom从发现漏洞到验证漏洞

原创

LICHOIN
LICHOIN

沥泉科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icibV4cctvpjUico27zyktFOic0ZB6oAxibBmDZ8a6FK9VO201OyYkLtVpQWlzZPQauOTLT0RgdTk0RlhNZ5SO0UMhOKsfSwPvsnsNtQDAmVVdZk/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjVgC1pmEpp6RBtrwjicNa8tgZcZTcsoUT0NWVZVg6EgiaJE0CqEusjpFHbDn7I6ic5yicRsnvUwnpJgZQAD9qyxbYCHsNR20gojibXs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/icibV4cctvpjUVk2Im7t3GkA2lR9s57Y1eC5xGhhEMz8DyM7etQHr420GV3sRBGo8eVsvXov79VUY1eQWaicIqC23zic7eSicaUQYVwlHUcXrFeQ/640?wx_fmt=gif&from=appmsg)

软件安全审计长期存在两个瓶颈：**代码读不完，结论信不过**。

*一个中大型项目动辄几十万行代码，人工审计往往只能抽样；而工具发现的问题，也需要进一步判断真假。*

*对于安全团队而言，真正花费时间的部分，恰恰是从“发现漏洞”到“验证漏洞”的过程。*

***沥泉科技自研 AI 白盒安全审计产品 TraceLoom，希望解决的正是这段距离。***

区别于传统单点扫描工具，**TraceLoom是一套全链路AI Agent智能审计引擎**。全程依托国产大模型DeepSeek驱动，实现供应链自主可控，解决传统审计的核心短板。

它将“**读懂代码 → 找到问题 → 排除误报 → 真实环境验证 → 输出报告**”这条链路整体 AI 化，由 AI Agent 执行从漏洞发现到验证交付的完整流程。

![](https://mmbiz.qpic.cn/mmbiz_gif/icibV4cctvpjWjia12ok4cXOcNXF2uYOHzBUuKHpM7gLibBuFfbUuvAok1EU87UV55bdQhG0AvNIJfQlrXATOibnLUm7Cx70PwSEnn3OTj65nYoI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjVGnibKuT12ic4EWEIfxczaPI7SlpicmxA16Eu9DkKSmKIzOZgVdDzdpJeJYxCyTTibibNFEmOaR86mcy10zT3UF1YdUzYblfM7Of6U/640?wx_fmt=png&from=appmsg)

*【**图一｜TraceLoom 能力全景**】从白盒审计到真实环境验证，再到报告交付，TraceLoom 形成完整的 AI 安全验证闭环。*

TraceLoom 的核心是一支分工明确的 AI Agent 团队。它们像一支审计小组一样协同工作，通过并行探索和分工复核，扩大审计覆盖面，减少人工反复查证的工作。

**1.全域测绘，摸清系统全貌**

项目接入后，TraceLoom 通过多个 AI Agent 并行探索，快速梳理软件的技术栈、功能入口、权限边界、数据流转路径，生成完整的系统安全地图，杜绝审计盲区。

**2.双线追查，锁定潜在漏洞**

一方面追踪数据全流转路径，排查外部输入可触发的安全风险；另一方面从全局视角预判高风险区域、主动求证风险假设，双线汇总形成完整候选漏洞清单。

**3.红蓝对抗，极致剔除误报**

针对每一个高危风险，AI自动拆分红蓝双方对抗核验：红方论证漏洞可被利用，蓝方举证现有防护可拦截风险。经过AI辩论复核、层层筛选，彻底过滤无效误报，确保每一条风险结论真实可信。

**4.实景复现，固化风险证据**

AI可自动搭建真实的软件运行环境，模拟黑客攻击行为，完整复现漏洞攻击路径，用真实场景验证风险危害性，进一步判断漏洞是否真实成立。

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjX8HvC9nHuzGou7Mictic9WNZ4QpTuSTtI0ruVibbnKawMSjytYtrFx1KoJMWTkfpPvNGDQ5qzkD2zo6C7oXtkjXyhP3iaMzlTPnBQ/640?wx_fmt=png&from=appmsg)

【***图二｜TraceLoom 完整工作流程***】*候选漏洞经逐条核查后进入真实环境复现，验证结论回流至扫描环节。*

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjWFSYiaicRO7ggD6iaJIgOzVVaaoTj7ic3Opu4gu58zgGbfdz9PwEiaH621eznxClBJ4yZnLbEgnnuAicEcW4EYv75nWHjmECSj0640Y/640?wx_fmt=png&from=appmsg)

**真实落地案例：AI 如何完成一次漏洞发现与验证**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjWibhsY1BPfzicp6lad41A2kfD346Gycuic3gib2yn7K2YdicL7AEmadbq3MibLQspYXPSzJnFAalVUEHNCN5xB371ribf5BhKcWACMBU/640?wx_fmt=png&from=appmsg)

系统能力是否真正有效，最终还需要通过真实任务进行验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icibV4cctvpjXmHiasZyZlowk4Xcz9ZW45bcD0veDicfKHYtsL57ajksc0uuQiahpoZj69CECAUzlDrOxMDxgGuq3hC3wr5N3lyiaf8vBg6WZ7EYE/640?wx_fmt=gif&from=appmsg)

**案例一**

**uWSGI 数据库配置插件远程命令执行漏洞（CVSS 9.8）**

“

本案例来自主流 Python 应用服务器 **uWSG**I，其广泛用于互联网、政企、 SaaS 平台的线上业务。TraceLoom AI 完整复盘从代码分析、漏洞溯源、误报排查、版本考古到实景复现的全流程，证实该组件存在**长期潜伏、全网通用的远程高危命令执行漏洞**。

**业务背景：广泛应用的核心组件存重大隐患**

uWSGI是全球通用的Web应用服务器，绝大多数Python架构的网站、系统均依赖该组件运行，普及率极高。

它自带一套「总管（Emperor）」管理模式：由一个总管理进程，统一调度、监控成百上千个业务子服务，实现批量管理。为了方便集中维护所有业务的配置，官方开发了数据库插件，总管会定时读取 MongoDB 数据库里的配置记录，数据库里新增一条配置，总管就自动拉起一个对应的业务实例。

这个插件支持两种数据库连接格式：**mongodb:// 和 mongodb2://**，两种写法的底层能力存在差异，也是本次漏洞产生的关键伏笔。

**AI全程自主挖掘，还原完整风险链路**

TraceLoom AI在无人工辅助的情况下，完整拆解出漏洞风险逻辑：攻击者只需向企业配置数据库写入一条恶意记录，即可顺着系统正常运行流程，最终在服务器上执行任意恶意命令，**最高可获取系统root最高权限，完全接管企业所有业务实例**。

**数据库里的一条配置记录（Source），经过“启动子实例”的内部入口，被当作配置文件解析，最终变成服务器上的一条命令（Sink）。**

这套用来自动化管理业务的机制，因为代码校验逻辑缺失，让数据库变成了攻击者下发指令、接管服务器的入口。

**AI精准定位出漏洞的四大核心成因，层层拆解风险根源：**

**1**

**认证机制结构性缺失**

mongodb:// 协议解析逻辑中，代码完全没有读取账号、密码、数据库名的入口，认证分支永久无法触发。而同插件的 mongodb2:// 完整支持账号密码认证，证明这是**代码实现缺陷，而非设计如此**。

**2**

**配置内容零安全校验**

系统仅校验实例名后缀格式，**完全不检测配置内容风险**。数据库内的恶意配置可原样送入业务启动流程。

**3**

**权限管控失效**

降权模式仅禁止 0 号权限，攻击者可自定义任意非零运行身份；默认环境下子实例直接继承总管权限，普遍为 root 最高权限。

**4**

**合法功能可被恶意滥用**

uWSGI 原生支持 attach-daemon 配置项，可启动外部守护命令。AI 证实：恶意配置可通过该功能，最终调用 /bin/sh -c 执行任意系统命令。

四层缺陷叠加，最终形成稳定攻击链路，

每一步都有代码依据的完整数据链。

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjW9AR9EkmKagic9BCG7A1MCWNCkh9IfiaI81BLDEKmibPlJG74MOkURmPxAZxHibAKxoia4iaxBD4sdgb89qJ12YECxQYF0aYoP2cL2A/640?wx_fmt=png&from=appmsg)

*【**图2-1｜*****案例机制与证据示意**】*依据本文案例描述绘制，展示配置触发执行的过程，以及随机标识、权限回显和实例启停行为之间的证据关联。图中画面为示意，非原始验证截图。*

**AI多重核验，排除所有伪风险**

针对代码中看似存在的安全防护机制，AI逐一穿透核查，最终确认所有防护均为“无效摆设”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjUxj2FMEGkb0ArqoqEUFV5pbZwAV0IcLjMKFS2yKWaicAodcNdaCh9njJbibX551IugHEjhotiaYAn3Cp2z8cbhuuAe7dfxG1XMEQ/640?wx_fmt=png&from=appmsg)

还有一个很有说服力的细节：同一个插件里的另一种写法（mongodb2://）具备完整的账号密码配置能力。这说明产品的设计意图本就包含“数据源侧认证”，前一种写法属于实现层面的缺陷。按国际通用弱点分类标准（CWE），该问题同时命中“关键功能缺少认证”与“代码注入”两类缺陷。

“

同时AI通过版本溯源，完成“版本考古”，确认该漏洞**从2012年组件诞生之初就已存****在**，覆盖1.3至2.0.31所有发行版本。

**实景复现，坐实高危危害**

在白盒审计确认漏洞链路成立后，TraceLoom 自动进入验证环节。AI Agent 使用 Docker 搭建一套真实运行环境：基于官方源码构建 2.0.31 版本的应用服务器和插件，编译配套旧版数据库驱动，启动未开启认证的数据库服务。

环境就绪后，AI 模拟攻击者，通过数据库协议向配置表写入一条带随机标识的记录，观察服务器反应：

```
/* 写入配置表的记录（示例载荷，命令输出回传用于确认） */name:   pwn-547e4da075a7.ini        /* 受支持后缀即可通过门禁 */config:[uwsgi]  attach-daemon = id > /evidence/proof.txt 2>&1
```

* 总管进程的日志出现“新实例已被拉起”，以及“以 root 身份拉起守护进程”的记录；
* 记录里的命令被真实执行，回显显示当前身份是 root，即系统最高权限；
* 换成反弹 shell 载荷后，取得一个可交互的 root 权限远程命令行，能够直接控制目标；
* 删除这条记录后，总管主动停掉了对应实例——危害的另一半，即随意启停、接管所有实例，同样成立。

这条随机标识可以把 “写入的配置记录” 和服务器执行结果一一绑定，排除巧合与模拟测试带来的误判。从搭建环境到完成攻击验证，全程由 AI 独立完成，无需人工介入复现工作。

**最终交付成果**

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjWt7Av9Hl2QNLUY4VfUUK3ibpiaDOYn6yRqzfpGeibEIWDFvwUtfEUibHEyTUshibic7D6PuMDap3mh8SjfhmAZuQemCmPmRVMGMNes8/640?wx_fmt=png&from=appmsg)

该漏洞为全网通用高危漏洞，可导致服务器权限完全失守、全站业务被接管。TraceLoom 输出含影响版本、攻击前置条件、危害边界、完整代码链路、实景验证证据、**可直接落地的修复与监控方案的标准化报告**，技术团队可直接对照整改，快速闭环安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjV8eJkg40C7RYjWDlBsIibtgaPehLNdEu22LHppnQNZ9qejOTX7X5eTxppa3ibuuDelhRk7LH7NwszeGXJd355lrPTJpdAxBEib5U/640?wx_fmt=png&from=appmsg)

**案例二**

**从一条上游提交反推出的 Redis 集群总线双重高危漏洞（CVSS 10.0/9.8）**

“

TraceLoom 对主流开源组件保持逐提交级的持续追踪。8 月 28 日，系统在 Redis 官方仓库捕捉到一条不起眼的配置类提交：维护者将“明文集群总线”从默认允许调整为默认拒绝。改动本身只有几行，AI 随即对它展开反向推导——官方为什么要动这个默认值？答案指向一个被默认配置掩盖的真实风险面。顺着这条线索，TraceLoom 对集群总线协议做了全链路深挖，推出两条相互独立、均可稳定利用的高危攻击链，并搭建生产级环境完成实景验证。

**通俗理解漏洞原理：集群“对讲通道”无身份核验**

把 Redis 集群想象成一**栋楼里的一群管家**。

楼栋管家依靠一条**内部对讲频道（官方叫“集群总线”）**完成多节点的数据分片、状态同步与节点互联，但是这条核心协议通道存在两个致命底层缺陷：

**01.谁都能插话**

频道不查证件。只要连通集群总线端口，外部设备即可参与集群通信，就能像楼里的管家一样讲话；

**02.说什么信什么**

话里自报的身份、数据归属和联系方式，对方照单全收，不去核实。

**简单来说：攻击者不需要任何账号密码，谁接上这条频道，谁就能冒充楼里的任何管家。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjWWbib0xfLGlLo25WostfiajguP5iaic6fA7fGc01dql8bYjWhHicacMvFduPDclKo9zXRqatc87qOoK7NHhIXA1KzPBza6pQezlclE/640?wx_fmt=png&from=appmsg)

***图 1-1｜Redis 集群总线漏洞的本质****。对讲频道不查证件、说什么信什么——不需要任何账号密码，谁接上这条频道，谁就能冒充楼里的任何管家。*

**反向推导出的两条高危攻击链（CVSS 10.0/9.8）**

TraceLoom AI 通过代码追踪与路径推演，完整挖出两条独立、可稳定利用的攻击链：

**路径1:**

抢走全部数据，顺手拿走密码（CVSS 10.0）

对着频道喊一句“我是新管家，我的电话是 X”——楼里的管家真按这个号码打了过来，打到我们这儿；

再喊一句“我是总管家，全部数据都归我”——对方把自己管的全部数据的归属划给了我们；

划完之后，它主动降级成我们的下属，并主动连回我们，把它自己保存的上一级数据库密码明文交了出来。

**路径2:**

骗一张内部通行证，直接当管理员（CVSS 9.8）

用楼里任何一个人的公开编号，喊一句“我是老员工”——这个编号在集群里是公开信息，随处可得；

对方回话时，自动附上了一张内部通行证（一串 40 位的内部口令）；

拿着这张通行证去大楼正门，直接换到一个不受任何权限限制的管理员身份：数据随便读、随便改、密码随便改。

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjWN60zn1TC1kibdMiaWdiaic3ias8XLzsjroU0XibtL0ApEOfNfPCT2fxHPtbZktiaXUsbumbiab03Ykl2qCVicvrHLhvE11icxnxUz9Via5Q/640?wx_fmt=png&from=appmsg)

***图 2-1｜两条利用路径****。第一条路径（CVSS 10.0）：抢走全部数据并拿到上一级数据库密码；第二条路径（CVSS 9.8）：骗取内部通行证、直接当管理员。全程不需要任何账号密码。*

**技术核心依据：报文关键字段全部可控**

本次漏洞的底层根源，AI 精准定位在集群总线报文结构。节点之间讲话用的报文，头部里的关键字段**全部由发送方自己填写**，没有任何签名或凭证绑定，而接收方收到之后，会**原样采信**。

**深度挖掘的起点：从一条提交反推协议风险**

这条提交就是本次发现的起点。8 月 28 日，TraceLoom 的上游提交监控捕捉到该 PR，AI 随即展开三步推导：第一，默认值调整说明官方确认“集群总线缺少来源认证”是必须消除的风险；第二，顺着总线协议逐段审计，定位到报文头部关键字段全部由发送方自报、无凭证绑定的信任缺陷；第三，由此推出两条完整攻击链。9 月 15 日该提交合入开发主干，同期 TraceLoom 已完成两条链路的实景验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icibV4cctvpjWyVZIxaBMdvLMN0jCKHVjVlQXxwFSpfnkIBFKGA6gGltTjgq2Sy6ich5oIicC9Ariac9AawryPWF5osVmekhKnmchkFHhxE1G5V8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icibV4cctvpjX9ttE5kTMJ9Hx38NZKB17TziccUYj7k6CoXW7qEbELe0cY2aCA6cXGEgl31JEJjiaJxlhqiagicwLDm4ZaoKSW9UrvRX...