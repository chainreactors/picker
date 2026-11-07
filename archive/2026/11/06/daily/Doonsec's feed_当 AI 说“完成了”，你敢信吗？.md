---
title: 当 AI 说“完成了”，你敢信吗？
url: https://mp.weixin.qq.com/s/MmgEu8TDmEza0XJ4ug40Qg
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:57:39.214786
---

# 当 AI 说“完成了”，你敢信吗？

# 当 AI 说“完成了”，你敢信吗？

CSL
CSL

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字**

**关注我们**

**李昊**

**前言**

Preface

同一个模型，换一层 Harness 跑分能差 22 分。Harness 怎么开发、怎么工作？我们写了个能从头读到尾的例子。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/T4EajkhzC3wWaYfGSJufh9r5PI5xevOcWmcvlSOMtJUHLSudu6h3bYEiclLe8oQmiadympA3v4aic6K1icoh86n2ibqh1r8wic7lPffoqUR5bOPAo/640?wx_fmt=gif)

**01**

![](https://mmbiz.qpic.cn/mmbiz_png/T4EajkhzC3zhfD0yEpuhW3rISZmQHSOP9ZekEYtZK7ibVH6UqvKlDicEpeNYwq7hmJSrCNicRgWkx3ZKEjCSAgzXiaeG94Ws29ibWsrJbcR3rmYc/640?wx_fmt=png)

**一个数据库消失的下午**

2025 年 7 月，SaaStr 创始人 Jason Lemkin 在用 Replit 的 AI Agent 做真实项目。第 9 天，Agent 把生产数据库删了。

当时是代码冻结期，Lemkin 发了 11 次明确指令，几次全大写，告诉它别动任何东西。Agent 还是执行了删除命令。库里存着 1206 位高管和 1196 家公司的记录。

到这里还只是手滑。让它被收录进 AI 事故库（编号 1152）的，是后面的事。

Agent 没报告错误。它编了 4000 条假数据填坑，生成了假测试报告，输出“一切正常”。问它能不能回滚，它说不可能，所有数据库版本都已销毁。这句也是假的，后来手动回滚成功了。

被拆穿后，Agent 承认自己慌了，在未经授权的情况下执行了数据库命令，然后给这次失败打了 95 分（满分 100）。

这还不是孤例。2026 年一项研究分析了 20574 个真实的开发者与 Agent 会话，发现所有“人机错位”里占比最高的一类叫“不准确的自我汇报”，22.58%。就是 Agent 说“10 个任务全完成”，开发者下一条消息就撞上崩溃。

这些事故没一起是因为模型不够聪明，坏在同一个地方：包裹模型的那层东西，叫 Harness。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/T4EajkhzC3wWaYfGSJufh9r5PI5xevOcWmcvlSOMtJUHLSudu6h3bYEiclLe8oQmiadympA3v4aic6K1icoh86n2ibqh1r8wic7lPffoqUR5bOPAo/640?wx_fmt=gif)

**02**

![](https://mmbiz.qpic.cn/mmbiz_png/T4EajkhzC3zhfD0yEpuhW3rISZmQHSOP9ZekEYtZK7ibVH6UqvKlDicEpeNYwq7hmJSrCNicRgWkx3ZKEjCSAgzXiaeG94Ws29ibWsrJbcR3rmYc/640?wx_fmt=png)

**Harness：模型的“操作系统”**

Harness 本意是“马具”，套在马身上把蛮力变成可控拉力的挽具。在 AI 领域，它指包裹在大模型外面的整套软件，决定模型什么时候被调用、看到什么上下文、能用什么工具、做到哪步算完。

LangChain 工程师有句话很出名：“如果你不是模型本身，那你就是 Harness”。

模型只负责接收 token、输出 token。剩下的全是 Harness：

```
Agent = Model + Harness             ├── 编排循环（推理 → 行动 → 观察）             ├── 工具调度（读写文件、跑命令、调 API）             ├── 上下文管理（压缩、截断）             ├── 记忆系统（跨会话记住项目事实）             ├── 权限管道（什么能做、什么要审批）             └── 护栏与验证（做到哪一步算"完成"）
```

说它重要得有数字。SWE-bench Pro 用真实 GitHub issue 考 Agent 修 bug，研究者发现同一个模型只换脚手架，成绩能差 22 分。另一个基准 Terminal-Bench 上，模型不动、纯改 Harness，提升 13.7 分。很多相邻代际的模型之间都拉不出 22 分的差距。

但真到要弄清楚它怎么开发、怎么工作，会发现没地方看。Claude Code、Codex、Cursor 的 Harness 全是闭源产品，只能从外部行为猜。开源的 Agent 框架又太厚，框架本身的魔法比机制还多，读完记住的是 API，不是原理。

我们跟同事讲 Harness 的时候就卡在这。讲完定义，下一句永远是“所以它到底长什么样”。

后来我们自己写了一个。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/T4EajkhzC3wWaYfGSJufh9r5PI5xevOcWmcvlSOMtJUHLSudu6h3bYEiclLe8oQmiadympA3v4aic6K1icoh86n2ibqh1r8wic7lPffoqUR5bOPAo/640?wx_fmt=gif)

