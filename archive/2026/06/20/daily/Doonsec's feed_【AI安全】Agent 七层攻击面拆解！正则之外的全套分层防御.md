---
title: 【AI安全】Agent 七层攻击面拆解！正则之外的全套分层防御
url: https://mp.weixin.qq.com/s/VWbKS9fWCPFXolGFR_jq8Q
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:49:38.991094
---

# 【AI安全】Agent 七层攻击面拆解！正则之外的全套分层防御

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHQf3ze1iay3sGtXzRqXzyVpDl8icWgAx56SZX4hIpOvxL3ym6gO842TKLfW45JckLW9BPMkt2OHXXCsJtKAyozibqkVues13pJTxw/0?wx_fmt=jpeg)

# 【AI安全】Agent 七层攻击面拆解！正则之外的全套分层防御

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、Agent安全为什么不是加个正则

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

Agent 安全正在从“提示词安全”变成“运行时安全”。过去我们担心的是模型会不会被一句 `ignore previous instructions` 带偏；现在更现实的问题是：Agent 会读文件、调工具、跑命令、访问网络、委派子任务，还可能把第三方 Skill、MCP 服务和供应链包接进同一个工作流。⚠️

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHSkclxHtmcRvcpicia5PCbGOmP32As57CiaYmU6mtDUoVwjRjUfMoJtLyskhSR3SFhVqBdLPfkkwJFCrwObgibiaA6V7xt1CPKoltYw/640?wx_fmt=png&from=appmsg)

这意味着攻击面不再只在输入框里。**只要某段信息能进入 Agent 的上下文，或者某个工具能被 Agent 调用，它就可能成为攻击路径的一部分。** 原资料把攻击面拆成 7 层、43 类向量，这个拆法很有价值，因为它把“模型会不会听话”这个模糊问题，拆成了工程上可以逐层检查的问题。

一个典型误区是：看到 Prompt 注入，就想用正则封住危险句式。正则当然有用，尤其对字面注入、危险命令、路径穿越这类模式明确的攻击。但 Agent 的麻烦在于，很多风险不是“字符串长得像攻击”，而是“语义上改变了目标”。比如：

* 🧠 用户输入可以要求模型忽略规则，也可以用同义表达绕过字面规则。
* 🛠 工具结果可以夹带指令，让模型把“不可信输出”误当成新的任务。
* 📦 Skill、MCP、依赖包可以在安装、描述、参数或返回值里影响 Agent。
* 🔑 进程内凭据、共享 API key、环境变量很难靠提示词隔离。
* 🔁 循环、递归委派、上下文膨胀会把安全问题变成资源问题。

**Agent 的智能来自不确定性，Agent 的不安全也来自同一个来源。** 如果把所有不确定性都消掉，Agent 就只剩传统脚本；如果完全放开，Agent 又会把“理解能力”带来的误判、越权和幻觉一起放大。

原资料里最值得抓住的结论，是这三条行动指南：

| 判断点 | 不推荐的做法 | 更稳的做法 |
| --- | --- | --- |
| 工具暴露 | 先给全量工具，再靠规则拦截 | 先裁剪工具，不需要的能力直接不给 |
| 弱防御区 | 指望模型自律兜底 | 用 OS 隔离、权限系统和最小权限兜底 |
| 性能取舍 | 所有操作全量扫描 | 按信任等级和后果严重度选择检查层级 |

这里的关键不是“哪一层最强”，而是**不能把任何单层防御当成安全边界**。提示词不是边界，正则不是边界，AST 也不是天然边界。真正能接近边界的，通常是权限、隔离、预算、文件系统和网络策略这些 Agent 进程之外或半进程之外的控制点。🧱

所以，Agent 安全的第一步不是买一个“万能扫描器”，而是把问题画清楚：哪些输入能进上下文？哪些工具能改变外部状态？哪些凭据能被同一进程读到？哪些动作必须 fail-closed？哪些错误可以修复后继续？这张图不画出来，后面的安全建设很容易变成“补丁堆叠”。

# 二、7层攻击面：风险不是从一个入口进来的

