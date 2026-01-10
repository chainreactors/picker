---
title: IRify 报告功能：一键生成专业代码审计报告！
url: https://mp.weixin.qq.com/s/H0vW2aju9F4rPHXZVBh67Q
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:47.782657
---

# IRify 报告功能：一键生成专业代码审计报告！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBKTEGuOqIZSdqmNt0fdSdy1CmiccnDaYwPFES0WvGnuJo79gKNtplOhA/0?wx_fmt=jpeg)

# IRify 报告功能：一键生成专业代码审计报告！

原创

YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=4emnuw71&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcqcotRNtbcj6OdN50LB5LrV3wU9HUhF3jTBkeOsnQQnlzCelPcExiblPAZIygYNgibjVyNDtWgtjZA/640?wx_fmt=png&from=appmsg&randomid=1a529q6n&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBue8C2FRqb83xqJricLJpiaTYoThoo1nN8gzxqHT1UgSnHNGdPicRSkOnA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBuribS7LoIKZYk65rXPJtzjRzWKYfZg8qdPCB2YCRYZjssFiaaWiaOIRkA/640?wx_fmt=jpeg)

在 IRify 客户端的 Tab 列表选择数据库，点击报告，再点击生成报告按钮：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB0YMdIqorKm8e67FTPIR9AfY86UAUt3svurSum3mPriagAvXLjicDnWeA/640?wx_fmt=png&from=appmsg)

选择你需要生成报告的扫描任务，然后生成报告：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB8BtBppBSLoc1j7PIS9yGsNmezBT8qU1eAOIdeibLDrO1RiaicNmYl5Row/640?wx_fmt=png&from=appmsg)

报告生成后，即可在客户端内预览：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBCRibzuOI2lw7NAnJOmUEu7jZiaIUt6WVysdmYLjHc3vvo94A4zPffpng/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB6QQQCDq7zqOwLozBkapBrEDahS25a6CTxRiaiaGTUSkv6DKL6PvOdNhQ/640?wx_fmt=png&from=appmsg)

#### 智能图表优化

报告中的南丁格尔玫瑰图采用了智能数据优化算法。当漏洞数量分布极端不均匀时（例如高危漏洞 100 个，信息级漏洞仅 1 个），系统会自动调整图表比例，确保小数量的分类也能清晰可见，同时保留真实数据供查看。

#### 性能优化

为保证报告加载性能，系统对漏洞详情部分做了限制：

* 漏洞类型分组最多显示 100 个
* 代码片段最多显示 1000 字符
* 超出部分会有相应提示

#### 稳定排序

报告中的漏洞列表采用多级稳定排序策略：

1、首先按漏洞类型分组

2、同类型内按严重程度排序

3、同严重程度按漏洞名称排序

这确保了每次生成的报告内容顺序一致，便于对比和追踪。

## 通过 Risk 尝试生成利用 PoC

现在 Risk 页面查看想要生成 PoC 的 RiskID：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB0zXnVMInwGr753EfVhXO4kt1zWIgq8oJHV2xQRWiaic29KGrDrnJ5BUg/640?wx_fmt=png&from=appmsg)

进入 AI Agent 界面：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBHpB2icLMtVIWP5VzOJ8UVR6ICTdVQlUnUujFyvAHY9qCP35NKDfXM1w/640?wx_fmt=png&from=appmsg)

选择如图模板：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB1IAFdNU4mwm1TuWAmpYTzOV5MkR1GnnfneXQpSjuGicicR2t1ibsQxj7Q/640?wx_fmt=png&from=appmsg)

填入 RiskID 和保存路径运行：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBjo5ibzKdibicP7mHgMl1kCHjGWd56CIjhPssEyOrEcpKabRKWp2Yicmf0A/640?wx_fmt=png&from=appmsg)

生成结束后可以找到生成的报告：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBYOuyooPNOaQEJWL1p5lc6Rt6127n3g2V9ibkuQMtpzmtIMsPhkW5KMA/640?wx_fmt=png&from=appmsg)

同时，在右侧自由对话中可以在报告生成完毕后继续和 AI 对话。此时 AI 上下文中包含了这个 Risk 所关联文件和项目的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBdsKz8OIFe9jibsGw4plolA3fO6KoAfExYqsGBRHzVvmdgGI1sfdckTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpB56PqTzcUwQtwkBWPhjvd4ZZLWQnX8EoNI3p1vyax6eYGNSAIB8J9Xg/640?wx_fmt=png&from=appmsg)