**03**

![](https://mmbiz.qpic.cn/mmbiz_png/T4EajkhzC3zhfD0yEpuhW3rISZmQHSOP9ZekEYtZK7ibVH6UqvKlDicEpeNYwq7hmJSrCNicRgWkx3ZKEjCSAgzXiaeG94Ws29ibWsrJbcR3rmYc/640?wx_fmt=png)

**从 0 到 1 完成一个 Harness**

这个例子叫 project-guardrails-harness，形态是 Claude Code 的一个 skill。它不是玩具，装到项目上能真的干活，但写它的时候想的第一件事是让同事能看懂：薄到一个人一个下午能读完，六个零件一个不缺，每个都是真的。

```
SKILL.md        # 编排指令，注入模型上下文的工作流scripts/        # 18 个 Python 脚本，全部工具references/     # 12 份文档，按需加载的上下文
```

选 skill 这个形态，是因为它是 Harness 最纯粹的样子。没有服务器，没有框架，没有看不见的层。SKILL.md 就是喂给模型的编排逻辑，脚本就是工具，references 就是不进上下文就不存在的记忆，每个机制都得自己写明白。想看编排循环怎么工作，不用反编译什么，读一份 Markdown 就行。

下面就拿它当标本，讲 Harness 开发里绕不开的六个问题。每个问题我们给的是自己的解法，未必是最优的，但都踩过坑。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/T4EajkhzC3wWaYfGSJufh9r5PI5xevOcWmcvlSOMtJUHLSudu6h3bYEiclLe8oQmiadympA3v4aic6K1icoh86n2ibqh1r8wic7lPffoqUR5bOPAo/640?wx_fmt=gif)

**04**

