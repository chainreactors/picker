---
title: 限免一周｜Memfit 全面升级：安全评估，流量分析与知识系统
url: https://mp.weixin.qq.com/s/gbDcWk3ernZOn0x9b5X52w
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:32.277838
---

# 限免一周｜Memfit 全面升级：安全评估，流量分析与知识系统

# 限免一周｜Memfit 全面升级：安全评估，流量分析与知识系统

Yak
Yak

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudBzo08KsWzzBtEzpIf5l8zyaU3uqV4GA4USxXeyfnPuQa0ibK1Kr9fibQ/640?wx_fmt=webp&from=appmsg)

基于我们之前的文章[《网络安全 Harness 的悲歌》](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247530485&idx=1&sn=5fe2257c15891a7286294d9ccf3080b2&scene=21#wechat_redirect)讲到的“流水不争先，争滔滔不绝”的无限游戏玩家理念。我们更希望我们的 Memfit AI 的产品是一个大家日常在很多场景和生产工作中使用的工具或平台，而不是放着“展览”的产品。

一般的安全类 AI Agent 在功能趋于稳定之后，会因为工具不可控，外部依赖众多，或者没有新的场景和生态导致生命力会迅速下降；这类“速生速死”并不是我们希望发生的。

一、一个有生命力的故事

在 Yak Project 的叙事中，我们希望我们自己是“**广泛使用的开源网络安全基础设施**”，我们在前AI时代，使用编程语言与编译器为核心路径，把基础的网络安全能力使用 Yaklang 与 YakVM 进行非常深度的融合，做一站式的安全方案。事实也证明，基于这套理念下，在用户们的帮助下，产品的研发效能和实际效果都取得了非常好效果。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HGm2S2lZbX7eF6bDO2icIsxPGg8dRDVgOSpRTFIicVHLKuQ9ZKETbcOmDQkWEsP7O4qwHxZfVfoVSxMMvBiczU3oEQ0PajicmKfRs/640?wx_fmt=png&from=appmsg)

但是AI时代之后，行业内做了大量的探索和实践，AI 用于攻击也好，AI 用于编码也好，或者AI用于防御手段。实际上我们赋予了 AI 大量的工具：发送数据包，扫描器，漏洞利用工具，协议分析器，并且沉迷于 AI 发挥这些老伙计的能力，但是本质上，原本的人类专家或者 SOP 专家也在发挥原本的这些工具的能力，原本由人调度的东西，由 docker 或者容器化调度的东西，变成了由 AI 调度。**我们短期内忽略了这些底层工具，但是他们在AI工作中却起到了非常重要的作用。**

就好比，curl 和 bash 如果出问题，那么市面上百分之九十九的 AI Agent 执行任务和命令都会有问题；某一个工具不够高效，那么整体就会多浪费一些 AI 的 Token 和步骤以及时间。

**“安全能力融合”的故事还在继续**：我们仍然可以通过提升工具的质量和特殊场景化的工具，来进行具体场景工作的效能优化；AI 完成专业的工作应该使用专业高效的工具，而不是 bash 或者 curl，wget 这类基础工具。

简单举个例子：我们提供了一个do\_http\_request.yak的工具，他可以提供比 curl 更少的依赖和更强的兼容性，甚至还包含批量发包的功能

| 对比项 | Bash + cURL | do\_http\_request.yak 工具 |
| --- | --- | --- |
| 命令注入风险 | 拼接不可信输入时，**可能引入 Shell 命令注入** | 结构化调用，不经过 Shell，规避这一层命令注入 |
| 原始数据包 | 主要通过 URL 和选项构造，完整报文需拆分转换 | **支持直接输入完整 HTTP 原始报文，控制重复参数、顺序及编码** |
| 批量发包 | 需AI额外编写脚本多次发包 | 模版展开、并发控制、**一次调用完成批量发送** |
| Payload 组合与编码 | 不支持，需 AI 现场复杂编程 | **AI 支持使用 Fuzztag**，支持复杂的组合，展开，配对与嵌套 |
| 快速结果分析 | 自己使用 sed awk grep 分析，不同系统不一样 | 内置常见状态码，长度，正则等筛选，并且可以自动汇总 |
| 流量接入与复核 | 需要使用中间人或者代理外挂存储流量 | 完全兼容Yakit流量系统与项目系统，支持重放和复核 |
| TLS 兼容性 | 额外配置不常见版本TLS，**默认无国密适配** | 支持自动**兼容低版本和老旧版本，国密TLS系统**，自动修复兼容错误 |
|  |  |  |
| --- | --- | --- |
| ⟷ 左右滑动查看完整表格⟷ 左右滑动查看完整表格 | | |

