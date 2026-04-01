---
title: Claude Code 51万行源码全网裸奔！Anthropic：我们终于成了“真·Open Claude”
url: https://mp.weixin.qq.com/s/joOfXGJkuXmXdR1jtN0jGw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:11.309214
---

# Claude Code 51万行源码全网裸奔！Anthropic：我们终于成了“真·Open Claude”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ib6PGXfLnjAPVBjYAHoavgJgInyO24yI6OziaM5RYmcjTibN0MjlBic95icUzBRGNz2XNFg1UUxyHhZRrKQ6hbS5tYRQH9LZnhVKmbOEhB7Z50xw/0?wx_fmt=jpeg)

# Claude Code 51万行源码全网裸奔！Anthropic：我们终于成了“真·Open Claude”

原创

心态与度量
心态与度量

随心记事

![]()

在小说阅读器中沉浸阅读

吃瓜地址：

**https://github.com/instructkr/claude-code/tree/main/src**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib6PGXfLnjAPaH9Ke1gia2hibA8otg4Nz0kPzClfqtPGHLlyunDBJg1stPpaVrWoCGKCzLoYdK5gfHnpHIS6ibV1NQibjtjrmSpeSCQIxcK3BHs4/640?wx_fmt=png&from=appmsg)

issue页迅速成为了合影留念等，广告发源地

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib6PGXfLnjAN2Kcn2boKbXl6rn87fTZ3Dm6PHzgCEO3HfibpfzrkSQsBEuTiaG5JvHgzZCqpicpLwAhnxJ83jVU7VUvfVw6JJa1x9twhRBJzROw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib6PGXfLnjAO5gJEo0TEMgTcnRU09YIgNmsiacE6YvIEpH65SxFfjWziaxJOaOCziamtbB2qcTRuvibQibjzqUvUSQeTAhoibaoibQhrK7RakIamiaM4/640?wx_fmt=png&from=appmsg)

今天2026年3月31日，本来就是个普通周二，结果Anthropic直接给全网开发者发了个超级大礼包——**「Claude Code CLI的完整TypeScript源码」**，整整1900多个文件、51.2万行代码，一点都没藏着掖着，就这么“开源”了！不是他们在GitHub上主动发的，也不是突然良心发现，而是npm包里忘记删掉的\*\*.map文件\*\*干的好事。

安全研究员Chaofan Shou（@shoucccc）一发帖，瞬间全网炸锅。GitHub上几个镜像仓库几个小时就冲到上万star。Anthropic反应倒挺快，赶紧把源地图删了……但已经晚了，代码早就被大家存档、下载、狂抄了。

这已经是他们本月第二次“意外公开”了，上次是Claude Mythos模型的内部文档，这次直接把自家旗舰终端Agent的心脏整个掏出来给大家看。AI公司自己用Claude写代码，结果打包的时候Claude都没提醒删debug文件，这操作也太抽象了吧哈哈哈。

更离谱的是，想想今年1月的事儿——Anthropic对“Claude”商标护得那叫一个死。热门开源项目Clawdbot就因为名字带个“Clawd”听起来太像，直接被律师函伺候，硬生生改名叫Moltbot。当时全网都在刷“商标零容忍”“Claude家法伺候”，开发者吐槽“连个‘d’都不让沾”。结果这才俩月，自己就把Claude Code 51万行源码打包送全网……从“名字都不许像”到“代码全裸奔”，这反差感，Anthropic这波是把“严于律人、宽以待己”玩到极致了，笑死我了😂

### 一、到底是怎么翻车的？简单说说技术细节

就出在 **「@anthropic-ai/claude-code v2.1.88」** 这个npm包上。

正常来说，前端/CLI打包流程里，TypeScript代码会用tsc加esbuild/rollup压成生产环境的JS（压缩+摇树）。调试的时候会顺便生成source map（.map文件），里面塞了原始TS源码、行列映射、文件路径啥的。

正常人生产发布的时候，**「sourceMap要关掉，或者把.map文件踢出npm publish」**。结果Anthropic的CI/CD流水线里这个开关没关严，**「cli.js.map」**（60MB+的大块头）就这么堂而皇之躺在npm仓库里了。

随便`npm install @anthropic-ai/claude-code@2.1.88`解压一下，完整可读的TypeScript源码就到手了。研究员直接镜像到GitHub，现在大家都在狂欢。

