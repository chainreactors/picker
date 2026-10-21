---
title: DeepSentry 2.0.6 发布：让 Agent 会搜索、会思考，也能直接交付 Office 报告
url: https://mp.weixin.qq.com/s/Vxcwqi2hDhRBub6yC3rBCQ
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:47:56.551636
---

# DeepSentry 2.0.6 发布：让 Agent 会搜索、会思考，也能直接交付 Office 报告

# DeepSentry 2.0.6 发布：让 Agent 会搜索、会思考，也能直接交付 Office 报告

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

产品 · 版本发布

DeepSentry 2.0.6
会搜索，会思考，
也能直接交 Office 报告

2026 年 10 月 20 日，Hx0 工作室 发布 DeepSentry v2.0.6 Ultimate。执行效率、DeepSeek 适配、文档交付、远程连接、桌面与鹰眼五条线同时收口；全平台二进制已开放下载。

· v2.0.6 Ultimate　· 2026-10-20　· Apache-2.0 开源

DeepSentry 是一个跑在你自己电脑或服务器上的 AI 安全应急与智能运维 Agent：用中文说清目标，它自己规划步骤、调用工具、连本地或远程主机，最后留下可审计的报告。

2.0.6 没有再加新的入口。它把日常最容易卡住的四件事做顺了：Agent 少绕路、深度适配DeepSeek API真正能联网和思考、结果能直接变成文件、老设备和受限网络也能连上。

工具下载地址：https://github.com/asaotomo/DeepSentry/releases/tag/DeepSentry\_v2.0.6\_Ultimate

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8MxoxibOSC5A4G6p9TNndnEBuUl20K24n12RAEPLe6sSJC21aXh4K9XklxrYXTb9ibztPCsMkb3hM2W0htvq5XaIgc1FbRZyMaE/640?wx_fmt=png&from=appmsg)

图1 | v2.0.6 官方发布图——多 Agent 协作、本机桌面、DeepSeek 适配、Office/PDF、远程运维、聊天与定时六项能力。

01先认识它：一台会动手的 Agent

如果你还没用过，先看这份最小画像。它不要求你背命令，只要求你把目标、范围、权限边界和交付物说清楚。

|  |  |
| --- | --- |
| 你想做什么 | 它会怎么做 |
| **排查一台服务器** | 中文下任务，自动看系统、资源、进程、端口、登录记录 |
| **用手机指挥** | 扫码绑定微信 / QQ / 飞书等，私聊下发任务，验证码回原对话确认 |
| **网页设备留证** | 接上鹰眼后用真实浏览器打开控制台、截图，再出带封面的 Word |
| **多台一起巡检** | 配置主机清单，按名称或标签批量只读检查 |
| **要审计留痕** | 每次任务写 Markdown 报告，附带 SHA256 串联的证据档案 |

底层是 79 个内置工具，由 Go 原生实现或统一调度。Agent 按任务发现工具，不会每一轮都把全部工具塞进 prompt；大量能力在控制端完成，目标机不必装齐常用命令。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9N5Ekm9mex3Ck4yXeLDNQV9ZFcQQdaRXuNbBZu02oBUnS5JWuUztB300bPa4ABGOibdqKIUKCUVrkJtAn5dmB2YoVpc2DQgMUw/640?wx_fmt=png&from=appmsg)

图2 | 四层结构——交互、决策、执行、交付各自独立，串起来是一条可回溯的执行链。

本地 / SSH / Telnet / FTP / Fleet / WebShell 六种目标连接方式并存，同一套任务语言可以覆盖单机、多机和无交互环境。

**这一版改了五处**，先看速览，后面逐条展开。

|  |  |
| --- | --- |
| 方向 | 这一版的变化 |
| **执行效率** | 工具按需发现、只读并发 / 修改串行、上下文预算 48K / 16K |
| **深度适配DeepSeek** | 内置 web\_search、/thinking 思考控制、/cost /context /balance |
| **文档交付** | 真实 DOCX / XLSX / PPTX / PDF 生成，创建后回读结构 |
| **远程连接** | SFTP-only、旧 SSH2 算法兼容、配置事务化更新 |
| **桌面与鹰眼** | 鹰眼 MCP 53 个工具、桌面控件按文字与角色定位 |

02执行效率：少搬一点，多想一步

长任务最容易浪费的地方不是模型慢，而是每一轮都在重复搬运：重复的提示、无关的历史、塞不下的工具定义。2.0.6 从三处下手。

