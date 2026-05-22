---
title: 个人微信接入 CyberStrikeAI（扫码绑定）
url: https://mp.weixin.qq.com/s/ISmldITQvZ4ObIVQLvA8ag
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:02:44.087555
---

# 个人微信接入 CyberStrikeAI（扫码绑定）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33ua6XkODLYJrvzQ1KDCORTMicVDYw8f6QPD9KtdhibicIvzHguLviaTvia94Y0N4kpQtEeo5KDC9Hhqc5B426BibwSvkoIy2kqF1zhxI/0?wx_fmt=jpeg)

# 个人微信接入 CyberStrikeAI（扫码绑定）

学安全也就图一乐
学安全也就图一乐

安全鸭

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33upvhfVFicVjZe5fnXvNYn030WSGeQxkd7lalCmI93ZtibuNUxticcjaWL9x7QCO8peicOLVaqDrYKZu6NHiaR0gOdIo0H1SpIicRuuQ/640?wx_fmt=png&from=appmsg)

做渗透测试、漏洞研判的时候，遇到过这种场景：

* 人在外面，只有手机，服务器上的 CyberStrikeAI 却懒得开浏览器；
* 钉钉 / 飞书 / 企业微信都配好了，但日常沟通还是**个人微信**；
* 机器人回调要公网、要备案，家里 NAS 或小内网部署总差点意思。

这一次，**CyberStrikeAI** 在钉钉、飞书、企业微信之外，新增了**个人微信（iLink）机器人**接入；同时把**系统设置 · 机器人**相关的前端界面做了一轮体验优化。

下面按「能做什么 → 怎么配 → 界面改了什么」说清楚。

---

## 一、个人微信机器人：能做什么？

和已有的钉钉、飞书、企业微信机器人一样，微信侧的核心目标不变：

**在手机里发文字，就能驱动 CyberStrikeAI 的 AI Agent 做授权范围内的安全测试与分析。**

具体能力包括：

| 能力 | 说明 |
| --- | --- |
| 与 Web 同源对话 | 机器人里创建的会话会出现在 Web「对话」列表，两边数据打通 |
| 完整 Agent 链路 | 执行路径与 Web 端 `/api/agent-loop/stream` 一致，含过程记录与工具调用 |
| 内置命令 | `帮助` 、`列表`、`新对话`、`切换 <ID>`、`停止`、`角色` 等，中英均可 |
| 可选多代理 | 在「基本设置」中开启后，微信机器人也可走 Eino 多代理编排（成本更高） |
| **无需公网回调** | 采用微信 **iLink 长轮询**，程序主动拉消息，内网部署更友好 |

与企业微信的区别一句话概括：

* **企业微信**：HTTP 回调 + 主动发消息 API，需要公网可达与后台配置；
* **个人微信**：Web 端**扫码绑定**，绑定后自动写配置并拉起长连接，**不用折腾回调 URL**。

---

## 二、半分钟完成绑定（Web 端可视化）

路径：**登录 CyberStrikeAI → 系统设置 → 机器人设置 → 微信 / iLink**。

### 步骤 1：生成二维码

点击 **「生成二维码并绑定」**。页面会显示加载动画，并展示绑定二维码；若图片无法显示，也可通过备用链接在手机微信中打开。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vVjQIOoWvs5EOxkueWWabgTdoZoia4swycahj4RXTlhpQXghnwJ3ibx4Sdpia6B08kKQe0mQNWeIZWZl8qmtye3Vy8Gib9t9KibxSY/640?wx_fmt=png&from=appmsg)

### 步骤 2：微信扫码确认

用手机微信扫描二维码，在手机上完成确认。界面顶部状态会从 **「未绑定」→「绑定中…」**，并展示三步进度：**生成二维码 → 微信扫码 → 确认绑定**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33vlXeIlCiczft7OGc2r9YibecHiae3HFwC5m1sKA78I837ibo9qwl6y6mAutpA2Q8xFBSSD2CY3pmLJjc4QsdR3HqDLFs5Ogg1YMDM/640?wx_fmt=jpeg&from=appmsg)

### 步骤 3：完成绑定（部分账号需配对码）

* 多数账号扫码确认后即可完成；
* 若手机提示需要输入**配对数字**，在页面下方输入框填写并提交，系统会继续轮询直至绑定成功。

绑定成功后：

* 状态徽章变为 **「已连接」**；
* `bot_token`、`ilink_bot_id` 等写入 `config.yaml`；
* 机器人长连接**自动启动**，一般**无需再整进程重启**。

高级用户可展开 **「高级设置」**，按需调整 API Base URL、Bot Type、Bot Agent 等（默认值对大多数场景已够用）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sT5yhpJM2gK3yEVosXgh9H91encvUylhlEmjwQcTh92vqxQ43qAZDVABibqrImJFrYss1wmWpgUzWnvnfbWoqUcV6yGpu3Y8g4/640?wx_fmt=png&from=appmsg)

---

## 三、绑定之后，在微信里怎么用？

向绑定的微信账号（或 iLink 提供的对话入口）直接发**文本**即可。

### 常用命令速查

