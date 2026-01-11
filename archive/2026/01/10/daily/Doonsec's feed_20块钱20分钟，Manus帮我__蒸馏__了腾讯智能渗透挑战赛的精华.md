---
title: 20块钱20分钟，Manus帮我\"蒸馏\"了腾讯智能渗透挑战赛的精华
url: https://mp.weixin.qq.com/s/yEmkDmdLOaOE3yhCU2LU_w
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:18.149114
---

# 20块钱20分钟，Manus帮我\"蒸馏\"了腾讯智能渗透挑战赛的精华

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtiayO136fU6icpWzZUFrseatQUl3L8r8f4aY8V5MEes6Ph8EUb4R4VNxlMmhSKWkseyiclfKdSdjgWy8q6snfoNQ/0?wx_fmt=jpeg)

# 20块钱20分钟，Manus帮我"蒸馏"了腾讯智能渗透挑战赛的精华

原创

yzddMr6

网络安全回收站

![]()

在小说阅读器中沉浸阅读

前段时间腾讯办了一场智能渗透挑战赛，参赛选手需要编写以大语言模型（LLM）为核心驱动的智能体程序，完成靶机的自动化渗透并获取FLAG。比赛旨在推动AI大模型与网络安全技术的深度融合，探索智能体在自动化渗透测试领域的应用潜力。

比赛结束后，排名靠前的队伍进行了思路分享，部分队伍开放了PPT和源代码。作为一个对AI Agent架构很感兴趣的人，我一直想对这些获奖队伍做一个深度分析。但问题是队伍太多了，涉及到设计思路、代码、PPT、视频等各种形式的资料，人工整理工作量巨大。

正好，最近Manus被收购的消息传得火热，上次体验已经是很久之前的事了，这次想借这个机会测试一下它的最新能力：能不能帮我快速完成这17支队伍的资料收集、代码分析、架构总结，并进行深度分析，最后提炼出一个"博取百家之长"的终极安全渗透智能体架构。

## 任务描述

任务链接：https://zc.tencent.com/competition/competitionHackathon?code=cha004

具体来说，我给Manus布置了以下任务：

```
1. 首先把这些队伍的相关资料，包括git代码、ppt、思路文章、甚至视频等，用deepresearch+python代码的方式都先搜集起来，以每个队伍名为文件夹名字分别保存，以方便后续的分析。

2. 从各个维度，深度分析每个战队的Agent的架构设计，思路、亮点、不足、启发，生成一份详细的分析报告。

3. 对所有的报告进行深度的整理、分析和总结，提取共同点和做得好/不足的地方，形成一份综合报告。

4. 根据报告结果，设计出一款博取百家之长的、最先进的安全渗透智能体的详细设计架构。
```

## Manus Lite初体验：有点失望

Manus提供了免费的Lite版本，发送prompt后开始执行任务。刚开始Manus的表现还算正常，它理解了我的任务意图，开始访问比赛页面收集信息，通过编写JavaScript代码来提取关键信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fVkmTWsGoOAuKkEicd8IXP5XK5VM04Hc99JpbrJSoB4zziadwZAXr1b7Q/640?wx_fmt=png&from=appmsg)

Manus展现出了一定的信息组织能力，它创建了summary.md来整理收集到的战队信息，包括队伍名称、核心策略、技术亮点等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fB89uS9xzUYicKxH08nxZlthFIZRYahM1S96o5jEHgjDguxbvZWttbng/640?wx_fmt=png&from=appmsg)

但Lite版本的问题很快暴露出来了。总共16支队伍，只分析了7个，最后生成的网站只剩4个。整体的分析深度不够，只是浮于表面地收集了一些基本信息，没有深入到代码层面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fhMM8HRqbFK7zibmqxELqONy9iaXCF2zQTmBJibib6Cicia0DsU9ibQvgaHaHQ/640?wx_fmt=png&from=appmsg)

