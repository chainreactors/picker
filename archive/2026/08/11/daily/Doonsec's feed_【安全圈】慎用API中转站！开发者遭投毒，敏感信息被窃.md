---
title: 【安全圈】慎用API中转站！开发者遭投毒，敏感信息被窃
url: https://mp.weixin.qq.com/s/D4kef7Rk0eMLXuZIHKL5aQ
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T03:59:50.158283
---

# 【安全圈】慎用API中转站！开发者遭投毒，敏感信息被窃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEvHn4tZhqhSjF4RUHzw3wwxHfn6WXHUIYcu6UCA7uHYgt1Bv2DhnvowoUrI3VNibCwgicNgK8GApDF1Xey0rwYL4bWJnObkcmMA/0?wx_fmt=jpeg)

# 【安全圈】慎用API中转站！开发者遭投毒，敏感信息被窃

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

API中转站

由于各种原因，很多用户可能会使用API中转站来调用AI模型。但使用API中转站也存在很大的风险，包括**信息泄露**和**恶意投毒**两大问题。

信息泄露指的是部分中转站会将真实用户的上下文数据打包卖给下游，用来训练模型或进行其他用途；恶意投毒则是在模型回复中插入恶意代码窃取信息。

## ⚠️ 事件经过

V2EX网友 @TheGuaGua 日前发帖称，自己在使用Codex中转站进行开发任务时，发现思维链中突然出现了奇怪的命令。网友立即暂停执行并开始检查，发现这是一段超长的Shell命令，其目的正是**窃取开发环境中的各类敏感数据并发送到黑客控制的服务器**。

值得注意的是，这应该不是中转站主动投毒。这家中转站早前刚发公告称遭遇了脚本注入攻击，但安全问题似乎并未彻底解决，仍有用户在使用时被投毒。

## 🔍 黑客窃取了哪些数据？

通过分析恶意代码，黑客收集的数据范围极其广泛，主要包括以下几个方面：

* **主机信息**

  ：hostname、用户名、系统版本等基础信息
* **环境变量**

  ：包含各类密钥和凭证的ENV文件
* **配置文件**

  ：YAML、YML等各类配置文件
* **认证目录**

  ：用于窃取API KEY的JSON文件
* **SSH私钥**

  ：~/.ssh/下的所有私钥和已知主机名单
* **云环境凭证**

  ：AWS、Azure、GCP等各类云平台凭证
* **包管理器凭证**

  ：npm、yarn、pip等包管理器的认证信息
* **Shell历史**

  ：~/.bash\_history和~/.zsh\_history的最近100条记录

## 🧪 恶意代码分析

从过滤关键词中可以看到，黑客重点关注AI/LLM相关工具的信息、开发者环境、云与容器和凭证集中存放位置。在获取到开发者关键凭证后，黑客还可以利用凭证继续展开攻击，形成危害更大的**供应链攻击**。

如果开发者开着无人值守+完全访问权限，那所有信息都会被黑客窃取。

## 🛡️ 紧急应对措施

如果你近期使用过VSLLM等中转站，建议：

* **立即轮换**

  开发环境中的所有令牌（Token）
* **彻底重建**

  开发环境以确保安全
* 如果本地开发环境中有各类云令牌，还要**提防供应链攻击**——黑客可能通过云令牌入侵云端环境并窃取数据

> 提醒：开发者在使用AI编程工具时，切勿开启"无人值守+完全访问权限"。务必在执行命令前仔细审查AI生成的命令内容，尤其是超长的Shell命令。

***END***

阅读推荐

[【安全圈】OpenAI紧急暂停！新AI模型竟会自学"黑客技术"](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=1&sn=cc5cca1ffdaf71baba9728066f84d777&scene=21#wechat_redirect)

[【安全圈】200万人身份告急！比利时电子身份证曝致命漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=2&sn=cdb595c396ed85c7d7cbec78a2e74951&scene=21#wechat_redirect)

[【安全圈】开发者小心！VS Code扩展暗中窃取加密钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=3&sn=27ac74789ce072180bb82f5b25e79d15&scene=21#wechat_redirect)

[【安全圈】服装品牌李维斯遭黑客攻击，部分企业数据被窃取](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078212&idx=1&sn=82c69a11c8cde7ebde9dbae49bcc8da3&scene=21#wechat_redirect)

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