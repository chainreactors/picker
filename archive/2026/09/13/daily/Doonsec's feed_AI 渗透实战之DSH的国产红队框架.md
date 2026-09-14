---
title: AI 渗透实战之DSH的国产红队框架
url: https://mp.weixin.qq.com/s/PGYExE8wU_LbhQAd4En_lg
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:03.668210
---

# AI 渗透实战之DSH的国产红队框架

# AI 渗透实战之DSH的国产红队框架

原创

智能化态势感知
智能化态势感知

智能化态势感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/wAz56BweAib5uGEIjxwJmIic1tFeyTYLQxxicic1o6M8DMxQEEo4MgqKfZFolyWTQmbPaX5wUsiaf3HjicEPicxmUbTaSSQrKV42Ub61pP5GtKicHOE/640?wx_fmt=png&from=appmsg)

AI 从来不缺知识。问它一个漏洞原理，它讲得比大多数人清楚；丢个 CVE 编号过去，它能把影响面、利用链、修复建议一条条捋明白。单论「懂」，它比谁都懂。

但只要让它真的上手干一件活，它就开始原地打转——反复读同一个文件、来回试同一条命令、token 哗哗地烧，最后给出一个看着挺像那么回事、其实根本站不住脚的结论。

问题不出在模型身上。根源在于：只给它喂了知识，却没给它规矩。

dsh-redteam-model 就是冲着这个问题来的——它把红队日常要干的活，拆成 10 个工作模式 + 17 个运行时插件，挂在 DeepSeek Harness 上。同样的任务，它会自己拆解步骤、会卡阶段门、会把每一步的证据落盘。

项目目前 418 Star、33 Fork、MIT 协议、全自包含离线可部署。这篇一次讲透：它凭什么这么设计、能干什么、怎么装、怎么用。

|  |
| --- |
| 📌  01  项目介绍 |
| 一句话定位 / 设计理念 / 覆盖范围 |

一句话说清楚

这是一个基于 DeepSeek Harness（下称 dsh） 实现的红队安全研究框架，把最常用的工作场景拆成 10 个模式预设 和 17 个运行时插件，自包含、可离线部署，面向已获授权的安全研究——渗透测试、红队评估、代码审计等。

很多人在用 AI 做安全时会撞上同一堵墙：模型什么都懂，但干不成活。

AI 环境下知识点很多、知识面也很广。如果只是一味地给 AI 投递 knowledge，你问它，它能答得出来；但让它去完成一个任务，而没有规定这个任务如何去完成、如何高效完成、如何命中需要的点——尽管它掌握着大量知识，但没有那个「workflow」去引导、去把控，也许能得到想要的结果，但往往非常浪费 token，甚至在某些方面没有栅栏，它就可能一头扎进死胡同。

换句话说，它要解决的是很具体的一件事：让 AI 在没有护栏的地方有护栏，在该收口的地方收口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib7oDZ04ZZcfH6ia0Y0bOetEwLGexQvbzaGZ582oTBqAKZ6VjE4XicF2e45ZqREXqiavicUjiblR9ia3ia0vj2H4nv8U4ncJ4pP9VibBc84/640?wx_fmt=png)

为什么底座是 DeepSeek Harness

需要先说明的是：dsh 在安全工作这方面的设计其实有限，只能从 playbook 里去设计，插件的载体终归还是 harness 本身。

之所以仍然选它，是因为 harness 有个别的方案比不了的优势——在「反拒绝」这件事上，harness 相比 Claude 原生的 hook、Codex 原生的 hook，又或者其他三方智能体带来的封号风险，要 easy 太多。

覆盖领域

十个模式各自盯一个方向，基本把红队日常要干的活都铺开了：

| 领域 | 说明 |
| --- | --- |
| 渗透测试 | Web / API / App / 小程序等专业级渗透 |
| 红队评估 | Web 打点 + 内网环境（Windows / Linux / 域 / 云内网多场景） |
| 代码审计 | 白盒源码审计，动静态结合 |
| 二进制分析 | 病毒分析、逆向破解、脱壳还原 |
| 免杀对抗 | 攻击视角的 shell / loader / C2 变形 |
| 应急溯源 | Windows / Linux 应急响应与攻击溯源 |
| 云安全攻防 | 云平台与云原生渗透 |
| CTF 解题 | 题面登记 → 模块路由 → 解题循环 → flag 台账 |
| 资产测绘 | FOFA/Hunter/Quake 等多源测绘，产出可审计清册 |

