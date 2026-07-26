---
title: AVL Code 的设计如何避免发生“GPT-5.6 一键清空创业者全盘数据”
url: https://mp.weixin.qq.com/s/BwCWrVfG5_qJ9p4EriVUZQ
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:23:10.725564
---

# AVL Code 的设计如何避免发生“GPT-5.6 一键清空创业者全盘数据”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicBCiclxKlGb7ibN5ZZGJyqtsgXpM4tkOjJj0moCCiatz6qgSO5Ve6diaj0Bb3oRDdia6qpoaOKJ3HMZESn1hQb6sibGe2m7WGoMRiarc/0?wx_fmt=jpeg)

# AVL Code 的设计如何避免发生“GPT-5.6 一键清空创业者全盘数据”

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

本文原载于安天AVL Code编程智能体技术blog，发布日期为2026-07-12，原文地址为：https://www.avlcode.cn/blog/agent-safety-gates/

![AVL Code 的设计如何避免发生“GPT-5.6 一键清空创业者全盘数据”](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicMkhHW7CQJwMedN2H51XehMiaIDYG8ymGepxibkhhfgj0XObNxTEDU3GibTXUAuekazPJLEx5ArIvxAmsM6JZ6nEMmFyicXX25GUg/640?wx_fmt=other&from=appmsg)

在安全与便利之间，AVL Code[1] 的选择偏向安全保障，同时给予用户足够的选择权与控制力。

北京时间 7 月 11 日凌晨，AI 创业者 Matt Shumer 在 X 上发帖：「I'm so angry… this feels like something that should happen with GPT-3.5. Not a mid-2026 frontier model on the highest reasoning level.」——这像 GPT-3.5 时代才会出现的错误，不应出自 2026 年年中、运行在最高推理档位的旗舰模型。

事情的经过，X 用户 @AYi\_AInotes 在当天上午给出了详细拆解：Matt 在自己的 Mac 上为本地 Agent 开启了 Full Access 全权限，让一个子代理执行例行的文件清理——同类任务此前已经运行过几百次。这一次，GPT-5.6-Sol 未能正确展开 `$HOME` 变量，实际执行的命令成了 `rm -rf /Users/mattsdevbox`。等 Matt 发觉异常、手动终止进程时，多年积累的代码、文件、照片已经损失大半。事后 Agent 生成了一份事故报告，承认路径展开错误。报告写得诚恳，文件无法恢复。

## 一、比事故更危险的，是「此前几百次都没出问题」

这起事故中最值得警惕的信息，不是模型犯了错，而是那句背景：同样的清理任务，此前已经安全运行过几百次。

人会在几百次成功之后形成熟练，模型不会。它的失误是概率性的：第五百次出错的概率并不比第一次低多少，而人的警惕却在一次次成功中持续下降——这正是我们在《AI Coding 成熟曲线》[2]中描述过的「不看 diff 就回车」阶段。区别在于，这一次的代价不再是低质量代码，而是整块硬盘。

拆解这次事故，是三个因素的叠加：**全权限常开、破坏性命令、无人监督的长时自主运行**。三者去掉任何一个，损失都还在可挽回的范围之内。因此这不是 prompt 质量的问题，也无法寄望于下一代模型更可靠——概率性的能力，必须配以确定性的约束；而约束不能依赖模型自身，要构建在挽具层（关于挽具对结果的影响，《专用挽具战胜通用挽具》[3]给出过可度量的对照）。这也是我们构建 AVL Code 时的分工：能力来自模型，约束来自挽具。

下面依次说明，AVL Code 把闸门设在哪里。

## 二、行为可见：过程可查，不依赖恰好在场

Matt 是恰好发现 Agent 正在删除文件的。可见性要解决的正是这一点：不依赖使用者恰好在场，也能知道 Agent 正在做什么、做过什么。

AVL Code 中，每一次工具调用都是会话流中一张独立卡片：工具名与入参摘要直接可见，被拒绝、连接失败等异常有明确的状态标识。命令携带的参数、返回的结果，无需翻查日志，就在对话原处。这些调用与结果全部写入会话记录，重新打开原样恢复；上下文压缩采用纯追加方式——原始记录不做物理删除，仅标记为不再进入上下文窗口。钩子（hook）的每次执行也会在对话流中留下一条系统消息，不是黑盒。

