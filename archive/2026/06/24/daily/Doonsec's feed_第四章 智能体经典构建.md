---
title: 第四章 智能体经典构建
url: https://mp.weixin.qq.com/s/jvOgUbQxLVj4urbRPhfyYg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:01:42.080516
---

# 第四章 智能体经典构建

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaiaehJqQJocuwkiapyTcvcMC2nvxXP7exJdjdKgqn2JNYdSN1X3icibuWNFFUHXYcibg3TnIgQA0wDfwOagTZcYHNYVdVV5OcB0MzNMcdiarls3aA/0?wx_fmt=jpeg)

# 第四章 智能体经典构建

Yang
Yang

AI+网络安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在上一章节里，我们剖析了大语言模型作为现代智能体核心“大脑”的运作机制，深入学习了其Transformer架构原理、交互方式及其固有的能力局限。现在，是时候跨越理论的桥梁，将这些认知付诸实践，亲手打造属于我们的智能体。

## 现代智能体的核心竞争力，在于其能够将大模型内在的推理能力与外部环境有效连通。它具备了自主解析用户意图、拆解复杂任务结构的能力，并能通过调用代码解释器、搜索引擎及各类API接口等“工具箱”，来实现信息的获取与操作的执行，从而达成最终目标。当然，智能体并非无所不能，它同样受限于大模型本身的“幻觉”缺陷，在处理复杂逻辑时可能陷入死循环，或出现工具调用的误操作，这些构成了其实际应用的边界。

## 为了更科学地组织智能体的“思维”与“行动”流程，业界发展出了多种经典的架构模式。本章将聚焦于其中最具代表性的三种架构，并带领读者从零开始逐一实现：

* ## ReAct (Reasoning and Acting)： 一种强调“知行合一”的范式，促使智能体在思考中行动，在行动中动态调整策略。

* ## **Plan-and-Solve**： 一种推崇“谋定后动”的范式，要求智能体先构建完整的行动蓝图，随后按部就班地执行。

* ## **Reflection**： 一种赋予智能体“自省能力”的范式，通过内部的自我批判与修正机制来迭代优化结果。

## 了解了上述背景，或许你会疑惑：既然市面上已有LangChain、LlamaIndex等成熟的开发框架，为何还要费力去“重复造轮子”？原因在于，虽然成熟的封装极大地提升了工程效率，但过度依赖高度抽象的工具，往往会让我们对底层的设计逻辑与运行机制一知半解。其次，亲手构建的过程会让我们直面各类工程挑战。框架在底层默默处理了诸多细节，诸如模型输出格式的解析容错、工具调用失败后的重试机制、以及如何防止智能体陷入死循环等。亲自解决这些问题，是磨炼系统设计思维最直接的途径。最后，也是最关键的一点，只有洞悉了设计原理，你才能完成从框架“使用者”到应用“创造者”的身份蜕变。当标准组件无法满足你的定制化需求时，你将具备深度定制乃至从零构建全新智能体的底气。

### 4.1 环境准备与基础工具定义

在正式开工之前，我们需要先搭建好开发环境，并定义一组基础组件。这将确保我们在后续实现不同架构时，能够复用代码，从而集中精力攻克核心逻辑。

#### 4.1.1 安装依赖库

本书的实战环节主要基于 Python 语言，推荐使用 Python 3.10 及以上版本。首先，请确保安装了 `openai` 库以便与大语言模型进行交互，同时安装 `python-dotenv` 库来安全管理 API 密钥。 在终端中执行以下指令：

```
pip install openai python-dotenv
```

#### 4.1.2 配置 API 密钥

为了保证代码的通用性，我们将模型服务相关的配置（模型ID、密钥、服务地址）统一放置在环境变量中管理。 在项目的根目录下，新建一个名为 `.env` 的配置文件。 在文件中填入以下内容。你可以根据实际情况，将其配置为 OpenAI 官方服务，或任何兼容 OpenAI 接口的第三方/本地服务。 若不清楚如何获取，可参考“环境配置”章节。

```
# .env file
LLM_API_KEY="YOUR-API-KEY"
LLM_MODEL_ID="YOUR-MODEL"
LLM_BASE_URL="YOUR-URL"
```

后续代码将自动从该文件读取这些配置信息。