#### ssapoc 工作流架构

ssapoc 是 Yaklang AI Forge 体系中的一个专用模板，专门用于从 SSA（Static Single Assignment）风险分析结果智能生成 Python PoC 代码。

其核心配置位于 common/aiforge/buildinforge/ssapoc/forge\_cfg.json：

```
{    "name": "ssapoc",    "verbose_name": "根据SSA Risk智能生成POC",    "description": "通过接收一个SSA RiskID，智能分析风险信息、评估POC生成可行性、获取适当模板，最终生成可执行的Python POC代码",    "tools": "poc_template_searcher,ssa-risk,ssa-project-info,ssa-list-files,ssa-read-file,ssa-grep,call_yak_plugin,write_file",    "actions": "ssa_poc_result,poc_generation_result,python_poc"}
```

该配置定义了三个关键要素：

1、工具集（Tools）：AI 可调用的能力边界，包括 SSA 风险查询、项目源码访问、PoC 模板搜索等

2、动作集（Actions）：AI 可执行的结构化操作，如进入 Python PoC 生成专注模式

3、提示词体系：由 init.txt、persistent.txt、plan.txt、result.txt 四个文件构成的多阶段提示词

#### 多阶段任务规划机制

ssapoc 采用预定义的任务规划策略，将 PoC 生成分解为九个有序子任务：