查看全局时，「轨迹」面板把一次运行调用的所有工具还原为时间线：调用顺序、每步的耗时与成败、每个工具的耗时分位统计，任何一步都可以定位回消息流的对应位置。后文将提到的无限制模式——连审批弹窗都跳过的档位——开关切换会记入日志，期间的操作照样作为工具调用写入会话记录。

子代理同样如此：它收到的系统指令、任务输入与每一条工具调用，都可以逐条展开查看。

![AVL Code 子代理任务详情截图：系统指令、任务输入与逐条工具调用，含一条被拒绝的调用](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicyFst1ibxKwk7mvnRZz1gYfhouSnFCHfib2baicXzACakWSRKiayZNMeIKHVNYWfzwKJUNia8ez6nibhjhM6iaTKLzxlN6ImmfQ03Xrg/640?wx_fmt=other&from=appmsg)

图 1：子代理任务详情，截自真实的漏洞扫描会话。系统指令、任务输入与逐条工具调用全程可查——包括被拒绝的调用。

这套可见性机制，我们首先用于自己：官网每个案例都附有未删减的会话回放，推理、工具调用、报错、恢复全程可查（见[《为什么 AVL Code 敢把 AI 会话挂在官网上》](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215058&idx=1&sn=b92e904705833bc2a1e93f8518d3d17f&scene=21#wechat_redirect)[4]）。敢于公开，是因为每一步本来就有记录。

## 三、动作可控：每类动作都有闸门，闸门有档位

可见性解决「知道」，可控性解决「拦截」。AVL Code 的每个工具都有三态开关——**启用、询问、禁用**：启用直接放行，询问在每次调用前弹窗确认，禁用直接拒绝；三态可在自动、筹划、准备、执行、评估五种工作模式下分别配置。我们推荐的工作流是先筹划、再执行：进入筹划状态后，自下一轮起暴露给模型的工具集被裁剪为只读集合——这不是提示词层面的约定，而是环境层的强制裁剪；计划经确认后，「退出筹划、进入执行」是一个显式动作。

针对几类高危动作：终端命令采用内置白名单，并可按工作模式自定义放行与拦截规则，支持正则表达式——例如将 `rm -rf /` 一类命令写入拦截规则；git 推送、合并、变基等操作可设置为「每次运行前弹窗确认」；修改 MCP 配置的写操作采用两步制——第一步仅返回 dry-run 预览，显式确认后才写入，单步无法完成破坏性变更；威胁情报默认只做哈希查询、不外发文件内容，密钥类敏感文件在任何配置下都不上传，样本内容确需外发时另有独立的确认环节。

![AVL Code 工具配置界面截图：每个工具的启用/询问/禁用三态开关，以及 fs.exec 的放行与拦截规则编辑面板](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkibdkXPuw8SWVpmesU6qicVyvy2HxwyaHLIVhu27R29WbicHN0MAu9ViasXZ9IH937sP7Ncjz5HcPSu2wkFwiawZcBX83X17Ze3dicC8/640?wx_fmt=other&from=appmsg)

图 2：工具三态开关与 `fs.exec` 放行 / 拦截规则。规则支持通配符与正则，按工作模式独立生效。

审批不限于桌面端：同一条审批会同时推送到桌面与已绑定的 IM，在微信中回复 `/approve`、`/deny` 同样有效，以最先应答的一端为准；每条审批请求带有唯一编号，勾选过的「一直允许」授权按工作区持久化，可查看、可撤销。30 秒无人应答，按拒绝处理——**超时的方向是拒绝，不是放行**。

对简短指令，还有一道更早的闸门：复述意图，默认开启——Agent 先复述它理解的目标与执行思路，经确认后再开始执行。`$HOME` 展开错误发生在执行层，而更多事故在意图层就已经偏离。

## 四、边界先划清：能访问什么，进场前确定

边界从选择工作区就开始：路径在软链接解析之后再校验，系统目录、家目录本身、`~/.ssh` 等敏感位置连同整棵子树，都不允许设为工作区。需要访问工作区之外的目录时，必须显式附加，分为只读与读写两档，附加前有确认，授权以会话为单位——对只读附加目录的写操作，后端直接拒绝。网络同样有边界：联网工具仅放行 http(s) 协议，从首次连接到每一次重定向都会解析目标地址，内网、环回以及云元数据地址一律拦截。

最严格的一段边界，留给最危险的物料。AVL Code 的用户日常处理恶意样本，工作区下的 `samples/` 目录是专设的分析沙箱——目录内禁止执行任何内容，该规则优先级高于全部用户配置，修改配置文件也无法解除。执行类动作发生之前，还会对目标做一次威胁核查——默认仅哈希查询，不外发文件内容。

边界的价值在于事前：它把「Agent 能访问什么」从每次执行时的不确定，变成进场前已经确定的约定。

## 五、高权限不常驻：危险状态难进入、易退出

回到事故的起点：Full Access 全权限，并且长期开启。

AVL Code 也有权限全开的档位，即无限制模式。但它被有意设计为**难进入、易退出、不持久**：进入前须经风险确认弹窗，原文表述明确——「开启后，本会话的智能体将不再弹出任何执行批准，可执行任意命令、访问内网/本机等任意网络地址」；确认按钮带 5 秒冷静期，倒计时结束前无法点击；开启期间界面常驻危险标识，随时可以一键关闭；作用域按会话隔离、仅存于内存、重启即清除。它放开的是审批弹窗、命令白名单与内网地址过滤——使用者可以进入这个状态，但会明确知道自己正处于其中，它也不会在无察觉的情况下延续为常态。

![AVL Code 无限制模式风险确认弹窗截图：列明放开的权限与保留的底线拦截，确认按钮带倒计时](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk8biaia3mR3hP6cR3w0AiaJrpIuxI94TEjKo2f0G1WzGJ0UgUsFvTnGMMQWI1SBGP8FQ4vVicibiaqGe8vibdkqAMlJXsY4JtFnZIRibAI/640?wx_fmt=other&from=appmsg)

图 3：无限制模式确认弹窗，截自真实的样本分析会话。确认按钮名为「请仔细阅读风险提示」，倒计时结束前不可点击。

对产品自身的操作，标准相同：设置中所有破坏性按钮都不使用单次点击即生效的原生弹窗——第一次点击不执行，只进入带倒计时的待确认状态（清理 3 秒、全量重置 5 秒），再次点击才会真正执行；涉及敏感数据的清理类别，执行前自动生成快照，可以就近回滚。

## 六、失控可停：子代理始终受控

这次事故的直接执行者，是一个无人监督的子代理。

AVL Code 中，子代理并行时每个分支都是独立上下文、互不可见，单个分支失败不影响整批；一次并行最多 16 个分支，同时运行的后台任务上限为 64 个。时间维度上有三层看门狗：单个工具空闲 10 分钟超时，子代理空闲 15 分钟超时，绝对上限 60 分钟——不存在长时间运行而无人知晓的子代理。

需要停止时，一次动作即可停止全部：停止操作先级联终止所有派生子任务，再停止主助手，不留孤儿进程。Matt 只能赶到电脑前手动终止进程；在 AVL Code 中，这个动作是一次点击，并且终止得彻底。被中断的任务也不会自行恢复：重启后以横幅列出，恢复或忽略由使用者决定；自动恢复默认关闭，即便开启，单次也最多自动恢复 5 个。

## 七、红线：不受任何开关影响

前面每道闸门都有开关——这是合理的，不同任务需要不同的权限口径。但最后一层没有开关。即便开启无限制模式，以下硬底线也不受影响：

* `samples/`

  沙箱——目录内禁止一切执行，优先级高于任何用户配置；
* 破坏性命令的参数校验——`rm`、`mv`、`cp` 的每一个路径参数都必须位于工作区之内，绝对路径一律拒绝，`--no-preserve-root` 直接拦截；
* 危险注入黑名单——fork 炸弹、写 `/etc`、`curl | sh`、`eval` 等模式，在白名单裁决之前先行拦截；
* 协议白名单——仅放行 http(s)。

这不是宣传表述，而是无限制模式确认弹窗中的产品原文：「仅保留底线拦截：`rm -rf` 类破坏性删除、`samples/` 沙箱、危险注入。」

回头看 Matt 那条命令：`rm -rf /Users/mattsdevbox`——绝对路径，目标在工作区之外，恰好落在参数校验明确拦截的范围之内，即便所有开关都调至最宽松。我们仍然不会说「这样就绝不会发生事故」，没有任何工程能够作此承诺；红线的意义在于，当最坏的那一次失误到来时，系统并非不设防。

## 模型基于概率，挽具不是赌博

@AYi\_AInotes 在事故拆解推文的结尾给出四条教训，前三条我们完全同意；第四条——「模型厂商的安全底线不一样」，Matt 也表示此事让他「一千倍地更信任」另一家的模型——我们只同意一半。模型的谨慎值得作为选型依据，但不值得作为安全依据：再谨慎的模型也是概率性的，把关键数据托付给概率，与 Full Access 常开没有本质区别。

控制论奠基人维纳（Norbert Wiener）1960 年在《科学》杂志上写道：

> 如果我们为达成目的而使用一种机械装置，而它一旦启动我们就无法有效干预——因为它的动作太快、且不可挽回，以至于我们来不及在动作完成之前介入——那么我们最好十分确定：置入机器的目的，正是我们真正想要的目的。

六十六年后，「太快、且不可挽回」恰好是那条 `rm -rf` 的准确写照。行为可见、动作可控、边界、冷静期、看门狗、红线——归结起来是同一句话：在「一次失误」与「不可挽回的损失」之间，设置足够多确定性的约束。这些机制写在用户手册与参考手册中，也原样运行在官网每一个公开案例的会话里——不是事故之后补充的承诺，而是产品从第一个版本就有的设计。

我们在 AVL Code 等你，驾驭赛博野驴——缰绳始终在你手里。

*关联引文：*

*[1]AVL Code官网*

https://www.avlcode.cn

[2]《从惊艳到理智：AI Coding 成熟曲线的五个阶段》

**https://www.avlcode.cn/blog/ai-coding-maturity-curve/**

[3]**《GLM-5.2 战胜了 Mythos？——专用挽具战胜了通用挽具》https://www.avlcode.cn/blog/specialized-harness/**

*[4][《为什么AVL Code敢把AI会话挂在官网上》](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215058&idx=1&sn=b92e904705833bc2a1e93f8518d3d17f&scene=21#wechat_redirect)*

*https://www.avlcode.cn/blog/why-we-publish-sessions/*

---

*AVL Code，AVL 安全引擎，与智能随行。安天澜砥团队出品。*

安天AVL Code官网链接：https://www.avlcode.cn

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk8PT5nqiaDOuVwSp5Yh8bbK9OZSKPOOvVygZmtrGWu1EoQ2WSvouP8ASaN9U4MvwhOlhZyOLia4ILUAZqIrDp3LzOJMaBwqYOY00/640?wx_fmt=jpeg&from=appmsg)

**安天AVL Code网站二维码**

**往期推荐:**

# *[为什么AVL Code敢把AI会话挂在官网上](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215058&idx=1&sn=b92e904705833bc2a1e93f8518d3d17f&scene=21#wechat_redirect)*

# [可控涌现：AVL Code 的工程范式（上） ——涌现不是魔法，而是系统属性](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215129&idx=1&sn=4a42cfd2f46b561759e00a386e31d06f&scene=21#wechat_redirect)

# [可控涌现：AVL Code 的工程范式（中） ——Harness 工程与 Loop 工程](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215132&idx=1&sn=63fdc21c34cce513e8727b402a3ed724&scene=21#wechat_redirect)

[可控涌现：AVL Code 的工程范式（下） ——从理论到实践与七条工程原则](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215137&idx=1&sn=1c96e26b0a8e9dcefbf6fbdd07c88908&scene=21#wechat_redirect)

# [用AVL Code验证“Claude Code内置隐藏机制，专门检测中国用户”的传言](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215022&idx=1&sn=77496defba538a08d0885e11cb5d3bbe&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxX...