---
title: 28 个 AI 特工帮你打渗透测试，这工具要抢安全人的饭碗？
url: https://mp.weixin.qq.com/s/y4WZpWVnGTchTwoYLRBd3g
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:59:17.564842
---

# 28 个 AI 特工帮你打渗透测试，这工具要抢安全人的饭碗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NOEA4kjeYuKr3RJCafR9S2qzxcQ3LsWN3iav9sgB8hCun3Lp2MiciaMiayibgVak5fvcpgzcMhXur1KXLrH1nCYJsgfIc20vHwicu4Y/0?wx_fmt=jpeg)

# 28 个 AI 特工帮你打渗透测试，这工具要抢安全人的饭碗？

原创

杜明
杜明

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **导语**：安全研究员 0xSteph 近日在 GitHub 开源了一款名为 pentest-ai-agents 的工具包，将 Anthropic 的 Claude Code 打造成拥有 28 个专业子代理的渗透测试助手。从侦察、Web 应用到 Active Directory 攻击，从云安全到社会工程学，AI 特工们几乎覆盖了渗透测试的全生命周期。这事儿吧，得从两边儿看——红队兄弟可能要笑醒了，蓝队兄弟怕是要睡不着了。

---

## 一、事件概述

### 1.1 工具亮相

pentest-ai-agents 是一个开源工具包，由安全研究员 0xSteph 开发并发布在 GitHub 上。它的核心思路很清晰：**与其让一个通用 AI 模型啥都懂点但啥都不精，不如养一支"特工队"，每个成员都是某个领域的专家**。

这支特工队目前有 28 名成员（最新版本已扩展到 31 个），覆盖了渗透测试的方方面面：

* **侦察与 OSINT**：recon-advisor、osint-collector
* **Web 应用测试**：web-hunter、api-security、bug-bounty、bizlogic-hunter
* **Active Directory 攻击**：ad-attacker、credential-tester
* **云安全**：cloud-security、cicd-redteam
* **移动安全**：mobile-pentester、reverse-engineer
* **无线攻击**：wireless-pentester
* **社会工程学**：social-engineer、phishing-operator
* **漏洞利用链**：exploit-chainer、poc-validator
* **检测与防御**：detection-engineer、threat-modeler
* **报告生成**：engagement-planner、report-generator

![pentest-ai-agents 工具覆盖范围](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MSRwibgILf2M1TSnLEy33rQLevicFdZhougwZrhjUR128PDVRAPkvoPxoYAiamZyicia3McGCNczC11ImJzokxxCb6qxoGjxj49pOw/640?wx_fmt=png "pentest-ai-agents 工具覆盖范围")

### 1.2 安装方式

这工具的.install 脚本简单到让人怀疑人生：

```
curl -fsSL https://raw.githubusercontent.com/0xSteph/pentest-ai-agents/main/install.sh | bash
```

一行命令，完事。脚本会把 28 个代理文件复制到 `~/.claude/agents/` 目录下，无需服务器、无需外部依赖、无需复杂配置。而且支持幂等操作——重复运行也不会出问题，只会安全地更新现有代理。

对于有洁癖的师傅，还支持项目级部署（`--project`）和成本优化模式（`--global --lite`，用 Claude Haiku 跑顾问型代理，省 token）。

---

## 二、技术架构

### 2.1 双层执行模型

pentest-ai-agents 设计了一个挺有意思的安全机制：**双层执行模型（Two-Tier Execution Model）**。

**Tier 1（顾问模式）**：所有代理都支持这个模式。用户自己运行工具，把输出粘贴给 AI，AI 负责分析结果、给出优先级排序、推荐下一步操作。这种方式下，AI 只是个"军师"，动嘴不动手。

**Tier 2（执行模式）**：部分精选代理支持。用户声明授权范围后，AI 可以直接生成并执行命令，但 Claude Code 会在执行前显示每条命令，需要用户明确批准。支持 Tier 2 的代理包括：

| 代理 | 可执行工具 |
| --- | --- |
| Recon Advisor | nmap, dig, whois, curl, netcat, traceroute, whatweb, nikto |
| Vuln Scanner | nuclei, nikto, nmap NSE scripts |
| Web Hunter | ffuf, gobuster, feroxbuster, sqlmap, dalfox, whatweb |
| AD Attacker | BloodHound, Impacket, CrackMapExec, Certipy, ldapsearch |
| Exploit Chainer | 多步骤攻击链执行，每步需批准 |
| PoC Validator | 安全、非破坏性的概念验证脚本 |
| Business Logic Hunter | 逻辑漏洞测试（价格操纵、竞态条件等） |

