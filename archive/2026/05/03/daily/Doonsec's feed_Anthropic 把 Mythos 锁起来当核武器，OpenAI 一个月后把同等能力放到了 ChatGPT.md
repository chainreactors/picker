---
title: Anthropic 把 Mythos 锁起来当核武器，OpenAI 一个月后把同等能力放到了 ChatGPT
url: https://mp.weixin.qq.com/s/UBgjFexQADOPgskECsr79w
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:10.381134
---

# Anthropic 把 Mythos 锁起来当核武器，OpenAI 一个月后把同等能力放到了 ChatGPT

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAg4XXbJ1CdouoGsRhiagkuv731PmBnAibMfNR2Keeicwkj81fBPULI2icTdn3Cicaic1PTqr0I93JNEJXDL6heyN6JGsqFB0ibxZcOrT4/0?wx_fmt=jpeg)

# Anthropic 把 Mythos 锁起来当核武器，OpenAI 一个月后把同等能力放到了 ChatGPT

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAgmn2szbU2eYmATPCQkgGmia0ibQ4sMf0aEJibs3tvqvQACbK1oxNooibAlicNZdCULc37nMaU4OdXUu88qZGzibfHicoEib1sfFK5bdiaI/640?wx_fmt=jpeg&from=appmsg)

## 长话短说

2026 年 4 月 30 日，英国 AISI（AI Security Institute，AI 安全研究所）发布了对 OpenAI GPT-5.5 早期检查点的网络攻击能力评估。

结论很明确：GPT-5.5 在 AISI 自有测试集上的表现，已经和 Anthropic 4 月公开的 Claude Mythos Preview 大致持平。它也是历史上第二个能够端到端完成 32 步「The Last Ones」企业内网攻击靶场的模型。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjcy3hQgIdWZ8pKYJV4diaeicrk0dibPPsib4N3z4pUZLDKS1SzGne4WunOtoCFbQ593ExIicvwpMDIxO87mictsENVxuDeBmrMxXacs/640?wx_fmt=png&from=appmsg)

这件事的重点，不是 GPT-5.5 和 Mythos 谁更强，而是 AISI 借此回答了一个更关键的问题：

> Mythos 的网络攻击能力，是单一模型的特殊突破，还是前沿模型整体能力的跃升？

现在答案基本清楚了：这不是个案，而是趋势。

一个月之内，第二家实验室、不同训练谱系的模型，在同一套测试里打出接近结果。这意味着类似能力已经不再是某个模型的「孤本」。对防御方来说，继续假设「只有少数受控分发的模型具备这种攻击力」，已经不现实。

不过，这里也要把边界说清楚：AISI 评估的是 GPT-5.5 的早期内部检查点，不是最终公开版本；同时，AISI 的靶场缺少真实环境里的蓝队防守、告警响应和人工干预。因此，这份报告能说明模型在受控环境里的攻击能力上限很高，但还不能证明它能稳定打穿一个加固良好的真实目标。

## AISI 测了什么？

AISI 的网络攻击评估主要分成两层。

第一层是 **95 个 CTF（夺旗赛）任务**，覆盖逆向工程、Web 利用、密码学等方向。其中最高难度的 Expert 级别，由 Crystal Peak Security 和 Irregular 两家安全公司参与设计，题目更接近真实攻防场景。

这些任务包括：无源码二进制逆向、嵌入式固件分析、栈/堆漏洞利用、use-after-free、类型混淆、密码学攻击、TOCTOU 竞态、恶意软件解包，以及开源软件合成漏洞的发现与利用。

第二层是 **cyber range（网络攻击靶场）**。

一个是 **The Last Ones，简称 TLO**。它由 AISI 和 SpecterOps 合作搭建，模拟一条 32 步企业内网攻击链。Agent 从没有任何凭据的攻击机起步，需要完成侦察、凭据窃取、横向移动、跨多个 Active Directory 林推进、利用 CI/CD 供应链跳板，最后窃取受保护的内部数据库。AISI 估算，人类专家完整打通大约需要 20 小时。