| 命令 | 作用 |
| --- | --- |
| `帮助 / help` | 查看命令说明 |
| `列表 / list` | 查看对话列表与 ID |
| `新对话 / new` | 开启新会话 |
| `切换 <对话ID>` | 在指定对话中继续 |
| `停止 / stop` | 中断当前正在执行的任务 |
| `角色 <名称>` | 切换渗透、Web 扫描等预设角色 |
| `版本` | 查看当前 CyberStrikeAI 版本 |

除命令外，**任意自然语言**都会交给 AI，例如：「对 example.com 做授权范围内的信息收集」「帮我梳理这份漏洞报告的风险等级」等——与 Web 控制台同一套能力，只是交付渠道换成了微信。

> **合规提醒**：请仅在**已获得书面授权**的目标与环境上使用。CyberStrikeAI 面向授权安全测试场景设计，请勿用于未授权访问或任何违法用途。

---

## 四、技术实现

若你关心「为什么内网也能用」，核心机制如下：

1. **iLink 协议**：通过 `https://ilinkai.weixin.qq.com`（可配置）与微信侧通信；
2. **长轮询 `getUpdates`**：后台 goroutine 持续拉取消息，断线后按 5s～60s 指数退避自动重连；
3. **扫码绑定 API**：`/api/robot/wechat/qrcode` 生成会话，`/qrcode/status` 轮询状态，绑定成功由 `ApplyWechatRobotBinding` 持久化并触发 `RestartRobotConnections`；
4. **消息回复**：收到文本后走统一 `HandleMessage`，经 Agent 处理后再 `SendTextMessage` 回传。

这意味着：你不需要像企业微信那样配置 Token、EncodingAESKey 和公网回调地址，**个人微信场景的部署门槛明显更低**。

---

## 五、前端界面优化：设置页与仪表盘

本次除了微信机器人，还对 Web 前端做了一轮「能感知到」的体验打磨。

### 1. 机器人设置 · 微信专区

* **独立卡片布局**：微信配置与钉钉 / 飞书 / 企业微信分区展示，信息层次更清晰；
* **实时状态徽章**：未绑定 / 绑定中 / 已连接，一眼可知当前状态；
* **绑定流程可视化**：三步进度条 + 二维码边框动效 + 加载 Spinner；
* **绑定成功页**：成功图标与 Bot ID 展示，支持「重新绑定」；
* **国际化**：中英文界面同步支持（`data-i18n` + `wechat-robot.js`）。

### 2. 配置热生效

在「机器人设置」或相关配置修改并 **「应用配置」** 后，钉钉 / 飞书 / **微信** 长连接会通过 `RestartRobotConnections`**自动重连**，多数情况下**不必重启整个 CyberStrikeAI 进程**——改完就能测，迭代更顺手。

### 3. 系统仪表盘

* **智能刷新**：已有数据时后台静默更新，避免整页闪成「…」占位；
* **自动轮询**：每 60 秒刷新，标签页隐藏时暂停，回到页面立即补拉；
* **数据过期提示**：超过 5 分钟未更新时，「上次更新」徽章变灰并提示，减少「以为是最新数据」的误判；
* **并行拉取**：任务、漏洞、HITL 待审批、C2、WebShell 等多路指标一次聚合，打开仪表盘即可纵览全局。

这些改动不改变核心能力，但让**日常运维与状态感知**更省心——尤其是你同时开着 Web 控制台和手机机器人的时候。

---

## 六、与企业微信 / 钉钉 / 飞书如何搭配？

CyberStrikeAI 的机器人矩阵现在是：

| 平台 | 接入方式 | 典型场景 |
| --- | --- | --- |
| **个人微信** | iLink 扫码 + 长轮询 | 个人习惯、小团队、内网部署 |
| 企业微信 | HTTP 回调 + 主动 API | 企业合规、统一办公 |
| 钉钉 | Stream 长连接 | 国内企业协作 |
| 飞书 | 长连接 + 事件订阅 | 研发协作团队 |

你可以按团队习惯**只开一种**，也可以**多平台并存**——会话数据在 Web 端统一可见，便于在电脑前复盘、在手机边跟进。

---

## 七、快速排错

| 现象 | 建议检查 |
| --- | --- |
| 扫码后一直「绑定中」 | 是否超过 5 分钟会话过期；重新生成二维码 |
| 提示需要配对数字 | 在手机查看数字，在 Web 输入框提交 |
| 绑定成功但发消息无回复 | 设置里是否勾选「启用微信机器人」；看日志是否有「微信 iLink 长轮询已启动」 |
| 改配置后不生效 | 点击「应用配置」；仍异常可重启进程 |
| 想解绑重绑 | 使用「重新绑定」，或在 `config.yaml` 清空 `robots.wechat` 相关字段后重新扫码 |

更完整的机器人说明见项目文档：`docs/robot.md`（企业微信 / 钉钉 / 飞书章节）；微信 iLink 以 Web 设置页引导为准。

---

**项目地址**：GitHub - https://github.com/Ed1s0nZ/CyberStrikeAI

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/flBFrCh5pNakoPXq9aPYuhOj3SrCc1eLXB37lY487tvRfKhZWGIojsRzJDDibZQEZ3ic0l8tg5GcMS6qgu4zzDhw/0?wx_fmt=png)

安全鸭

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/flBFrCh5pNakoPXq9aPYuhOj3SrCc1eLXB37lY487tvRfKhZWGIojsRzJDDibZQEZ3ic0l8tg5GcMS6qgu4zzDhw/0?wx_fmt=png)

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