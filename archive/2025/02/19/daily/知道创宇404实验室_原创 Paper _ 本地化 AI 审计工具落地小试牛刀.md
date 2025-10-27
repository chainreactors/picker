---
title: 原创 Paper | 本地化 AI 审计工具落地小试牛刀
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990663&idx=1&sn=d3612bcdf320efdc783e5740d519c69d&chksm=8079aa75b70e2363a96c1c2318ebdea7a8fda22f5029416d80c2a7cc641c0ee2e3d263c0c79b&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2025-02-19
fetch_date: 2025-10-06T20:47:25.113372
---

# 原创 Paper | 本地化 AI 审计工具落地小试牛刀

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkfbjSFhZQICc4IRVM1I8N15jmXjhusdxQHibThhwXfthlrEEqbzjyQpaw/0?wx_fmt=jpeg)

# 原创 Paper | 本地化 AI 审计工具落地小试牛刀

原创

404实验室

知道创宇404实验室

**作******者：wh0am1i@********知道创宇404实验室****

**时间：**2025年2月18日****

****本文为知道创宇404实验室内部分享沙龙“404 Open Day”的议题内容，作为目前团队AI安全研究系列的一部分，分享出来与大家一同交流学习。****

**1.前言**

参考资料

2022年11月30日，OpenAI正式发布基于GPT-3.5架构的ChatGPT，这一里程碑事件引发了全球范围内的技术革命。在网络安全领域，人工智能代码审计迅速成为行业热点：一方面，安全研究人员通过深入探索逐步揭示了现有AI模型在代码审计场景中的技术边界与局限性；另一方面，开源社区持续涌现出多个创新性AI代码审计项目，展现出该技术路径的潜在应用价值。

**2.现存方案**

参考资料

**ChatGPTScan-SAST**

ChatGPTScan-SAST 是一个基于 ChatGPT 的开源代码审计平台。该项目通过精心设计的 prompt，使模型能够深度解析代码语义特征；通过多轮对话，引导AI执行漏洞模式匹配、风险影响评估等任务，最终输出漏洞分级报告。

#### **CodeArgus**

CodeArgus 采用多智能体协作方案，通过软件分析师、代码审计工程师和软件工程师这三个 Agent 的分工协作，由软件分析师解析软件的架构和程序流，再由软件工程师分析代码的具体作用，代码审计工程师再分析代码中存在的风险点。若是发现漏洞会由代码审计工程师给出修复方案，软件工程师进行修复，至此形成“检测-修复” 的闭环。

#### **vulnhuntr**

vulnhuntr 由 AI 提取项目的 README 内容并整合到 system prompt 中，首先通过 AI 的初筛识别出潜在的分析安点，接着针对不同的风险点生成专属的检测命令进行二次分析，在每次分析的过程中都会调用相关的代码片段作为依据。整个过程通过"初步筛查+定向验证"的双重检测机制，结合上下文关联分析，实现对代码漏洞的系统性排查。

**3.现存问题**

参考资料

#### 在安全研究员使用 AI 进行代码审计的过程中会发现大模型存在下面的问题：

#### **3.1 上下文窗口限制**

代码审计场景中，复杂调用链往往需要跨多个模块进行追踪分析。受限于当前大模型的上下文窗口长度（通常4k-32k tokens），在处理深度调用关系时会遭遇信息截断，导致多轮对话后期出现语义偏离、逻辑断层等问题，严重影响审计完整性。

#### **3.2 模型幻觉现象**

大语言模型固有的概率生成机制，可能导致其生成看似合理但实际错误的漏洞判定结论（如虚构不存在的函数参数、错误推断数据流向等）。这种现象使得审计结果必须经过严格的人工验证，显著增加了误报筛查工作量。

#### **3.3 云端服务成本压力**

对于需要高频调用、大规模代码库分析的应用场景，商业大模型的API调用成本（如GPT-4的3.750/1Minputtokens，3.750/1Minputtokens，15.000 / 1M output tokens）与安全研究员的预算限制形成矛盾。特别是在处理百万行级代码项目时，费用支出呈指数级增长。

#### **3.4 本地化部署困境**

当前开源模型存在参数规模与推理性能的矛盾：7B 以下小模型在代码理解能力上存在明显缺陷，而 70B 以上大模型又需要专业级 GPU 集群支持（如8xA100）。这种硬件资源门槛使得本地化部署方案难以实现理想的审计效果。

**4.本地方案**

参考资料

###

首先介绍本次实验所用到的环境：

* qwen2.5-coder:14b
* llama\_index

根据上面的问题我们制定了一下 AI + 工具的代码审计方案，即：通过将研究员的模糊输入转换成计算机可以理解的命令输出，最后将审计工具的结果返回给 AI 模型让其分析和解读，最后输出结果。

在此之前我们需要了解计算机和 AI 大模型在运算时的区别，首先是计算机在获取到输入后根据内部的逻辑运算再输出结果，计算机的处理过程可以抽象为图1所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkfVw04L8RzjrFs4Gh8BzGdbFA3yygXUmS3WKib1vtsA1IdyS0FiawtRkvw/640?wx_fmt=png&from=appmsg)

图1.计算机处理输入

而 AI 大模型在处理输入时通过的预测机制来输出结果，整体流程如图 2 所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkfLhxSEMybjzr8KnJj7J6nUhPLFeM8yTX6nG2w6GfHTbEDQk4Ne2wt9A/640?wx_fmt=png&from=appmsg)

图2.AI 大模型处理输入

如果我们需要通过 AI 来调用工具，需要解决下面的两个问题：

