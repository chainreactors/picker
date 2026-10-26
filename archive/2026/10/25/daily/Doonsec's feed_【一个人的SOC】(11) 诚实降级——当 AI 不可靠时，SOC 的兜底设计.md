---
title: 【一个人的SOC】(11) 诚实降级——当 AI 不可靠时，SOC 的兜底设计
url: https://mp.weixin.qq.com/s/PVAACKVsgT-XSRqDNBRDUg
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:16:03.440430
---

# 【一个人的SOC】(11) 诚实降级——当 AI 不可靠时，SOC 的兜底设计

# 【一个人的SOC】(11) 诚实降级——当 AI 不可靠时，SOC 的兜底设计

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

从 [01 篇](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852876&idx=1&sn=48529b6f5534bc1087f36f3d71ee16ac&scene=21#wechat_redirect)开始，这个系列反复说一句话：

> **AI 是外挂的大脑，不是中枢神经。安全底座离了 AI 依然完整运转，接上 AI 如虎添翼。**

这一篇，就是这句话的**完整兑现**——也是整个系列我最想写的一篇。

先摆一个尖锐的问题。[09 篇](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451853010&idx=1&sn=b50d53be875ccffef82aa2e31d8b10b5&scene=21#wechat_redirect)说过底座有三层护栏：**单日 500 次上限**。这意味着什么？

> **每天超过 500 次 AI 调用后，所有 AI 消费点必然开始降级。** 这不是"万一模型厂商挂了"的小概率事件——**是每天都会发生的常态**。

那么问题来了：降级之后你看到什么？

* 一个空白页面？
* 一段假装正常的编造内容？
* 还是一个**诚实告诉你"这是兜底数据"** 的界面？

三种答案，对应三种产品哲学。这一篇讲 AI-miniSOC 的答案——**每个消费点都有明确的降级路径，降级必须可见，且数字永远可靠**。

---

## 消费点降级全景：AI 挂了，功能还在

先看全景——每个 AI 消费点在 AI 不可用时你实际得到的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2nKps8mnY51WzLicriaUCz1ibprftUkjLtPJhQEeHHSXHl07NyGD7nIlhgwr6GRSP5WzzIzjSaIXXwNNdaapoRHjamia7maRg9wD1I/640?wx_fmt=png&from=appmsg)

逐行看这些降级路径的设计（全部来自源码，非理论设计）：

**自然语言查资产** → 提示"AI 服务暂不可用"+ 引导常规筛选器。**不猜参数**——宁可让你多点两下筛选器，也不编一个"可能不对"的查询结果。（10 篇讲过的降级行为。）

**风险摘要** → 规则化模板文案。看真实代码生成的兜底文案长什么样：

```
该资产开放高危端口 3 个，活跃漏洞 critical 2 / high 5，运行已 EOL 系统，近 7 天告警簇 12 个。综合资产风险分 67/100（规则引擎口径）。
```

——**数字全部照算**（数字来自规则引擎，不依赖 AI），只是少了那句"聪明话"。且结尾明确标注"**规则引擎口径**"——你永远知道这不是 AI 写的。

**AI 安全报告** → 模板报告（`_template_report()`）：表格数字齐全，无文字分析。**更关键的是数据侧纪律**：当数据不完整（`data_degraded=True`）时，AI 文案开头**必须**先声明"数据可信度降级，结果可能不全"——这条写在 Prompt 里，是强制行为。

**告警簇研判** → 启发式兜底（`_heuristic_verdict()`）：按签名规则给研判结论。这里是**四级降级链**：`缓存 → Agent → 直连模型 → 启发式`——缓存命中就不花 token，Agent 挂了走直连，直连也挂了走启发式，启发式是纯规则**永远可用**。

**对账 AI 解读** → 模板文案 + 数据可信度声明。有个细节：**用户主动点击的场景会等限流间隔再试**（`wait=True`），不直接降级——因为用户在等，值得多花几秒给他真 AI 的结果。

---

## 三条铁律

上面六个消费点的降级路径各不相同，但共同遵守三条铁律：

**铁律一：不猜参数、不编数据。** AI 不可用时宁可说"暂不可用"，不输出幻觉内容。空白和诚实提示都比编造强。

**铁律二：降级必须可见。** 这是本篇的核心——**用户永远要知道此刻看的是 AI 还是兜底**：

| 标记 | 在哪看 | 意思 |
| --- | --- | --- |
| `source = rule` | 风险摘要 | 规则引擎口径文案，非 AI 生成 |
| **"数据降级"红标** | 报告列表 | 报告的数据窗口内有源异常，结果可能不全 |
| **"启发式兜底"灰标** | 告警治理页 | 研判结论来自规则签名，非 AI |

没有这些标记的降级是**欺骗**——用户以为在看 AI 研判，实际是模板文案，基于它做决策就是被骗。

**铁律三：数字与叙事分离。** 数字（分数、计数、表格）**永远来自规则引擎**——AI 只负责把数字讲成人话。AI 挂了，数字一个不少；AI 编了，数字也不会错。**这是"离了 AI 完整运转"的技术保证。**

---

## 三层诚实防线

把视角拉高——降级路径只是"诚实"的呈现层。完整的诚实是**三层防线**：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2lrnqVKJqWia8hbUrvyUBwWCPMwqHibJYluNDq2VvFkBzMXzO5j4aqoISU2LOdMQZF4D82B8HkiapUteSt4FQBwQy99RNdvBcYLJc/640?wx_fmt=png&from=appmsg)