当然，这只是我们很多好用的 AI 工具的一小部分，我们经过大量的实际测试，这个do\_http\_request.yak在日常工作的表现非常好，**除了节约大量token之外，对一些老系统和内网系统的兼容也非常棒**，反观 cURL 很多时候就没有那么好运咯。
随着 Memfit AI 项目推进，我们完成了很多非常有意思的功能和场景适配，实现了非常多有趣的细节和实用功能，希望用户能继续给我们一些机会~

二、Memfit UI 全面优化

既然我们希望 Memfit AI 仍然是一个工具类型的产品，那认真做好人机交互其实是一个头等大事。毕竟，单纯想让一个 Agent 跑起来是一个非常简单的事情，但是想让别人承认在使用它，才是最难的地方。

大部分 AI Agent 其实都是一个对话框，这让人又爱又恨：我们应该**怎么传达给用户 Agent 是做什么领域的？**编码 Agent 和办公 Agent 很不一样，同样的安全领域 Agent 应该承担的工作也绝对不只是一个“对话框”能表达的。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FpicHYcM9OTH3zqgrRI2BfbP6pnmZNT29JQm3U9H7yCKoKDW4KyXLx30bFKWibrtjWFH11g27yUj3Voe2vLHByFehqesTiaDPwo8/640?wx_fmt=png&from=appmsg)

虽然我们做了一些其他的工作：侧边栏和右侧工具气泡增加了一定输入引导，虽然整体看起来清爽很多，但是想要在“专业度”和“简洁”中找到一个平衡，还是很有难度的。

三、任务执行过程优化

日常工作，尤其是中长程任务中，有一些非常让人纠结的地方：

1.跟随 AI Agent 的进程，需要在对话框中一步一步展示任务吗？

2.当任务进程非常长的时候，应该怎么去理解几百个 Step 中，到底做了那些事情？

我们曾经尝试抛弃对话式的“AI交互”，**减弱甚至取消“用户输入”的功能，得到了非常负面的反馈**：用户和客户普遍反馈无法干预执行过程，整体的“失控感”完全压制了“任务执行过程”。

随后我们又**极大强化了“纯对话”模式，马上又遭到了很多反噬**：“任务执行过程中发出去的流量我去哪儿看？”，“AI 说写了一个文件，如何快速查看这个文件？”，“我想勾选一些流量到 Agent 中执行应该如何操作？”

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EH3znzGYURDg7xeft0L4mkD8PWcvQ6LXN0GVbICb6Uibu7fD407sovaovftF7PJIoiapiaHLkHjUZqQnsxD9MLj0ckiaIhDN8v6Sg/640?wx_fmt=png&from=appmsg)

其实我们团队内通过各种试错后认真反思了一下，反而安全领域的 Agent 需要的拼图组件要远大于“编程”Agent，我们**需要文件系统，需要浏览器，需要流量表，需要异步任务，需要状态表，需要能记录漏洞的位置，需要能报告进度的位置。**

那么常见的 Agent 右侧工具状态气泡模式，我们就需要增加一些“安全领域”的专用子系统：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FbY8iaawo4948UmdHnJ2yk3l1RfcZdiaLvZlBib8oFYYEYbHrRqgRC6ytCUnhAfexNaKDg2sb7IC9EczHapRSOHeleB8baz1jgy8/640?wx_fmt=png&from=appmsg)

与此同时呢，在执行过程中其实，并不能完全不展示“任务详情”，一般任务为了保持一致性和同步信息，TODO List 这种最基础的机制是一定要的，但是如何知道这个 TODO 执行到什么进度了？什么时候执行的什么呢？

