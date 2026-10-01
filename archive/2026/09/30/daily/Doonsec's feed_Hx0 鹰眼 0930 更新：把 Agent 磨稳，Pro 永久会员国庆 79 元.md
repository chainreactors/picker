---
title: Hx0 鹰眼 0930 更新：把 Agent 磨稳，Pro 永久会员国庆 79 元
url: https://mp.weixin.qq.com/s/xFo3Ln5mAaDCTPgFv_oriw
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:18.966238
---

# Hx0 鹰眼 0930 更新：把 Agent 磨稳，Pro 永久会员国庆 79 元

# Hx0 鹰眼 0930 更新：把 Agent 磨稳，Pro 永久会员国庆 79 元

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

版本更新 · v1.0.6 · 0930

把 Agent 磨稳，把界面磨顺
Hx0 鹰眼 1.0.6 · 0930 更新

如果你还没用过：它是跑在浏览器侧栏里的安全工作台，抓包、改包、重放、Fuzz 与 AI 都在里面，不用配系统代理。如果你已经在用：0930 这一版没有加大功能，而是把已经在用的东西逐项打磨——Agent 更稳、模型更多、抓包台更顺手。

· 更新日期 2026-09-30　· Chrome / Firefox

不管你是第一次听说 Hx0 鹰眼，还是已经用了一段时间——这一篇前半段先说清「它是什么」，后半段说清「0930 这一版改了什么」。

01先认识一下 Hx0 鹰眼

Hx0 鹰眼是一款面向 **Chrome、Firefox 与主流 Chromium 浏览器**的浏览器安全工作台。它以扩展形态运行，主界面就是浏览器侧栏——不是又一个独立客户端，也不用先配一套代理环境。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibsoCKx5dCsRRibd6P4ib9DIdgHPHC593ZyJQ565dpIpoFlQjIUics5zJ5nWsG4D7Bz4ac8zPUnNMA93MjgvayiaX1rzyUpSJEnw38/640?wx_fmt=png&from=appmsg)

图1 | Hx0 鹰眼 v1.0.6介绍。

它把日常研发联调与授权测试里最常来回切换的几件事，收敛到了同一个侧栏：

|  |  |
| --- | --- |
| 能力 | 说明 |
| **抓包与拦截改包** | HTTP 与 WebSocket；按域名 / IP 通配、资源类型、后缀过滤；拦截队列可改包、放行、丢弃 |
| **历史与详情审计** | IndexedDB 持久化；Pretty / Raw / Hex / Render；敏感信息聚合高亮；Burp 风格导出 |
| **重放与微型 Fuzz** | 请求默认 Pretty 打开；标记注入点后跑 HTTP / WS 微型 Fuzz；基线对比 |
| **敏感信息与暗链检测** | 证件、手机、银行卡、邮箱、Shiro / JWT / Swagger / Druid 等指纹，外加自定义正则与关键词库 |
| **AI 安全审计** | BYOK，云端或本地模型都行；单包解读、批量归纳、AI 任务台与 Skills 知识库 |
| **鹰眼 MCP 与浏览器级 Agent** | 专业版能力；让外部 Agent Host 或侧栏内的 Agent 直接操作真实标签页 |

**和传统代理类工具最不一样的地方**：基础抓包**不需要配置系统代理**，不依赖 JVM，装完即用。它就在你真实的标签页和登录态里工作，看到的正是 XHR / Fetch / WebSocket 这些现代前端的实际流量。

版本上分**社区版与专业版**：社区版覆盖抓包、详情审计、普通重放、拦截改包、基础编解码、全量深搜与敏感信息匹配；专业版另外解锁页面内重放 / Fuzz、HTTP 与 WS 微型 Fuzz、AI 分析与 AI 任务台、Skills 知识库、油猴脚本工作台、暗链检测、批量工作台，以及鹰眼 MCP 与浏览器级 Agent。新装之后可以先免费体验 **30 分钟专业版全功能**。

没接触过的同学，看完这一节就够接着往下读了；已经在用的可以直接跳到 **第 02 节**看这次更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9VzJPyD6O6NOiancyePUlTNibHJgQXBRp4qE3GS8MAD1NoYuhWOicGbtN8entoETGOBrJaJ6Bzp9oJh056Kk2PnWhZzgicvQus3tA/640?wx_fmt=png&from=appmsg)

图2 | Hx0 鹰眼 v1.0.6（0930 更新）能力总览——抓包审计、重放 Fuzz、鹰眼 MCP、浏览器级 Agent 四大板块。