这设计挺聪明——既给了自动化便利，又保留了人工把关，避免 AI 一激动把生产环境给"渗透"了。

### 2.2 持久化发现数据库

工具内置了一个 SQLite 支持的发现数据库（findings.sh），可以在多次 Claude Code 会话之间持久化保存渗透测试数据。这意味着什么？**你可以今天测一半，明天接着来，AI 记得你昨天发现了啥**。

Tier 2 代理会自动将发现写入数据库（前提是 findings.sh 在系统 PATH 中）。报告生成器代理可以基于这些数据生成专业的渗透测试报告，包括执行摘要、CVSS 评分和修复路线图。

### 2.3 本地模型支持

对于有数据隐私要求或者网络隔离的环境，工具提供了 `opencode-setup.sh` 脚本，可以将代理转换为 OpenCode 自定义命令，兼容 Ollama、LM Studio 或任何本地模型。

还有个配套的 MCP 服务器（pentest-ai），提供 150+ 工具封装、自主漏洞利用链和 CI/CD 管道集成，支持 Claude Desktop、Cursor 和 VS Code Copilot。

---

## 三、社区反响

### 3.1 期待派：AI 要统治渗透测试了？

HackerNews 上有位老哥预测得很直接：

> "从中期来看，代理平台基本上会在所有'常规化'的渗透测试任务上碾压未增强的人工测试团队——网络、Web、移动、代码审计都不例外。这项工作有太多方面天生就适合代理循环。"

另一位老哥更激进：

> "到 2027 年底，如果你做一个三角测试，2:1 的 AI/人类或者反过来，我觉得你根本区分不出来。"

支持这个观点的理由很充分：

1. **横向扩展能力**：人类渗透测试员受限于时间和注意力，AI 可以同时启动 1000 个子代理测试每个假设、每个 API 参数、每种注入可能
2. **不会疲劳**：人类在最佳状态可能比 AI 有 20% 的创造力优势，但 AI 能在整个测试过程中始终保持峰值表现
3. **自动化需求**：有人直言，"网络渗透测试还需要人类做大量工作，这本身就是自动化失败的证明"

### 3.2 怀疑派：别高兴太早

当然，也有冷静的声音。Reddit 上有安全从业者指出：

> "自动化渗透测试扫描器只能找到底部 10-20% 的漏洞，真正的渗透测试工程师不会认为它们有多厉害。AI 可能把这个数字提升到 40%-50%，它们真正擅长的是发现'信号'，让人类去调查。"

还有人担心模型厂商的政策风险：

> "好玩归好玩，直到 Anthropic 决定不允许你用他们的模型做渗透测试，然后封禁你的个人和企业访问权限。"

对此，0xSteph 在 Reddit 上回应说，他花了很多时间思考这个问题，专门设计了代理专注于**授权测试**，所有攻击行为都映射到 MITRE ATT&CK 框架，并配对防御上下文。

### 3.3 技术派的担忧

有经验丰富的安全专家指出了 AI 的短板：

> "AI 代理找不到绕过攻击，因为它们没有记忆。像 SSL Heartbleed 这类漏洞，需要理解 memset 或 malloc 的工作原理，或者需要利用泄漏函数创建特定偏移量——这些对 LLM 来说很难，因为它们容易忘记太多关于代码和程序的重要信息。"

不过也有人反驳说，记忆问题正在通过架构方式解决，比如使用结构化状态在迭代之间传递，而不是依赖模型的上下文窗口。

---

## 四、紫队视角：这事儿怎么看？

### 4.1 红队兄弟怎么看

红队兄弟估计已经笑醒了。想想看：

* 以前写报告要熬夜，现在 report-generator 代理帮你搞定执行摘要、CVSS 评分、修复建议
* 以前做侦察要手动跑一堆工具，现在 recon-advisor 自动分析 nmap 输出，告诉你哪个目标优先级最高
* 以前研究利用链要查一堆文档，现在 exploit-chainer 自动把低危发现串成完整攻击路径

一位红队师傅在社交媒体上说："这工具最爽的不是自动化，而是它真的懂行。每个代理都有深度领域知识，不是那种只会说'建议加强安全意识培训'的 AI 。"

### 4.2 蓝队兄弟怎么看

蓝队兄弟可能心情复杂。一方面，detection-engineer 代理可以帮你写 Sigma 规则、Splunk SPL、Elastic KQL 检测规则，还带误报调优；另一方面，ad-attacker 代理能把你的 AD 环境扒得底裤都不剩。

但话说回来，**最好的防守是知道攻击者怎么想**。pentest-ai-agents 的每个攻击代理都配对了防御上下文，这其实是在帮蓝队理解攻击者的思路。

