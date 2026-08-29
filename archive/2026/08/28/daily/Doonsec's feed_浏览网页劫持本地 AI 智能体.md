---
title: 浏览网页劫持本地 AI 智能体
url: https://mp.weixin.qq.com/s/6EImMB_pEhT_zq3wLmK-bw
source: Doonsec's feed
date: 2026-08-28
fetch_date: 2026-08-29T08:30:20.603149
---

# 浏览网页劫持本地 AI 智能体

# 浏览网页劫持本地 AI 智能体

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

你有没有想过，仅仅点开一个网页，本地运行的 AI agent（AI 智能体）就会被悄悄接管，后续每一轮对话都在执行攻击者的隐藏指令，而使用者完全察觉不到异常。

Cyera 与 Oasis Security 最新发布的安全研究就揭露了这样一类 Drive‑By Agent Hijacking（路过式智能体劫持）攻击，对应 NVIDIA NemoClaw 的高危漏洞 CVE‑2026‑65105，给正在快速普及的本地 AI 部署敲响警钟。

NemoClaw 是 NVIDIA 推出的工具，专门用来把开源 AI 智能体 OpenClaw 部署到 NVIDIA OpenShell 沙箱内部，沙箱原本会提供文件系统、网络、进程层面的隔离，本意就是降低 AI 智能体越权操作主机的风险。在推理运行环节，NemoClaw 支持多种后端，其中一个主流方案就是对接 Ollama，开发者可以把大模型完全跑在自己本机硬件之上，不用把提示词、业务代码上传第三方云端 API，数据全部留在本地，这也是很多企业和开发者选择本地大模型的核心原因。

为了让 Docker 容器内部的 OpenShell 沙箱能够访问主机上的 Ollama 服务，NemoClaw 启动 Ollama 时会把监听地址设置成`OLLAMA_HOST=0.0.0.0:11434`，也就是绑定机器全部网络接口。这里存在一处极具迷惑性的细节，程序输出日志会提示`Using Ollama on localhost:11434`，很容易让使用者误以为服务只允许本机回环访问，实际上外部网络、局域网设备都可以触达这套 Ollama 的 API 接口，而 Ollama 本身的 11434 端口 API 是完全没有身份认证机制的。

很多人会好奇，Ollama 难道没有自带防护吗，其实 Ollama 设计了两层浏览器攻击防护，分别是 CORS 中间件和 Host 头部校验。CORS 中间件会校验请求的 Origin 来源头部，Host 头部校验则只放行`localhost`、本机主机名、`.localhost`、`.local`这类本地域名，这套组合防护原本就是用来抵御网页侧发起的本地服务攻击。但是这里藏着关键逻辑缺陷，一旦 Ollama 绑定到非回环地址例如`0.0.0.0`，程序就会直接跳过全部 Host 头部校验，只剩下 CORS 一层屏障，而 DNS rebinding（DNS 重绑定）攻击技术刚好可以绕过 CORS 的限制。

DNS rebinding 是一套成熟的浏览器攻击手段，攻击者只需要拥有一个自己控制的域名，不需要操控受害者的局域网或者 DNS 基础设施就可以完成攻击。攻击域名初始解析指向攻击者的公网服务器 IP，受害者访问网页之后，浏览器加载页面内的 JavaScript 脚本，攻击者迅速修改 DNS 解析记录，把同一个域名解析地址切换到`127.0.0.1`或者受害者局域网 IP。浏览器同源策略的判断依据是域名，不是最终解析得到的 IP 地址，浏览器依旧把后续请求判定为同源，直接把请求发送到本机 11434 端口的 Ollama 服务上。此时因为 Ollama 绑定在`0.0.0.0`，Host 校验已经失效，Origin 头部又匹配攻击者域名，CORS 校验直接放行，攻击者就此拿到 Ollama API 完整的无认证访问权限。

拿到 API 权限之后攻击者可以执行的操作远比想象中丰富，不止调用 GPU 跑推理任务，还可以读取全部已安装模型的版本、量化参数、系统提示词、模板配置，获取主机主机名、Ollama 公钥等敏感信息，也能下载大量模型占满磁盘空间、删除本机模型、强制登出账号，甚至把本地模型推送上传到ollama.com平台。但整个攻击链条中破坏力最强的，并不是简单调用接口，而是**模型模板注入（template injection）**，实现持久化的模型投毒。

这里需要区分两种投毒思路，直接修改模型内置 system 字段的提示词注入是行不通的，OpenClaw 智能体每次发起请求会在 messages 数组中携带自身的系统提示词，会直接覆盖模型内置的 system 配置，攻击者植入的指令会被直接忽略。真正奏效的攻击点是 Ollama 的 template 模板，这是一套 Go template 模板，它会在推理阶段把结构化的 messages 消息数组渲染拼接成模型真正接收的原始文本，这套模板属于模型层面的属性，调用 API 的上层客户端没有读取、感知、拦截它的能力。