#### 4.1.3 封装基础 LLM 调用函数

为了提升代码的整洁度与复用性，我们来定义一个专属的LLM客户端类。该类将封装所有与模型服务交互的底层细节，使主逻辑能更专注于智能体的构建。

```
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict
# 加载 .env 文件中的环境变量
load_dotenv()
classHelloAgentsLLM:
    """
    为本书 "Hello Agents" 定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并默认使用流式响应。
    """
    def__init__(self, model: str = None, apiKey: str = None, baseUrl: str = None, timeout: int = None):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey = apiKey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_TIMEOUT", 60))

        ifnot all([self.model, apiKey, baseUrl]):
            raise ValueError("模型ID、API密钥和服务地址必须被提供或在.env文件中定义。")
        self.client = OpenAI(api_key=apiKey, base_url=baseUrl, timeout=timeout)
    defthink(self, messages: List[Dict[str, str]], temperature: float = 0) -> str:
        """
        调用大语言模型进行思考，并返回其响应。
        """
        print(f"正在调用 {self.model} 模型...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )

            # 处理流式响应
            print("大语言模型响应成功:")
            collected_content = []
            for chunk in response:
                ifnot chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()   # 在流式输出结束后换行
            return"".join(collected_content)
        except Exception as e:
            print(f"调用LLM API时发生错误: {e}")
            returnNone
# --- 客户端使用示例 ---
if __name__ == '__main__':
    try:
        llmClient = HelloAgentsLLM()

        exampleMessages = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code."},
            {"role": "user", "content": "写一个快速排序算法"}
        ]

        print("--- 调用LLM ---")
        responseText = llmClient.think(exampleMessages)
        if responseText:
            print("\n\n--- 完整模型响应 ---")
            print(responseText)
    except ValueError as e:
        print(e)
```

```
>>>
--- 调用LLM ---
正在调用 xxxxxx 模型...
大语言模型响应成功:
快速排序是一种非常高效的排序算法...
```

### 4.2 ReAct

在准备好LLM客户端后，我们将着手构建第一个，也是最经典的一种智能体范式——**ReAct (Reason + Act)**。ReAct范式由Shunyu Yao于2022年提出[1]，其核心理念在于模仿人类解决问题的路径，将**推理**与**行动**显式地串联结合，构建起一个“思考-行动-观察”的闭环。

#### 4.2.1 ReAct 的工作流程

在ReAct问世之前，主流方法主要分为两派：一派是“纯思考”型，例如**思维链**，它能引导模型进行深层逻辑推演，但无法触达外部世界，容易产生事实性幻觉；另一派是“纯行动”型，模型直接输出动作指令，却缺乏规划与纠错机制。 ReAct的高明之处在于，它认识到**思考与行动是相辅相成的**。思考为行动指明方向，行动的结果反过来又修正思考。为此，ReAct范式通过特定的提示工程引导模型，使其每一步输出都遵循固定轨迹：

Thought (思考)： 这是智能体的“内心独白”。它负责分析现状、拆解任务、规划下一步，或反思上一步的结果。

Action (行动)： 这是智能体决定采取的具体手段，通常指向一个外部工具调用，例如 `Search['华为最新款手机']`。

**Observation (观察)**： 这是执行 `Action` 后从外部工具返回的反馈，例如搜索摘要或API响应。****

****智能体将不断循环 `Thought -> Action -> Observation` 过程，将新的观察追加到历史记录中，形成不断增长的上下文，直到它在 `Thought` 中判定任务完成，进而输出结果。这一过程形成了强大的协同效应：**推理赋予了行动目的性，而行动为推理提供了事实支撑。**我们可以将这一过程形式化表达，如图4.1所示。具体而言，在每个时间步 ，智能体的策略（即大语言模型 ）会依据初始问题  和历史轨迹 ，生成当前的思考  和行动 ：

随后，环境中的工具  执行行动 ，并返回新的观察 ：

这一循环持续进行，将新的  对追加到历史中，直到模型在思考  中判断任务终结。