原资料把 Agent 攻击面拆成输入层、执行层、数据层、系统层、子 Agent 层、供应链层、资源层和模型层。严格说这里有 8 个观察维度，但前 7 个更偏工程边界，模型层更像贯穿其中的根因。📌

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHSagmt4EepBnWZY3Vl3KBMgicUsLgUYIPia4syEUn1LicvdylLRR5s9WaK0tOO7h9RYnwQs1BbZYpCPDWEZLIshBUZCwickZNXBsXM/640?wx_fmt=png&from=appmsg)

为了更容易理解，可以把它看成一栋办公楼：输入层是前台，执行层是员工电脑，数据层是档案室，系统层是机房，子 Agent 是外包团队，供应链是快递和装修队，资源层是电力和工时，模型层则是每个人的判断力。

**攻击者不一定要从正门进来。** 他可以递一张带指令的纸条，可以让员工运行一条命令，可以把恶意配置塞进外包团队的工作说明，也可以让系统陷入无限循环，消耗掉预算和上下文。

几个高频风险可以这样归类：

| 层面 | 典型风险 | 防御难点 | 更可靠的控制 |
| --- | --- | --- | --- |
| 输入层 I | 字面注入、语义注入、上下文文件注入 | 字面好拦，语义难拦 | 不可信标签、来源隔离、敏感动作二次确认 |
| 执行层 E | 命令注入、Shell 变体、ReDoS | Shell 语法复杂，变体多 | AST、白名单、超时、权限分级 |
| 数据层 D | SSRF、凭据读取、数据外泄 | 同进程天然共享信任域 | 网络 denylist、凭据隔离、容器化 |
| 系统层 S | 关键文件写入、配置篡改 | 一次写入可能长期驻留 | 黑名单、只读挂载、审计 |
| 子 Agent A | 递归委派、共享凭据、角色退化 | 委派链路扩大上下文 | 深度限制、能力裁剪、输出过滤 |
| 供应链 C | Skill/MCP/依赖包污染 | 描述和代码都可能带毒 | 签名验证、信任分级、安装前扫描 |
| 资源层 R | 无限循环、预算耗尽、上下文膨胀 | 不一定是恶意，也可能是失控 | 迭代预算、断路器、优雅终止 |
| 模型层 M | 幻觉参数、对抗性操控 | 概率系统没有绝对保证 | 参数校验、修复链、隔离兜底 |

这张表说明一个很实际的事实：**Prompt 注入只是入口之一，不是 Agent 安全的全部。** 对企业来说，更危险的往往是“输入影响执行”，也就是一段不可信文本最终触发了写文件、跑命令、读凭据或访问内网。

例如，输入层的字面注入可以靠 9 类正则模式获得不错覆盖；但语义注入换一种说法，字面规则就容易失效。执行层的 AST 能覆盖多种命令结构，可 Shell 生态里还有 Zsh、IFS、进程替换、环境变量扩展等特殊语法。数据层的 SSRF 可以通过阻断私有 IP、链路本地地址、CGNAT、Tailscale 地址来做硬防御；但进程内凭据读取，只要凭据和 Agent 在同一信任域，靠模型自律就不现实。🔍

**最弱的地方往往不是没有规则，而是规则所在的位置太靠后。** 如果危险能力已经暴露给 Agent，再用提示词告诉它“不要滥用”，这就像把钥匙交出去以后再贴一张纸条：请勿开门。

更好的顺序是：

1. 🧩 先决定 Agent 到底需要哪些工具。
2. 🔐 再给工具设置权限和动作分级。
3. 🧪 对高风险动作做确定性扫描。
4. 🧯 对扫描不到的语义风险，用隔离和审计兜底。
5. 📉 对资源失控，用预算、超时和断路器处理。

这也是为什么“工具裁剪”比“万能检测”更优先。**50 行白名单有时比 10000 行扫描规则更安全，因为它直接减少了可被滥用的能力。**

# 三、8层防御：真正有效的是叠加，不是神话

**🎯【8层防御：真正有效的是叠加，不是神话】**

这一节真正关键的不是「8层防御：真正有效的是叠加，不是神话」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「8层防御：真正有效的是叠加，不是神话」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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