---
title: 3. 工具集成与函数调用
url: https://mp.weixin.qq.com/s/DL-nCDykvECfde27TPJ8OQ
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:06.382582
---

# 3. 工具集成与函数调用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4YXPHAI86cgXgAWg2MRQE01sbjtt92hfSRm6hXkTltWQbHmobUjkEpKFrpqUkkicESjkExbMOtejuUiaA5yQ7GXaY05COUcJ2bmk/0?wx_fmt=jpeg)

# 3. 工具集成与函数调用

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

前两章你已经了解了Agent的核心架构模式——ReAct的循环思维和Plan-and-Execute的计划执行策略，也构建了ConfigManager、LLM Provider、MessageHistory、ToolRegistry和ExecutionEngine等基础模块。但一个只能"思考"却无"手脚"的Agent，就像一位被困在玻璃房中的大脑：洞察力再强，也无法触碰外部世界。工具（Tool）就是Agent的手脚，Function Calling（函数调用）则是连接大脑与手脚的神经系统。

想象一个场景：用户问Agent"帮我看看sample-project目录下的main.py文件质量如何，顺便检查一下它的依赖是否有过时的"。没有工具的Agent只能回答"我无法访问您的文件系统"——这是一个教科书式的正确答案，却毫无实用价值。而配备了文件系统工具、代码分析工具和HTTP查询工具的Agent，则会这样工作：首先调用 `list_directory` 确认项目结构，然后调用 `read_file` 读取main.py的内容，接着调用 `analyze_file` 计算圈复杂度和检测代码异味，再调用 `read_file` 读取requirements.txt，最后调用 `http_get` 查询PyPI确认依赖版本——整个过程完全自主，无需人工干预。这种从"只能对话"到"能做事"的跨越，正是工具集成赋予Agent的核心能力。

在AI工程实践中，工具系统的质量往往决定了一个Agent的实用上限。再强大的LLM，如果无法准确地调用工具、处理工具返回的结果、从错误中恢复，都只能是一个"聪明的聊天机器人"。本章将带你从零开始构建一套完整的工具系统。你将学习如何用Zod定义工具参数结构、用装饰器模式实现工具注册、如何安全地执行文件和网络操作、如何让LLM准确理解工具用途，最终整合第1-3章的全部知识构建一个支持文件分析和网络查询的命令行Agent工具。

### 3.1 工具（Tool）系统设计

在深入实现之前，你需要理解工具系统的整体架构。一个成熟的工具系统包含四个核心层面：Schema定义层负责描述工具的参数结构，让LLM知道调用工具时需要传什么参数；注册与发现层负责管理工具的生命周期，支持动态添加和查询；执行与错误处理层负责调用工具并处理超时、异常等各种边界情况；描述优化层则确保LLM能准确理解每个工具的用途，减少误调用。这四个层面协同工作，构成了Agent与外部世界交互的完整管道。

从LLM的视角来看，工具调用遵循一个固定的循环：用户输入 → LLM分析意图 → 判断是否需要工具 → 生成工具调用JSON → 系统执行工具 → 结果返回LLM → LLM基于结果继续思考或生成最终回复。这个循环就是Function Calling的核心流程。你的工具系统需要在这个循环的每个环节都提供可靠的支持：注册阶段给LLM完整的工具目录，执行阶段可靠地运行工具并返回结构化结果，错误处理阶段确保即使工具失败也不会打断整个对话流程。

#### 3.1.1 工具的定义与Schema：Zod对象定义工具参数结构，自动生成JSON Schema

工具的本质是一个带有元数据的函数。这个元数据告诉LLM：这个工具叫什么、能做什么、需要传入什么参数。LLM收到用户的自然语言请求后，会分析意图并生成一个结构化调用——`{"tool": "read_file", "arguments": {"path": "/home/user/main.py"}}`。但LLM如何知道 `read_file` 存在、它需要哪些参数？答案就是JSON Schema。