* 怎么让 AI 稳定的输出计算机能够识别的命令
* 如何让 AI 与外界交互

首先让我们来解决第一个问题，AI 的知识储备丰富，但是每次对话的输出结果不一定相同，因此我们在编写提示的词时候就应该明确说明，我们需要什么样的输出格式，给出模板，AI 基本上会按照模板进行输出。为此我总结了一个模板如图3所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkf6Ticzrh0Ka64BLm6ib8XaqHgUtTL3ZIvibuEUZXibpMVaTxpQYgrOSaW1A/640?wx_fmt=png&from=appmsg)

图3 提示词模板

最后来解决 AI 模型与外界交互的问题，在 AI 模型提供了 tools ，tools指的是模型可以调用的外部功能或服务，用于扩展模型的能力，使其能够执行超出纯文本生成范围的任务。这些工具允许模型与外部世界交互，获取信息，或执行特定的操作。下面是一个简单的实例：

```
import asyncio
import subprocess
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import ToolSelection, ToolOutput
from llama_index.core.workflow import Event
from typing import Any, List

from llama_index.core.tools import FunctionTool
from llama_index.core.llms.function_calling import FunctionCallingLLM
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import Settings
from llama_index.core.tools.types import BaseTool
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step
from llama_index.llms.ollama import Ollama

class InputEvent(Event):
    input: list[ChatMessage]

class ToolCallEvent(Event):
    tool_calls: list[ToolSelection]

class FunctionOutputEvent(Event):
    output: ToolOutput

class FuncationCallingAgent(Workflow):
    def __init__(
        self,
        *args: Any,
        llm: FunctionCallingLLM | None = None,
        tools: List[BaseTool] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.tools = tools or []

        self.llm = llm or Ollama()
        assert self.llm.metadata.is_function_calling_model

        self.memory = ChatMemoryBuffer.from_defaults(llm=llm)
        self.sources = []

    @step
    async def prepare_chat_history(self, ev: StartEvent) -> InputEvent:
        # clear sources
        self.sources = []

        # get user input
        user_input = ev.input
        user_msg = ChatMessage(role="user", content=user_input)
        self.memory.put(user_msg)

        # get chat history
        chat_history = self.memory.get()
        return InputEvent(input=chat_history)

    @step
    async def handle_llm_input(
        self, ev: InputEvent
    ) -> ToolCallEvent | StopEvent:
        chat_history = ev.input

        response = await self.llm.achat_with_tools(
            self.tools, chat_history=chat_history
        )
        self.memory.put(response.message)

        tool_calls = self.llm.get_tool_calls_from_response(
            response, error_on_no_tool_call=False
        )

        if not tool_calls:
            return StopEvent(
                result={"response": response, "sources": [*self.sources]}
            )
        else:
            return ToolCallEvent(tool_calls=tool_calls)

    @step
    async def handle_tool_calls(self, ev: ToolCallEvent) -> InputEvent:
        tool_calls = ev.tool_calls
        tools_by_name = {tool.metadata.get_name(): tool for tool in self.tools}

        tool_msgs = []

        # call tools -- safely!
        for tool_call in tool_calls:
            tool = tools_by_name.get(tool_call.tool_name)
            additional_kwargs = {
                "tool_call_id": tool_call.tool_id,
                "name": tool.metadata.get_name(),
            }
            if not tool:
                tool_msgs.append(
                    ChatMessage(
                        role="tool",
                        content=f"Tool {tool_call.tool_name} does not exist",
                        additional_kwargs=additional_kwargs,
                    )
                )
                continue

            try:
                tool_output = tool(**tool_call.tool_kwargs)
                self.sources.append(tool_output)
                tool_msgs.append(
                    ChatMessage(
                        role="tool",
                        content=tool_output.content,
                        additional_kwargs=additional_kwargs,
                    )
                )
            except Exception as e:
                tool_msgs.append(
                    ChatMessage(
                        role="tool",
                        content=f"Encountered error in tool call: {e}",
                        additional_kwargs=additional_kwargs,
                    )
                )

        for msg in tool_msgs:
            self.memory.put(msg)

        chat_history = self.memory.get()
        return InputEvent(input=chat_history)

def run_code(cmd: str):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    return ret.stdout.split()

# 初始化 Ollama（默认使用 localhost:11434）
llm = Ollama(
    model='qwen2.5-coder:14b',
    temperature=0,
    request_timeout=120,
    base_url='http://localhost:11434',
    verbose=False
)

Settings.llm = llm

tools = [
    FunctionTool.from_defaults(run_code),
]

agent = FuncationCallingAgent(
    llm=llm,
    tools=tools,
)

async def main():
    user_input = input("\nuser input: ")

    ret = await agent.run(input=user_input)
    print("\n回答:", ret['response'].message.content)

if __name__ == '__main__':
    asyncio.run(main())
```

代码1 tools 实例

运行效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkfKWR6qeT3STZ7hmmdI57rPnBzORzvtgVF9TbZ6ezG08eibb2kC2nYAhw/640?wx_fmt=png&from=appmsg)

图4 tools 运行结果

而实际文件也确实如此：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkfIWHibjYOnqJIMtLJTn7PsHC3SDBWficl4pnzVjukYkgjdib1113ohkrnw/640?wx_fmt=png&from=appmsg)

至此利用 AI 模型进行代码审计的过程存在的两个问题都已经得到解决。那么整理一下整体的思路：首先在用户与AI 模型进行对话时，会根据用户的输入判断是否需要去调用 tools，用于执行计算机命令。当不要执行计算机命令时，就是正常的文本对话；而但需要...