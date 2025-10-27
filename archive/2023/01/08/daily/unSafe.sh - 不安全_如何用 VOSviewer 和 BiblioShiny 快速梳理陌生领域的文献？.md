---
title: 如何用 VOSviewer 和 BiblioShiny 快速梳理陌生领域的文献？
url: https://buaq.net/go-144568.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:48.577605
---

# 如何用 VOSviewer 和 BiblioShiny 快速梳理陌生领域的文献？

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

![](https://8aqnet.cdn.bcebos.com/35d7b1661b69c169c5108ac56185436e.jpg)

如何用 VOSviewer 和 BiblioShiny 快速梳理陌生领域的文献？

全场回放 | VOSviewer 和 BiblioShiny 使用技巧分享 付费栏目文章试读欢迎各位读者打开《经验卷轴：入门学术论文写作》栏目。《经验卷轴：入门学术论文写作》是一本知识点
*2023-1-7 16:59:14
Author: [sspai.com(查看原文)](/jump-144568.htm)
阅读量:49
收藏*

---

![](https://cdn-static.sspai.com/ui/img-placeholder.png)

全场回放 | VOSviewer 和 BiblioShiny 使用技巧分享

**付费栏目文章试读**

欢迎各位读者打开《经验卷轴：入门学术论文写作》栏目。《经验卷轴：入门学术论文写作》是一本**知识点覆盖全面的经验之书**。王老师将从零基础储备知识和选题开始，完整覆盖科研写作从选题、考察、知识储备到内容创作以及最终答辩的全流程，手把手带你完成长篇学术论文创作的全流程。

我们在直播回放视频的基础上，为各位整理了内容梗概和知识点，配合时间戳可在视频中直接找到相应内容。

如果你对内容有任何疑问或想法，欢迎在评论区中分享。

📮 前往了解[栏目](https://sspai.com/series/278)

## 直播回放

**本期主讲**：崔雷悦、王悦、王慧，天津师范大学管理学院图书情报专业研究生。

## 内容梗概

在本期直播中，三位同学为我们介绍了 VOSviewer 和 BiblioShiny 两款文献分析软件，演示了使用 VOSviewer 分析中、英文献作者关系与关键词共现以及使用 BiblioShiny 分析科研领域现状的具体流程，并回答了关于文献分析的一些问题。

## 知识点

### 为什么要使用文献分析工具？

在科研活动中，通常需要通过阅读文献了解某一个领域科研现状，或者需要查阅大量文献支撑想法和选题。如果通过个人的努力下载、阅读大量文献并从中筛选出重点，非常耗费时间和精力且困难的。

文献分析工具则可以帮助我们高效的将文献关系可视化，梳理出文献之间的引用关系、重要程度、作者对领域的贡献以及关键词组等重要信息，为接下来的科研活动提供支撑。

### **简介 VOSviewer 和 BiblioShiny**

VOSviewer 官网的描述是「一种用于构建和可视化文献计量网络的软件工具（a software tool for constructing and visualizing bibliometric networks）」。对文献的信息进行可视化的计量和分析，即通过分析文献中提及的关键词与引用的作者等信息，构建可视化的关系网络。

BiblioShiny 则是一款基于 R 语言 Bibliometrix 包的可视化分析工具，可以提供全面的科学测绘分析，通过文献信息生成词云、发展趋势图等图表。但它仅支持 Web of Science 等来源的外文文献分析，暂不支持中文文献。

### **VOSviewer 分析英文文献作者关系、关键词共现**

**📍 07:05 文献采集：**在 Web of Science 中，检索所需领域相关关键词，勾选所需文献，选择`导出 - 制表符分隔文件`，将`记录内容`修改为`全记录与引用的参考文献`，并导出。

![](https://cdn.sspai.com/2023/01/06/article/dd2ac79f16a39a77c1124e1d5f58ae69?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**📍 08:06 作者关系分析：**

![](https://cdn.sspai.com/2023/01/06/article/38e469d82221c06eecf9d8bcf4b82731?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/01/06/article/a894a6f3d2256f417b7b61526cc3b078?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/01/06/article/478e52758db765a0a0c7348542f3fd19?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/01/06/article/aee7fe8d5b13d64764132278ce59450e?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 在 VOSviewer 中点击左侧`Map - Create`新建地图；
2. 选择`Create a map based on bibliographic data`选项；
3. 选择包含 Web of Science 类型的`Read data from biliographic database files`选项；
4. 选择从 Web of Science 导出的文件；
5. 修改`Type of analysis`为`Co-authorship`，保持其他选项为默认；
6. 适当缩小阈值`Minimum number of documents of an author`；
7. 保持其他选项为默认。

**📍 09:13 关键词共现分析：**操作步骤与作者关系分析基本一致，仅步骤五、六略有区别。

![](https://cdn.sspai.com/2023/01/06/article/e69f99ac534d178fc1a5b5e71e530bf8?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/01/06/article/a1b3de51b6698af72ca06e1807bf0734?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 在 VOSviewer 中点击左侧`Map - Create`新建地图；
2. 选择`Create a map based on bibliographic data`选项；
3. 选择包含 Web of Science 类型的`Read data from biliographic database files`选项；
4. 选择从 Web of Science 导出的文件；
5. 修改`Type of analysis`为`Co-occurrence`，保持其他选项为默认；
6. 适当增大阈值`Minimum number of occurrence of a keyword`；
7. 保持其他选项为默认。

**📍 09:52 地图：**地图由节点以及之间的连线构成。节点大小反应涉及的关键文献数量，连线反映节点间的相互关系。联系紧密的节点连线多、距离近，不同主题的节点颜色不同。

### **VOSviewer 分析中文文献作者关系、关键词共现**

使用 VOSviewer 分析中文文献需要借助 EndNote 将知网导出的文献格式转换为可供 VOSviewer 分析的 RIS 格式，基本流程如下。

**📍 11:07 文献采集：**在中国知网中，检索所需领域相关关键词，勾选所需文献，选择`导出与分析 - 导出文献 - EndNote`，并导出。

**📍 13:45 格式转换：**

![](https://cdn.sspai.com/2023/01/06/article/28657de498d424ac5bb624a15d8fa50e?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/01/06/article/0a8271745c4fd2ee96651087c80595d6?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 在 EndNote 中，选择`Import`；
2. 打开从知网导出的文献，修改`Import Option`为`EndNote Import`，点击 `Import`；
3. 删除数据中没有作者信息的文献；
4. 全选文献，选择`Export`；
5. **修改文件后缀名为**`.ris`，保存类型为`Text File（*.txt）`，`Output Style`为`Refman(RIS) Export`，并保存。

**📍 17:00 作者关系分析：**

1. 在 VOSviewer 中点击左侧`Map - Create`新建地图；
2. 选择`Create a map based on bibliographic data`选项；
3. 选择包含 RIS 类型的`Read data from reference manager files`选项；
4. 选择从 EndNote 导出的文件；
5. 修改`Type of analysis`为`Co-authorship`，保持其他选项为默认；
6. 适当调节阈值`Minimum number of documents of an author`；
7. 保持其他选项为默认。

**📍 18:17 关键词共现分析：**操作步骤与作者关系分析基本一致，仅步骤五略有区别。

1. 在 VOSviewer 中点击左侧`Map - Create`新建地图；
2. 选择`Create a map based on bibliographic data`选项；
3. 选择包含 RIS 类型的`Read data from reference manager files`选项；
4. 选择从 EndNote 导出的文件；
5. 修改`Type of analysis`为`Co-occurrence`，保持其他选项为默认；
6. 适当调节阈值`Minimum number of occurrence of a keyword`；
7. 保持其他选项为默认。

**📍 18:55 地图：**地图的组成与含义与英文文献一致。

### **BiblioShiny 分析科研领域现状**

**📍 20:10 文献采集：**在 Web of Science 中，检索所需期刊，筛选`高被引论文`，勾选所需文献，选择`导出 - BibTex`，将`记录内容`修改为`全记录与引用的参考文献`，并导出。如果所需文献数量较大，可以分多次导出后放置在同一压缩包内。

![](https://cdn.sspai.com/2023/01/06/article/f99be4e90a9600a3df593bf8d3a1c802?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**📍 22:52 启动 BibilioShiny：需要提前安装 R Studio 与 Bibiliometrix 包。**

![](https://cdn.sspai.com/2023/01/06/article/02352064f6f3a95a926789605b14b4d2?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

```
library(bibliometrix)    // 读取 Bibiliometrix 包
biblioshiny              // 启动 Bibilioshiny
```

**📍 23:57 加载数据：**

![](https://cdn.sspai.com/2023/01/06/article/9e47278ef4965f9f8a189f620e6fda03?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 点击左侧`Data - Load Data`；
2. 修改`Please, choose what to do`为`Import raw file(s)`，修改`Database`为`Web of Science (WoS/WoK)`，选择从 Web of Science 导出的文件，点击`Start`；

**📍 25:08 BiblioShiny 功能简介：**BiblioShiny 可以分析导入文献的作者、文档、概念结构、知识结构、社会网络等内容。科研活动中，最受关注的问题有：领域中哪些作者具有一定权威；领域中哪些文献更受关注；领域中哪些主题受重视且具有较好的发展趋势。BiblioShiny 则可以通过对数据的可视化分析帮助我们找到这些问题的答案。

**📍 29:25 分析高产作者：**

![](https://cdn.sspai.com/2023/01/06/article/6a17badabb252340db57bac1903c16f8?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 点击左侧`Authors - Most Relevant Authors`；
2. 点击`Run`进行分析；
3. 分析结束后，右侧可以调节作者数量等变量；中间的图表则展示了分析的结果。图表纵轴是作者，横轴是发文数量。

**📍 30:29 分析受关注文献：**

![](https://cdn.sspai.com/2023/01/06/article/b36486762f7ae8cb81df0e3f261b6dc1?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 点击左侧`Intellectual Structure - Historiograph`；
2. 点击`Run`进行分析；
3. 分析结束后，右侧可以调节节点数量等变量；中间的图表则展示了分析的结果。
4. 图表纵轴是被引次数，横轴是发文时间，每个节点代表一篇文献。LCS 表征了文献在平台的总被引次数；GCS 表征了文献在当前数据集中的被引次数。

**📍 32:44 分析词云：**

![](https://cdn.sspai.com/2023/01/06/article/7f28a8ad38f3f536bf145c71dc1d738a?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 点击左侧 `Documents - Word - WordCloud`；
2. 点击`Run`进行分析；
3. 分析结束后，右侧可以调节关键词来源、数量等变量。中间的图表则展示了分析的结果。单词的大小表征了出现次数。

**📍 33:55 分析主题：**

![](https://cdn.sspai.com/2023/01/06/article/a4910af45a6489967698568d1ed1afc8?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 点击左侧 `Conceptual Structure - Network Approach - Thematic Map`；
2. 点击`Run`进行分析；
3. 分析结束后，右侧可以调节关键词来源等变量；中间的图表则展示了分析的结果。

图表纵轴是主题发展趋势，横轴是主题重要程度。图表被坐标划分为四个象限：位于第一象限的主题一般重要度高，发展态势好；位于第一象限的主题一般重要度弱，但发展态势好；位于第三象限的主题一般重要度弱，发展态势差，可能是新兴或即将衰落的主题；位于第一象限的主题一般重要度高，发展态势差。通过观察主题在图表中的位置，可以指导科研活动中研究方向与选题的选择。

## 问答环节

### 如何关注系列的讲座直播信息？

本期直播是《经验卷轴：入门学术论文写作》的专享直播，订阅栏目后，可以通过栏目文章和少数派站内系统通知收到直播预告。

### **BiblioShiny 可以分析知网文献吗？**

BiblioShiny 现在只支持对外文献的一些数据的分析，关于 CNKI 是否可以通过一些其他的中间的中介工具对转化后导入 BiblioShiny，可以在研究后与大家再做讨论。

### 如何通过 **BiblioShiny** 找到两三年内比较重要的文章？

建议先找到想要研究领域的权威期刊，按需要的时间范围筛选期刊文献，然后导入 BiblioShiny 进行分析。

### 如何通过 **BiblioShiny 分析多本期刊**？

把从 Web of Science 导出的文件放在同一个压缩包内。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [B 站账号](https://space.bilibili.com/176321970)，找到数字时代更好的生活方式 🎊

> 往期精彩、[2021 年度回顾](https://sspai.com/page/2021/movie)，更多影视推荐尽在 [#本周看什么](https://sspai.com/tag/%E6%9C%AC%E5%91%A8%E7%9C%8B%E4%BB%80%E4%B9%88) 🎬

[![数字工具组](https://cdn-static.sspai.com/ui/im...