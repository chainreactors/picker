---
title: OpenViking：专为AI Agent打造的长期记忆数据库
url: https://mp.weixin.qq.com/s/4TPIxnyRLi0a-2tedhNo2A
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:44.629384
---

# OpenViking：专为AI Agent打造的长期记忆数据库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XHKUQGK0BNGtA4w5mnMqt70OnhUCUAt6x5qd3abKsFyNENwRTWyRtvrRttuwQy58UX8oDiaHJmMaSU2WAz6IrsmfYmbRMPyZmtkXkK6Dvu5A/0?wx_fmt=jpeg)

# OpenViking：专为AI Agent打造的长期记忆数据库

原创

凌木LSJ
凌木LSJ

AI技术LSJ

![]()

在小说阅读器中沉浸阅读

## 一、OpenViking是什么？

OpenViking是一个开源的**上下文数据库**，专为AI Agent设计。简单来说OpenViking是一个面向 AI Agent 的长期记忆框架，它让 AI 可以像人一样：

* 记住用户偏好
* 积累知识
* 总结历史对话
* 持续进化

OpenViking采用**虚拟文件系统**范式来统一管理Agent所需的三种核心上下文：

* 资源：知识和规则（文档、代码、常见问题解答）【长期、相对静态】
* 记忆：代理的认知（用户偏好、学习经验）【长期、动态更新】
* 技能：可调用功能（工具、MCP）【长期、静态】

所有上下文都以 `viking://` URI唯一标识，支持类似Unix文件系统的操作——`ls`、`read`、`find`，让Agent能通过确定性路径和语义搜索两种方式定位信息。

```
viking://├── resources/              # Resources: project docs, code repos, web pages│   └── my_project/├── user/                   # User: preferences, habits│   └── memories/└── agent/                  # Agent: skills, instructions, task memories    ├── skills/    └── memories/
```

## 二、OpenViking 的核心能力

### 1. 分层上下文按需加载（L0/L1/L2）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNHPdfXhELcoeyBNRk1iam84qMF5tDjbG2QvUKWhk4Uvo4I3rIjrXBZUl6Tniao8Yf78ZvjVbpjNzddLLTh9TfCkk8KAXJGlQxZe8/640?wx_fmt=png&from=appmsg)

### 2. 可视化检索轨迹

### OpenViking的每一次检索都会完整记录浏览了哪些目录、定位了哪些文件。开发者可以清楚看到Agent的“思考路径”，从而优化检索策略或调试问题。

![](https://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNFxHgjx4KOfsxkPOrPOVIIb5cjt3rwO5Casl78QeTy8nO5bHTxwhPIoltBrKebmArILVCp5ElEjVylNhgO63FTMncqdOlYQEiag/640?wx_fmt=png&from=appmsg)

### 3. 自动会话管理与记忆迭代

这是OpenViking最令人兴奋的特性之一。在每个会话结束时，调用`session.commit()`，系统会自动记忆提取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNEUmA5M8Yic8NYo6nWPH83SHfYgL8PB4Muh6EIuic4dPgxnDJ7Fb4XYHOrpa725YBZ4myCmnbegVJKlt4XWkqttOoUlUDjuEY0mc/640?wx_fmt=png&from=appmsg)

Agent因此能够“越用越聪明”，实现真正的自我进化。

## 三、RAG检索能力实测

传统 RAG / 向量库有几个典型问题：

- 1️⃣ 上下文是碎片 ：检索回来是“片段”，没有结构

- 2️⃣ Token 成本高 ： 塞满上下文窗口，截断丢信息

- 3️⃣ 检索不可解释 ： 为什么召回这段？

- 4️⃣ 没有长期记忆 ： Agent 每次从零开始

OpenViking如何解决？

通过文件系统范式统一管理智能体所需的上下文（内存、资源和技能） ，从而实现分层上下文交付和自我迭代。

本质：不是单纯向量数据库，而是\*\*“文件系统 + 向量检索”\*\*的混合架构

### 1）创建配置文件ov.conf

```
{    "embedding": {        "dense": {            "api_base": "",            "api_key": "",            "provider": "openai",            "dimension": 3072,            "model": "text-embedding-3-large"        }    },    "vlm": {        "api_base": "",        "api_key": "",        "provider": "openai",        "model": "gpt-4o-mini"    }}
```

```
export OPENVIKING_CONFIG_FILE=ov.conf
```

```
pip install openviking （Python 版本：3.9 或更高版本）
```

### 2）初始化数据库