攻击者先调用接口拉取原始模板完整内容，在不破坏原有工具渲染逻辑、特殊标记符的前提下，往系统消息的末尾拼接攻击者自定义的隐藏指令，再通过`/api/create`接口写回模型配置。之后无论上层 AI 智能体传入什么样的 system 系统提示词，在送入大模型之前，恶意指令都会被自动追加进去，模型名称、文件大小、元数据看不出任何改动痕迹，这套恶意逻辑会留存下来，作用于之后每一次对话，CLI 命令行、API 调用、AI 智能体全部都会受其影响，普通使用者完全无从分辨。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqiaIpzHK7M5BXuLhGO8QhpTBDKbKJUpK6Nxpvz8AkwM8yhzSav2EXXuwKuZUhbOiacMPFA2lp3IvtmzsBXxkWNtKIScSibJcu9Mo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDojlw3kN2a5wKutvdFRfJ8ej1YYlichEmBy30iapcpLPMMnNH5YRibbqpE1LgzvHO3dOUvDHH7vqRxN2tuWdbaYnP2PedtJaYJsEs/640?wx_fmt=png&from=appmsg)

被投毒之后的 AI 智能体会在完全静默的状态下执行攻击者意图，它可以生成暗藏漏洞的代码，并且在人工简单审查的时候伪装正常，可以主动屏蔽安全告警、不再输出风险提醒，引导使用者选用攻击者可控的软件包、链接、配置，如果智能体具备对外网络访问权限，还会偷偷把对话记录、读取到的本地文件外传。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpF5ERdlLNAGUria5XGwrNRw3nJ7c6ia10aIqeTibo323ekFSDFQaYJcpvMhp66qcNCctVwCPL9dlTKdokHYCqHPTZQ7kMTzicKRuc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrquJdFeOoByoslRM6JicialQD1u9srwJXJXyBuQnocxl3YuvS3ngBD2qsbfrsYicvdOIObv10toIxxFRFrbW0wL2TV6o1xYyvzgw/640?wx_fmt=png&from=appmsg)

很多开发者会产生疑问，OpenShell 不是部署了沙箱吗，为什么还会造成严重后果，沙箱确实可以隔离主机的文件、进程、基础网络访问，保护终端设备本体不被直接破坏，但现实生产环境当中，AI 智能体往往会被授予大量业务权限，对接代码仓库、CI/CD 流水线、内部 API、云服务、MCP servers 工具服务。攻击者劫持的不是主机，而是**智能体本身拥有的合法权限**，攻击影响范围不再受沙箱边界约束，而是取决于这套 AI 智能体被分配了多少内部业务资源访问权限。除此之外`0.0.0.0`的绑定配置还会把 Ollama 直接暴露给整个局域网，同网络下的其他沦陷设备、物联网设备都可以直接访问 API，不需要借助 DNS 重绑定就能发起攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpY7tJjJja11FpH2oMtnTZfaOeiaCLVt9J8lHMuwgRroQic4SXL8vyqk6P9OpzCUd5ws3UmAyXWzK50eGYQIYePTricny5FlR3iccU/640?wx_fmt=png&from=appmsg)

研究团队也放出了完整 POC 演示视频，整个攻击流程可以完整复现，从访问恶意网页，到窃取本机 Ollama 信息，改写模型模板，再回到智能体对话界面，相同提问已经带出注入标记，全程没有弹窗，没有用户确认交互，全部在后台完成。相关研究已经遵循负责任披露流程，提前把全部漏洞细节提交给 NVIDIA 的 PSIRT（产品安全事件响应团队）。

这项漏洞带给我们几条很现实的安全启示，首先给 AI 智能体做沙箱隔离是必要条件，但远远不等于安全，威胁的爆炸半径由智能体被授予的业务权限决定，而不是沙箱本身；其次服务绑定`0.0.0.0`不只是一项简单网络配置，更是重要安全决策，没有身份认证的本地服务，除非完整评估风险并做好防护，否则严禁绑定全部网络接口；DNS rebinding 这类老旧攻击手段，在本地 AI 大模型兴起之后又找到了新的攻击目标，当 Ollama 被绑定到非回环地址，原本用来抵御该攻击的 Host 头部校验就会失效。

随着 AI agent 深度融入开发流程和企业内部工作流，安全边界已经不只是模型权重文件，聊天模板、网络监听配置、推理后端接口每一个环节，都需要纳入安全防护的考量范围。本地大模型带来隐私优势的同时，也丢掉云厂商集中式安全防护，开发者不能默认本地部署就更加安全。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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