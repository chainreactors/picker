---
title: G.O.S.S.I.P 阅读推荐 2024-10-16 LLM帮你理解安全补丁
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499007&idx=1&sn=7d4018c268e37ef75faf6b91665e3db8&chksm=c063d226f7145b30cbbb7460d3ba18efd25e36ba49ab011cd3d41213c71ffc8731db2586fc08&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-17
fetch_date: 2025-10-06T18:52:14.310210
---

# G.O.S.S.I.P 阅读推荐 2024-10-16 LLM帮你理解安全补丁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EMj3mjib8oeUHevR4b44rToZja3TQYgjGiajyianr5U1QSxiaz0A15hXr5WSfNQQWvfJ5bGhyaiaKtIzg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-16 LLM帮你理解安全补丁

原创

G.O.S.S.I.P

安全研究GoSSIP

我们今天介绍的这篇论文*Pairing Security Advisories with Vulnerable Functions Using Open-Source LLMs*来自2024年的DIMVA会议，论文介绍的研究工作正是现在风头正劲的AI for Security中的一项具体的应用：利用LLM来帮助确定代码补丁中到底哪些函数直接和安全漏洞相关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rTodp5hIOGTuEWVsC8b4bnmfZ2aGM6O3GAYiaNnLQKpziaetFhHdVplhWKQ/640?wx_fmt=png&from=appmsg)

简单介绍一下研究背景：在软件代码安全分析里面，安全补丁（security patch）是一个非常有价值的对象，厂家只要发布了补丁，大家就知道肯定有安全漏洞被修复了，然后就赶紧去分析补丁，找到问题。但是这个过程是一个高度依赖人工介入的labour work，目前能够比较自动化的分析思路仅限于通过代码比对（比较patch前和patch后的代码），找到所有改动过的函数，然后把这些函数视为有问题的函数。但现实中并不是所有改动过的函数都是有安全问题的，实际上针对一些数据集的人工调查表明，在安全补丁涉及的所有改动过的代码中，大概只有五分之一是和安全问题相关的，其他的改动跟安全其实并没有关系。

听起来太抽象？先来看一个例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rTo2uWvQam5C8dPwX2K3TTTWCicoL1p4g3OUq7Lf8sKSg1R27q9Dt39YdA/640?wx_fmt=png&from=appmsg)

这个例子是CVE-2023-28105的安全报告（security advisory）的摘要，其中包含了对这个CVE安全漏洞的简要描述。虽然在这个报告中提到了与之对应的fix（就是https://github.com/dablelv/go-huge-util/commit/0e308b0 这个commit），你切不可认为这次代码更新只是修复了安全问题，整个fix一共修改了4个源代码文件，修改了5个已有函数，添加了2个函数，总共增加了104行新代码，同时删掉了45行旧代码。可是跟安全相关的函数并没有那么多（如下图所示）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rToLzG9aU8miaUtCVF0ibe9Jk8RyVqlWc6pibS67LY00ibbJrluEKtSz1fXrw/640?wx_fmt=png&from=appmsg)

针对上面观察到情况，本文就提出了一种利用LLM来对改动过的代码进行辅助标记的方法，作者认为这种方法能够更好地（当然也只是比现有的方法更好）找到那些真正涉及安全问题的函数。作者设计的方法的流程如下图所示（太丑了）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rTo1D8xdbXiaJfibJISia41v4q59bJTMQlYticTW9SfmCT7lF3EWIXAC4NJwQ/640?wx_fmt=png&from=appmsg)

这个流程里面，首先需要提供的是安全问题的描述（advisory description）以及代码的更改情况。在这里，作者用了一个叫做`function git-hunk`的输入形式，要了解它，首先我们复习一下git-hunk这个代表代码修改情况的技术概念：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rToF4XemiaGWlq9WNkXm1K0ia4ReQG7XHQzibmseicNOjdyzLc8DJCCLbX6vA/640?wx_fmt=png&from=appmsg)

而`function git-hunk`就是根据git-hunk的信息，把那些改动过的函数标记出来，把原来的粒度从代码块改成了函数。

在输入都准备好以后，接下就进入到了人工智能时代，疯狂使用提示词工程来向AI查询，下面就是作者设计并用来让AI 代替自己思考 大显神通的提示模板

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rToVJRL8AXa5lCsDiaQrsY1Aj6jMaPzPWiaggV0t1qIPL9QTYqH2q2vh1sQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rToBOWOKMENrMW3MYNibXibtIRqUWKFyW2sF53QFiaRKpRDnx2gPTblYF1Fg/640?wx_fmt=png&from=appmsg)

好吧，我们对这部分不熟悉，就照抄一遍给大家看看然后进入后续。这里面还有一个细节，就是在few-shot的情况下，作者还提供立了一个参考的数据库（里面包含了一些已经标记好的样例），通过函数相似性分析，搜索到一些相关的已有知识，给prompt提供参考（帮助LLM思考）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EMj3mjib8oeUHevR4b44rToCvvvE4QVxZz3fJ3dPI3RSwZK1BLXY2WMIVkrCibF84tpfbFWOL1q4hA/640?wx_fmt=png&from=appmsg)

论文的实验部分是那种非常无趣、列了一大堆数据表示自己比已有的技术进步了多少个百分点的 AI论文特色 风格，我们就不想介绍了。作者提供了相关的实验材料（用了4个开源的model，好像需要超过100G的空间），如果有读者去测试了，欢迎给我们反馈一下这个设计到底靠谱不靠谱：

> https://github.com/s3c2/llm-vulnerable-functions

---

> 论文：https://www.enck.org/pubs/dunlap-dimva24.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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