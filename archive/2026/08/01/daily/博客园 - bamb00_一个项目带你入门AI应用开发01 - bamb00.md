---
title: 一个项目带你入门AI应用开发01 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22137356
source: 博客园 - bamb00
date: 2026-08-01
fetch_date: 2026-08-02T05:10:37.779669
---

# 一个项目带你入门AI应用开发01 - bamb00

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [人怜直节生来瘦，自许高材老更刚。](https://www.cnblogs.com/goodhacker)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/goodhacker/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/bamb00)
* 订阅
* [管理](https://i.cnblogs.com/)

# [一个项目带你入门AI应用开发01](https://www.cnblogs.com/goodhacker/p/22137356 "发布于 2026-08-01 19:36")

# 第 1 课：从零开始，让 AI 和你对话

## 1.1 你的目标

写一个 Python 程序，在终端里输入文字，AI 会回答你。

```
You: 你好
AI: 你好！有什么可以帮你的？

You: 查一下订单
AI: 抱歉，我目前无法查询订单信息...
```

## 1.2 最直接的方式：一行代码调 API

所有大模型（DeepSeek、GPT、通义千问）都提供 HTTP API。最简单的调用方式：

```
import requests

resp = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk-你的key",
        "Content-Type": "application/json",
    },
    json={
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "你好"}
        ],
    },
)
print(resp.json()["choices"][0]["message"]["content"])
```

把这段代码保存为 `test.py`，把 `sk-你的key` 替换成你从 DeepSeek 官网申请的 API Key，然后运行：

```
python test.py
```

如果看到 AI 回复了，说明一切正常。

### 为什么要从这里开始？

不是要你记住这个 JSON 结构，而是要理解一个事实：**所有 AI Agent 的底层就是一次 HTTP 请求**。不管多复杂的系统，最终都是这个东西。

## 1.3 第一个问题：API Key 暴露了

上面那段代码里，API Key 是直接写在字符串里的。如果你把这个文件传到 GitHub，任何人都能看到并使用你的 Key。

### 为什么不能把 Key 写死在代码里？

* 你可能会把代码传到 GitHub（不管有意还是无意）
* 不同环境（开发/测试/生产）要用不同的 Key，写死意味着改代码
* 换 Key 要重新部署

### 正确的做法：环境变量 + .env 文件

```
import os
from dotenv import load_dotenv

# 读取 .env 文件（如果有的话）
load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1")
MODEL = os.getenv("LLM_MODEL", "deepseek-chat")
```

把 Key 写在 `.env` 文件里：

```
LLM_API_KEY=sk-你的key
LLM_BASE_URL=https://api.deepseek.com/v1
LLM_MODEL=deepseek-chat
```

然后把 `.env` 加到 `.gitignore`：

```
.env
```

这样就安全了。`load_dotenv()` 会自动读取 `.env` 文件的内容。

### 更进一步：用 pydantic-settings 管理

手动 `os.getenv` 每个变量，写起来很啰嗦。`pydantic-settings` 可以自动从环境变量和 `.env` 文件读取配置：

```
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com/v1"
    llm_model: str = "deepseek-chat"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

settings = Settings()
```

然后代码里用 `settings.llm_api_key` 就行。所有配置集中管理，一目了然。

## 1.4 第二个问题：重复代码

每次调 API 都要写：

1. 拼 URL
2. 拼 headers
3. 拼 body
4. 发请求
5. 解析 response

如果代码里每个调 API 的地方都这么写一遍，有 10 处就要写 10 遍。想改点什么（比如加个 timeout）就要改 10 个地方。

### 为什么重复代码是问题？

想象一下，某天你要给所有 API 调用加一个 timeout=30 的参数。如果代码写在一个函数里，改 1 处就够了。如果散落在 10 个地方，你很可能漏掉某个地方——然后某个功能在特定场景下静默失败。

### 正确的做法：封装成函数

```
def call_llm(messages, temperature=0.7):
    """一次封装，到处调用"""
    resp = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": messages,
            "temperature": temperature,
        },
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
```

现在每次调用只需要一行：

```
reply = call_llm([{"role": "user", "content": "你好"}])
print(reply)
```

### 封装的边界在哪里？

`call_llm` 函数的接口设计值得你思考：

* **参数**：只暴露调用方需要关心的东西（`messages` 和 `temperature`），其他内部细节隐藏了
* **返回值**：只返回 AI 回复的内容，JSON 解析的细节在里面处理了
* **异常**：`resp.raise_for_status()` 让调用方可以通过 try/except 统一处理错误

这不是"为了封装而封装"，而是**让调用方不需要知道 API 的细节**。第 4 课我们会在不改变调用方式的情况下，给 `call_llm` 加上 tools 参数支持——调用方代码几乎不需要改。

## 1.5 第三个问题：只能问一次

现在的程序跑完就退出了。一次对话就要重新启动一次程序。

### 正确的做法：对话循环

```
def main():
    print("AI 客服终端（输入 /quit 退出）")

    messages = [
        {"role": "system", "content": "你是一个友好的电商客服助手。"}
    ]

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input == "/quit":
            break

        messages.append({"role": "user", "content": user_input})
        reply = call_llm(messages)
        print(f"AI: {reply}")
        messages.append({"role": "assistant", "content": reply})
```

注意 `messages` 数组的变化：

```
开始时: [system]
第1轮: [system, user_1] → AI 回复 → [system, user_1, assistant_1]
第2轮: [system, user_1, assistant_1, user_2] → AI 回复 → ...
```

每次对话都把历史传回去，这样 AI 才能"记住"前面说了什么。**这是"多轮对话"的本质。**

## 1.6 完整代码

```
# 01-basic-chat/chat.py

import requests
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com/v1"
    llm_model: str = "deepseek-chat"
    model_config = {"env_file": "../.env", "env_file_encoding": "utf-8"}

settings = Settings()

def call_llm(messages, temperature=0.7):
    """通用 LLM 调用函数"""
    url = f"{settings.llm_base_url.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": settings.llm_model,
        "messages": messages,
        "temperature": temperature,
    }
    resp = requests.post(url, headers=headers, json=body, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def main():
    messages = [{"role": "system", "content": "你是一个友好的电商客服助手。"}]
    print("AI 客服终端（输入 /quit 退出）")

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input == "/quit":
            break

        messages.append({"role": "user", "content": user_input})
        try:
            reply = call_llm(messages)
            print(f"AI: {reply}")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"出错了：{e}")

if __name__ == "__main__":
    main()
```

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| API 调用 | HTTP POST → `/v1/chat/completions` | 所有大模型都兼容这个接口，学一次通吃所有 |
| 配置管理 | pydantic-settings + .env | Key 不写进代码，不同环境用不同配置 |
| 函数封装 | 抽出 `call_llm` | 一处修改，全局生效；调用方不关心内部细节 |
| 消息结构 | messages: [system, user, assistant] | LLM 本身无状态，上下文全靠 messages 数组传递 |
| 参数设计 | 暴露调用方关心的，隐藏内部细节 | 接口稳定，后续扩展（如 tools）不影响已有调用方 |

## 课后作业

1. 把 `temperature` 改成 0.1 和 1.0 分别试试，观察回复差异
2. 加一个 `/new` 命令，清除对话历史重新开始
3. 去掉 `messages` 中的 system 消息，看看 AI 的行为有什么变化

## 面试可能会问

> "LLM API 调用的 messages 里 system、user、assistant 三种 role 的区别是什么？"

posted @
2026-08-01 19:36
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(59)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22137356&targetId=22137356&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260609221536870-1777800795.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=...