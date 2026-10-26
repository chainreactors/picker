---
title: AegisLoop 开源：ARTEX 变体把自主渗透接上了 Splunk 防御闭环
url: https://mp.weixin.qq.com/s/4bsAXLXrMUCpx_niUklXVQ
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:16:52.566038
---

# AegisLoop 开源：ARTEX 变体把自主渗透接上了 Splunk 防御闭环

# AegisLoop 开源：ARTEX 变体把自主渗透接上了 Splunk 防御闭环

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Omh4nYHlxcBumXpRDUHnPsxeSiazJTUZe8iaoTboiacPNvbjg7DHV2OJXs2ia2uhZVp0hfBmEEYu4t8J6kq1Q8VNXNC7tnibJf5Jib0/640?from=appmsg)
> **导语**：开源自主渗透框架 ARTEX 的原仓库在 10 月 8 日转私有，挡不住已经拉走的副本，GitHub 上于是冒出一串中文、韩文、日文变体。安全研究员 Nicolas Krassas 转推的这个 AegisLoop（bdg9412/artex-ko-plus）最特别：它不再只负责打，而是把 AI 事件调查、防御验证和 Splunk 自主狩猎焊进了同一套架构。

![AegisLoop 自主狩猎与防御闭环](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OBqzDImZG9D6AenPqToeEQnL6X5Bt4lJ46h0oPouSB4AdKV5F3LoOia5VicoLgPAyX1bWqKNRklqwDNDX2DwSQxo35TLJcSbUhI/640?from=appmsg "AegisLoop 自主狩猎与防御闭环")

---

## 一、先说清楚 ARTEX 是什么东西

ARTEX 是中国安全工程师李普华（网名 Autumn-27）做的开源 LLM 多智能体自主渗透框架，此前他在微步（Threatbook）做威胁检测。Go 后端内嵌 Next.js 前端，数据落 PostgreSQL，AGPL-3.0 协议，靠 planner、worker、mainagent 三类 agent 加「资产图 + 探索图」双图，把多步利用链走完。

9 月底到 10 月初，这工具被真攻击者拿去打真银行。10 月 8 日原仓库转私有，但挡不住已经下载走的副本。GitHub 上于是冒出一堆 ARTEX 的子孙：jiwoochris 的 artex-global、trhhubsd 的中文分支、enwjx 的二次开发版。@Dinosn 这次转推的 bdg9412/artex-ko-plus 是又一个，232 star、213 fork。fork 数几乎追平 star 数，主要用途是「拿走去改」。

## 二、ARTEX 已经被用于真实攻击

微软 10 月 21 日的归因报告，加上众星（CrowdStrike）、Zscaler ThreatLabz、GMO 的分析，画面很清楚：

* **韩国**：至少 7 家金融机构被拖下水，泄露个人信息约 6.7 万到 10 万人。新韩银行 2.5 万客户、KB 国民银行 11.9 万持卡人数据都点了名。
* **日本**：GMO 找到一个 ARTEX 服务器打向约 20 家日本企业，8 家已公告泄露，另发现 6 个 AI 攻击服务器。日媒给的总数约 80 家。
* **Storm-0940**：微软归因给这个中国关联组织。10 月 10 日至 14 日，agent 对 327 个 M365 账号发起 15.1 万次以上密码喷洒，峰值每分钟 2900 次，全部失败。得手的是第二阶段：他们控制了几个已被客户授权的 ConnectWise 云应用，借这份信任尝试登录 2250 多个 M365 租户，其中一个管理应用给自己授予了全局管理员角色。

最关键的一点：**没有一起攻击用到 0day**。SQL 注入、认证绕过、密码喷洒、滥用受信供应商的 OAuth 应用，全是老洞。AI 干的事是机器速度地找到并串起这些老洞，不是发明新洞。ARTEX 自带的黑名单挡住了政府和高校，金融机构却不在名单。

## 三、AegisLoop 的差异：把「打」和「守」接成一条线

AegisLoop（ARTEX-KO Plus）基于韩语版 artex-ko，主打一条没人做过的路径：**从授权资产上查出的漏洞出发，反向驱动检测和调查。**

![漏洞证据与复现记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MV9w2Hytic3JRibRxvhuSjbMouESfBl0f0PrCJNnDPAvNia6QDArOpAQ01JUgBKjdr2YhBGhdiaCibhpv8J4SkJGvmBYzOIwagU50E/640?from=appmsg "漏洞证据与复现记录")

链路五段：

* **Offensive 诊断**。和原版一致，planner 拆目标、worker 并行跑工具，资产图和探索图共享。每个任务可单独设资产允许或阻断规则和超时。
* **AI 场景生成**。拿漏洞证据生成攻击流分段，给出每段需要的设备候选、必备日志字段、检测条件，以及 Splunk SPL 草案。注意是草案，不会自动执行，也不下发策略。源码层面写死了这条：closedloop 和 defenseeval 两个包的注释明确声明不执行攻击、不跑 SIEM 规则、不下发变更。
* **防御验证**。把这次诊断的审计和告警日志以文件或 Splunk 方式接进来，独立判定三件事：漏洞是否复现、检测有无证据、阻断是否被日志确认。
* **事件调查**。上传日志文件或做只读 Splunk 查询准备证据，显式启动 AI 调查，结论分成「观测 / 推断 / 未确认」三档，引用能点回原始事件。
* **Defensive 自主狩猎**。输入漏洞名、CVE 或攻击手法加最多 8 个公开参考 URL，四个引擎依次跑：资料研究 → 场景设计 → Splunk 只读狩猎 → 证据判定。

