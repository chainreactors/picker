---
title: Langfuse 使得 LLM 应用全链路可观测
url: https://blog.einverne.info/post/2025/08/langfuse.html
source: Verne in GitHub
date: 2025-08-15
fetch_date: 2025-10-07T00:12:41.600367
---

# Langfuse 使得 LLM 应用全链路可观测

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# Langfuse 使得 LLM 应用全链路可观测

Posted on 08/14/2025
, Last modified on 08/14/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-08-14-langfuse.md)

不知道大家在运用 LLM 的过程中有没有遇到过这样的问题，我需要不断的调试 Prompt，让 Prompt 给出符合自己满意的结果，并且在应用中使用 Prompt 的时候我需要进行成本的控制，并且持续的迭代优化，而目前大语言模型后台虽然能提供一个简单的支出统计，但用户交互过程中的信息都是捕捉不到的，比如用户的每次请求输出栓输出是否符合预期，不同版本之间的 Prompt 对结果的影响评估，以及用户请求的延迟等等。带着这些需求，我搜寻了一些方案，然后就发现了 Langfuse。

## Langfuse 是什么

Langfuse 是一款开源的 LLM 工程平台，通过全面的追踪（Tracing）与可视化，帮助开发者从请求端到模型端的每一步数据都留痕、可度量，从而实现快速调试、成本管控与持续优化
。

Langfuse 是专为大规模语言模型（LLM）应用设计的开源可观测与分析平台，能捕获模型交互过程中的所有上下文信息——输入、输出、工具调用、延迟及成本等。它支持多种模态（文本、图像、音频等）、多家模型服务商以及主流开发框架（如 LangChain、LlamaIndex 等），并提供 Python、JavaScript 等多种语言 SDK。

这么说可能比较抽象，那么我就举一些具体的例子，Langfuse 能做什么。

| 功能模块 | 主要能力 | 价值 |
| --- | --- | --- |
| 追踪管理 | 记录每次 LLM 请求的输入、输出、上下文与调用链，生成可视化的时序图 | 快速定位问题节点，洞察复杂流程 |
| 提示词版本管理 | 集中式管理与版本控制 Prompt，可在线编辑与灰度发布 | 缩短 Prompt 调优反馈循环，确保多版本演进可控 |
| 多模型支持 | 可以同时管理多个 LLM | 满足不同场景需求 |
| 评估（Evaluations） | 支持 LLM 自评、人工标注与自定义评估流水线，对模型输出质量打分 | 建立一致可复现的评价体系，持续提升应用效果 |
| 数据集与实验 | 构建测试集与基准，自动化运行 A/B 测试与对比分析 | 持续验证不同配置的效果，保障生产环境质量 |
| LLM Playground | 交互式 Playground，可实时调试 Prompt 与模型配置 | 在发现异常追踪后，直接跳转调试环境，加速问题修复 |
| 开放 API | 提供完整 REST / SDK 接口，可二次开发自定义工作流 | 融入既有 LLMOps 流水线，满足企业级定制需求 |
| 框架支持 | DeepSeek，LangChain，LlamaIndex 和 AWS Bedrock 等框架集成 | 非常轻松地接入 |

Langfuse 的核心技术优势

1. 开源＋自托管或云端二选一：可在分钟级完成自托管部署，也可使用官方托管服务，根据业务需求弹性选型。
2. 框架与语言无关：自 OpenAI、Anthropic 到开源模型均可接入；与 Python、TypeScript、JavaScript 等语言 SDK 无缝集成。
3. 多模态支持：不限于文本，对图像、音频等多种模态进行统一追踪与度量。
4. 成本与性能监控：自动统计 Token 用量、API 调用成本和延迟指标，实时洞察运营开销。
5. 透明化 Roadmap：公开开发计划与版本更新日志，社区活跃度高，生态不断完善。

典型应用场景

* 开发调试：在开发阶段，通过 Trace 定位生成环节中的异常或性能瓶颈，加速迭代。
* 质量评估：对比不同 Prompt、模型或配置方案效果，以数据驱动选择最优方案。
* 运营监控：实时监测生产环境调用趋势、错误率与成本消耗，及时发现与预警。
* 用户反馈闭环：收集用户标注或打分，将反馈融合进评估流水线，支持持续改进。

## 安装和使用

安装 SDK：

```
pip install langfuse openai
```

配置环境变量：

```
export LANGFUSE_SECRET_KEY="sk-lf-..."
export LANGFUSE_PUBLIC_KEY="pk-lf-..."
export LANGFUSE_HOST="https://cloud.langfuse.com"
```

在代码中添加追踪装饰器：

```
from langfuse import observe
from langfuse.openai import openai

@observe()
def ask_model(prompt: str):
   return openai.chat.completions.create(
       model="gpt-4o",
       messages=[{"role": "user", "content": prompt}],
   ).choices.message.content

@observe()
def main():
   return ask_model("什么是 Langfuse？")

main()
```

打开 Langfuse 仪表盘，即可查看每次请求的 Trace 树、生成记录与指标面板。

## 总结

Langfuse 以其全链路追踪、多模态支持与开放生态，正在成为 LLM 应用的必备 LLMOps 平台。无论是在新项目验证阶段还是大规模生产环境，Langfuse 都能帮助团队快速定位问题、优化成本与确保服务质量，为 AI 应用的持续演进提供坚实支撑。

## related

* [[LangSmith]]

## Related Posts

* [Langfuse 使得 LLM 应用全链路可观测](/post/2025/08/langfuse.html) - 08/14/2025
* [RAG 简介](/post/2025/03/rag.html) - 03/21/2025
* [LangChain 是什么](/post/2023/04/langchain.html) - 04/05/2023

---

* [← Previous（前一篇）](/post/2025/08/vibetunnel.html "VibeTunnel 将终端带到浏览器 开启移动化 Vibe Coding")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/08/claunch-claude-code-session-manager-under-cli.html "解决 Claude Code 上下文丢失问题: claunch 项目会话管理")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/08/langfuse.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [langfuse 1](/tags.html#langfuse)
* [llm 9](/tags.html#llm)
* [tracing 1](/tags.html#tracing)
* [langchain 2](/tags.html#langchain)
* [llamaindex 1](/tags.html#llamaindex)
* [llmops 1](/tags.html#llmops)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").