市面上主流的是使用“图”的方式来展示的，这是一种“伪智能”，实际上对模型来说，**图不图的其实并不重要，纯列表文本填进去，AI 的聪明程度也并不会减弱多少。**其实流程展示核心是为了方便人，为了让人更有掌控欲。

既然为人理解 AI 运行服务，那必然是我们应该采用人最能理解的概念“时间与排期”，那我们就使用**“甘特图”以时间轴为核心，来展示任务可视化**：把整体任务状态转化为符合人类直觉的时间与空间关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72EcNTEsURzk5wlLwGwxiaics2EpjrMtBkHicz8liclLulmBoxQawvc7viagr88Ft5p3qiantN0VkGkH9McJbuulnJzwT2EXUkILJlYoo/640?wx_fmt=png&from=appmsg)

实现的效果如下所示，我们可以很容易的看到这个任务执行的情况，哪些完成了，哪些跳过了，什么时间完成的，执行了大概多久

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HtdocnmF35xibTeDym8dkvOR7KwrhKQXEp0SjSrr0gH3qbczWtibD85tMjAwiaRjmfdJnj57eGzDic5fNv7wVpgyBic7fRR7FiadHME/640?wx_fmt=png&from=appmsg)

当然，我们仍然保留了重要的任务运行时，例如你可以随时观察 AI 系统发出了什么样的数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GAsNsqKedMJHVJNHNibDIeFa0icfZO0k4YOPfnctprkicv8GVEhd5ibhL14Hql0GwZ5jhJpd0v1dvDMAfNMxd0mOicCE85w7ScIiaPA/640?wx_fmt=png&from=appmsg)

在整个执行任务的过程中，人机交互其实完全不局限在“我和AI说句话”的Chat模式，人可以随时观察到AI Agent的系统行为，追加上下文，随时调整方向，也可以在不影响 AI 执行的时候，随时检查任务内容。

四、新功能：按时长持续执行

虽然我们这个功能已经推送有一段时间了，一直没有拿出来讲。但是实际生产使用中，产生了非常好的效果，收获了广大**用户客户的非常好评**。

**我们可以设置一个任务的运行时间。**

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72E958DNHH5KWC2oTS373dCEic34ITID3mYFFYibkou5BDzdeXTVj1go7iaxL78zpbaI7W9vhzibdVB53ZtFu1ZkgFBFQ4qt2ost3wg/640?wx_fmt=png&from=appmsg)

为什么我们要设置这样的一个**在别的地方无法见到目标模式呢**？

实际上在安全领域里面，探索性质的任务占了绝大多数，几乎所有的安全领域任务都不像“编码”一样，有一个明确的终结状态：

1.安全评估完成了一个漏洞就算评估完成了吗？那么目标应用是不是还有更多漏洞？

2.审计代码审计出了一个链路就算完成了吗？那么还有没有其他的链路？

3.流量分析分析出了一个可疑行为就可以写报告了吗？有没有关联其他问题？

说点更实际的内容，**漏洞是以“存在”为前提的，一个应用有漏洞才可能被攻破或者发现**，如果一个 Nginx 的纯静态页面，也没有任何 mod，那从正面攻破这个网站的机会微乎其微。就好比，没有人会指望攻破example.com吧？

但是 AI 其实并不擅长“纯探索”性的任务，**他总是以“阶段性发现”，“重大发现！”来想提前终结任务。**与此同时，我们发现绝大多数的用户，经常对 AI 说的话是：“继续”！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72EZwVfnM4wxajK6BMMM6fyO6iaic5pTtxFNdVhicko6jQjqkFjFhYjTtYdFicnx9r8EPSgMxP4h53fKxeWN5icV9WWPvSgPLOaxeMgE/640?wx_fmt=png&from=appmsg)

因此，我们实际在引导用户使用“设置一个3小时的不间断任务”，整体取得了非常棒的效果，其实很多时候大家对“continue”多次的结果表示满意，这就说明 AI 的能力其实完全可以达到，Agent 自然有义务帮助用户去把这个事儿做了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72EsnxscGptv9KNKFZBCBBicJkoNHJA4ZQNd9ibO49aaA96jP67YcibPPjrKjXnVEK9tNdSQK4916LAmDPUt1W5myYB4PCc3o9DBGg/640?wx_fmt=png&from=appmsg)