```
import openviking as ovclient = ov.SyncOpenViking(path="./ovBase")  client.initialize()result = client.add_resource(    path="./data/修炼手册.pdf",    target="viking://resources/修炼手册.pdf",    wait=True,             timeout=30)client.wait_processed()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNGMACZEcAWtGdENKAe2UruQ6IBqMU8yyxmibTEZgHticuJ9N8jcINtLcztd8hA3XbClVvyDqnTgtrVyXe0hdrgIRKQulV5ickHk9o/640?wx_fmt=png&from=appmsg)

### 3）检索查阅

* find() – 语义检索
* search() – 会基于会话历史进行**意图分析**和**查询扩展**

![](https://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNFPfHPjiaicvdKPKKgk9Yt7g7xN0MZicexP4otvRs6ics1qt4GYhFHTRfgMlXHGVMrjV4U0ibKojuibfFT1iaMK9mbdfWCsyePJjickYUo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNGSflzycNvCXUCfwQgbSEZ021TXaBibUTcAnJP9kCBflDCjKfxGyDgicab9a6icfTsGfDckNyHE6M1GTS66Ig3uw5kL3QHicU8Ju6A/640?wx_fmt=png&from=appmsg)

## 四、与LangChain集成RAG检索实例

## 1）自定义检索器

```
from langchain_core.retrievers import BaseRetrieverfrom langchain_core.documents import Documentfrom typing import Any, List
class OpenVikingRetriever(BaseRetriever):    client: Any      def __init__(self, client: Any, **kwargs):        super().__init__(client=client, **kwargs)    def _get_relevant_documents(self, query: str) -> List[Document]:        results = self.client.find(query=query, limit=5, score_threshold=0.2)        docs = []        for ctx in results.resources:            content = self.client.read(ctx.uri)            docs.append(Document(                page_content=content,                metadata={"uri": ctx.uri, "score": ctx.score}            ))        return docs
```

### 2）RAG Chain

```
from langchain_openai import ChatOpenAIfrom langchain_classic.chains import RetrievalQA
retriever = OpenVikingRetriever(client)qa_chain = RetrievalQA.from_chain_type(    llm=llm,    retriever=retriever,    return_source_documents=True,    chain_type="stuff"  )
```

### 3）RAG查询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNHqu5iaGUds9NrukSFw2pNNc8iap7xmx23aUN52LxpZwr6tyqepkM3Micibw7icqP0cJgKyV70KyVkbjUibREF71pFX4lUFvZ9iarMCLY/640?wx_fmt=png&from=appmsg)

## 五、与LangChain Agent集成实战

### 1）集成为工具

```
@tooldef viking_find(query: str, limit: int = 5) -> str:    """    在知识库和用户记忆中语义搜索。可用于检索：    - 用户偏好（如书籍、食物、风格）    - 历史对话中提取的信息    - 项目文档或知识库内容    输入：简短的查询字符串，例如“用户偏好”、“书籍推荐”、“哲学”    返回：最匹配的条目 URI、相关性分数和摘要。    """    results = client.find(query, limit=limit)    output = []    for ctx in results.resources + results.memories:        output.append(            f"URI: {ctx.uri}\n"            f"Score: {ctx.score:.2f}\n"            f"摘要: {ctx.abstract[:200]}"        )    return "\n\n".join(output) if output else "没有找到相关内容"
@tooldef viking_read(uri: str) -> str:    """读取完整内容"""    return client.read(uri)
@tooldef viking_overview(uri: str) -> str:    """获取文档概览"""    return client.overview(uri)
@tooldef viking_ls(uri: str = "viking://") -> str:    """列出知识库目录"""    entries = client.ls(uri)    return "\n".join([e["name"] for e in entries])
```

### 2）创建智能体

```
agent = create_agent(    model=llm,    tools=tools,    system_prompt=prompt)
```

### 3）记忆能力测试

```
async def main():    # 第一轮    reply1, sid = await chat("我喜欢哲学和人工智能的书",session_id="user001")    print("AI:", reply1)    # 第二轮    reply2, _ = await chat("推荐几本书",session_id="user001")    print("AI:", reply2)await main()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNGQsfib3jbmpMdrLiaya3qkmxhuNic8iaWo0uEFB8oPcs1SkGvj12LH5aupPW6rQILGm8MrNH6mGwbl5WMhvyCcoPDfibIWUl13f6uM/640?wx_fmt=png&from=appmsg)

六、OpenViking数据库结构

最后，看一下ovBase本地基于虚拟文件系统的存储结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNECtjuwPmDichBeJvic5BLfTPlSWOVI4610QhQz2TplcKjpjMTBpmP3zGoJVuhMLtzu4giaKa1pYSRokWagPaLJ6Nf76HEHY8GvX4/640?wx_fmt=png&from=appmsg)

```
ovBase/  └── vectordb/                     └── viking/default/                      ├── agent/             # Agent 相关记忆（案例、模式）            ├── resources/         # 资源文件（文档、代码等）            ├── session/           # 会话归档历史            ├── temp/              # 临时文件            └── user/              # 用户相关数据                 └── default/      # 用户命名空间（默认）                      └── memories/        # 长期记忆目录                           ├── entities/   # 实体记忆（人物、项目等）                           ├── events/     # 事件记忆（决策、里程碑等）                           ├── preferences/# 用户偏好记忆（书籍、风格等）                           │    ├── .abstract.md   # L0 摘要                           │    ├── .overview.md   # L1 概览                           │    └── mem_*.md       # 具体记忆文件（L2）                           ├── .abstract.md        # memories 目录摘要                           └── .overview.md        # memories 目录概览
```

### 整个结构分为向量索引（vectordb）和知识空间（viking）。

### 其中 resources 用于存储知识库文档，session 保存对话历史并用于自动提取记忆，agent 存储 Agent 的经验与模式，而 user/memories 则用于记录用户的长期记忆（如实体、事件和偏好）。每条记忆采用 L0 摘要、L1 概览、L2 原文的三层结构，使 AI 能先读取摘要再逐步深入，从而降低 Token 成本并提升检索效率。

### 相比传统只存向量的 RAG 系统，这种结构既支持语义检索，又支持可读的知识组织和长期记忆积累，使 AI 能够持续学习用户信息和知识内容，是构建长期记忆型 AI Agent 的重要基础设施。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNHPd1F9v90aKgxLcUKK26W2ibae6BYQC0Nbzqn1JS9FRHSK78InKaIVM9QicB3D69xU8nmlUWAjAJNaNeibggBYIAePFkrqcADUn4/0?wx_fmt=png)

AI技术LSJ

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNHPd1F9v90aKgxLcUKK26W2ibae6BYQC0Nbzqn1JS9FRHSK78InKaIVM9QicB3D69xU8nmlUWAjAJNaNeibggBYIAePFkrqcADUn4/0?wx_fmt=png)

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