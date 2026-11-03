---
title: Wiz Q3发布会：抢的不是检测模型，是四个新遥测入口
url: https://mp.weixin.qq.com/s/tRFxd1lRCacFQN8X7zKmlA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:26.466959
---

# Wiz Q3发布会：抢的不是检测模型，是四个新遥测入口

# Wiz Q3发布会：抢的不是检测模型，是四个新遥测入口

OSINT研习社

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Wiz 在 10 月 29 日办了 Wiz Wrapped Q3，直播 39 分钟，官方没挂 PPT 附件。

中文安全圈关注不多，大部分人看到的是"Forrester Wave 领导者"这类 PR 标题。那条不重要——评分是结果，不是信号。

这 39 分钟真正的信息量，用一句话概括：

**Wiz 本季度没有发布任何一项 GA 功能，但它把采集范围从"云里跑了什么"，推到了"人是怎么用 AI 把东西造出来、Agent 是怎么被用起来"的位置上。**

它抢的不是检测模型，是遥测入口。

## 一、先看清骨架：四进一出

把 40 页摊开，结构比任何一页内容都更能说明问题。三节标题分别是 AI SAST & Dev Workstation Sensor、Wiz Defend Updates、Wiz for SaaS Security。

![议程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RdkWPwibvQFDfzzicP3mxk27XNLbQ4NFK5IR6I4V6xYk63r5wqUejcFdarfVultEZEAOmvo6hI2Yq87Ego22pgZ0JXBXDMs0JFrhGBghkWdfQ/640?wx_fmt=jpeg&from=appmsg)

三个位置——开发者的笔记本、AI 的推理调用、销售在用的 SaaS——此前都不在 Wiz 的采集范围里。

画成一张图是这样的：

| 层次 | 新增入口 | 采集内容 |
| --- | --- | --- |
| ① 开发者工作站 | Endpoint Sensor | 本地包 / IDE 扩展 / 本地凭据 |
| ② 代码 | AI SAST | 业务逻辑缺陷 / 跨文件数据流 |
| ③ AI 推理调用 | AI Invocation Logs | 系统提示 / 输入输出 / 工具调用 / 思维链 |
| ④ SaaS | SaaS Connectors | 审计日志 / OAuth 授权 / Agent |

四个入口全部汇入中间的 Security Graph——统一资产与身份上下文。往下挂三个 Agent：Red 从外部真实验证可利用性，Blue 像响应分析师那样跑完调查，Green 指派到人和工单。

这张图同时解释了进攻和防守两侧：单点能力（一个 AI SAST 引擎、一个 SaaS 日志解析器）都能被复制，但把四类遥测挂到同一张资产图上、再让 Agent 依次验证和定性，需要数据密度做前提。

反过来说，这也是它的天花板——**离开 Wiz 已有的云资产，这套叙事转不动**。

## 二、开发者工作站与 AI SAST

这一节解决同一个问题的两端：代码在写出来之前、在写出来的那一刻，就已经出问题了。

### 三个数字，目的不是证明风险大

P06 给了三个数字：**80%** 的组织在用 AI IDE 扩展，**71%** 至少有一个"未授权使用"的 AI 编码工具，开源恶意软件同比增长 **75%**。

讲者点名三起事件：Shai-Hulud、Axios 投毒，以及一起被念作 "singularity" 的供应链事件，攻击起点都是开发工作站。

![三个数字](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RdkWPwibvQFBTShhU9xXphwiaNI4QUEtEvFVMjwPgaH2n0qfMQXpLYVNYucNk0BricwwmKg5VEMibaDDOgdPGvR7ITR3nFCj7mnibQJV9Xzm71fk/640?wx_fmt=jpeg&from=appmsg)

这三个数字真正的作用，是证明**风险已经绕开了传统控制点**：CI/CD 流水线看不到开发者笔记本上装了哪个 IDE 扩展，代码仓库的 SCA 也看不到本地 `.npmrc` 里那把长期有效的云 key。

潜台词是："你现有的安全工具在这台机器上没有布点。"

### 端点之所以必须自己做，因为要"读懂云端"

P07 是产品定义：装在 Windows / macOS 上的端点传感器，右下角标注 **Private Preview**，讲者口述时也带保留（"if I'm not mistaken"）。