2.1 工具按任务发现，同一步只复用一份定义

执行指导与工具 schema 改为按任务加载，同时保留用户目标和已发现的工具；预算、诊断和请求共享同一步的工具定义。重复提示与原生调用里的空字段被精简，但实际参数类型保持不变。

工作历史默认预算 **48K**，子 Agent 默认 **16K**，都可以配置；摘要会排除图片二进制和重复推理内容，不再把同一段思考反复计入上下文。

2.2 只读并发，修改串行

独立的只读 I/O 有界并发，存在依赖或会修改目标的操作保持顺序屏障。共享执行器被覆盖、取消信号传不出去这两个老问题一并修掉——取消之后不会再有后台动作继续跑。

2.3 出错了，先分清是哪一种错

HTTP 错误按真实状态码与错误字段分类，遵守服务商的 Retry-After，区分认证失败、额度不足与限流。不该重试的不再重试，该等的时间按服务商说的等。

这笔账算在长任务上

少一次无效重试、少一段无关历史，最后都会变成更少的步数和更清楚的结论。这一版的收益不体现在某一次短任务的秒数上，而体现在整条链路的稳定性上。

03深度适配DeepSeek API：联网、思考、算账

这一版把 DeepSeek API的三件事接进了日常流程：查得到、想得清、花得明。

|  |  |
| --- | --- |
| 命令 | 作用 |
| **/search status | on | off** | 查看或热切换联网搜索，状态写回 config.yaml 并立即生效 |
| **/thinking on | off | low | high | max** | 控制思考模式与强度 |
| **/thinking budget 96k** | 给思考内容设置输出预算 |
| **/cost** | 查看服务商返回的实际 token 用量与缓存明细 |
| **/context** | 在本地估算本次请求的组成 |
| **/balance** | 查看支持厂商的账户余额，TUI 状态栏同步展示 |

内置的 web\_search 走 DeepSeek 官方 Search API，用来补充实时网页、新闻、版本发布和漏洞公告证据。它不在固定 schema 里，只有任务需要联网检索时才通过工具目录发现并加载；/search off 之后它会从工具目录和原生 schema 中消失，Agent 无法再发起搜索。

检索语法支持 site:、-site:、精确短语、after: / before: 等写法，返回结果必须保留 URL 作为来源。计费按成功请求计，**5 元 / 1000 次**，count 不影响单价；查询词会发送到 DeepSeek，主模型不是 DeepSeek 时必须单独配置 search.api\_key，不会把别家的 Key 递过去。

Chat、Responses、Anthropic 三种协议这一版统一支持原生函数调用、工具结果与思考内容回传。切换模型厂商时，工具调用不再退回“模型输出一段 JSON 再解析”的旧路径。

/cost 显示的是服务商真实返回的 usage 和缓存命中情况，/context 是本地估算，两者不混用。余额查询本身不调用模型，失败时保留上一次的值并标明更新时间。

04交付物：从一段话到一个文件

以前让它写报告，拿到的是 Markdown；现在可以直接拿到能发出去的文档。

|  |  |
| --- | --- |
| 能力 | 说明 |
| **读附件** | 解析 Word、Excel、PPT、PDF，支持表格、公式、PPT 备注与中文 PDF 文本提取 |
| **生成文件** | 真实 DOCX / XLSX / PPTX / PDF，不是改后缀的文本 |
| **结构回读** | 创建后回读文件结构，确认标题层级、工作表、页数和公式真的写进去了 |
| **原件保护** | 计算文件哈希，默认拒绝覆盖原文件 |

三个顺手的使用场景：巡检结束直接出整改报告；资产清单出多工作表 Excel，公式和汇总一并在里面；周会材料出 PPT，备注页带上讲解要点。

需要提醒的是，文档能力覆盖的是“结构化生成”，复杂排版模板、扫描件 OCR 和图片内容理解仍然需要专用工具——这条边界我们写在这一节，而不是藏在脚注里。

05远程连接：连得上，也改得动

5.1 SFTP-only 与老设备兼容

新增 SFTP-only 模式，适合“只要传文件、不要 shell”的受限场景。旧 SSH2 设备补上 AES-192/256-CBC、HMAC-MD5 与 SHA1 GEX 兼容；严格模式仍然排除弱算法，并继续核验主机身份。

5.2 传到一半断了，能停干净

