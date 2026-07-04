---
title: 这帮人把安全审计做成了六道流水线，结果真挖出不少东西
url: https://mp.weixin.qq.com/s/hW38mpafNbj7Lg4sMXX_Ig
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:47:54.752425
---

# 这帮人把安全审计做成了六道流水线，结果真挖出不少东西

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf3bSI2FibicHleaoqV5wQFUYAiaiaIk6kLAJYjyujlsrE7o2CRBcsr2DicHbdWO7pfWNHKObHEeDAian6WLveVr03HvprYDWu2fzXYw/0?wx_fmt=jpeg)

# 这帮人把安全审计做成了六道流水线，结果真挖出不少东西

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Cloudflare 开源了一个 coding-agent skill，把安全审计变成了六阶段流水线。侦察、猎杀、验证、报告、结构化输出、独立复核——每一步都有专门的 agent 干活。实测下来，单次运行能覆盖约一半漏洞，多跑几次覆盖面会明显扩大。他们坚持“只报告你真正能利用的”，这个标准挺狠。

## 这玩意儿是怎么来的

先说背景。Cloudflare 的安全团队一直在搞自动化漏洞挖掘，他们内部折腾出了一套多阶段、跨舰队规模的漏洞猎杀系统。这套系统的原型，就是今天要聊的这个 security-audit skill。

它本质上是给 coding agent 用的技能包，装上之后你的 agent 就摇身一变成了安全审计员。Cloudflare 写了篇文章详细讲他们怎么搭建这套系统[1]，这个 skill 就是一切的起点——单仓库版本，麻雀虽小，五脏俱全。

## 六个阶段，环环相扣

审计流程拆成了六步，每一步都有明确的分工。说实话这个设计挺务实的，不是那种花架子。

### Phase 1：侦察

多个 parallel agent 同时开工，把应用的架构、信任边界、输入面全部摸一遍，输出一份 architecture.md。这一步相当于战前测绘，后续所有攻击都建立在这张地图上。

### Phase 2：猎杀

平行运行的通用 agent 从不同角度进攻代码库：注入、访问控制、业务逻辑、密码学、功能滥用、链式攻击，再加一个 wildcard 兜底。每个 agent 如果嗅到可疑点，可以自己 spawn 子 agent 深挖。这种自主决策机制让覆盖深度上了一个台阶。

### Phase 3：验证

最关键的一步。每个发现都会交给另一个独立 agent 去证伪。对抗性审查直接干掉误报。Cloudflare 强调一条铁律：检查漏洞的 agent 永远不能是发现漏洞的那个。这条规则从根本上杜绝了确认偏差。

### Phase 4：报告

产出两份文件：REPORT.md 给人看，FINDINGS-DETAIL.md 给 MEDIUM 级别以上的漏洞保存详细追踪记录。两层设计，兼顾可读性和可追溯性。

### Phase 5：结构化输出

所有发现写进 findings.json，格式严格遵循 report-schema.json。然后用零依赖的 Node.js 校验器 validate-findings.cjs 做 schema 验证。这一步确保下游工具能可靠消费这些数据。

### Phase 6：独立验证

全新的一批 agent 重新进场，拿着结构化输出中的每一条事实声明，去和源代码逐条比对。双重确认，把质量底线守住。

## 设计理念：有点激进，但很管用

这个 skill 有几个设计原则值得细说，因为它们直接决定了输出的可信度。

**只报告你能利用的。**没有具体攻击场景的东西不报。不说“攻击者理论上可能”，只说你到底能不能打进去。这个标准一下子砍掉了大量 noise。

**对抗性验证。**前面提过了，查漏洞的和找漏洞的不是同一批 agent。有点像 red team 和 blue team 分离，但这里是在 agent 层面实现的。

**严重度看影响，不看 checklist 偏离。**Likelihood 乘以 impact，不是因为你少了个 header 就给你标高危。这避免了那种“合规式审计”的毛病。

**纵深防御缺口不算漏洞。**如果 Layer A 已经挡住了攻击，Layer B 的缺失只是 hardening note，不会当作漏洞报。这个判断标准挺有争议性，但确实减少了假阳性。

**多次运行会扩大覆盖面。**他们的测试显示，单次运行大约只能发现总漏洞的一半。因为每次都探索不同的代码路径，skill 还会自动读取之前的 findings.json 文件，跳过已知问题，集中火力打新目标。

## 安装和使用，出奇地简单

装这个 skill 只需要一条命令：

npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit

想全局安装加 `--global` 就行。然后让 agent 指向目标代码库，说人话就行：

security audit this codebase

或者更具体一点：

find security vulnerabilities in ./src

甚至指定输出路径：

do a security review, output to ~/audits/my-project

skill 会自动匹配触发词（security audit、find vulnerabilities、pen-test the code 等等）。输出目录默认是 `~/security-audit-skill/<repo>/run-<n>`，你也可以自己指定。

## 限制条件和前提

* 需要一个支持 tool use 和 parallel sub-agent 的 coding agent 模型
* Node.js 环境，Phase 5 的 schema 验证要用

除此之外没有别的依赖。那个 validate-findings.cjs 是零依赖的纯 Node.js 脚本，不引入任何第三方包，这点考虑得很细致。

## 文件清单

整个 skill 就 7 个文件，结构清晰：

| 文件 | 作用 |
| --- | --- |
| SKILL.md | 安装配置、核心原则、平台术语、工作流概览、审计反模式 |
| RECONNAISSANCE.md | Phase 1 侦察提示词和综合指令 |
| HUNTING.md | Phase 2 编排、猎杀方法论、验证规则 |
| ATTACK-CLASSES.md | 核心攻击类、wildcard、基础攻击提示词 |
| VALIDATION-AND-REPORTING.md | Phase 3-6 的验证、报告和复核流程 |
| report-schema.json | findings.json 的 JSON Schema 定义 |
| validate-findings.cjs | 零依赖 Node.js 校验脚本 |

## 我的一些观察

这套系统最大的价值不在于自动化本身——自动化审计工具多得是。它的亮点在于把对抗性思维和独立验证这两个概念工业化了。

传统的 SAST 工具经常被诟病 noise 太多，安全工程师花大量时间排误报。这个 skill 用 agent-on-agent 验证来解决这个问题，思路很巧。但这也意味着计算成本不低：每个漏洞要经过发现、挑战、复核三轮处理，相当于至少三个 agent 在接力。

另外，“只报告能利用的”这条原则，对 agent 的能力要求很高。它需要 agent 真正理解漏洞的利用链条，而不仅仅是模式匹配。Cloudflare 的模型显然能满足这个标准，但换成其他模型效果会不会打折扣，这是个问号。

多次运行扩大覆盖面的特性也很实用。安全性审计没法穷尽，但通过随机性和增量分析，可以在有限时间内逼近一个比较完整的覆盖面。读取历史 findings 来跳过已知问题的设计，避免了重复劳动。

如果你也在搞自动化安全审计，这个 skill 的设计文档值得仔细读。哪怕不直接用，里面的很多理念——尤其是对抗性验证和分级报告——都可以借鉴到自己系统里。

---

### 参考资料

[1] https://blog.cloudflare.com/build-your-own-vulnerability-harness

[2] https://github.com/cloudflare/security-audit-skill

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过