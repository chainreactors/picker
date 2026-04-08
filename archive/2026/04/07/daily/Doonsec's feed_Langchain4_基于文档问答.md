---
title: Langchain4_基于文档问答
url: https://mp.weixin.qq.com/s/GjIRnqwHuMHQzhqk5WZcpw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:46.139056
---

# Langchain4_基于文档问答

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TdxqpHZFSV3HJ2FksQ5ibwQ1qWXhskZiaADTMw8ibnIHjpvIErliaoypu8R6VvZDYia45BSD6Oo38uLpZpAiaqpQd34DzgGGVuyVPeg3leQsPxVJc/0?wx_fmt=jpeg)

# Langchain4\_基于文档问答

原创

羽泪云小栈
羽泪云小栈

羽泪云小栈

![]()

在小说阅读器中沉浸阅读

# 基于文档的问答

有时候我们想通过检索pdf、txt、csv等文档，让llm帮忙总结内容等... 需要向量的参与

https://www.bilibili.com/video/BV1b4421D71Y/?spm\_id\_from=333.788.videopod.episodes&vd\_source=c49e37118f69c7a5b34915b73d1b78ab&p=5

https://github.com/ConnectAI-E/LangChain-Tutior/blob/main/python/cn/5.%E6%96%87%E6%A1%A3%E9%97%AE%E7%AD%94.ipynb

需要两个模型噢，一个向量模型(可以本地解决)，一个对话模型

## 前置准备

https://docs.langchain.com/oss/python/integrations/vectorstores/docarray\_in\_memory

```
pip install -qU  langchain-community "docarray"
```

我需要重配置一下虚拟环境，不然下载库的时候有冲突

```
python -m venv langchain_env

1.langchain_env\Scripts\activate
或者
2.在VSCode中，不需要手动激活：
按 Ctrl+Shift+P
输入 Python: Select Interpreter
选择你的虚拟环境：E:\Langchain_Learn\langchain_env\Scripts\python.exe
打开新的cmd终端，VSCode会自动激活虚拟环境

虚拟环境下：
pip install langchain langchain-openai langchain-community docarray dotenv pandas
```

右键运行时会报错，找不到文件，还是要新建文件夹为.vscode，该目录下新建文件settings.json

配置为：

```
{
    // Python 解释器配置
    "python.defaultInterpreterPath": "E:\\Langchain_Learn\\langchain_env\\Scripts\\python.exe",

    // 终端自动激活虚拟环境
    "python.terminal.activateEnvironment": true,
    "python.terminal.activateEnvInCurrentTerminal": true,

    // Code Runner 配置
    "code-runner.executorMap": {
        "python": "cd $dir && E:\\Langchain_Learn\\langchain_env\\Scripts\\python.exe $fileName"
    },
    "code-runner.runInTerminal": true,
    "code-runner.fileDirectoryAsCwd": true,
    "code-runner.saveFileBeforeRun": true,
    "code-runner.clearPreviousOutput": false,
    "code-runner.respectShebang": false,
    "code-runner.ignoreSelection": true,

    // 文件编码配置
    "files.encoding": "utf8",
    "files.autoSave": "afterDelay",

    // 终端配置
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell"
        }
    }
}
```

相当于每次用的是虚拟环境的python.exe

## csv准备

准备好本次的文档，让llm生成下即可

