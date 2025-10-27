---
title: LangChain初探 - 郑瀚Andrew
url: https://buaq.net/go-171393.html
source: unSafe.sh - 不安全
date: 2023-07-07
fetch_date: 2025-10-04T11:52:36.164349
---

# LangChain初探 - 郑瀚Andrew

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b43f2c3e75cad9ebb3e806377de513ba.jpg)

LangChain初探 - 郑瀚Andrew

LangChain是一个使用LLMs构建应用程序的工具箱，包含Models（LLM 调用）支持多种模型接口，比如 OpenAI、Hugging Face、AzureOpenAI ...F
*2023-7-6 18:6:0
Author: [www.cnblogs.com(查看原文)](/jump-171393.htm)
阅读量:35
收藏*

---

LangChain是一个使用LLMs构建应用程序的工具箱，包含

* **Models（LLM 调用）**
  + 支持多种模型接口，比如 OpenAI、Hugging Face、AzureOpenAI ...
  + Fake LLM，用于测试
  + 缓存的支持，比如 in-mem（内存）、SQLite、Redis、SQL
  + 用量记录
  + 支持流模式（就是一个字一个字的返回，类似打字效果）
* **Prompts（Prompt管理）**：支持各种自定义模板
* **Indexes（对索引的支持）**
  + 文档分割器
  + 向量化
  + 对接向量存储与搜索，比如 Chroma、Pinecone、Qdrand
* **Memory**
* **Chains**
  + LLMChain
  + 各种工具Chain
  + LangChainHub
* **Agents**：使用 LLMs 来确定采取哪些行动以及以何种顺序采取行动。操作可以是使用工具并观察其输出，也可以是返回给用户。如果使用得当，代理可以非常强大。
* **Callbacks**
* 等核心模块

本质上讲，LangChain 是一个用于开发由语言模型驱动的应用程序的框架。他主要拥有 2 个能力：

1. 可以将 LLM 模型与外部数据源进行连接
2. 允许与 LLM 模型进行交互

参考链接：

```
https://zhuanlan.zhihu.com/p/628433395
https://serpapi.com/dashboard
https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide
```

因为数据相关性搜索其实是向量运算。所以，不管我们是使用 openai api embedding 功能还是直接通过向量数据库直接查询，都需要将我们的加载进来的数据 `Document` 进行向量化，才能进行向量运算搜索。转换成向量也很简单，只需要我们把数据存储到对应的向量数据库中即可完成向量的转换。

官方也提供了很多的向量数据库供我们使用。

我们可以把 Chain 理解为任务。一个 Chain 就是一个任务，当然也可以像链条一样，一个一个的执行多个链。

```
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# location 链
llm = OpenAI(temperature=1)
template = """Your job is to come up with a classic dish from the area that the users suggests.
% USER LOCATION
{user_location}

YOUR RESPONSE:
"""
prompt_template = PromptTemplate(input_variables=["user_location"], template=template)
location_chain = LLMChain(llm=llm, prompt=prompt_template)

# meal 链
template = """Given a meal, give a short and simple recipe on how to make that dish at home.
% MEAL
{user_meal}

YOUR RESPONSE:
"""
prompt_template = PromptTemplate(input_variables=["user_meal"], template=template)
meal_chain = LLMChain(llm=llm, prompt=prompt_template)

# 通过 SimpleSequentialChain 串联起来，第一个答案会被替换第二个中的user_meal，然后再进行询问
overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain], verbose=True)
review = overall_chain.run("Rome")
```

用于衡量文本的相关性。这个也是 OpenAI API 能实现构建自己知识库的关键所在。

他相比 fine-tuning 最大的优势就是，不用进行训练，并且可以实时添加新的内容，而不用加一次新的内容就训练一次，并且各方面成本要比 fine-tuning 低很多。

## 0x1：Agents技术基本概念

Agent作为Langchain框架中驱动决策制定的实体。它可以访问一组工具，并可以根据用户的输入决定调用哪个工具。正确地使用agent，可以让它变得非常强大。

Agents 有以下几个核心概念：

* **Tool**：执行特定的功能。可以是谷歌搜索，数据库查找，Python REPL，其他暴露API借口的任意工具。工具的接口目前是一个函数，期望以字符串作为输入，以字符串作为输出。
* **LLM**：驱动 Agents 的语言模型。
* **Agent**：要使用的代理，这应该是一个引用支持代理类的字符串，本质就是一系列prompt program。

简单来说，用户向LangChain输入任意的内容，同时将一套工具集合（也可以自定义工具）托管给LLM，让LLM自己决定使用工具中的某一个（如果存在的话）。

**input answer query -> thought for actions -> action call -> observation result -> judge if anymore **thought -> loop until finnish answers****