JSON Schema是一种标准化的数据格式描述语言（IETF RFC规范）。当你向LLM发送请求时，需要将每个工具的参数定义转换为JSON Schema格式作为请求的一部分。OpenAI的Function Calling接口、Anthropic的Tool Use接口、Google的Function Calling接口，以及MCP协议，底层都依赖JSON Schema来描述工具参数。理解JSON Schema的语法规则，是设计工具系统的必备基础。

在TypeScript生态中，Zod是定义参数Schema的最佳选择。它不仅是运行时类型验证库，还能自动生成JSON Schema。更重要的是，Zod与TypeScript的类型系统深度融合——`z.infer<typeof schema>` 能自动推导出参数的类型，你无需维护两套定义。这种"单一真相源"的设计大大降低了维护成本，当你修改参数结构时，类型系统和LLM接口会自动同步更新。

来看第一个完整代码示例，涵盖Zod的各种参数类型：

```
// examples/01_tool_schema_definition.ts
import { z } from "zod";

// ====== 基础类型参数 ======

// 1. 字符串参数（最常用）
const stringSchema = z.object({
  query: z.string()
    .min(1, "搜索关键词不能为空")
    .max(200, "关键词过长，最大200字符")
    .describe("搜索关键词，如 'TypeScript 教程'"),
});

// 2. 数值参数与范围限制
const numberSchema = z.object({
  page: z.number()
    .int("页码必须为整数")
    .min(1, "页码从1开始")
    .max(1000, "最大页码1000")
    .optional()
    .default(1)
    .describe("页码，默认第1页"),
  pageSize: z.number().int().min(1).max(100).optional().default(20)
    .describe("每页条数，默认20条"),
});

// 3. 布尔参数
const booleanSchema = z.object({
  recursive: z.boolean().optional().default(false)
    .describe("是否递归处理子目录，默认 false"),
});

// ====== 复合类型参数 ======

// 4. 枚举参数（限制取值范围）
const enumSchema = z.object({
  format: z.enum(["json", "markdown", "table", "yaml"])
    .optional().default("json")
    .describe("输出格式：json（结构化数据）、markdown（易读文本）、table（表格）、yaml"),
});

// 5. 对象嵌套（复杂配置）
const nestedSchema = z.object({
  file: z.string().describe("目标文件路径"),
  options: z.object({
    encoding: z.enum(["utf8", "base64", "binary"]).default("utf8")
      .describe("文件编码格式"),
    maxSize: z.number().int().max(10 * 1024 * 1024).default(1024 * 1024)
      .describe("最大读取字节数，默认1MB"),
  }).optional().describe("高级读取选项"),
});

// 6. 数组参数与对象数组
const arraySchema = z.object({
  files: z.array(z.string()).min(1).max(100)
    .describe("待处理的文件路径列表"),
  operations: z.array(z.object({
    type: z.enum(["read", "write", "delete", "analyze"]),
    target: z.string().describe("操作目标路径"),
  })).min(1).describe("要执行的操作序列"),
});

// ====== 工具接口与Schema生成器 ======

interface ToolDefinition<T extends z.ZodTypeAny> {
  name: string;
  description: string;
  parameters: T;
  execute: (args: z.infer<T>) => Promise<unknown>;
}

function zodToJsonSchema(schema: z.ZodTypeAny): any {
  if (schema instanceof z.ZodObject) {
    const shape = schema.shape;
    const properties: Record<string, any> = {};
    const required: string[] = [];
    for (const [key, value] of Object.entries(shape)) {
      const zodValue = value as z.ZodTypeAny;
      properties[key] = extractTypeInfo(zodValue);
      if (!(zodValue instanceof z.ZodOptional) && !(zodValue instanceof z.ZodDefault))
        required.push(key);
    }
    return { type: "object", properties, required };
  }
  return { type: "unknown" };
}

function extractTypeInfo(schema: z.ZodTypeAny): any {
  if (schema instanceof z.ZodOptional || schema instanceof z.ZodDefault)
    return extractTypeInfo(schema._def.innerType);
  if (schema instanceof z.ZodString) return { type: "string", description: schema.description };
  if (schema instanceof z.ZodNumber) return { type: "number", description: schema.description };
  if (schema instanceof z.ZodBoolean) return { type: "boolean", description: schema.description };
  if (schema instanceof z.ZodEnum) return { type: "string", enum: schema._def.values, description: schema.description };
  if (schema instanceof z.ZodArray) return { type: "array", items: extractTypeInfo(schema._def.type), description: schema.description };
  if (schema instanceof z.ZodObject) return zodToJsonSchema(schema);
  return { type: "string" };
}

// ====== 实战：天气查询工具 ======
const weatherSchema = z.object({
  city: z.string().describe("城市名称，如 '北京'、'Shanghai'、'Tokyo'"),
  units: z.enum(["celsius", "fahrenheit"]).optional().default("celsius")
    .describe("温度单位：celsius（摄氏度）或 fahrenheit（华氏度）"),
});

const weatherTool: ToolDefinition<typeof weatherSchema> = {
  name: "get_weather",
  description: `获取指定城市的当前天气信息。当用户询问天气、温度、湿度、降雨或户外活动建议时，必须使用此工具。不适用于历史天气查询或长期预报。`,
  parameters: weatherSchema,
  execute: async ({ city, units = "celsius" }) => ({
    city, temperature: units === "celsius" ? 25 : 77,
    condition: "Sunny", humidity: 60, units,
  }),
};

console.log(JSON.stringify(zodToJsonSchema(weatherSchema), null, 2));
```