02先分清：功能版和打磨版

**1.0.6 是功能版**——鹰眼 MCP 与浏览器级 Agent 都是在 1.0.6 里落地的，这个版本已经带着它们跑了十天。

**0930 是打磨版**——它没有新增能力模块，而是把 1.0.6 里已经交到手里的东西逐项修：稳定性、交互、模型覆盖、抓包与重放的细节，以及发布包本身。

九个方向的变化如下，后面几节挑重点展开。

|  |  |  |
| --- | --- | --- |
| 方向 | 性质 | 这次改了什么 |
| **Agent 稳定性与记忆** | 打磨 | 批准弹窗打不散，中断能从检查点恢复，跨会话记忆默认关闭 |
| **模型与 AI 设置** | 扩充 | 新增 Grok、MiniMax、Gemini 与本地 Ollama / LM Studio |
| **弹窗与工作台** | 理顺 | 开关自动展开收起，抓包范围与重放行为更明确 |

|  |  |
| --- | --- |
| 更新方向 | 关键变化 |
| **Agent 对话控制插件** | 聊天里直接管理抓包、拦截、代理、页面脚本、MCP、人设、Skills 与设置 |
| **Agent 稳定性与记忆** | 批准弹窗不会被误关，中断可从检查点恢复，跨会话记忆默认关闭 |
| **模型与 AI 设置** | 新增 Grok、MiniMax、Gemini，Ollama 与 LM Studio 归入本地 |
| **弹窗交互** | 开关自动展开对应设置；删除确认统一用插件内置弹窗 |
| **抓包工作台** | 范围明确为当前域名 / 当前标签页 / 全部记录；角标按站点计数 |
| **重放与筛选** | 重放台默认 Pretty；修正「当前标签页流量」误筛选 |
| **抓包与拦截** | 拦截队列自动刷新；请求体 / 响应体缺失时说明原因 |
| **分析与暗色界面** | WebSocket 帧、批量重放、AI 分析与暗链检测的反馈改进 |
| **MCP 接入与正式包** | 本地 MCP Server 升至 1.0.13；正式 ZIP 仅含混淆后的扩展脚本 |

03Agent：从「能干活」到「敢让它干活」

让 Agent 操作真实浏览器，最难的不是"能不能点对"，而是**出错之后怎么办**。这一版几乎全部改在这个方向上。

1**批准弹窗打不散**——待批准的操作不会被遮罩层或 Esc 误关，点击「等待批准」状态可以重新把弹窗打开。手滑一次不至于让整轮任务重来。

2**中断了能接上**——侧栏关闭或后台中断后可从检查点恢复；对结果不明的提交、下载这类操作，它会先核实再决定，避免重复执行。

3**Skill 落盘以回执为准**——保存与更新 Skill 时不再"看起来成功"，要拿到真实回执才算数。

4**跨会话记忆默认关闭**——只有你主动打开后才按相关性召回；默认不开，聊天内容不会悄悄进模型上下文。

04Agent 能直接改鹰眼的配置

这一版把 Agent 的触角从页面延伸到了插件本身。你跟它说一句「把当前网站加入抓包拦截域名」，它会自己去读设置、写规则，再把操作证据回报给你。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9U1Q9wFKoI201dJQHlSLFbfsLqMQ9f3ibz46IbHkZqhSBUGDzHehYaGqcTof1bmOydGuiaYATDBicUbf837NY59nCQsuNf53g7IY/640?wx_fmt=png&from=appmsg)

图3 | 在 Agent 模式里说一句「将当前网站加入抓包拦截域名」，它自己去读设置、写规则，并回报操作证据。

在上面这次执行里，它把抓包规则和拦截规则一起收敛到了目标站点，并明确说明了「现在抓包只针对该域名生效，拦截目标域名也已限定」，还交代了后续换站点该改哪个字段。**改完告诉你改了什么、怎么改回去**，这比"操作成功"四个字有用得多。

它能碰的范围包括：启停抓包与拦截、查看队列并放包、配置 SOCKS / HTTP 代理、创建和修改页面脚本、管理 MCP 与人设、调整抓包类型与后缀、开关「完整响应体（被动监听）」、修改敏感信息与暗链规则、切换语言和 AI 配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO83Qnfd7LXrwqOpmia0iceQV3GM1gGSOIRIl92UMmIiaBvlRaPFqPRXd6lEG3TV50cMP8RE5A5CvEzuJddV3rU8SKMX8Wa3ACo9ibI/640?wx_fmt=png&from=appmsg)

