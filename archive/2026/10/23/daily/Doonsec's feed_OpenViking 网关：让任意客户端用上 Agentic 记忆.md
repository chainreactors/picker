---
title: OpenViking 网关：让任意客户端用上 Agentic 记忆
url: https://mp.weixin.qq.com/s/odoGjnnUwzAwppQXv08F0A
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:39.408964
---

# OpenViking 网关：让任意客户端用上 Agentic 记忆

# OpenViking 网关：让任意客户端用上 Agentic 记忆

原创

OpenViking
OpenViking

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个项目聊到第三天，你希望 AI 接着上次的结论往下做，而不是重新问一遍背景。要做到这一点，它需要在回答时找到之前的信息，也需要把新的进展保存下来。但接入记忆并不总是方便。有的客户端能装插件，有的只能聊天；有的脚本可以调用模型，却没有检索、读取和保存记忆的逻辑。

**OpenViking 网关把这些工作接了过来。**它位于客户端和模型服务之间，帮助模型查找和使用 OpenViking 中的记忆，让兼容客户端不必各自实现一套记忆功能。

**一、它能帮你做什么**

网关提供三项能力，分别对应对话里的三个问题。

**之前说过什么？自动找。**你发出新消息后，网关会查找相关记忆，连同问题一起发给模型。这样，模型回答时就能参考之前的背景。

**信息不够怎么办？继续查。**你问“上次定的发布日期是哪天”，模型可以先搜索，再打开对应原文确认。检索和读取由网关执行，客户端不需要自己支持这些工具。

**这次聊出的内容怎么办？保存下来。**开启对话保存后，OpenViking 会从中整理出有用信息，供以后使用。对话太长时，网关还可以让模型生成摘要，缩短后续请求中携带的历史内容。

**AI 不只是被动收到一段背景，还能在需要时自己查找和使用记忆。如果开放了保存工具，它也能按你的要求记住内容。**

**二、接入主要改两项配置**

在已经部署好网关的前提下，兼容客户端主要调整两项设置：

* **Base URL：**模型接口地址，改为网关地址，即网关所在服务的地址加 /gateway。
* **API Key：**访问凭证，换成在 Studio 中签发的网关密钥。

不需要再为这些客户端安装 OpenViking 插件，也不用单独编写记忆处理代码。Claude Code 还需增加一项环境配置，用来区分它的后台请求，具体步骤见文末接入指南。

Studio 是网关的管理页面，可以设置连接哪个模型、是否保存对话，以及允许模型使用哪些工具。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fee4cSrMlWkMXmAMTYxFJsFu52bwD9pUicDZwInficpFic0AQ0sT8lEpliagNnxic4B1sA5vEKxZUSiaKqMPd7NTo0p57p1WKribe5qy4E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Feeibm02QljVEKTrf8tM5ag28ymICWNDXeub2ZmGWhM4I1mJIofNDOf5FF49EzibyN7cg1nXeK2sXBVCibxV9kibr6hEYBP06w9zXgw/640?wx_fmt=png&from=appmsg)

模型服务和运行情况也能在这里查看，不必在每个客户端里分别维护。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeVPpKDC4VM74NP3JMJJK0CQJlvibu9iar76QBZm5asCxGbLfWJre8vwiazn4UJ70mGibYnDdGz27hibWXf7uibtaBhDw1ibVBJnhezww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fec9ib5JyDYDn8xbI5NL8U1CzZhyvFEHGTHMqABaDAMylNAicpEgb50XddOHbD6twXRfL9PaS4b7xWLVetyibKut0wLiaibTiaFP2ogyk/640?wx_fmt=png&from=appmsg)

网关可以随 OpenViking Server 一起运行，也可以独立部署、连接已有的 OpenViking 服务，包括火山引擎托管服务。更多原理可查看官网：https://openviking.ai/gateway

**三、哪些客户端可以用**

网关主要面向能自定义模型接口地址、并满足接口要求的聊天应用、自己写的调用脚本和低代码平台。对已有的编程 Agent，它也可以补充记忆能力。

在已完成的测试中，Claude Code、Codex CLI 和 OpenAI Python SDK 已验证能查找和保存记忆；Cherry Studio 的纯聊天模式也能使用记忆工具。其他客户端仍需按实际环境验证。

下图是 Cherry Studio、pi 和 Codex 的接入示例，均未安装 OpenViking 插件，只更换了模型来源。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FefkbBPXiaGWoptkCQg7zDnibucJjVI2enKztQua2UwygfUzr9vXqAO9iaQ4j8ibG72apJ8icuiay7iajyNXtLg1ic0amlxEqBEqkZM3cXs/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeejUBPaia4KhTVClJGnaMACK5Bvrh7kmRcjwsNcuQqVktMFiacTbQg9lScG55opOtFmgaX8kkWSwdJp4v2nvA5WRCyZq5SbS6nYs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeedgicrZfB0zs6Snj2tRt58QAMn1LxiaiaYXbmzic30ibPturKtDLMqVS2AQ5S02ngzLQVTFrxFW331LHRseX9qVS5P0iaTnnpYUmarA/640?wx_fmt=png&from=appmsg)