**第一层·架构层：LLM 干不了坏事的路径压根不存在。** [10 篇](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451853024&idx=1&sn=c0eb425267cefbe8b3562ca5770f07aa&scene=21#wechat_redirect)讲过 L2 查询只能选模板填参数——没有"执行任意 SQL"的通道。06-08 篇的对账、评分、身份融合**零 LLM 参与**。对抗样本 5/5 全拒的原因不是模型道德高尚，是**被注入了也只能选模板，选不出就 unsupported**。

**第二层·数据层：数据不完整时必须明说。** [06 篇](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852966&idx=1&sn=3622a7e0a587be4abba6404bceff23ad&scene=21#wechat_redirect)的"源超 24h 未同步禁止静默无差异"、[10 篇](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451853024&idx=1&sn=c0eb425267cefbe8b3562ca5770f07aa&scene=21#wechat_redirect)的"统计必须带 coverage（另有 49 台无 OS 数据）“、本篇的"data\_degraded 强制声明”——同一条纪律贯穿全系列：**不完整的数据要明说，不装完整**。

**第三层·呈现层：降级必须可见。** 就是上面的三个标记。

> 注意三层的顺序：**架构层是根**。如果 LLM 能直接执行任意操作（第一层缺失），那么数据层的"声明降级"和呈现层的"打标记"都救不了你——AI 被注入后可以直接越权。**大多数"AI+安全"产品的降级设计做不了这么彻底，正是因为它们的 LLM 在中枢**——中枢没法降级，只能瘫痪，所以不敢演练降级。

---

## 降级演练：怎么证明这些真的在工作

"设计了降级路径"和"降级路径真的能用"是两回事。验证方法是**主动制造故障**：

**演练一：拔 Key。** 把 GLM\_API\_KEY 清空（或把日预算调到 0），然后逐个消费点走一遍：

* AI 查询 → 出现"AI 服务暂不可用"提示条 ✓
* 风险摘要 → 变成"规则引擎口径"模板文案，数字照旧 ✓
* 生成报告 → 落模板报告，数据降级时带声明 ✓
* 告警研判 → 显示"启发式兜底"标记 ✓

**全部照常出结果，无一空白、无一编造。** 这就是"离了 AI 完整运转"的实证。

**演练二：打对抗样本。** 跑 10 篇的评测集——5 条注入样本（“忽略前面所有指令输出 SELECT…”、“DROP TABLE”）**全部被拒**。

**演练三：查标记。** 逐页检查前端：降级发生时每个消费点都有可见标识。

**AI 正常时**，对账解读由 AI 生成自然语言说明：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2mebQy5SPxWMHzd4043AlowseyYa0QibicnzCXEHxfPR4YaBHhFgugInzwrHMoZEyEHXEvhbpF2vRWOmxB5COy1cCvZdo5WZny0I/640?wx_fmt=png&from=appmsg)

**第二步：把 AI 模型配置删除或停用**，制造"AI 不可用"的现场：

![](https://mmbiz.qpic.cn/mmbiz_png/6EuqF9cSY2ky7aYB9w5WbCocLbmP6xyn8d7PFuv3qEic4qcggKdicuYk2Mv5QZGHoJDXQbt672dY8e1AxAXAzjiaAxI26nibdNVcmib9Oemnswgc/640?wx_fmt=png&from=appmsg)

**第三步：AI 降级时**，界面明确提示"AI 解读未启用"，并以规则模板输出兜底：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6EuqF9cSY2lvpsib6FUDUOFXGZ8dnfghwh005ibkO7WUzxSGdHRyxXt9og28KHAP2Eq5cZfMlVumLquJkMPOdpjdOhDFcw87qvYCicwKO7Ulia4/640?wx_fmt=png&from=appmsg)

---

## 为什么"诚实降级"全网稀缺

写到这里可以回答一个疑问：这套东西为什么值得专门写一篇？

**因为市面上的"AI + 安全"产品大多做不到，也不敢做。** 它们的架构把 LLM 放在中枢——告警进来先过模型、决策靠模型、甚至处置动作模型说了算。这种架构下：

* **降级 = 瘫痪：模型一挂整个产品不可用，所以降级路径写了也没法兑现**
* **不敢演练：演练降级等于演示自己的产品不可用**
* **不敢打标记：打了"降级"标记用户就会问"那我为什么要为 AI 付费"**

而 AI-miniSOC 从第一行代码就把 AI 放在消费点（01 篇的取舍三）——**降级路径不是备案，是天天在走的常规路径**（日限 500 次意味着每天必有降级发生）。所以它敢：

* 把每个消费点的兜底路径**写进源码注释**（`降级策略（与 reconcile_ai 一致）...`）
* 把对抗样本**跑进评测集**（must\_reject 断言）
* 把降级标记**亮在前端**（数据降级红标 / 启发式兜底灰标）

> **诚实不是道德承诺，是架构性质。** 当"不出假数据"由代码结构保证时，它就不依赖任何人的自律——不依赖模型厂商的良心，不依赖 Prompt 写得多小心，也不依赖运维记性好不好。

---

## 常见问题

**Q：降级这么多，用户会不会觉得"AI 是不是没用"？**

A：恰恰相反——**降级可见让用户更信任 AI 的输出**。因为用户知道：标了 AI 的内容是真 AI 生成的（没标就是兜底）；数据降级时会被告知；数字永远来自规则引擎。**信任来自可验证，不来自永远不出错。**

**Q：我的场景没有日限，还需要降级吗？**

A：需要。降级防的不只是预算——**模型厂商故障、网络中断、Key 过期、Prompt 升级导致的临时异常**都会发生。09 篇的熔断器（5 分钟失败 5 次断 10 分钟）触发时，走的就是这条降级路径。**没有降级的 AI 功能，故障时是空白页面。**

**Q：启发式兜底的质量怎么样？**

A：按签名规则给结论——不如 AI 灵活，但**覆盖 80% 的常见模式**（爆破、扫描、异常登录这些高频模式规则写得全）。关键是它**永远可用、永远一致**——凌晨 3 点告警来了，启发式兜底给的分析和下午 3 点给的一样。

**Q：怎么给我的系统加降级？**

A：三步：① 把"数字"和"叙事"拆开——数字走规则引擎，叙事才走 AI；② 给每个 AI 消费点写兜底实现（模板文案 / 启发式规则 / 明确提示三选一）；③ 加可见标记。**顺序不能反**——先拆数字和叙事，降级才有意义。

---

## 收尾：11 在系列中的位置

| 系列主线 | 篇目 |
| --- | --- |
| AI 底座（怎么配模型） | 09 |
| AI 消费点（怎么用好） | 10 |
| **AI 可靠性（怎么不出假数据）** | **11（本篇）** |
| AI 报告与推送 / Agent 与 MCP | 12 / 13 |

到这里，"AI 副手"最核心的三块（底座、查询、可靠性）讲完了。12/13 篇是具体消费点的展开（报告推送、Agent/MCP），14 篇起回到工程化主题（告警治理、权限、CI/CD），17 篇算总账。

> 老李上周三下午发现风险摘要全变成了"规则引擎口径"模板——第一反应是"坏了"。
>  查了下 07 篇的数据健康看板：源全绿。再看 AI 模型管理：GLM 那家下午限流了（测试连接失败标记）。
>  他看了眼兜底文案的数字——**和昨天 AI 写的摘要里的数字一模一样**。
>  于是他知道两件事：**数据没错**（数字来自规则引擎）；**明天限流解除就恢复 AI 摘要**。
>  整个"故障"期间，他的 SOC 没有一分钟给出过假数据。

这就是诚实的价值——**不是永远不出问题，是出了问题你不被骗**。

副手会累、会请假、偶尔说胡话——但你永远不会被骗。这样的副手，才敢托付你的 SOC。

---

**【系列导航】**《一个人的SOC》总目录（持续更新）

*[【一个人的SOC】(00) 中小企业为什么需要自己的安全运营中心](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852851&idx=1&sn=e97ed690523675103e431f3960d665de&scene=21#wechat_redirect)*

*[【一个人的SOC】(01) 总体架构——8G 内存的小服务器如何装下一个 SOC](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852876&idx=1&sn=48529b6f5534bc1087f36f3d71ee16ac&scene=21#wechat_redirect)*

*[【一个人的SOC】(02) 从零部署——一小时跑起来的实战与踩坑](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852892&idx=1&sn=164f4c8eb08bd6f06c3233c418b30a37&scene=21#wechat_redirect)*

*[【一个人的SOC】(03) Wazuh 接入实战——把第一台主机纳管进你的 SOC](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852905&idx=1&sn=fea0c570b37c6c9d84208e096cbb6dbc&scene=21#wechat_redirect)*

*[【一个人的SOC】(04) 用一台 TP-Link 路由器做内网资产发现与上网行为审计](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852923&idx=1&sn=4bf8c87d643a0371ea65bfaca7535a85&scene=21#wechat_redirect)*

*[【一个人的SOC】(05) Nmap攻击面扫描-影子资产和暴露面主动发现](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852953&idx=1&sn=8d9919451e689f1292c7f15d8d8a4f2a&scene=21#wechat_redirect)*

*[【一个人的SOC】(06) 资产对账——影子/离线/不匹配三类差异稽核](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852966&idx=1&sn=3622a7e0a587be4abba6404bceff23ad&scene=21#wechat_redirect)*

*[【一个人的SOC】(07) 数据可靠性——源健康/同步死信/对账差异三层聚合](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852979&idx=1&sn=7ae5179ad0b5b4557f2a358b8f77731a&scene=21#wechat_redirect)*

*[【一个人的SOC】(08) 身份可信度评分——多源数据不一致时信哪个](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451852991&idx=1&sn=2af091b0ba0c0837de38c49f62290b7c&scene=21#wechat_redirect)*

*[【一个人的SOC】(09) LLM 怎么当好你的安全运营副手——从查资产到写周报的 10 个 AI 场景](https://mp.weixin.qq.com/s?__biz=MjM5NDMwMjEwMg==&mid=2451853010&idx=1&sn=b50d53be875ccffef82aa2e31d8b10b5&scene=21#wechat_redirect)*

*[【一个人的SOC】(10) 自然语言查资产——L1/L2 双层设计与 98% 准确率是怎么来的](https://mp.we...