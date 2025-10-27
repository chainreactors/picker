---
title: 构建LLM AI应用的几种范式思考 - 郑瀚Andrew
url: https://buaq.net/go-166450.html
source: unSafe.sh - 不安全
date: 2023-05-31
fetch_date: 2025-10-04T11:37:17.680131
---

# 构建LLM AI应用的几种范式思考 - 郑瀚Andrew

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5100bf8526bbd555ef41a78d8a1ee8d6.jpg)

构建LLM AI应用的几种范式思考 - 郑瀚Andrew

单纯的LLM多轮交互更多面向C端消费场景，而B端应用场景需要LLM进行更多的被集成工作更抽象、更本质地看，LLM充当的是物理世界人类语言—>信息世界比特信息的翻译者的角色，它带来的是一种新的人机
*2023-5-30 22:3:0
Author: [www.cnblogs.com(查看原文)](/jump-166450.htm)
阅读量:42
收藏*

---

## 单纯的LLM多轮交互更多面向C端消费场景，而B端应用场景需要LLM进行更多的被集成工作

更抽象、更本质地看，LLM充当的是物理世界人类语言—>信息世界比特信息的翻译者的角色，它带来的是一种新的人机交互方式的改变。

基于这种范式改变，传统的所有B端应用都有希望被重新定义和重构一遍。

## 只有思考的”大脑“，而缺少行动的”手脚“，无法在LLM模型之外的真实世界开展行动

不论是

* 搜索网页
* 调用外部第三方 API
* 查找数据库
* 执行代码数理计算逻辑
* 执行操作系统指令
* ....

这些能力都无法被基础的LLM模型提供。

关于“手臂”的探索也有很多，

* OpenAI 的 WebGPT 给模型注入了使用网页信息的能力
* Adept 训练的 ACT-1 则能自己去网站和使用 Excel、Salesforce 等软件
* PaLM 的 SayCan 和 PaLM-E 尝试让 LLM 和机器人结合
* Meta 的 Toolformer 探索让 LLM 自行调用 API
* 普林斯顿的 Shunyu Yao 做出的 ReAct 工作通过结合思维链 prompting 和这种“手臂”的理念让 LLM 能够搜索和使用维基百科的信息
* ChatGPT 可以运行Python编译器处理上传或下载的代码、文件。ChatGPT支持用户将文件上传至会话工作区、可以执行Python编译器运行代码，并在会话中持续存在供后续调用。该功能能够协助程序员提升工作流程效率，在用户实际使用中能够解决定量和定性的数学问题，进行数据分析和可视化，转换文件格式。
* ……

有很多迹象表明，xxxGPT Plugins有望成为AI时代的核心入口，从大模型技术赋能者转向平台经济重要生态入口卡位，

* 一方面可以接入应用、赋能应用
* 一方面可以调用应用、操作应用，以大模型兼具“操作系统”角色，加速海外生态中与其他应用层的精细化分工。

## LLM的参数空间维度十分巨大，生成内容的质量（helpful、honest、harmless）强依赖输入的质量

大语言模型在预训练阶段就已习得大部分知识，如果想要LLM产生针对特定任务的高质量内容，有三种技术方向：

* **instruction-align对齐**，使模型对特定任务的输入具备更好地向量化编码与特征提取能力，这对prompt-tune语料的质量有一定要求。
* **few-shot prompt**，通过prompt注入更多的上下文知识，从而构造出更高质量的输入向量，但是这往往受限于 token 数量。
* **embedding search**，通过对输入进行embedding search，从而获得contextful prompt，降低了prompt engineering的难度和门槛。

不管是instruction-aling对齐、few-shot prompt，还是embedding search，都需要为模型注入 Context 并进行一定的 Prompt Engineering。正确的 Prompt 可以激发出 LLM 的能力，这在 GPT-3.5 以前的时代更为重要。

将 Context 注入 LLM 实际上在 Prompt Engineering 的上游，把知识告诉 LLM，Prompt 只是中间桥梁。前 Stitch Fix 的 ML 总监 John McDonnell 画的这幅图很好地展示出了二者的关系：

![](https://img2023.cnblogs.com/blog/532548/202305/532548-20230530205341149-299446572.png)

## LLM模型的参数在训练阶段结束后就完全固定，只具备知识/逻辑推理能力，缺少对历史经验和知识的强记忆能力

基础大模型的能力来自于在训练阶段喂入的海量、丰富、多维度的训练语料，这让模型只能根据自己的”记忆“尝试进行推理，并且经常给出与事实相悖的答案。

基础LLM模型无法精确地”搜索“已经存在于历史数据库中的事实性信息，也无法从自己以往的生成中”提取记忆“。事实上，LLM模型每次的内容生成都是一次全新地从零开始的知识推理。这是 GPT-3 和 ChatGPT 刚刚出现时最初被体验的能力 —— 让 ChatGPT 写首诗，你可以接受它的上述不完美。

针对这个问题，embedding database（向量数据库）提供了一种良好的基础设施，我们需要将embedding database和LLM进行有机的结合，创造出一种新的LLM+embedding vector的新范式。

## LLM模型对输入token存在最大长度的限制

针对这个问题，Map Reduce 是目前业内比较主流的技术应对方向。

参考链接：

```
https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247501117&idx=1&sn=e860ac5e259a969f62b05d080bf42d14&chksm=ce9b7aa3f9ecf3b503656e9a09b55210fdba0844b54bd6a5714f5fc8c57b8c3570acbe2d342f&scene=21#wechat_redirect
```

![](https://img2023.cnblogs.com/blog/532548/202305/532548-20230530215112831-1689818082.png)

参考链接：

```
https://wallstreetcn.com/articles/3685072
https://www.geekpark.net/news/319478
https://www.infoq.cn/article/kxARbquFMCbx39KPoTxY
```

文章来源: https://www.cnblogs.com/LittleHann/p/17441900.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)