---
title: ChatGPT 能做什么，为什么它做到了
url: https://buaq.net/go-149555.html
source: unSafe.sh - 不安全
date: 2023-02-16
fetch_date: 2025-10-04T06:44:54.207596
---

# ChatGPT 能做什么，为什么它做到了

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

![]()

ChatGPT 能做什么，为什么它做到了

ChatGPT 能自动生成流畅合理的文本，看似出自人类之手，这一成就非同凡响。它是如何做到的？ Mathematica 作者 Stephen Wolfram 写了一篇长文分析背后的工作原理
*2023-2-15 20:45:24
Author: [www.solidot.org(查看原文)](/jump-149555.htm)
阅读量:21
收藏*

---

ChatGPT 能自动生成流畅合理的文本，看似出自人类之手，这一成就非同凡响。它是如何做到的？ Mathematica 作者 Stephen Wolfram 写了一篇长文分析背后的工作原理。从根本上说，ChatGPT 总是尝试从目前的文本产生“合理的延续”，所谓合理是指在用数十亿网页文本训练之后人们期望看到的文本。举个例子，对于“The best thing about AI is its ability to”这句话后面应该跟什么，你可以扫描数十亿页文本中寻找到频率最高的词。ChatGPT 的方法类似，但它不是看字面意义上的文本，而是寻找某种“意义匹配”，它会生成一组候选词，每个词都有不同的概率——The best thing about AI is its ability to learn(4.5%)/predict(3.5%)/make(3.2%)...依此类推。但 ChatGPT 并不总是选择概率最高的词，因为这样产生的文本可能并不让人感兴趣，太平淡，它有时候会随机挑选低概率的候选词，产生一篇更有趣的文章。这就是为什么我们多次用相同的提问词问 ChatGPT 它很可能会产生不同的文章。

https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

文章来源: https://www.solidot.org/story?sid=74143
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)