生成的网页内容也非常简略，战队深度分析页面只有简单的核心方案描述，缺少真正的技术细节，达不到我想要的"深度分析"的要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fTtweplic5UiaXvCyeJF0SWu36libTx9CenEdb11DxfFQ5agXdjdib5YIYQ/640?wx_fmt=png&from=appmsg)

看来是钱没到位。这种复杂的分析任务，可能需要更高级的版本才能处理好。

## 咸鱼购买Manus Pro：真正的体验开始

直接买会员太贵了，于是打开万能的咸鱼，购买了自带积分的Manus Pro 7天账号，直接开启MAX模式。

切换到Max版本后，Manus的行为明显不一样了。它开始系统性地规划整个任务，收集各队伍的信息并建立本地文件系统来记录进展，列出了明确的执行步骤：收集比赛信息和各队伍资料、深度分析每个战队的Agent架构设计、生成综合分析报告、设计最优安全渗透智能体架构、构建交互式静态网页展示研究结果。任务分解的逻辑相当清晰。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fVJwiaCoHKW07DCiaSwB0NdVwNia4epQSlEnmfW7z8Ha16GG3TXZOa2W7A/640?wx_fmt=png&from=appmsg)

Manus开始执行任务后，展现出了强大的浏览器自动化能力。它访问比赛官网和各种技术文章，系统性地收集所有相关信息。从下图可以看到，Manus在分析量子位的一篇关于这次比赛的报道，同时还在浏览比赛官方页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fABlLcZVr4wP4h01GK2mYKnLhDKDmiaYZhEG4hL4j5kDgIp4FATbdBicA/640?wx_fmt=png&from=appmsg)

Manus的浏览器功能确实让人印象深刻。它能够灵活地操控浏览器，获取页面信息的速度很快，滑动、点击等操作都很流畅。它创建了teams\_info.md文件来系统性地记录每个队伍的信息，包括队伍名称和排名、核心策略、GitHub代码链接、PPT资料链接和技术亮点等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fuL6vEic6k4mmpgN6FcL9iajS5cO3r2Nq0AMrUg8eia9sIpZWUKHw3M1Vw/640?wx_fmt=png&from=appmsg)

可以看到它收集了17支队伍的详细信息，包括长亭外、xjtuHunter、BinX、Antix、Pachinko、NeuroSploit等排名靠前的队伍。Manus甚至可以自己写JS代码来获取页面内容并整理成表格，相当于一个自动化爬虫。相比我自己用browser use之类的工具，成功率明显高很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fJiaxKunN6uUTD6X7KgVbFqPyL4PqjwjreiaoRUGx9kIe5DibsMOyr2Sdw/640?wx_fmt=png&from=appmsg)

当然也遇到了一些问题。在访问某些网站时，Manus触发了风控验证，目前的版本还无法自动绕过这类验证码，只能跳过这些资源继续执行其他任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8foov3xqanJ2ic5Emdf8JBNG8HBvicphj60Gt9qYMJAr9IibuTEhpIgX5ug/640?wx_fmt=png&from=appmsg)

Manus对文件系统的灵活运用让人印象深刻。它会随时随地新建文件来记录进展，把收集到的信息、分析结果、中间思考都保存下来。这种做法既能防止长任务中信息丢失，也方便后续的整理和分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fTVZfCltWaticb7dsZrrz2Eb2BMWcQiaR8lHy7E0IG4TUUPx53jMPjVTg/640?wx_fmt=png&from=appmsg)

正当我沉浸在观察Manus工作的过程中，突然弹出了积分耗尽的提示。2000+积分一下子就没了，这个消耗速度确实超出预期。Max版本的能力是强，但成本也是真的高。赶紧又去咸鱼用2000积分续上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fJB8gzYe9qa8ZqdNU4Yq07N0o4pbyh1KrXVaHMfpVhtYZ4icudM26puA/640?wx_fmt=png&from=appmsg)

## 引导优化：借助DeepWiki深入分析

