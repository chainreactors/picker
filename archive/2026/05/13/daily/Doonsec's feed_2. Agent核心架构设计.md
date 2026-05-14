---
title: 2. Agent核心架构设计
url: https://mp.weixin.qq.com/s/v-anYMB_l2vk-P7ChRj2mw
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:41.780669
---

# 2. Agent核心架构设计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4aKVM2Z06hMenvlC5NUKlphwXBqeacIJqibqxRJLFUp2ksjZXlibTlj8RsuEntjLppzHgnQBFh9rIOKrOCpQvbg6GJYmuemGgicfc/0?wx_fmt=jpeg)

# 2. Agent核心架构设计

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

完整docx文件关注公众号回复：从零构建AI驱动的二进制安全系统

在第1章中，你搭建好了开发环境并运行了第一个Hello Agent程序，对Agent的基本概念和工作原理有了初步认识。本章将带领你深入Agent的核心架构——你会系统学习三种主流的Agent架构模式，亲手设计并实现一个可扩展的Agent框架核心模块，最终完成一个完整的ReAct循环Agent。这些知识将为你后续构建二进制分析Agent打下坚实的架构基础。

---

## 2.1 Agent架构模式

Agent（智能体）并非一个单一固定的程序结构，而是有多种架构模式来组织其推理和执行流程。选择合适的架构模式取决于任务复杂度、工具数量和可靠性要求等因素。本节将详细介绍三种最核心的架构模式：ReAct、Plan-and-Execute和Multi-Agent协作，并通过对比分析帮助你理解各模式的适用场景。

### 2.1.1 ReAct模式：思考-行动-观察循环

**ReAct**（Reasoning + Acting，推理+行动）是当前最广泛使用的Agent推理模式1^。它的核心思想源于人类解决问题的认知过程：人们在面对复杂问题时，往往交替进行思考和行动——先思考下一步该做什么，然后执行相应的操作，观察结果后再决定下一步的思考方向。ReAct模式正是将这种人机认知机制编码到LLM驱动的Agent中。

#### ReAct循环的三步机制

ReAct Agent的执行流程是一个紧密耦合的循环，每一步都包含三个核心环节：

**Thought（思考）**：Agent接收用户输入和之前的观察结果后，LLM首先进行推理，生成一段内部独白式的思考文本。这段思考描述了Agent对当前任务状态的理解、已掌握的信息、以及下一步应该采取的策略。例如，当用户要求"分析这个二进制文件是否存在缓冲区溢出漏洞"时，Agent的思考可能是："我需要先获取文件的基本信息，确认文件类型和架构，然后反汇编查找危险函数调用，最后让LLM分析潜在漏洞。"

**Action（行动）**：基于思考的结果，Agent选择一个可用的工具（Tool）并准备调用参数。这一步本质上是将抽象的推理转化为具体的函数调用。Agent必须从注册的工具列表中选择最匹配当前需求的那个，并构造符合工具参数Schema的输入数据。

**Observation（观察）**：工具执行完毕后，将结果返回给Agent。这个结果被称为"观察"——它是Agent对外部世界执行操作后获得的反馈信息。观察结果可能是文件元数据、反汇编指令列表、字符串提取结果等。Agent将观察结果纳入上下文，用于指导下一步的思考。

#### ReAct循环流程图

下图直观展示了ReAct模式的完整执行流程：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4b0EHuFXR53jrYP06bd0TOjbH7Vlia2pr8c2PuklnGYmokx3BFWLiaQXUOu4xIGfO61e08FIpsX5Wa72iaqCp3V7icC07taLh1QspM/640?wx_fmt=png&from=appmsg)

除了静态图，你也可以通过Mermaid语法来理解ReAct循环的流程结构。

flowchart TD
    A[用户输入<br/>User Input] --> B[思考 Thought<br/>分析当前状态，决定下一步]
    B --> C{需要工具?}
    C -->|是| D[行动 Action<br/>选择工具 + 构造参数]
    C -->|否| E[最终答案<br/>Final Answer]
    D --> F[工具执行<br/>Tool Execution]
    F --> G[观察 Observation<br/>获取执行结果]
    G --> H{任务完成?}
    H -->|是| E
    H -->|否| B
    E --> I[返回结果给用户]

    style A fill:#5C7A99,stroke:#2E4A62,color:#fff
    style B fill:#4A6FA5,stroke:#2E4A62,color:#fff
    style D fill:#4A6FA5,stroke:#2E4A62,color:#fff
    style G fill:#8BA3C7,stroke:#2E4A62,color:#fff
    style E fill:#5C7A99,stroke:#2E4A62,color:#fff
    style F fill:#E8D5B7,stroke:#C4956A,color:#333
    style H fill:#E8D5B7,stroke:#C4956A,color:#333

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Ye3siahpHUMCqlh2vZCSRPYicfNKz4HAIDkoy8zKtqjJRTLTaNXEw9BouHQcFmgibZPlHECgzzeyia2b9tpbibQVcLicIYSGSyWSiaTs/640?wx_fmt=png&from=appmsg)