![image-20260404184202957](https://mmbiz.qpic.cn/sz_mmbiz_png/TdxqpHZFSV3fCaBHcicb5CbTVmicKAxQywj2OmeQKbrBfkYfolPoibZP7OkDqXKzcRorW6FMqSaGicjyZ4ST37xfH1OfA764r0Ng1OILeBnLsGo/640?from=appmsg "null")

```
import pandas as pd
from io import StringIO
import os
from langchain_community.document_loaders import CSVLoader

file='cybersecurity_qa.csv'
loader=CSVLoader(file_path=file,encoding="utf-8")
docs = loader.load()
print(docs[0])

"""
page_content='title: SQL注入攻击原理
content: SQL注入是一种将SQL代码插入或添加到应用（用户）的输入参数中的攻击技术，攻击者通过这些参数传递给后台
SQL服务器加以解析并执行。常见的注入方式包括：联合查询注入、布尔盲注、时间盲注、报错注入等。防御措施：使用参
数化查询、输入验证、最小权限原则。
category: Web安全' metadata={'source': 'cybersecurity_qa.csv', 'row': 0}
```

## 向量

https://zhuanlan.zhihu.com/p/634237861 嵌入(embedding)和向量(vector)

很像做机器学习的时候的特征提取，将通用的数据用向量表示其含义。

这里的向量也不是以前学数学的那种平面向量，机器学习里，是一个有序的数字列表，理解为一种编码的方式吧，将事物编码成向量，模型就能够学习、计算和推理。

要用到向量模型，而不是对话模型。

比如：`from langchain_openai import OpenAIEmbeddings`

Embedding是将文本，变为一组数字(向量)，这组数字就代表它所表示的文本含义。

内容相似的文本，也有相似的向量值；内容不同的文本，向量值的区别也大。

所以这种技术是利用向量找到和问题相似的文本片段，一起传递给llm回答问题。

用了本地免费向量模型**HuggingFaceEmbeddings**

```
#这是旧版
from langchain_community.embeddings import HuggingFaceEmbeddings
#新版推荐安装pip install -U langchain-huggingface 我下不下来，就算了
pip install sentence-transformers #embeddings需要这个
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com' #第一次使用时要下载的，超时就用镜像站
```

```
import pandas as pd
from io import StringIO
import os
from langchain_community.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
file='cybersecurity_qa.csv'
loader=CSVLoader(file_path=file,encoding="utf-8")
docs = loader.load()
#print(docs[0])
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
embed = embeddings.embed_query("Web安全")
print(len(embed))
print(embed[:5])

384
[-0.09801744669675827, 0.014501313678920269, -0.014877825044095516, -0.008558204397559166, -0.017776664346456528]
```

这个意思是说，它有384个维度的向量值

来三个例子，直观感受一下，并用**余弦相似度**比较向量之间是否相似

```
import pandas as pd
from io import StringIO
import os
from langchain_community.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
file='cybersecurity_qa.csv'
loader=CSVLoader(file_path=file,encoding="utf-8")
docs = loader.load()
#print(docs[0])
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text1="SQL注入是一种数据库攻击技术"
text2="SQL注入可以窃取数据库中的敏感数据"
text3="上传shell可以获取权限"
embed1 = embeddings.embed_query(text1)
print(len(embed1))
print(embed1[:10])
embed2 = embeddings.embed_query(text2)
print(len(embed2))
print(embed2[:10])
embed3 = embeddings.embed_query(text3)
print(len(embed3))
print(embed3[:10])

vectors = [embed1,embed2,embed3]
sim_matrix = cosine_similarity(vectors)
print("\n相似度矩阵:")
print(sim_matrix)
```

![image-20260404212007549](https://mmbiz.qpic.cn/mmbiz_png/TdxqpHZFSV0ycCcgibF1PfOhV8cYbiaGM59xzyFmzib8S2l3iaoDSdkU7Yn4Agk47u6VO6VDYofohGt6ZUz2Gx255ZhZ2jEQWIqqWgYcNaSnrc4/640?from=appmsg "null")

都是384个维度，然后相似度矩阵就是二维数组嘛

文本跟自身比那肯定完全一致。

可以看出文本1和文本2 是**比较相似**的。为0.74

文本1和文本3，以及文本2和文本3**不太相似**。因为小于0.5了都

其实也取决于模型本身的采用过的数据集啊、训练方式等等吧，为了严谨一点，用一个支持**中文的模型**(也支持中英混合)

https://hf-mirror.com/BAAI/bge-small-zh-v1.5

```
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)
text1="SQL注入是一种数据库攻击技术"
text2="SQL注入可以窃取数据库中的敏感数据"
text3="上传shell可以获取权限"
```

![image-20260405111838288](https://mmbiz.qpic.cn/mmbiz_png/TdxqpHZFSV2XkqBw8MwoE81RKZlBLjKOTOwTuZSBcibUYficF6mar5rcR7KWHzRtbctiaOjwiaJw3O1wDn0ZwA3ureBibfa7O5hpBFOsVRHlSicIg/640?from=appmsg "null")

**总结一下：**

llm通过**嵌入向量**(embedding vectors)达到目的

就是我们并不指望llm能看懂文字，实际上它也不需要懂。

只需要将文本转化为向量值，也就是一组数字，用这组数字来代表文本含义。

这样一来，问题就被转化成了：问题文本对应一个向量，而 CSV 文件里的每条内容也对应各自的向量。

接下来要做的，就是找出与问题向量最相似的其它向量。找到了，也就找到了想要的答案

特别说明，有时候两个差别很大的词，对应的向量也被认为是相似的，**不是因为它们属性相同，而是因为它们在大量文本中总是一起出现（比如"苹果电脑"），模型把"上下文使用场景的相似"当作了"相似"**

某种方面来讲：**向量相似度 ≠ 属性相似度，而是"文本搭配/上下文环境的相似度"**

用英文的模型试试：苹果和电脑的关联度

```
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text1="apple"
text2="pear"
text3="computer"

[[1.         0.47442532 0.5624204 ]
 [0.47442532 1.         0.35905761]
 [0.5624204  0.35905761 1.        ]]
```

看，apple和computer的相似度 比另外两个相互搭配的确实要高一些，为0.5624204...

中文模型呢

```
embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)
text1="苹果"
text2="梨子"
text3="电脑"

[[1.         0.58180949 0.66143068]
 [0.58180949 1.         0.39980222]
 [0.66143068 0.39980222 1.        ]]
```

这里苹果和电脑的相似度为0.66，也会高一些，当然，取决于预训练的模型质量等等...

## 索引查询

**`VectorstoreIndexCreator` 一键创建"向量存储索引"**，算是一键完成了所有步骤。(文档加载、分割文本、创建向量存储、创建检索器、链)

先用英文的向量模型试试

```
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
import pandas as pd
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

load_dotenv(find_dotenv())
llm = ChatOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("KEY2"),
    base_url=os.environ.get("base_url2"),
    temperature=0.0,#让预测不让那么随机，偏平稳
    model=os.environ.get("model2")
)

file='cybersecurity_qa.csv'
loader=CSVLoader(file_path=file,encoding="utf-8")
#data = pd.read_csv(file,header=None)
#print(data)

embed...