|  |
| --- |
| ⚡  02  核心设计 |
| 十模式架构 × 十七插件 × 双层防线 |

  1. 十个模式：一个模式就是一个专家

每个模式不是换个提示词那么简单，而是按 dsh 的模式设计论自包含四层资产：

| 层级 | 内容 | 作用 |
| --- | --- | --- |
| persona | 角色 / 认识论 / 边界 / 报告纪律 | 定住「是谁、什么不做」 |
| playbook | 方法论与门禁文本契约 | 定住「活怎么干、卡在哪一步」 |
| skills | 可加载技能 | 定住「手上有什么家伙」 |
| refs/ | 外部知识库，原文索引化 | 定住「依据从哪来」 |

十个模式分别是：redteam（通用）、pentest（渗透测试）、code-audit（代码审计）、binary-analysis（二进制分析）、attack-defense（攻防评估）、av-evasion（免杀对抗）、

incident-response（应急溯源）、cloud-security（云安全攻防）、ctf-solver（CTF 解题）、asset-mapping（资产测绘）。

|  |
| --- |
| 💡 一个刻意的设计  通用模式 redteam 里并没有定义 Gate 强制链路，日常问题随便问；  但深度任务一定要切专业模式——专业模式才是这个项目的初衷。 |

  2. 十七个插件：给模式装上「护栏」

模式是纸面纪律，插件才是运行时强制。其中最有代表性的几个：

| 插件 | 干的事 |
| --- | --- |
| dsh-stage-gate | 八模式 32 道阶段门的结构校验，判定写入 gate-log.md |
| dsh-route-boost | 逐轮治理信封：阶段推断 + 门禁清单 + 证据等级预判 + 预算记账 |
| dsh-sec-enforce | 确定性工具拦截：报告门、写边界、高危命令先问后做 |
| dsh-refusal-guard | 反拒绝兜底 |
| dsh-trace-vault | 全量落库工具调用，可检索、可出会话画像 |
| dsh-attack-atlas | 攻击面图谱：架构矩阵四态点亮、目标锚定、自定义工作方法论 |
| dsh-scanner-tools | 本机扫描器封装，六节点工具调用阶梯 + 防盲打登记 |
| dsh-campaign-memory | 跨会话打法沉淀，热度 × 时间衰减排序，按工作区隔离 |

  3. 最值钱的部分：双层防线

这个项目最值钱的地方，是它的边界不靠「提示模型自觉」，而是靠两层防线叠加：

● 文本纪律（persona / playbook）——管住「打算怎么做」；

● 运行时强制（插件）——管住「实际做了什么」。

在这个框架下，有几条规则是被焊死了的：

| 硬规则 | 含义 |
| --- | --- |
| 模型不能自评门禁 | 结构校验必须是工具调用，不能「我觉得我过了」 |
| 语义门禁归独立复核员 | 自己判自己不算数 |
| 关键发现双签 | dsh 复核 + claude/codex 复核一致，才能进报告 |
| 一切判定落审计 | gate-log / enforce-log / evidence-index 全程可追溯 |

一句话概括：它不只让 AI 更强，还让 AI 的行为「可被检查」。在安全这个行当里，这比多几个功能重要得多。

|  |
| --- |
| 🎯  03  使用场景 |
| 五类场景，装上就能上手 |

❖ 场景一：Web 渗透测试全流程

Web / API / App / 小程序的目标，切 pentest 模式。模式里内置了专业级渗透方法论与门禁链路，配合 dsh-scanner-tools 把本机扫描器串成阶梯调用，再用 dsh-hunter 做资产测绘与「实测」验证。

适合：渗透测试工程师、乙方红队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib5jrW5UDvqoeDFndll71HNgvxoK0icNb47OIZKgNoUzHnJljohDQFcOYico9oHcUcGJl9fTShYSLVJ4VajgPKmn2L6pFYfnu4Qnk/640?wx_fmt=png)

