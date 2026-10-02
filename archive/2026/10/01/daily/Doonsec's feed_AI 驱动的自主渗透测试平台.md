---
title: AI 驱动的自主渗透测试平台
url: https://mp.weixin.qq.com/s/7eBVKdVn8-dWj7EXa859XQ
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:44:09.283902
---

# AI 驱动的自主渗透测试平台

# AI 驱动的自主渗透测试平台

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 介绍

## 它不是漏扫，而是一个"手动化"的渗透测试 agent

传统漏扫器只会跑 CVE 指纹和已知 payload。Dhunter 让一个（未来多个）**LLM agent** 驱动一套精选工具，像真人渗透测试员那样思考与行动：

* 先做**侦察**（子域 / JS / 指纹 / 历史 URL），把攻击面摸清；
* 再**规划**攻击意图，一个黑板（blackboard）协调多个 worker **并行探索**；
* 每个结论都要**先验证再上报**——SRC 验收门禁会机械重放你的 PoC，时变噪声会被自动驳回；
* 最终把确认的漏洞汇总成一份 **Markdown 报告**。

## 真实效果

下面这张攻击链图来自一次真实的授权测试（Typecho 博客靶场）：agent 自主构建了 49 条事实、7 个攻击意图，把 `.git` 暴露、XML-RPC SSRF、install.php 等发现串成完整的攻击链。

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ibAnWVv8MO2WhbmqXFaFIiafUvLt6ymd8W5kEOC0V4dAbAYSkKm0pOGsHqRLQkwhl0bjic5absg8JL5Hl7MibbcTlrS9X70nN7Dqk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0) *攻击链图：agent 自主构建的事实 → 意图 → 发现网络，实时可视化*

平台主界面与核心功能：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ibBOG7tibiccncXScNThG44yEAia3oGiae084GXbfXxLUsczLEt0T5icKvU6hjibcvB1iaxx9JqNUnqpTqk1IKibEH2X0onBvQlj89SJaw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic68ibYfGGQh9hGoWP5Aib5KOH6cyZCZBibT86WibSYux0SWUSOZT88gQLibiabnnicHgwh4U9noJMoxtcYzibg0XSCBEqibKIy7zuLHawTLk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

## 核心特性

| 特性 | 说明 |
| --- | --- |
| 🧠 **黑板引擎** | facts/intents/hints 持久化到 SQLite，planner 提出意图 → 多 worker 并行探索 → 收敛，纯 stigmergy 协调 |
| 🔍 **手动化侦察** | 子域枚举、JS 资产与凭据分析、历史 URL、技术指纹，20+ 内置工具随平台启动 |
| ⚔️ **主动测试** | HTTP 手工探测、参数 fuzz、认证绕过、信息泄露路径、业务逻辑测试，agent 自主选工具 |
| 🛡️ **SRC 验收门禁** | verifier 对每条漏洞做**机械重放 + 稳定性检查**：同一 PoC 两次结果不一致 = 时变噪声 → 自动驳回，杜绝误报 |
| 🎯 **漏洞优先验证** | worker 每落地一条漏洞立即触发 verifier 机械重放验证，不用等扫描结束 |
| 🔌 **MCP 扩展中心** | 把你自己的 MCP server 接进来，工具以 `<server>::<tool>` 命名空间暴露，UI 一键增删测 + 同步到 agent |
| 🧰 **库 / Skills / 模板** | 一级菜单「库」聚合 MCP / Skills / 模板三类可复用资产，3 个内置 skill 种子可基于此创建自定义副本 |
| 🧵 **每项目并发设置** | 创建目标时可指定并发 worker 数，深挖大目标时加大并发、小目标降速省 token |
| ⏸️ **运行暂停/恢复** | 随时暂停 run（保留已发现的黑板），之后一键「继续」从断点恢复 |
| 📦 **项目一键导出** | 目标卡上「导出报告」一键打包该项目全部漏洞为 Markdown（含 PoC/复现/证据） |
| ⚡ **实时思考流** | SSE 实时推送 agent 的思考、工具调用、工具结果，整个过程透明可见；命名空间工具带 EXTERNAL 标签 |
| 📄 **一键报告** | 每次运行导出 Markdown 报告（v0.6.0 起 PoC 块带 verifier 机械复现记录 + curl 复现命令） |
| 🔐 **首启自动账号** | 首次运行自动生成管理账号（用户名 + 随机密码），横幅展示，之后可在设置页修改 |
| 💻 **跨平台** | macOS / Linux / Windows 三平台启动脚本，Go 纯静态二进制（无 CGO） |

项目地址

https://github.com/Dest1ny-Sec/dhunter

内容转自HACK之道，侵删

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套***【2026最新网安资料】***网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！

Web安全👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

渗透测试👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全面试题👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFgrmaDLaYT1yV5lst9tKC72QrYjd5I8IN7kcOZIZSfQJJz8MdX6a1uA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码审计👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFxmUkTNP1iagssZL5zkjID8hibpZsRCj1OnEb4x7ZYWqpiaymSjc8O7vSQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

红队笔记👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVZS1mB4MKAo4FoMBGyVSzq38ZXEKJCjZVaTsFtLE7tIJ3zbRWF5xeA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

入门视频👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgxtiaXGtk7loXV41e8AXiaORJMhqFbrtcfHvJWTia6ME2oSI9msVYJu79uCicb7foufuibEHaVg32XnWw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

以上所有资料获取请扫码

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

识别上方二维码

备注：***2026安全合集***

100%免费领取

（是扫码领取，不是在公众号后台回复，别看错了哦）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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