---
title: 探索 AI 驱动的代码安全工具 VulnHuntr
url: https://mp.weixin.qq.com/s?__biz=MzAxNTg0ODU4OQ==&mid=2650358583&idx=1&sn=825ce4fe98145a5b6744dd6a1e3a86b5&chksm=83f026d5b487afc3e724f8feb6fb79e4bcf5ed1bd4919d4d96f55c9ee46cf1db7761251d085d&scene=58&subscene=0#rd
source: 安全引擎
date: 2024-12-15
fetch_date: 2025-10-06T19:37:59.732008
---

# 探索 AI 驱动的代码安全工具 VulnHuntr

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yjc5YCCspxVicf6icYPumXjbia1YfRXto46bgNb5wJ1cykvbtic5aoXDiaO9js1bdOhcxQdDM5cbCCXPOA0awNzIxJA/0?wx_fmt=jpeg)

# 探索 AI 驱动的代码安全工具 VulnHuntr

原创

KINGX

安全引擎

10月份，Project AI 开源了 VulnHuntr 项目，这是一款由大模型驱动的 Python 静态代码安全分析工具，并成功发现了多个 AI 相关应用系统中的安全漏洞。

前段时间本地实测了一下，整体上说这是一个偏向于 Demo 性质的项目，但是主体功能已经比较完整。VulnHuntr 实现了多个步骤的代码分析，并且对于不同类型漏洞，设置了针对性的 Prompt。通过符号查找，允许大模型主动请求上下文函数或类的代码，并结合上下文进行更深入的代码分析。扫描过程中会进行多轮迭代，来分析复杂的代码逻辑，提升结果准确度。内置 Prompt 中的代码分析指令也非常具有学习参考意义。

不过在实际使用过程中也遇到了不少问题。例如：VulnHuntr 工具与大模型交互使用了较为复杂的 JSON 数据格式，并且校验严格，使用 OpenAI、Anthropic 之外的其他模型实测体验并不好，非常容易输出不符合规范的 JSON 数据，导致程序异常退出。另外大模型输出存在一定随机性，不可避免的会出现不少误报和漏报，且每次输出的结果也可能会有差异，有时候还会出现结果中多个字段逻辑不相符的问题。整体使用下来，使用 Claude 模型时的运行效果是最好的，大家可以自行体验。

为了提高易用性、更多大模型的兼容性，我抽空在 VulnHuntr 基础上做了一些小小的优化：

* 优化大模型交互格式，大幅提升大模型输出的兼容性
* 支持更多国内大模型，例如 Qwen、Hunyuan
* 增加了多语言 Prompt 选项，增加了中文 Prompt
* 增加了简单的报告功能，以及更多的命令行选项
* 优化控制台日志信息

修改版的报告和运行截图：

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxVicf6icYPumXjbia1YfRXto46OpcXDUBW0B2R67UCib1jZ0u7GVtI5ibOUAE5TLiblg5Yd7PyZ51GtOccQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxVicf6icYPumXjbia1YfRXto46ZibJgibb3iagibLNVLzZ57ia6JS3lhgPR7KEa1T4IFLEuia6GeB1RLBfrk9g/640?wx_fmt=png&from=appmsg)

修改版项目代码，可以在此公众号后台留言 “vulnhuntr” 获取下载地址。

## 开始使用

原版项目下载之后，需要做一些修改和设置才能正常使用：

```
# 必须使用 Python 3.10，兼容 jedi
conda create --name vulnhuntr python=3.10

# 修复 requirements.txt
echo " \\ \n    --hash=sha256:f5971a9226b701070a4bf2c38c89e5a3f0d64de8debda981d1db98583009122a" >> requirements.txt

# 安装依赖
python -m pip install -r requirements.txt

# 将主函数代码拷贝出来方便运行
cp vulnhuntr/__main__.py ./run.py

# 根据需要设置 Ollama 模型
export OLLAMA_MODEL=qwen2.5:32b
export OLLAMA_MODEL=llama3.1:8b

# 启动扫描，建议使用 claude
python run.py -r path/to/target -l ollama
python run.py -r path/to/target -l claude

# 修改版的启动命令
python run.py -r ../../targets/dvpwa -l gpt -m gpt-4o -vv -k your-api-key
```

## 代码简读

```
__main__.py   主逻辑
LLMs.py    大模型接入类
prompts.py   各种Prompt模板
symbol_finder.py 代码符号查找工具类
```

1. 预处理，筛选出核心代码文件

排除代码仓库中的测试、示例、文档等非核心文件，然后使用大量正则表达式识别出可能包含网络相关功能的代码，例如 Python Web 框架、WebSocket、服务器启动代码等。

2. 代码项目整体解读，进入通用代码分析阶段

找到项目的  Readme 文件进行总结，并将总结结果合并作为 System Prompt 的内容。Prompt中将大模型定设定为“Python静态代码安全审计专家”的角色，并多次强调可以主动请求更多的上下文代码。接下来遍历预处理筛选出来的重点代码文件，进行第一轮通用代码分析。

第一轮分析的 Prompt 中包括代码内容、通用分析指令、分析方法、输出规范、输出格式Schema等等。重点在于尽可能的找出所有潜在风险点，并且给大模型阐明了具体的分析方法和原则。例如：先整体Review、再关注远程可利用的漏洞、分析用户输入的数据流处理存储以及输出的逻辑、分析安全控制措施，并提醒大模型关注上下文。输出规范的 Prompt 中对 JSON 格式提出了细节规范的要求。

3. 针对性漏洞检测阶段，多轮精确扫描

对通用扫描中发现漏洞并且置信度大于0的漏洞类型，逐个进行针对性的漏洞扫描。与通用代码分析阶段相比，此阶段附上了大模型所请求的上下文代码，指令 Prompt 更新为特定漏洞类型的 Prompt、并且增加了特定漏洞类型的 Bypass Payload，例如 XSS 的代码审计 Prompt、SQLi 的代码审计 Prompt，指令更具针对性。

根据大模型对上下文的请求情况，此阶段最多迭代7次。此阶段的第一轮不会立即获取上下文代码，而是等到迭代的第二轮才会处理 context\_code 请求。如果大模型重复请求同一个上下文超过 1 次，则跳出迭代。

大模型请求上下文包括 name（函数名、类名、方法名），code\_line（引用的代码行），reason（原因）。VulnHuntr 使用 jedi 库进行代码符号查找，找到相应的 code\_line，然后再定位到相应源代码位置，最后给大模型反馈的内容如下：

```
<context_code>
 <code>
  <name></name>
  <context_name_requested></context_name_requested>
  <file_path></file_path>
  <source></source>
 </code>
</context_code>
```

如果引用的类/函数在第三方代码中，则返回一句话 “Third party library. Claude, use what you already know about {name.full\_name} to understand the code” 作为源代码内容。

4. 结果输出

修改版中将多轮检测迭代完成之后依然存在的漏洞结果输出到报告文件中。

## 结语

尽管仍有很大改进空间，VulnHuntr 还是一个值得学习借鉴的开源项目，在 LLM 代码安全分析方面的应用思路值得关注。感兴趣的朋友，欢迎关注、留言、转发。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWk63WInibYqv5eurbOzDXK95PFxEYlPRSJHYG7l2vt2FoRI9f34TWe6T2vmKBYKp61KuFBmmxwezw/0?wx_fmt=png)

安全引擎

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWk63WInibYqv5eurbOzDXK95PFxEYlPRSJHYG7l2vt2FoRI9f34TWe6T2vmKBYKp61KuFBmmxwezw/0?wx_fmt=png)

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