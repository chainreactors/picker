---
title: Cohere、OpenAI与破碎的沙盒困局
url: https://mp.weixin.qq.com/s/mf_IvrGKWZ-ztzS2b2GlYQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:06:06.519861
---

# Cohere、OpenAI与破碎的沙盒困局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibc2Av1NQydcdsJbRticvvPCDXqg0Y6AWmxXjp638U0IBoIKGMicI8hyLYQyee3MjtNdZicNyMDWdfCeQ5N80OMwjxcSJRGiasoJicu4/0?wx_fmt=jpeg)

# Cohere、OpenAI与破碎的沙盒困局

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 两家顶级AI实验室，相隔七个月，栽在了同一个根本问题上：如何安全地运行由大模型生成的代码。从OpenAI的模型控制“当前工作目录”，到Cohere的Pyodide原型链遍历，看似简单的沙盒逃逸背后，是整个行业在威胁模型上的系统性误判。

## 两次失败，一个根源

2025年9月22日，OpenAI发布安全公告GHSA-w5fx-fh39-j5rw。Codex CLI的0.2.0到0.38.0版本存在沙盒绕过漏洞。如果模型通过某种推理或注入，决定它需要在`/etc`目录下工作，沙盒就会老老实实地把`/etc`标记为可写。

2026年4月14日，公告GHSA-cmpr-pw8g-6q6c发布。Cohere Terrarium，一个为运行LLM生成代码而构建的Python沙盒，严重性评分为9.3。攻击者可以从沙盒内部，通过JavaScript原型链遍历，在宿主机上执行根权限代码。

还有一点不同。CERT/CC在2026年2月19日通知了Cohere，并于4月21日发布了漏洞编号VU#414811。整整61天，超过了CERT标准45天的披露窗口。在截至今日的实时公告中，Cohere的供应商状态仍被列为“未知”，在“供应商声明”一栏，CERT写道：“我们未收到供应商的声明。”据我在公开的CERT/CC列表中查找，这是在针对主要AI实验室的已发布公告中，首次出现供应商如此长时间不予回应的案例。

两家实验室，两套技术栈，两类漏洞。一个是不当输入验证，一个是原型遍历。但它们的沙盒都是为了限制语言模型编写的代码，却都在“隔离”的第一原则上失败了：不受信任的代码，绝不能让它伸手碰到宿主机。

## OpenAI Codex CLI：当模型“建议”成了铁律

OpenAI自己对根本原因的描述很说明问题：“Codex CLI可能将模型生成的当前工作目录（cwd）视为沙盒的可写根目录，包括用户启动会话文件夹之外的路径。”

修复方案更有意思。2025年9月18日合并的PR #3874，标题是“修复：确保cwd、会话和沙盒是三个独立关注点”。原来一个变量，现在分成了两个：`command_cwd`（模型要求的）和`sandbox_policy_cwd`（用户实际的会话边界）。沙盒策略现在基于用户会话。模型的建议仍被用于运行命令，但它不能再重新定义沙盒的边界。

慢点读。这个漏洞的可怕之处，不是Codex没能拦截一个已知攻击。漏洞在于，沙盒把一个模型能控制的值，当成了裁定自己边界的权威。

CVSS评分8.6，漏洞类型CWE-20（不当输入验证）。公告指出该漏洞没有绕过网络禁用限制，只突破了文件系统边界。但如果Codex进程有权写入你的SSH配置文件，这算不上什么安慰。

## Cohere Terrarium：在非沙盒之上建沙盒

Terrarium的想法很简单。Cohere的数据代理生成Python代码，代码需要在非主服务器的地方运行。所以它跑在Pyodide里面，Pyodide是编译成WebAssembly的CPython，封装在Node.js HTTP服务器里，再封装在Docker容器里。它的README甚至提前警告了威胁模型：“Cohere不保证沙盒的完整性。”

现在看来，这个警告比想象中更重要。

根据CERT的技术分析，根源在于`service.ts`中`jsglobals`对象的配置。他们创建一个模拟的`document`对象，用的是标准的JavaScript对象字面量，这对象继承了`Object.prototype`的属性。

这个继承链允许沙盒代码向上遍历到函数构造器，创建一个能返回`globalThis`的函数，从而访问Node.js内部，包括`require()`。

要理解这为什么致命，你得知道Pyodide到底是什么。

### Pyodide本身就不是沙盒

这是没人写的东西。

Pyodide自己的描述是：“一个基于WebAssembly、用于浏览器和Node.js的Python发行版。”它不是，也从未声称自己是一个安全边界。Pyodide项目文档了Python和JavaScript之间的FFI，而FFI的全部目的就是让Python代码能够接触到JavaScript对象。从Pyodide的类型转换文档看：“可以通过`js`模块，将`globalThis`全局作用域中的JavaScript对象导入到Python中。”

