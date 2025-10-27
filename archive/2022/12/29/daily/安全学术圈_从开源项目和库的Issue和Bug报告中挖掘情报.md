---
title: 从开源项目和库的Issue和Bug报告中挖掘情报
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247488396&idx=1&sn=93b9a6e36d7b22eb0c7b5f712c618939&chksm=fe2eec07c95965116404ccdfff91e5b6f61b82dc37b96544bedb0b96ebb702d14a1ae6071f68&scene=58&subscene=0#rd
source: 安全学术圈
date: 2022-12-29
fetch_date: 2025-10-04T02:40:51.897814
---

# 从开源项目和库的Issue和Bug报告中挖掘情报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6Dibw6L070WGpCCmJowvrU1Z2RMlOiaLu6a5mB3XqZYvib12cPXPmlsrProQ84LMpTJDiaxv3Qtt3vlCAe1vUg2fIg/0?wx_fmt=jpeg)

# 从开源项目和库的Issue和Bug报告中挖掘情报

原创

JSY2019

安全学术圈

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFxb2EWWK8Fjz8olK6TTB3bjBjiabwoiacicib08WCLJqibNDMT3ba8YJwSwVolWbjoFQu7icX4m7wE6LwQ/640?wx_fmt=jpeg)

> *原文标题：Mining Threat Intelligence about Open-Source Projects and Libraries
> from Code Repository Issues and Bug Report*
> *原文作者：L Neil，S Mittal，A Joshi*
> *原文链接：https://ieeexplore.ieee.org/document/8587375*
> *发表会议：2018 IEEE International Conference on Intelligence and Security Informatics (ISI)*
> *笔记作者：JSY2019@SecQuan*
> *笔记小编：ourren@SecQuan*

## 研究背景和研究介绍

在如今，开源项目和开源库在越来越多的软件中被使用。在这样的三方软件生态下，产生了新的攻击方法，即黑客通过利用项目所关联的其他安全性较低的其他项目来达到攻击目的。

作者提到了其先前的工作，即CyberTwitter[1]和Cyber-All-Intel[2]，这些工作都是从OSINT中获取内容。

在该论文中，作者提出了一个提示开发者关于在开发项目中链接某开源软件或某开源库时可能的威胁和漏洞的系统。并开发了一个可追踪客户机安装软件的程序。

## 研究问题与结果

### 提出的核心问题

1. **威胁情报的获取：**从基于web的版本控制服务平台中获取社区中提出的issues和bugs等威胁情报知识。这些平台包括GitHub、GitLab、bitbucket等。
2. **安全知识图谱的构建：**使用提取的威胁情报知识建立包含不同开源项目漏洞信息的知识图谱。

### 所采用的方法

总体的系统架构如下图：![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGpCCmJowvrU1Z2RMlOiaLu6GOBW2qzyZ2LspGk0ckEe7ttEgHPwiaVtqWKw5k5yxRhANk5Yz6w2kicA/640?wx_fmt=png)

1. **威胁情报的获取**

在本文中，主要的威胁情报来源于GitHub社区的bug和issue报告。

流程图大致如下。![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGpCCmJowvrU1Z2RMlOiaLu66mKIXZpg0ib9hEjPYZ9R7k3r3QlMk0cW7w19BLr1b0v3f61qtTPBicRA/640?wx_fmt=png)

文中利用GitHub REST API来获取并追踪项目仓库的issues和pull申请。对于issues，作者通过[1]中提出的SVCE工具来标记issues中内含多于两个安全名词的情报。

2. **安全知识图谱的构建**

作者基于UCO[3]构建本体图；并构建了软件依赖本体图来表达已安装的软件和其依赖。

软件依赖本体图：![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGpCCmJowvrU1Z2RMlOiaLu6MNiaBSy63jXkCPdhSg6crLydtIpK7FiaRzwoO5vWaccQJjxfibQAAOItA/640?wx_fmt=png)

在获取知识后，作者通过URI关联将知识变为结点，通过DBpedia链接现实概念和不同图谱节点，最后储存为RDF三元组。

3. **警报系统的构建**最终，作者通过建立一个SQARQL endpoint来收取查询，通过加入SWRL规则来生成警报。

### 结果

作者在安装了包括预装程序在内的81个程序的Ubuntu Linux上测试成果，

作者收集了2018年1月以后的、关于这81个程序的110800个GitHub issue，经过SVCE处理后，余下9194个。最后放入了知识图谱。

作者抽取了150个随机issue来人工检查系统的准确度。其中，98个正确，18个完全错误，余下34个部分正确。

## 其他想法

对于最后的准确度（65.3%完全正确，88%非完全错误率），作者提到了被丢弃的issues、拼写错误、无法分辨的字母、不正规的词语用法和非英文的词汇等。

社区情报的准确度正是因为这些情况的影响而无法很高。另一个问题是，仅是81个程序就存在着十万以上的issue，在处理后也余下近万个。对于互联网上存在着的巨量开源程序，其issues的量也是巨大的。对于知识图谱的储存、查询的要求会很大，所遗漏的漏洞也可能会变得很多。

## 参考文献

[1] Mittal S ,  Das P K ,  Mulwad V , et al. CyberTwitter: using Twitter to generate alerts for cybersecurity threats and vulnerabilities[C]// Advances in Social Networks Analysis and Mining. IEEE Computer Society, 2016.

[2] Mittal S ,  Joshi A ,  Finin T . Cyber-All-Intel: An AI for Security related Threat Intelligence[J].  2019.

[3] Syed Z ,  Padia A ,  Finin T , et al. UCO: A Unified Cybersecurity Ontology[C]// AAAI Workshop on Artificial Intelligence for Cyber Security. 2016.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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