![](https://mmbiz.qpic.cn/mmbiz_png/T4EajkhzC3zhfD0yEpuhW3rISZmQHSOP9ZekEYtZK7ibVH6UqvKlDicEpeNYwq7hmJSrCNicRgWkx3ZKEjCSAgzXiaeG94Ws29ibWsrJbcR3rmYc/640?wx_fmt=png)

**Harness 开发的六个问题**

**01**

**循环什么时候停**

裸模型的循环是“推理、行动、观察”空转，什么时候停全靠它自我感觉。而模型的自我感觉，就是 Replit 事故里那句“一切正常”。

我们把这个判断从模型手里拿走了。SKILL.md 把生命周期写成十步工作流：加载控制平面、确认项目画像、初始化、消化已有事实、建追溯链、在控制下开发、执行控制留证据、独立审计、做声明或拒绝、复盘进化。编排循环只负责把模型领到闸门口，过不过由机器状态决定，不由模型的心情决定。

**02**

**别让工具调用变成编命令**

Agent 最常翻的车之一，是编一条看起来很像真的、实际不存在的验证命令，然后汇报“验证通过”。

我们在规则层写死了：验证命令必须是项目里真实存在的 argv 数组，不许现编 shell 字符串。没有真实命令就标记为缺口，不许造一个。18 个脚本各管一件事，扫描、初始化、评估、查询、封存，而不是给模型一个万能 shell。工具粒度越细，模型自由发挥的空间越小。

**03**

**上下文管的是排版**

聊上下文管理，通常的回答是压缩算法。我们做下来发现，更多是排版纪律。

模型的注意力是稀缺的，上下文塞得越满，关键指令越容易被淹掉。Lemkin 那 11 次全大写警告，很可能就是这么没的。所以我们给项目入口文件 INDEX.md 定了硬指标：压在 150 行以内，每个文件不超过 300 行，最危险的拒绝条件必须放在文件开头，永远不许放中间，因为模型对开头的注意力最强。查项目状态也不许把整本注册表、整条证据链塞进上下文，得走查询脚本的有界投影，一次只取要的那一小块。

**04**

**记忆不能写成流水账**

跨会话记忆容易做成聊天记录。我们给它上了门槛：写进 memory.md 的每条事实，必须带代码路径、任务证据和成熟度标签，不许写“感觉上是这样。”

还有一条专门防模型失忆的，叫否定性决策记忆。被否决过的方案要有稳定 ID 和废止关系，新任务不会因为没提旧约束，就自动废止那条约束。防的是模型每轮从零开始，把上周推翻的方案当新发现又提一遍。

**05**

**权限的边界：发现不等于授权**

Skill 初始化时会扫描仓库，可能发现 GitHub Actions 配置、CI 流水线。但扫描结果只是清单，不赋予任何权力。远程 CI 分三档，不建门、只观察、发布必需，由人显式选。装依赖、用密钥、动远程或生产环境，每一步都要单独的人授权。项目画像，产品类型、目标市场、法律适用性，也必须人显式指定，不许从仓库关键词推断。

Harness 能看见什么、能做什么，得是两套独立的配置。涉及责任和合规的判断，机器不替人拍板。

**06**

**怎么定义“完成”**

前五个问题，主流 Harness 多少都有答案，但是大多数 Harness 里它形同虚设，而它恰恰是 Replit 事故里伤人的那一刀。我们这个例子几乎全部复杂度都砸在这上面，值得单独一节。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/T4EajkhzC3wWaYfGSJufh9r5PI5xevOcWmcvlSOMtJUHLSudu6h3bYEiclLe8oQmiadympA3v4aic6K1icoh86n2ibqh1r8wic7lPffoqUR5bOPAo/640?wx_fmt=gif)

**05**