有蓝队师傅在评论里说："我用这工具做内部评估，比等外部渗透测试快多了。每周跑一次，发现问题马上修，总比被真黑客找出来强。"

### 4.3 紫队想说啥

作为紫队视角的观察者，我觉得这事儿有几个关键点：

**第一，AI 不是取代，是增强**。pentest-ai-agents 的设计者很聪明，Tier 2 模式要求用户批准每条命令，这不是限制，是保护。AI 负责处理重复性、高并发的任务，人类负责判断、决策和创造性工作。

**第二，授权是底线**。工具文档里反复强调"authorized penetration testing"，所有攻击行为都应该在授权范围内使用。这不是套话，是法律红线。

**第三，攻防协作才是未来**。红队用这工具找漏洞，蓝队用这工具写检测规则，双方在同一个框架下对话，这本身就是紫队理念的体现。

---

## 五、使用建议

### 5.1 入门步骤

1. **安装**：一行命令搞定

   ```
   curl -fsSL https://raw.githubusercontent.com/0xSteph/pentest-ai-agents/main/install.sh | bash
   ```
2. **检查工具链**：运行 `db/doctor.sh` 看看你缺哪些底层工具（nmap、nuclei、sqlmap 等）
3. **安装工具**（可选）：

   ```
   ./install.sh --tools
   ```
4. **开始使用**：打开 Claude Code，直接描述任务

   ```
   "为 500 台终端的 AD 环境规划一次内部渗透测试，时间窗口 2 周"
   ```

### 5.2 注意事项

* **授权范围**：始终在授权范围内使用，Tier 2 模式会验证目标是否在声明的范围内
* **容器隔离**：建议在 Docker 容器中运行安全工具，保持工作站清洁，避免触发终端防护
* **成本优化**：可以使用 `--global --lite` 模式，用 Claude Haiku 跑顾问型代理，降低 token 消耗
* **本地部署**：敏感环境可以用 `opencode-setup.sh` 转换为本地模型

### 5.3 快速命令参考

| 命令 | 功能 |
| --- | --- |
| `/recommend "任务描述"` | 推荐合适的代理并给出具体命令 |
| `/agents-for web` | 列出所有与 Web 测试相关的代理 |
| `/agents-for cloud` | 列出云安全相关代理 |
| `findings.sh init <id>` | 初始化新的渗透测试项目 |
| `findings.sh stats` | 查看项目进度 |
| `findings.sh export` | 导出完整 JSON 数据 |
| `bash handoff.sh` | 生成 Markdown 交接报告 |

---

## 六、总结

pentest-ai-agents 的出现，标志着 AI 在渗透测试领域的应用进入了一个新阶段。它不是简单的"AI+ 安全工具"堆砌，而是真正理解了渗透测试的工作流程，用多代理架构模拟了一支专业团队。

这事儿吧，得从两边儿看：

**红队这波操作**：28 个专业代理覆盖全流程，一键安装，自动写报告，我给 85 分。剩下 15 分扣在——别太依赖 AI，基本功还得练。

**蓝队这招防守**：用同样的工具做内部评估，提前发现问题，检测规则直接让 AI 写，也挺香。

**紫队的建议**：攻守之道，在于平衡。AI 是工具，不是答案。最好的安全团队，是会用 AI 增强自己，而不是被 AI 取代思考的团队。

最后送大家一句话：**黑客和内防的战争，比美剧还精彩。现在，AI 也加入战局了。这出戏，越来越好看咯。**

---

## 参考资料

1. pentest-ai-agents GitHub 仓库：https://github.com/0xSteph/pentest-ai-agents[1]
2. Cybersecurity News 报道：https://cybersecuritynews.com/pentest-ai-agents-tool/[2]
3. HackerNews 讨论：https://news.ycombinator.com/item?id=46518996[3]
4. AI Pentesting Agents 2026 分析：https://appsecsanta.com/research/ai-pentesting-agents-2026[4]
5. 0xSteph 在 Reddit 的回应：https://www.reddit.com/r/cybersecurity/comments/1s6wu98/[5]

---

*本文从第三方视角分析 pentest-ai-agents 工具，旨在提供客观的技术评估和社区观点汇总。工具本身为开源项目，使用前请确保在授权范围内使用。*

### 引用链接

[1]*https://github.com/0xSteph/pentest-ai-agents*

[2]*https://cybersecuritynews.com/pentest-ai-agents-tool/*

[3]*https://news.ycombinator.com/item?id=46518996*

[4]*https://appsecsanta.com/research/ai-pentesting-agents-2026*

[5]*https://www.reddit.com/r/cybersecurity/comments/1s6wu98/*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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