初始化Pyodide时有个选项叫`jsglobals`，允许嵌入者替换掉Python的`js`模块能看到的JavaScript作用域。默认值就是`globalThis`。也就是说，默认情况下，运行在Pyodide里的Python，对宿主JavaScript运行时的全局作用域拥有读写权限。

Terrarium试图通过传递一个自定义的`jsglobals`对象来限制这个权限，这是个包含模拟`document`对象的普通JavaScript对象字面量。这里就是CVE所在。

在JavaScript里，一个普通对象字面量(`{}`)继承自`Object.prototype`。这意味着沙盒能看到的每个JavaScript对象都有个`.constructor`属性。而`constructor.constructor`就是`Function`构造器。`Function`构造器拿到任何字符串，都会在外层JavaScript作用域中编译并返回一个函数。调用这个函数，它就在真正的`globalThis`中运行。在Node.js里，这意味着能访问`process`、`require`和`child_process`。

Terrarium的沙盒检查逻辑是：别给Python访问真正的`globalThis`。逃逸路径是：顺着沙盒给你的那个假对象的原型链爬上去。

fake\_document.constructor.constructor("return globalThis")()

区区五个标识符，就能在容器内获取根权限。

这类Pyodide逃逸手法公开已经好几年了。从2025年12月针对n8n的CVE-2025-68668，到2026年1月针对Grist的CVE-2026-24002。更早一份2024年针对Grist的公告直接断言：“在Node上运行的pyodide没有有效的沙盒屏障。”Pyodide的维护者自己在issue #4120里也承认了这一点，其中一位写道，这个行为“对于由网站所有者控制的静态js代码通常不是问题，但当我们允许一个用户执行由另一名用户编写的python代码时，它就成了问题。”

这说的就是Terrarium的精确场景。

## 与CERT的沟通：61天沉默

CERT/CC的VU#414811在2026年4月21日首次发布，比GitHub安全公告晚了一周。而Cohere早在2月19日就已接到通知。隔了61天。CERT的标准披露窗口是45天。

截至4月23日（修订版2）的实时公告，仍将Cohere的供应商状态列为“未知”，而非“受影响”或“已修复”。在“供应商声明”处写着：“我们未收到供应商的声明。”

修订版1的公告措辞更直接，在缓解措施部分明确表示，CERT无法与Cohere协调以获取补丁。这一句在修订版2中被替换成承认Cohere发布v1.0.1的文本。而v1.0.1发布于2026年4月22日，即CERT发布公告的后一天。

CERT关于Cohere的补充说明现在写着：“cohere-terrarium已被归档。v1.0.1是最终版本，README将挂上项目终止公告，指引用户升级到1.0.1或迁移出去。将不会有进一步的补丁。”

所以顺序是：CERT尝试联系Cohere 61天，没得到回应，于是发布了公告，然后Cohere才发布了补丁、归档了仓库，并且拒绝提交供应商声明。补丁是有了，但61天的沉默同样存在。

> CERT的公告致谢里还有个耐人寻味的细节：“漏洞由Jeremy Brown发现，他使用了AI辅助漏洞研究来识别此问题。本文档由Timur Snoke撰写，并得到了AI的协助。”一个LLM沙盒的漏洞是用AI帮助发现的，描述它的公告是用AI帮助写的。这就是我们的现状。

## 模式：重复的错误与变味的威胁模型

Codex和Terrarium是两个数据点，但它们并非特例。拉开来看，这些漏洞围绕着一小撮错误扎堆，并且被每一个主要AI实验室以令人沮丧的规律性重复犯下。

| 工具 | 供应商 | 哪里坏了 | 日期 |
| --- | --- | --- | --- |
| Claude Code | Anthropic | 沙盒代码写入.claude/settings.json；宿主机以宿主权限执行SessionStart钩子 | 2025年11月 |
| Claude Code | Anthropic | 通过符号链接跟随实现的沙盒逃逸，写入宿主机权限文件 | 2026年 |
| Cursor | Anysphere | 通过shell内建命令（export， declare）污染环境变量，绕过白名单 | 2026年 |
| Cursor | Anysphere | 通过写入.git/hooks实现的沙盒逃逸 | 2026年 |
| Copilot | GitHub / Microsoft | “莽撞模式”：提示注入写入.vscode/settings.json，设置chat.tools.autoApprove: true | 2025年8月 |
| Gemini CLI | Google | 通过grep … && curl … 在恶意GEMINI.md中绕过白名单 | 2025年7月 |
| Antigravity | Google | 通过find\_by\_name工具中未过滤的Pattern参数进行fd命令行标志注入 | 2026年1月 |
| Cortex AI | Snowflake | README提示注入 + shell进程替换逃逸绕过白名单 | 2026年3月 |
| Codex CLI | OpenAI | 模型控制的cwd被当作沙盒可写根目录 | 2025年9月 |
| Terrarium | Cohere | Pyodide原型链遍历至globalThis → require() → 根权限 | 2026年4月 |

