---
title: 自主渗透测试系统 -- PenAI
url: https://mp.weixin.qq.com/s/0RaXNLEbeK1ggDuNYd73xQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:53.864636
---

# 自主渗透测试系统 -- PenAI

# 自主渗透测试系统 -- PenAI

qiuxuewl
qiuxuewl

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**网盘下载链接（一定要在虚拟机运行）：**

```
后台回复：20261118获取下载链接，仅一天有效
```

PenAI 是一套 AI 自主渗透测试系统：Go 后端加 Next.js 前端，AGPL-3.0。planner 和一群 worker 在事件循环里跑，一个共享资产图记全局，每个任务再挂一张探索图。README 把能力写得很满——自主侦察、漏洞发现、利用链、Nuclei 扫描、实时资产图、MITM 代理和工具审批门。

这篇不写它怎么打。只看两件事：它用什么机制保证不会乱来，以及它自己在一次安全审计里被翻出了哪些问题。有意思的地方恰恰在后半段。

01

TWO GRAPHS

### 一份家底，一本任务账

它把记忆拆成两张图。一张是共享资产图，域名、IP、服务、端点都存在 assets 表里，跨任务可见；另一张是每任务探索图，节点带状态、优先级、来源和锚点，边只有五种关系：派生、意图链、产出、证明、覆盖。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQth0wN3gwCpw97DuwFKiayiaXN3cb1a5YeO0YyM07k6BmP7pZedglxwdXe8Uyg3lwVctj3UYvvwYhBkLVFC302zBLhQM1SZvz6VE/640?wx_fmt=png&from=appmsg)

— 探索链路：起点 → 目标 → 意图 → 事实 / 漏洞（仓库官方截图）

拆开的好处很实在：多个任务共享同一份资产底账，不用各自重扫一遍；但每个任务的推理路径、试错和结论都关在自己的图里，互不污染。worker 干完活就用 done、finding、goal 这类事件把 planner 叫醒，planner 再决定下一步。

代码量也说明这不是个 demo：533 个 Go 文件、约 13 万行，251 个测试文件；前端另有 187 个 ts/tsx 文件、约 5.6 万行。有意思的是它的 go.mod 至今仍叫github.com/Autumn-27/artex，入口也是 cmd/artex——从骨架到测试环境变量，都还带着 ARTEX 系的影子。

02

THREE BRAKES

### 刹车装了三道，默认踩住几道

第一道在提示词里。任务的操作约束被拼成一段最高优先级文本，压在探索启发式之前；写了「发现新目标不等于获得授权，越界事实只能记下、不得派生动作」这样的话。它管的是模型 intention，不是执行。

第二道在数据库里

每次工具调用过 PreToolUse 钩子，按优先级降序匹配拦截规则，首条命中生效，动作分 allow、deny、ask 三种。内置规则有三批：17 条破坏性命令（rm -rf、mkfs、dd、fork 炸弹、DROP、TRUNCATE 等）、2 条数据外泄管道（默认关）、以及一条后补的删除类接口路径规则。它们都是普通的内置行，可在「系统 → 命令拦截」里停用或删除。

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQsvSLLDsk8kZ6fSLNyrTUl3adXicGic2dpAmnYN3V2DtF3suG1cEFBBSp5dHZgr0C8VpA7Gq2rF5251FY3kXGxibeVVWhNcnkQC68/640?wx_fmt=png&from=appmsg)

— 拦截规则按优先级逐条匹配，首条命中即生效（仓库官方截图）

那条后补的规则挺能说明问题：原先的破坏性规则只认 DELETE 方法，可多数应用的删除接口用 GET 或 POST 就能触发，curl 'http://t/api/user/delete?id=1' 会真的删数据。补上的规则改看路径里的 /delete、/del、/remove 等，优先级 80，默认开，且刻意避开 /delivery、/details 这类词。

第三道交给另一个模型

规则拿不准时，可以交给「模型兜底审批」再判一次，独立计量、单独看 token 花了多少。但这道默认关闭，而且裁判超时或出错时是放行——代码里 15 秒超时、ask 300 秒后按 deny 处理，唯独裁判失败那一步选择的是「不拦」。要用它，得自己先把这个默认值翻过来。

03

EVIDENCE CHAIN

### 报告里的证据，得能倒查到原始报文

这是整个项目里工程味最重的一块。漏洞详情可以关联真实流量，用途分 baseline（正常对照）、proof（漏洞证明）、verification（补充验证）、supporting（辅助）四类；报告 Agent 拿到的是带版本号的证据快照，不是一句「我发现了一个漏洞」。

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQtDPBthE2oUibO2zI8KeI2xxicgYMIX86aXLDMCGvm3sSjOMGoaPT3DzSWvico3FOFuUu6PtS0LhZP9L8sprgejKJQdN764Qdwic0s/640?wx_fmt=png&from=appmsg)

— 跨任务漏洞汇总（仓库官方截图）

按内容哈希存，按版本锁写

证据正文不按原流量路径存，而是算 SHA-256、按哈希放到evidence/blobs/<前两位>/<hash>.bin。多个漏洞可以共享同一份快照，校验不一致就让读取和导出直接失败。生成报告时要带上读取到的evidence\_version，期间证据一变就拒绝旧版本写入。清理器每小时跑一次，只回收无引用且超过 24 小时的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQt2BUEQ284w6Q7jlC0PNhwUUNVJA7Tnao9gWF0ibyf0Vxx1R0uZYic6FrhX6mftAZk7pDxtlvKwniaCnWDR3R8Fiavkc0WENicpuxwI/640?wx_fmt=png&from=appmsg)