图4 | Agent 可调整的抓包目标域名、完整响应体被动监听与抓包类型开关。

**边界也划清楚了**：你明确要求持续开启的抓包或拦截会保留，临时任务开启的会在任务结束后清理。不会出现"我就问了一句，结果它把我抓包关了"这种事。

05抓包台：范围、重放、拦截

Agent 是这一版的重点，但每天真正高频用的还是抓包台。0930 在它身上修的三处，都属于"用久了才会疼"的地方。

1**范围名称说清楚了**——「当前域名流量 / 当前标签页流量 / 全部抓包记录」三者分工明确，扩展角标按当前站点的抓包数量更新，Chrome 与 Firefox 的界面和 Agent 工具保持同步。

2**重放台默认 Pretty**——Pretty 和 Raw 里改的内容都能直接发出去，切换视图时保留编辑，不用怕改完没生效。

3**「当前标签页流量」不再漏请求**——修正了按地址栏域名误筛选的问题，这个标签页发往其他子域名的请求现在能正常看到。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO84bngaDuFGx8nhkQIx6MoYicRMlhKO34IgYEbFRm5iam94PgDMx4ibNP3o3G3wN9icvRZyvYODDUyAFedV89uD8mhzLu9JRX9quJc/640?wx_fmt=png&from=appmsg)

图5 | 抓包工作台切到「当前域名流量」，列表范围与角标口径一致。

配合角标一起用，现在切范围时心里有数：想盯单个站点看「当前域名流量」，想追一个页面的完整行为链看「当前标签页流量」，做全局回溯看「全部抓包记录」。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9oSy3F3dgO1Qd51JHaGKy4PgLgkuBzZiaFWJxayouV9MLpFNIhqvkXMqe234qj4lQoU1ABWmDa6HE9kzib9wsQkGic3cw3q0vDFs/640?wx_fmt=png&from=appmsg)

图6 | 「全部抓包记录」用于全局回溯，配合类型 / 状态码 / 敏感命中多维筛选。

拦截队列有新请求时会自动刷新；**请求体 / 响应体拿不到时会说明原因**，而不是留一片空白让人猜。Chrome 的「完整响应体（被动监听）」依旧只对浏览器允许读取的请求生效；Firefox 在移除带响应体的请求时会明确说明原始响应体不可用、但请求可能已发送——重放产生的是新响应，这一点不再含糊。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicicaCC1vibeicC0FSHibEmN0pRvic8BBnp4VDOxyTwLBghxAll7CGgw4EzM3stPKzAszV9Hnicuu77HtSBnbTqoc5f5XlmiaBicbDquiaE/640?wx_fmt=png&from=appmsg)

图7 | 放开到「全部域名」，跨站与第三方请求一屏可见。

06模型与 AI 设置：云端随便挑，本地也能跑

AI 提供商这次补上了 **Grok（xAI）、MiniMax、Gemini**；Ollama 与 LM Studio 被明确归入**本地**选项，连同原有的 OpenAI、DeepSeek，基本覆盖了"云端随便挑一个"到"数据完全不出内网"两种取向。新配置的默认模型候选也一并更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9IciaBBf6slKPib8kOX91ojL1OXAEK4RFmL6ticbrSlxbc6l4wmtXRH4os8QaafIicZcofKuJt5dDLV8NB1NCCf5UtwSvR3WgkW5E/640?wx_fmt=png&from=appmsg)

图8 | 高级设置里的 AI 分析提供商：OpenAI、DeepSeek、Anthropic、Grok、MiniMax，以及本地 Ollama / LM Studio。

几个容易被忽略但很关键的修正：切换提供商**不会串用密钥**；已经保存的模型选择**不会被自动覆盖**；获取可用模型列表时会提示不合法的密钥字符；提供商、模型、Token 窗口三个下拉的样式也统一了。全套仍是 BYOK，模型请求发往你自己配置的端点。

07弹窗与界面：少点几下，少踩几个坑

设置页做过一轮**收纳**。抓包、智能代理分流器与鹰眼 MCP 的开关会自动展开或收起对应设置；抓包目标、内网 / 自签名 HTTPS、类型 / 后缀三块一起折叠，标题空白处仍可手动切换。代理配置名和 MCP 端口只在启用时才显示；人设、Skills、敏感信息与暗链的详细设置，也各自跟着开关收起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibxbDZ9m8ibpHlO7aDS6xZ4Ve5vNFeZW3YKtbn7bibiawvgQFdZT7efH2RxRoGZXq4DXdnIwNVGO1vN5X2nxwAK9vYsHMk4Grch5s/640?wx_fmt=png&from=appmsg)

