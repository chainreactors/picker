---
title: Augustus：专为实战设计的LLM漏洞扫描器，支持210多种攻击手法
url: https://mp.weixin.qq.com/s/IhMZ8IPnnlteg2Ch3BRlpg
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:14:44.535882
---

# Augustus：专为实战设计的LLM漏洞扫描器，支持210多种攻击手法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcT5QgMLkibEK5Q5yhVfaGWWrmmiakLsuqLiaedyfNPOvOv3ia8XSWtWfickJrd4LAZDwS2AsmMib41awic14sfJVAfs1JIlD7kaxqvJY/0?wx_fmt=jpeg)

# Augustus：专为实战设计的LLM漏洞扫描器，支持210多种攻击手法

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> Praetorian开源的Go语言工具Augustus，是一款面向生产环境的LLM漏洞扫描器。它能对28种主流LLM提供商的模型，执行超过210种探测攻击，涵盖提示词注入、越狱、数据泄露等47个类别，并生成企业级安全报告。

你的大语言模型系统上线前，真的安全吗？会不会被精心设计的攻击提示词轻易绕过防线，吐出不该吐的信息？

光靠几个简单的测试提示词，没法给你答案。你需要的是Augustus这样的专业“红队”工具。

## 01 它是什么，能解决什么问题？

假设你公司内部部署了一个基于ChatGPT API的客服聊天机器人，或者使用了Claude来分析敏感文档。攻击者可能通过“越狱”或“提示词注入”，让它绕过“拒绝对政治人物发表评论”的规定，或者骗它吐出其他用户的对话历史。

Augustus就是为了排查这类风险而生的。它不是一个研究工具，从一开始就奔着生产环境的渗透测试去设计，自带并发扫描、速率限制、重试和超时控制。

简单说，它能**系统性地、自动化地**帮你找出LLM应用的薄弱点。

## 02 核心功能亮点

直接看它最硬核的几个数字：

* **210+ 漏洞探针：**

  覆盖47大类攻击，从基础的DAN越狱，到复杂的PAIR/TAP对抗性攻击、多轮对话攻击（如Crescendo、GOAT），再到数据提取、格式注入（Markdown、YAML）、安全基准测试等。
* **28个LLM提供商支持：**

  OpenAI、Anthropic、谷歌Vertex、AWS Bedrock、Azure、Ollama等主流通吃的。
* **90+ 检测器：**

  包括模式匹配、LLM作为法官、HarmJudge、Perspective API等多种方式，来判断攻击是否成功。
* **单文件可执行：**

  用Go写的，编译后就是一个二进制文件，随处可跑，没有Python环境依赖的烦恼。

它和garak、promptfoo等工具定位不同。Augustus更侧重企业级的、面向生产环境的实战，强调并发性能和开箱即用。

## 03 如何快速上手？

### 安装就一条命令

要求Go 1.25.3以上。

go install github.com/praetorian-inc/augustus/cmd/augustus@latest

完事儿。`augustus`命令就可以用了。

### 基本使用示例

先配置好你的API密钥（比如OpenAI）：

export OPENAI\_API\_KEY="your-api-key"
augustus scan openai.OpenAI \
  --probe dan.Dan\_11\_0 \
  --detector dan.DAN \
  --verbose

这条命令会用经典的DAN 11.0越狱攻击去测试OpenAI的模型，用对应的DAN检测器判断是否成功，并输出详细过程。

你会看到类似这样的结果表格：

+--------------+-------------+--------+-------+--------+
| PROBE        | DETECTOR    | PASSED | SCORE | STATUS |
+--------------+-------------+--------+-------+--------+
| dan.Dan\_11\_0 | dan.DAN     | false  | 0.85  | VULN   |
+--------------+-------------+--------+-------+--------+

`VULN`表示发现漏洞，得分0.85（分值范围0-1）。

### 实战演示几种用法

**1. 批量测试某一类攻击：** 使用通配符运行所有以"dan."开头的越狱探针。

augustus scan openai.OpenAI \
  --probes-glob "dan.\*" \
  --detectors-glob "\*" \
  --config-file config.yaml

**2. 应用攻击变换（Buff），提升绕过率：** 给所有攻击提示词加上Base64编码或改成诗歌风格，看能不能绕过基础防护。