![端点传感器](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RdkWPwibvQFBF45d0X9icr96Y58rKMOicdAMxqjNkJzq8w4SqnNu55p5X5d3UEvAYQ9O6icADSBjSrm3qzcT4tFQYibI4WqL2xVkdbmGGoHPs12Y/640?wx_fmt=jpeg&from=appmsg)

纯 EDR 厂商也能装端点。差异不在采集，而在采集之后能不能接上云：在笔记本上发现一把 AWS key，别的产品只能告警"发现硬编码凭据"，Wiz 能顺着 Security Graph 算出这把 key 通向哪些实例、哪些桶、哪些数据。

**本地发现、云端定性**——这是它把端点塞进自己叙事的关键理由。

六步闭环里有一处分层值得单独记：事中阻断是检测到 `npm install` 或 trufflehog 外传时终止进程，这是 EDR 的常规动作；**事前护栏是已知恶意包永不落盘**，这才是差别所在。

从"发现坏事发生"变成"让坏事没有发生的条件"。

### AI SAST：先把问题定义成"一整类缺陷被系统性漏掉"

这段的说服逻辑值得单独拆，因为它没从功能讲起，而是先证明品类存在空白。

P09 是一张 CWE 覆盖矩阵，蓝点是规则引擎已覆盖的，白色空白是需要语义理解才能覆盖的那一整类——**空白本身就是论点**。

![CWE 覆盖空白](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFDvQUM1Y4QUsVicBoibL6HlZwuLSDsibaHdGle88FRqezDt8SP5Rxm1gED6y38adAJmPtSibWk83l5eoLlticIhTvrZW0uzQUeP4vYc/640?wx_fmt=jpeg&from=appmsg)

接着 P10 逐条否证现有补救路径：

| 现有做法 | 为什么不成立 |
| --- | --- |
| 人工审计 / 代码评审 | 撑不住代码量涨 100 倍 |
| 渗透测试 / 众测 | 上线后才发现，单次 1 万–15 万美元 |
| 把通用大模型直接指向代码库 | 不叫策略：贵、只是时点快照、还要自己搭 harness 和结果归口 |

第三栏几乎是冲着"给个 LLM 扫代码"的那批创业公司去的。没有威胁模型、没有 harness、没有结果归口，就不构成产品。

官方口径是 **over 81 new CWE types**——注意是"新增覆盖 81 类以上"，且明确"与规则引擎互补而非替代"。

![AI SAST](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RdkWPwibvQFBUWIPaFJtISqYAQxdibSPH8KhLCCQILn6hlbOwRfpN3J1V5NT9KrxiaMpIQpNiaZ6zaXCfoPfwxNjxgIe2PSuYJvfia6iaxnkA0icls/640?wx_fmt=jpeg&from=appmsg)

可信度背书：CyberGym benchmark **91%** 成功率、发布当天登顶；**200+ 零日漏洞**在高度审计过的开源项目里自主挖出。

![benchmark](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFAAdP8xEUmM3KUPAxmibXZH8a4QkSunkyVQMLJlq8t3Aib46kq9O7M1ARic0SLxZdbUGicxoOaQhF2N3so3EgH9UtYNlq47bJicM8Cg/640?wx_fmt=jpeg&from=appmsg)

引用时口径要说清：91% 是特定 benchmark 上的单点成绩，不等于真实客户代码库的检出率；200+ 零日来自 Wiz Research 的自主挖掘，和"客户环境里能挖出多少"是两件事。

### 六段式编排：一份现成的降误报模板

AI SAST 内部不是单一模型，而是六段式多 Agent 多模型编排：

| 序号 | 环节 | 用什么模型 | 做什么 |
| --- | --- | --- | --- |
| 1 | Threat Modeling | 前沿推理 | 先建威胁模型和攻击者假设 |
| 2 | Hunting Agent | 前沿推理 | 按假设去找证据 |
| 3 | Triage Agent | 轻量模型 | 降噪分诊，扔掉不值钱的候选 |
| 4 | Adversarial Debate | 前沿推理 | 对抗辩论，正反互相挑战 |
| 5 | Judging | 前沿推理 | 裁定 |
| 6 | Prove Exploit | 前沿推理 | 必须证明可利用才放行 |

关键设计：**只有分诊用便宜模型，其余五段全是前沿模型，中间插一轮对抗辩论，最后必须"证明可利用"才出结论。**

这解释了它为什么贵却精度高。对正在压误报率的团队，这几乎是可直接套用的结构：便宜模型降噪 → 贵模型判断 → 对抗辩论二次校验 → 可复现作为单一的放行闸门。