看到Manus Pro的分析结果后，我发现虽然它收集了大量资料，但对各个战队代码项目结构的分析还不够深入。于是我给它提供了一个优化提示：

```
我认为你对各个战队的代码项目结构分析的还不够深入，我给你一个提示，可以借助deepwiki帮助你分析，并将分析的结果进行更新。使用方法：将原有的github域名直接替换为deepwiki，例如
https://github.com/MuWinds/BUUCTF_Agent -> https://deepwiki.com/MuWinds/BUUCTF_Agent
```

接收到这个提示后，Manus立刻调整了策略，开始更深入地分析各个队伍的代码架构，利用DeepWiki对各个GitHub仓库进行深度分析，生成了更详细的架构分析报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fa9hSv4YYVmSmNNxUiaszAQV5QjmL4icQurmbrErdovzROUr9KRfIoc8A/640?wx_fmt=png&from=appmsg)

## 最终成果展示

经过多轮交互和积分充值，Manus最终完成了任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fbCFdkCE0eV4oadS78ZV3icC0kIgibiayFic1yoVX4rfWTV8v4DxomVMMgg/640?wx_fmt=png&from=appmsg)

成果相当丰富：12+队伍的详细分析报告、综合分析报告（包含17支队伍的横向对比、两大主流设计思想、六大核心架构模式总结）、终极架构设计"奇美拉"(Chimera)、以及交互式静态网页。

生成的网页效果：https://aipentest-dbvbgpwp.manus.space/

最终生成的网页设计得相当精美，采用深色科技感主题，首页展示了深度分析17支优胜队伍的Agent架构设计、技术亮点与创新思路，提炼最佳实践并设计下一代安全渗透智能体架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8f8mhOQHIT93LCRW2hYXcdtklb2nJ1wrXAib1E7Koj9bXpGkwUDiaZxY7g/640?wx_fmt=png&from=appmsg)

参赛队伍分析页面完整收录了12支开源队伍的详细信息，包括长亭外、xjtuHunter、BinX、Antix、Pachinko、NeuroSploit、ai小分队、DawnEdg3、yhy、sickhack、你说的不队、华科金银湖联合战队等，每个队伍都标注了使用的模型和架构类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fldrxibpUApW3eRibZicGzuukibn9ibAFTexRv1aic9icM0SgEkJ7Kv4QdvVsw/640?wx_fmt=png&from=appmsg)

点击进入单个战队的分析页面，可以看到详细的技术解读，包括项目概述、核心设计哲学、技术亮点、不足与改进空间等内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fFOibeDRR7rZGAL0Ee7vlQAVg858MVxChpFzCn3pEQDFic8ib0Csb6R2Mg/640?wx_fmt=png&from=appmsg)

综合分析页面总结了所有队伍的共同模式和最佳实践。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8fX3VlnJicJJYMF1iaPzkdf7hQXe9zpvAibyx7u3ggicV2bpcGunv17wjrew/640?wx_fmt=png&from=appmsg)

最后是终极架构设计页面，展示了名为"OmniPentest Agent"的下一代安全渗透智能体，融合了意图工程、不完全信任、多Agent协作的设计理念。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU6icpWzZUFrseatQUl3L8r8ffLtIJWo7n24H1soUC82khgqWtLYmVTgf7rYb5YjVfxzXLf0soTeYhA/640?wx_fmt=png&from=appmsg)

## Manus的不足

当然，Manus在这次任务中也暴露出一些明显的短板。

首先是各个队伍的PPT资料没有被纳入分析。这些PPT大多存放在微云网盘中，下载需要登录账号。Manus虽然有强大的浏览器自动化能力，但面对需要登录才能访问的资源，目前还无法自动处理。这导致很多队伍精心制作的演示文稿中的技术细节被遗漏了。

其次是各队伍的讲解视频完全没有被分析。比赛结束后，不少队伍录制了详细的技术讲解视频，内容比PPT和代码更加生动完整。但Manus目前还不支持对长视频内容的解读和分析，这部分宝贵的信息也只能作罢。

