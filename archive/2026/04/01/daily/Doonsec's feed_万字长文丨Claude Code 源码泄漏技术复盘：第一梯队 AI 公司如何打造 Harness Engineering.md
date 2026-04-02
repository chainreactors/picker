---
title: 万字长文丨Claude Code 源码泄漏技术复盘：第一梯队 AI 公司如何打造 Harness Engineering
url: https://mp.weixin.qq.com/s/P2q0ZuQWeIOP-XRLgdLVVw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:55.024291
---

# 万字长文丨Claude Code 源码泄漏技术复盘：第一梯队 AI 公司如何打造 Harness Engineering

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lfebBgkWzEPb7CXPoxUpRnmMCrXaAxaADf2WjEXVYx6AG1hwcV6RMjk8UfFXjcAbhTxicfSoHuBE8wbDvRb8kIH0Fsk8j9ibMOUwd64yurRj8/0?wx_fmt=jpeg)

# 万字长文丨Claude Code 源码泄漏技术复盘：第一梯队 AI 公司如何打造 Harness Engineering

玉衡实验室
玉衡实验室

山海之关

![]()

在小说阅读器中沉浸阅读

**摘要**

本次泄漏事件，表面上是一份 Claude Code 发布包，实质上却让外界第一次较完整地看到了顶级 AI Coding Agent 的工程骨架。从 cli.js.map 可恢复的大量源码来看，Claude Code 的核心并不是“会写代码的聊天机器人”，而是一套典型的 [Harness Engineering](https://mp.weixin.qq.com/s?__biz=MzY5NjE2OTU0Mg==&mid=2247483874&idx=1&sn=2fa046ab66dcca78fc16bc388cbd8a68&scene=21#wechat_redirect) 系统：它把大模型装进一个有工具注册表、权限系统、沙箱策略、计划模式、任务清单、子 Agent 协作、会话记忆、MCP/插件接入和灰度开关的可控执行框架里。结论很明确：第一梯队 AI 公司竞争的重点，已经不只是模型能力，而是如何把模型封装进一个能够稳定执行、可验证交付、可灰度运营、可持续扩展的 Harness Engineering。

**一、研究背景：为什么这次事件值得技术复盘**

大多数人看 AI Coding 产品时，注意力会自然落在模型回答得准不准、代码写得快不快、会不会自动改文件。但从工程视角看，这些只是表层表现。真正决定产品上限的，往往是下面几个问题：

* 模型如何安全地接触真实文件系统和终端
* 模型如何被约束在可解释、可审计的工具调用路径里
* 模型如何管理长任务、拆分任务、做验证、保留状态
* 产品如何把实验功能、内部能力和正式功能放进同一套 runtime
* 团队如何把 AI 能力做成平台，而不只是某个 prompt 技巧

这正是 Harness Engineering 的问题域。

如果用更通俗的话说，Harness Engineering 不是研究“模型会不会做事”，而是研究“怎样让模型在真实系统里、按可控方式、持续稳定地做事”。  这份 Claude Code 包，恰好提供了一个观察窗口。

**二、研究方法与证据边界**

**0****1**

**一手证据：当前目录中的打包产物与 Source Map**

本次分析主要基于以下文件：

* package/package.json

* package/cli.js
* package/cli.js.map

其中，最关键的是 cli.js.map。它不是压缩包，而是一个 source map 文件，内部包含：

* sources：原始源码路径
* sourcesContent：原始源码正文

基于这份 map，内嵌源码已完整恢复到本地目录：

* recovered-src

共恢复出约 1900 个 src/\*\* 文件片段，用于本文中的代码核查与引用。

**0****2**

**二手证据：官方博客、官方文档、官方账号可验证资料**

参考文献部分优先采用大厂官方资料，尤其是 Harness Engineering 相关文档与博客。因此，“概念框架”和“行业背景”优先锚定在：

* Anthropic 官方博客 / 文档
* OpenAI 官方文档
* Google / Cloud 官方博客或文档

###

**0****3**

**分析边界**

本文坚持两个原则：

* 代码事实优先：任何关于 Claude Code 的细节判断，优先由源码支持
* 推论有限：源码没写清的地方，不做过度猜测

也就是说，本文会区分：

* 源码事实：代码里直接能看到的模块、状态、注释、功能开关
* 工程推论：基于源码结构得出的合理解释，但不会把推论说成事实

**三、什么是 Harness Engineering，为什么它适合解释 Claude Code**

在传统软件工程里，大家更熟悉“框架”“平台”“运行时”“编排系统”这些词。  到了 Agent 时代，[Harness Engineering](https://mp.weixin.qq.com/s?__biz=MzY5NjE2OTU0Mg==&mid=2247483874&idx=1&sn=2fa046ab66dcca78fc16bc388cbd8a68&scene=21#wechat_redirect) 可以理解为这些能力在 AI 系统中的重新组合。

它通常包括几个核心问题：

* 如何把模型能力绑定到工具能力
* 如何定义执行边界，而不是仅靠 prompt 自觉
* 如何让任务可以被拆分、追踪、验证和恢复
* 如何把长期记忆、外部系统和多 Agent 协作纳入统一执行平面
* 如何通过 feature flag、权限模式、实验开关来运营整个系统

而且，“harness”并不是为分析方便临时拼接出来的词。Anthropic 官方的 Claude Code SDK 文档明确把 SDK 描述为建立在“the agent harness that powers Claude Code”之上。这一点非常重要，因为它意味着从官方表述看，Claude Code 本身就被 Anthropic 理解为一个 agent harness。

从 Anthropic、OpenAI 等官方资料看，这个方向的关键词高度一致：

* tool use
* handoff / agents
* tracing / observability
* memory / long-running sessions
* safety boundaries
* evaluation harness

因此，把 Claude Code 解释为一个 [Harness Engineering](https://mp.weixin.qq.com/s?__biz=MzY5NjE2OTU0Mg==&mid=2247483874&idx=1&sn=2fa046ab66dcca78fc16bc388cbd8a68&scene=21#wechat_redirect) 案例，比把它解释为一个“强一点的 CLI 助手”要准确得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lfebBgkWzEMW6gffvo0XDaV8dljeFIhqkGibDQvwnc2uDIQCEVYqibCnw3GhtFqcia6boUk7ebcCePddcjLOiaZNyhRCS9JMZ4dWb6zInjiad9Hk/640?wx_fmt=png&from=appmsg)

图 1：Harness Engineering 的重点不是模型本身，而是模型与执行环境之间的那一层系统设计

**四、从源码看 Claude Code 的真实形态：它首先是一个工具执行框架**

**0****1**

**工具注册表说明了一切**

recovered-src/src/tools.ts 是最值得先看的文件之一。里面的 getAllBaseTools() 基本就是 Claude Code 执行平面的目录表：

```
export function getAllBaseTools(): Tools {
return [
    AgentTool,
    TaskOutputTool,
    BashTool,
    ...(hasEmbeddedSearchTools() ? [] : [GlobTool, GrepTool]),
    ExitPlanModeV2Tool,
    FileReadTool,
    FileEditTool,
    FileWriteTool,
    NotebookEditTool,
    WebFetchTool,
    TodoWriteTool,
    WebSearchTool,
    TaskStopTool,
    AskUserQuestionTool,
    SkillTool,
    EnterPlanModeTool,
    ...(process.env.USER_TYPE === 'ant' ? [ConfigTool] : []),
    ...(process.env.USER_TYPE === 'ant' ? [TungstenTool] : []),
```

单看这一段，已经足够得出一个基础判断：

* Claude Code 的核心不是消息窗口
* 它是一个以工具调用为中心的Agent运行时

这些工具覆盖了多个层面：

* 文件系统操作
* 终端与 PowerShell 执行
* Web 获取与搜索
* 计划与任务清单
* 用户问答
* 技能系统
* 子Agent能力

这意味着 Claude Code 不是“让模型输出文本”，而是“让模型驱动一个被定义好的行动集合”。

**0****2**

**大量能力被 feature gate 包裹，说明这是平台级产品**

同一文件里，大量工具并不是永久启用，而是跟随特性开关：

```
const SleepTool =
  feature('PROACTIVE') || feature('KAIROS')
    ? require('./tools/SleepTool/SleepTool.js').SleepTool
    : null

const cronTools = feature('AGENT_TRIGGERS')
  ? [
      require('./tools/ScheduleCronTool/CronCreateTool.js').CronCreateTool,
      require('./tools/ScheduleCronTool/CronDeleteTool.js').CronDeleteTool,
      require('./tools/ScheduleCronTool/CronListTool.js').CronListTool,
    ]
  : []

const RemoteTriggerTool = feature('AGENT_TRIGGERS_REMOTE')
  ? require('./tools/RemoteTriggerTool/RemoteTriggerTool.js').RemoteTriggerTool
  : null
```

这里至少透露出三层工程信号：

* 有正式功能与实验功能并存的机制
* 有面向不同用户群、不同环境做差异化启停的能力
* Claude Code 背后存在完整的线上配置与灰度系统

这已经不是一个“打包好的桌面小工具”的组织方式，而是成熟平台软件的组织方式。

**五、Claude Code 的命令层不是附属功能，而是统一入口层**

如果说 tools.ts 展示了动作集合，那么 recovered-src/src/commands.ts 展示的就是入口集合。

文件里除了传统命令，还出现了大量能指向未来产品形态的入口：

```
import teleport from './commands/teleport/index.js'
import chrome from './commands/chrome/index.js'
import stickers from './commands/stickers/index.js'
import advisor from './commands/advisor.js'
import mobile from './commands/mobile/index.js'
```

还有按特性启用的命令：

```
const voiceCommand = feature('VOICE_MODE')
  ? require('./commands/voice/index.js').default
  : null

const webCmd = feature('CCR_REMOTE_SETUP')
  ? (
      require('./commands/remote-setup/index.js') as typeof import('./commands/remote-setup/index.js')
    ).default
  : null

const buddy = feature('BUDDY')
  ? (
      require('./commands/buddy/index.js') as typeof import('./commands/buddy/index.js')
    ).default
  : null
```

从工程角度看，这说明 Claude Code 不是单一使用场景产品，而是一个正在向多宿主环境扩张的 Agent 平台。命令层很像一层路由系统，把不同入口需求映射到统一 runtime。

工程推论可以概括为一句话：Claude Code 的 CLI，只是它当前最清晰的壳；并不意味着它的能力边界只在 CLI。

**六、计划模式、Todo、验证 Agent：这不是“会规划”，而是“把规划做成系统状态”**

很多 AI 产品会说自己“支持 planning”。但大多数时候，这只是 prompt 层的行为。  Claude Code 不一样，它把规划做成了 runtime 的显式状态。

**0****1**

**Plan Mode 是一个真模式，而不是口头承诺**

recovered-src/src/commands/plan/plan.tsx 中，可以看到：

```
if (currentMode !== 'plan') {
  handlePlanModeTransition(currentMode, 'plan');
  setAppState(prev => ({
    ...prev,
    toolPermissionContext: applyPermissionUpdate(prepareContextForPlanMode(prev.toolPermissionContext), {
      type: 'setMode',
      mode: 'plan',
      destination: 'session'
    })
  }));
  const description = args.trim();
if (description && description !== 'open') {
    onDone('Enabled plan mode', {
      shouldQuery: true
    });
  } else {
    onDone('Enabled plan mode');
  }
return null;
}
```

这段代码至少说明三件事：

* plan 是一个显式 mode
* mode 会驱动 toolPermissionContext 变化
* 计划流程会影响后续 query 行为

这和“模型先想一想再答”是两个层次的事情。  前者是系统状态机，后者只是语言习惯。

**0****2**

**Todo 是执行骨架的一部分**

recovered-src/src/tools/TodoWriteTool/TodoWriteTool.ts 中，Todo 并不是 UI 装饰，而是执行主线的组成部分：

```
export const TodoWriteTool = buildTool({
  name: TODO_WRITE_TOOL_NAME,
  searchHint: 'manage the session task checklist',
  ...
  async call({ todos }, context) {
    const appState = context.getAppState()
    const todoKey = context.agentId ?? getSessionId()
    const oldTodos = appState.todos[todoKey] ?? []
    const allDone = todos.every(_ => _.status === 'completed')
    const newTodos = allDone ? [] : todos
```

这说明 Claude Code 把任务清单做成了 session state 的一部分，而不是单纯的前端展示。

**0****3**

**验证不是“可选美德”，而是被编码进工作流的要求**

同文件中最值得注意的一段，是对 verification 的提醒：

```
if (
  feature('VERIFICATION_AGENT') &&
  getFeatureValue_CACHED_MAY_BE_STALE('tengu_hive_evidence', false) &&
  !context.agentId &&
  allDone &&
  todos.length >= 3 &&
  !todos.some(t => /verif/i.test(t.content))
) {
  verificationNudgeNeeded = true
}
```

并且结果信息中还会追加明确提示：

```
const nudge = verificationNudgeNeeded
  ? \n\nNOTE: You just closed out 3+ tasks and none of them was a verification step. Before writing your final summary, spawn the verification agent...
  : ''
```

这说明 Claude Code 的工程哲学不是“做完就汇报”，而是“做完之前需要 verification”。  从 harness 角度看，这是一种非常关键的差异：系统开始主动约束交付质量，而不是只提升生成速度。

![](https://mmbiz.qpic.cn/mmbiz_png/lfebBgkWzENs1EWAFJSxsodsxXsppf7N0xdicrVF8Ds...