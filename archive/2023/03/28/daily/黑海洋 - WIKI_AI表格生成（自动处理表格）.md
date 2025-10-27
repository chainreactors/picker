---
title: AI表格生成（自动处理表格）
url: https://blog.upx8.com/3370
source: 黑海洋 - WIKI
date: 2023-03-28
fetch_date: 2025-10-04T10:53:19.645346
---

# AI表格生成（自动处理表格）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# AI表格生成（自动处理表格）

发布时间:
2023-03-27

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
42141

# 北大团队搞出ChatExcel，说人话自动处理表格

ChatExcel的原理一言以蔽之，就是直接把“大白话指令”转换成类似于VBA这样的程序语言，然后再执行程序。

底层基于Transformer架构，基本技术路线就是无监督训练+具体场景微调。

但NLP模型搞数学，一直都很容易出错，强大如ChatGPT都很难避免。

为此，团队在训练模型的过程中，将重点放在了**符号逻辑**上，期间还有意引入了一些逻辑符号的新知识。

由此我们也看到，它在计算上出错的概率并不高。

除了**数学能力**出众之外，ChatExcel最大的一个特点就是**持续交互**。

![](https://i.postimg.cc/xT94kX2c/image.png)

这是因为ChatExcel每次的生成结果，都是基于用户提出的新需求+上一轮生成的表格。对模型的理解力及运算其实提出了更高的要求。

为什么要实现这一功能？

团队介绍说，如Dall·E、ChatBCG等AI工具，完成任务的方式都是单次不持续的。但在人们的实际使用过程中，想法是一步步推进的。

ChatExcel团队表示的确有商业化的考虑，但会是To B层面的。

在线地址：
https://chatexcel.com/

[取消回复](https://blog.upx8.com/3370#respond-post-3370)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")