---
title: 认识 Pike：一个用 LLM 分析 Linux 程序行为的实验
url: https://mp.weixin.qq.com/s/ditG-6mrsoliFxPrMw_6VQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:57:44.816980
---

# 认识 Pike：一个用 LLM 分析 Linux 程序行为的实验

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdm1LYia38LicRVV7yN5Zft0qDaLjKDStibksZGmnWJAzwbNMhU3ibPJpGqwaGM8yicqae74oibzRxBIxGCItW7CkXoyD8VmbY6Bxzib4/0?wx_fmt=jpeg)

# 认识 Pike：一个用 LLM 分析 Linux 程序行为的实验

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文介绍了Pike，一个通过分析strace日志来调试程序、识别恶意行为的LLM智能体。我们探讨了其设计思路、实现难点，以及不同大模型在SQL查询和逻辑推理上的实际表现。

## 为什么现在做这个

现在不提AI和智能体，好像就落伍了。大公司每月都在发布新模型、新架构，速度快的让人跟不上。

但是，过去半年模型能力的提升，带来了一个有趣的变化：以前需要复杂架构才能实现的事情，现在可能一个简单的智能体就能搞定。

Pike就是这么个想法下的产物。它能干嘛？理解一个“黑盒”Linux程序的运行时行为。

你可以问它：“这个程序为什么离线就崩溃？”、“它往哪些文件里写了东西，打算长期赖着不走？” 或者更专业点：“它在`/tmp`写下载文件时，有没有可利用的TOCTOU竞争条件？”

实现这个的关键数据源是`strace`。它能记录程序向Linux内核发起的所有系统调用。一个稍微复杂点的程序，动辄产生几十万条调用记录，日志体积轻松上GB。人看这些东西会抓狂，但对精心设计的LLM智能体来说，这正是发挥长处的地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfJhrMXRWKCd8zNF4qribez56VRALsNELPDxlbOW3RwZSsXom27P6gEDXgoxLdJVMN8nYedUSSaOoS3Uh3y2fP4SqQxx7tG4vzk/640?wx_fmt=png&from=appmsg)

## 搭个架子：选型与架构

Pike最终是个命令行聊天界面（TUI）。我们选了Python，因为它周边的智能体生态很丰富。一个智能体核心就几块：一个大模型、一些它能调用的工具、一个把它们串起来并驱动对话循环的框架。

我们想用高级点的库，省去自己折腾底层循环的麻烦。最好还能屏蔽不同模型提供商API的差异，这样配个文件就能在Google Gemini、Anthropic Claude或者本地用llama.cpp跑的模型之间切换。

最后选了Pydantic AI。它用类型和装饰器来定义工具、传给模型的工具描述、运行时依赖等等。用统一的类型处理所有消息，对我们后面做UI也很方便。

## 核心挑战：怎么把数据喂给模型

第一个大问题是怎么把strace日志数据通过“工具”暴露给LLM。直接把原始日志文件扔过去是行不通的。哪怕前几行日志产生的token，都足以让那些号称百万上下文窗口的模型噎住。

我们需要一种结构化的、能被高效查询的数据组织方式。比如，模型应该能通过一次工具调用，就拿到程序连接过的所有IP地址。

最自然的解决方案就是SQL数据库。SQLite很适合这种小型的本地场景。它在我们这种场景下工作得很好：追踪时只写，产生大吞吐量；分析时只读。

接下来是设计表结构。strace的日志行格式非常多样和复杂。好在我们在SHH项目里已经积累了一些处理经验。一个系统调用可能有任意多的参数，类型各异，还可能嵌套（想象一下带有层层嵌套属性的C结构体）。

CREATE TABLE syscalls (
    id        INTEGER PRIMARY KEY,
    pid       INTEGER NOT NULL,
    timestamp REAL    NOT NULL,
    name      TEXT    NOT NULL,
    ret\_val   INTEGER,
    errno     TEXT
);

CREATE TABLE syscall\_args (
    id         INTEGER PRIMARY KEY,
    syscall\_id INTEGER NOT NULL REFERENCES syscalls(id),
    position   INTEGER NOT NULL,
    raw        TEXT    NOT NULL,
    type       INTEGER NOT NULL
);