****![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230706224328883-1116047462.png)****

从开发者的角度来看，Agents技术带来了两个主要的好处：

* （1）**为工具类软件提供全新的智能交互体验**：对于许多工具类软件而言，新手引导是不可或缺的。然而，实际情况是新手引导并未能有效降低用户使用工具的门槛。若能基于Agent构建一个自然语言控制的工具软件，用户将会非常容易上手，真正实现“人人都能上手”的目标。
* （2）**搭建智能化工作流，实现真正的面向NLP的数据驱动智能编程**：尽管AutoGPT近期非常火，但我认为更有效的方法是构建一套智能化的工作流。即通过人工预先定义一套流程，然后借助不同的Agent去执行，最终达成特定目标。与AutoGPT相比，这种智能化工作流方法更具可控性和可靠性。

## 0x2：一个简单的Agents例子

下面用一个简单的例子说明使用过程，

首先，这里自定义了两个简单的工具

```
from langchain.tools import BaseTool

# 天气查询工具 ，无论查询什么都返回Sunny
class WeatherTool(BaseTool):
    name = "Weather"
    description = "useful for When you want to know about the weather"

    def _run(self, query: str) -> str:
        return "Sunny^_^"

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")

# 计算工具，暂且写死返回3
class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "useful for when you need to answer questions about math."

    def _run(self, query: str) -> str:
        return "3"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("BingSearchRun does not support async")
```

接下来是针对于工具的简单调用。

```
# -*- coding: utf-8 -*-
from langchain.tools import BaseTool
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# 天气查询工具 ，无论查询什么都返回Sunny
class WeatherTool(BaseTool):
    name = "Weather"
    description = "useful for When you want to know about the weather"

    def _run(self, query: str) -> str:
        return "Sunny^_^"

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")

# 计算工具，暂且写死返回3
class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "useful for when you need to answer questions about math."

    def _run(self, query: str) -> str:
        return "3"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("BingSearchRun does not support async")

if __name__ == '__main__':
    llm = OpenAI(
        temperature=0,
        openai_api_key="sk-xxxx"
    )
    tools = [WeatherTool(), CustomCalculatorTool()]
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    agent.run("Query the weather of this week, And How old will I be in ten years? This year I am 28")
```

完整的响应过程：

## 0x3：基本工作原理

我们来看一下上述例子的工作原理。

首先看输入的问题

```
Query the weather of this week, And How old will I be in ten years? This year I am 28
```

查询本周天气，以及十年后我多少岁，今年我28。

主要是调用**AgentExecutor**的**\_call**方法，代码如下：

```
def _call(self, inputs: Dict[str, str]) -> Dict[str, Any]:
    """Run text through and get agent response."""
    # Construct a mapping of tool name to tool for easy lookup
    name_to_tool_map = {tool.name: tool for tool in self.tools}
    # We construct a mapping from each tool to a color, used for logging.
    color_mapping = get_color_mapping(
        [tool.name for tool in self.tools], excluded_colors=["green"]
    )
    intermediate_steps: List[Tuple[AgentAction, str]] = []
    # Let's start tracking the number of iterations and time elapsed
    iterations = 0
    time_elapsed = 0.0
    start_time = time.time()
    # We now enter the agent loop (until it returns something).
    while self._should_continue(iterations, time_elapsed):
        next_step_output = self._take_next_step(
            name_to_tool_map, color_mapping, inputs, intermediate_steps
        )
        if isinstance(next_step_output, AgentFinish):
            return self._return(next_step_output, intermediate_steps)

        intermediate_steps.extend(next_step_output)
        if len(next_step_output) == 1:
            next_step_action = next_step_output[0]
            # See if tool should return directly
            tool_return = self._get_tool_return(next_step_action)
            if tool_return is not None:
                return self._return(tool_return, intermediate_steps)
        iterations += 1
        time_elapsed = time.time() - start_time
    output = self.agent.return_stopped_response(
        self.early_stopping_method, intermediate_steps, **inputs
    )
    return self._return(output, intermediate_steps)
```

主要是while循环体中的逻辑，主体逻辑如下：

* 调用\_take\_next\_step方法
* 判断返回的结果是否可以结束
* 如果可结束就直接返回结果，否则继续步骤1-2

**\_take\_next\_step方法**

在”**thought-action-observation循环“**中采取单一步骤。重写此方法以控制Agent如何做出选择和行动。

```
def _take_next_step(
        self,
        name_to_tool_map: Dict[str, BaseTool],
        color_mapping: Dict[str, str],
        inputs: Dict[str, str],
        intermediate_steps: List[Tuple[AgentAction, str]],
    ) -> Union[AgentFinish, List[Tuple[Agent...