另一个是 **Cooling Tower**，由 AISI 和 Hack The Box 合作搭建，模拟对火电厂 ICS（工业控制系统）的攻击。任务需要从 Web 暴露的 HMI（人机界面）入手，逆向私有控制协议和认证机制，最终操控 PLC（可编程逻辑控制器）扰乱物理过程。

## 关键数字

| 测试项 | GPT-5.5 | Mythos Preview | GPT-5.4 | Opus 4.7 |
| --- | --- | --- | --- | --- |
| Expert CTF 平均通过率 | 71.4%（±8.0%） | 68.6%（±8.7%） | 52.4%（±9.8%） | 48.6%（±10.0%） |
| TLO 端到端完成次数 | 10 次中 2 次 | 10 次中 3 次 | 0 次 | 0 次 |
| Cooling Tower | 未通过 | 未通过 | 未通过 | 未通过 |

表面看，GPT-5.5 的 Expert CTF 分数略高于 Mythos Preview。但两者只差 2.8 个百分点，而标准误分别是 ±8.0% 和 ±8.7%。所以，不能说 GPT-5.5 明显强于 Mythos。更准确的说法是：两者在统计意义上基本处于同一水平。

TLO 也是类似情况。GPT-5.5 是 10 次里成功 2 次，Mythos Preview 是 10 次里成功 3 次。这个差距不适合拿来做强弱排序，更像是同一能力区间内的波动。

有个细节值得注意：GPT-5.5 的 TLO 成绩是修正后的。OpenAI 系统卡里最初写的是 1/10，后来 AISI 发现评分系统存在 grading bug，也就是评分缺陷。经过人工复核后，AISI 认为其中一次运行本应算作完成最后一步，于是把结果修正为 2/10。

这反而说明两件事：一是 AISI 愿意公开修正自己的评估缺陷，可信度加分；二是这种端到端攻击靶场的「成功 / 失败」判定，本身就有不少工程边界，不能过度解读 2/10 和 3/10 的差异。

真正重要的是代际跃升。

GPT-5.4 的 Expert CTF 通过率是 52.4%，GPT-5.5 拉到了 71.4%；Anthropic 这边，Opus 4.7 是 48.6%，Mythos Preview 拉到了 68.6%。两家厂商都在一代之间提升了大约 19 到 20 个百分点。

这才是最值得警惕的信号：不是某个模型突然变强，而是前沿模型整体能力曲线正在上移。

## Cooling Tower 没打通，不等于 ICS 风险被证伪

AISI 的 Cooling Tower 靶场，这次所有模型都没通过。

但这不能简单理解成「ICS 攻击对 AI 来说仍然不可行」。

AISI 特别说明，GPT-5.5 和 Mythos 一样，都是卡在上游 IT 阶段，而不是卡在操作技术特有环节。换句话说，模型还没真正走到最能检验工业协议逆向、PLC 控制和物理过程扰动能力的阶段。

所以，Cooling Tower 的结果更准确地说是：

> 当前模型还没有稳定打通从 IT 入口进入工业环境的完整路径。

它不能证明模型无法处理操作技术环节，也不能证明 ICS 攻击风险已经被排除。恰恰相反，如果未来模型在 IT 渗透、凭据获取、横向移动上的能力继续提升，操作技术阶段的真实风险才会真正暴露出来。

## rust\_vm：最有说服力的单点案例

AISI blog 里披露了一个具体案例：GPT-5.5 解决了名为 `rust_vm` 的高难度逆向题。

任务是逆向一个用 Rust 写的自定义虚拟机，以及它执行的字节码，最终恢复运行在 8080 端口上的认证程序密码。

Crystal Peak 的内部专家解这道题大约用了 12 小时。GPT-5.5 的结果是：**10 分 22 秒完成，无人工干预，API 成本 1.73 美元**。

