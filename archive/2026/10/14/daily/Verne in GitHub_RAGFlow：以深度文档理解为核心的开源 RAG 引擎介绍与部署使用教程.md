---
title: RAGFlow：以深度文档理解为核心的开源 RAG 引擎介绍与部署使用教程
url: https://blog.einverne.info/post/2026/10/ragflow-open-source-rag-engine.html
source: Verne in GitHub
date: 2026-10-14
fetch_date: 2026-10-15T06:41:58.419081
---

# RAGFlow：以深度文档理解为核心的开源 RAG 引擎介绍与部署使用教程

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

# RAGFlow：以深度文档理解为核心的开源 RAG 引擎介绍与部署使用教程 PDF 里的表格、扫描件和多栏排版，终于有一个开源 RAG 方案认真对待了

Posted on 10/14/2026
, Last modified on 10/14/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-10-14-ragflow-open-source-rag-engine.md)

这两年我陆陆续续接触过一些 RAG 小工具，从最早自己用 [[LangChain]] 拼一个 demo，到后来用 [[AnythingLLM]]、[[Dify]] 的知识库功能，有一个体验几乎每次都会重演：拿几篇 Markdown 测试的时候效果惊艳，一旦换成真实的业务材料，比如一份带合并单元格的财报 PDF、一份双栏排版的论文、几页扫描的合同，回答马上就开始胡说八道。追查下去会发现问题根本不在大模型，而在最前面的解析和切块环节，表格被拍平成一串没有表头的数字，左右两栏的文字被交错拼接在一起，模型拿到的上下文本身就是错的。也正是因为这个痛点，我在调查 [ESP32](https://esp32.einverne.info) 小智 AI [后端](https://esp32.einverne.info/projects/xiaozhi#%E8%87%AA%E5%BB%BA%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8E%E7%A4%BE%E5%8C%BA%E5%AE%9E%E7%8E%B0)的时候发现了 [[RAGFlow]]，一个可以「深度文档理解」的开源 RAG 引擎。

![RAGFlow 开源 RAG 引擎](https://pic.einverne.info/images/2026-10-14-13-45-01-ragflow-rag-engine.png)

## RAGFlow 是什么

[RAGFlow](https://ragflow.io/) 是 InfiniFlow 开源的检索增强生成（[[RAG]]，Retrieval-Augmented Generation）引擎，采用 Apache-2.0 协议，是开源 RAG 领域最活跃的项目之一。官方现在给自己的定位是「融合 RAG 与 Agent 能力、为大模型提供上下文层（context layer）的引擎」，翻译成大白话就是：负责把真实文档整理成大模型能可靠使用的知识，并在此之上提供问答、检索 API 和 Agent 编排。

和很多「上传文档加聊天框」的工具不同，RAGFlow 的口号是 “Quality in, quality out”。它认为 RAG 效果的上限在解析阶段就已经决定了，所以把大量工程投入放在了别人不太愿意做的脏活上：用视觉模型识别文档版面，分辨哪里是标题、正文、表格、图片和页眉页脚，再根据文档类型选择合适的切块方式。这也决定了 RAGFlow 不是一个 Python 库，而是一整套需要用 [[Docker]] 部署的服务栈，这一点是它和 LangChain、[[LlamaIndex]] 这类开发框架最本质的区别。

## 为什么值得关注

开源 RAG 生态现在的选择其实很多，我习惯把它们分成三类。第一类是开箱即用的应用，比如 RAGFlow、AnythingLLM、[[FastGPT]]，部署好就能用；第二类是 AI 应用搭建平台，比如 Dify、[[Coze]]、[[n8n]]，知识库只是其中一个节点；第三类是开发者框架，比如 LangChain、LlamaIndex、Haystack，需要自己写代码组装。RAGFlow 属于第一类，但它在解析质量上和同类拉开了明显的差距。

| 项目 | 定位 | 文档解析能力 | 部署形态 | 协议 |
| --- | --- | --- | --- | --- |
| RAGFlow | 开箱即用的 RAG 引擎 | 版面感知，最强 | Docker 多容器 | Apache-2.0 |
| AnythingLLM | 无代码文档问答 | 一般 | 桌面端 / Docker | MIT |
| Dify | LLM 应用平台 | 中等 | Docker | Apache-2.0 附加条款 |
| FastGPT | 知识库加工作流 | 中等 | Docker | Apache-2.0 附加条款 |
| LlamaIndex | 数据索引框架 | 较强，依赖 loader | Python 库 | MIT |

如果瓶颈在解析质量，文档里全是表格、扫描件、多栏排版和严格的条款结构，RAGFlow 基本是开源方案里的第一选择；如果 RAG 只是一个更大业务流程里的一环，需要审批、分支和对接一堆外部系统，Dify 的工作流和插件生态更成熟；如果只是几个人想和几百份结构简单的 PDF 聊聊天，AnythingLLM 的桌面端更轻，没必要维护一套多容器的服务；如果需要在代码层面完全掌控检索策略，那还是 LlamaIndex 配合 [[Qdrant]] 或 [[Milvus]] 自己搭更合适。另外值得一提的是 RAGFlow 采用的是纯粹的 Apache-2.0 协议，没有多租户或者去除 Logo 之类的附加限制，商业使用相对干净，这也是不少公司内部选型时会考虑的因素。

## 核心特性

### 深度文档理解

RAGFlow 内置的 DeepDoc 模块负责版面分析、OCR 和表格结构识别，支持 PDF、Word、PPT、Excel、TXT、图片、扫描件、网页和 EPUB 等格式。它会识别出页面上每个区域的类型，再把表格还原成带表头的结构化内容，而不是简单地按行抽取文字。除了 DeepDoc，RAGFlow 还可以选择接入 [[MinerU]]、Docling、MonkeyOCR、PaddleOCR-VL 等外部解析器，PDF 和 DOCX 中嵌入的图片也可以交给多模态模型去理解。实际体验下来，对于财报、技术规范、学术论文这类文档，它的解析结果明显比按页抽文本的方案靠谱得多。

### 模板化切片与可视化干预

RAGFlow 没有提供 chunk size 、overlap 等切块参数，而是根据文档类型给出十几种切片模板，比如 General、Q&A、Resume、Manual、Table、Paper、Book、Laws、Presentation、One 等。Laws 模板会以法条为单位切分，保证每一条完整；Presentation 模板让 PPT 每一页成为一个独立的块；Q&A 模板直接使用问答对格式的 Excel；One 模板则把整篇文档作为一个块，适合需要全文语境的场景。

我认为比模板更有价值的是切块结果的可视化。解析完成后可以在 Web 界面上逐块查看每个 chunk 的内容，直接编辑、禁用或者添加关键词。做过 RAG 的人都知道，回答不好的时候最难的是定位问题出在哪一步，大多数工具只能盲猜调参，而 RAGFlow 让你直接「看到」模型拿到的上下文长什么样，这一点在调优阶段帮了我很大的忙。

### 引用溯源与混合检索

RAGFlow 的回答默认带有引用标记，点击可以回溯到具体的 chunk 以及原始文档里的位置，最近的版本连 Excel 的引用来源都能在预览中定位到单元格附近。这对法务、金融这种需要审计答案来源的场景非常重要，也是降低幻觉最实用的手段。检索阶段同时使用向量相似度和全文关键词检索，再经过 rerank 模型做融合重排，相似度阈值、关键词权重、Top N 都可以调整，界面上还有专门的检索测试面板，可以输入问题直接看召回了哪些块、分数是多少。

### 知识编译与 Agentic RAG

2026 年 8 月 RAGFlow 引入了一个我觉得很有意思的功能，叫做知识编译（Knowledge Compilation）。它可以在单个文档或整个数据集的层面，用大模型把原始内容「编译」成结构化的知识产物，包括 Wiki、知识图谱、树状结构、PageIndex、思维导图、时间线和 Skills。这其实是对传统 RAG 只做「碎片检索」的补充，之前的 GraphRAG 和 RAPTOR 层级摘要也可以看作这个思路的前身，现在被统一到了一个框架下，产物还可以查看、更新和重新生成。

同一时期上线的还有 Agentic RAG，也就是多步检索。面对复杂问题，模型会先分析问题，必要时拆成多个子问题分别检索，再汇总回答，并提供 Low、Medium、High、Ultra 四档思考强度。档位越高效果越好，但 token 消耗和延迟也会成倍上升，日常问答我一般用 Low 或 Medium 就够了。

### Agent 编排与数据源

RAGFlow 提供了可视化的 Agent 画布和一批预置模板，支持条件分支、代码执行、网页浏览、联网搜索、Agent Memory 和 [[MCP]] 等组件。数据源方面可以从 Confluence、[[Notion]]、Google Drive、S3、WebDAV、Azure DevOps、Google BigQuery 等地方同步，并支持增量更新，9 月的版本还新增了基于 sitemap.xml 抓取整站内容的能力，拿来给自己的文档站或者博客做一个问答助手非常方便。做好的助手可以部署到飞书、Discord、Telegram、Line 等渠道，可观测性上则接入了 [[Langfuse]]。

## 技术架构与 Go 重写版本

在 0.x 时代，RAGFlow 的后端是 Python 写的，主要分为提供 API 和 Web 服务的 `ragflow_server.py`，以及负责解析、向量化、图谱构建的 `task_executor.py`。依赖的中间件包括 [[Elasticsearch]] 或 InfiniFlow 自研的 Infinity 作为文档引擎、[[MinIO]] 作为对象存储、[[MySQL]] 保存元数据，以及 [[Redis]] 作为缓存和任务队列。这套组合功能完整但相当吃资源，也是很多人望而却步的原因。

2026 年 9 月 29 日发布的 v1.0.0-rc1，整个后端用 Go 全面重写，官方说法是大幅降低系统资源消耗，把原先的重量级部署模型换成轻量架构。几个关键变化值得注意：消息队列从 Redis 换成了 [[NATS]]，缓存和检查点改由 [[Kvrocks]] 承担；服务拆分成 Admin、Syncer、Ingestor、API 等几个角色，可以用同一个二进制以不同参数启动；命令行工具 RAGFlow CLI 也用 Go 重新实现；文档引擎除了 Elasticsearch 和 Infinity，还可以选 OpenSearch、OceanBase 等。对 API 用户来说，已经标记为废弃的旧 API 别名在 Go 版本里不再支持，但 Python SDK 不受影响。

无论是 0.x 还是 1.0，RAGFlow 都不内置大模型和 embedding 服务，而是通过配置对接外部推理服务，包括 OpenAI、[[DeepSeek]]、Gemini、AWS Bedrock 等云端 API，以及 [[Ollama]]、Xinference 等本地推理框架。这意味着只要本地推理跟得上，完全可以做到全离线、数据不出内网的私有化部署。

## 部署 RAGFlow

官方推荐的配置是 4 核 CPU、16 GB 内存、50 GB 可用磁盘，Docker 版本不低于 24.0.0，Docker Compose 不低于 v2.26.1。需要提醒的是，官方镜像目前只面向 x86 Linux，README 里明确写了 macOS 暂不支持，ARM64 需要自行构建镜像，想在 Mac 上直接试玩的话最好找一台 [Linux 服务器](https://client.einverne.info) 或者虚拟机。

如果使用默认的 Elasticsearch 作为文档引擎，首先要检查内核参数 `vm.max_map_count`，否则 ES 容器会启动失败：

```
sysctl vm.max_map_count
# 小于 262144 时临时调整
sudo sysctl -w vm.max_map_count=262144
# 永久生效需要写入 /etc/sysctl.conf
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

然后克隆仓库并切换到想要的版本标签。这里我的建议是，生产环境先用 v0.27.2 稳定版，想体验 Go 重写版本的话在单独的测试机上跑 v1.0.0-rc1：

```
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/docker
git checkout v0.27.2   # 或 v1.0.0-rc1
docker compose -f docker-compose.yml up -d
```

一定要先 `git checkout` 到和镜像匹配的标签再启动，否则 `docker` 目录下的 compose 文件和 entrypoint 脚本可能与镜像版本不一致，出现一些莫名其妙的问题。首次启动需要拉取镜像和初始化数据库，时间会比较长。1.0 版本提供了一个健康检查接口，返回 200 就说明服务就绪了：

```
curl -f http://localhost/api/v1/system/healthz
# 启动失败时查看日志
docker logs --tail 50 ragflow-cpu
```

默认情况下 Web 界面监听 80 端口，浏览器直接访问服务器 IP 即可，API 服务则在 9380 端口。如果太早打开页面可能会看到 network abnormal 之类的提示，等容器全部就绪即可。需要修改端口、密码、文档引擎或者是否启用 GPU 时，编辑 `docker/.env` 中的 `SVR_HTTP_PORT`、`MYSQL_PASSWORD`、`ELASTIC_PASSWORD`、`DOC_ENGINE`、`DEVICE` 等变量，改完之后执行 `docker compose up -d` 重新创建容器。默认的密码都是 `infini_rag_flow` 这种公开值，只要服务暴露在公网，第一件事就是把它们全部改掉，并在前面加一层 [[Caddy]] 或 [[Nginx]] 反向代理配上 HTTPS。

## 上手使用流程

### 配置模型

注册登录之后，第一步是到模型供应商页面添加三类模型：对话用的 LLM、向量化用的 embedding 模型，以及重排用的 reranker 模型，填写模型名称、服务地址和 API Key 即可。我自己的组合是云端 LLM 负责生成，embedding 和 rerank 用本地 Ollama 或者便宜的国内 API，既能控制成本，文档内容在向量化阶段也不用全部发到海外服务。

这里有一个非常重要的坑：知识库创建时选定的 embedding 模型决定了向量维度，之后中途更换 embedding 模型会导致检索报错或者结果错乱，只能重建知识库重新解析。所以在大量导入文档之前，务必先想清楚用哪个 embedding 模型，别等解析了几千份文档之后才发现要换。

### 创建知识库并解析文档

新建知识库时需要选择 embedding 模型、切片方法（也就是前面说的模板）以及解析器。上传文档之后点击解析，RAGFlow 会在后台排队处理，复杂的 PDF 在 CPU 上解析比较慢，几十页的扫描件跑几分钟很正常。解析完成后，我强烈建议不要急着去聊天，而是先打开文档的切块列表，挑几份最有代表性的文档逐块看一遍：表格是否完整、标题有没有和正文粘在一起、页眉页脚有没有混进来。如果某类文档切得不理想，就换一个模板重新解析，或者针对少数关键文档手动编辑 chunk。

### 检索测试与调参

切块确认没问题之后，用检索测试面板输入几个真实用户会问的问题，看召回的结果是否包含正确答案。如果相关的块排不上来，可以调低相似度阈值、调整关键词权重或者加上 reranker；如果召回了太多不相干的内容，就提高阈值或者减少 Top N。这一步做扎实了，后面对话助手的效果基本就有保障。我的经验是，绝大多数「RAG 回答不准」的问题都能在这两步定位出来，而不需要去换更贵的大模型。

### 创建对话助手

最后创建一个 Chat 助手，关联一个或多个知识库，设置系统提示词、是否显示引用、无召回时的兜底回复等。系统提示词里我一般会写清楚「只根据知识库内容回答，找不到时明确说不知道」，配合引用溯源，可以显著减少模型自由发挥的情况。需要更复杂的流程，比如先判断问题类型再决定查哪个知识库，或者查不到时去联网搜索，就可以转到 Agent 画布里用组件拼出来。

## 通过 API 和 SDK 集成

RAGFlow 提供完整的 HTTP API 和 Python SDK，基址是 `http://<host>:9380/api/v1`，请求时带上 `Authorization: Bearer <API_KEY>`，API Key 可以在个人设置里生成。如果只是想把 RAGFlow 当作检索后端，在自己的应用里调用检索接口，用 Python SDK 写起来很简单：

```
from ragflow_sdk import RAGFlow

rag = RAGFlow(api_key="<YOUR_A...