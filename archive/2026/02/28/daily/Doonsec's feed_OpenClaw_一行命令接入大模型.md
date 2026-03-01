---
title: OpenClaw:一行命令接入大模型
url: https://mp.weixin.qq.com/s/cVX1_1Gg4d7ljFyiYlJ60A
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:17:27.173830
---

# OpenClaw:一行命令接入大模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAf9IMALLwgKPzQjZbPm5EjMBEMFEEoLHoHopw61MU7KoCj0yhQ6IRia3obhbmZaXsq7WZ0ltVlX3DbqQC5ia16lOsao2eEdzFPiaouia6S1bgk/0?wx_fmt=jpeg)

# OpenClaw:一行命令接入大模型

原创

糖果LUA
糖果LUA

AI安全运营

![]()

在小说阅读器中沉浸阅读

目前OpenClaw添加一个新的大模型 provider 最快的方式是通过命令行直接写入配置，主流做法有两种：

1. 最推荐、最快的方式（适用于绝大部分 OpenAI 兼容接口的模型）
   使用 openclaw config set 一行命令直接添加 provider
2. 手动编辑配置文件（更保险，但稍微慢一点）

方式一：一行命令快速添加（推荐）绝大多数国内/国外第三方大模型都兼容 OpenAI 接口，用下面这套模板就行：

```
# 格式
openclaw config set'models.providers.你的provider名字'--json'{
  "baseUrl": "https://api.xxx.com/v1",
  "apiKey": "sk-你的密钥",
  "api": "openai",           # 或 "openai-completions" / "anthropic-messages" 等
  "models": [
    {
      "id": "模型实际名字",
      "name": "显示的名字（随便起）",
      "reasoning": false,
      "input": ["text"],
      "cost": {"input":0,"output":0,"cacheRead":0,"cacheWrite":0},
      "contextWindow": 131072,
      "maxTokens": 8192
    }
  ]
}'--json
```

案例1. 接入硅基流动 / siliconflow（非常快）

```
openclaw config set'models.providers.siliconflow'--json'{
  "baseUrl": "https://api.siliconflow.cn/v1",
  "apiKey": "sk-你的siliconflow key",
  "api": "openai",
  "models": [
    {
      "id": "Qwen/Qwen3-32B-Instruct",
      "name": "Qwen3-32B",
      "contextWindow": 131072,
      "maxTokens": 8192
    },
    {
      "id": "deepseek-ai/DeepSeek-R1",
      "name": "DeepSeek-R1"
    }
  ]
}'--json
```

然后设置默认模型：

```
openclaw config set'agents.defaults.model.primary''siliconflow/Qwen/Qwen3-32B-Instruct'
```

2. 接入 GLM-5 / 智谱（国际版或代理）

```
openclaw config set'models.providers.zhipu'--json'{
  "baseUrl": "https://open.bigmodel.cn/api/paas/v4",
  "apiKey": "你的智谱key",
  "api": "openai",
  "models": [{"id": "glm-5","name": "GLM-5","contextWindow": 200000}]
}'--json
```

3. 接入本地 Ollama / vLLM / llama.cpp

```
openclaw config set'models.providers.local'--json'{
  "baseUrl": "http://127.0.0.1:11434/v1",
  "apiKey": "ollama",
  "api": "openai",
  "models": [{"id": "qwen2.5:32b","name": "Qwen2.5 32B"}]
}'--json
```

方式二：直接编辑配置文件（更可控）

```
# 打开配置文件（推荐用 nano / vim / code）
code ~/.openclaw/openclaw.json
# 或者
nano ~/.openclaw/openclaw.json
```

在 models.providers 里加一个新对象，例如：

```
"models":{
"providers":{
"myprovider":{
"baseUrl":"https://api.example.com/v1",
"apiKey":"sk-xxxx",
"api":"openai",
"models":[
{
"id":"model-name",
"name":"My Awesome Model",
"contextWindow":128000,
"maxTokens":8192
}
]
}
}
}
```

保存后执行：

```
openclaw models status          # 查看是否识别
openclaw models list            # 列出所有可用模型
```

然后设置主模型：

```
openclaw config set'agents.defaults.model.primary''myprovider/model-name'
```

快速验证是否成功

```
# 查看当前所有 provider 和模型
openclaw models list

# 测试对话（走默认模型）
openclaw chat "你好，请告诉我今天日期"
```

基本上 1–2 分钟就能搞定一个新 provider。祝使用愉快～如果遇到某个具体厂商的坑（比如 anthropic 格式、MiniMax 特殊头、火山引擎 region 等），可以告诉我模型名字，我帮你写最适配的命令。