这压根不是黑客入侵，就是最经典的供应链手滑——老DevOps看了沉默，新手看了流泪。

### 二、源码里到底有啥？这次我直接深挖技术细节（技术党狂喜）

我把几个公开镜像翻了个底朝天，挑最硬核的部分跟你细聊（纯技术讨论，不涉及任何商业机密，纯学习）：

1. **「架构层：React + Ink + Zustand 的现代TUI框架」**
   整个CLI其实是个完整的React应用跑在Ink上（Ink是React的终端渲染引擎）。源码里主入口 `src/app.tsx` 里用了 `useInk` 渲染根组件，状态管理直接上 Zustand（不是Redux那种重型货），全局 store 分成了 `agentStore`、`sessionStore`、`toolStore` 三个模块。
   界面组件树超级清晰：`<CommandPalette>` 用 `ink-text-input` 实现模糊搜索，`<StreamingOutput>` 用 `useEffect` + SSE（Server-Sent Events）实时渲染Claude的token流，`<AgentOrchestrator>` 负责多轮对话的有限状态机（FSM），里面还有 `useTransition` 处理loading态，丝滑得一批。比我以前见过的所有CLI工具都现代，怪不得大家用完就回不去了。
2. **「Agentic核心：40+ Tool + 50+ Slash Command + 动态Tool Registry」**
   最牛的是 `src/tools/` 目录，里面每个Tool都是一个独立的 TS 类，继承 `BaseTool` 抽象类，实现 `execute()`、`getSchema()`、`validatePermission()` 三个方法。
   比如 `FileSystemTool` 里直接用 `fs.promises` + `globby` 做文件读写，还带了沙箱限制（只能操作当前workspace）；`GitTool` 封装了 `simple-git`；`BrowserTool` 居然用了 Puppeteer + stealth插件，能无头控制浏览器；`CodeSandboxTool` 则是子进程跑临时 Node REPL，执行用户代码前先做 AST 静态扫描防恶意。
   Slash Command 用 `commander.js` 扩展，`/edit` 命令直接调用内部 diff 算法（基于 `diff` 库），支持多文件并行编辑。里面还有几个隐藏模式（`hiddenModes` 配置），比如 `autonomous-refactor` 能让Agent自己跑循环：分析→重构→测试→迭代，最多10轮自动停止。源码里注释写着“Claude建议增加反思步骤”，我直接笑喷。
3. **「上下文引擎：动态压缩 + RAG + 长时记忆全家桶」**
   `src/context/` 这一块是精华。`ContextManager` 类里实现了三层上下文处理：

* **「短期」**：直接塞最近20轮对话（token预算动态计算）；
* **「中期」**：用 `langchain` 风格的 summarizer 把历史对话压成摘要；
* **「长期」**：内置向量检索（用 `@xenova/transformers` 在本地跑 embedding + LanceDB 做向量库），支持“回忆上周改的那个bug”。
  还有 `reflectionLoop` 函数，每3轮就让Claude自己审视一次输出质量，生成 self-critique，然后自动修正。代码质量高到离谱，类型定义全用 Zod 校验，注释里到处是“Claude在prompt里建议的优化点”。

4. **「安全与OpSec」**
   讽刺到爆：`src/security/` 目录里有 `PromptInjectionGuard`、`ToolCallAuditor`、`PermissionBoundary` 等一堆类，做了输入清洗、输出沙箱、审计日志全链路。结果自己打包的时候把source map全扔进去了……安全团队现在估计在喝咖啡压惊。

总的来说，这51万行代码把“**「怎么把Claude真正打造成生产级终端Agent」**”的工程细节全摊开了，从TUI交互到Agent编排、从Tool沙箱到上下文优化，全是干货中的干货。

### 三、源码怎么利用？开发者直接起飞的实用指南

这波泄漏不是让你白嫖，而是真·教科书。已经有人在Discord和GitHub Issues里开始讨论怎么玩了，我给你整几条最实际的：

1. **「快速fork做自己的Agent」**
   把仓库clone下来，改 `package.json` 把 Anthropic API key换成你自己的（或者直接支持OpenAI/Groq），`npm run dev` 就能本地跑。想换模型？改 `src/llm/claude.ts` 里的 `createClient` 就行，10分钟出个“本地版Claude Code”。