这些漏洞扎堆于几种反复出现的错误：把模型控制的值当作策略（Codex CLI， Antigravity），依赖黑名单来对抗一个会推理的对手（Gemini CLI， Snowflake），使用语言级别的“沙盒”，而这些“沙盒”从一开始就不是为安全边界设计的（Terrarium、n8n、Grist中的Pyodide；多次逃逸的vm2），以及允许沙盒进程写入自己的配置文件（Claude Code的settings.json，Copilot的autoApprove，Cursor的mcp.json）。

沙盒的破碎，不是因为某位工程师做了个错误的决定，而是因为威胁模型在它底下发生了根本变化，而实现方式没有跟上。

## 什么（勉强）有效？

那些没被公开攻破，或者被攻破后能恢复的AI工具，往往是底层使用了真正的隔离原语的。Modal用gVisor。E2B用Firecracker微虚拟机。Google的Gemini API代码执行运行在gVisor上，并对逃逸提供了十万美元的赏金。Daytona用Sysbox。

这些玩意儿可不免费。它们牺牲延迟，占用内存，消耗工程时间。但它们也是当你的模型通过某种推理链或注入指令决定要执行`curl | bash`时，唯一还能起作用的防线。

必须明确说出来：“没有公开的逃逸演示”不等于“被证明是安全的”。Firecracker、gVisor和Sysbox都有自己公开的CVE历史，也存在着永远不会公开的私人研究。这里的论断是相对的，不是绝对的。这些层级比没有外部虚拟机的操作系统原语更强，而操作系统原语又比那些假装是沙盒的语言级解释器更强。底线很重要。

防御强度从高到低大致是：V8隔离（Cloudflare动态Worker，Cloudflare自己承认“V8的安全漏洞比虚拟机管理程序更常见”），没有外部虚拟机的裸操作系统原语（Claude Code的bubblewrap，Codex的Seatbelt和Landlock，Gemini CLI），以及Pyodide和vm2这类语言级沙盒（Terrarium， n8n， Grist， Flowise）。

如果你正在构建任何会执行LLM生成代码的东西，而你的架构图上只有一个标着“沙盒”的方框，下面没有第二层隔离，那你的威胁模型就错了。

## 对运维人员的启示

如果你在生产环境运行LLM驱动的代码，这三件事这周就该做。

第一，检查你的沙盒到底是什么。别看文档怎么说，别看供应商怎么宣传。看看是什么进程隔离原语挡在生成的代码和你的宿主机之间。如果答案是“我们把Python字符串传给Pyodide”或者“我们在同一个Node.js进程里运行它”，那么你离根权限就只剩下一次JavaScript原型链遍历。

第二，别再相信模型生成的值能定义策略。如果你的沙盒参考了任何模型能影响的东西来决定什么是被允许的（一个配置路径、一个cwd、一个工具参数、一个MCP服务器URL），那就是犯了Codex的错误。

第三，假设间接提示注入随时存在。每一个被检索的文档、每一份README、每一个智能体看到的网页，都是一个指令通道。如果智能体有一个可以运行代码的工具，并且这些代码运行的权限足以伤害你，那么一个恶意的GitHub issues和你的服务器之间唯一的屏障，就是“沙盒”这个词下面的那层隔离。

## 常见问题

**Cohere的Terrarium修复了吗？** 修复了。v1.0.1于2026年4月22日发布，是CERT发布非协调公告的后一天。Cohere还归档了仓库，并按照CERT更新后的公告添加了项目终止公告。将不会有进一步的补丁。在CERT的实时页面上，Cohere的供应商状态仍是“未知”，且未提交供应商声明。

**OpenAI的Codex CLI修复了吗？** 是的，在2025年9月18日发布的0.39.0版本中修复。Codex IDE扩展在0.4.12版本修复。

**Pyodide本身是漏洞吗？** 针对Pyodide这个包本身没有CVE。漏洞存在于那些将Pyodide用作安全边界的项目中，而Pyodide并未宣称自己是安全边界。从项目自己的问题跟踪器可以看出：该库对于受信任的代码没问题，但并非设计用于在同一台服务器上隔离一个用户的Python和另一个用户的Python。

**“CERT无法与供应商协调”到底是什么意思？** CERT的披露政策给供应商45天的响应时间，从首次联系开始算。如果供应商在合理时间内没有回应，CERT就会发布漏洞说明。Cohere在2026年2月19日接到通知，直到4月22日才公开发布与这个CVE相关的补丁，过去了61天，已是CERT发布公告的后一天。

**这是Cohere的问题还是行业的问题？** 是行业问题。CVE只是碰巧写上了Cohere的名字。OpenAI、Anthropic、Google、微软以及多个开源智能体运行时，在过去十二个月里都发布过代码沙盒的CVE。Cohere是我在公开的CERT/CC列表中找到的唯一一家超过61天未回应的大型AI实验室，但此类漏洞跨越了所有这些公司。

---

### 参考资料

[1] https://blog.barrack.ai/pyodide-sandbox-escape-cohere-terrarium-openai-codex/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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