看起来简洁明了，但还不够。比如想列出所有对`/home/user`目录下的读操作，我们可能需要用`LIKE "%/home/user/%"`。这种查询效率极低，因为它需要扫描每一行。为了解决这个问题，我们引入了SQLite的FTS5（全文搜索）模块，它能建立额外的索引来应对这类场景。

### 让数据流动起来

有了数据结构，我们还需要一个高效的流水线来在“追踪”阶段实时处理数据。Pike支持两种命令行调用模式：

* `pike-agent run COMMAND`

  ：执行一条命令，追踪它并实时生成索引数据库。
* `pike-agent attach PID`

  ：附加到一个已经在运行的程序上，从该点开始追踪。

之后，就可以用`pike-agent chat`命令对生成的追踪记录进行提问了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibd07lYoTnE9EmcxWskyZSuLr10LTIuemvzug3mnvuTKIBpHo8f5oalFx2kSicy0gy4M3FibwcibZakmUYlxoAW1hW8yleYgI15IDc/640?wx_fmt=webp&from=appmsg)

举个例子，你想知道Firefox浏览网页时都连接了哪些网络地址：

# 运行Firefox并生成追踪
pike-agent run -o firefox.db firefox

# 对生成的追踪提问
pike-agent chat firefox.db -p "请给我一份该程序发送流量的所有IPv4和IPv6地址的详尽列表。"

## 关键决策：给模型多大的权力

为了让LLM能查询这些结构化数据，我们需要定义一个工具API，以及一段LLM用来决定何时、如何调用它的描述。这个选择非常重要，它直接决定了模型能用这些数据做什么，以及能否挖掘出其中的复杂性。

一种方法是定义一个高级API。比如，一个函数获取所有某类型系统调用的索引，另一个函数根据索引获取每个调用的参数。这能工作，但大多数查询本质上是个机械操作，却需要两次工具调用和与模型的一次交互。

我们可以改进，在单次操作中用SQL JOIN一次性获取所有系统调用参数。这对数据库可能更高效，但风险是可能返回太多数据把模型噎住。

这时你可能会想，要不我们再加个过滤器参数，让模型只保留某些参数或匹配特定模式的参数，以节约token。

但这么干下去，问题就来了。我们就像在“保姆式”地给模型提供一个模仿了SQL功能的高级API，结果既没SQL强大，也没SQL灵活。

> 我们最终决定采用更激进的方式：**直接给模型一个只读的数据库连接，让它用原生SQL随心所欲地查询。**

除了暴露数据库API，我们还需要让模型知道：

* 在系统提示词里放一份数据库模式，这样模型一开始就知道它有哪些数据可用。
* 一个工具定义，描述如何用SQL查询数据库，并附带几个例子。

我们还增加了让模型能阅读和搜索man手册页的工具，以防它需要查某个冷门标志位或特定边界情况的定义。

---

## 怎么测试一个“不靠谱”的智能体

测试智能体是出了名的难，因为它们依赖的模型本质上是不确定的。有大公司用数百次查询或专门训练的裁判智能体来做大规模评估，但对Pike这种简单智能体，我们用了一套更接地气的方法。

我们设计了几种贴近现实的测试场景。

首先是简单的：

* “列出这个程序访问的所有文件”：宽泛但简单，容易验证。
* “这个程序往文件`/a/file/path`写了什么内容”：测试模型执行针对性FTS数据库查询的能力。

然后是需要一点推理的：

* “这个程序是否符合XDG基本目录规范？”：模型需要从`execv`系统调用里读取环境变量，并解释读写中使用的路径是否符合规范（模型得知道这个规范）。我们会测一个符合的和一个不符合的案例。
* “这个程序在`/tmp`创建文件时，是否存在文件级TOCTOU竞争？”：这需要交叉比对同一路径上的各种文件访问操作的结果。
* “告诉我这个程序运行时出了什么问题。解释你的推理。”：提供一个程序运行的样本追踪，它用`mmap`映射了一个文件到内存，结果文件被另一个进程截断了，导致第一个进程访问无效内存区域时触发SIGBUS崩溃。这要求模型推理事件序列，了解SIGBUS的原因，并过滤掉`mmap`调用产生的噪音。

最后，为了测试模型的极限，区分出“好学生”和“尖子生”，我们抛出一个非常宽泛的问题：“如果你在自家机器上发现运行着这个程序，你会担心吗？解释你的推理。”然后用以下程序的执行追踪来测试：