在项目的文档或README中，你可以直接嵌入以下Mermaid图表：在这个流程图中，菱形节点代表决策点。第一个决策点"需要工具？"判断Agent是否已经掌握了足够信息来直接回答；第二个决策点"任务完成？"判断观察结果是否满足任务目标。只要任务未完成，流程就会回到"思考"节点，开启下一轮循环。这种循环结构赋予了Agent强大的适应性——它可以根据中间结果动态调整策略，而不是死板地遵循预设步骤。

#### 为什么ReAct模式如此有效

ReAct模式的威力在于它将**推理轨迹**（Reasoning Traces）和**任务行动**（Task Actions）交织在一起2^。这种交织带来了三个关键优势：

第一，**推理过程可解释**。由于每一步思考都以自然语言文本的形式显式记录在对话历史中，你可以精确追踪Agent的决策逻辑。当Agent做出错误决策时，你能看到它"想了什么"，从而定位问题根源。

第二，**错误恢复能力强**。如果某个工具调用失败或返回了意外结果，Agent在下一步思考中可以识别问题并调整策略。例如，如果反汇编工具因不支持的架构而报错，Agent可以切换到备用分析工具或请求用户提供更多信息。

第三，**利用LLM的涌现推理能力**。大型语言模型在Chain-of-Thought（思维链）提示下表现出强大的逐步推理能力3^。ReAct模式正是将工具调用嵌入到思维链中，让LLM在每一步都能基于最新的观察结果做出更准确的判断。

#### ReAct的简化JavaScript实现

下面是一个最简化的ReAct Agent实现，帮助你理解其核心逻辑：

```
// react-simplified.mjs - ReAct Agent 核心循环的简化实现
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

/**
 * 简化的ReAct Agent执行循环
 * @param {string} question - 用户问题
 * @param {Array} tools - 可用工具列表
 * @param {number} maxSteps - 最大执行步数（安全限制）
 */
async function reactAgent(question, tools, maxSteps = 10) {
  // 初始化对话历史，包含系统提示
  const messages = [
    {
      role: 'system',
      content: 'You are a ReAct agent. Think step by step. ' +
        'Format your response as: Thought: <your reasoning>\n' +
        'Action: <tool_name>\nAction Input: <json_params>\n' +
        'Or "Final Answer: <answer>" when done.'
    },
    { role: 'user', content: question }
  ];

  // 核心循环：Thought -> Action -> Observation
  for (let step = 0; step < maxSteps; step++) {
    console.log(`\n=== Step ${step + 1} ===`);

    // 1. 调用LLM生成Thought和Action
    const response = await generateText({
      model: openai('gpt-4o'),
      messages,
      tools: Object.fromEntries(tools.map(t => [t.name, t])),
    });

    // 2. 检查是否产生Final Answer（任务完成）
    if (response.text && response.text.includes('Final Answer:')) {
      return response.text.split('Final Answer:')[1].trim();
    }

    // 3. 执行工具调用（Action -> Observation）
    if (response.toolCalls && response.toolCalls.length > 0) {
      for (const toolCall of response.toolCalls) {
        const tool = tools.find(t => t.name === toolCall.name);
        if (!tool) {
          messages.push({
            role: 'tool',
            content: JSON.stringify({ error: `Tool "${toolCall.name}" not found` })
          });
          continue;
        }

        // 执行工具函数，获得Observation
        const result = await tool.execute(toolCall.args);
        messages.push({
          role: 'tool',
          content: JSON.stringify(result)
        });
        console.log(`  Tool: ${toolCall.name} -> ${JSON.stringify(result).slice(0, 100)}`);
      }
    }
  }

  throw new Error(`Max steps (${maxSteps}) exceeded without final answer`);
}

// 使用示例
const tools = [
  {
    name: 'get_weather',
    description: 'Get weather for a city',
    parameters: { type: 'object', properties: { city: { type: 'string' } }, required: ['city'] },
    execute: async ({ city }) => ({ temperature: 22, condition: 'Sunny', city })
  }
];

// await reactAgent("What's the weather in Tokyo?", tools);
```

