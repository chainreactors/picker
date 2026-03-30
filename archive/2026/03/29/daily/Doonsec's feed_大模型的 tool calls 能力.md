---
title: 大模型的 tool calls 能力
url: https://mp.weixin.qq.com/s/dHjAuKU5cO6YlJa3RzVzgQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:15.262285
---

# 大模型的 tool calls 能力

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LjdkpgSF7PefZKJFCgzxKEYOibsUDX5DMiarqT2xllkhrcnHhRPeCyqxzfCFcvHhV75E8ycTGvaPhWcJg9ibpD2CqtqjNKicK1iaGBsYicywcM2Lw/0?wx_fmt=jpeg)

# 大模型的 tool calls 能力

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器中沉浸阅读

大模型的各项能力中有一项能力叫 “tool calls“，如果直接翻译就叫"工具调用"。

什么是 tool calls 的能力？

在 deepseek 模型的官方文档中有这么一个表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfIK3ezbXFo1wA0nnhgibuiatRZDkmJoBkbDBlm08YiaOxTeRdF9kJTIj8zytYdhNwibGBsLPQl9XfXXUk5U6hvnDKeKbzIQD8ZL9o/640?wx_fmt=png&from=appmsg)

```
https://api-docs.deepseek.com/zh-cn/quick_start/pricing
```

关于 tool calls 的解释，文档中是这样说的：

Tool Calls 让模型能够调用外部工具，来增强自身能力。

DeepSeek API 文档给出了 tool calls 的 API 示例：

```
from openai import OpenAI
def send_messages(messages):    response = client.chat.completions.create(        model="deepseek-chat",        messages=messages,        tools=tools    )    return response.choices[0].message
client = OpenAI(    api_key="<your api key>",    base_url="https://api.deepseek.com",)
tools = [    {        "type": "function",        "function": {            "name": "get_weather",            "description": "Get weather of a location, the user should supply a location first.",            "parameters": {                "type": "object",                "properties": {                    "location": {                        "type": "string",                        "description": "The city and state, e.g. San Francisco, CA",                    }                },                "required": ["location"]            },        }    },]
messages = [{"role": "user", "content": "How's the weather in Hangzhou, Zhejiang?"}]message = send_messages(messages)print(f"User>\t {messages[0]['content']}")
tool = message.tool_calls[0]messages.append(message)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})message = send_messages(messages)print(f"Model>\t {message.content}")
```

这个例子中没有给出 get\_weather 的实现，例子跑不起来。我在 ollama 下完成了一个可实际执行的例子，其中 get\_current\_weather() 是 dummy 函数，主要用来演示 tool calls 的用法。

```
import jsonfrom openai import OpenAI# 1. 初始化客户端 - 使用 Ollama APIclient = OpenAI(    base_url="http://192.168.1.1:11434/v1",    api_key="ollama"  # Ollama 本地运行通常不需要 API key，这里任意填写即可)# 2. 定义工具（函数）的 schematools = [    {        "type": "function",        "function": {            "name": "get_current_weather",            "description": "获取指定城市的实时天气",            "parameters": {                "type": "object",                "properties": {                    "location": {                        "type": "string",                        "description": "城市名称，例如：北京、上海"                    },                    "unit": {                        "type": "string",                        "enum": ["celsius", "fahrenheit"],                        "description": "温度单位"                    }                },                "required": ["location"]            }        }    }]# 3. 模拟实际执行的天气查询函数（实际可替换为 API 调用）def get_current_weather(location, unit="celsius"):    # 这里仅为演示，返回模拟数据    weather_data = {        "北京": {"celsius": 22, "fahrenheit": 72, "condition": "晴朗"},        "上海": {"celsius": 26, "fahrenheit": 79, "condition": "多云"},    }    data = weather_data.get(location, {"celsius": 20, "fahrenheit": 68, "condition": "未知"})    # 不区分大小写处理 unit 参数    unit_lower = unit.lower() if unit else "celsius"    temp = data[unit_lower]    condition = data["condition"]    return f"{location}当前{condition}，气温{temp}°{'C' if unit_lower=='celsius' else 'F'}"# 4. 用户对话messages = [    {"role": "user", "content": "北京今天天气怎么样？"}]# 第一次请求：模型判断是否需要调用工具response = client.chat.completions.create(    model="gpt-oss:20b",  # 请替换为你在 Ollama 中实际使用的模型名称，例如：llama3.1, gemma, qwen2 等    messages=messages,    tools=tools,    tool_choice="auto"   # auto 让模型自主决定是否调用)# 获取模型返回的消息response_message = response.choices[0].messagetool_calls = response_message.tool_calls# 5. 如果模型决定调用工具，则处理调用请求if tool_calls:    # 将模型的原始回复追加到对话历史    messages.append(response_message)    # 遍历模型请求的所有工具调用（本例只有一个）    for tool_call in tool_calls:        function_name = tool_call.function.name        function_args = json.loads(tool_call.function.arguments)        # 执行对应的函数        if function_name == "get_current_weather":            result = get_current_weather(                location=function_args.get("location"),                unit=function_args.get("unit", "celsius")            )        else:            result = f"未知工具: {function_name}"        # 将工具执行结果作为新消息加入历史        messages.append({            "role": "tool",            "tool_call_id": tool_call.id,            "content": result        })    # 6. 第二次请求：将工具结果发回模型，生成最终答案    final_response = client.chat.completions.create(        model="gpt-oss:20b",  # 请替换为你在 Ollama 中实际使用的模型名称，例如：llama3.1, gemma, qwen2 等        messages=messages,    )    final_answer = final_response.choices[0].message.content    print("最终答案：", final_answer)else:    # 模型未调用工具，直接输出回复    print("直接回复：", response_message.content)
```

这个例子用的模型是 gtp-oss:20b，它也有 tool calls 的能力，这段代码演示了 tool calls 的用法，可以理解为 tool calls 就是大模型调函数。

目前 OpenClaw、Claud Code 等 agent 都有工具调用的能力，它们的原始能力就是 tool calls。

具体做法如下：

以 Claude Code 调用 grep 命令为例，首先大模型返回一个 `tool_use` 块，内容如下：

```
{  "name": "Bash",  "input": {    "command": "grep -r \"function\" --include=\"*.js\" ."  }}
```

后续步骤：

1. 宿主程序（Claude Code CLI）拦截这个 JSON，**并没有再次请求模型**，而是在真实的终端里执行 `grep`。

2. 宿主程序捕获命令的退出码（exit code）、`stdout`、`stderr`。

3. 宿主程序将结果封装成新的 `tool_result` 消息发回给模型。

4. 模型分析结果，决定是继续执行下一条命令，还是给出最终答案。

模型本身并不直接执行 `exec` 系统调用，它只是“建议”执行某条命令，由宿主程序作为代理去执行。

**命令行调用是 Tool Calls 的一种具体实现形式，Agent 对 Tool Calls 进行了进一步的封装，增加了状态管理、对话树等结构。**

****大模型是无状态的，**Agent 的本质是“状态管理器”。******

****Claude Code 等工具利用模型的原生 Tool Calls 能力输出指令，再由一个高性能的宿主程序（Rust/Go/TypeScript 编写）去执行这些指令，并通过精密的 Prompt Engineering 和历史管理，让模型产生“我在操作电脑”的连贯感知。****

****Tool Calls 是实现手段，而对话树、状态维护、流式执行是赋予其“Agent 智能”的工程架构。****

****理解了 **Tool Calls，基本上就理解了 OpenClaw、Claud Code 等 agent 的能力来源。******

****全文完。****

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

生有可恋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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