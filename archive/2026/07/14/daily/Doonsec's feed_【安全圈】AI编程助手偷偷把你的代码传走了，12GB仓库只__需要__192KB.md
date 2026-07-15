---
title: 【安全圈】AI编程助手偷偷把你的代码传走了，12GB仓库只\"需要\"192KB
url: https://mp.weixin.qq.com/s/ddhHqMMvzETki7gDIR7x4g
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:42:22.460277
---

# 【安全圈】AI编程助手偷偷把你的代码传走了，12GB仓库只\"需要\"192KB

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGsNmtcFdoibianyOBXcc2FNl1bDDvyjS95UvseF0nfV7x3VPgGzCWAOpOG95ycmvIsLQnia0wesDP3b5yJib51KDhPr4iacoTqbAuw/0?wx_fmt=jpeg)

# 【安全圈】AI编程助手偷偷把你的代码传走了，12GB仓库只"需要"192KB

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEFTMIOLLXEtnXBMfB9Ca4RFSUXy7OSRkgwp4gXPXvMbW6pR2YsKNthhAmFw7ibAzTicMBz75JmSyV5pOSwicqmRGFrwno0XHGj1A/640?wx_fmt=jpeg&from=appmsg)

你用AI编程助手写代码的时候，有没有想过一个问题：它到底把你的代码传到了哪里？

xAI推出的AI编程工具Grok Build，被发现存在一个惊人行为：当你让它处理一个代码文件时，它不仅读取了你需要的文件，还把整个Git仓库——包括全部提交历史、所有分支、所有文件——全部上传到了xAI的云端存储桶。

研究人员抓包发现：

* AI模型实际需要的数据：约192KB
* 实际上传到云端的数据：约5.10GB
* 差距：约27,800倍

更令人不安的是，这个上传走的是一条独立通道，和AI模型本身的通信完全分开。研究人员明确告诉AI不要打开某个文件，但这个文件还是被上传了。

存储桶的名字叫 grok-code-session-traces（"会话追踪"），这说明这可能不是bug，而是设计如此。

如果你的代码库里有商业机密、API密钥、提交历史……它们可能已经在别人手上了。

***END***

阅读推荐

[【安全圈】SpaceX 官方账号被黑！黑客发币圈诈骗，马斯克的"门面"都守不住？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077817&idx=1&sn=a7e600502d41b4d612a410a0ff2a4db9&scene=21#wechat_redirect)

[【安全圈】CVSS 满分！Joomla 两大插件被零日攻击，6月起已沦陷数千网站](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077817&idx=2&sn=d3699093e9aeb7929d0ab0216a911a04&scene=21#wechat_redirect)

[【安全圈】学术论文变成武器：黑客伪造真实研讨会资料，向研究人员投放 RokRAT](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077817&idx=3&sn=ca12b56a5d9434bfa32cebf100eb89a9&scene=21#wechat_redirect)

[【安全圈】勒索软件谈判顾问勾结黑客反向收割客户，被判近六年监禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077805&idx=1&sn=6b6595acfb0550598252fee7c782f905&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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