完善了 FTP 传输取消、代理配置快照、Telnet 分片协商、TCP half-close 与 HTTP CONNECT 缓冲处理。停止代理时会等待 BIND 与 UDP 资源释放，不再出现“面板显示已停止、连接还在转发”的情况。

5.3 用自然语言改配置

自身配置支持检索、分组描述、预览、事务 patch、原子保存与失败恢复。SSH 和 Fleet 的局部更新会保留未指定的认证字段——你说“把端口改成 2222”，它不会顺手把密码清空。

06桌面与鹰眼：看得见，点得准

Computer Use 是 2.0.5 就已经落地的能力：真实截图观察本机桌面，在系统授权和高风险确认之后执行键鼠动作。2.0.6 补的是“点得准”：按文字和角色查询前台窗口控件，用观察 ID 绑定后续的语义操作；换了窗口要重新观察，旧截图不会被继续沿用。

鹰眼这边对齐到扩展 1.0.7 / MCP Server 1.0.14 的 **53 个工具**，新增书签与脚本管理，保留 page\_token 分页续读与图片证据。TUI 同时修了长行、窄屏布局和代码复制混入面板装饰字符的问题。

哪些是新增，哪些是延续

Computer Use、聊天接入、定时巡检、多 Agent 协作、SHA256 证据链都在 2.0.5 及更早版本落地。2.0.6 做的是让它们更准、更稳、更好交付，不把旧能力重新包装成新功能。

07升级：一条命令，一个 ZIP

先确认手上的版本：

./deepsentry --version
# DeepSentry v2.0.6 Ultimate (build 日期)

按系统选一个主程序，或直接下载整包。整包里含全部平台程序、示例配置、内置 Skills、使用说明和这版宣传图。

|  |  |
| --- | --- |
| 系统 | 文件 |
| **macOS Apple Silicon** | deepsentry-darwin-arm64 |
| **macOS Intel** | deepsentry-darwin-amd64 |
| **Linux 64 位 x86** | deepsentry-linux-amd64 |
| **Linux ARM 64 位** | deepsentry-linux-arm64 |
| **Windows 64 位** | deepsentry-windows-amd64.exe |

unzip deepsentry-v2.0.6-all-platforms.zip
shasum -c SHA256SUMS

如果你沿用 2.0.x 的 config.yaml，升级后建议先跑一次只读任务，确认模型、聊天通道和 MCP 都通，再执行修改型操作。macOS 首次运行如果提示“无法验证开发者”，先处理 quarantine 属性再执行。

08边界与提醒

工具越能干，越要把适用范围写在明面上。

只在你拥有、或已获得明确书面授权的系统上使用。

任务描述、必要上下文和工具结果会发送给你配置的大模型服务；涉密环境请改用受控本地模型，公开报告和截图前先脱敏。

Linux 桌面操作依赖 X11；Windows / Linux 的真实桌面链路仍需在目标环境验收。

macOS 的 computer-use-helper 采用临时签名，需要屏幕录制与辅助功能权限；面向生产分发应使用 Developer ID 签名并公证。

复杂 Word 模板、扫描件 OCR、图片内容理解超出 2.0.6 的文档能力范围，请配合专用工具。

扫描、探测、抓包、代理转发都属于会产生实际影响的操作，务必确认授权范围；生产环境不要用无人值守自动批准替代人工确认。

安全工具最后拼的不是功能列表有多长，而是能不能把一次排查稳定地变成一份可复核的交付。2.0.6 把搜索、思考、文档和连接各补齐了一格——剩下的，交给你在自己的授权环境里验证。

仓库地址：github.com/asaotomo/DeepSentry。如果它帮你省下过排查时间，欢迎回仓库点个 Star。遇到问题可以开 Issue，提问前请去掉 API Key、密码、真实客户地址和未脱敏截图；安全漏洞请走 Security Advisories，不要开公开 Issue。

参考链接

**1. DeepSentry 仓库（README / 使用说明）**
https://github.com/asaotomo/DeepSentry

**2. v2.0.6 Release 与下载**
https://github.com/asaotomo/DeepSentry/releases/tag/DeepSentry\_v2.0.6\_Ultimate

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO96vQKict5Njccs0NxhzcTHbkVeVnSnNvIwf6d01l7x12WMEFaxAwJIPG1feicAbYLzUoDjBbAvhRE9t9FbusNWcVHpIUs20TSyc/0?wx_fmt=png)

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