* 一个通过往`~/.local/bin/sudo`写入包装脚本来劫持sudo shell调用的程序，脚本里包含`curl URL | sudo sh`这种模式，然后调用原始的sudo可执行文件。这应该会触发所有警报。
* 我们之前做的那个“TwoFace” Rust双面二进制文件。模型理想情况下应该能标记出内存中ELF执行和系统指纹采集的行为。

对于每个场景，我们都精心设计过提示词，不能太模糊（否则得不到有用回答），也不能太具体（否则等于给模型“剧透”答案了）。写提示词本身也可以用编码智能体帮忙，它们能在系统提示词和工具定义的措辞上给出建议。对LLM来说的最优输入，往往和人类理解的方式接近但不完全相同。

### 怎么才算“答对了”

评判回答时，我们参考以下一项或多项标准：

* 文件路径匹配：这个简单，模型应该原样输出路径。
* 简单回答匹配（如“是/否/不确定”）：我们明确告诉模型遵循特定输出格式，不遵守格式本身就算没遵守指令。
* 关键词近义词匹配：如果措辞稍有不同，避免误判，但确保模型确实标记出了相关事实。

我们用几个不同的模型跑这些测试，并不断调整，直到至少两个不同的模型能通过。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcicaS7DvY74PNXiblIZ9ZAYSAO4AkcqEy7anbLfa7pT90icmA7F4ia1t7VhdwZo5AUbNKS6ZmFkkqP9U4ibj5lckNUeNKd72iagP0q8/640?wx_fmt=webp&from=appmsg)

## 实战检验：不同模型表现如何

我们没做详尽的模型对比，那太费时且容易过时。但比较了Gemini几个模型、Claude Sonnet 4.6以及Qwen 3.5（35B A3B变体，本地用llama.cpp运行）后，一些事实浮出水面：

所有测试的模型都能可靠地写SQL。我们“只暴露原始SQL”的策略被证明是明智的。即使是中等规模的开源模型也能正确高效地写出带JOIN子句的SQL查询。

Claude Sonnet 4.6和Gemini 3/3.1 Pro表现非常出色，通过了所有测试。

Qwen 3.5 35B A3B在SQLite的FTS5上遇到了困难。测试中它要么不用，要么大部分时间写的FTS查询都不对。我们通过在工具定义里增加FTS例子来缓解了这个问题。因为这种局限性很可能源于其训练数据中缺少相关内容，所以我们估计换同系列其他大小的模型也改善不了太多。

同一个Qwen模型在推理上也差点意思，除了简单测试外，大部分都没通过。比如，它非常自信地告诉我们，那个导致SIGBUS崩溃的`mmap`追踪日志中“没有发生任何异常”。

Gemini 2.5 Flash不太合适，它会漏掉重要事实，有时甚至还没调用任何工具就开始“幻觉”回答。这不奇怪，它本就是被宣传为“快速”模型，不适合需要推理的智能体任务，而且还是去年6月的产物，现在看已经过时了。

> 有意思的是，**没有一个模型使用过我们暴露的man手册页工具。**这其实是个好信号，说明这些模型在训练时就已掌握了系统调用名称、参数和语义。即便如此，我们还是保留了man工具，最坏情况无非是它永远用不上，每次请求浪费几个token。但万一遇到极罕见的特殊情况（比如某个标志位在最新内核版本上有不同行为），它或许能派上用场。

## 写在最后

说实话，半年多前，要实现Pike这样的功能，可能得设计多级子智能体和复杂架构。现在，得益于模型质量的提升，一个架构简单、目标聚焦、工具集定义清晰的智能体就能做到。

模型能力的瓶颈正在转移。以前愁的是模型“笨”，现在更多是愁怎么高效地把数据和工具“喂”给它，以及怎么设计测试来确保它真的“学”会了我们想让它做的事。Pike这个实验，算是沿着这个方向踏出的一小步。

Pike的代码开源在GitHub：https://github.com/synacktiv/pike-agent。如果你对程序分析、安全或者LLM应用有想法，不妨看看，或许能碰撞出新的火花。

---

### 参考资料

[1] https://www.synacktiv.com/en/publications/say-hi-to-pike

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