❖ 场景二：白盒代码审计

切 code-audit 模式，联合 dsh-semgrep-audit 的 semgrep 封装与预设离线规则集自动定位。命中结果双写对账（scan-reconcile.md / .csv）——命中不等于漏洞，要复核补链后才升格。

适合：甲方安全、SDL 团队、外包审计

❖ 场景三：应急响应与攻击溯源

Windows / Linux 双场景，切 incident-response 模式。挖矿、蠕虫、木马攻防下的排查都有对应玩法。建议在 prompt 里把所处场景描述清楚，模型的路由判断会准得多。

适合：蓝队、SOC 值守、应急响应组

❖ 场景四：CTF 竞赛解题

切 ctf-solver 模式，流程被固定成：题面登记 → 模块路由（web/pwn/reverse/crypto/misc）→ 解题循环 → flag 台账 → 复盘。比赛里最怕「解到一半忘记试过什么」，这套台账正好治这个。

适合：CTF 战队、安全专业学生

❖ 场景五：资产测绘与清册

切 asset-mapping 模式，整合 FOFA / Hunter / Quake / ZoomEye / Shodan 五源 + 子域/DNS 校验 + ICP 备案归属 + 指纹识别，最终产出可审计的资产清册 Excel（六工作表）。

适合：甲方资产管理、攻防演练前期踩点

|  |
| --- |
| 🚀  04  部署教程 |
| 从零到跑通，保姆级 |
| ⏱ 环境要求  前置：Node.js >= 22（dsh 本身的要求）；无需预装 pnpm / dsh，经 npx 拉起；bash / python 非必需。  顺序：这是给 dsh「赋能」的项目，必须先装好 deepseek-harness，再装本项目。 |

  第一步：装好 DeepSeek Harness

先确保本机 dsh web 版本 >= 0.1.0-rc.6（项目验证于 0.1.1-rc.2）。dsh 本体是「Everything is a Plugin」的设计，本项目就是挂在它上面的一套插件合集。

  第二步：两种安装方式选一个

❖ 方式一：设置页管理台（推荐）

把整个合集作为一个 dsh 插件安装：

|  |
| --- |
| dsh plugin --profile web add github:SeaOf0/dsh-redteam-model |

装完打开 dsh web 设置页 → Redteam Manager，就能：

● 一键部署十个安全模式（空目录用整体链接；已有实体 .agent-presets 时写入管理器持有的实体副本）

● 安装 / 更新 / 卸载十七个运行时插件

● 查看操作进度与失败原因，最近 50 条记录按 profile 保留

模式复制状态刷新页面即可更新；宿主平面插件安装 / 卸载以及管理器自身更新后，需要重启 dsh web 才生效。

  第三步：如果第二步报错直接把链接给workbuddy，链接获取方式在下文

|  |
| --- |
| 💬  05  写在最后 |
| AI 安全的下一步往哪走 |

AI 安全这件事，走到今天已经很清楚了：

拼的不再是「谁的知识库更大」，而是「谁的 workflow 更靠谱」。

给模型投知识，它能答；给模型投 workflow，它才能干活。dsh-redteam-model 真正回答的是一个很多人没想清楚的问题——当你把危险的能力交给 AI 时，你靠什么保证它不乱来？

它给出的答案是：文本纪律 + 运行时强制，双层防线，一切判定落审计。这个思路，值得所有在做 AI Agent 的人抄一遍。

需要提醒的是：本项目面向已获授权的安全测试、CTF 与漏洞赏金场景，使用前请确保已取得书面授权。

|  |
| --- |
| 📮 资料获取  完整部署脚本、模式预设文件、十七个插件的清单说明都在源链接。  需要的话关注后在公众号后台留言【DSH红队框架】，即可领取。 |

|  |
| --- |
| 如果对你有用的话点赞+推荐+关注三连一下吧  持续更新 AI  网络安全实战拆解：本地化、离线化、自动化的下一步 |

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib6pja6TlWh8CL72mheGVw2a8iarW891tdOcXZzHJ1CgtJcnkom7NfYJzaj7MDUkBHeOEWz4kiaLOjL2jOf0PiccEU3wNoxEvqZ0u0/0?wx_fmt=png)

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