图9 | 智能代理分流器：按站点规则把命中请求转发给上游代理，未命中保持原路径。

其余几处是实打实的体验修正：设置里的删除确认统一改用**插件内置弹窗**；英文界面下的快捷键按钮、人设与暗链设置卡片的裁切、规则标题换行都已修正；按钮的对齐、字号与蓝色主操作样式统一。深色模式下，PRO 标识不再遮挡内容，macOS 系统深色时弹窗文字对比度也调过。

08MCP 与正式包

本地 **MCP Server 更新至 1.0.13**，配置示例与启动诊断都做了改善——连不上时更容易看出是哪一环出了问题。正式 ZIP 的分发方式也收紧了：Chrome / Firefox 包内只包含**混淆后的扩展脚本**与中英文手册，而独立的 MCP 服务 MJS 仍保持可读、可由 Node 直接运行，并附带校验信息。升级时记得替换扩展和 MJS，并重启 MCP Host。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOiczPXzuPOgegfmrO9j6UYCibMGqG8DibpyiaSsMUOq9Sacibktzu49kOYvsq8HCxqIFHSPaLTE4OQ6CMVnX3ytMydQ5Q8gxDnxHDBk/640?wx_fmt=png&from=appmsg)

图10 | 0930 版本更新清单。

09怎么升级，和几个已知边界

升级流程和以往一致：先从旧版导出需要保留的数据，关闭相关侧栏，用新包内容替换原来的**固定目录**，再回扩展管理页点**重新加载**。

注意别同时加载两个不同目录的鹰眼，否则会生成两个扩展 ID，本地数据互相看不见。用 MCP 的记得一并替换 MJS 并重启 Host。

另外几条边界也一并说清楚，免得你升级完才发现：

1Chrome 的「完整响应体（被动监听）」只对**浏览器允许读取**的请求生效；Firefox 没有这个开关。

2Firefox 对未签名扩展不提供永久安装，重启后需要重新临时载入。

3代理账号密码认证：Firefox SOCKS5 已支持；Chrome SOCKS 与 Firefox SOCKS4 暂不支持这种认证方式。

**授权与合规**：抓包、拦截、重放与 Fuzz 请**只在取得授权的系统**上使用。启用 AI 分析 / AI 任务 / Agent 时，完成任务所需的报文与页面上下文可能发送到你配置的模型服务；默认自动脱敏会尽量遮蔽 Cookie、Token 等常见字段，但不能保证识别全部敏感数据。MCP Server 只监听本机回环地址，但你信任并连接的第三方 Agent Host 仍可能把工具结果发送到其模型服务，不用时请关闭桥接。

10国庆活动：送一年 Pro，永久会员限时 79

国庆这一波准备了两个活动，**都到 2026/10/08 12:00 截止**。

🎉 活动一 · 加入知识星球，送一年 Pro 会员

**活动内容**　加入「Hx0战队」知识星球，送一年 Hx0 鹰眼 Pro 会员。

**活动时间**　2026/09/30 12:00 至 2026/10/08 12:00。

**新人优惠**　20 元立减金，仅限前 100 名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOib7zaniaQprPIfQj69jWEG2rdCoUvYW3mcX9DUkYfqflzrcuEaMibrTqS0omh11uT66ojXgyj6tX1bxkjup0sOict7qtsR91YtNvE/640?wx_fmt=png&from=appmsg)

图11 | 「Hx0战队」知识星球 20 元立减金优惠券——仅限前 100 名，领取时间 2026/09/30 12:00 至 2026/10/08 12:00。

🔥 活动二 · Hx0 鹰眼 Pro 永久会员国庆限时抢购

原价 ¥198¥79国庆价

一次拿下 Pro 永久会员：鹰眼 MCP、浏览器级 Agent、AI 任务台、Skills 知识库、页面内重放 / Fuzz、HTTP 与 WS 微型 Fuzz、暗链检测、批量工作台，专业版能力都在里面。

需要提前说一句：**永久会员近期会下架**。想一次买断、不想按年续费的同学，这次是最后的窗口期——机不可失，失不再来。

**两个活动都到 2026/10/08 12:00 截止。**已经装了社区版、想先把 Pro 能力完整跑一遍的，这是成本最低的一个窗口期；打算长期用的，趁永久会员还在，别等它下架。

11进群一起折腾

这个项目是持续迭代的，0930 只是其中一次打...