演示共 11 页，全是剪好的界面截图。但编排顺序很有意思：**先选靶子（P15 按暴露面给 Tier 建议），再算成本（P15 顺带预测本次扫描的 token 消耗），最后才看结果。**

这是把采购异议提前到演示里解决，而不是等客户问。

那个 IDOR 案例值得记住：越权改一个 URL 参数就能下单别人的购物车。规则引擎抓不到它，因为它不是语法错误，而是"这个接口的业务语义不允许这样访问"。

这正是 AI SAST 存在的全部理由。

## 三、Wiz Defend：三处变化，每一处都在否定传统检测的前提

Tal Moriah 这一节先立论、再给引擎、最后给证据。

| 变化 | 为什么它在拆传统检测的地基 |
| --- | --- |
| Agentic 威胁模型本质不同 | Agent 非确定性运行、有"意图"，意图会漂移或被操纵。传统 IOC 与规则匹配的底层假设是"同样输入产生同样行为"，这个假设一破，规则只剩滞后的事后描述能力 |
| 攻击面与爆炸半径被放大 | Agent 天生要宽权限才有用，攻击点分布在工作站、云、SaaS。权限设计本身成了风险源，不是配置错误的副产品 |
| 检测响应窗口在收缩 | 前沿模型能发现、串联并自动执行利用链，攻击者以算力速度作战。防守方有同样的模型，但流程和组织速度跟不上 |

### 新增的遥测类型：AI 调用日志长什么样

这是全场技术含量最高的一段。新增日志类型包含**系统提示、输入输出、工具与工具调用、思维链**。

特点是体量大、语义复杂，而且"哪一步是恶意"极难判定——一段提示里夹了一句注入，从日志形态上看和正常请求没有差别。

![AI 调用日志架构](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFBEKQ4zx7vtJ9uNhnP9KwhEMcqURqf6wbNAEXaickWnxbsEDuxXudDWTA1bHpDlcZtm5pT4mjzXcoyZIubD5k5lQxoz8gBWJppQ/640?wx_fmt=jpeg&from=appmsg)

这一页最该注意的不是检测类别，而是**中间那个圆环的画法**："检测引擎"和"Security Graph"被画成一个整体。

它要表达的是：AI 调用日志里的可疑行为只有放回资产图里才能定性——孤立看一条日志，没法判断"这个 Agent 调那个工具"算不算越权。

### 四段管道：算力花在判断，不是花在过滤

![四段管道](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RdkWPwibvQFBDh33GyQSp0wpRRnCK9OT5wXw8BbtQcZrBIapib3ib9xkWVpJDWb0YKJLlsBbQwqibeYicep5UpmP9WUWmkplhL0fG3WoVeuAwkBw/640?wx_fmt=jpeg&from=appmsg)

三个细节值得记：

1. **初筛是四路并行而不是一条链。**

   要同时抓"形态异常"和"语义异常"两类线索，串行会漏。
2. **小模型降噪 + 大模型定性的两段式。**

   本质是把算力花在判断而不是过滤上，这也是它敢按日志量收费的前提。
3. **脱敏被单独画成一个环节。**

   说明"数据不出域"是这类产品的采购前提。

### AI 专用 TDR：选 ATLAS 而不是自造框架

规则库已超 **4,000 条**，按 MITRE Tactic、平台、来源、严重度筛选。

但注意可信度差别：**映射 MITRE ATLAS 是页面背书，4,000+ 这个总数是纯口述，界面里并没有标。** 对外引用必须标注"讲者口述"。

![TDR 规则库](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFDXrS4sNIwLqZxLcYFKpueicVy8j5kDETico7jKy7rOLGOGicnQe2BSjrLFVBdbKgZkg0A2BnCGjd88SzXj6IiaL3asZ06ticOEtZf4/640?wx_fmt=jpeg&from=appmsg)

选 ATLAS 而不是自造框架，是降低客户认知成本——客户安全团队已经懂 ATT&CK，迁移成本远低于学一套新分类。

### 本场仅有的实质性商务变化

**Blue Agent 对所有 Wiz Defend 客户默认开启。**

这是整场仅有的一项真正的商务宣布。不需要加购、不需要单独开通。把它放在发布会靠后位置讲，说明 Wiz 把它当成"应该有的东西"而不是"要卖的东西"。

