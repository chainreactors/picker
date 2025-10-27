---
title: vulnhuntr: LLM与SAST结合的AI产品漏洞自动化挖掘
url: https://forum.butian.net/share/4295
source: 奇安信攻防社区
date: 2025-04-28
fetch_date: 2025-10-06T22:02:42.247957
---

# vulnhuntr: LLM与SAST结合的AI产品漏洞自动化挖掘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### vulnhuntr: LLM与SAST结合的AI产品漏洞自动化挖掘

* [漏洞分析](https://forum.butian.net/topic/48)

通过结合静态代码分析和大语言模型（LLM）的方式来批量检测AI产品中的潜在漏洞

pre
---
通过结合静态代码分析和大语言模型（LLM）的方式来检测代码中的潜在漏洞，据作者描述通过该工具在AI bug bounty平台挖掘出多个漏洞，核心是来学习该项目的结果，如何组织LLM和SAST，同时对该项目的缺点进行分析便于进行定制化的重构
![image-20250414113410053.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d7d398b567b1857d6868be23b579d71cdabbbf2f.png)
（图源protect ai）
本着阅读项目比阅读文章更能学到新东西的态度对项目进行了分析
workflow
--------
首先我们来看下作者提供的一个完整的框架图
![image-20250405154359384.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b83df54a9048ba8d250aa3b96079f1036f5b329d.png)
大致表达了其完整的`workflow`：
1. 将待分析的文件从GitHub仓库中下载
2. 经过初步的漏洞分析
3. 再次经过第二次的分析，在这一步中，LLM将会请求获取更多的相关代码，这里会利用静态分析的方式更加精确的将上下文信息加入到LLM的Context中去，再次进行漏洞分析
4. 最后将会得到可攻击成功的POC，以及对于本次漏洞分析的置信度分数表征其分析的可靠性
下面从代码层面学习其实现方式：
其项目结构如下：
vulnhuntr/
├── .devcontainer/ # 开发容器配置
├── vulnhuntr/ # 主要源代码目录
│ ├── \\_\\_init\\_\\_.py
│ ├── \\_\\_main\\_\\_.py # 主入口文件
│ ├── LLMs.py # LLM模型相关实现
│ ├── prompts.py # 提示词模板
│ └── symbol\\_finder.py # 代码符号提取器
├── .env.example # 环境变量示例文件
├── Dockerfile # Docker构建文件
├── pyproject.toml # 项目配置文件
└── requirements.txt # 依赖包列表
从代码分析来看，这是一个使用 LLM (Large Language Model) 进行代码安全分析的工具，主要功能包括：
1. 支持多种 LLM 模型：Claude、ChatGPT 和 Ollama
2. 可以分析多种漏洞类型：LFI、RCE、SSRF、AFO、SQLI、XSS、IDOR
3. 能够分析 Python 项目中的网络相关代码
4. 提供详细的漏洞分析报告
### Pre-preparation
在其入口函数，执行的是`run()`方法
![image-20250405155247316.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-be94ab39fc53823d1bb4f072d825f4bda7b50a99.png)
首先看一下框架可选的参数列表
![image-20250408221042719.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-be6711b35cd987a88c9430ad0f42ecd8a6e911b3.png)
- -r, --root ：必需，指定要分析的项目根目录
- -a, --analyze ：可选，指定具体要分析的文件或路径
- -l, --llm ：可选，选择使用的 LLM 模型（默认为 claude）
- -v ：可选，增加输出详细程度（-v 为 INFO，-vv 为 DEBUG）
在指定了待分析的项目根目录后，`vulnhuntr`将会对项目抽象成`RepoOps`类对象，以及`SymbolExtractor`类对象
![image-20250410144935137.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ae5744ddde51b08debe949514f9f585822edf9c0.png)
`RepoOps`类其中封装了项目操作相关的多个API，主要是在整个工作流中扮演者预处理的角色，详细实现可见后文子模块的分析
![image-20250408221651439.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-6535301ba78e5dceb415c6711fe65764fb219c1e.png)
而对于`SymbolExtractor`类，其同样封装了多个API操作，核心是利用的`jedi`这一个python语言下的静态分析框架进行项目代码分析，主要特点为采用多层次搜索策略，确保能够寻找到不同情况的符号定义，同时提供了比较灵活的文件搜索和过滤机制，具体的分析见后面的子模块分析
![image-20250410145808749.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-07a2d65b6ae1cc01bd37109b3e9a95a4516755f7.png)
接下来进入具体的分析逻辑
1. 他会通过封装的`RepoOps`类对象的`get\_relevant\_py\_files`方法来获取，不包括以下内容的所有项目中的`.py`文件
![image-20250410161534354.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b84dbce6f46bdab6bfffdac32c03dd28e529ca88.png)
2. 接下来进入一个小小的分支，将会对通过`--analyze`参数指定的文件路径或者文件进行漏洞分析，若没有对其进行指定则将会分析完整的项目
![image-20250412201340298.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f27177c135fe8a9251b4c939235427ea46e741ea.png)
不管是使用的`get\_files\_to\_analyze`或者`get\_network\_related\_files`，其均是返回待分析的文件列表，其中后者是筛选出以下source点文件进行分析
3. 接下来则为通过LLM的能力进行README文件信息的提取，构建出一个`System Prompt`出来使得LLM能够更好的理解待分析的项目
![image-20250412211402369.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f7237c8f1bc5f10e75b41d367dab74b68db99d7a.png)
其中的`README\_SUMMARY\_PROMPT\_TEMPLATE`提示词是用来进行README文件的信息提取
![image-20250412211526769.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-8602c6aac8decd9814655ed0943d24ef48aed8a8.png)
而`SYS\_PROMPT\_TEMPLATE`提示词是用来指定LLM的任务，列举了需要分析的漏洞列表
![image-20250412211706998.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-616ae6c038c874d5db7e108d588188d51c06dbe6.png)
### Core Analysis
上述过程的pipeline中得到了如下的关键信息
1. 通过提取README文件的信息使得LLM能够一定层度理解项目
2. 通过正则匹配的方式获取到了后续漏洞分析的起始文件（也即是包含有路由信息的.py文件）
后续根据上述得到的信息进行进一步的漏洞检测任务
这里待分析的文件包含有两个维度，其一为通过`--analyze`参数指定的文件或者文件夹下的文件，另外则是所有`network-related`文件（像是Flask框架的`@app.route(xx)`类似的API调用文件）
![image-20250412212547356.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e4e5a23af99eea56b506237b83b0c5d806fcf834.png)
核心的漏洞检测任务将会遍历获取的所有文件列表中的任意个`.py`
首先当然是加载理解了项目信息的LLM
#### initial analysis
之后进行初步的分析任务：
![image-20250412213018965.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d0ff375693b57530c4cc271a0346f9b79b77a6a0.png)
1. 这里使用`<file\_code>`标签包裹待分析的单个`.py`文件的所有代码
2. 使用`<instructions>`标签包裹我们的进行代码分析的指令
![image-20250412215004599.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-306af21ea54cdbd5939c603ceee1f377b69131d0.png)
\*\*指令剖析\*\*：指定了需要检查的sinks，同时表明如果存在安全限制的情况下需要对其进行bypass操作，在这个基础上从`API endpoints`为起点进行漏洞检测，同时表明了对于不能够明显的判断其存在对应的漏洞的情况下，可以通过`<context\_code>`包裹你需要请求的类或者方法代码进行进一步的漏洞分析验证
3. 使用`<analysis\_approach>`标签用来包裹在漏洞分析过程中的具体方法
![image-20250412222014397.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d35e038caec34834ff5054358e6e1a67e037637f.png)
\*\*指令剖析\*\*：
- 再次强调需要全面的进行审计
- 漏洞扫描规则：指明关注可远程利用的漏洞，并指出可能需要对一些不是很明显的攻击方式进行更为细致的检查，更加强调了漏洞成因的多元化
- 代码调用路径分析规则：指出需要重点关注从`source`点位置流出的数据流信息，需要分析每一类数据流的处理方式、存储位置、输出内容，防止在漏洞检测过程中出现过高的\*\*假阳性\*\*
- 安全限制绕过思路：首先对其安全限制的实现方式进行理解和分析，在充分了解安全防御的基础上，制定可能的绕过方法并验证其可行性
- 上下文敏感分析：强调在漏洞检测的过程中需要具备上下文敏感的特性，维护一个`context\_code`域进行上下文函数调用的相关代码记录，在分析过程中进行结合分析
- 最后就是审计的结果输出要求
4. 只用`<guidelines>`包裹一些输出的指南
![image-20250412223541120.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e9b0ecb61aa92389a56adee57f180f8f9669bfbf.png)
5. 最后就是通过`<response\_format>`包裹我们预期的输出格式
核心内容为pydantic定义的类`Response`
![image-20250412223926431.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-501d758e1abc2061fa816bea7d3935adb7f41ba7.png)
会将上述的所有标签及标签中的内容喂给LLM进行理解分析进行初步的漏洞审查
\*\*总结：\*\*初步审查的目的是用来进行可能的漏洞点存在的筛选，这里不存在有具体的漏洞检测任务
#### secondary analysis
将会对初始审查结果中的可能存在漏洞风险的代码进行对应漏洞类型的具体审查，具体来说分成了多个轮次
##### First round
对于第一个轮次，其不会进行具体的漏洞审查工作
![image-20250413100429300.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f781279d8711d7756a2c6955e51de9f7a3529f37.png)
\*\*个人理解：\*\*这样设置的作用个人感觉主要是出于以下原因进行考虑
1. 渐进式分析：让LLM首先基于`initial analysis`进行分析，再根据需要请求更多的上下文
2. 细化工作流：使用LLM进行具体漏洞类型的分析，获取更精确的分析结果
好的，下面看一下其如何实现：
1. 在第一个轮次中，并不会请求`context code`，同时也不会引入`initial analysis`的分析结果
2. 构建具体漏洞审查的`prompt`
![image-20250413101317015.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-7971d45d50be29b9f8be4f1a99021f7a16f97dca.png)
1. 引入待分析`.py`文件代码
2. 第一个轮次中不存在`context code`，其他轮次中，将会加载获取的`context functions and classes`
3. 加载一些特定漏洞的Bypass示例，更好的知道LLM进行Bypass任务
![image-20250413101705039.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-24c2e5db120be1808d6a25ac02236c07d4be7fef.png)
4. 引入特定漏洞的具体如何审查的指令
这里以`RCE`漏洞为例：
![image-20250413101850297.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ff481587667376e0f692d105801b147c1680c3ce.png)
5. 最后规定了LLM生成回复范式，同样包含有下面这几类元素
![image-20250413102018614.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c14ea8e3c039c800808fe95d5a6c8040f9379f30.png)
##### other rounds
其他轮次相比于第一个轮次多了两点：1. `context code`的加载 2. `previous analysis`的协同分析
![image-20250413102706229.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b8ebeb0783bc73b06d14b69ad04c40f697eb77ed.png)
1. 首先会对上次的分析进行转存记录，后续遍历上次请求中所有需要获取的`context code`，在确保了没有请求已经存在的`context code`的情况下，将会调用`SymbolExtractor`类的`extract`方法进行对应Function或者...