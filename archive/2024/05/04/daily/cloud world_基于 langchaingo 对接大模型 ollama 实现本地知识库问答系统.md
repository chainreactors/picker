---
title: 基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统
url: https://cloudsjhan.github.io/2024/05/03/%E5%9F%BA%E4%BA%8E-langchaingo-%E5%AF%B9%E6%8E%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B-ollama-%E5%AE%9E%E7%8E%B0%E6%9C%AC%E5%9C%B0%E7%9F%A5%E8%AF%86%E5%BA%93%E9%97%AE%E7%AD%94%E7%B3%BB%E7%BB%9F/
source: cloud world
date: 2024-05-04
fetch_date: 2025-10-06T17:15:47.772606
---

# 基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统

posted

2024-05-03

|

in

[ollama](/categories/ollama/)

|

visitors:

|

|

wordcount:

1,447
|

min2read ≈

6

基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统

![](https://)

[Ollama](https://github.com/ollama/ollama "ollama") 是一个基于 Go 语言开发的简单易用的本地大语言模型运行框架。在管理模型的同时，它还基于 Go 语言中的 Web 框架 [gin](https://github.com/gin-gonic/gin "gin")提供了一些 Api 接口，让你能够像跟 OpenAI 提供的接口那样进行交互。

Ollama 官方还提供了跟 docker hub 一样的模型 hub，用于存放各种大语言模型，开发者也可以上传自己训练好的模型供其他人使用。

### 安装 ollama

可以在 ollama 的 github [release](https://github.com/ollama/ollama/releases "ollama release")  页面直接下载对应平台的二进制包进行安装，也可以 docker 一键部署。这里演示的机器是 macOS M1 PRO 版本，直接下载安装包，安装即可，安装之后，运行软件。

运行之后，项目默认监听 `11434` 端口，在终端执行如下命令可验证是否正常运行：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` $ curl localhost:11434 Ollama is running ``` |

![](https://files.mdnice.com/user/4760/83011ecd-e86e-4932-9d5c-841a929599b0.png)

### 大模型管理

ollama 安装后，就可以对大模型进项安装使用了。Ollama 还会携带一个命令行工具，通过它可以与模型进行交互。

* `ollama list`：显示模型列表。
* `ollama show`：显示模型的信息
* `ollama pull`：拉取模型
* `ollama push`：推送模型
* `ollama cp`：拷贝一个模型
* `ollama rm`：删除一个模型
* `ollama run`：运行一个模型

在官方提供的模型仓库中可以找到你想要的模型：<https://ollama.com/library>

> 注意：应该至少有 8 GB 可用 RAM 来运行 7 B 型号，16 GB 来运行 13 B 型号，32 GB 来运行 33 B 型号。

比如我们可以选择 [Qwen](https://github.com/QwenLM/Qwen1.5 "Qwen") 做个演示，这里用 1.8B 的模型(本地电脑比较可怜，只有 16G😭)：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $ ollama run qwen:1.8b ``` |

是不是觉得这个命令似曾相识，是的，跟 docker run image 一样，如果本地没有该模型，则会先下载模型再运行。

![](https://files.mdnice.com/user/4760/5aec9be5-52dc-4078-8780-d8fa0bcc4c3f.png)

既然跟 docker 如此一致，那么是不是也会有跟 Dockerfile 一样的东西，是的，叫做 Modelfile :

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` FROM qwen:14b  # set the temperature to 1 [higher is more creative, lower is more coherent] PARAMETER temperature 1  # set the system message SYSTEM """ You are Mario from super mario bros, acting as an assistant. """ ``` |

保存上面的代码为 Modelfile，运行 `llama create choose-a-model-name -f Modelfile` 就可以定制你的模型，`ollama run choose-a-model-name` 就可以使用刚刚定制的模型。

![](https://files.mdnice.com/user/4760/9d52c8ff-abb0-4af9-811d-38944b63989e.png)

### 对接 ollama 实现本地知识库问答系统

#### 前置准备

模型都在本地安装好了，我们可以对接这个模型，开发一些好玩的上层 AI 应用。下面我们基于 langchaningo 开发一个问答系统。

下面的系统会用到的模型有 ollama qwen1.8B，nomic-embed-text，先来安装这两个模型：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ollama run qwen:1.8b ollama run nomic-embed-text:latest ``` |

我们还需要一个向量数据库来存储拆分后的知识库内容，这里我们使用 `qdrant` :

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` docker pull qdrant/qdrant $ docker run -itd --name qdrant -p 6333:6333 qdrant/qdrant ``` |

![](https://files.mdnice.com/user/4760/e55f492c-c783-4086-b02f-35f540568076.png)

启动 qdrant 后我们先创建一个 Collection 用于存储文档拆分块:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` curl -X PUT http://localhost:6333/collections/langchaingo-ollama-rag \   -H 'Content-Type: application/json' \   --data-raw '{     "vectors": {       "size": 768,       "distance": "Dot"     }   }' ``` |

#### 知识库内容切分

这里提供一篇[文章](https://baijiahao.baidu.com/s?id=1770104977332994833&wfr=spider&for=pc "样例文章")供大模型学习，下面的代码将文章拆分成小的文档块：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` func TextToChunks(dirFile string, chunkSize, chunkOverlap int) ([]schema.Document, error) { 	file, err := os.Open(dirFile) 	if err != nil { 		return nil, err 	} 	// create a doc loader 	docLoaded := documentloaders.NewText(file) 	// create a doc spliter 	split := textsplitter.NewRecursiveCharacter() 	// set doc chunk size 	split.ChunkSize = chunkSize 	// set chunk overlap size 	split.ChunkOverlap = chunkOverlap 	// load and split doc 	docs, err := docLoaded.LoadAndSplit(context.Background(), split) 	if err != nil { 		return nil, err 	} 	return docs, nil } ``` |

#### 文档存储到向量数据库

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` func storeDocs(docs []schema.Document, store *qdrant.Store) error { 	if len(docs) > 0 { 		_, err := store.AddDocuments(context.Background(), docs) 		if err != nil { 			return err 		} 	} 	return nil } ``` |

#### 读取用户输入并查询数据库

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` func useRetriaver(store *qdrant.Store, prompt string, topk int) ([]schema.Document, error) { 	// 设置选项向量 	optionsVector := []vectorstores.Option{ 		vectorstores.WithScoreThreshold(0.80), // 设置分数阈值 	}  	// 创建检索器 	retriever := vectorstores.ToRetriever(store, topk, optionsVector...) 	// 搜索 	docRetrieved, err := retriever.GetRelevantDocuments(context.Background(), prompt)  	if err != nil { 		return nil, fmt.Errorf("检索文档失败: %v", err) 	}  	// 返回检索到的文档 	return docRetrieved, nil } ``` |

#### 创建并加载大模型

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` func getOllamaQwen() *ollama.LLM { 	// 创建一个新的ollama模型，模型名为"qwena:1.8b" 	llm, err := ollama.New( 		ollama.WithModel("qwen:1.8b"), 		ollama.WithServerURL(ollamaServer)) 	if err != nil { 		logger.Fatal("创建ollama模型失败: %v", err) 	} 	return llm } ``` |

#### 大模型处理

将检索到的内容，交给大语言模型处理

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` // GetAnswer 获取答案 func GetAnswer(ctx context.Context, llm llms.Model, docRetrieved []schema.Document, prompt string) (string, error) { 	// 创建一个新的聊天消息历史记录 	history := memory.NewChatMessageHistory() 	// 将检索到的文档添加到历史记录中 	for _, doc := range docRetrieved { 		history.AddAIMessage(ctx, doc.PageContent) 	} 	// 使用历史记录创建一个新的对话缓冲区 	conversation := memory.NewConversationBuffer(memory.WithChatHistory(history))  	executor := agents.NewExecutor( 		agents.NewConversationalAgent(llm, nil), 		nil, 		agents.WithMemory(conversation), 	) 	// 设置链调用选项 	options := []chains.ChainCallOption{ 		chains.WithTemperature(0.8), 	} 	res, err := chains.Run(ctx, executor, prompt, options...) 	if err != nil { 		return "", err 	}  	return res, nil } ``` |

#### 运行应用

|  |  |
| --- | --- |
| ``` 1 ``` | ``` go run main.go getanswer ``` |

输入你想要咨询的问题

![](https://files.mdnice.com/user/4760/4e989a5d-f7f8-4191-87f9-adff732d8d5a.png)

系统输出结果：

![](https://files.mdnice.com/user/4760/9d7d30bc-1f71-4e79-9783-2bb3f2d4277f.png)

输出的结果可能会因为学习资料的不足或者模型的大小存在区别，有很多结果都不是很准确，这就需要提供更多的语料进行训练。而且还要对代码里的各个参数进行调优，并结合文档的内容，大小，格式等进行参数的设定。

项目的源码可以参考：<https://github.com/hantmac/langchaingo-ollama-rag.git>

---

-------------The End-------------

Title:[基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统](/2024/05/03/%E5%9F%BA%E4%BA%8E-langchaingo-%E5%AF%B9%E6%8E%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B-ollama-%E5%AE%9E%E7%8E%B0%E6%9C%AC%E5%9C%B0%E7%9F%A5%E8%AF%86%E5%BA%93%E9%97%AE%E7%AD%94%E7%B3%BB%E7%BB%9F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月03日 - 10:05

Last Update:2024年05月03日 - 10:05

Original Link:[https://cloudsjhan.github.io/2024/05/03/基于-langchaingo-对接大模型-ollama-实现本地知识库问答系统/](/2024/05/03/%E5%9F%BA%E4%BA%8E-langchaingo-%E5%AF%B9%E6%8E%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B-ollama-%E5%AE%9E%E7%8E%B0%E6%9C%AC%E5%9C%B0%E7%9F%A5%E8%AF%86%E5%BA%93%E9%97%AE%E7%AD%94%E7%B3%BB%E7%BB%9F/ "基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[langchaingo](/tags/langchaingo/)
 [ollama](/tags/ollama/)

(>给这篇博客打个分吧<)

[数据同步工具考古](/2024/02/07/%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5%E5%B7%A5%E5%85%B7%E8%80%83%E5%8F%A4/ "数据同步工具考古")

[Golang 如何实现自定义 CDC 工具？](/2024/05/04/Golang-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%AE%9A%E4%B9%89-CDC-%E5%B7%A5%E5%85%B7%EF%BC%9F/ "Golang 如何实现自定义 CDC 工具？")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hant...