---
title: 给大模型通过RAG挂上知识库
url: https://mp.weixin.qq.com/s/o_EtmHGCn6MZZ2Kp_CPktw
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:14:13.558243
---

# 给大模型通过RAG挂上知识库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkjS1lew6n3RLRx5jwwA60iamUrzXgV7eEI679icR220licd7O2SER2QNBcQjPQVtiaH2FVoKwlIJvwYPBNclauib35fzJFh2DmIpzS8/0?wx_fmt=jpeg)

# 给大模型通过RAG挂上知识库

Jumbo
Jumbo

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5znJiaZxqldyq3SBEPw0n6hCXNk6PmR3gyPFJDUCibH91GiaAHHKiaCpcsfnQJ2oImQunzubgDtpxzxNHONU88CypA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 前言

因为大模型的知识库存在于训练期间，因此对于一些最新发生的事或者是专业性问题可能会出现不准确或者是幻觉，因此可以使用RAG技术给大模型外挂知识库来达到精准回答的目的。

## 实操

### gpt4all

可以参考之前的文章：[Llama模型私有化教程](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247552081&idx=1&sn=9d549d6e256255e45be57198b1e93fc0&scene=21#wechat_redirect)

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image1.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPMyGENZUfLLsWgzzfUniauzHibOtfIFtDaAAZzqs2b3j5RLzC0F6Wib4ic3w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image2.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPMiaZiaibd2iauc3iaDV7XuAZhVTWkdkrYvybB6BCUOYFB7zyuCcC2oSeBdqA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

他的优点就是通过UI在线下载模型和导入知识库，操作都比较一站式、傻瓜式。注意的是gpt4all的模型文件和ollama不通用。

### open-webui

安装可以参考[Llama模型私有化教程](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247552081&idx=1&sn=9d549d6e256255e45be57198b1e93fc0&scene=21#wechat_redirect)，也比较简单就不多赘述。

先看下在没有知识库的情况下，咨询相关问题时得到的结果是错误的：

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image3.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPMaMUibEC2zeqoOdOOMeHrQiaFTGD1EJgdDicSKjk4GSho8ibJ86dQRdGPNA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

可以通过如下方式进行知识库的构建：

```
1. 右上角-工作空间-知识库-新增知识库空间-上传知识库文件
```

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image4.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPM14DOOia5L7hNmrhYwkWbXibbvwj6YxFqRVac0DHrcluoRCC8SCT9gmcA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

这个时候再咨询知识库中存在的内容时就可以得到满意的结果（引用的方式是在输入框中输入#）：

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image5.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPM8hAnia80iczNbqrVxfiaNBGHqepOTKVIOD9TibsuorVsXOAgXKPBNLNpow/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

### ima

https://ima.qq.com/

ima是腾讯出品的AI+知识库的软件。创建知识库的流程为：

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image6.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPM8YAs2mD6cLvp7V939j25HSUXJE0KaMLriad5Cia2mEA9CGWb7qp3WIKw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

首先有个缺点，它竟然不能上传markdown。还有些其他BUG，比如明明存在知识库，但是却选择不了：

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image7.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPMoVLxwqfwTmyIaiciaweXG03FmMupib72y6RO3vyPagfFXVxAQ7vS7wpuQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image8.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPMA5rckyQh3ynW97iclg0L8xk59v1Wq5ctvsg3dSPxEKn9ic0oXLpGrfZA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

因为没法设置prompt，如果你想让大模型每次都只从知识库中搜索不要联想，那么就就需要每次在输入框中输入特定prompt告知不要胡乱回答，结果发现又是混元问题，问答模型改成deepseek后好点：

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image9.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPM8wF5FJGOV9s2aV6v1j4R9FNMsXPJJyYuwUvA8dRc14vWVgKT5a5VuA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

![%E7%BB%99%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%80%9A%E8%BF%87RAG%E6%8C%82%E4%B8%8A%E7%9F%A5%E8%AF%86%E5%BA%93%201a299cb8437880b4b2fbeffb089f8084/image10.png](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxgRmiaqrHTTUicF2ceQ4micPM24S4aicIoGzsmIyMjtqzbe42PAicTuV53sTBDyjappyGXuTLmnMyjKtQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

终于明白这些公司为什么要接deepseek了，因此自己公司的太差。

### langchain+chroma

上面介绍的都是通过图形化的方式进行，但是在一些工程化的地方可能没法进行图形化操作，接下来介绍使用代码的方式来进行让大模型外挂知识库。把文档投喂给大模型时需要先对文档进行向量转换，这里以chroma 官方代码为例：

```
1. import chromadb
2. # setup Chroma in-memory, for easy prototyping. Can add persistence easily!
3. client = chromadb.Client()

5. # Create collection. get_collection, get_or_create_collection, delete_collection also available!

7. collection = client.create_collection("all-my-documents")

9. # Add docs to the collection. Can also update and delete. Row-based API coming soon!

11. collection.add(
12. documents=["This is document1","This is document2"],# we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
13. metadatas=[{"source":"notion"},{"source":"google-docs"}],# filter on these!
14. ids=["doc1","doc2"],# unique for each doc
15. )

17. # Query/search 2 most similar results. You can also .get by id

19. results = collection.query(
20. query_texts=["This is document1"],
21. n_results=2,
22. # where={"metadata_field": "is_equal_to_this"}, # optional filter
23. # where_document={"$contains":"search_string"}  # optional filter
24. )
25. print(results)
```

上述代码含义是创建了一个集合，并且往集合中添加知识库，每个知识库都必须有自己的独立id。注意，chroma只支持传入文本不支持直接引用文件，因此想要把文件转成向量需要先把文件读取出内容给到chroma才行。

得到的内容如下：

```
1. {'ids':[['doc1','doc2']],'embeddings':None,'documents':[['This is document1','This is document2']],'uris':None,'data':None,'metadatas':[[{'source':'notion'},{'source':'google-docs'}]],'distances':[[0.0,0.2221483439207077]],'included':[<IncludeEnum.distances:'distances'>,<IncludeEnum.documents:'documents'>,<IncludeEnum.metadatas:'metadatas'>]}
```

其中distances代表是距离，笔者特地把搜索的问题和id为doc1的内容一致，因此可以看到得到的距离为0（距离越小，相似度越高），代表问题和文档一模一样，因此在后续投喂给大模型时，可以选择小于多少距离的投喂给大模型来解决token过长的问题。

接下来介绍langchain，langchain功能和它的名字一样，简单理解就是它可以把各个东西和大模型串在一起，比如可以把上面chroma生成的文档向量投喂给大模型进行知识库问答。langchain牛逼的点是他做了很多第三方工具的集成，比如以langchains调用chroma生成向量数据库为例：

```
1. from langchain_ollama importOllamaEmbeddings
2. from langchain_chroma importChroma
3. from uuid import uuid4
4. from langchain_core.documents importDocument
5. embeddings =OllamaEmbeddings(model="nomic-embed-text:latest")
6. vector_store =Chroma(
7. collection_name="example_collection",
8. embedding_function=embeddings,
9. persist_directory="./chroma_langchain_db",# Where to save data locally, remove if not necessary
10. )
11. document_1 =Document(
12. page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
13. metadata={"source":"tweet"},
14. id=1,
15. )
16. document_2 =Document(
17. page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
18. metadata={"source":"news"},
19. id=2,
20. )
21. document_3 =Document(
22. page_content="Building an exciting new project with LangChain - come check it out!",
23. metadata={"source":"tweet"},
24. id=3,
25. )
26. document_4 =Document(
27. page_content="Robbers broke into the city bank and stole $1 million in cash.",
28. metadata={"source":"news"},
29. id=4,
30. )
31. document_5 =Document(
32. page_content="Wow! That was an amazing movie. I can't wait to see it again.",
33. metadata={"source":"tweet"},
34. id=5,
35. )
36. docume...