**![ReAct范式中的“思考-行动-观察”协同循环](https://mmbiz.qpic.cn/sz_mmbiz_png/iaiaehJqQJocv4QDnYgPNYKBbWN9BuicHnCTJEppVC3InVFzwfAKUgGdRAxFFV0P4icWqrXl1hia8anibl3ngeqdglp9AlJianu1oSfFpDRpicWZwwY/640?wx_fmt=png&from=appmsg)**

**图 4.1 ReAct 范式中的“思考-行动-观察”协同循环**

这种机制在以下场景中表现尤为出色：

* **需要外部知识的任务**：如查询实时资讯（天气、新闻、股价）、检索专业领域知识等。
* **需要精确计算的任务**：将数学运算交给计算器工具，规避LLM的计算错误风险。
* **需要与API交互的任务**：如操作数据库、调用特定服务接口完成功能。 因此，我们将构建一个具备**外部工具调用**能力的ReAct智能体，来回答一个仅凭大模型知识库无法直接解答的问题：“华为最新的手机是哪一款？它的主要卖点是什么？”这要求智能体意识到需要联网搜索，调用工具获取结果并进行总结。

#### 4.2.2 工具的定义与实现

若将大语言模型比作智能体的大脑，那么**工具**便是其与外界交互的“四肢”。为了让ReAct范式真正发挥作用，我们需要赋予智能体调用外部工具的能力。 针对本节目标，我们需要为智能体配备一个网页搜索工具。这里我们选用 `SerpApi`，它通过API提供结构化的Google搜索结果，能直接返回“答案摘要框”或知识图谱信息。 首先，安装该库：

```
pip install google-search-results
```

同时，你需要前往 SerpApi官网 注册免费账户获取API密钥，并将其添加到项目根目录的 `.env` 文件中：

```
# .env file
# ... (保留之前的LLM配置)
SERPAPI_API_KEY="YOUR_SERPAPI_API_KEY"
```

接下来，我们通过代码定义并管理这个工具。我们将分步实施：先实现核心功能，再构建通用管理器。

**（1）实现搜索工具的核心逻辑**一个定义良好的工具应包含三个核心要素：

* **名称**：简洁唯一的标识符，供智能体在 `Action` 中调用，如 `Search`。
* **描述**：清晰的自然语言功能说明。这是关键，模型依赖此描述判断何时调用。
* **执行逻辑**：真正执行任务的函数或方法。 我们的首个工具是 `search` 函数，负责接收查询词并返回结果。

```
from serpapi import SerpApiClient
defsearch(query: str) -> str:
    """
    一个基于SerpApi的实战网页搜索引擎工具。
    它会智能地解析搜索结果，优先返回直接答案或知识图谱信息。
    """
    print(f"正在执行 [SerpApi] 网页搜索: {query}")
    try:
        api_key = os.getenv("SERPAPI_API_KEY")
        ifnot api_key:
            return"错误:SERPAPI_API_KEY 未在 .env 文件中配置。"
        params = {
            "engine": "google",
            "q": query,
            "api_key": api_key,
            "gl": "cn",   # 国家代码
            "hl": "zh-cn", # 语言代码
        }

        client = SerpApiClient(params)
        results = client.get_dict()

        # 智能解析:优先寻找最直接的答案
        if"answer_box_list"in results:
            return"\n".join(results["answer_box_list"])
        if"answer_box"in results and"answer"in results["answer_box"]:
            return results["answer_box"]["answer"]
        if"knowledge_graph"in results and"description"in results["knowledge_graph"]:
            return results["knowledge_graph"]["description"]
        if"organic_results"in results and results["organic_results"]:
            # 如果没有直接答案，则返回前三个有机结果的摘要
            snippets = [
                f"[{i+1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(results["organic_results"][:3])
            ]
            return"\n\n".join(snippets)

        returnf"对不起，没有找到关于 '{query}' 的信息。"
    except Exception as e:
        returnf"搜索时发生错误: {e}"
```

上述代码会优先检查 `answer_box` 或 `knowledge_graph` 等高价值信息，若存在则直接返回；否则退而求其次，返回前三个常规搜索结果的摘要。这种“智能解析”能为LLM提供更高质量的输入。

**（2）构建通用的工具执行器**当智能体需驾驭多种工具时（如搜索、计算、查库），我们需要一个统一的管理器来注册和调度。为此，创建 `ToolExecutor` 类。

```
from typing import Dict, Any
classToolExecutor:
    """
    一个工具执行器，负责管理和执行工具。
    """
    def__init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
 ...