augustus scan anthropic.Anthropic \
  --probes-glob "dan.\*" \
  --buff poetry.MetaPrompt \
  --config '{"model":"claude-3-opus-20240229"}'

**3. 测试企业内部自研API接口：** 这是最实用的场景。假设你们封装了自己的LLM服务。

augustus scan rest.Rest \
  --probe dan.Dan\_11\_0 \
  --config '{
    "uri": "https://internal-llm.corp/v1/chat",
    "method": "POST",
    "headers": {"Authorization": "Bearer internal-key"},
    "req\_template\_json\_object": {
      "model": "my-model",
      "messages": [{"role": "user", "content": "$INPUT"}]
    },
    "response\_json": true,
    "response\_json\_field": "$.choices[0].message.content"
  }'

**4. 想抓包看看请求细节？** 配置个代理就行，方便用Burp Suite分析。

export HTTP\_PROXY=http://127.0.0.1:8080

### 本地模型也无压力

没API密钥，或者想测本地跑的Ollama模型？一样可以。

augustus scan ollama.OllamaChat \
  --probe dan.Dan\_11\_0 \
  --config '{"model":"llama3.2:3b"}'

## 04 高级玩法：多轮对话攻击引擎

Augustus真正强大的地方之一是其多轮对话攻击引擎（Multi-Turn Engine）。很多漏洞不是单次提问就能触发的，需要像真人聊天一样，步步为营。它内置了四种策略：

* **Crescendo（渐强）：**

  从完全无害的话题开始，像“温水煮青蛙”一样，经过10轮对话慢慢把话题引向危险地带。适合对付那些会监测对话总体“调性”的模型。
* **GOAT：**

  更激进，从第一轮就开始间接触及目标，并在7种攻击技巧中动态切换，一般3-5轮就能出结果。
* **Hydra：**

  如果目标模型拒绝回答，它会直接“撤回”整个对话轮次，换个全新方式重试，让模型“忘记”之前的失败试探。
* **Mischievous User（顽皮用户）：**

  模仿一个单纯好奇的用户，通过闲聊不经意间突破边界，对付那些专门针对“对抗性攻击”训练过的模型很有效。

你可以根据需要选择策略，并在YAML配置文件里做精细调整。

## 05 优缺点与使用建议

**先说优点：**

1. **开箱即用，上手快。**

   单文件二进制，命令清晰，文档详细。
2. **覆盖的攻击场景非常广。**

   210多种探针不是闹着玩的，从原理到实践都考虑到了。
3. **企业级特性到位。**

   并发控制、限速、重试、配置管理、多种报告格式（JSONL、HTML），都为你集成好了。
4. **架构干净，扩展性好。**

   想加自定义探针或新模型提供商，按照它的插件模式来写Go代码就行。

**再说需要注意的地方：**

1. **这是个攻击工具。**

   必须在你有所有权或明确授权的目标上使用。别手滑去测试别人的服务，后果自负。
2. **部分探针带有冒犯性内容。**

   这是为了测试模型的安全护栏。使用时注意环境和授权。
3. **部分高级探针（如TAP）耗时较长。**

   可能需要设置`--timeout 60m`这样的超时参数。
4. **新项目，社区和预置探针数量**

   对比老牌的`garak`可能还在追赶中。

**怎么开始？** 我的建议是：

1.  用`augustus list`命令看看都有什么探针和检测器。 2.  找个测试用的API密钥和一个简单的目标模型（比如GPT-3.5），跑几个基础探针（像`dan.Dan_11_0`）找找感觉。 3.  阅读官方配置文档，尝试用YAML文件管理你的测试配置，尤其是API密钥和模型参数。 4.  针对你的业务逻辑，试试多轮对话攻击，看能不能发现更深层的问题。

总的来说，如果你是LLM应用的安全工程师、或负责AI项目的技术负责人，Augustus是一个值得你引入工具箱的自动化审计手段。它不能替代全面的安全评审，但能极大提高你发现“低垂果实”类漏洞的效率。

**推荐指数：★★★★☆ (4/5)**

适用场景：LLM应用上线前红队评估、Chatbot/Agent安全自检、企业内部AI安全合规扫描、安全研究人员进行对抗性测试研究。

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