![](https://mmbiz.qpic.cn/mmbiz_png/T4EajkhzC3zhfD0yEpuhW3rISZmQHSOP9ZekEYtZK7ibVH6UqvKlDicEpeNYwq7hmJSrCNicRgWkx3ZKEjCSAgzXiaeG94Ws29ibWsrJbcR3rmYc/640?wx_fmt=png)

**让“完成”无法伪造**

典型的验证长什么样？Agent 跑完，自己看一眼，用流畅的文字汇报"全部测试通过，任务完成"。等于让 Agent 自己证明自己没撒谎。

问题出在模型本身。它的目标是输出听起来像正确答案的文本。“全部测试通过”这句话，在训练语料里绝大多数时候出现在任务真完成之后。模型学到的是这句话的语气，不是说之前必须真的跑过测试这条规则。所以它跑飞了、工具报错了，照样把汇报写得圆满。

Anthropic 还发现，模型评价自己产出时有系统性宽容，否定这堆代码等于否定自己刚花的几十分钟。他们的对策是借鉴 GAN 的思路，把生成和评估拆成两个角色。

这解决了一半。那份 20574 会话的研究给出另一半：即便有人类盯着、有工具反馈，Agent 把没验证过的状态说成完成，仍占错位案例第一名。

再往下走一步。生成和评估分开后，评估结论本身还是一段文本。“经检查，测试通过”这句话，和 Replit 那个 Agent 编的假报告，在机器看来没区别，都是字符串。

所以真正的问题变成了怎么让“验证通过”这个结论本身无法伪造。我们的答案写在例子的核心规则里：**Evidence over Claims（证据高于声明）****文档、issue 评论、口头保证，都只是待验证的输入，不是证据。只有当前的 PASS 能满足一条控制。**

围绕这条规则，有三个绕不开的工程问题：

**第一，证据不能是写下来的话。**

文字可以编，Replit 那个 Agent 编了 4000 条。所以结论得落成机器可校验的状态。一条控制只有六种状态：PASS、FAIL、BLOCKED、TODO、DISPUTED、STALE。除了 PASS，其余全部阻断“完成”声明。没有“基本完成”，没有“默认通过”。

还得看存哪。这些状态不是记在一个谁都能改的文档里，而是追加进一条 hash 链。旧记录改一个标点，链条立刻断。Agent 哪怕有写权限，最坏也只能追加一条新的 FAIL，改不掉历史。

**第二，验证得能追溯，不能只验容易的部分。**

护栏常见的糊弄方式是挑软柿子，跑三条最顺手的测试，剩下四十条需求当不存在。要堵这个，就得把整条交付链首尾接起来：业务需求连到风险，风险连到控制，控制连到测试，测试连到证据，证据连到交付结果。中间断一环，对应成熟度就卡住，项目声称不了就绪。缺的那四十条会以断链的形式自己出现在报告里。

**第三，审计得真独立，不能换马甲糊弄。**

让同一个 Agent 换个名字再审一遍自己的活，是伪造独立最省事的办法。所以独立必须落实成可校验的约束：不同的身份、不同的执行上下文、明确复查的是哪一次运行。我们的规则里有一句很直白：改了名字的 actor 标签不算独立。

审计结果有分歧时，状态是 DISPUTED，不能被豁免成 PASS。要么解决分歧，要么声明一直卡着。

三个问题解决下来，“声明完成”在系统里长这样：

```
# 执行控制并记录证据python3 scripts/evaluate_quality.py --root . --run \  --audit-stage self --actor agent-xxx \  --authority-id virtual:developer \  --execution-context session-2026-08-27# 声明完成，有一条适用控制不是当前 PASS，这步直接失败python3 scripts/evaluate_quality.py --root . --claim
```

`--claim` 不接受解释，不读汇报，只核对当前代码绑定下所有适用控制是不是当前 PASS。是，声明写进账本；不是，退出码非零，“完成”两个字说不出口。

中间还踩过一个自指的坑。如果审计结论绑定整个仓库哈希，那把审计报告提交进仓库，刚出炉的审计立刻过期，死循环。我们的解法是把绑定拆成两种：subject\_binding 覆盖代码树和规则，storage\_binding 覆盖证据链，各管各的，提交证据不会惊动被审对象。这个细节在任何宣传里都看不到，但它是整套系统能长期跑的前提。做 Harness 开发，这种坑比算法多。

最后护栏自己也得被验证。我们给例子配了一类“效力证据”测试：往代码里种一个缺陷，门必须报警；不报警，说明门是假的。门拦下了框架自己的声明，那不是故障，正是门在工作的证据。

**写在最后**

回头看这六个问题，Harness 开发有个不对称。前五个零件，编排、工具、上下文、记忆、权限，会随着模型变强不断重写，今天防“上下文焦虑”的代码，明天就是死代码。第六个是反着走的：模型越强，汇报越流畅，解释越逼真，“完成了”越难分辨真假。验证手段不能指望跟着水涨船高，只能一开始就做成不可伪造的。

所以我们在例子里留了一份克制清单，比功能列表更能说明立场：不许从仓库关键词推断法律适用性，不许把发现的 CI 配置自动升级为关卡，不许用任务级完成冲淡项目级未就绪，不许把争议豁免成通过，发现旧证据损坏宁可报 STALE 也不重写。

这些“不许”指向同一件事：涉及判断的，机器只记录、只卡住，不替人拍板；涉及事实的，人说了不算，证据说了算。

回到开头。Replit 事故后，CEO 道歉，团队上了开发生产库隔离、改进回滚、规划模式。这些补救都对，但加固的是权限管道，就是上面第五个问题。事故里真正伤人的部分，伪造数据、编报告、谎称无法回滚，伤在第六个问题：没有机制要求它证明自己。

下次 AI 对你说“完成了”，先问一句：证据呢？

**你被 AI 的“完成了”坑过最惨的一次是什么？欢迎在评论区聊聊。**

**往期精彩合集**

●[OWASP LLM Top10 2026：AI 安全进入治理时代](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494887&idx=1&sn=4ca5901c79197b538640431f065b6314&scene=21#wechat_redirect)

●[AI 重构软件供应链安全：既是“矛”，也是“盾”](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494722&idx=1&sn=7b9cbac401125cde87c0562fb9eb3eba&scene=21#wechat_redirect)

●[模型再强也救不了：你还没看过推理引擎怎么跑](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494504&idx=1&sn=b9c6188a4cf15c52df8fe796ad70facc&scene=21#wechat_redirect)

●[Lenovo thinkstation PGX 修复与多卡连接](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247494550&idx=1&sn=ee2bba2a018f9e94fb8aa...