参照意义很直接：**调查定性这一层的商品化速度会比想象中快**，它正在从差异化卖点变成基线能力。

## 四、SaaS 安全：每一个控制都"正常工作"

Sakshi Khurana 这一节如果只看结论，是"我们也能管 SaaS 了"。真正的价值在中间那个案例。

### 先争定义权：SaaS 是云的延伸

P35 的论点：攻击者不按你的生命周期看问题。你说 code / pipeline / cloud / runtime，他看到的是一个连通系统，而 **SaaS 是插在每一段上的**。

OAuth token、服务账号、贴进工单的 API key 都在 SaaS 里。

这句话不止是技术判断，更是**争夺品类定义权**：客户接受"SaaS 属于云安全"，Wiz 的既有资产就直接覆盖过来；客户认为 SaaS 是独立品类，那就要重新采购。

看懂这层，就理解为什么它把 SaaS 放进同一场发布会而不是单独开一场。

### Agent 的四重身份：一个很好用的拆法

新的风险源头在于：Agent 不再由平台工程师在云控制台里建，而是销售团队在 Agentforce、Copilot Studio、Gemini Enterprise 里建。

讲者原话大意是：**"没写过代码的人在建软件，而且完全跳过了安全评审。"**

![Agent 四重身份](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFD3wbv5nIYmlj0OibdLibArn8O5y9zj2YDPsT5cLVQbXFNbribOnmChGoA2O9Ykib71eeAhtoWOUW5xPloic4INQv87j2pf87R43pHQ/640?wx_fmt=jpeg&from=appmsg)

这个四象限拆法可以直接拿来用：

| 维度 | 内容 | 风险 |
| --- | --- | --- |
| 身份 | 一个非人类身份 | 无法用"人"的流程做审批 |
| 权限 | 一组授权范围 | 要它有用就必须给宽权限 |
| 动作目录 | 它能调用的工具清单 | MCP server 越多，攻击路径越多 |
| 语料库 | 它能读到的数据 | 提示注入的入口 |

要它有用就得上公网（招来提示注入）、就得接 MCP server（招来 SaaS↔SaaS、SaaS↔云 的攻击路径）。

**能力与风险是同一个决定的两种后果**——这个表述比"AI 有风险"有力得多，因为它指向设计取舍，不是道德判断。

### Salesloft Drift：每一个控制都"正常工作"

这是全场最好的案例，引自 Google 威胁情报团队。

![Drift 攻击链](https://mmbiz.qpic.cn/mmbiz_jpg/RdkWPwibvQFABwhNNP0JJZt0Cd2M9KP0d2UyCzZtl6gEvzjjbnRwkgE0Q8Ggq3XNQKT5lOiarw17s9QL56kl8uRSqGqHmk6HLLwRNYqibgkj1E/640?wx_fmt=jpeg&from=appmsg)

整条链走了 **10 天**。没有钓鱼、没有恶意软件、没有单点登录失陷。攻击者偷了 Drift 在 Salesloft 的 OAuth token，通过 API 查询了 **700+ 个 Salesforce 组织**。

| 步骤 | 动作 | 为什么没被拦住 |
| --- | --- | --- |
| 01 | 偷 OAuth token | Drift 在 Salesloft 的第三方授权被拿走 |
| 02 | 查询 700+ 组织 | 全部是合法 API 调用，控制没有报警 |
| 03 | 把 CRM 当索引翻出云凭据 | case record 里贴着的 AWS key、口令、Snowflake token |
| 04 | 换成 IAM user | 从 SaaS 身份跳到云身份，跨了控制域 |
| 05 | 摸到 S3 桶 | 数据湖暴露 |
| 06 | Snowflake → 客户 PII | 继续横向，终点是最终数据 |

全案的关键句是：**每一个控制都正常工作，因为每一次 API 调用在技术上都是合法的。**

每一步单看都不构成入侵信号：第三方授权是正常的商业集成，API 查询是正常的 CRM 使用，搜索是正常功能。

**检测点不在"某次调用异常"，而在"这条授权关系不该通向这些数据"。** 这也解释了为什么 SaaS 安全必须依赖资产与权限图，而不能只靠日志规则。

同一套打法还打了 Gainsight 和 Clue。这不是孤例，是可复用的攻击模式。

### 能力矩阵：四块，但只有一张图

![SaaS 能力矩阵](https://...