— MITM 代理全局录制，8788 端口（仓库官方截图）

写路径用 PostgreSQL advisory lock 7337741004 协调文件和 SQL 引用，先落盘校验、再用单个事务写入节点、漏洞、快照和绑定，提交后才通知规划者。导出 ZIP 前会读完所有条目的 CRC，缺一个就整体失败。这些细节不花哨，但决定了报告拿出去以后别人能不能复现。

有个细节值得单独说：文档明确写了「缺少录制记录或完整正文时不能补造证据」，也明确不按域名、时间、浏览记录去猜绑定。这是把「证据不能编」当硬规则钉在执行层，而不是当作一句倡议。

04

AUDITING ITSELF

### 一份把自家漏洞写全的更新日志

CHANGELOG 里 0.3.15 那节「漏洞推送」，修复列表前写着一句话：本节是功能初版完成后一轮安全审计的结论，每条都先复现、再修、再补回归测试。然后老老实实列了十几条。

NOTE

配置合并对「未提及的键」一律保留原值，于是只改目标地址、对凭据避而不谈，就能让服务端把库里的真凭据发到任意地址，且完全静默。修复方式是：目标地址一变，每个凭据字段都必须显式表态。

同批修掉的还有：漏洞标题和资产 URL 来自模型与扫描结果，构造标题能在钉钉、飞书、企业微信里渲染成可点击外链，图片语法会让客户端拉取并泄露阅读者 IP；投递地址的 SSRF 面能配合失败响应体回显形成半盲读，改在拨号阶段设防才挡住 DNS 重绑定；token、key 这些凭据在 URL 里，失败时会流进四处日志和提示，现在统一脱敏。

还有几条是「静默失效」类的：最低级别写成 hgih 时判定退化成恒真，用户以为只收高危、实际全收；rate\_per\_min=0 被写库层悄悄改回默认值，以为放开了限流其实还卡着；汇总消息被截断的漏洞既不在消息里也不在失败列表里，投递历史却显示成功。这些 bug 不会报错，只会让人误以为系统按自己想的方式在工作。

「一个专门找别人漏洞的工具，肯花一轮篇幅写自己哪里不严谨，比多列五个功能点更值钱。」

05

FINE PRINT

### 用之前，这几行小字要看

最该说清楚的一条：硬授权范围校验已被移除。guard 包的注释直接写着，RoE authorization-scope mechanism was removed，将来可能再加。现在约束主要靠提示词和数据库规则；资产读取有按任务 scope 过滤的门，但给一个任意目标 URL，并没有代码级的授权校验。README 末尾那句「仅供授权测试」，目前就是一句声明。

也就是说：边界得由使用它的人自己先划好，系统不会替你划。

几处口径也对不上。README 标 v0.3.16-nuclei，CHANGELOG 最新条目停在 0.3.15，仓库里一个 git tag 都没有；Nuclei 技能写「模板库每日更新」，但仓库内没有对应的定时更新实现，只有 release 工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQtm0ztT4cqgqxmYJIBjw1ScugwIbbfDS7L1Eubuv0Z9haqhGEqH62k1SNrJDV0ZPxGOKFicIBAcxzm9unZyXZOuIhO4XV6aPkSw/640?wx_fmt=png&from=appmsg)

— 全 Agent 共享的 LLM Profile：格式、模型、Base URL、代理（仓库官方截图）

默认监听是 :8787，全网卡；流量代理绑在 127.0.0.1:8788。JWT 密钥首次随机生成、TTL 七天，认证本身是有的，但别把默认地址直接暴露到公网。LLM 那边支持 Anthropic、OpenAI、OpenAI Responses 三种格式，带按优先级故障转移和熔断——这部分做得扎实，需要配 API Key 才能跑。

还有一个资源上的现实：这是 PostgreSQL + LLM 的整套服务，本机不具备运行环境，所以这篇是对着源码、文档和仓库自带截图写的工程分析，没有实跑的端到端验证。图是仓库官方 Demo 截图，不是我实测的输出。

∞

THE END

### 真正值钱的不是它会自动打，而是它知道证据不能编

把双图、三道刹车、哈希证据链和那份自审清单放在一起看，PenAI 最值得记的不是「自主」两个字，而是它反复在回答一个问题：做了什么，凭什么说，谁来决定停。探索图回答第一问，证据版本回答第二问，拦截规则和人回答第三问。

至于硬授权校验被移除这件事，就留在小字里：工具再严谨，边界最终还是使用者的责任。用来做授权测试，它是个能讲清楚来龙去脉的工程样本；不划范围就上手，再多的刹车也帮不上忙。

END

**网盘下载链接（一定要在虚拟机运行）：**

```
后台回复：20261118获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U7LDNXUGXQub3KK5tkrM7OBFenR17licS1hcib5YKjkC6pI9V89ZUWDfJeTzfNHZt579zZ7ia2jyXSUfbC31A6ic6lkuIRRwp3DricYOB9qPOk0Y/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过