能改地址不代表所有调用方式都支持。客户端还需要把完整聊天记录带给模型；只用订阅账号登录，或由厂商服务器发起模型调用的方式，不适用这条接入路径。具体支持情况以接入指南为准。

**四、一张图看懂架构**

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fef4ibK5xiaXhmgL6YY0ulUKmvc99Mn2j7b460ejFVicunvlURnW17gentM5RrR7juVofE3D4ZCCYxzDl8SadPoH5D7wPtpeZFFia4o/640?wx_fmt=png&from=appmsg)

* **运行在哪：**网关可以嵌入 OpenViking Server，和 Server 共用端口；也可以用 openviking-gateway 独立运行，连接已有的 OpenViking 服务（例如火山引擎托管的 OpenViking）。两种形态下，客户端地址都是服务地址加 /gateway（见“部署方式”）。
* **和 OpenViking 的关系：**网关只调用 OpenViking 的公开接口，向量化和记忆提取都在 OpenViking 里做。
* **数据在哪：**会话和记忆的正本在 OpenViking；网关本机只有两个 SQLite 文件，一个存上游、密钥和配置，一个存对话状态（见图），对话闲置 30 天过期。加密、删除与隔离见“安全与数据边界”。
* **出故障时：**OpenViking 不可用时对话照常，只是不带记忆，写回自动重试。网关停止服务时（嵌入形态下即 OpenViking Server 停止时），经过它的模型调用全部失败。
* **谁来管：**用户在 Studio 给自己签发网关密钥，账号管理员也能替本账号用户签发。每把密钥绑定一位 OpenViking 用户、一份**上下文配置**（召回预算、是否写回、开放哪些工具）和一组**上游**（转发到的模型服务地址和 Key）。

**五、接入后，对话会发生什么**

网关自动认出同一段对话，只有用户的新消息触发召回，工具步骤和辅助请求不召回。压缩切点之前的原文不再发给模型，模型可以用 OpenViking 工具回会话里查原文。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fed8BteclNibibhTiaRJbcpgdAbQ5icRGVaibQWwqZ4XEmOwdQUEApvuFeKXv1ialN0j4icj4W5tDGFic9h4eib9BNXOPAdeP3WSwyXKuAqc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecVzBMxOES0AmW6Ql3gH95mF2DmATibUfYez1cq0aCXyDQPh5B6HDo5IZXpXoUNgybrNRsJeBiaZMDyWktQ8C6dnZuYLUqdP4d0I/640?wx_fmt=png&from=appmsg)

**六、让任意客户端拥有 Agentic 记忆**

自动召回是网关替模型猜它需要什么；有了 OpenViking 工具，模型自己决定查什么、读什么、记什么。工具由网关执行，客户端不用声明或实现任何工具，请求里一个工具都没有也能用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecWXhBvPEMvcN9UzviaCibbpciaGibEU71XhJVajgcOiab6aSTDY1lP6t61a0gicq9aX5okKCNrXnAHhuyl6XwggRibBe8dMmAvnSMdF0/640?wx_fmt=png&from=appmsg)

* **一条回复里的多步操作：**网关拦下模型发出的 OpenViking 工具调用，用该用户的 OpenViking 密钥执行，把结果接回再问模型，直到模型不再调用。客户端只收到一条连贯的回复。
* **客户端自己的工具照常用：**同一条回复里可以同时调用 OpenViking 工具和客户端工具（例如 Bash），客户端的调用原样交给客户端执行，照常经过它的权限确认。
* **下一轮还记得：****工具往返**（模型发出的工具调用和网关拿回的结果）不在客户端历史里，网关把它们存下来，下一轮原样放回，模型记得查到过什么，提示缓存也不断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefLdZicXsicM69IIPP6pzKWIibMGibvWiaxL7HjfQIRrBY7pLicynR6gvuciac4LB66uvjBW4b31vrVyibwX7ibI3uZ8e77ru5E7dUta2G0/640?wx_fmt=png&from=appmsg)

**6.1 模型能用哪些工具**

工具直接来自所连 OpenViking 服务的工具清单，随服务端版本增减，名字前加 openviking\_。写入、导入、删除和改权限这几类会改数据的工具默认不勾选，其余默认勾选（包括 OpenViking 以后新增的工具，开放前可以先看一眼清单）。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fec9KQzN9ibkyWoqGrN8ycmn1ibV1AsZQMkWhR5bHibTMgk5O2gjklWac6wobMRCaMoesCa1nuyZKGVp1rJ7fqhq6sFtUvEX9s3U0g/640?wx_fmt=png&from=appmsg)

**七、部署方式**

网关有两种运行形态，客户端用法相同：地址都是服务地址加 /gateway，只改 Base URL 和 API Key。详细步骤见官方文档 **OpenViking 网关部署与运维（https://docs.openviking.ai/zh/guides/22-gateway-operations）**