五、新工具：生态级联动

我们之前探讨了很多关于“架构”本身意义的事情，其实在 AI for Security 推进和发展的过程中，人的认知逐步在加深，会逐渐认识到一个事实：**“AI Agent 架构再怎么设计，不如多给 AI 提供几个数据源”。就好比：大家最希望 WorkBuddy 打通的一个数据源是谁呢？**

**微信！**

所以啊，与场景打通与生态打通才是要紧的事儿。

我们最近到底新增了多少 Agent 的新数据源和场景化的能力，不如就让 Memfit 自己来回答大家吧：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Hial2PXZFEGMFceSeuypTdWKTDvibXibPoknAw6MYdK9mgI6LFC8huSCWz3Stxq0Kiap8EwIRb5hXl6zf4K2PS7qIcTDOQe5myqkQ/640?wx_fmt=png&from=appmsg)

***YAK***

**5.1 生态入口：引擎数据层**

很多时候，在 Yakit 中寻找某一些流量，还是会花一段时间的，用户可能需要在自己的项目目录中跳转，搜索。但是实际上，我们近期版本提供的list\_yak\_projects以及query\_http\_packet\_history可以实现在 Memfit 中跨目录，跨项目地搜索任何之前发生过的流量。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HNMXVkLIFyVpH0kG2jVwtgXo6IouLickHp7Rx2TEY1vyf72ibBGE7QbVTQGeTkVTfQuGAMCeQD645G8VPaJUxrib623icu0w7qgM0/640?wx_fmt=png&from=appmsg)

***YAK***

**5.2 在 Agent 中管理知识库**

为了让用户长期和生产中使用 Memfit 的系统，维护好自己的专业数据，我们**实现了一个核心在本地运行的知识系统，这实际上对体验提升巨大**。我们之前在 “知识库” 的专用 TAB 中进行操作的内容，现在可以直接 Chat 让 Agent 直接调用核心 Yak 工具去维护数据库了。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HhqD6Bz8222Homd6Mo1WSIDB6VTXdIBVWmjNCJYny3sEEaVyicxAsFp51tdoH2ZEib5tFlUQQ3NyqIU0QBdicq5pvCGQdRT0lFQU/640?wx_fmt=png&from=appmsg)

实际上，在我们新的接口和新的工具系统中，我们甚至都不必学习“知识库”的UI到底是怎么使用的，**在这种能力体系下，直接交互其实是最简单且暴力的。**

接下来我们就直接展示知识库是如何管理的（同样，这也是几乎 Memfit AI 独有的系统）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72F40oPicMhA9R0YNg40icmW63fKyoxiauuuQXpaBfs0iav1piajx748JfsIXwHOKu0Sdd0yQQZPHU1oPn4TaSibuFm0bLR43ol9eG02I/640?wx_fmt=png&from=appmsg)

在建立好知识库之后，他就开始验证，我们可以看到如下验证过程：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FkicJqkxochej6jgria3JAmIyzjUILbFsaVArD8WjEVwpXWgILoWwUd3PicICh5VRAUjXJQfBcHwF03Avo4iaibxymG1cts4KhvlGQ/640?wx_fmt=png&from=appmsg)

***YAK***

**5.3 自进化RSI与记忆系统**

我相信，很多人在各种公众号上看到“自进化”与记忆系统的故事，这实际上我认为是非常有意义的事情。犯过的错误不再犯了，出过的洋相不再出了，这些才是**长期生产的保障。**

但是过分的强调 RSI 自进化与记忆系统，会陷入一个怪圈，如果记忆本身除了问题，那就会出现以讹传讹，众口铄金的不好现象。当然这是另一个话题了，我们后面再聊

虽然这股风潮还没有完全吹到“安全 Agent”中，但是**不妨碍我们去实现和完成 RSI 自进化的基础设施。**

我们设计了一些非常棒的接口来完成这个内容：

![](https://mmbiz....