这个简化实现虽然不到50行核心逻辑，却完整展现了ReAct的本质：一个以LLM推理为驱动、工具调用为手段、对话历史为记忆载体的循环执行系统。在第2.3节中，你将实现一个更加完整、具备结构化输出解析和健壮错误处理的ReAct Agent类。

### 2.1.2 Plan-and-Execute模式：先规划后执行

与ReAct的"边想边做"不同，**Plan-and-Execute**（规划-执行）模式采用**两阶段架构**4^：首先让LLM生成一个完整的执行计划（Plan），然后严格按照计划逐项执行（Execute）。这种模式更适合结构化、可预见的多步骤任务。

#### Plan-and-Execute的三个阶段

**规划阶段（Planning Phase）**：Agent接收任务后，首先调用LLM生成一个详细的执行计划。这个计划通常是一个子任务列表，每个子任务都有明确的输入、输出和依赖关系。例如，分析一个二进制文件的计划可能是：

1. 获取文件基本元数据（格式、架构、大小）
2. 提取文件中的可打印字符串
3. 反汇编.text段获取函数列表
4. 扫描危险函数调用
5. 综合分析结果并生成报告

**执行阶段（Execution Phase）**：Agent按照计划中的顺序逐一执行每个子任务。执行可以是串行的（一个完成后再开始下一个），也可以是并行的（没有依赖关系的子任务同时执行）。每个子任务的输出结果会被收集起来，作为后续子任务的输入或最终报告的素材。

**反思阶段（Reflection Phase）**：所有子任务执行完毕后，Agent会对整体结果进行检查和反思。如果某些步骤执行失败或结果不符合预期，Agent可以决定是否需要调整计划并重新执行部分任务。这个阶段是可选的，但在复杂任务中能显著提高成功率。

下图展示了Plan-and-Execute模式的完整流程，你可以将其与ReAct模式的流程进行对比，体会两者在控制流上的根本差异：

```
工具3工具2工具1Executor执行器Planner规划器用户工具3工具2工具1Executor执行器Planner规划器用户规划阶段和执行阶段严格分离无依赖的子任务可并行执行提交任务LLM推理：分解任务为子计划返回执行计划[Step1, Step2, Step3]按计划执行调用 Step1结果1调用 Step2 (可与Step1并行)结果2调用 Step3结果3汇总所有结果返回最终报告
```

从序列图中可以清楚看到，Plan-and-Execute的核心特征是**阶段分离**——规划器（Planner）完成全部分析后才将控制权移交给执行器（Executor），执行器则严格按照预定计划执行，不再进行动态决策。这种"先思后行"的方式在执行确定性任务时更加可靠，因为你可以在执行前审查和修改计划。

#### Plan-and-Execute的优势场景

Plan-and-Execute模式特别适合以下场景：

* **任务步骤可预见**：任务可以被清晰地分解为固定序列的子任务，如二进制分析流水线
* **需要确定性控制**：你希望严格掌控执行顺序，而不是让Agent"随机应变"
* **可并行化**：部分子任务之间没有依赖关系，可以并行执行以提高效率
* **结果可组合**：每个子任务的输出可以被独立收集并组合成最终结果

#### Plan-and-Execute的实现示例

```
// plan-and-execute.mjs - 两阶段架构的简化实现
import { generateText } from 'ai';

/**
 * Plan-and-Execute Agent
 * 先规划完整步骤，再按顺序执行
 */
async function planAndExecute(task, tools, llm) {
  // ===== Phase 1: Planning =====
  const planPrompt = `Create a step-by-step plan to: ${task}\n` +
    `Available tools: ${tools.map(t => t.name).join(', ')}\n` +
    `Respond with JSON: { "steps": [{ "tool": "name", "input": {}, "reason": "why" }] }`;

  const planResponse = await generateText({
    model: llm,
    prompt: planPrompt,
  });

  // 解析计划（假设LLM返回了有效的JSON）
  const plan = JSON.parse(planResponse.text);
  console.log(`Plan created with ${plan.steps.length} steps`);

  // ===== Phase 2: Execution =====
  const results = [];
  for (const step of plan.steps) {
    const tool = tools.find(t => t.name === step.tool);
    if (!tool) {
      results.push({ step, error: `Tool not found: ${step.tool}` });
      continue;
    }

    // 执行子任务
    const result = await tool.execute(step.input);
    results.push({...