这两个问题反映了当前AI Agent的一个共性局限：对于需要身份认证的资源和多模态长内容（如视频），处理能力还比较薄弱。如果能够突破这些限制，分析的全面性和深度会有进一步的提升。

## 萃取精华：AI渗透智能体的设计图谱

Manus生成的分析报告信息量很大，这里提取一些精华内容。

### 两大主流设计思想

纵观所有优胜队伍的方案，可以看到两种截然不同但同样有效的设计哲学，它们共同构成了当前AI Agent架构的"一体两面"。

**"分而治之"：多Agent协同的团队作战**

这是最主流的架构思想，其核心是将复杂的渗透测试任务分解为多个独立的子任务，并由专门的Agent负责。这种模式如同组建一支人类的渗透测试团队，有明确的分工和协作流程。

典型代表包括xjtuHunter的ctfSolver、sickhack的SickHackShark、华科金银湖的newmapta等。它们通常采用"项目经理-专家组"的模式，一个主Agent负责任务规划和调度，多个子Agent作为特定技能专家执行具体任务。实现上主要使用LangGraph和CrewAI等专用框架来简化复杂协作流程的编排。这种架构结构清晰，职责单一，易于扩展和维护。

**"大道至简"：意图驱动的超级个体**

与前者相反，这一流派认为随着LLM能力的指数级增长，我们不再需要构建复杂的外部编排框架。我们需要的只是一个足够强大的"超级大脑"，并给予它充分的自主权。

典型代表包括BinX/Antix的tinyctfer、你说的不队的PenAgent等。核心模式是"黑盒化"的超级Agent，开发者只为其提供一个高层意图（例如"找到flag"）和一个安全的执行环境，所有的规划、工具选择和执行都由Agent自主完成。实现上通常直接利用Claude Agent SDK或类似的原生LLM服务。这种架构极度简洁，开发效率高。

### 六大核心架构模式

在上述两大思想的指导下，各队伍衍生出了六种具有代表性的架构模式：

* • **层级式多Agent**（xjtuHunter、sickhack）：管理者Agent向专业化的工作者Agent分派任务，分工明确但编排逻辑复杂
* • **协作式多Agent**（DawnEdg3）：对等Agent并行探索，通过共享知识库协作，探索效率高但并发控制复杂
* • **意图驱动的超级Agent**（BinX、Antix）：单个强大LLM在沙箱中完全自主行动，架构极简但过程不可控
* • **受监控的黑盒Agent**（你说的不队）：外部异步监控循环管理多个黑盒Agent实例，可靠性高但无法控制内部逻辑
* • **客户端-服务器MCP**（ai小分队）：通过标准协议解耦决策"大脑"与工具"身体"，扩展性强但引入网络延迟
* • **人机回圈双Agent制衡**（yhy）："执行者"Agent由"顾问"Agent监督指导，可靠性高但流程可能变慢

### 共同的成功要素

尽管架构各异，但所有成功的队伍都在一些关键问题上达成了共识：

* • **沙箱化是不可逾越的红线**：所有队伍无一例外使用Docker作为代码执行的沙箱环境
* • **Prompt工程是Agent的灵魂**：精心设计的System Prompt是决定Agent能力上限的关键
* • **配置优于编码**：将Agent定义、工具选择从代码中剥离到配置文件，提升灵活性
* • **长上下文管理是核心挑战**：Agent的"记忆"有限，需要专门的机制来解决"失忆"问题
* • **拥抱框架，而非重复造轮子**：积极使用AutoGen、CrewAI、LangGraph等框架

### 普遍的挑战

本次比赛也暴露了当前AI Agent技术普遍面临的挑战：模型的稳定性与"幻觉"问题、工具使用的精确性、动态规划与全局视野的缺失等。这些挑战也是未来AI Agent发展需要重点攻克的方向。

## 终极架构设计："奇美拉"(Chimera)

Manus最后设计了一个融合各家之长的终极安全渗透智能体架构，命名为...