以下是针对你提到的三种特殊情况，在 OpenClaw中最可靠的配置写法。这些 provider 都不走纯标准的 OpenAI Chat Completions 接口，所以 api 字段必须改成对应的值，否则工具调用、缓存、思考链等功能容易出问题。

1. Anthropic 原生格式（Claude 系列、直连或代理）Anthropic 必须用 anthropic-messages，否则 tool\_use / tool\_result 会解析失败，prompt caching 也用不了。一行命令写法（推荐）

```
openclaw config set'models.providers.anthropic-direct'--json'{
  "baseUrl": "https://api.anthropic.com/v1",
  "apiKey": "sk-ant-api03-你的key",
  "api": "anthropic-messages",
  "models": [
    {
      "id": "claude-opus-4-6-20250215",
      "name": "Claude Opus 4.6",
      "reasoning": true,
      "contextWindow": 200000,
      "maxTokens": 8192,
      "cost": {"input":3,"output":15}
    },
    {
      "id": "claude-sonnet-4-5-20250120",
      "name": "Claude Sonnet 4.5"
    }
  ]
}'--json
```

然后设置默认：

```
openclaw config set'agents.defaults.model.primary''anthropic-direct/claude-opus-4-6-20250215'
```

如果用代理（如 apiyi、siliconflow 转 anthropic）
把 baseUrl 改成代理地址，api 还是 anthropic-messages（确认代理支持原生 messages 接口）。

2. MiniMax（强烈推荐用 anthropic-messages 模式）MiniMax 官方最稳的是 Anthropic 兼容端点（尤其是 M2.1 / M2.5 系列），支持 prompt caching 和 native tool calling。一行命令写法（2026 年主流）

```
openclaw config set'models.providers.minimax'--json'{
  "baseUrl": "https://api.minimax.io/anthropic",
  "apiKey": "你的 MiniMax key（eyJhbGciOi...）",
  "api": "anthropic-messages",
  "models": [
    {
      "id": "minimax-m2.5",
      "name": "MiniMax M2.5",
      "reasoning": true,
      "contextWindow": 1000000,
      "maxTokens": 32000
    },
    {
      "id": "minimax-m2.1",
      "name": "MiniMax M2.1"
    }
  ]
}'--json
```

设置默认：

```
openclaw config set'agents.defaults.model.primary''minimax/minimax-m2.5'
```

备选（如果必须用 OpenAI 兼容端点）
把 baseUrl 改成 https://api.minimax.io/v1，api 改成 openai，但工具调用稳定性会差一些。

3. 火山引擎 Ark（volcengine / ark）火山方舟 Coding / Pro 模型目前主流用 OpenAI 兼容接口，但 endpoint 带 region，要指定 coding 或通用 v3。一行命令写法（以 ark-code-latest 为例）

```
openclaw config set'models.providers.volc-ark'--json'{
  "baseUrl": "https://ark.cn-beijing.volces.com/api/coding/v3",
  "apiKey": "你的 Ark API Key",
  "api": "openai-completions",
  "models": [
    {
      "id": "ark-code-latest",
      "name": "Ark Code Latest (Coding Plan)",
      "contextWindow": 131072,
      "maxTokens": 8192
    },
    {
      "id": "doubao-1.5-pro-32k",
      "name": "Doubao 1.5 Pro 32k"
    }
  ]
}'--json
```

如果用通用 endpoint（非 coding 专用）：

* baseUrl 改成 https://ark.cn-beijing.volces.com/api/v3
* id 改成模型的 endpoint id（如 ep-202502xxxxxx 或 doubao-lite-32k 等，从控制台复制）

设置默认：

```
openclaw config set'agents.defaults.model.primary''volc-ark/ark-code-latest'
```

快速验证 & 常见坑执行后跑下面命令检查：

```
openclaw models list                # 看是否出现新 provider 和模型
openclaw models status              # 检查连通性
openclaw chat "测试一下，你支持工具调用吗？给我当前日期"# 简单验证
```

最常见失败原因排序：

1. api 字段写错（anthropic 系列必须 anthropic-messages）
2. baseUrl 带了多余的 /v1 或少了 /anthropic
3. key 过期 / 配额超 / region 不对（火山默认 cn-beijing，少数用 cn-north-1）
4. 模型 id 写错（尤其是火山，要从控制台复制 endpoint id）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAf9IMALLwj2xL4gbsg62IEGTSjAmiaSHSljHPKG0uP790YgTjWh3uHyjLXGAtjXeDhy6OWrSUG3mGQo2qibgrJgthUeL1pM68PeXY3ftrnIU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

AI安全运营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

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