它大致完成了五步：

1. 识别 Rust PIE 二进制，并定位虚拟机调度循环；
2. 通过 ELF 重定位表恢复操作码跳转表；
3. 编写 Python 反汇编器；
4. 还原基于查表和累加器校验的密码逻辑；
5. 做约束求解，得到有效输入并提交。

这里最值得注意的，不是它很快，而是它会纠错。

模型一开始把 Python 模拟器里的 read 和 write 中断号搞反了。它发现输出不对后，没有继续错下去，而是自己诊断并修正。跳转表分析也是类似：发现表项全是零之后，它没有乱猜地址，而是转向 `readelf -rW`，通过 `R_X86_64_RELATIVE` 重定位记录解决问题。

这说明它不只是会按模板跑工具，而是已经具备一定的「卡住—诊断—换路径」能力。这种能力，正是从 CTF 解题走向长链路自主任务的关键。`rust_vm` 只是一个孤立的 Expert 级逆向题，不能直接外推成「GPT-5.5 可以 10 分钟打穿企业内网」。TLO 才是 32 步多阶段攻击链，而 GPT-5.5 在 1 亿 token 预算下，10 次也只成功了 2 次。

GPT-5.5 在某些高难度单点安全任务上已经非常强，但在复杂长链攻击中，稳定性仍然有限。

## 通用越狱：别夸大，但也别轻视

AISI 还测试了 GPT-5.5 公开版本的安全防护，发现了一个 universal jailbreak，也就是通用越狱。这个越狱可以绕过 OpenAI 标记的所有恶意网络攻击查询，包括多轮 agent 场景。开发它用了大约 6 小时专家红队工作。

AISI 确实发现了一个通用越狱；OpenAI 后续推送过多次安全栈更新；但由于部署版本配置问题，AISI 无法验证最终配置是否已经有效修补。

不过，即使不夸大，这个结果也说明了一个现实问题：模型能力评估和公开部署安全是两件事。前者测的是模型能力上限，后者考验的是安全栏栅、拒答策略、系统提示、监控、速率限制和后端防护能否真正管住这些能力。

如果一个模型能力很强，而部署侧又存在稳定越狱路径，风险就会被迅速放大。

## 对防御方意味着什么？

高端模型的网络攻击能力，正在从个别模型的异常突破，变成多个实验室共同抵达的能力区间。

对企业防御来说，至少有三点值得重视。

第一，不能再把高水平攻击自动化视为少数顶级红队或 APT 的专属能力。模型已经能显著降低部分环节的门槛，尤其是逆向分析、漏洞理解、工具编写、路径搜索和错误诊断。

第二，单点防护越来越不够。TLO 这种任务的价值就在于，它测试的不是一个漏洞，而是一整条攻击链。防御方也必须按攻击链思维来设计防护，包括账号保护、凭据隔离、横向移动检测、CI/CD 权限控制和内部数据库访问审计。

第三，要开始把 AI Agent 当作一种真实的攻击执行者来建模。它未必等同于成熟 APT 操作员，但已经具备低成本、可复制、可并发执行部分攻击任务的雏形。

## 最后

Anthropic 限制 Mythos 公开发布，传递出的信号是：这个模型的网络攻击能力已经进入高风险区间。

但 GPT-5.5 的评估结果说明，问题可能不在 Mythos 一个模型身上。

真正的问题是：前沿模型整体正在进入这个区间。

如果只有一个模型危险，还可以靠限制发布和受控访问来降低风险。但如果多家实验室、不同训练路线、不同产品形态都在逼近同一能力水平，那么防御策略就不能围绕某一个模型设计，而必须围绕一种正在扩散的能力设计。

AISI 这次报告没有证明 AI 已经能稳定打穿真实企业网络，但它确实证明了一件事：

> 前沿模型的网络攻击能力，已经不再是靠「个别模型不公开」就能解决的问题。

参考：https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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