2. **「魔改Tool和Slash Command」**
   复制 `src/tools/` 里的模板，加你自己的Tool（比如连接公司内部Jira、自动部署到 Vercel）。我看到已经有老哥在群里说要加“微信发消息”Tool，哈哈哈。
3. **「学架构做开源替代品」**
   很多人已经在计划fork成完全开源的“OpenClaude-Code”，去掉所有Anthropic依赖，用 Llama3.1 或 DeepSeek 跑本地模型。TUI框架、上下文引擎、Tool Registry这些模块直接拿来就能用，省半年开发时间。
4. **「企业级定制」**
   大厂可以把整个Agent嵌入内部DevOps流水线：自动code review、生成PR描述、跑安全扫描。源码里权限控制写得巨完善，直接拿来就能合规。
5. **「学习价值拉满」**
   想提升前端TUI能力？研究Ink组件；想搞Agent框架？抄 `AgentOrchestrator`；想学安全？看 `security/` 那堆guard。甚至能拿来反向研究Anthropic的prompt工程（注释里藏着不少）。

当然，提醒一句：源码是公开了，但Anthropic的API还是要付费的，别干违法的事儿。玩归玩，尊重知识产权。

### 四、吐槽时间：Anthropic，你的安全脸呢？😂

* Anthropic：我们用Claude自动化了80%的内部开发！
  打包工程师（小声BB）：那source map也一起打包呗？Claude说调试方便👍
  Claude（在脚本里默默点赞）：嗯嗯，安全第一（狗头）
* 网友已经笑疯：OpenAI天天喊“Open”，结果模型权重死活不真open，天天玩半开半闭；Anthropic一不小心，直接把Claude Code彻底open了——这才是**「真·Open Claude」**啊！Sam Altman估计看完沉默三秒，然后默默把“Open”俩字从自己公司名上划掉😂
* 最绝的还是商标那事儿：前脚律师函把别人项目名字改了，后脚自己51万行代码全网公开课。这操作简直“家法只管别人，自己先裸奔”。安全团队集体破防：我们写了那么多反注入代码，结果最要命的bug是CI/CD没关sourceMap？？？
* Claude Code自己也太会“现身说法”了：天天教大家写安全代码、搞沙箱、审计调用，结果自己先在供应链上翻了超级大车。温柔语音：“连我们自己都会犯的低级错误，你们可别犯哦～”

当然，说归说，这事儿也提醒大家：**「再牛的AI Agent，也救不了人类在CI/CD里的手滑」**。Claude，你先把自己打包脚本优化一下行不行啊兄弟！

### 五、这事儿对行业到底意味着啥？

**「对我们开发者」**：纯福音！顶级Agent的实现思路直接摆在面前，少走一大堆弯路。下周估计就有人fork出更好用的开源版Claude Code替代品。

**「对Anthropic」**：有点小尴尬，不过影响不大。核心权重没泄，闭源逻辑还在，最多让对手多研究两天架构。

**「对整个Agent赛道」**：直接加速！大家现在都知道生产级Agent到底长啥样，卷王们新一轮军备竞赛要开始了。

### 最后

这次本质就是一场低级但高调的供应链事故，却意外给开源社区送了大礼。Anthropic的工程师们，辛苦了（手动狗头）。

你们已经冲GitHub去扒源码了吗？里面最让你惊艳的是哪一块？或者你打算怎么利用它？评论区一起聊聊啊～

**「点赞+在看」**，下次Anthropic再手滑咱们继续吃瓜！

（公众号：随心记事 | 欢迎关注不迷路）

——完——

（注：所有分析都基于公开镜像的公开代码，纯学习讨论，不涉及任何知识产权建议）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BfOib3dGxj5RDwaiaCtREjkDndTuJgxIsYnOthBr5RkKJiaEicUYHibRWxyTxrGUOpbuQ9DsqEX05xIr43YaXK1fvpQ/0?wx_fmt=png)

随心记事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BfOib3dGxj5RDwaiaCtREjkDndTuJgxIsYnOthBr5RkKJiaEicUYHibRWxyTxrGUOpbuQ9DsqEX05xIr43YaXK1fvpQ/0?wx_fmt=png)

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