这个示例覆盖了Zod的六种核心类型。字符串 `z.string()` 是最常用的参数类型，通过 `.min()` 和 `.max()` 限制长度。数值 `z.number()` 配合 `.int()` 确保整数，配合 `.min()` 和 `.max()` 限定范围。枚举 `z.enum()` 是控制LLM参数取值的最有效方式。特别值得关注的是 `.optional().default()` 链——它标记参数为可选并提供默认值，LLM不确定时可以省略这个参数。

为什么要用Zod而不是直接手写JSON Schema？答案有三个层面。第一是类型安全：Zod Schema在编译时提供TypeScript类型推断，`z.infer<typeof weatherSchema>` 会自动推导出参数类型。第二是运行时验证：工具被调用时，Zod的 `safeParse()` 自动校验参数合法性，不合法的调用在执行前就会被拦截。第三是描述内联：`.describe()` 与类型定义写在一起，避免了"改Schema忘改描述"的维护问题。这三者的结合让Zod成为工具Schema定义的事实标准。

#### 3.1.2 工具注册与发现机制：装饰器模式注册、运行时工具列表动态构建

定义好工具后，你需要一个注册中心来统一管理它们。ToolRegistry是Agent架构中的核心模块，负责工具的注册、发现和元数据查询。这里采用装饰器模式来实现——这是TypeScript中最优雅的元数据注册方式。

装饰器模式的核心思想是"声明即注册"。当你用 `@Tool({...})` 装饰一个类方法时，工具的元数据就被附加到该类的元数据存储中。运行时通过反射读取这些元数据，自动完成工具注册。这种方式让你无需在代码角落维护冗长的注册列表，工具的定义和实现始终在一起。

```
// examples/02_tool_registry_decorator.ts
import { z } from "zod";
import "reflect-metadata";

const TOOL_METADATA_KEY = Symbol("tool:metadata");

interface ToolMetadata {
  name: string;
  description: string;
  schema: z.ZodTypeAny;
  target: any;
  propertyKey: string | symbol;
}

function Tool(config: { name: string; description: string; schema: z.ZodTypeAny }) {
  return function (target: any, propertyKey: string | symbol, descriptor: PropertyDescriptor) {
    const existing: ToolMetadata[] =
      Reflect.getMetadata(TOOL_METADATA_KEY, target.constructor) || [];
    existing.push({ name: config.name, description: config.description,
      schema: config.schema, target, propertyKey });
    Reflect.defineMetadata(TOOL_METADATA_KEY, existing, target.constructor);
  };
}

class ToolRegistry {
  private tools = new Map<string, {
    metadata: ToolMetadata;
    handler: (args: any) => Promise<unknown>;
    jsonSchema: object;
  }>();

  registerFromInstance(instance: any): void {
    const constructor = instance.constructor;
    const tools: ToolMetadat...