```
{  "@action": "plan",  "query": "-",  "main_task": "根据用户输入的SSA RiskID智能生成Python POC代码",  "main_task_goal": "通过分析SSA风险详情、评估POC生成可行性、获取适当模板，最终生成可执行的Python POC代码，用于验证和演示安全漏洞。",  "tasks": [    {      "subtask_name": "SSA风险信息获取与分析",      "subtask_goal": "使用ssa-risk工具根据用户提供的RiskID，查询和获取详细的SSA风险信息，包括漏洞类型、影响组件、漏洞描述、代码位置、数据流路径等关键信息，为后续POC生成提供基础数据。尤其需要注意获取`program_name`字段，`program_name`字段表示risk关联的程序意思是这个risk源自对这个程序的扫描 *不需要获取完整问题代码*"    },    {      "subtask_name": "检查项目源码可用性",      "subtask_goal": "使用ssa-project-info工具检查Risk关联的项目(通过上一步获取的`program_name`)是否有源码可访问。如果is_memory_mode为true或has_source_code为false，说明项目是内存模式编译的，源码不可访问，需要在后续步骤中仅依赖Risk中的CodeFragment信息。"    },    {      "subtask_name": "获取SSA风险信息关联项目源码上下文信息",      "subtask_goal": "使用ssa-risk工具根据用户提供的RiskID，获取Risk关联的风险代码上下文为后续POC生成中潜在的API路由信息（例如Java Spring风格的注解）或者POC生成所需信息做准备。重点关注代码上下文、API注解、函数签名等POC生成所需的技术细节。*需要获取完整问题代码*"    },    {      "subtask_name": "探索项目结构获取更多上下文（可选）",      "subtask_goal": "如果项目源码可访问(非内存模式)且需要更多上下文信息，使用ssa-list-files列出项目文件结构，使用ssa-grep搜索相关代码（如路由定义、配置文件、相关类等），使用ssa-read-file读取关键文件内容。这一步可以帮助理解完整的数据流和API结构。"    },    {      "subtask_name": "漏洞类型分类与攻击向量分析",      "subtask_goal": "基于可行性评估结果，对确认可以生成POC的风险进行详细分类，识别具体的漏洞类型（如SQL注入、XSS、RCE、反序列化、文件包含、SSRF等），分析漏洞的利用原理、攻击向量、所需参数和条件。结合SSA分析结果中的数据流路径，确定POC的实现思路和技术路线。这一步不要生成 Markdown 报告"    },    {      "subtask_name": "Python POC模板搜索与获取",      "subtask_goal": "使用poc_template_searcher工具根据识别的漏洞类型和攻击向量，搜索和获取相应的Python POC模板。模板包括请求构造、参数处理、响应解析、结果判断等通用代码结构，为POC生成提供代码框架参考。优先选择与目标编程语言和漏洞类型最匹配的模板。 - 不要主动输出文件， 最终的POC会嵌入到生成文档中"    },    {      "subtask_name": "目标API端点URL和参数信息分析",      "subtask_goal": "通过已有信息或是通过ssa相关工具你能获取项目的结构，读取漏洞所在位置的上下文代码目录结构等信息。你应该提取目标应用的关键信息，包括：1）API端点和路由信息（从注解如@RequestMapping、@GetMapping等提取），但对于某些简单的项目场景也可能是通过目录结构和文件位置直接访问，例如PHP项目没有实现路由框架的情况下直接请求对应php脚本文件即可；2）POC请求中的参数和数据类型；3）认证和授权机制，端点是否存在访问控制需要Cookie；4）框架类型（如Spring、JAX-RS等）。这些信息将用于生成更精确和可执行的POC代码。- 不要主动输出文件， 最终的POC会嵌入到生成文档中"    },    {      "subtask_name": "使用专注模式生成Python POC代码",      "subtask_goal": "根据前面收集的漏洞信息、API端点、攻击向量等信息，生成完整的Python POC代码。你需要输出 `{\"@action\": \"python_poc\", \"human_readable_thought\": \"根据漏洞分析结果生成Python POC代码\"}` 进入python_poc专注模式。在专注模式中使用write_python_poc创建POC文件，如有语法错误使用modify_python_poc修复。POC代码必须：1）语法正确，可以通过Python解释器验证；2）包含完整的漏洞检测和利用逻辑；3）使用规范的代码结构（类封装、异常处理、文档字符串）；4）包含使用说明和免责声明。"    },    {      "subtask_name": "根据已有信息输出包含Python POC的MarkDown报告",      "subtask_goal": "基于已有信息生成包含Python POC的MarkDown报告，报告必须包含前一步生成的Python POC代码。MarkDown报告应该以文件的形式被写入到用户指定的save_path中，你应该调用工具来写文件。报告内容包括：1）漏洞概述；2）影响范围；3）完整的Python POC代码（从专注模式生成的代码）；4）使用说明；5）修复建议；6）免责声明。当生成 MarkDown 文件内容时：不要对换行符进行转义，不要使用 `\\n` 形式，必须使用真实的多行文本，content 字段必须是原始 Markdown。报告使用简体中文，对于某些专业术语可以使用对应英文单词"    }  ]}
```

对应前端展示的任务树：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBNKtkBhdLUxy3kTMxyn6yY5qCbnsVyq63bhFPCRkyIe7lMGjcC3gOOg/640?wx_fmt=png&from=appmsg)

#### 【阶段一】信息收集

|  |  |  |
| --- | --- | --- |
| 子任务 | 目标 | 关键工具 |
| SSA风险信息获取 | 获取漏洞类型、代码位置、数据流路径 | ssa-risk |
| 项目源码可用性检查 | 判断源码访问方式（数据库/本地文件系统） | ssa-project-info |
| 源码上下文获取 | 提取 API 注解、函数签名等技术细节 | ssa-risk (get\_full\_code=true) |

#### 【阶段二】可行性评估系统根据风险类型自动判断是否适合生成 PoC

#### 适合生成 PoC 的漏洞类型包括：

* 注入类：SQL注入、命令注入、代码注入、LDAP注入
* 跨站攻击：XSS（反射型、存储型、DOM型）、CSRF
* 文件操作：文件包含（LFI/RFI）、路径遍历、任意文件读写
* 反序列化：Java/Python/PHP 反序列化漏洞
* 服务端请求伪造：SSRF、XXE

不适合生成 PoC 的风险类型（代码质量问题）：

* 资源未关闭、内存泄漏、死代码
* 弱密码、默认配置等合规性问题
* 性能问题、代码可维护性问题

#### 【阶段三】PoC 生成当可行性评估通过后，AI 进入 python\_poc 专注模式，启动 ReAct 循环进行代码生成。

####

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcQFdiaHLjvGSvHyGUe8wUpBAEwFNmgSvPwdIVYw585JLyWsVicM9Zn13997j9xsgX6XcxKqjKst5Kg/640?wx_fmt=png&from=appmsg)

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![图片](https://mmb...