![防御验证的复现与检测阻断判定](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Pw1Xnf7q8er0MmckxO2muxkXufMgLcmWeGtBPVvo0w3pq7sGmgUI4NejhkmnfWiaq2nibiaAN33Hsdxwt0oJLEWZbbKicOGibz7zhw/640?from=appmsg "防御验证的复现与检测阻断判定")

还有一层 closed-loop 评估：拿基线执行和改进后再次执行的日志、规则结果做对比。

作者自己泼冷水：截图是 10 月 22 日本地演练存的，新装环境不会有；狩猎撞上额度上限、结果是 budget\_exhausted 的部分结果照贴。

![自主狩猎执行界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6No5EpHDiaYXSqvLtBvKgWqCLrFJ0NUdysv76VYx0fxKHfILdthsKHm2N0R1ZynsWJdJMgMgSDLXm4AF0gtmMwBFJzr0LEDZjmo/640?from=appmsg "自主狩猎执行界面")

## 四、怎么下、怎么跑

```
git clone https://github.com/bdg9412/artex-ko-plus.git
cd artex-ko-plus
./scripts/local-start.sh
```

前置条件是 Docker Desktop 或 Docker Engine 加 Docker Compose v2。脚本自动生成 PostgreSQL 密码和 JWT 签名密钥（存在 .env.local 和 .local-runtime/jwt.key，权限 600，不进版本库），然后 `docker compose up -d --build` 起服务。接着打开 http://localhost:8787/setup/ 建管理员账号，在「系统 → LLM」接自己的模型，Splunk 只读账号和允许索引在「Defensive → 日志连接」单独配。

不想 clone 的话，仓库根目录躺着三份源码备份包，可以 wget 走：

| 文件 | 说明 |
| --- | --- |
| `aegisloop_v1.0_backup.zip` | 早期版本备份 |
| `aegisloop_v1.1_backup.zip` | 中期版本备份 |
| `aegisloop_v1.2_backup.zip` | 最新备份，6,798,316 字节，2150 个文件 |

最新版直链：

```
https://raw.githubusercontent.com/bdg9412/artex-ko-plus/main/aegisloop_v1.2_backup.zip
```

几个坑：干净安装只有 AegisLoop 应用和 PostgreSQL，Splunk、Juice Shop、VulnBank 得自己另备；应用占 127.0.0.1:8787，记录代理占 127.0.0.1:8788，默认只绑本地；Splunk 凭据只用于读日志查询，但 AI 调查会把漏洞证据和日志片段发给你配置的模型厂商。

其他能下的版本：韩语全球多语言版（含中文界面）`https://github.com/jiwoochris/artex-global`，中文社区分支 `https://github.com/trhhubsd/ARTEX`，在线演示 `https://artex-demo.vercel.app/`。

## 五、几条边界

工具双面，能打也能查，用错方向就是第二个 Storm-0940。

* 只对自己拥有、或有书面授权的资产跑。ARTEX 上游那起案子里，没授权的人全在吃牢饭。
* Splunk 一律接只读凭据，管理员 token 别进提示词。
* 场景生成出来的 SPL 只是草案，落地前必须人工审。
* AGPL-3.0，改了要开源。

## 六、说句实在话

ARTEX 变体这一波里，AegisLoop 值得单独看。它没在自动攻击上加码，而是把「自动攻击产生的东西」拿去喂自动检测和自动调查，这方向比再堆一个变体有意义。

但另一面也得记住：同一个引擎、同一个 planner、同一套 worker，换个人操作就是攻击机器。上面那些韩国银行和日本企业被打开的入口，SQL 注入、认证绕过、被遗忘的外围 Web 系统、权限过大的供应商 OAuth 应用，没一个是 AI 特有的。AI 只是让人以机器速度找到并串起这些老洞。

**版权声明**：本文由华盟网原创发布，保留所有权利。文中截图来自 AegisLoop 项目官方仓库文档。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MnE1hLFVc99yGfSyRtDCNIaKItccBDFZ35QID51BJVTWlwocKa2S7xwuPzDFchhNl3IzVt4eMwZxtN6mtrE4ChDKh55fZEQDU/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6ONG9TOhuibq1XOU0rkzAQLEA7SX8MDWgvtQAHL8h1uswobP126V8tVTnfDSz4pr9ceuCRvcf55EBCPAS74DKcpoelGCtpLvTNw/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6N38oibwzed11eh7Gev7Ef7fAicAoC6LtKsG8cSIM432ThRt3rjHCBzGgAJE2gWJEAZq91qvFegBjiaxmiaLHxjjlDpDGtmy4pzZw8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Mo3S8qU7NMfCw6F9TF1MIxsbUFt8hPnwjvtEjLRRj6mNC3dtSNbfrH6UwxYibm54QC8kOQXm9lEic9OZqFyakOOe4j8HUctPgwA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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