**7.1 开始前准备**

* 已有可用的 OpenViking。运行网关的本机安装 OpenViking **0.5.1 及以上**；本地 OV 已配置好 embedding 和 VLM。
* 准备火山方舟 API Key；路径 B 还需准备自己的 **OV 用户 API 密钥**。本机已安装 Claude Code，可运行 claude，并有 curl。
* 以下命令适用于 macOS / Linux 终端，默认仅供本机访问。需要升级时，在原安装环境执行：

```
python -m pip install --upgrade openviking
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefTpz1sBsMwiaKnMDmBmoicJZZkkurVpUoeJSuibg8KHfn5DjRfSQ5vADzonGiccPuGwiaqpJQPD8k9PKiaZTHmDYpI91pKrK01Fakibg/640?wx_fmt=png&from=appmsg)

**7.2 路径 A：本地 OV**

网关与已有 OV 共用端口，地址为 http://127.0.0.1:1933/gateway。以下以本地 dev 模式为例。

**A1 开启网关**

终端执行：

```
openviking-server init
```

1. 用方向键选 **Update gateway (now: disabled)**，按回车。**不要直接确认默认的 Start over**，它会重新配置整套服务。
2. 在 Enable OpenViking Gateway on the same port? 输入 y。
3. 在 Save configuration? 按回车保存；原配置自动备份为 ov.conf.bak。
4. 在 Validate the setup now? 输入 n，网关稍后单独验证。
5. 如果 OV 已在运行，Start the server now? 选 N，按 A2 重启；如果未运行，可选 y 直接启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee0xKcYf9WgXKP2fZst9B8DLphHYfEO763MlZlD6LbqG2J0BvM4Ch3S25p0ciaHFUvEOzBAwvfuoGA5qSicSPA403wpSal6KwGhE/640?wx_fmt=png&from=appmsg)

图 1｜用方向键选中 Update gateway，再按回车

默认配置文件为 ~/.openviking/ov.conf。若使用其他路径，执行 OPENVIKING\_CONFIG\_FILE=/实际路径/ov.conf openviking-server init，启动时也指定同一文件。自建 api\_key 服务若禁止用户自行配置上游，需保存向导生成的 ovgm\_… 管理密钥。

**A2 重启并检查**

1. 若服务在原终端前台运行，按 Ctrl-C 停止，然后执行下方启动命令；若由进程管理器托管，用原方式重启，不要重复启动。

```
openviking-server --config ~/.openviking/ov.conf
```

2. 保持服务运行，另开终端执行：

```
curl -s http://127.0.0.1:1933/health; echocurl -s http://127.0.0.1:1933/gateway/v1/models; echo
```

**成功标准：**第一条返回"status":"ok"；第二条返回 **401 / Invalid gateway key**，表示网关已挂载，只是还没带密钥。若为 404，检查是否启用并重启。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeePRV9b8EUlEociacCd6WqXyYgC2IowGJSZjPhUJpUI3bJJ4lLz14UUPGN1eZafEQoeuI5X1zQqTqjR7VNngwn1xhfjrDrZEHEU/640?wx_fmt=png&from=appmsg)

图 2｜未携带密钥时返回 401，是本步骤的预期结果

**A3 进入 Studio**

1. 浏览器打开 http://127.0.0.1:1933/studio/。
2. 首次连接选择 **开源服务 → 添加新服务地址**，手动输入 http://127.0.0.1:1933，点 **下一步**；灰色占位地址不算已填写。
3. 本地 dev 模式的用户 API 密钥留空，点 **验证连接 → 进入** Studio。自建 api\_key 服务在此填用户 API 密钥。
4. 左侧选择 **OpenViking 网关**，然后跳到“通用配置与接入”。

**成功标准：**连接验证成功，能打开网关页面。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fee0hibwqbo4aRDsLwH1TjlNM3l6eMFkQW2hsDVkctJtNlGqFnJRiaqXIE8cLSnzrrMbotxfau5G2H9micy0fSMzfAtXic8l6Tyk7wk/640?wx_fmt=png&from=appmsg)

图 3｜本地 dev 模式无需 API 密钥，验证成功后进入 Studio

**7.3 路径 B：火山托管 OV**

本机运行独立网关，连接已有托管服务；记忆仍保存在托管 OV。网关地址为 http://127.0.0.1:1935/gateway。

**B1 初始化独立网关**

终端执行：

```
openviking-gateway init
```

按提示依次填写：

1. OpenViking server URL：输入 https://api.vikingdb.cn-beijing.volces.com/openviking。
2. Listen host：回车，保持 127.0.0.1。
3. Listen port：回车，保持 1935。
4. Require a management key to change upstreams and profiles?：输入 y。
5. 立即保存生成的ovgm\_…管理密钥，只显示一次。 配置写入 ~/.openviking/gateway.conf。

**成功标准：**向导保存配置，并生成管理密钥。商业版显示 Version: unknown 不代表连接失败。

![](https...